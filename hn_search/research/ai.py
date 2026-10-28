"""The single boundary for structured, isolated Codex calls."""

import json
import copy
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from stan_ai_client import CodexRunOptions, StructuredSchema


# Verified against the installed Codex model catalog, 2026-10-27.
CONTEXT_WINDOWS = {"gpt-6-astra": 272_000, "gpt-6-luna": 272_000, "gpt-6.1-sol": 500_000}
EFFORTS = ("low", "medium", "high", "xhigh", "max")
DEFAULT_SETTINGS = {
    "keywords": {"model": "gpt-6-luna", "effort": "medium"},
    "classification": {"model": "gpt-6-luna", "effort": "high"},
    "thread_analysis": {"model": "gpt-6-astra", "effort": "max"},
    "report": {"model": "gpt-6-astra", "effort": "max"},
}
TIMEOUTS = {"settings": 300, "keywords": 300, "description": 1800, "verdict": 1800,
            "analysis": 7200, "synthesis": 7200, "folder_synthesis": 43_200}
CITATION = re.compile(r"\[c([0-9]+)\]")
ANALYSIS_FIELDS = ("arguments", "counterarguments", "assumptions", "conditions",
                   "lived_experiences", "unresolved_disagreements")


def input_limit(model):
    return CONTEXT_WINDOWS[model] * 4 // 5


@lru_cache(maxsize=1)
def resolve_codex_runtime():
    """Resolve the native Linux runtime, never granting a launcher directory.

    The npm entry point selects an optional platform package. Follow that same
    package resolution, including its bundled-vendor fallback. On this host
    codex-upstream is the installation's launcher behind the shell wrapper.
    """
    entry = shutil.which("codex-upstream") or shutil.which("codex")
    if entry is None:
        raise ValueError("research requires a logged-in codex CLI on PATH")
    executable = Path(entry).resolve(strict=True)
    if executable.suffix == ".js":
        package = executable.parent.parent
        if json.loads((package / "package.json").read_text())["name"] != "@openai/codex":
            raise ValueError("cannot identify the installed Codex package")
        targets = {"x86_64": ("x86_64-unknown-linux-musl", "@openai/codex-linux-x64"),
                   "aarch64": ("aarch64-unknown-linux-musl", "@openai/codex-linux-arm64")}
        if platform.system() != "Linux" or platform.machine() not in targets:
            raise ValueError("research runtime isolation currently requires Linux x64 or arm64")
        target, package_name = targets[platform.machine()]
        script = """const {createRequire} = require('node:module');
const path = require('node:path');
const req = createRequire(process.argv[1]);
let vendor;
try { vendor = path.join(path.dirname(req.resolve(process.argv[2] + '/package.json')), 'vendor'); }
catch { vendor = path.join(path.dirname(process.argv[1]), '..', 'vendor'); }
process.stdout.write(path.join(vendor, process.argv[3], 'bin', 'codex'));"""
        executable = Path(subprocess.check_output(
            ["node", "-e", script, str(executable), package_name, target], text=True,
        )).resolve(strict=True)
    if not executable.is_file() or not os.access(executable, os.X_OK):
        raise ValueError(f"Codex runtime is not an executable file: {executable}")
    with executable.open("rb") as file:
        if file.read(4) != b"\x7fELF":
            raise ValueError(f"cannot resolve a native Codex runtime from {entry}")
    return executable


def run_options(name, cwd, model, effort):
    runtime = json.dumps(str(resolve_codex_runtime()))
    return CodexRunOptions(
        cwd=Path(cwd), model=model, reasoning_effort=effort,
        timeout_seconds=TIMEOUTS[name], permission_mode="default",
        skip_git_repo_check=True, ignore_user_config=True, ignore_rules=True,
        extra_args=("--ephemeral",),
        config_overrides=(
            'default_permissions="hn_research"',
            'permissions.hn_research.filesystem={":root"="deny", ":minimal"="read", '
            '":workspace_roots"="read", ":tmpdir"="deny", ":slash_tmp"="deny", '
            + runtime + '="read"}',
            "permissions.hn_research.network.enabled=false",
            'approval_policy="never"', 'web_search="disabled"', "features.apps=false",
            # Calls have complete, versioned instructions in their prompt.
            # Do not discover AGENTS.md in denied ancestors or the Codex home.
            "project_doc_max_bytes=0",
        ),
    )


