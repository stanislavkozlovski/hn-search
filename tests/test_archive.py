from concurrent.futures import ALL_COMPLETED, ThreadPoolExecutor, wait as wait_for_all
from contextlib import closing, redirect_stderr, redirect_stdout
from io import StringIO
import json
import os
from pathlib import Path
import select
import sqlite3
import subprocess
import sys
import tempfile
from threading import Barrier, Event, Lock, get_ident
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

from hn_search.__main__ import main
from hn_search.archive import UncataloguedStories, archive, archive_story
from hn_search.catalog import commit_page, migrate_archives, open_catalog
from tests.helpers import HNOpener, NOW, post, start_history


ROOT = Path(__file__).resolve().parents[1]
TREE = {
    4517440: {"id": 4517440, "type": "story", "title": "Rent vs. buy", "descendants": 5, "kids": [4517521, 4520037]},
    4517521: {"id": 4517521, "type": "comment", "by": "Daisy", "parent": 4517440, "kids": [4517587, 4517797]},
    4520037: {"id": 4520037, "type": "comment", "by": "Evbn", "parent": 4517440},
    4517587: {"id": 4517587, "type": "comment", "by": "DamnYuppie", "parent": 4517521},
    4517797: {"id": 4517797, "type": "comment", "by": "pc86", "parent": 4517521, "kids": [4517878]},
    4517878: {"id": 4517878, "type": "comment", "by": "malyk", "parent": 4517797},
}


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "catalog.sqlite3"
        self.exports = Path(self.directory.name) / "exports"
        self.conn = open_catalog(self.path)
        self.addCleanup(lambda: self.conn.close())
        self.output = StringIO()
        self.stdout = redirect_stdout(self.output)
        self.stdout.__enter__()
        self.addCleanup(self.stdout.__exit__, None, None, None)

    def add_roots(self, *roots):
        commit_page(self.conn, [post(root) for root in roots])

    def reopen(self):
        self.conn.close()
        self.conn = open_catalog(self.path)

    def run_archive(self, roots, opener, *, now=NOW):
        return archive(self.conn, roots, self.exports, opener=opener, clock=lambda: now)

    def payload(self, root):
        return json.loads((self.exports / f"{root}.json").read_text())

    def test_exact_tree_failure_reopen_resume_and_zero_request_reuse(self):
        self.add_roots(4517440)
        start_history(self.conn, next_id=123)
        first = HNOpener(TREE | {4517797: TimeoutError("timed out")})
        with self.assertRaises(TimeoutError):
            self.run_archive([4517440], first)
        self.assertEqual(first.requests, [4517440, 4517521, 4520037, 4517587, 4517797])
        self.assertEqual(first.timeouts, [30] * 5)
        self.assertIn("status=incomplete comments=3 pending=1", self.output.getvalue())
        self.assertFalse(self.exports.exists())
        self.reopen()
        second = HNOpener(TREE)
        self.run_archive([4517440], second, now=NOW + 10)
        self.assertEqual(second.requests, [4517797, 4517878])
        payload = self.payload(4517440)
        self.assertEqual((payload["comments"], payload["saved_items"], payload["unavailable"]), (5, 6, 0))
        self.assertEqual((payload["started_at"], payload["finished_at"]), (NOW, NOW + 10))
        self.assertEqual(payload["root"]["retrieved_at"], NOW)
        self.assertEqual(payload["root"]["replies"][0]["replies"][1]["retrieved_at"], NOW + 10)
        self.assertEqual(self.conn.execute("SELECT * FROM collection_progress").fetchall(), [(123, 0, 100)])
        original = (self.exports / "4517440.json").read_bytes()
        (self.exports / "4517440.md").unlink()
        commit_page(self.conn, [post(4517440, title="Catalog was refreshed", descendants=100)])
        third = HNOpener()
        self.run_archive([4517440, 4517440], third, now=NOW + 10_000_000)
        self.assertEqual(third.requests, [])
        self.assertEqual((self.exports / "4517440.json").read_bytes(), original)
        self.assertIn("reused=true", self.output.getvalue())
        self.assertIn("Rent vs", (self.exports / "4517440.md").read_text())
        self.assertNotIn("Catalog was refreshed", (self.exports / "4517440.md").read_text())

    def test_first_run_uses_breadth_first_order_and_deduplicates_roots(self):
        self.add_roots(4517440)
        opener = HNOpener(TREE)
        self.run_archive([4517440, 4517440], opener)
        self.assertEqual(opener.requests, [4517440, 4517521, 4520037, 4517587, 4517797, 4517878])
        self.assertEqual(len(self.output.getvalue().splitlines()), 1)

    def test_admission_reports_every_missing_id_before_migration_or_requests(self):
        self.add_roots(1)
        opener = HNOpener()
        with self.assertRaises(UncataloguedStories) as raised:
            self.run_archive([1, 99, 99, 88], opener)
        self.assertEqual(raised.exception.roots, [99, 88])
        self.assertEqual(opener.requests, [])
        self.assertEqual(self.conn.execute("PRAGMA user_version").fetchone()[0], 1)
        self.assertEqual(self.conn.execute("SELECT name FROM sqlite_master WHERE name LIKE 'archive%'").fetchall(), [])
        self.assertFalse(self.exports.exists())

    def test_null_root_and_omitted_optional_fields_complete_without_retries(self):
        self.add_roots(1, 2)
        opener = HNOpener({1: None, 2: {"id": 2, "extra": {"future": [True, 1, "雪"]}}})
        self.run_archive([1, 2], opener)
        first, second = self.payload(1), self.payload(2)
        self.assertIsNone(first["root"]["item"])
        self.assertEqual((first["comments"], first["unavailable"], first["saved_items"]), (0, 1, 1))
        self.assertIsNone(first["reported_descendants"])
        self.assertEqual(second["root"]["item"]["extra"], {"future": [True, 1, "雪"]})
        self.assertIn("[unavailable]", (self.exports / "1.md").read_text())

    def test_flags_nulls_polls_unknown_fields_and_cyclic_children_preserve_evidence(self):
        self.add_roots(1)
        records = {
            1: {"id": 1, "type": "poll", "title": "Question?", "kids": [2, 2, 3], "parts": [5, 6, 5], "descendants": 999},
            2: {"id": 2, "deleted": True, "parent": 1, "kids": [4, 1]},
            3: None,
            4: {"id": 4, "dead": True, "by": "雪", "text": "[flagged]", "kids": [2], "unknown": {"a": [1, "<b>x</b>"]}},
            5: {"id": 5, "type": "pollopt", "text": "Option &amp; one", "score": 73, "poll": 1},
            6: None,
        }
        opener = HNOpener(records)
        self.run_archive([1], opener)
        self.assertEqual(opener.requests, [1, 2, 3, 5, 6, 4])
        self.assertEqual(set(opener.requests), set(records))
        saved = {row[0]: json.loads(row[1]) for row in self.conn.execute("SELECT item_id, item_json FROM archive_items")}
        self.assertEqual(saved, records)
        payload = self.payload(1)
        self.assertEqual((payload["comments"], payload["unavailable"], payload["saved_items"]), (2, 2, 6))
        self.assertEqual(payload["reported_descendants"], 999)
        self.assertEqual([node["id"] for node in payload["poll_options"]], [5, 6])
        self.assertEqual([node["id"] for node in payload["root"]["replies"]], [2, 3])
        self.assertEqual(payload["root"]["replies"][0]["replies"][0]["item"], records[4])
        markdown = (self.exports / "1.md").read_text()
        for marker in ("[deleted]", "[flagged]", "[unavailable]", "votes: 73", "^c2", "^c3", "^c4"):
            self.assertIn(marker, markdown)

    def test_dead_root_with_negative_descendants_completes_and_preserves_evidence(self):
        self.add_roots(1)
        records = {
            1: {"id": 1, "type": "story", "dead": True, "descendants": -1, "kids": [2]},
            2: {"id": 2, "type": "comment", "parent": 1, "text": "Saved reply"},
        }
        opener = HNOpener(records)
        self.run_archive([1], opener)
        self.assertEqual(opener.requests, [1, 2])
        saved = {row[0]: json.loads(row[1]) for row in self.conn.execute("SELECT item_id, item_json FROM archive_items")}
        self.assertEqual(saved, records)
        payload = self.payload(1)
        self.assertEqual(payload["status"], "complete")
        self.assertEqual(payload["reported_descendants"], -1)
        self.assertEqual(payload["root"]["item"], records[1])
        self.assertEqual(payload["root"]["replies"][0]["item"], records[2])
        self.assertIn("reported_descendants=-1", self.output.getvalue())
        self.assertIn("Reported comments: -1", (self.exports / "1.md").read_text())

    def test_invalid_payloads_never_become_checkpoints(self):
        self.add_roots(1)
        invalid = [[], 1, "text", {}, {"id": True}, {"id": 2}, {"id": 1, "kids": None},
                   {"id": 1, "kids": [True]}, {"id": 1, "kids": [0]}, {"id": 1, "parts": ["2"]},
                   {"id": 1, "by": None}, {"id": 1, "text": []}, {"id": 1, "title": 4},
                   {"id": 1, "url": False}, {"id": 1, "type": []}, {"id": 1, "parent": 0},
                   {"id": 1, "time": -1}, {"id": 1, "descendants": True}, {"id": 1, "score": "4"},
                   {"id": 1, "dead": 1}, {"id": 1, "deleted": "true"}, b'{', b'{"id":1,"extra":NaN}',
                   b'{"id":1,"extra":1e999}', b'\xff']
        for payload in invalid:
            with self.subTest(payload=payload), self.assertRaises((ValueError, UnicodeError)):
                self.run_archive([1], HNOpener({1: payload}))
            self.assertEqual(self.conn.execute("SELECT * FROM archive_items").fetchall(), [])
            self.assertEqual(self.conn.execute("SELECT status FROM archives").fetchone()[0], "incomplete")

    def test_request_failures_keep_original_exception_class_without_retry(self):
        self.add_roots(1)
        failures = [TimeoutError("timeout"), URLError("offline"), HTTPError("https://example.com", 429, "slow down", {}, None)]
        for error in failures:
            opener = HNOpener({1: error})
            with self.subTest(error=error), self.assertRaises(type(error)) as raised:
                self.run_archive([1], opener)
            self.assertIs(raised.exception, error)
            self.assertEqual(opener.requests, [1])
            self.assertIn("archive root=1 item=1", error.__notes__)

    def test_item_write_failure_retains_earlier_commits_and_resumes_only_missing(self):
        self.add_roots(1)
        migrate_archives(self.conn)
        with self.conn:
            self.conn.execute("""CREATE TRIGGER fail_item BEFORE INSERT ON archive_items WHEN NEW.item_id = 2
                BEGIN SELECT RAISE(ABORT, 'item write failed'); END""")
        opener = HNOpener({1: {"id": 1, "kids": [2]}, 2: {"id": 2}})
        with self.assertRaises(sqlite3.IntegrityError):
            self.run_archive([1], opener)
        self.reopen()
        self.assertEqual(self.conn.execute("SELECT item_id FROM archive_items").fetchall(), [(1,)])
        with self.conn:
            self.conn.execute("DROP TRIGGER fail_item")
        second = HNOpener({2: {"id": 2}})
        self.run_archive([1], second)
        self.assertEqual(second.requests, [2])

    def test_completion_write_failure_can_finish_without_any_refetch(self):
        self.add_roots(1)
        migrate_archives(self.conn)
        with self.conn:
            self.conn.execute("""CREATE TRIGGER fail_completion BEFORE UPDATE ON archives
                BEGIN SELECT RAISE(ABORT, 'completion failed'); END""")
        with self.assertRaises(sqlite3.IntegrityError):
            self.run_archive([1], HNOpener({1: {"id": 1}}))
        self.assertIn("status=incomplete comments=0 pending=0", self.output.getvalue())
        self.reopen()
        with self.conn:
            self.conn.execute("DROP TRIGGER fail_completion")
        self.run_archive([1], HNOpener())
        self.assertEqual(self.payload(1)["status"], "complete")

    def test_batch_failure_drains_successes_without_admitting_ninth_root(self):
        self.add_roots(*range(1, 11))
        barrier = Barrier(8)
        lock = Lock()
        running = set()
        max_running = 0
        sqlite_threads = []
        self.conn.set_trace_callback(lambda sql: sqlite_threads.append(get_ident()))

        def response(root):
            def fetch():
                nonlocal max_running
                with lock:
                    self.assertNotIn(root, running)
                    running.add(root)
                    max_running = max(max_running, len(running))
                barrier.wait(timeout=5)
                with lock:
                    running.remove(root)
                if root == 1:
                    raise URLError("stop batch")
                return {"id": root, "kids": [30]} if root == 3 else {"id": root}
            return fetch

        opener = HNOpener({root: response(root) for root in range(1, 9)})
        with patch("hn_search.archive.wait", side_effect=lambda futures, **kwargs: wait_for_all(futures, return_when=ALL_COMPLETED)):
            with self.assertRaises(URLError):
                self.run_archive(range(1, 11), opener)
        self.assertEqual(max_running, 8)
        self.assertEqual(set(sqlite_threads), {get_ident()})
        self.assertEqual(set(opener.requests), set(range(1, 9)))
        statuses = dict(self.conn.execute("SELECT root_id, status FROM archives"))
        self.assertEqual(set(statuses), set(range(1, 9)))
        self.assertEqual(statuses[1], "incomplete")
        self.assertEqual(statuses[3], "incomplete")
        for root in (2, 4, 5, 6, 7, 8):
            self.assertEqual(statuses[root], "complete")
            self.assertTrue((self.exports / f"{root}.md").exists())
        self.assertEqual(self.conn.execute("SELECT item_id FROM archive_items WHERE root_id=3").fetchall(), [(3,)])
        self.assertIn("root=1 status=incomplete comments=0 pending=1", self.output.getvalue())
        self.assertIn("root=3 status=incomplete comments=0 pending=1", self.output.getvalue())

    def test_more_than_eight_roots_and_each_child_starts_after_parent_commit(self):
        self.add_roots(*range(1, 13))
        barrier = Barrier(8)

        def root_response(root):
            def fetch():
                if root <= 8:
                    barrier.wait(timeout=5)
                return {"id": root, "kids": [root + 100]}
            return fetch

        def child_response(root):
            def fetch():
                with closing(sqlite3.connect(self.path, autocommit=True)) as reader:
                    self.assertIsNotNone(reader.execute("SELECT item_json FROM archive_items WHERE root_id=? AND item_id=?", (root, root)).fetchone())
                return {"id": root + 100}
            return fetch

        opener = HNOpener({root: root_response(root) for root in range(1, 13)} | {root + 100: child_response(root) for root in range(1, 13)})
        self.run_archive(range(1, 13), opener)
        self.assertEqual(set(opener.requests[:8]), set(range(1, 9)))
        self.assertEqual(len(opener.requests), 24)
        self.assertEqual(self.conn.execute("SELECT count(*) FROM archives WHERE status='complete'").fetchone()[0], 12)

    def test_failure_cancels_submitted_requests_that_have_not_started(self):
        self.add_roots(*range(1, 10))
        # Constrain worker startup to leave submitted work queued. The production
        # scheduler still admits eight roots and must cancel unstarted requests.
        executor = ThreadPoolExecutor(max_workers=1)
        self.addCleanup(executor.shutdown, wait=True)
        ready = Event()
        cancelled = Event()
        submitted = []
        original_submit = executor.submit

        def submit(*args, **kwargs):
            future = original_submit(*args, **kwargs)
            future.add_done_callback(lambda done: cancelled.set() if done.cancelled() else None)
            submitted.append(future)
            if len(submitted) == 8:
                ready.set()
            return future

        def first():
            self.assertTrue(ready.wait(5))
            raise TimeoutError('stop queued work')

        def second():
            self.assertTrue(cancelled.wait(5))
            return {'id': 2}

        opener = HNOpener({1: first, 2: second})
        with patch('hn_search.archive.ThreadPoolExecutor', return_value=executor), patch.object(executor, 'submit', side_effect=submit):
            with self.assertRaises(TimeoutError):
                self.run_archive(range(1, 10), opener)
        self.assertGreaterEqual(sum(future.cancelled() for future in submitted), 6)
        self.assertTrue(set(opener.requests) <= {1, 2})
        self.assertEqual(self.conn.execute('SELECT count(*) FROM archives').fetchone()[0], 8)

    def test_export_failure_stops_dispatch_and_drains_running_response(self):
        from hn_search.archive_export import write_exports

        self.add_roots(1, 2)
        started = Event()
        release = Event()

        def first():
            self.assertTrue(started.wait(5))
            return {"id": 1}

        def second():
            started.set()
            self.assertTrue(release.wait(5))
            return {"id": 2, "kids": [20]}

        def fail_exports(conn, root, path):
            if root == 1:
                release.set()
                raise OSError("export failed")
            return write_exports(conn, root, path)

        opener = HNOpener({1: first, 2: second})
        with patch("hn_search.archive.write_exports", side_effect=fail_exports), self.assertRaisesRegex(OSError, "export failed"):
            self.run_archive([1, 2], opener)
        self.assertEqual(dict(self.conn.execute("SELECT root_id, status FROM archives")), {1: "complete", 2: "incomplete"})
        self.assertEqual(self.conn.execute("SELECT item_id FROM archive_items WHERE root_id=2").fetchall(), [(2,)])
        self.assertNotIn("status=complete", self.output.getvalue())
        self.assertIn("root=2 status=incomplete", self.output.getvalue())
        retry = HNOpener({20: {"id": 20}})
        self.run_archive([1, 2], retry)
        self.assertEqual(retry.requests, [20])

    def test_archive_story_delegates_to_batch_scheduler_and_propagates_failure(self):
        self.add_roots(1)
        opener = HNOpener({1: TimeoutError("offline")})
        with self.assertRaises(TimeoutError):
            archive_story(self.conn, 1, self.exports, opener=opener, clock=lambda: NOW)
        self.assertEqual(opener.requests, [1])
        archive_story(self.conn, 1, self.exports, opener=HNOpener({1: {"id": 1}}), clock=lambda: NOW)
        self.assertEqual(self.payload(1)["status"], "complete")

    def test_killed_process_preserves_checkpoints_and_completed_state(self):
        script = """
from contextlib import redirect_stdout
from io import BytesIO
import json
import sys
from unittest.mock import patch
from hn_search.archive import archive
from hn_search.catalog import open_catalog, commit_page
from hn_search.clickhouse import Post
conn = open_catalog(sys.argv[1])
commit_page(conn, [Post(1, 'root', '', '', 1, 5)])
def pause():
    print('ready', file=sys.__stdout__, flush=True)
    sys.stdin.read(1)
def opener(url, *, timeout):
    item_id = int(url.rsplit('/', 1)[1].split('.')[0])
    if item_id == 2 and sys.argv[3] == 'checkpoint':
        pause()
    return BytesIO(json.dumps({'id': item_id, 'kids': [2] if item_id == 1 else []}).encode())
def trace(sql):
    if sys.argv[3] == 'item_write' and sql.startswith('INSERT INTO archive_items VALUES (1, 2,'):
        pause()
conn.set_trace_callback(trace)
with redirect_stdout(sys.stderr):
    if sys.argv[3] == 'completion':
        with patch('hn_search.archive.write_exports', side_effect=lambda *args: pause()):
            archive(conn, [1], sys.argv[2], opener=opener)
    else:
        archive(conn, [1], sys.argv[2], opener=opener)
"""
        for mode in ("checkpoint", "item_write", "completion"):
            with self.subTest(mode=mode):
                path = Path(self.directory.name) / f"{mode}.sqlite3"
                exports = Path(self.directory.name) / mode
                proc = subprocess.Popen([sys.executable, "-c", script, str(path), str(exports), mode], cwd=ROOT,
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                try:
                    readable, _, _ = select.select([proc.stdout], [], [], 10)
                    self.assertTrue(readable, "process did not reach checkpoint")
                    self.assertEqual(proc.stdout.readline().strip(), "ready")
                finally:
                    proc.kill()
                    proc.communicate(timeout=5)
                with closing(open_catalog(path)) as conn:
                    self.assertEqual(conn.execute("SELECT status FROM archives").fetchone()[0], "complete" if mode == "completion" else "incomplete")
                    opener = HNOpener({2: {"id": 2}})
                    archive(conn, [1], exports, opener=opener)
                    self.assertEqual(opener.requests, [] if mode == "completion" else [2])


class ArchiveCommandTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "catalog.sqlite3"
        with closing(open_catalog(self.path)) as conn:
            commit_page(conn, [post(1), post(2)])

    def test_defaults_explicit_paths_and_command_line_usage_errors(self):
        cwd = os.getcwd()
        try:
            os.chdir(self.directory.name)
            Path("hn.sqlite3").write_bytes(self.path.read_bytes())
            with redirect_stdout(StringIO()):
                self.assertEqual(main(["archive", "1"], opener=HNOpener({1: {"id": 1}}), clock=lambda: NOW), 0)
                self.assertEqual(main(["--db", str(self.path), "archive", "--export-dir", "selected", "2", "2"], opener=HNOpener({2: {"id": 2}})), 0)
            self.assertTrue(Path("exports/1.json").exists())
            self.assertTrue(Path("exports/1.md").exists())
            self.assertTrue(Path("selected/2.md").exists())
            for args in (["collect"], ["feed", "--config", "missing.toml"], ["archive"], ["archive", "nope"], ["archive", "1", "--bad"]):
                with self.subTest(args=args), patch("hn_search.__main__.open_catalog") as opened, redirect_stderr(StringIO()):
                    with self.assertRaises(SystemExit) as raised:
                        main(args, opener=HNOpener())
                    self.assertEqual(raised.exception.code, 2)
                    opened.assert_not_called()
        finally:
            os.chdir(cwd)

    def test_missing_ids_exit_one_with_each_approved_error_before_archive_changes(self):
        opener = HNOpener()
        errors = StringIO()
        with redirect_stderr(errors):
            status = main(["--db", str(self.path), "archive", "1", "99", "88", "99"], opener=opener)
        self.assertEqual(status, 1)
        self.assertEqual(errors.getvalue().splitlines(), [f"error: {root} is not in the catalog; archive accepts only catalog stories" for root in (99, 88)])
        self.assertEqual(opener.requests, [])
        with closing(open_catalog(self.path)) as conn:
            self.assertEqual(conn.execute("PRAGMA user_version").fetchone()[0], 1)

    def test_network_failure_cli_exits_one_and_identifies_root_and_item(self):
        run = subprocess.run([sys.executable, "-c", """
import sys
from hn_search.__main__ import main
def opener(url, *, timeout):
    raise TimeoutError('offline')
raise SystemExit(main(['--db', sys.argv[1], 'archive', '1'], opener=opener))
""", str(self.path)], cwd=ROOT, capture_output=True, text=True, timeout=10)
        self.assertEqual(run.returncode, 1)
        self.assertIn("archive root=1 item=1", run.stderr)
        self.assertIn("status=incomplete", run.stdout)


if __name__ == "__main__":
    unittest.main()
