from contextlib import closing, redirect_stderr
from io import StringIO
import json
import os
import subprocess
import sys
from unittest.mock import Mock, patch

from hn_search.__main__ import main
from hn_search.feed import store
from tests.feed_helpers import CONFIG, NOW, TOKEN, FeedCase, RecordingOpener, hit, sent, window

FORBIDDEN = {"ok": False, "error_code": 403, "description": "Forbidden: bot was blocked by the user"}


class RunTests(FeedCase):
    def test_hourly_send_two_score_edits_and_expiry_keep_every_row(self):
        first = self.run_feed(window(hit()), sent())
        self.assertNotIn("<s>", first.requests[1]["payload"]["text"])
        second = self.run_feed(window(hit(points=19)), sent(), now=NOW + 3600)
        self.assertIn("<s>6 points</s> 19 points", second.requests[1]["payload"]["text"])
        third = self.run_feed(window(hit(points=31)), sent(), now=NOW + 7200)
        self.assertIn("<s>6 points</s> <s>19 points</s> 31 points", third.requests[1]["payload"]["text"])
        self.run_feed(window(), now=NOW + 36000)
        self.assertEqual(len(self.calls()), 1)
        with closing(store.open_feed(self.path)) as conn:
            self.assertEqual(conn.execute("SELECT count(*) FROM stories").fetchone()[0], 1)
            self.assertEqual(conn.execute("SELECT count(*) FROM decisions").fetchone()[0], 1)
            self.assertEqual(conn.execute("SELECT count(*) FROM observations").fetchone()[0], 3)
            self.assertEqual(conn.execute("SELECT count(*) FROM messages").fetchone()[0], 1)

    def test_failed_send_exits_one_then_retries_with_observed_growth(self):
        with self.assertRaises(SystemExit) as raised:
            self.run_feed(window(hit()), FORBIDDEN)
        self.assertEqual(raised.exception.code, 1)
        retry = self.run_feed(window(hit(points=19)), sent(), now=NOW + 3600)
        self.assertIn("<s>6 points</s> 19 points", retry.requests[1]["payload"]["text"])
        self.assertEqual(len(self.calls()), 1)
        self.assertIn("failures=0", self.output.getvalue())

    def test_failed_send_continues_other_destinations_and_retries_only_missing_lines(self):
        self.config.write_text(CONFIG + CONFIG.replace('name = "ai-agents"', 'name = "second"').replace("123456789", "987654321"))
        with self.assertRaises(SystemExit):
            self.run_feed(window(hit()), FORBIDDEN, sent())
        with closing(store.open_feed(self.path)) as conn:
            self.assertEqual(conn.execute("SELECT lens FROM message_lines").fetchone()[0], "second")
        retry = self.run_feed(window(hit()), sent(813), now=NOW + 3600)
        self.assertEqual(len(retry.requests), 2)
        self.assertEqual(retry.requests[1]["payload"]["chat_id"], 123456789)
        self.assertEqual(len(self.calls()), 1)

    def test_classifier_failure_stops_batches_still_sends_pending_and_edits(self):
        with self.assertRaises(SystemExit):
            self.run_feed(window(hit(1)), FORBIDDEN)
        self.run_feed(window(hit(1), hit(2)), sent(), now=NOW + 1)
        # One pending send remains while another message needs an edit.
        with self.assertRaises(SystemExit):
            self.run_feed(window(hit(1), hit(2), hit(3)), FORBIDDEN, now=NOW + 2)
        before = len(self.calls())
        with patch.dict(os.environ, {"FAKE_CODEX_MODE": "fail"}), self.assertRaises(SystemExit):
            self.run_feed(window(hit(1, points=19), hit(2), hit(3), *[hit(i + 10) for i in range(21)]),
                          sent(813), sent(), now=NOW + 3600)
        self.assertEqual(len(self.calls()), before + 1)
        self.assertIn("feed send", self.output.getvalue())
        self.assertIn("feed edit", self.output.getvalue())
        self.assertIn("failures=1", self.output.getvalue())

    def test_failed_edit_alone_succeeds_and_retries_without_updating_shown_points(self):
        self.run_feed(window(hit()), sent())
        self.run_feed(window(hit(points=19)), FORBIDDEN, now=NOW + 3600)
        self.assertIn("edit-failed", self.output.getvalue())
        self.assertIn("failures=0", self.output.getvalue())
        with closing(store.open_feed(self.path)) as conn:
            self.assertEqual(json.loads(conn.execute("SELECT shown_points FROM message_lines").fetchone()[0]), [6])
        opener = self.run_feed(window(hit(points=31)), sent(), now=NOW + 7200)
        self.assertIn("<s>6 points</s> 31 points", opener.requests[1]["payload"]["text"])

    def test_edits_keep_sent_content_and_update_only_current_stories_once_per_message(self):
        self.run_feed(window(hit(1), hit(2)), sent())
        opener = self.run_feed(window(hit(1, title="Agent renamed", url=None, points=19)), sent(), now=NOW + 3600)
        self.assertEqual(len(opener.requests), 2)
        text = opener.requests[1]["payload"]["text"]
        self.assertNotIn("renamed", text)
        self.assertIn("https://example.com/agents", text)
        self.assertEqual(text.count("<s>6 points</s> 19 points"), 1)
        self.assertIn("6 points ·", text)

    def test_removed_lens_sends_nothing_but_shared_destination_still_edits(self):
        self.run_feed(window(hit()), sent())
        self.config.write_text(CONFIG.replace('name = "ai-agents"', 'name = "second"'))
        self.run_feed(window(hit(points=19)), sent(), now=NOW + 3600)
        self.assertEqual(len(self.calls()), 1)
        self.config.write_text(self.config.read_text().replace("123456789", "987654321"))
        self.run_feed(window(hit(points=31)), now=NOW + 7200)
        self.assertEqual(len(self.calls()), 1)

    def test_rejudgment_to_empty_cancels_pending_send(self):
        with self.assertRaises(SystemExit):
            self.run_feed(window(hit()), FORBIDDEN)
        self.run_feed(window(hit(title="Unrelated news")), now=NOW + 3600)
        self.run_feed(window(), now=NOW + 7200)
        with closing(store.open_feed(self.path)) as conn:
            self.assertEqual(conn.execute("SELECT count(*) FROM messages").fetchone()[0], 0)
            self.assertEqual(conn.execute("SELECT categories FROM decisions").fetchone()[0], "[]")

    def test_pending_matches_survive_search_expiry_and_restart(self):
        with self.assertRaises(SystemExit):
            self.run_feed(window(hit()), FORBIDDEN)
        opener = self.run_feed(window(), sent(), now=NOW + 36000)
        self.assertIn("Agent frameworks", opener.requests[1]["payload"]["text"])
        with closing(store.open_feed(self.path)) as conn:
            self.assertEqual(conn.execute("SELECT count(*) FROM messages").fetchone()[0], 1)
            self.assertEqual(store.pending_lines(conn, self.settings().lenses), [])

    def test_ten_shown_values_cap_and_unchanged_score_no_request(self):
        self.run_feed(window(hit()), sent())
        self.run_feed(window(hit()), now=NOW + 1)
        for number in range(1, 10):
            self.run_feed(window(hit(points=6 + number)), sent(), now=NOW + number * 60)
        self.run_feed(window(hit(points=100)), now=NOW + 1000)
        with closing(store.open_feed(self.path)) as conn:
            self.assertEqual(len(json.loads(conn.execute("SELECT shown_points FROM message_lines").fetchone()[0])), 10)

    def test_clock_is_read_once_usage_errors_touch_nothing_and_collect_imports_no_feed(self):
        for args in (["--db", str(self.path), "feed"], ["--db", str(self.path), "feed", "--bad"]):
            with redirect_stderr(StringIO()), self.assertRaises(SystemExit) as raised:
                main(args, opener=RecordingOpener())
            self.assertEqual(raised.exception.code, 2)
            self.assertFalse(self.path.exists())
        clock = Mock(return_value=NOW)
        main(["--db", str(self.path), "feed", "--config", str(self.config)], opener=RecordingOpener(window()), clock=clock)
        clock.assert_called_once_with()
        run = subprocess.run([sys.executable, "-S", "-c",
                              "import sys; from hn_search.__main__ import main; "
                              "assert not any(n.startswith(('hn_search.feed', 'stan_ai_client')) for n in sys.modules); "
                              "main(['--help'])"], capture_output=True, text=True, timeout=10)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertNotIn(TOKEN, self.output.getvalue() if hasattr(self, "output") else "")
