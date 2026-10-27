from contextlib import redirect_stdout
from io import StringIO
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

from hn_search.archive import archive
from hn_search.archive_export import html_to_markdown, write_exports
from hn_search.catalog import commit_page, migrate_archives, open_catalog
from tests.helpers import HNOpener, NOW, post


class MarkdownTests(unittest.TestCase):
    def test_paragraphs_italics_links_entities_and_unicode(self):
        result = html_to_markdown('<p>雪 &amp; café &lt;tag&gt; &#39;ok&#39;</p><p><i>italic</i> <a href="https://example.com/a_(b)?x=1&amp;y=2">a &amp; b</a></p>')
        self.assertEqual(result, "雪 \\& café \\<tag\\> 'ok'\n\n*italic* [a \\& b](https://example.com/a_%28b%29?x=1&y=2)")
        self.assertEqual(html_to_markdown('The literal &amp;nbsp; is six characters. AT&amp;T'), r'The literal \&nbsp; is six characters\. AT\&T')
        # HN emits no other tags; any that appear keep their escaped text.
        self.assertEqual(html_to_markdown('<b>bold</b> <code>`x`</code><br>'), r'bold \`x\`')

    def test_literal_obsidian_and_markdown_syntax_is_escaped(self):
        result = html_to_markdown(r'[[x]] ![[image]] #tag ^c1 %%hidden%% ==bright== $math$ **bold** `tick` \ [x](url)')
        for literal in (r'\[\[x\]\]', r'\!\[\[image\]\]', r'\#tag', r'\^c1', r'\%\%hidden\%\%', r'\=\=bright\=\=', r'\$math\$', r'\*\*bold\*\*', r'\`tick\`', r'\\', r'\[x\]\(url\)'):
            self.assertIn(literal, result)

    def test_preformatted_code_preserves_text_and_backtick_runs(self):
        self.assertEqual(html_to_markdown('<pre><code>[[x]]\n\n```\n^c1\n</code></pre>'), '````\n[[x]]\n\n```\n^c1\n````')
        self.assertEqual(html_to_markdown('<pre>unclosed &amp; code'), '```\nunclosed & code\n```')

    def test_relative_links_and_source_html_cannot_create_active_markup(self):
        result = html_to_markdown('<a href="item?id=42">reply</a> <a href="javascript:evil()">bad</a> &lt;script&gt;literal&lt;/script&gt;')
        self.assertIn('[reply](https://news.ycombinator.com/item?id=42)', result)
        self.assertNotIn('javascript:', result)
        self.assertIn(r'\<script\>literal\</script\>', result)
        self.assertEqual(html_to_markdown('<a href="https://[broken">still readable</a>'), 'still readable')


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / 'catalog.sqlite3'
        self.exports = Path(self.directory.name) / 'exports'
        self.conn = open_catalog(self.path)
        self.addCleanup(self.conn.close)
        commit_page(self.conn, [post(1)])

    def seed(self, records, *, complete=True):
        migrate_archives(self.conn)
        with self.conn:
            self.conn.execute('INSERT INTO archives (root_id, started_at, finished_at) VALUES (1, ?, ?)', (NOW - 30, NOW if complete else None))
            self.conn.executemany('INSERT INTO archive_items VALUES (1, ?, ?, ?)',
                                  [(item_id, json.dumps(value, ensure_ascii=False), NOW - 15) for item_id, value in records.items()])

    def test_snapshot_source_values_order_and_markdown_anchors(self):
        records = {
            1: {'id': 1, 'title': '雪 [[Title]]', 'by': 'root', 'time': NOW - 100, 'url': 'https://example.com/a(b)', 'text': '<p>Root <i>text</i></p>', 'type': 'poll', 'parts': [6, 5], 'kids': [3, 2], 'descendants': 500},
            2: {'id': 2, 'by': 'literal#tag', 'time': NOW - 50, 'parent': 1, 'text': '<p>[[x]] ^c777 %%hidden%%</p><p>second</p>', 'extra': {'unicode': '雪', 'null': None}},
            3: {'id': 3, 'by': 'code-first', 'time': NOW - 60, 'kids': [4], 'text': '<pre><code>```\n^c999\n</code></pre>'},
            4: {'id': 4, 'deleted': True},
            5: None,
            6: {'id': 6, 'type': 'pollopt', 'text': 'Choice &amp; one', 'score': 73},
        }
        self.seed(records)
        paths = write_exports(self.conn, 1, self.exports)
        self.assertEqual(paths, (self.exports / '1.json', self.exports / '1.md'))
        snapshot = json.loads(paths[0].read_text())
        self.assertEqual(snapshot['root']['item'], records[1])
        self.assertEqual(snapshot['root']['retrieved_at'], NOW - 15)
        self.assertEqual((snapshot['started_at'], snapshot['finished_at']), (NOW - 30, NOW))
        self.assertEqual([node['id'] for node in snapshot['root']['replies']], [3, 2])
        self.assertEqual([node['id'] for node in snapshot['poll_options']], [6, 5])
        self.assertEqual(snapshot['root']['replies'][1]['item'], records[2])
        self.assertEqual((snapshot['comments'], snapshot['saved_items'], snapshot['unavailable']), (3, 6, 1))
        markdown = paths[1].read_text()
        self.assertTrue(markdown.startswith('# [雪 \\[\\[Title\\]\\]](https://news.ycombinator.com/item?id=1)'))
        self.assertIn('Article: [https://example\\.com/a\\(b\\)](https://example.com/a%28b%29)', markdown)
        self.assertIn('Root *text*', markdown)
        self.assertIn(r'Choice \& one', markdown)
        self.assertIn('votes: 73', markdown)
        self.assertLess(markdown.index('^c3'), markdown.index('^c4'))
        self.assertLess(markdown.index('^c4'), markdown.index('^c2'))
        self.assertIn('    - **unknown**', markdown)
        self.assertIn(r'\^c777', markdown)
        self.assertIn(r'\%\%hidden\%\%', markdown)
        # Generated comment IDs stay on the header paragraph, preceding body
        # fences even for code-first comments and placeholders.
        self.assertEqual(re.findall(r'^\s*- .* (?<!\\)\^c(\d+)$', markdown, re.M), ['3', '4', '2'])
        self.assertLess(markdown.index('^c3'), markdown.index('````'))

    def test_incomplete_archives_never_create_exports(self):
        self.seed({1: {'id': 1}}, complete=False)
        with self.assertRaisesRegex(ValueError, 'not complete'):
            write_exports(self.conn, 1, self.exports)
        self.assertFalse(self.exports.exists())

    def test_export_writes_and_renames_fail_independently_and_repair_without_requests(self):
        self.seed({1: {'id': 1, 'title': 'Saved root'}})
        self.exports.mkdir()
        for suffix in ('.json', '.md'):
            for operation in ('write', 'replace'):
                with self.subTest(suffix=suffix, operation=operation):
                    for name in ('1.json', '1.md'):
                        (self.exports / name).write_text('old')
                    target = self.exports / f'1{suffix}'
                    output = StringIO()
                    if operation == 'replace':
                        original = os.replace

                        def fail_replace(source, destination):
                            if destination == target:
                                raise OSError('rename failed')
                            return original(source, destination)

                        failure = patch('hn_search.archive_export.os.replace', side_effect=fail_replace)
                    else:
                        def fail_chunks(snapshot):
                            yield 'partial output'
                            raise OSError('write failed')

                        failure = patch('hn_search.archive_export.' + ('_json_chunks' if suffix == '.json' else '_markdown_chunks'), side_effect=fail_chunks)
                    with failure, redirect_stdout(output), self.assertRaises(OSError) as raised:
                        archive(self.conn, [1], self.exports, opener=HNOpener())
                    self.assertIn(f'export path={target}', raised.exception.__notes__)
                    self.assertEqual(output.getvalue(), '')
                    self.assertEqual(target.read_text(), 'old')
                    self.assertEqual(set(path.name for path in self.exports.iterdir()), {'1.json', '1.md'})
                    self.assertEqual(self.conn.execute('SELECT status FROM archives').fetchone()[0], 'complete')
                    with redirect_stdout(output):
                        archive(self.conn, [1], self.exports, opener=HNOpener())
                    self.assertEqual(json.loads((self.exports / '1.json').read_text())['root']['item']['title'], 'Saved root')
                    self.assertIn('reused=true', output.getvalue())

    def test_directory_failure_retains_complete_archive(self):
        self.seed({1: None})
        self.exports.write_text('not a directory')
        with redirect_stdout(StringIO()), self.assertRaises(OSError):
            archive(self.conn, [1], self.exports, opener=HNOpener())
        self.assertEqual(self.conn.execute('SELECT status FROM archives').fetchone()[0], 'complete')
        self.exports.unlink()
        with redirect_stdout(StringIO()):
            archive(self.conn, [1], self.exports, opener=HNOpener())
        self.assertIsNone(json.loads((self.exports / '1.json').read_text())['root']['item'])

    def test_deep_tree_exports_beyond_python_recursion_limit(self):
        depth = sys.getrecursionlimit() + 100
        records = {item_id: {'id': item_id, 'text': 'reply', 'kids': [item_id + 1] if item_id < depth else []} for item_id in range(1, depth + 1)}
        self.seed(records)
        json_path, markdown_path = write_exports(self.conn, 1, self.exports)
        content = json_path.read_text()
        self.assertEqual(content.count('"hn_url"'), depth)
        self.assertEqual(len(re.findall(r'^\s*- .* \^c\d+$', markdown_path.read_text(), re.M)), depth - 1)
        # Only the test decoder needs a higher limit; the exporter ran at the
        # normal limit and uses no recursion for construction or emission.
        previous = sys.getrecursionlimit()
        try:
            sys.setrecursionlimit(depth * 4)
            node = json.loads(content)['root']
            for item_id in range(1, depth):
                self.assertEqual(node['id'], item_id)
                node = node['replies'][0]
            self.assertEqual(node['id'], depth)
        finally:
            sys.setrecursionlimit(previous)

    def test_wide_tree_keeps_child_order_without_sampling(self):
        ids = list(range(1501, 1, -1))
        records = {1: {'id': 1, 'kids': ids}} | {item_id: {'id': item_id} for item_id in ids}
        self.seed(records)
        path, _ = write_exports(self.conn, 1, self.exports)
        snapshot = json.loads(path.read_text())
        self.assertEqual([node['id'] for node in snapshot['root']['replies']], ids)
        self.assertEqual(snapshot['comments'], 1500)


if __name__ == '__main__':
    unittest.main()
