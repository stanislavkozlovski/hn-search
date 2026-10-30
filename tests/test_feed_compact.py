from contextlib import closing, redirect_stdout
from dataclasses import replace
from io import StringIO
import json
import sqlite3
from unittest.mock import patch

from hn_search.feed import Line, Message, Story, store, telegram
from hn_search.feed.run import compact_messages
from tests.feed_helpers import NOW, FeedCase, RecordingOpener, hit, sent, window

DELETED = {"ok": True, "result": True}
FORBIDDEN = {"ok": False, "error_code": 403, "description": "Forbidden"}


class CompactionTests(FeedCase):
    def seed(self, conn, count=11, *, now=NOW, title_size=0, url_size=0, chat=123456789):
        lens = self.settings().lenses[0]
        stories = [Story(i, f"Agent {i} " + "x" * title_size,
                         "https://example.com/" + "x" * url_size, now - 100, 6)
                   for i in range(1, count + 1)]
        store.save_window(conn, (lens,), stories, now)
        for story in stories:
            line = Line(lens.name, story.id, ("agents",), story.title, story.url, (6,))
            store.record_message(conn, Message(lens.bot_token_env, chat, (line,)), 811 + story.id, now)

    def compact(self, conn, *responses, now=NOW):
        opener = RecordingOpener(*responses)
        with redirect_stdout(StringIO()):
            failures = compact_messages(conn, self.settings(), opener=opener, now=now)
        self.assertEqual(opener.responses, [])
        return failures, opener

    def test_hourly_arrivals_continue_and_eleventh_message_compacts_the_backlog(self):
        for hour in range(10):
            now = NOW + hour * 3600
            opener = self.run_feed(window(hit(hour + 1, created_at=now - 100)), sent(812 + hour), now=now)
            self.assertEqual(len(opener.requests), 2)
        now = NOW + 10 * 3600
        opener = self.run_feed(window(hit(11, created_at=now - 100)), sent(822), sent(),
                               *[DELETED] * 10, now=now)
        methods = [request["url"].rsplit("/", 1)[-1] for request in opener.requests[1:]]
        self.assertEqual(methods, ["sendMessage", "editMessageText", *["deleteMessage"] * 10])
        self.assertEqual(opener.requests[2]["payload"]["message_id"], 812)
        self.assertIn("11 new matches", opener.requests[2]["payload"]["text"])
        self.assertEqual({request["payload"]["message_id"] for request in opener.requests[3:]}, set(range(813, 823)))
        with closing(store.open_feed(self.path)) as conn:
            self.assertEqual(conn.execute("SELECT count(*) FROM message_lines").fetchone()[0], 11)
            self.assertEqual(conn.execute("SELECT count(*) FROM messages WHERE deleted_at IS NOT NULL").fetchone()[0], 10)
        self.run_feed(window(hit(12, created_at=now + 3500)), sent(823), now=now + 3600)

    def test_all_replacements_are_saved_before_any_original_is_deleted(self):
        def check_saved(request):
            self.assertTrue(request["url"].endswith("/deleteMessage"))
            with closing(sqlite3.connect(self.path)) as other:
                self.assertEqual(other.execute("SELECT count(*) FROM message_lines").fetchone()[0], 11)
                self.assertEqual(other.execute("SELECT count(DISTINCT message_id) FROM message_lines").fetchone()[0], 2)
                self.assertEqual(other.execute("SELECT count(*) FROM messages WHERE superseded_by IS NOT NULL").fetchone()[0], 9)
                for message_id, story_ids in original_stories.items():
                    row = other.execute("SELECT superseded_by FROM messages WHERE id=?", (message_id,)).fetchone()
                    if row[0] is None:
                        saved = {row[0] for row in other.execute("SELECT story_id FROM message_lines WHERE message_id=?", (message_id,))}
                        self.assertTrue(story_ids <= saved)
            return DELETED

        with closing(store.open_feed(self.path)) as conn:
            self.seed(conn, title_size=200, url_size=200)
            before = {tuple(row) for row in conn.execute("SELECT lens,story_id,tags,title,url,shown_points FROM message_lines")}
            original_stories = {row[0]: {row[1]} for row in conn.execute("SELECT message_id,story_id FROM message_lines")}
            failures, opener = self.compact(conn, sent(), sent(), check_saved, *[DELETED] * 8)
            self.assertEqual(failures, 0)
            self.assertTrue(all(request["url"].endswith("/editMessageText") for request in opener.requests[:2]))
            self.assertEqual(before, {tuple(row) for row in conn.execute("SELECT lens,story_id,tags,title,url,shown_points FROM message_lines")})
            self.assertEqual(conn.execute("PRAGMA foreign_key_check").fetchall(), [])
            for message in next(iter(store.recent_messages(conn, self.settings().lenses, NOW))):
                self.assertLessEqual(telegram.utf16_units(telegram.render(message, worst_case=True, markup=False)), 4096)

    def test_failed_replacement_never_deletes_or_moves_originals_and_can_retry(self):
        with closing(store.open_feed(self.path)) as conn:
            self.seed(conn, title_size=200, url_size=200)
            before = [tuple(row) for row in conn.execute("SELECT * FROM message_lines ORDER BY message_id,position")]
            failures, opener = self.compact(conn, sent(), FORBIDDEN)
            self.assertEqual(failures, 1)
            self.assertEqual(len(opener.requests), 2)
            self.assertEqual(before, [tuple(row) for row in conn.execute("SELECT * FROM message_lines ORDER BY message_id,position")])
            self.assertEqual(conn.execute("SELECT count(*) FROM messages WHERE superseded_by IS NOT NULL").fetchone()[0], 0)
            self.assertEqual(self.compact(conn, sent(), sent(), *[DELETED] * 9)[0], 0)

    def test_failed_delete_retries_after_restart_without_losing_or_resending_stories(self):
        with closing(store.open_feed(self.path)) as conn:
            self.seed(conn)
            failures, opener = self.compact(conn, sent(), FORBIDDEN, *[DELETED] * 9)
            self.assertEqual(failures, 1)
            self.assertEqual(len(list(store.messages_to_delete(conn, self.settings().lenses))), 1)
            other_chat = (replace(self.settings().lenses[0], chat_id=987654321),)
            self.assertEqual(list(store.messages_to_delete(conn, other_chat)), [])
            self.assertEqual(conn.execute("SELECT count(*) FROM message_lines").fetchone()[0], 11)
        missing = {"ok": False, "error_code": 400, "description": "Bad Request: message to delete not found"}
        with closing(store.open_feed(self.path)) as conn:
            failures, opener = self.compact(conn, missing, now=NOW + 3600)
            self.assertEqual(failures, 0)
            self.assertEqual(len(opener.requests), 1)
            self.assertTrue(opener.requests[0]["url"].endswith("/deleteMessage"))
            self.assertEqual(list(store.messages_to_delete(conn, self.settings().lenses)), [])

    def test_crash_after_saving_replacements_leaves_durable_pending_deletions(self):
        with closing(store.open_feed(self.path)) as conn:
            self.seed(conn)
            with patch("hn_search.feed.telegram.delete_message", side_effect=RuntimeError("interrupted")):
                with self.assertRaisesRegex(RuntimeError, "interrupted"):
                    self.compact(conn, sent())
        with closing(store.open_feed(self.path)) as conn:
            failures, opener = self.compact(conn, *[DELETED] * 10)
            self.assertEqual(failures, 0)
            self.assertTrue(all(request["url"].endswith("/deleteMessage") for request in opener.requests))
            self.assertEqual(conn.execute("SELECT count(*) FROM message_lines").fetchone()[0], 11)

    def test_ten_messages_old_messages_and_other_chats_are_left_alone(self):
        for count, timestamp, chat in ((10, NOW, 123456789), (11, NOW - 86400, 123456789), (11, NOW, 987654321)):
            path = self.directory / f"{count}-{timestamp}-{chat}.sqlite3"
            with self.subTest(count=count, timestamp=timestamp, chat=chat), closing(store.open_feed(path)) as conn:
                self.seed(conn, count, now=timestamp, chat=chat)
                self.assertEqual(self.compact(conn)[0], 0)
                self.assertEqual(conn.execute("SELECT count(*) FROM messages WHERE deleted_at IS NULL").fetchone()[0], count)

    def test_messages_that_cannot_be_merged_without_exceeding_the_limit_stay_intact(self):
        with closing(store.open_feed(self.path)) as conn:
            self.seed(conn, title_size=2100)
            self.assertEqual(self.compact(conn)[0], 0)
            self.assertEqual(conn.execute("SELECT count(*) FROM messages WHERE superseded_by IS NULL").fetchone()[0], 11)
            self.assertEqual(conn.execute("SELECT count(*) FROM message_lines").fetchone()[0], 11)

    def test_score_updates_follow_stories_into_the_retained_message(self):
        with closing(store.open_feed(self.path)) as conn:
            self.seed(conn)
            self.compact(conn, sent(), *[DELETED] * 10)
            edits = list(store.messages_to_edit(conn, self.settings().lenses, [Story(11, "Agent 11", None, NOW, 19)]))
            self.assertEqual(len(edits), 1)
            self.assertEqual(edits[0].telegram_message_id, 812)
            self.assertEqual(len(edits[0].lines), 11)
            self.assertEqual(edits[0].lines[-1].shown_points, (6, 19))
            store.record_edit(conn, edits[0])
            self.assertEqual(json.loads(conn.execute("SELECT shown_points FROM message_lines WHERE story_id=11").fetchone()[0]), [6, 19])
