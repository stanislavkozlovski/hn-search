import copy
import importlib.metadata
import importlib.util
import io
import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest.mock import patch

from hn_search.__main__ import main
from hn_search.catalog import commit_page, open_catalog
from hn_search.clickhouse import Post
from tests.research_helpers import ArchiveFixture, FakeClient, NOW, snapshot


ROOT = Path(__file__).resolve().parents[1]


class ResearchUsageTests(unittest.TestCase):
    def test_collect_does_not_import_the_client_and_missing_catalog_stays_missing(self):
        code = "import sys; import hn_search.__main__; assert 'stan_ai_client' not in sys.modules"
        subprocess.run([sys.executable, "-c", code], cwd=ROOT, check=True)
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.sqlite3"
            for args in (["--db", str(missing), "research"], ["collect"], ["archive", "1"]):
                with self.subTest(args=args), redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised:
                    main(args)
                self.assertEqual(raised.exception.code, 2)
            self.assertFalse(missing.exists())

    def test_missing_or_wrong_client_is_a_usage_error_before_any_new_files(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "catalog.db"
            open_catalog(db).close()
            for value in ("0.1.18", importlib.metadata.PackageNotFoundError("stan-ai-client")):
                manager = patch("importlib.metadata.version", side_effect=value) if isinstance(value, Exception) else patch(
                    "importlib.metadata.version", return_value=value)
                with manager, redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised:
                    main(["--db", str(db), "research", "--out", str(Path(directory) / "out")])
                self.assertEqual(raised.exception.code, 2)
            self.assertFalse((Path(directory) / "out").exists())


@unittest.skipUnless(importlib.util.find_spec("stan_ai_client"), "optional stan-ai-client is absent")
class PipelineTests(unittest.TestCase):
    def setUp(self):
        from hn_search.research import store

        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.conn = open_catalog(self.root / "catalog.db")
        self.addCleanup(self.conn.close)
        store.migrate(self.conn)
        commit_page(self.conn, [Post(sid, f"Renting story {sid}", "", "", 1, 5) for sid in range(1, 9)])
        self.client = FakeClient()
        self.archive = ArchiveFixture()
        self.stream = io.StringIO()
        runtime = patch("hn_search.research.ai.resolve_codex_runtime", return_value=Path("/native/codex"))
        runtime.start()
        self.addCleanup(runtime.stop)

    def run_pipeline(self, replies=None):
        from hn_search.research.pipeline import run_research

        scripted = iter(replies or ["looks good", "Is buying a home better than renting?", "go", "proceed"])
        return run_research(self.conn, self.root / "out", client=self.client, archive_story=self.archive,
                            ask=lambda prompt: next(scripted), stream=self.stream, clock=lambda: NOW)

    def test_all_downloads_precede_classification_folders_coverage_and_exact_reuse(self):
        def assert_downloaded(call):
            if call.name == "description":
                self.assertEqual(self.archive.calls, list(range(1, 9)))
        self.client.before_call = assert_downloaded
        report = self.run_pipeline()
        text = report.read_text()
        for sid in (1, 4, 6):
            self.assertTrue((report.parent / "stories" / str(sid) / "thread.json").is_file())
            self.assertTrue((report.parent / "stories" / str(sid) / "analysis.md").is_file())
            self.assertIn(f"[[./stories/{sid}/analysis|", text)
        for sid in (2, 3, 5, 7, 8):
            self.assertFalse((report.parent / "stories" / str(sid)).exists())
            self.assertIn(f"https://news.ycombinator.com/item?id={sid}", text)
        self.assertIn("test network down", text)
        self.assertIn("HN returned a null root", text)
        self.assertIn("Reason for 2", text)
        self.client.before_call = None
        self.client.calls.clear()
        self.stream.seek(0)
        self.stream.truncate()
        self.run_pipeline()
        self.assertEqual([call.name for call in self.client.calls], ["settings", "keywords", "keywords", "keywords"])
        self.assertIn("(6 stories reused)", self.stream.getvalue())
        self.assertEqual(self.conn.execute("SELECT count(*) FROM research_runs WHERE finished_at IS NOT NULL").fetchone()[0], 2)

    def test_edit_plus_approval_requires_display_and_a_revised_gate(self):
        from hn_search.research.ai import DEFAULT_SETTINGS

        changed = copy.deepcopy(DEFAULT_SETTINGS)
        changed["classification"]["model"] = "gpt-6-astra"
        self.client.settings_replies = [{"approved": True, **changed, "note": ""},
                                       {"approved": True, **changed, "note": ""}]
        question = "Is buying a home better than renting?"
        self.client.keyword_replies = [
            {"approved": False, "question": question, "keywords": ["renting"], "note": ""},
            {"approved": True, "question": question, "keywords": ["renting"], "note": ""},
            {"approved": True, "question": question + " in Europe?", "keywords": ["renting", "mortgage"], "note": ""},
            {"approved": True, "question": question + " in Europe?", "keywords": ["renting", "mortgage"], "note": ""},
            {"approved": True, "question": question + " in Europe?", "keywords": ["renting", "mortgage"], "note": ""},
        ]
        self.run_pipeline(["use Astra for classification and go", "looks good", question, "go",
                           "focus on Europe and add mortgage, go", "approve", "proceed"])
        self.assertEqual(self.stream.getvalue().count("Top matches by reported comments:"), 2)
        self.assertIn("classification   gpt-6-astra", self.stream.getvalue())
        self.assertIn("in Europe?", self.stream.getvalue())
        settings_calls = [call for call in self.client.calls if call.name == "settings"]
        self.assertTrue(all(call.options.model == "gpt-6-luna" and call.options.reasoning_effort == "medium"
                            for call in settings_calls))
        self.assertTrue(all("in Europe?" in call.prompt for call in self.client.calls if call.name == "verdict"))

    def test_split_story_combines_all_parts_and_keeps_their_citations(self):
        self.archive.large = True
        windows = {"gpt-6-luna": 2400, "gpt-6-astra": 2400, "gpt-6.1-sol": 2400}
        with patch.dict("hn_search.research.ai.CONTEXT_WINDOWS", windows):
            report = self.run_pipeline()
        analysis = (report.parent / "stories" / "4" / "analysis.md").read_text()
        rows = self.conn.execute("SELECT part FROM ai_results WHERE stage = 'analysis' AND story_id = 4 ORDER BY part").fetchall()
        self.assertGreater(len(rows), 1)
        for (part,) in rows:
            self.assertIn(f"Part {part} evidence", analysis)
        self.assertIn("[[./thread#^c", analysis)
        self.assertLess(analysis.index("## Part 1"), analysis.index("## Part 2"))

    def test_one_bad_reply_discards_the_entire_call_and_keeps_earlier_calls(self):
        def corrupt(name, output):
            if name == "verdict":
                output["stories"][-1]["comment_ids"] = [999999999]
            return output
        self.client.transform = corrupt
        with redirect_stderr(io.StringIO()), self.assertRaisesRegex(ValueError, "999999999"):
            self.run_pipeline()
        self.assertEqual(self.conn.execute("SELECT count(*) FROM ai_results WHERE stage = 'verdict'").fetchone()[0], 0)
        self.assertEqual(self.conn.execute("SELECT count(*) FROM ai_results WHERE stage = 'description'").fetchone()[0], 6)
        self.assertEqual(self.conn.execute(
            "SELECT count(*) FROM research_run_stories WHERE status = 'matched'").fetchone()[0], 6)

    def test_descriptions_reuse_across_questions_but_judgments_and_analyses_do_not(self):
        self.run_pipeline()
        self.client.calls.clear()
        self.run_pipeline(["looks good", "Is renting better in Europe?", "go", "proceed"])
        names = [call.name for call in self.client.calls]
        self.assertNotIn("description", names)
        self.assertIn("verdict", names)
        self.assertIn("analysis", names)
        self.assertIn("synthesis", names)

    def test_no_relevant_story_skips_analysis_and_synthesis_and_keeps_coverage(self):
        def irrelevant(name, output):
            if name == "verdict":
                for item in output["stories"]:
                    item["verdict"], item["comment_ids"] = "irrelevant", []
            return output
        self.client.transform = irrelevant
        report = self.run_pipeline()
        self.assertNotIn("## Thread index", report.read_text())
        self.assertIn("Matched: 8 · relevant: 0", report.read_text())
        self.assertFalse(any(call.name in ("analysis", "synthesis", "folder_synthesis") for call in self.client.calls))

    def test_second_failed_verdict_call_preserves_only_prior_call_results(self):
        commit_page(self.conn, [Post(sid, f"Renting story {sid}", "", "", 1, 5) for sid in range(9, 24)])
        self.archive.failures = False
        count = 0
        def fail(call):
            nonlocal count
            if call.name == "verdict":
                count += 1
            return call.name == "verdict" and count == 2
        self.client.fail = fail
        error = io.StringIO()
        with redirect_stderr(error), self.assertRaisesRegex(RuntimeError, "test client failure"):
            self.run_pipeline()
        self.assertEqual(self.conn.execute("SELECT count(*) FROM ai_results WHERE stage = 'verdict'").fetchone()[0], 20)
        self.assertEqual(self.conn.execute("SELECT count(*) FROM research_runs WHERE finished_at IS NOT NULL").fetchone()[0], 0)
        self.assertIn("verdict call 2/2 failed for", error.getvalue())

    def test_ai_failure_stays_below_the_shared_terminal_checklist(self):
        class Terminal(io.StringIO):
            def isatty(self):
                return True

        self.stream = Terminal()
        self.client.fail = lambda call: call.name == "verdict"
        with redirect_stderr(self.stream), self.assertRaisesRegex(RuntimeError, "test client failure"):
            self.run_pipeline()
        diagnostic = "research: verdict call 1/1 failed for 1, 2, 3, 4, 5, 6"
        output = self.stream.getvalue()
        self.assertEqual(output.count(diagnostic), 1)
        final_frame = output.rsplit("\x1b[J", 1)[-1].splitlines()
        self.assertEqual(final_frame[-1], diagnostic)
        self.assertEqual(len(final_frame), 6)
        for line, stage in zip(final_frame[:-1], ("search", "download", "classify", "analyze", "report")):
            self.assertRegex(line, rf"^[✓·] {stage}\b")
        # Clearing after this line would erase it on the shared screen.
        self.assertNotIn("\x1b[J", output[output.index(diagnostic):])

    def test_sqlite_and_interrupt_download_failures_propagate(self):
        for error in (sqlite3.OperationalError("locked"), KeyboardInterrupt()):
            def fail(*args):
                raise error
            self.archive = fail
            with self.subTest(error=type(error)), self.assertRaises(type(error)):
                self.run_pipeline()

    def test_existing_next_folder_exits_two_before_any_ai(self):
        (self.root / "out" / "run-1").mkdir(parents=True)
        self.conn.commit()
        with patch("stan_ai_client.CodexClient") as client, redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised:
            main(["--db", str(self.root / "catalog.db"), "research", "--out", str(self.root / "out")])
        self.assertEqual(raised.exception.code, 2)
        client.assert_not_called()

    def test_synthesis_boundary_uses_one_call_or_one_folder_session(self):
        from hn_search.research.ai import ANALYSIS_FIELDS, DEFAULT_SETTINGS
        from hn_search.research.pipeline import _synthesis_prompt, _synthesize
        from hn_search.research.progress import Progress
        from hn_search.research.threads import estimate_tokens

        stories = [{"snapshot": snapshot(), "descriptions": [{"description": "Housing", "tags": []}],
                    "analyses": [{field: ["Evidence [c1001]"] for field in ANALYSIS_FIELDS}], "row_ids": [10]}]
        prompt, _ = _synthesis_prompt("Q", stories)
        size = estimate_tokens(prompt)
        cwd, folder = self.root / "cwd", self.root / "run"
        cwd.mkdir()
        folder.mkdir()
        progress = Progress(self.stream, lambda: NOW)
        with patch("hn_search.research.pipeline.input_limit", return_value=size):
            _synthesize(self.conn, 1, "Q", DEFAULT_SETTINGS, stories, self.client, cwd, folder, progress, lambda: NOW)
        self.assertEqual(self.client.calls[-1].name, "synthesis")
        self.assertEqual(self.client.calls[-1].options.cwd, cwd)
        with patch("hn_search.research.pipeline.input_limit", return_value=size - 1):
            _synthesize(self.conn, 1, "Q", DEFAULT_SETTINGS, stories, self.client, cwd, folder, progress, lambda: NOW)
        self.assertEqual(self.client.calls[-1].name, "folder_synthesis")
        self.assertEqual(self.client.calls[-1].options.cwd, folder)
        calls = len(self.client.calls)
        self.assertIsNone(_synthesize(self.conn, 1, "Q", DEFAULT_SETTINGS, [], self.client, cwd, folder, progress, lambda: NOW))
        self.assertEqual(len(self.client.calls), calls)
