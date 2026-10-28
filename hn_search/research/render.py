"""Render archived HN markup and validated citations as portable run folders."""

import html
import re
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import quote, urljoin, urlsplit


CITATION = re.compile(r"\[c([0-9]+)\]")
FIELDS = ("arguments", "counterarguments", "assumptions", "conditions",
          "lived_experiences", "unresolved_disagreements")


def escape_text(text):
    text = re.sub(r"([\\\x60*_\[\]<>#^|$%=~])", r"\\\1", text)
    text = re.sub(r"(?m)^(\s*)([-+])", r"\1\\\2", text)
    return re.sub(r"(?m)^(\s*\d+)\.", r"\1\\.", text)


def safe_url(url):
    try:
        if urlsplit(url).scheme.lower() not in ("", "http", "https", "mailto"):
            return None
        return quote(urljoin("https://news.ycombinator.com/", html.unescape(url)),
                     safe="/:?#@!$&'*,;=+%-._~")
    except ValueError:
        return None


def code_block(text):
    longest = max((len(run) for run in re.findall(r"\x60+", text)), default=0)
    fence = chr(96) * max(3, longest + 1)
    return f"\n\n{fence}\n{text.rstrip(chr(10))}\n{fence}\n\n"


class _HTML(HTMLParser):
    def __init__(self, escape):
        super().__init__(convert_charrefs=True)
        self.escape = escape
        self.output = []
        self.code = None
        self.links = []

    def paragraph(self):
        if self.output and not self.output[-1].endswith("\n\n"):
            self.output.append("\n\n")

    def handle_starttag(self, tag, attrs):
        if tag == "pre":
            self.code = []
        elif self.code is not None:
            return
        elif tag == "p":
            self.paragraph()
        elif tag == "i":
            self.output.append("*")
        elif tag == "a":
            href = dict(attrs).get("href")
            target = safe_url(href) if href else None
            self.links.append(target)
            if target:
                self.output.append("[")

    def handle_endtag(self, tag):
        if tag == "pre" and self.code is not None:
            self.output.append(code_block("".join(self.code)))
            self.code = None
        elif self.code is not None:
            return
        elif tag == "p":
            self.paragraph()
        elif tag == "i":
            self.output.append("*")
        elif tag == "a" and self.links:
            target = self.links.pop()
            if target:
                self.output.append(f"](<{target}>)")

    def handle_data(self, data):
        if self.code is not None:
            self.code.append(data)
        else:
            self.output.append(escape_text(data) if self.escape else data)


def html_to_markdown(source, escape=True):
    parser = _HTML(escape)
    parser.feed(source)
    parser.close()
    if parser.code is not None:
        parser.output.append(code_block("".join(parser.code)))
    return "".join(parser.output).strip()


