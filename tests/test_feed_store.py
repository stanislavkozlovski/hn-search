from contextlib import closing
from dataclasses import replace
import sqlite3

from hn_search.catalog import open_catalog
from hn_search.feed import Decision, Story
from hn_search.feed import store
from tests.feed_helpers import NOW, FeedCase, hit, sent, window


class StoreTests(FeedCase):
    def test_research_catalog_is_refused_without_changing_posts_or_progress(self):
        with closing(open_catalog(self.path)) as conn:
            with conn:
                conn.execute("INSERT INTO posts (id,title,url,text,created_at,descendants) VALUES (1,'t','','',1,5)")
                conn.execute("INSERT INTO collection_progress VALUES (2, 0, 10)")
        before = self.path.read_bytes()
        with self.assertRaisesRegex(ValueError, "not an HN feed"):
            store.open_feed(self.path)
        self.assertEqual(before, self.path.read_bytes())
        with closing(open_catalog(self.path)) as conn:
            self.assertEqual(conn.execute("PRAGMA user_version").fetchone()[0], 1)
            self.assertEqual(conn.execute("SELECT * FROM collection_progress").fetchall(), [(2, 0, 10)])

    def test_schema_identity_versions_foreign_keys_and_reopen(self):
        with closing(store.open_feed(self.path)) as conn:
            self.assertEqual(conn.execute("PRAGMA application_id").fetchone()[0], 0x484E4644)
            self.assertEqual(conn.execute("PRAGMA foreign_keys").fetchone()[0], 1)
            with self.assertRaises(sqlite3.IntegrityError), conn:
                conn.execute("INSERT INTO observations VALUES (1, 1, 6)")
            with conn:
                conn.execute("PRAGMA user_version = 2")
        with self.assertRaisesRegex(ValueError, "user_version: 2"):
            store.open_feed(self.path)

    def test_observations_keep_discovery_and_created_at_and_never_prune(self):
        story = Story(1, "Agents", None, NOW - 7200, 6)
        lens = self.settings().lenses[0]
        with closing(store.open_feed(self.path)) as conn:
            store.save_window(conn, (lens,), [story], NOW)
            store.save_window(conn, (lens,), [replace(story, title="Retitled", url="https://example.com", created_at=NOW, points=19)], NOW + 3600)
            store.save_window(conn, (), [], NOW + 7200)
        with closing(store.open_feed(self.path)) as conn:
            saved = dict(conn.execute("SELECT * FROM stories").fetchone())
            self.assertEqual((saved["title"], saved["url"], saved["created_at"], saved["first_seen_at"]),
                             ("Retitled", "https://example.com", story.created_at, NOW))
            self.assertEqual(conn.execute("SELECT growth FROM story_growth").fetchone()[0], "6 → 19 points over 60 minutes")
            self.assertEqual(conn.execute("SELECT count(*) FROM observations").fetchone()[0], 2)

    def test_new_lens_skips_saved_stories_and_batches_save_only_needed_pairs(self):
        lens = self.settings().lenses[0]
        second = replace(lens, name="second")
        story = Story(1, "Agents", None, NOW - 100, 6)
        with closing(store.open_feed(self.path)) as conn:
            store.save_window(conn, (lens,), [story], NOW)
            store.save_decisions(conn, [Decision(lens.name, story, lens.categories_digest, ())], NOW)
            store.save_window(conn, (lens, second), [story, replace(story, id=2)], NOW + 3600)
            batches = list(store.batches_to_judge(conn, (lens, second), [story, replace(story, id=2)]))
            self.assertEqual([s.id for s in batches[0].stories], [2])
            self.assertEqual(batches[0].needed, {(lens.name, 2), (second.name, 2)})
            self.assertEqual(list(store.batches_to_judge(conn, (), [story])), [])

    def test_send_commits_message_and_lines_before_next_request(self):
        def check_first_commit(request):
            with closing(sqlite3.connect(self.path)) as other:
                self.assertEqual(other.execute("SELECT telegram_message_id FROM messages").fetchall(), [(812,)])
                self.assertGreater(other.execute("SELECT count(*) FROM message_lines").fetchone()[0], 0)
            return sent(813)

        stories = [hit(i + 1, title="Agent " + "x" * 200, url="https://example.com/" + "x" * 150) for i in range(8)]
        self.run_feed(window(*stories), sent(), check_first_commit)
        with closing(store.open_feed(self.path)) as conn:
            self.assertEqual(conn.execute("SELECT count(*) FROM messages").fetchone()[0], 2)
            self.assertEqual(conn.execute("SELECT count(*) FROM message_lines").fetchone()[0], 8)
            self.assertNotIn(self.settings().tokens["HN_FEED_TEST_TOKEN"].encode(), self.path.read_bytes())
