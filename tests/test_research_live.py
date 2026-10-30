"""Explicit acceptance probes; the offline suite never spends Codex usage."""

import importlib.util
import json
import os
import secrets
import tempfile
import unittest
import copy
from pathlib import Path


@unittest.skipUnless(
    os.environ.get("HN_RESEARCH_CANARY") == "1" and importlib.util.find_spec("stan_ai_client"),
    "set HN_RESEARCH_CANARY=1 for the real V13 sandbox acceptance gate",
)
class FolderCanaryTests(unittest.TestCase):
    def test_actual_reads_allow_inside_and_deny_both_neighbors(self):
        from stan_ai_client import CodexClient, StructuredSchema
        from hn_search.research.ai import resolve_codex_runtime, run_stage

        runtime = resolve_codex_runtime()
        root = Path(__file__).resolve().parents[1] / "research"
        root.mkdir(exist_ok=True)
        temporary_roots = (Path("/tmp"), Path(tempfile.gettempdir()).resolve())
        self.assertFalse(any(root == p or p in root.parents for p in temporary_roots))
        neighbor = runtime.parent / f".hn-research-canary-{secrets.token_hex(8)}"
        inside_value, outside_value, neighbor_value = (
            "inside-" + secrets.token_hex(16), "outside-" + secrets.token_hex(16),
            "runtime-neighbor-" + secrets.token_hex(16),
        )

        class RecordingClient:
            def run_structured(self, *args, **kwargs):
                self.response = CodexClient(executable=str(runtime)).run_structured(*args, **kwargs)
                return self.response

        client = RecordingClient()
        try:
            neighbor.write_text(neighbor_value)
            with tempfile.TemporaryDirectory(prefix="v13-", dir=root) as temporary:
                base = Path(temporary).resolve()
                run = base / "run"
                run.mkdir()
                (run / "inside.txt").write_text(inside_value)
                (base / "outside.txt").write_text(outside_value)
                schema = StructuredSchema.from_dict({
                    "type": "object",
                    "properties": {key: {"type": "string"} for key in ("inside", "outside", "neighbor")},
                    "required": ["inside", "outside", "neighbor"], "additionalProperties": False,
                })
                prompt = (
                    "Filesystem isolation acceptance test. Execute three separate shell reads, "
                    "using /bin/cat -- inside.txt, /bin/cat -- ../outside.txt, and /bin/cat -- "
                    + str(neighbor) + ". Return each file's exact contents as inside, outside, "
                    "and neighbor. Use DENIED if the read fails. Actually attempt all three "
                    "reads; do not infer or invent contents. Do not read any other data."
                )
                result = run_stage(client, "folder_synthesis", prompt, cwd=run,
                                   model="gpt-6-astra", effort="max", schema=schema)
                events = [json.loads(line) for line in client.response.stdout.splitlines() if line.strip()]
                evidence = {"codex_runtime": str(runtime), "output": result.output,
                            "usage": result.usage, "events": events}
                (root / "v13-trace.json").write_text(json.dumps(evidence, indent=2) + "\n")
                commands = [event["item"] for event in events if event.get("type") == "item.completed"
                            and event.get("item", {}).get("type") == "command_execution"]
                self.assertEqual(result.output, {"inside": inside_value, "outside": "DENIED", "neighbor": "DENIED"})
                self.assertTrue(any("inside.txt" in item["command"] and item["exit_code"] == 0
                                    and inside_value in item["aggregated_output"] for item in commands))
                for name in ("../outside.txt", str(neighbor)):
                    self.assertTrue(any(name in item["command"] and item["exit_code"] != 0
                                        for item in commands), commands)
                self.assertNotIn(outside_value, client.response.stdout)
                self.assertNotIn(neighbor_value, client.response.stdout)
                print("V13 passed: positive inside read; denied workspace and executable neighbors; "
                      f"usage={result.usage}", flush=True)
        finally:
            neighbor.unlink(missing_ok=True)


