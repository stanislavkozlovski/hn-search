import re
import unittest
from types import SimpleNamespace

from hn_search.research.render import comment_refs
from hn_search.research.threads import combine_verdicts, pack, split_story
from tests.research_helpers import node, snapshot


class ThreadTests(unittest.TestCase):
    def test_poll_option_replies_keep_their_parent_and_pack_as_root_subtrees(self):
        replies = [node(cid, parent=2, text="Reply. " * 60) for cid in (20, 21, 22, 23)]
        replies[0]["replies"] = [node(200, parent=20)]
        tree = snapshot()
        tree["root"]["item"]["type"] = "poll"
        tree["poll_options"] = [node(2, type="pollopt", poll=1, score=4,
                                     text="First choice", replies=replies)]
        whole, = split_story(tree, 10000)
        self.assertIn('<comment id="20" parent="2"', whole.text)
        self.assertIn('<comment id="200" parent="20"', whole.text)
        parts = split_story(tree, 400)
        self.assertGreater(len(parts), 1)
        self.assertLess(len(parts), 5)
        self.assertEqual([cid for part in parts for cid in part.comment_ids], [1001, 20, 200, 21, 22, 23])
        self.assertTrue(all(part.size <= 400 for part in parts))

    def test_prompt_markers_only_identify_citable_source_comments(self):
        missing = node(1004)
        missing["item"] = None
        tree = snapshot(replies=[node(1001), node(1002, deleted=True),
                                 node(1003, type="story"), missing])
        whole, = split_story(tree, 10000)
        self.assertEqual(whole.text.count("Source citation:"), 1)
        self.assertIn("Source citation: [c1001]", whole.text)
        for cid in (1002, 1003, 1004):
            self.assertNotIn(f"[c{cid}]", whole.text)
        # Validation allows, and Markdown links, exactly the comments the prompt marks.
        self.assertEqual({int(cid) for cid in re.findall(r"\[c(\d+)\]", whole.text)}, set(comment_refs(tree)))

    def test_top_level_and_nested_parts_keep_context_and_exact_coverage(self):
        children = [node(30 + i, parent=20, text="Reply. " * 35) for i in range(6)]
        tree = snapshot(replies=[node(10, text="Opening. " * 8,
                                     replies=[node(20, parent=10, text="Parent. " * 8, replies=children)]),
                                 node(40, text="Other top level. " * 20)])
        parts = split_story(tree, 260)
        self.assertGreater(len(parts), 2)
        self.assertEqual([cid for unit in parts for cid in unit.comment_ids], [10, 20, *range(30, 36), 40])
        self.assertTrue(all(unit.size <= 260 for unit in parts))
        later = next(unit for unit in parts if 33 in unit.comment_ids)
        self.assertIn("<context>", later.text)
        self.assertIn('<comment id="10"', later.text)
        self.assertIn('<comment id="20"', later.text)
        self.assertIn("#", later.input_key)
        whole = split_story(tree, 10000)
        self.assertEqual(len(whole), 1)
        self.assertEqual(whole[0].part, 0)
        self.assertEqual(whole[0].comment_ids, (10, 20, *range(30, 36), 40))
        self.assertEqual(re.findall(r'<comment id="(\d+)"', whole[0].text),
                         ['10', '20', *map(str, range(30, 36)), '40'])
        self.assertTrue(whole[0].text.startswith('<hn_story id="1" part="0"'))
        self.assertTrue(whole[0].text.endswith('</hn_story>'))
        self.assertIn('<comment id="20" parent="10"', whole[0].text)
        self.assertNotIn('<context>', whole[0].text)
        self.assertNotIn("#", whole[0].input_key)
        self.assertEqual(split_story(tree, whole[0].size)[0].part, 0)

    def test_largest_first_first_fit_and_twenty_unit_cap(self):
        units = [SimpleNamespace(size=size, story_id=sid, part=0)
                 for sid, size in enumerate([3, 7, 4, 6], 1)]
        calls = pack(units, 10)
        self.assertEqual([[unit.story_id for unit in call] for call in calls], [[2, 1], [4, 3]])
        tiny = [SimpleNamespace(size=1, story_id=sid, part=0) for sid in range(21)]
        self.assertEqual([len(call) for call in pack(tiny, 1000)], [20, 1])
        tied = pack([SimpleNamespace(size=5, story_id=2, part=1),
                     SimpleNamespace(size=5, story_id=1, part=2)], 5)
        self.assertEqual(tied[0][0].story_id, 1)

    def test_verdicts_combine_without_losing_citations(self):
        values = [{"verdict": verdict, "reasons": f"Part {index} [c{index}]",
                   "comment_ids": [index]} for index, verdict in enumerate(
                       ["irrelevant", "uncertain", "relevant"], 1)]
        result = combine_verdicts(values)
        self.assertEqual(result["verdict"], "relevant")
        self.assertEqual(result["comment_ids"], [1, 2, 3])
        self.assertIn("[c2]", result["reasons"])
        self.assertEqual(combine_verdicts(values[:2])["verdict"], "uncertain")
        self.assertEqual(combine_verdicts(values[:1])["verdict"], "irrelevant")
