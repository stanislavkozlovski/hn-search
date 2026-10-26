from contextlib import closing, redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch
from urllib.error import URLError

from hn_search.__main__ import main
from hn_search.catalog import commit_page, open_catalog
from hn_search.clickhouse import PAGE_SIZE
from hn_search.collect import collect_daily, collect_history
from tests.helpers import NOW, ScriptedOpener, post, row, start_history


ROOT = Path(__file__).resolve().parents[1]


class CollectionTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "catalog.sqlite3"
        self.conn = open_catalog(self.path)
        self.addCleanup(lambda: self.conn.close())

    def run_quietly(self, function, **kwargs):
        output = StringIO()
        with redirect_stdout(output):
            function(self.conn, **kwargs)
        return output.getvalue().splitlines()

    def progress(self):
        return self.conn.execute("SELECT * FROM collection_progress").fetchall()

    def test_full_page_advances_past_last_id_and_empty_page_completes_retained_range(self):
        records = [row(i * 10) for i in range(1, PAGE_SIZE + 1)]
        opener = ScriptedOpener([{"max_id": 100_010}], records, [])
        lines = self.run_quietly(collect_history, opener=opener)
        self.assertEqual(opener.requests[1]["param_next_id"], "1")
        self.assertEqual(opener.requests[2]["param_next_id"], "100001")
        self.assertEqual(self.progress(), [(100_011, 1, 100_010)])
        self.assertEqual(len(lines), 2)
        self.assertIn("next_id=100001 complete=false saved_posts=10000", lines[0])
        self.assertIn("next_id=100011 complete=true saved_posts=10000", lines[1])

    def test_history_resumes_saved_range_instead_of_looking_up_a_new_maximum(self):
        start_history(self.conn, next_id=8, through_id=25)
        opener = ScriptedOpener([row(9)])
        self.run_quietly(collect_history, opener=opener)
        request, = opener.requests
        self.assertEqual(request["param_next_id"], "8")
        self.assertEqual(request["param_through_id"], "25")
        self.assertEqual(self.progress(), [(26, 1, 25)])

    def test_completed_history_only_prints_saved_progress(self):
        start_history(self.conn, next_id=26, complete=True, through_id=25)
        commit_page(self.conn, [post(1)])
        opener = ScriptedOpener()
        lines = self.run_quietly(collect_history, opener=opener)
        self.assertEqual(opener.requests, [])
        self.assertEqual(self.progress(), [(26, 1, 25)])
        self.assertEqual(lines, [
            "historical source=play.clickhouse.com/hackernews_history "
            "range=1..25 next_id=26 complete=true saved_posts=1"
        ])

    def test_bound_is_durable_even_when_first_page_fails(self):
        opener = ScriptedOpener([{"max_id": 20}], URLError("network down"))
        with self.assertRaises(URLError):
            self.run_quietly(collect_history, opener=opener)
        self.conn.close()
        self.conn = open_catalog(self.path)
        self.assertEqual(self.progress(), [(1, 0, 20)])
        self.assertEqual(self.conn.execute("SELECT count(*) FROM posts").fetchone()[0], 0)

    def test_failed_bound_lookup_does_not_initialize_progress(self):
        with self.assertRaises(URLError):
            self.run_quietly(collect_history, opener=ScriptedOpener(URLError("offline")))
        self.assertEqual(self.progress(), [])

    def test_empty_mirror_range_finishes(self):
        self.run_quietly(collect_history, opener=ScriptedOpener([{"max_id": 0}], []))
        self.assertEqual(self.progress(), [(1, 1, 0)])

    def test_invalid_second_page_leaves_first_page_and_cursor_intact(self):
        records = [row(i) for i in range(1, PAGE_SIZE + 1)]
        for invalid in (b'{"data": [', [row(10_001), row(10_002, text=None)]):
            with self.subTest(invalid=str(invalid)[:80]):
                # Each subcase replays the same unfinished second page.
                if not self.progress():
                    start_history(self.conn, through_id=20_000)
                    commit_page(self.conn, [post(**record) for record in records], next_id=10_001)
                output = StringIO()
                with redirect_stdout(output), self.assertRaises(ValueError):
                    collect_history(self.conn, opener=ScriptedOpener(invalid))
                self.assertEqual(output.getvalue(), "")
                self.assertEqual(self.progress(), [(10_001, 0, 20_000)])
                self.assertEqual(self.conn.execute("SELECT count(*) FROM posts").fetchone()[0], PAGE_SIZE)

    def test_no_progress_is_printed_for_a_failed_page_commit(self):
        output = StringIO()
        opener = ScriptedOpener([{"max_id": 20}], [row(1)])
        with patch("hn_search.collect.catalog.commit_page", side_effect=sqlite3.OperationalError("disk full")):
            with redirect_stdout(output), self.assertRaises(sqlite3.OperationalError):
                collect_history(self.conn, opener=opener)
        self.assertEqual(output.getvalue(), "")
        self.assertEqual(self.progress(), [(1, 0, 20)])

    def test_daily_clock_is_read_once_and_all_pages_share_the_frozen_window(self):
        start_history(self.conn, next_id=101, complete=True)
        records = [row(i) for i in range(1, PAGE_SIZE + 1)]
        clock = Mock(side_effect=[NOW + 0.9, NOW + 86_400])
        opener = ScriptedOpener(records, [])
        lines = self.run_quietly(collect_daily, opener=opener, clock=clock)
        clock.assert_called_once_with()
        self.assertEqual([r["param_next_id"] for r in opener.requests], ["1", "10001"])
        for request in opener.requests:
            self.assertEqual(request["param_window_start"], str(NOW - 432_000))
            self.assertEqual(request["param_window_end"], str(NOW))
            self.assertNotIn("param_through_id", request)
        self.assertEqual(self.progress(), [(101, 1, 100)])
        self.assertIn("complete=false saved_posts=10000", lines[0])
        self.assertIn("complete=true saved_posts=10000", lines[1])

    def test_daily_refresh_inserts_newly_eligible_and_keeps_last_eligible_snapshot(self):
        start_history(self.conn, next_id=101, complete=True)
        old = post(3, created_at=NOW - 10 * 86_400, title="old snapshot")
        commit_page(self.conn, [post(1), old])
        # Post 2 was previously omitted at zero comments; it now qualifies.
        self.run_quietly(
            collect_daily, clock=lambda: NOW,
            opener=ScriptedOpener([row(1, descendants=9), row(2)]),
        )
        self.run_quietly(
            collect_daily, clock=lambda: NOW + 1,
            opener=ScriptedOpener([
                row(1, title="six", url="", text="<p>updated 雪</p>", descendants=6)
            ]),
        )
        # Later below-five and deleted versions are omitted by the server query.
        for now in (NOW + 2, NOW + 3):
            self.run_quietly(collect_daily, clock=lambda: now, opener=ScriptedOpener([]))
        self.assertEqual(self.conn.execute("SELECT count(*) FROM posts").fetchone()[0], 3)
        self.assertEqual(
            self.conn.execute("SELECT title, url, text, descendants FROM posts WHERE id=1").fetchone(),
            ("six", "", "<p>updated 雪</p>", 6),
        )
        self.assertEqual(self.conn.execute("SELECT descendants FROM posts WHERE id=2").fetchone()[0], 5)
        self.assertEqual(self.conn.execute("SELECT title FROM posts WHERE id=3").fetchone()[0], old.title)
        self.assertEqual(self.progress(), [(101, 1, 100)])

    def test_daily_failure_then_eight_days_offline_starts_a_fresh_window_from_id_one(self):
        start_history(self.conn, next_id=101, complete=True)
        records = [row(i) for i in range(1, PAGE_SIZE + 1)]
        first = ScriptedOpener(records, KeyboardInterrupt())
        with self.assertRaises(KeyboardInterrupt):
            self.run_quietly(collect_daily, opener=first, clock=lambda: NOW)
        later = NOW + 8 * 86_400
        second = ScriptedOpener([row(20_000, created_at=later - 1)])
        self.run_quietly(collect_daily, opener=second, clock=lambda: later)
        request, = second.requests
        self.assertEqual(request["param_next_id"], "1")
        self.assertEqual(request["param_window_start"], str(later - 432_000))
        self.assertEqual(request["param_window_end"], str(later))
        self.assertEqual(self.conn.execute("SELECT count(*) FROM posts").fetchone()[0], PAGE_SIZE + 1)
        self.assertEqual(self.progress(), [(101, 1, 100)])


class CommandTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "catalog.sqlite3"
        self.args = ["--db", str(self.path), "collect"]

    def test_three_runs_fail_resume_and_then_skip_history_with_real_sqlite_and_http_fixtures(self):
        records = [row(i) for i in range(1, PAGE_SIZE + 1)]
        first = ScriptedOpener([{"max_id": 20_002}], records, URLError("page two failed"))
        clock = Mock(return_value=NOW)
        output = StringIO()
        with redirect_stdout(output), self.assertRaises(URLError):
            main(self.args, opener=first, clock=clock)
        clock.assert_not_called()
        self.assertTrue(all("param_window_start" not in r for r in first.requests))
        self.assertEqual(len(output.getvalue().splitlines()), 1)
        with closing(open_catalog(self.path)) as conn:
            self.assertEqual(conn.execute("SELECT * FROM collection_progress").fetchall(), [(10_001, 0, 20_002)])
            self.assertEqual(conn.execute("SELECT count(*) FROM posts").fetchone()[0], 10_000)

        second = ScriptedOpener(
            [row(10_001), row(10_002)],
            [row(10_002, descendants=9), row(20_003)],
        )
        output = StringIO()
        with redirect_stdout(output):
            main(self.args, opener=second, clock=clock)
        clock.assert_called_once_with()
        self.assertEqual(len(second.requests), 2)
        self.assertEqual(second.requests[0]["param_next_id"], "10001")
        self.assertEqual(second.requests[0]["param_through_id"], "20002")
        self.assertIn("param_window_start", second.requests[1])
        lines = output.getvalue().splitlines()
        self.assertIn("complete=true saved_posts=10002", lines[0])
        self.assertIn("complete=true saved_posts=10003", lines[1])

        third = ScriptedOpener([row(10_002, descendants=6)])
        with redirect_stdout(StringIO()):
            main(self.args, opener=third, clock=lambda: NOW + 1)
        self.assertEqual(len(third.requests), 1)
        self.assertIn("param_window_start", third.requests[0])
        with closing(open_catalog(self.path)) as conn:
            self.assertEqual(conn.execute("SELECT * FROM collection_progress").fetchall(), [(20_003, 1, 20_002)])
            self.assertEqual(conn.execute("SELECT count(*) FROM posts").fetchone()[0], 10_003)
            self.assertEqual(conn.execute("SELECT descendants FROM posts WHERE id=10002").fetchone()[0], 6)
            self.assertEqual(conn.execute("SELECT descendants FROM posts WHERE id=20003").fetchone()[0], 5)

    def test_usage_errors_exit_two_without_opening_a_catalog_or_fetching(self):
        for args in ([], ["collect"], ["--db", str(self.path)],
                     self.args + ["--lookback", "10"], ["--db", str(self.path), "daily"]):
            opener = ScriptedOpener()
            with self.subTest(args=args), redirect_stderr(StringIO()):
                with self.assertRaises(SystemExit) as raised:
                    main(args, opener=opener)
                self.assertEqual(raised.exception.code, 2)
                self.assertEqual(opener.requests, [])
                self.assertFalse(self.path.exists())

    def test_uncaught_dependency_failure_exits_one_with_traceback(self):
        script = """
import sys
from urllib.error import HTTPError
from hn_search.__main__ import main
def offline(url, *, timeout):
    raise HTTPError(url, 500, 'quota exceeded', {}, None)
main(['--db', sys.argv[1], 'collect'], opener=offline)
"""
        run = subprocess.run(
            [sys.executable, "-c", script, str(self.path)], cwd=ROOT,
            capture_output=True, text=True, timeout=10,
        )
        self.assertEqual(run.returncode, 1)
        self.assertEqual(run.stdout, "")
        self.assertIn("Traceback", run.stderr)
        self.assertIn("urllib.error.HTTPError: HTTP Error 500: quota exceeded", run.stderr)
