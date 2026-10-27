"""Render complete archives from SQLite, preserving the saved API evidence."""

from datetime import datetime, timezone
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import tempfile
from urllib.parse import quote, urljoin, urlsplit


def load_items(conn, root):
    return {
        item_id: (json.loads(payload), retrieved_at)
        for item_id, payload, retrieved_at in conn.execute(
            "SELECT item_id, item_json, retrieved_at FROM archive_items WHERE root_id = ?", (root,)
        )
    }


def poll_options(item):
    """A poll lists its option IDs in parts; any other item has none."""
    return item.get("parts", []) if item and item.get("type") == "poll" else []


def archive_counts(root, items):
    item = items.get(root, (None, None))[0]
    options = set(poll_options(item))
    return {
        "saved_items": len(items),
        "comments": sum(value is not None and item_id != root and item_id not in options for item_id, (value, _) in items.items()),
        "unavailable": sum(value is None for value, _ in items.values()),
        "reported_descendants": item.get("descendants") if item else None,
    }


def _hn_url(item_id):
    return f"https://news.ycombinator.com/item?id={item_id}"


def _snapshot(conn, root):
    row = conn.execute("SELECT status, started_at, finished_at FROM archives WHERE root_id = ?", (root,)).fetchone()
    if row is None or row[0] != "complete":
        raise ValueError(f"Archive {root} is not complete")
    items = load_items(conn, root)
    nodes = {
        item_id: {"id": item_id, "hn_url": _hn_url(item_id), "retrieved_at": retrieved_at, "item": item, "replies": []}
        for item_id, (item, retrieved_at) in items.items()
    }
    root_node = nodes[root]
    option_ids = list(dict.fromkeys(poll_options(root_node["item"])))
    options = [nodes[item_id] for item_id in option_ids if item_id != root]
    visited = {root, *option_ids}
    queue = [root_node, *options]
    # A visited set also makes malformed repeated/cyclic edges finite; the raw
    # child lists remain unchanged under each node's item field.
    while queue:
        node = queue.pop()
        value = node["item"]
        for child in value.get("kids", []) if value else []:
            if child not in visited:
                visited.add(child)
                node["replies"].append(nodes[child])
        queue.extend(reversed(node["replies"]))
    return {
        "root_id": root,
        "status": row[0],
        "started_at": row[1],
        "finished_at": row[2],
        **archive_counts(root, items),
        "root": root_node,
        "poll_options": options,
    }


def _json_chunks(value):
    """Emit JSON iteratively so nesting is bounded only by available memory."""
    stack = [(False, value)]
    while stack:
        literal, value = stack.pop()
        if literal:
            yield value
        elif isinstance(value, dict):
            yield "{"
            stack.append((True, "}"))
            pairs = list(value.items())
            for index in range(len(pairs) - 1, -1, -1):
                key, child = pairs[index]
                stack.append((False, child))
                stack.append((True, ":"))
                stack.append((False, key))
                if index:
                    stack.append((True, ","))
        elif isinstance(value, list):
            yield "["
            stack.append((True, "]"))
            for index in range(len(value) - 1, -1, -1):
                stack.append((False, value[index]))
                if index:
                    stack.append((True, ","))
        else:
            yield json.dumps(value, ensure_ascii=False, allow_nan=False)
    yield "\n"


def _escape(text):
    # Include Obsidian's tags, block IDs, highlights, comments, and math.
    return re.sub(r"([\\`*_{}\[\]<>()#!|~^$=%+&\-.])", r"\\\1", text)


def _link(url):
    try:
        if urlsplit(url).scheme.lower() not in ("", "http", "https", "mailto"):
            return None
        target = urljoin("https://news.ycombinator.com/", url)
    except ValueError:
        return None
    return quote(target, safe="/:?#@!$&'*,;=+%-._~")


def _code(text):
    longest = max((len(run) for run in re.findall(r"`+", text)), default=0)
    fence = "`" * max(3, longest + 1)
    return f"\n\n{fence}\n{text.rstrip(chr(10))}\n{fence}\n\n"