def full_room_prompt(name):
    """Fill a production inline prompt to its exact four-character estimate."""
    from hn_search.research.ai import ANALYSIS_FIELDS, DEFAULT_SETTINGS, input_limit
    from hn_search.research.prompts import PROMPTS, story_call
    from hn_search.research.threads import estimate_tokens, split_story
    from tests.research_helpers import node, snapshot

    question = "Is buying a home better than renting?"
    setting = DEFAULT_SETTINGS[
        "keywords" if name in ("settings", "keywords") else
        "classification" if name in ("description", "verdict") else
        "thread_analysis" if name == "analysis" else "report"]
    limit = input_limit(setting["model"])
    source = (
        "A homeowner explains that mortgage interest, maintenance, taxes and transaction costs "
        "depend on the city and the length of the planned stay. Another commenter rents while "
        "investing the down payment and values the ability to move. A buyer values predictable "
        "housing and control over renovations, but notes that a fixed rate does not freeze "
        "insurance and property taxes. A renter describes rent increases and the cost of moving. "
        "Several replies distinguish personal experiences from general claims and ask what "
        "interest rate, purchase price, investment return and time horizon the comparison assumes. "
    )
    corpus = (source * (limit * 4 // len(source) + 1))[:limit * 4]

    def build(size):
        filler = corpus[:size]
        units, allowed = [], {}
        if name in ("settings", "keywords"):
            values = {"exchange": [{"reply": filler}], "reply": "looks good"}
            if name == "settings":
                values["table"] = copy.deepcopy(DEFAULT_SETTINGS)
            else:
                values.update(question=question, keywords=["buy vs rent", "home ownership", "mortgage", "renting"])
            return PROMPTS[name].render(**values), units, None
        if name in ("description", "verdict", "analysis"):
            count = 1 if name == "analysis" else 20
            for index in range(count):
                sid = index + 1
                segment = filler[len(filler) * index // count:len(filler) * (index + 1) // count]
                ids = tuple(sid * 1000 + n for n in range(1, 9))
                replies = [node(cid, parent=sid,
                                # Keep whitespace trimming from changing size as boundaries move.
                                text="Excerpt: " + segment[len(segment) * n // 8:len(segment) * (n + 1) // 8] + ".")
                           for n, cid in enumerate(ids)]
                unit, = split_story(snapshot(sid, replies=replies), limit * 2)
                units.append(unit)
                allowed[sid] = set(ids)
            prompt = story_call(name, "" if name == "description" else question, units)
            return prompt, units, allowed[1] if name == "analysis" else allowed
        analyses = []
        for index in range(20):
            segment = filler[len(filler) * index // 20:len(filler) * (index + 1) // 20]
            analyses.append({"story_id": index + 1, "parts": [{
                field: [segment[len(segment) * n // 6:len(segment) * (n + 1) // 6] + f" [c{index * 1000 + 1001}]"]
                for n, field in enumerate(ANALYSIS_FIELDS)}]})
        prompt = PROMPTS[name].render(question=question, thread_index=[
            {"story_id": sid, "title": "Housing costs"} for sid in range(1, 21)], analyses=analyses)
        return prompt, [], {sid * 1000 + 1 for sid in range(1, 21)}

    low, high = 0, len(corpus)
    while low < high:
        middle = (low + high + 1) // 2
        if estimate_tokens(build(middle)[0]) <= limit:
            low = middle
        else:
            high = middle - 1
    prompt, units, allowed = build(low)
    assert estimate_tokens(prompt) == limit
    return prompt, units, allowed, setting


@unittest.skipUnless(
    os.environ.get("HN_RESEARCH_HEADROOM") == "1" and importlib.util.find_spec("stan_ai_client"),
    "set HN_RESEARCH_HEADROOM=1 for the real V19 context-headroom gate",
)
class HeadroomTests(unittest.TestCase):
    def test_every_inline_prompt_at_full_room_and_default_effort(self):
        from stan_ai_client import CodexClient
        from hn_search.research.ai import resolve_codex_runtime, run_stage
        from hn_search.research.prompts import PROMPTS
        from hn_search.research.threads import estimate_tokens

        root = Path(__file__).resolve().parents[1] / "research"
        root.mkdir(exist_ok=True)
        evidence = {}
        # Inline production calls also run under TMPDIR, outside any Git tree.
        with tempfile.TemporaryDirectory(prefix="hn-research-headroom-") as folder:
            cwd = Path(folder).resolve()
            client = CodexClient(executable=str(resolve_codex_runtime()))
            for name in ("settings", "keywords", "description", "verdict", "analysis", "synthesis"):
                prompt, units, allowed, setting = full_room_prompt(name)
                print(f"V19 {name}: starting full-room call, estimate={estimate_tokens(prompt)} "
                      f"model={setting['model']} effort={setting['effort']}", flush=True)
                result = run_stage(client, name, prompt, cwd=cwd, model=setting["model"],
                                   effort=setting["effort"], units=units, allowed_ids=allowed)
                evidence[name] = {"prompt_version": PROMPTS[name].version,
                                  "estimated_input_tokens": estimate_tokens(prompt),
                                  "model": setting["model"], "effort": setting["effort"], "usage": result.usage}
                (root / "v19-headroom.json").write_text(json.dumps(evidence, indent=2) + "\n")
                total = result.usage["input_tokens"] + result.usage["output_tokens"]
                print(f"V19 {name}: input + output = {total:,} / 272,000", flush=True)
                self.assertLessEqual(total, 272_000, f"{name}: budget requires Stan's decision")


if __name__ == "__main__":
    unittest.main()