@dataclass(frozen=True)
class StageResult:
    output: dict
    usage: dict


def cited_ids(value):
    """Collect citation markers in arbitrary structured text."""
    if isinstance(value, str):
        return {int(match) for match in CITATION.findall(value)}
    if isinstance(value, dict):
        return set().union(*(cited_ids(item) for item in value.values()), set())
    if isinstance(value, list):
        return set().union(*(cited_ids(item) for item in value), set())
    return set()


def check_citations(value, allowed):
    foreign = cited_ids(value) - set(allowed)
    if foreign:
        raise ValueError(f"invalid comment citation c{min(foreign)}")


def verdict_schema(schema, units, allowed_ids):
    """Constrain each verdict to its source identity and printed comment IDs.

    These bounds derive from the archived input. The versioned output shape
    stays the same, and reuse remains independent of the other units in a call.
    """
    document = copy.deepcopy(schema.schema)
    variants = []
    for unit in units:
        variant = copy.deepcopy(document["properties"]["stories"]["items"])
        fields = variant["properties"]
        fields["story_id"] = {**fields["story_id"], "enum": [unit.story_id]}
        fields["part"] = {**fields["part"], "enum": [unit.part]}
        ids = sorted(cited_ids(unit.text) & set(allowed_ids[unit.story_id]))
        if ids:
            fields["comment_ids"]["items"] = {**fields["comment_ids"]["items"], "enum": ids}
        else:
            fields["comment_ids"]["maxItems"] = 0
        variants.append(variant)
    document["properties"]["stories"]["items"] = {"anyOf": variants}
    return StructuredSchema.from_dict(document)


def validate_reply(name, output, units, allowed_ids):
    if name in ("description", "verdict"):
        expected = Counter((unit.story_id, unit.part) for unit in units)
        actual = Counter((item["story_id"], item["part"]) for item in output["stories"])
        if expected != actual:
            raise ValueError(f"{name} units differ: expected {dict(expected)}, received {dict(actual)}")
        for item in output["stories"]:
            allowed = allowed_ids[item["story_id"]]
            check_citations(item, allowed)
            if name == "verdict":
                foreign = set(item["comment_ids"]) - set(allowed)
                if foreign:
                    raise ValueError(f"story {item['story_id']} invalid comment ID {min(foreign)}")
    elif name in ("analysis", "synthesis", "folder_synthesis"):
        for field in ANALYSIS_FIELDS:
            for item in output[field]:
                if not CITATION.search(item):
                    raise ValueError(f"{field} item has no comment citation: {item!r}")
                check_citations(item, allowed_ids)


def run_stage(client, name, prompt, *, cwd, model, effort, units=(), allowed_ids=None,
              schema=None, call_label=None, source_story_ids=(), stderr=None):
    """Validate the entire call before a caller can save any of its results."""
    if schema is None:
        from .prompts import PROMPTS
        schema = PROMPTS[name].schema
    response_schema = (verdict_schema(schema, units, allowed_ids)
                       if name == "verdict" and units and allowed_ids is not None else schema)
    label = call_label or name
    story_ids = sorted({unit.story_id for unit in units} | set(source_story_ids))
    start = time.monotonic()
    try:
        # Keep the same conservative estimate used by splitting and packing.
        if (len(prompt) + 3) // 4 > input_limit(model):
            raise ValueError(f"{name} prompt exceeds {model}'s input budget")
        if len(units) > 20:
            raise ValueError(f"{name} call exceeds 20 story units")
        response = client.run_structured(
            prompt, schema=response_schema, options=run_options(name, cwd, model, effort),
            capture_usage=True,
        )
        output = response.structured_output
        schema.validate_response(output)
        if allowed_ids is not None:
            validate_reply(name, output, units, allowed_ids)
        if response_schema is not schema:
            response_schema.validate_response(output)
    except BaseException:
        stories = ", ".join(map(str, story_ids)) or "conversation/report"
        print(f"research: {label} failed for {stories}", file=stderr or sys.stderr, flush=True)
        raise
    usage = {"elapsed_ms": round((time.monotonic() - start) * 1000)}
    payload = getattr(response, "payload", None)
    if payload is not None:
        usage.update(payload.usage)
    return StageResult(output, usage)
