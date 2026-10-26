import re
import unittest
from urllib.error import HTTPError, URLError

from hn_search.clickhouse import PAGE_SIZE, fetch_page, max_id
from tests.helpers import NOW, ScriptedOpener, post, result, row


class ClickHouseTests(unittest.TestCase):
    def test_history_query_uses_latest_versions_typed_bounds_and_only_throw_settings(self):
        record = row(42, title="<b>雪 & café</b>", url="", text="__exception__")
        opener = ScriptedOpener([record])
        self.assertEqual(fetch_page(40, through_id=50, opener=opener), [post(**record)])
        request, = opener.requests
        sql = request["query"]
        self.assertIn("FROM hackernews_history FINAL\nWHERE", sql)
        self.assertIn("id >= {next_id:UInt32}", sql)
        self.assertIn("id <= {through_id:UInt32}", sql)
        self.assertIn("type IN ('story', 'poll', 'job')", sql)
        for predicate in ("parent = 0", "deleted = 0", "descendants >= 5"):
            self.assertIn(predicate, sql)
        self.assertIn("ORDER BY id LIMIT 10000", sql)
        self.assertTrue(sql.endswith("FORMAT JSON"))
        for excluded in ("PREWHERE", "dead", "kids", "update_time", "SELECT *"):
            self.assertNotIn(excluded, sql)
        self.assertEqual(
            re.findall(r"(\w+)\s*=\s*'(\w+)'", sql.split("SETTINGS")[1]),
            [
                ("result_overflow_mode", "throw"),
                ("timeout_overflow_mode", "throw"),
                ("read_overflow_mode", "throw"),
            ],
        )
        self.assertEqual(
            {key: value for key, value in request.items() if key != "query"},
            {"user": "play", "wait_end_of_query": "1", "param_next_id": "40",
             "param_through_id": "50"},
        )
        self.assertEqual(opener.timeouts, [90])

    def test_reported_total_qualifies_even_with_two_direct_children(self):
        opener = ScriptedOpener([row(1, kids=[2, 3])])
        self.assertEqual(fetch_page(1, through_id=10, opener=opener), [post(1)])

    def test_daily_window_is_inclusive_below_exclusive_above_and_uses_creation_time(self):
        start = NOW - 432_000
        opener = ScriptedOpener([row(1, created_at=start), row(2, created_at=NOW - 1)])
        posts = fetch_page(1, window_start=start, window_end=NOW, opener=opener)
        self.assertEqual([p.created_at for p in posts], [start, NOW - 1])
        request, = opener.requests
        self.assertNotIn("param_through_id", request)
        self.assertEqual(request["param_window_start"], str(start))
        self.assertEqual(request["param_window_end"], str(NOW))
        self.assertIn("time >= toDateTime({window_start:UInt32}, 'UTC')", request["query"])
        self.assertIn("time < toDateTime({window_end:UInt32}, 'UTC')", request["query"])
        self.assertNotIn("update_time", request["query"])
        for timestamp in (start - 1, NOW):
            with self.subTest(timestamp=timestamp), self.assertRaises(ValueError):
                fetch_page(1, window_start=start, window_end=NOW,
                           opener=ScriptedOpener([row(created_at=timestamp)]))

    def test_empty_page_is_valid(self):
        self.assertEqual(fetch_page(1, through_id=100, opener=ScriptedOpener([])), [])

    def test_invalid_and_incomplete_responses_never_become_empty_pages(self):
        valid = result([row()])
        invalid = [
            b"", b"not JSON", b"\xff", valid[:-3], b"[]", b"null",
            valid + b"\r\n__exception__\r\nquery failed\r\n__exception__\r\n",
            b'{"data": [], "rows": 0, "exception": "quota exceeded"}',
            b'{"data": [], "rows": 0, "__exception__": "query failed"}',
            b'{"data": []}', b'{"rows": 0}', b'{"data": {}, "rows": 0}',
            b'{"data": [], "rows": true}', b'{"data": [], "rows": -1}',
            b'{"data": [], "rows": "0"}', b'{"data": [null], "rows": 1}',
            result([row()], rows=2),
        ]
        for body in invalid:
            with self.subTest(body=body[:80]), self.assertRaises((ValueError, UnicodeError)):
                fetch_page(1, through_id=100, opener=ScriptedOpener(body))

    def test_required_fields_are_validated_before_returning_any_posts(self):
        invalid = {
            "id": (None, 0, -1, True, "1", 1.5),
            "created_at": (None, -1, False, "1", 1.5),
            "descendants": (None, 4, True, "5", 5.5),
            "title": (None, [], 1), "url": (None, [], 1), "text": (None, [], 1),
        }
        for field, values in invalid.items():
            for value in values:
                with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                    fetch_page(1, through_id=100,
                               opener=ScriptedOpener([row(1), row(2, **{field: value})]))
            record = row()
            del record[field]
            with self.subTest(missing=field), self.assertRaises(ValueError):
                fetch_page(1, through_id=100, opener=ScriptedOpener([record]))

    def test_unordered_duplicate_and_out_of_range_ids_are_rejected(self):
        for records in ([row(4), row(3)], [row(3), row(3)], [row(1)], [row(11)]):
            with self.subTest(records=records), self.assertRaises(ValueError):
                fetch_page(2, through_id=10, opener=ScriptedOpener(records))

    def test_oversized_page_is_rejected(self):
        opener = ScriptedOpener([row(i + 1) for i in range(PAGE_SIZE + 1)])
        with self.assertRaises(ValueError):
            fetch_page(1, through_id=20_000, opener=opener)

    def test_http_transport_quota_timeout_and_overflow_failures_propagate_without_retry(self):
        errors = [
            URLError("connection interrupted"), TimeoutError("timeout"),
            HTTPError("https://play.clickhouse.com/", 500, "READONLY", {}, None),
            HTTPError("https://play.clickhouse.com/", 429, "quota exceeded", {}, None),
            HTTPError("https://play.clickhouse.com/", 500, "overflow", {}, None),
        ]
        for error in errors:
            opener = ScriptedOpener(error)
            with self.subTest(error=error), self.assertRaises(type(error)) as raised:
                fetch_page(1, through_id=100, opener=opener)
            self.assertIs(raised.exception, error)
            self.assertEqual(len(opener.requests), 1)

    def test_max_id_does_not_need_final_and_validates_the_bound(self):
        opener = ScriptedOpener([{"max_id": 50_235_582}])
        self.assertEqual(max_id(opener=opener), 50_235_582)
        self.assertIn("SELECT max(id) AS max_id FROM hackernews_history", opener.requests[0]["query"])
        self.assertNotIn("FINAL", opener.requests[0]["query"])
        self.assertEqual(max_id(opener=ScriptedOpener([{"max_id": 0}])), 0)
        for records in ([], [{"max_id": -1}], [{"max_id": True}], [{"max_id": "42"}],
                        [{}], [{"max_id": 1}, {"max_id": 2}]):
            with self.subTest(records=records), self.assertRaises(ValueError):
                max_id(opener=ScriptedOpener(records))

    def test_missing_or_mixed_modes_fail_before_http(self):
        for bounds in ({}, {"window_start": NOW - 1}, {"window_end": NOW},
                       {"through_id": 10, "window_start": 1, "window_end": 2}):
            opener = ScriptedOpener()
            with self.subTest(bounds=bounds), self.assertRaises(ValueError):
                fetch_page(1, opener=opener, **bounds)
            self.assertEqual(opener.requests, [])
