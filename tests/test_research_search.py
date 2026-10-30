import tempfile
import unittest
from pathlib import Path

from hn_search.catalog import commit_page, open_catalog
from hn_search.clickhouse import Post
from hn_search.research.search import gate_lines, normalize, search


class SearchTests(unittest.TestCase):
    def test_matching_and_top_three(self):
        cases = [
            ("super-renting", "", "", 7),
            ("Swiss homes", "https://example.org/zurich-switzerland-renting-homes", "", 9),
            ("Rent to own", "", "", 6), ("Rent vs. buy", "", "", 8),
            ("Current parenting", "", "", 20),
            ("test", "https://example.org/buy-vs-rent", "", 8),
            ("don't", "", "", 5), ("test", "", "don&#x27;t", 5),
            ("rent", "", "", 8), ("rent", "", "", 9),
        ]
        with tempfile.TemporaryDirectory() as directory:
            conn = open_catalog(Path(directory) / "catalog.db")
            self.addCleanup(conn.close)
            commit_page(conn, [Post(index, title, url, text, 1, count)
                               for index, (title, url, text, count) in enumerate(cases, 1)])
            result = search(conn, ["renting", "rent-to-own", "rent", "don t"])
            self.assertEqual(result.by_keyword["renting"], [1, 2])
            self.assertEqual(result.by_keyword["rent to own"], [3])
            self.assertEqual(result.by_keyword["rent"], [3, 4, 6, 9, 10])
            self.assertEqual(result.by_keyword["don t"], [7, 8])
            lines = gate_lines(result, room=1000)
            rent = [line for line in lines if line.startswith("  rent     ")][0]
            self.assertIn("10", rent)
            top = lines[lines.index(rent):lines.index(rent) + 3]
            self.assertIn("         4", top[1])
            self.assertIn("         6", top[2])
            self.assertNotIn(5, result.posts)
            self.assertEqual(normalize("ÉTUDE—don&#x27;t"), "étude don t")
