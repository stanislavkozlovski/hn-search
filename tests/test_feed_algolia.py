from urllib.error import URLError
from urllib.parse import parse_qs, urlsplit

from hn_search.feed.algolia import fetch_window
from tests.feed_helpers import NOW, FeedCase, RecordingOpener, hit, window


class AlgoliaTests(FeedCase):
    def test_exact_query_timeout_and_nullable_url(self):
        missing = hit(50237680)
        del missing["url"]
        opener = RecordingOpener(window(missing, hit(2, url=None), hit(3, url="")))
        stories = fetch_window(NOW, opener=opener)
        request = opener.requests[0]
        self.assertEqual(request["timeout"], 30)
        self.assertEqual(parse_qs(urlsplit(request["url"]).query), {
            "tags": ["story"], "numericFilters": [f"created_at_i>{NOW - 36000},points>=5"],
            "hitsPerPage": ["1000"],
        })
        self.assertEqual([story.url for story in stories], [None, None, None])

    def test_invalid_window_writes_no_story_or_lens_and_makes_no_other_request(self):
        invalid = [None, {}, {"hits": {}, "nbHits": 0}, {"hits": [], "nbHits": 1},
                   {"hits": [hit(i + 1) for i in range(1000)], "nbHits": 1001},
                   window(hit(), hit()), window("invalid")]
        for key, value in [("objectID", 1), ("objectID", "0"), ("objectID", "x"),
                           ("title", ""), ("title", None), ("points", 4), ("points", True),
                           ("points", 6.0), ("created_at_i", NOW - 36000),
                           ("created_at_i", "yesterday"), ("url", [])]:
            record = hit()
            record[key] = value
            invalid.append(window(record))
        for body in invalid:
            with self.subTest(body=str(body)[:80]), self.assertRaises(ValueError):
                fetch_window(NOW, opener=RecordingOpener(body))
        with self.assertRaises(URLError):
            self.run_feed(URLError("offline"))
        from hn_search.feed.store import open_feed
        with open_feed(self.path) as conn:
            self.assertEqual(conn.execute("SELECT count(*) FROM stories").fetchone()[0], 0)
            self.assertEqual(conn.execute("SELECT count(*) FROM lenses").fetchone()[0], 0)
