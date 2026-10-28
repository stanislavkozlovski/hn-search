import importlib.util
import tempfile
import tomllib
import unittest
import copy
import io
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


@unittest.skipUnless(importlib.util.find_spec("stan_ai_client"), "optional stan-ai-client is absent")
class RuntimeGrantTests(unittest.TestCase):
    def test_only_the_exact_native_file_is_granted(self):
        from hn_search.research.ai import run_options

        runtime = Path("/opt/isolated-codex/bin/codex")
        with patch("hn_search.research.ai.resolve_codex_runtime", return_value=runtime):
            options = run_options("folder_synthesis", "/work/run", "gpt-6-astra", "max")
        config = tomllib.loads("\n".join(options.config_overrides))
        self.assertEqual(config["permissions"]["hn_research"]["filesystem"], {
            ":root": "deny", ":minimal": "read", ":workspace_roots": "read",
            ":tmpdir": "deny", ":slash_tmp": "deny", str(runtime): "read",
        })
        self.assertNotIn(str(runtime.parent), config["permissions"]["hn_research"]["filesystem"])
        self.assertFalse(config["permissions"]["hn_research"]["network"]["enabled"])
        self.assertEqual(config["web_search"], "disabled")
        self.assertFalse(config["features"]["apps"])
        self.assertEqual(config["project_doc_max_bytes"], 0)
        self.assertEqual(options.permission_mode, "default")
        self.assertTrue(options.ignore_user_config)
        self.assertTrue(options.ignore_rules)
        self.assertEqual(options.extra_args, ("--ephemeral",))

    def test_resolver_follows_a_native_file_symlink_and_rejects_wrappers(self):
        from hn_search.research.ai import resolve_codex_runtime

        with tempfile.TemporaryDirectory() as folder:
            native = Path(folder) / "native"
            native.write_bytes(b"\x7fELFtest-only")
            native.chmod(0o700)
            link = Path(folder) / "codex"
            link.symlink_to(native)
            resolve_codex_runtime.cache_clear()
            try:
                with patch("hn_search.research.ai.shutil.which", return_value=str(link)):
                    self.assertEqual(resolve_codex_runtime(), native.resolve())
                resolve_codex_runtime.cache_clear()
                native.write_text("#!/bin/sh\nexit 0\n")
                with patch("hn_search.research.ai.shutil.which", return_value=str(link)):
                    with self.assertRaisesRegex(ValueError, "native Codex runtime"):
                        resolve_codex_runtime()
            finally:
                resolve_codex_runtime.cache_clear()

    def test_npm_launcher_resolution_returns_only_its_real_native_file(self):
        from hn_search.research.ai import resolve_codex_runtime

        with tempfile.TemporaryDirectory() as folder:
            package = Path(folder) / "node_modules" / "@openai" / "codex"
            (package / "bin").mkdir(parents=True)
            launcher = package / "bin" / "codex.js"
            launcher.write_text("// test launcher")
            (package / "package.json").write_text('{"name":"@openai/codex"}')
            native = Path(folder) / "platform-package" / "vendor" / "bin" / "codex"
            native.parent.mkdir(parents=True)
            native.write_bytes(b"\x7fELFtest-only")
            native.chmod(0o700)
            resolve_codex_runtime.cache_clear()
            try:
                with patch("hn_search.research.ai.shutil.which", return_value=str(launcher)), patch(
                    "hn_search.research.ai.platform.system", return_value="Linux"
                ), patch("hn_search.research.ai.platform.machine", return_value="x86_64"), patch(
                    "hn_search.research.ai.subprocess.check_output", return_value=str(native)
                ) as node:
                    self.assertEqual(resolve_codex_runtime(), native.resolve())
                argv = node.call_args.args[0]
                self.assertEqual(argv[-3:], [str(launcher), "@openai/codex-linux-x64", "x86_64-unknown-linux-musl"])
            finally:
                resolve_codex_runtime.cache_clear()


