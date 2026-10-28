import re
import unittest

from hn_search.research.render import analysis_md, html_to_markdown, report_md, thread_md
from tests.research_helpers import node, snapshot


class RenderTests(unittest.TestCase):
    def test_html_escaping_and_fences(self):
        source = '[[x]] #tag<p># heading ^c1 %%c%% ==hi== $x$ &lt;b&gt;<p><i>fine</i> <b>bold</b><pre><code>one ' + chr(96) * 3 + ' two</code></pre>'
        result = html_to_markdown(source)
        for text in [r"\[\[x\]\]", r"\#tag", r"\# heading", r"\^c1", r"\%\%c\%\%", r"\=\=hi\=\=", r"\$x\$", r"\<b\>"]:
            self.assertIn(text, result)
        self.assertIn("*fine* bold", result)
        self.assertIn(chr(96) * 4 + "\none " + chr(96) * 3 + " two\n" + chr(96) * 4, result)
        self.assertEqual(html_to_markdown('<a href="https://a.test/x y&gt;">link</a>'),
                         "[link](<https://a.test/x%20y%3E>)")
        self.assertEqual(html_to_markdown("1. one\n- two\n+ three"),
                         "1\\. one\n\\- two\n\\+ three")
        self.assertEqual(html_to_markdown("<b>[[x]]</b>", escape=False), "[[x]]")

    def test_first_paragraph_anchors_placeholders_and_relative_citations(self):
        tree = snapshot(replies=[node(11, text="First<p>Second"),
                                 node(12, text="<pre><code>code</code></pre>"),
                                 node(13, text="", deleted=True), node(14, text="", dead=True)])
        tree["root"]["replies"].append({"id": 15, "hn_url": "https://news.ycombinator.com/item?id=15",
                                        "item": None, "retrieved_at": 1, "replies": []})
        text = thread_md(tree)
        self.assertIn("  First ^c11\n\n  Second", text)
        self.assertRegex(text, r"- \*\*user12\*\*.* \^c12\n\n  ")
        for marker in ("[deleted]", "[flagged]", "[unavailable]"):
            self.assertIn(marker, text)
        lists = {field: ["A claim [c11]"] for field in (
            "arguments", "counterarguments", "assumptions", "conditions", "lived_experiences", "unresolved_disagreements")}
        descriptions = [{"description": "Description [[literal]]", "tags": ["home"]}]
        verdict = {"reasons": "Yes", "comment_ids": [11]}
        analysis = analysis_md(tree, descriptions, verdict, [lists, lists])
        self.assertIn("[[./thread#^c11|user11]]", analysis)
        self.assertLess(analysis.index("## Part 1"), analysis.index("## Part 2"))
        self.assertIn("### Arguments", analysis.splitlines())
        report = report_md("Question?", ["rent"], {}, [{"snapshot": tree, "descriptions": descriptions}],
                           lists, [(1, "Story", "relevant", ""), (2, "Other", "uncertain", "Unsure")])
        self.assertIn("[[./stories/1/thread#^c11|user11]]", report)
        self.assertIn("## Arguments", report.splitlines())
        self.assertIn("[[./stories/1/analysis|", report)
        self.assertIn("https://news.ycombinator.com/item?id=2", report)
        self.assertTrue(all(link.startswith("./") for link in re.findall(r"(?<!\\)\[\[([^\]]+)", report)))
