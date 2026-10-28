"""Whole-subtree splitting and deterministic, largest-first call packing."""

import hashlib
import html
import json
from dataclasses import dataclass
from pathlib import Path

from .render import body, date, walk_comments


UNITS_PER_CALL = 20


def unit_identity(story_id, part):
    return f"Source unit identity: story_id={story_id}, part={part}\n"


def estimate_tokens(text):
    return (len(text) + 3) // 4


@dataclass(frozen=True)
class Unit:
    story_id: int
    part: int
    text: str
    comment_ids: tuple
    input_key: str

    @property
    def size(self):
        return estimate_tokens(self.text + "\n" + unit_identity(self.story_id, self.part))


def load_export(path):
    with Path(path).open() as source:
        snapshot = json.load(source)
    if snapshot["status"] != "complete":
        raise ValueError(f"archive {snapshot['root_id']} is incomplete")
    return snapshot


def _attributes(values):
    return " ".join(f'{key}="{html.escape(str(value), quote=True)}"' for key, value in values.items())


def _comment(node, parent):
    item = node["item"] or {}
    attrs = _attributes({"id": node["id"], "parent": parent, "by": item.get("by", "unknown"),
                         "time": date(item.get("time"))})
    citation = (f"Source citation: [c{node['id']}]\n"
                if item.get("type") == "comment" and not item.get("deleted") else "")
    return f"<comment {attrs}>\n{citation}{body(node['item'], escape=False)}\n</comment>\n"


def _header(snapshot, part):
    item = snapshot["root"]["item"] or {}
    attrs = _attributes({"id": snapshot["root_id"], "part": part, "title": item.get("title", ""),
                         "by": item.get("by", "unknown"), "posted": date(item.get("time")),
                         "reported_comments": snapshot.get("reported_descendants", "unknown")})
    header = f"<hn_story {attrs}>\n{body(snapshot['root']['item'], escape=False)}\n"
    for option in snapshot.get("poll_options", []):
        header += f"<poll_option id=\"{option['id']}\" votes=\"{(option['item'] or {}).get('score', 'unknown')}\">\n"
        header += body(option["item"], escape=False) + "\n</poll_option>\n"
    return header


def story_prompt(snapshot, comment_ids=None, context_ids=(), *, part=0):
    nodes = {node["id"]: (node, parent) for node, _, parent in walk_comments(snapshot)}
    if comment_ids is None:
        comment_ids = tuple(nodes)
    result = _header(snapshot, part)
    if context_ids:
        result += "<context>\n" + "".join(_comment(*nodes[cid]) for cid in context_ids) + "</context>\n"
    return result + "".join(_comment(*nodes[cid]) for cid in comment_ids) + "</hn_story>"


def split_story(snapshot, room):
    """Keep every saved comment once as owned text; repeat only ancestry as context."""
    story_id = snapshot["root_id"]
    base_key = f"archive:{story_id}@{snapshot['finished_at']}"
    ordered = list(walk_comments(snapshot))
    ids = [node["id"] for node, _, _ in ordered]
    nodes = {node["id"]: node for node, _, _ in ordered}
    parents = {node["id"]: parent for node, _, parent in ordered}
    snippets = {node["id"]: _comment(node, parent) for node, _, parent in ordered}

    def make(owned, context, number):
        text = _header(snapshot, number)
        if context:
            text += "<context>\n" + "".join(snippets[cid] for cid in context) + "</context>\n"
        text += "".join(snippets[cid] for cid in owned) + "</hn_story>"
        key = base_key
        if number:
            digest = hashlib.sha256(json.dumps(owned, separators=(",", ":")).encode()).hexdigest()[:12]
            key += "#" + digest
        return Unit(story_id, number, text, tuple(owned), key)

    whole = make(ids, (), 0)
    if whole.size <= room:
        return [whole]
    if not ids:
        raise ValueError(f"story {story_id} root exceeds the input budget")
    positions = {cid: index for index, cid in enumerate(ids)}
    ends = {}
    stack = []
    for index, (node, depth, _) in enumerate(ordered):
        while stack and stack[-1][1] >= depth:
            ends[stack.pop()[0]] = index
        stack.append((node["id"], depth))
    while stack:
        ends[stack.pop()[0]] = len(ids)
    prefix = [0]
    for cid in ids:
        prefix.append(prefix[-1] + len(snippets[cid]))

    def ancestors(cid):
        chain = []
        parent = parents[cid]
        while parent in nodes:
            chain.append(parent)
            parent = parents[parent]
        return list(reversed(chain))

    parts, owned, context = [], [], []
    owned_chars = 0

    def fits(extra_chars, chain, *, new_part=False):
        number = len(parts) + 1 + int(new_part and bool(owned))
        overhead = len(_header(snapshot, number)) + len("</hn_story>\n")
        overhead += len(unit_identity(story_id, number))
        if chain:
            overhead += len("<context>\n</context>\n") + sum(len(snippets[cid]) for cid in chain)
        return (overhead + extra_chars + 3) // 4 <= room

    def finish():
        nonlocal owned, context, owned_chars
        if owned:
            parts.append(make(owned, context, len(parts) + 1))
        owned, context, owned_chars = [], [], 0

    tasks = [(node["id"], False) for node, depth, _ in reversed(ordered) if depth == 0]
    while tasks:
        cid, alone = tasks.pop()
        start, end = positions[cid], positions[cid] + 1 if alone else ends[cid]
        size = prefix[end] - prefix[start]
        parent_available = parents[cid] == story_id or parents[cid] in owned or parents[cid] in context
        if owned and parent_available and fits(owned_chars + size, context):
            owned.extend(ids[start:end])
            owned_chars += size
            continue
        chain = ancestors(cid)
        if fits(size, chain, new_part=True):
            finish()
            owned, context, owned_chars = ids[start:end], chain, size
        elif not alone:
            tasks.extend((child["id"], False) for child in reversed(nodes[cid]["replies"]))
            tasks.append((cid, True))
        else:
            raise ValueError(f"story {story_id} comment {cid} and its ancestry exceed the input budget")
    finish()
    covered = [cid for unit in parts for cid in unit.comment_ids]
    if covered != ids or len(set(covered)) != len(ids):
        raise AssertionError(f"split lost or repeated comments in story {story_id}")
    if any(unit.size > room for unit in parts):
        raise AssertionError(f"split exceeds the input budget for story {story_id}")
    return parts


def pack(units, room):
    calls, sizes = [], []
    for unit in sorted(units, key=lambda item: (-item.size, item.story_id, item.part)):
        if unit.size > room:
            raise ValueError(f"story {unit.story_id} part {unit.part} exceeds the call budget")
        for index, call in enumerate(calls):
            if len(call) < UNITS_PER_CALL and sizes[index] + unit.size <= room:
                call.append(unit)
                sizes[index] += unit.size
                break
        else:
            calls.append([unit])
            sizes.append(unit.size)
    return calls


def combine_verdicts(parts):
    verdict = next((value for value in ("relevant", "uncertain", "irrelevant")
                    if any(part["verdict"] == value for part in parts)), "uncertain")
    return {"verdict": verdict, "reasons": "\n\n".join(part["reasons"] for part in parts),
            "comment_ids": sorted({cid for part in parts for cid in part["comment_ids"]})}