@unittest.skipUnless(importlib.util.find_spec("stan_ai_client"), "optional stan-ai-client is absent")
class StructuredCallTests(unittest.TestCase):
    def setUp(self):
        self.runtime = patch("hn_search.research.ai.resolve_codex_runtime", return_value=Path("/native/codex"))
        self.runtime.start()
        self.addCleanup(self.runtime.stop)

    def test_all_schemas_and_calls_use_the_boundary(self):
        from stan_ai_client import validate_codex_output_schema
        from hn_search.research.ai import run_stage
        from hn_search.research.prompts import PROMPTS
        from hn_search.research.threads import split_story
        from tests.research_helpers import FakeClient, snapshot

        for name, prompt in PROMPTS.items():
            validate_codex_output_schema(prompt.schema)
        client = FakeClient()
        unit = split_story(snapshot(), 10000)[0]
        from hn_search.research.prompts import story_call
        for name in ("description", "verdict", "analysis"):
            result = run_stage(client, name, story_call(name, "Question?", [unit]), cwd="/work/run",
                               model="gpt-6-luna", effort="high", units=[unit],
                               allowed_ids={1001} if name == "analysis" else {1: {1001}})
            self.assertEqual(result.usage["input_tokens"], 100)
        self.assertEqual(len(client.calls), 3)
        self.assertTrue(all(call.options.cwd == Path("/work/run") for call in client.calls))
        self.assertTrue(all(call.options.permission_mode == "default" for call in client.calls))

    def test_missing_middle_story_is_named_and_all_identities_are_explicit(self):
        from hn_search.research.ai import run_stage
        from hn_search.research.prompts import story_call
        from hn_search.research.threads import split_story
        from tests.research_helpers import FakeClient, snapshot

        ids = [29696653, 46673809, 11120249, 21753230, 31752153]
        units = [split_story(snapshot(sid), 10000)[0] for sid in ids]
        prompt = story_call("description", "", units)
        manifest = prompt[prompt.rfind("</hn_story>") + len("</hn_story>"):]
        for sid in ids:
            self.assertEqual(manifest.count(f"story_id={sid}, part=0"), 1)
        client = FakeClient()
        client.transform = lambda name, output: {"stories": output["stories"][:2] + output["stories"][3:]}
        stderr = io.StringIO()
        with self.assertRaisesRegex(ValueError, "11120249"):
            run_stage(client, "description", prompt, cwd="/work/run", model="gpt-6-luna",
                      effort="high", units=units, allowed_ids={sid: {sid * 1000 + 1} for sid in ids},
                      stderr=stderr)
        for sid in ids:
            self.assertIn(str(sid), stderr.getvalue())

    def test_verdict_schema_restricts_source_ids_without_mutating_the_contract(self):
        from jsonschema.exceptions import ValidationError
        from stan_ai_client import validate_codex_output_schema
        from hn_search.research.ai import verdict_schema
        from hn_search.research.prompts import PROMPTS
        from hn_search.research.threads import split_story
        from tests.research_helpers import node, snapshot

        contract = PROMPTS["verdict"]
        original, version = copy.deepcopy(contract.schema.schema), contract.version
        units = [split_story(snapshot(1, replies=[node(1001), node(1002, deleted=True)]), 10000)[0],
                 split_story(snapshot(2), 10000)[0]]
        schema = verdict_schema(contract.schema, units, {1: {1001}, 2: {2001}})
        validate_codex_output_schema(schema)
        rows = [{"story_id": sid, "part": 0, "verdict": "relevant", "reasons": "Housing discussion",
                 "comment_ids": [sid * 1000 + 1]} for sid in (1, 2)]
        schema.validate_response({"stories": rows})
        for wrong_id in (1002, 2001, 99999):
            changed = copy.deepcopy(rows)
            changed[0]["comment_ids"] = [wrong_id]
            with self.assertRaises(ValidationError):
                schema.validate_response({"stories": changed})
        self.assertEqual(contract.schema.schema, original)
        self.assertEqual(contract.version, version)

    def test_verdict_schema_allows_only_empty_ids_without_citable_comments(self):
        from jsonschema.exceptions import ValidationError
        from stan_ai_client import validate_codex_output_schema
        from hn_search.research.ai import verdict_schema
        from hn_search.research.prompts import PROMPTS
        from hn_search.research.threads import split_story
        from tests.research_helpers import node, snapshot

        unit = split_story(snapshot(replies=[node(1001, deleted=True)]), 10000)[0]
        schema = verdict_schema(PROMPTS["verdict"].schema, [unit], {1: set()})
        validate_codex_output_schema(schema)
        row = {"story_id": 1, "part": 0, "verdict": "uncertain", "reasons": "No readable comments",
               "comment_ids": []}
        schema.validate_response({"stories": [row]})
        with self.assertRaises(ValidationError):
            schema.validate_response({"stories": [{**row, "comment_ids": [1001]}]})

    def test_identity_manifest_counts_toward_the_packing_budget(self):
        from hn_search.research.prompts import story_call, story_instructions
        from hn_search.research.threads import estimate_tokens, pack, split_story
        from tests.research_helpers import snapshot

        units = [split_story(snapshot(sid), 10000)[0] for sid in (12345678, 23456789)]
        bare_room = sum(estimate_tokens(unit.text + "\n") for unit in units)
        calls = pack(units, bare_room)
        self.assertEqual(len(calls), 2)
        for name in ("description", "verdict", "analysis"):
            budget = estimate_tokens(story_instructions(name, "Question?")) + bare_room
            for call in calls:
                self.assertLessEqual(estimate_tokens(story_call(name, "Question?", call)), budget)

    def test_missing_repeated_extra_foreign_and_deleted_units_fail_the_call(self):
        from hn_search.research.ai import run_stage
        from hn_search.research.prompts import story_call
        from hn_search.research.threads import split_story
        from tests.research_helpers import FakeClient, node, snapshot

        tree = snapshot(replies=[node(1001), node(1002, deleted=True)])
        unit = split_story(tree, 10000)[0]
        changes = [
            lambda rows: [],
            lambda rows: rows + copy.deepcopy(rows),
            lambda rows: rows + [{**rows[0], "story_id": 2}],
            lambda rows: [{**rows[0], "comment_ids": [99999]}],
            lambda rows: [{**rows[0], "comment_ids": [1002]}],
            lambda rows: [{**rows[0], "reasons": "Unsupported [c99999]"}],
        ]
        for change in changes:
            client = FakeClient()
            client.transform = lambda name, output: {"stories": change(output["stories"])}
            error = io.StringIO()
            with self.subTest(change=change), self.assertRaises(ValueError):
                run_stage(client, "verdict", story_call("verdict", "Question?", [unit]), cwd="/work/run",
                          model="gpt-6-luna", effort="high", units=[unit], allowed_ids={1: {1001}}, stderr=error)
            self.assertIn("verdict failed for 1", error.getvalue())

    def test_uncited_or_foreign_analysis_items_and_typed_failures_are_visible(self):
        from stan_ai_client import CodexTimeoutError
        from hn_search.research.ai import run_stage
        from hn_search.research.prompts import story_call
        from hn_search.research.threads import split_story
        from tests.research_helpers import FakeClient, snapshot

        unit = split_story(snapshot(), 10000)[0]
        for claim in ("no citation", "foreign [c2001]"):
            client = FakeClient()
            client.transform = lambda name, output: {**output, "arguments": [claim]}
            with self.subTest(claim=claim), self.assertRaises(ValueError):
                run_stage(client, "analysis", story_call("analysis", "Question?", [unit]), cwd="/work/run",
                          model="gpt-6-astra", effort="max", units=[unit], allowed_ids={1001}, stderr=io.StringIO())
        # The boundary preserves the client's exception object and never retries.
        error = CodexTimeoutError.__new__(CodexTimeoutError)
        Exception.__init__(error, "test timeout")
        client = SimpleNamespace(run_structured=lambda *args, **kwargs: (_ for _ in ()).throw(error))
        stream = io.StringIO()
        with self.assertRaises(CodexTimeoutError) as raised:
            run_stage(client, "analysis", story_call("analysis", "Q", [unit]), cwd="/work/run",
                      model="gpt-6-astra", effort="max", units=[unit], allowed_ids={1001}, stderr=stream)
        self.assertIs(raised.exception, error)
        self.assertIn("analysis failed for 1", stream.getvalue())

    def test_report_failure_names_all_source_stories(self):
        from hn_search.research.ai import run_stage
        from tests.research_helpers import FakeClient

        client = FakeClient()
        client.fail = lambda call: True
        stream = io.StringIO()
        with self.assertRaisesRegex(RuntimeError, "test client failure"):
            run_stage(client, "synthesis", "Synthesize evidence", cwd="/work/run",
                      model="gpt-6-astra", effort="max", allowed_ids=set(),
                      source_story_ids=[4, 1], stderr=stream)
        self.assertIn("synthesis failed for 1, 4", stream.getvalue())


if __name__ == "__main__":
    unittest.main()