class _MarkdownParser(HTMLParser):
    """Render only HN's markup: <p>, <i>, <pre><code>, and <a>; other tags keep their text."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.output = []
        self.code = None
        self.links = []

    def paragraph_break(self):
        if self.output and not self.output[-1].endswith("\n\n"):
            self.output.append("\n\n")

    def handle_starttag(self, tag, attrs):
        if tag == "pre":
            self.code = []
        elif self.code is not None:
            return
        elif tag == "p":
            self.paragraph_break()
        elif tag == "i":
            self.output.append("*")
        elif tag == "a":
            href = dict(attrs).get("href")
            target = _link(href) if href else None
            self.links.append(target)
            if target:
                self.output.append("[")

    def handle_endtag(self, tag):
        if tag == "pre" and self.code is not None:
            self.output.append(_code("".join(self.code)))
            self.code = None
        elif self.code is not None:
            return
        elif tag == "p":
            self.paragraph_break()
        elif tag == "i":
            self.output.append("*")
        elif tag == "a" and self.links:
            target = self.links.pop()
            if target:
                self.output.append(f"]({target})")

    def handle_data(self, data):
        if self.code is not None:
            self.code.append(data)
        else:
            self.output.append(_escape(data))


def html_to_markdown(text):
    parser = _MarkdownParser()
    parser.feed(text)
    parser.close()
    if parser.code is not None:
        parser.output.append(_code("".join(parser.code)))
    return "".join(parser.output).strip()


def _date(value):
    if value is None:
        return "unknown"
    try:
        return datetime.fromtimestamp(value, timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    except (OverflowError, OSError, ValueError):
        return f"{value} UTC epoch seconds"


def _body(item):
    if item is None:
        return "[unavailable]"
    markers = []
    if item.get("deleted"):
        markers.append("[deleted]")
    if item.get("dead"):
        markers.append("[flagged]")
    text = html_to_markdown(item.get("text", ""))
    if text:
        markers.append(text)
    elif not markers:
        markers.append("[no text]")
    return "\n\n".join(markers)


def _markdown_chunks(snapshot):
    root = snapshot["root"]
    item = root["item"] or {}
    title = _escape(item.get("title") or f"HN item {root['id']}")
    yield f"# [{title}]({root['hn_url']})\n\n"
    if item.get("url"):
        target = _link(item["url"])
        yield f"Article: [{_escape(item['url'])}]({target})\n\n" if target else f"Article: {_escape(item['url'])}\n\n"
    yield f"Author: {_escape(item.get('by', 'unknown'))}  \nPosted: {_date(item.get('time'))}  \n"
    reported = snapshot["reported_descendants"]
    yield f"Reported comments: {reported if reported is not None else 'unknown'}  \n"
    yield f"Archived: {_date(snapshot['finished_at'])}  \nObservation started: {_date(snapshot['started_at'])}  \n"
    yield f"Status: {snapshot['status']}; saved items: {snapshot['saved_items']}; comments: {snapshot['comments']}; unavailable: {snapshot['unavailable']}\n\n"
    if root["item"] is None or item.get("text") or item.get("deleted") or item.get("dead"):
        yield _body(root["item"]) + "\n\n"
    if snapshot["poll_options"]:
        yield "## Poll options\n\n"
        for option in snapshot["poll_options"]:
            value = option["item"] or {}
            yield f"- [Option {option['id']}]({option['hn_url']}) — votes: {value.get('score', 'unknown')}\n\n"
            for line in _body(option["item"]).splitlines():
                yield f"    {line}\n" if line else "\n"
            yield "\n"
    yield "## Comments\n\n"
    stack = [(node, 0) for node in reversed(root["replies"])]
    while stack:
        node, depth = stack.pop()
        value = node["item"] or {}
        indent = "    " * depth
        # The anchor belongs to this header paragraph, always outside body code.
        yield f"{indent}- **{_escape(value.get('by', 'unknown'))}** · [{_date(value.get('time'))}]({node['hn_url']}) ^c{node['id']}\n\n"
        for line in _body(node["item"]).splitlines():
            yield f"{indent}    {line}\n" if line else "\n"
        yield "\n"
        stack.extend((child, depth + 1) for child in reversed(node["replies"]))


def _atomic_write(path, chunks):
    try:
        # Exiting removes the temporary file unless os.replace() already moved it.
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", delete_on_close=False) as handle:
            handle.writelines(chunks)
            handle.close()
            os.replace(handle.name, path)
    except OSError as error:
        error.add_note(f"export path={path}")
        raise


def write_exports(conn, root, export_dir):
    """Replace each export atomically; reruns repair either file from SQLite."""
    snapshot = _snapshot(conn, root)
    directory = Path(export_dir)
    directory.mkdir(parents=True, exist_ok=True)
    json_path = directory / f"{root}.json"
    markdown_path = directory / f"{root}.md"
    _atomic_write(json_path, _json_chunks(snapshot))
    _atomic_write(markdown_path, _markdown_chunks(snapshot))
    return json_path, markdown_path