def date(value):
    if value is None:
        return "unknown"
    try:
        return datetime.fromtimestamp(value, timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    except (ValueError, OSError, OverflowError):
        return f"{value} UTC epoch seconds"


def body(item, *, escape=True):
    if item is None:
        return "[unavailable]"
    markers = []
    if item.get("deleted"):
        markers.append("[deleted]")
    if item.get("dead"):
        markers.append("[flagged]")
    text = html_to_markdown(item.get("text", ""), escape=escape)
    return "\n\n".join(markers + ([text] if text else [])) or "[no text]"


def walk_comments(snapshot):
    roots = [(node, 0, snapshot["root_id"]) for node in snapshot["root"]["replies"]]
    for option in snapshot.get("poll_options", []):
        roots.extend((node, 0, option["id"]) for node in option["replies"])
    stack = list(reversed(roots))
    while stack:
        node, depth, parent = stack.pop()
        yield node, depth, parent
        stack.extend((child, depth + 1, node["id"]) for child in reversed(node["replies"]))


def comment_refs(snapshot):
    return {node["id"]: (snapshot["root_id"], node["item"].get("by", "unknown"))
            for node, _, _ in walk_comments(snapshot)
            if node["item"] is not None and node["item"].get("type") == "comment"
            and not node["item"].get("deleted")}


def render_citations(text, refs, *, report=False):
    pieces = []
    start = 0
    for match in CITATION.finditer(text):
        pieces.append(escape_text(text[start:match.start()]))
        comment_id = int(match.group(1))
        story_id, author = refs[comment_id]
        target = f"./stories/{story_id}/thread" if report else "./thread"
        pieces.append(f"[[{target}#^c{comment_id}|{escape_text(author)}]]")
        start = match.end()
    pieces.append(escape_text(text[start:]))
    return "".join(pieces)


def thread_md(snapshot):
    root = snapshot["root"]
    item = root["item"] or {}
    title = escape_text(item.get("title") or f"HN item {root['id']}")
    lines = [f"# [{title}]({root['hn_url']})", ""]
    if item.get("url"):
        url = safe_url(item["url"])
        lines.extend([f"Article: [{escape_text(item['url'])}](<{url}>)" if url
                      else f"Article: {escape_text(item['url'])}", ""])
    lines.extend([
        f"{escape_text(item.get('by', 'unknown'))} · {date(item.get('time'))} · "
        f"{snapshot.get('reported_descendants', 'unknown')} reported comments · archived {date(snapshot['finished_at'])}",
        f"Observation: {date(snapshot['started_at'])} → {date(snapshot['finished_at'])}", "",
    ])
    if root["item"] is None or item.get("text") or item.get("deleted") or item.get("dead"):
        lines.extend([body(root["item"]), ""])
    if snapshot.get("poll_options"):
        lines.extend(["## Poll options", ""])
        for option in snapshot["poll_options"]:
            value = option["item"] or {}
            lines.extend([f"- {body(option['item'])} · {value.get('score', 'unknown')} votes", ""])
    lines.extend(["## Comments", ""])
    for node, depth, _ in walk_comments(snapshot):
        value = node["item"] or {}
        indent = "  " * depth
        content = body(node["item"])
        paragraphs = content.split("\n\n")
        first = paragraphs.pop(0)
        header = (f"- **{escape_text(value.get('by', 'unknown'))}** · "
                  f"[{date(value.get('time'))}]({node['hn_url']})")
        if first.startswith(chr(96) * 3):
            paragraphs.insert(0, first)
            lines.append(indent + header + f" ^c{node['id']}")
        else:
            lines.append(indent + header)
            first_lines = first.splitlines() or [""]
            lines.extend(indent + "  " + line for line in first_lines[:-1])
            lines.append(indent + "  " + first_lines[-1] + f" ^c{node['id']}")
        for paragraph in paragraphs:
            lines.append("")
            lines.extend(indent + "  " + line for line in paragraph.splitlines())
        lines.append("")
    return "\n".join(lines) + "\n"


def analysis_lists(results, refs, *, report=False):
    lines = []
    heading = "### " if len(results) > 1 else "## "
    for index, result in enumerate(results, 1):
        if len(results) > 1:
            lines.extend([f"## Part {index}", ""])
        for field in FIELDS:
            lines.extend([heading + field.replace("_", " ").capitalize(), ""])
            lines.extend("- " + render_citations(item, refs, report=report)
                         for item in result[field])
            lines.append("")
    return lines


def analysis_md(snapshot, descriptions, verdict, analyses):
    item = snapshot["root"]["item"] or {}
    story_id = snapshot["root_id"]
    refs = comment_refs(snapshot)
    lines = [f"# [{escape_text(item.get('title', str(story_id)))}](https://news.ycombinator.com/item?id={story_id})",
             "", "[[./thread|Discussion]]", "", "## Description", ""]
    for index, description in enumerate(descriptions, 1):
        if len(descriptions) > 1:
            lines.append(f"### Part {index}")
        lines.extend([render_citations(description["description"], refs),
                      "Tags: " + escape_text(", ".join(description["tags"])), ""])
    lines.extend(["## Relevance", "", render_citations(
        verdict["reasons"] + " " + " ".join(f"[c{cid}]" for cid in verdict["comment_ids"]), refs), ""])
    lines.extend(analysis_lists(analyses, refs))
    return "\n".join(lines).rstrip() + "\n"


def report_md(question, keywords, settings, stories, synthesis, coverage):
    refs = {}
    for story in stories:
        refs.update(comment_refs(story["snapshot"]))
    setting_text = " · ".join(f"{stage}: {value['model']} {value['effort']}" for stage, value in settings.items())
    lines = ["# " + escape_text(question), "", "Keywords: " + escape_text(", ".join(keywords))
             + " · " + escape_text(setting_text), ""]
    if synthesis is not None:
        lines.extend(analysis_lists([synthesis], refs, report=True))
    if stories:
        lines.extend(["## Thread index", ""])
        for story in stories:
            snapshot = story["snapshot"]
            story_id = snapshot["root_id"]
            title = escape_text((snapshot["root"]["item"] or {}).get("title", str(story_id)))
            descriptions = " ".join(
                (f"Part {index}: " if len(story["descriptions"]) > 1 else "")
                + render_citations(part["description"], refs, report=True)
                for index, part in enumerate(story["descriptions"], 1))
            lines.append(f"- [[./stories/{story_id}/analysis|{title}]] · "
                         f"[[./stories/{story_id}/thread|thread]] · "
                         f"[HN](https://news.ycombinator.com/item?id={story_id}) — {descriptions}")
        lines.append("")
    lines.extend(["## Coverage", "", f"Matched: {len(coverage)} · relevant: {len(stories)}", ""])
    for status in ("not_downloaded", "unavailable", "uncertain", "irrelevant"):
        rows = [row for row in coverage if row[2] == status]
        lines.extend(["### " + status.replace("_", " "), ""])
        for story_id, title, _, reason in rows:
            lines.append(f"- [{escape_text(title)}](https://news.ycombinator.com/item?id={story_id}) — "
                         + escape_text(reason))
        if not rows:
            lines.append("None.")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"
