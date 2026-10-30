"""Convert HN's small HTML vocabulary using the caller's rendering policies."""

from html.parser import HTMLParser
import re


def code_block(text):
    longest = max((len(run) for run in re.findall(r"`+", text)), default=0)
    fence = "`" * max(3, longest + 1)
    return f"\n\n{fence}\n{text.rstrip(chr(10))}\n{fence}\n\n"


class _MarkdownParser(HTMLParser):
    def __init__(self, escape_text, link_target):
        super().__init__(convert_charrefs=True)
        self.escape_text = escape_text
        self.link_target = link_target
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
            target = self.link_target(href) if href else None
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
            self.output.append(self.escape_text(data) if self.escape_text else data)


def html_to_markdown(source, *, escape_text, link_target):
    """Escape text with a callback (or None); link_target returns a URL or None."""
    parser = _MarkdownParser(escape_text, link_target)
    parser.feed(source)
    parser.close()
    if parser.code is not None:
        parser.output.append(code_block("".join(parser.code)))
    return "".join(parser.output).strip()
