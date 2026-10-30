import dataclasses
import sqlite3
import tempfile
import unittest
from pathlib import Path

from hn_search.catalog import commit_page, migrate_archives, open_catalog
from hn_search.clickhouse import Post
from hn_search.research import store


class StoreTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.path = Path(directory.name) / "catalog.db"
        self.conn = open_catalog(self.path)
        self.addCleanup(self.conn.close)
        commit_page(self.conn, [Post(1, "Housing", "", "", 1, 5), Post(2, "Renting", "", "", 1, 5)])

    def test_additive_migrations_and_collector_rollback_compatibility(self):
        for version in (1, 2, 4):
            with self.subTest(version=version):
                if version == 2:
                    migrate_archives(self.conn)
                with self.conn:
                    self.conn.execute(f"PRAGMA user_version = {version}")
                store.migrate(self.conn)
                expected = max(3, version)
                self.assertEqual(self.conn.execute("PRAGMA user_version").fetchone()[0], expected)
                before = self.conn.execute("SELECT sql FROM sqlite_master ORDER BY name").fetchall()
                store.migrate(self.conn)
                self.assertEqual(self.conn.execute("SELECT sql FROM sqlite_master ORDER BY name").fetchall(), before)
                self.assertEqual(self.conn.execute("SELECT count(*) FROM posts").fetchone()[0], 2)
                tables = {row[0] for row in self.conn.execute("SELECT name FROM sqlite_master")}
                self.assertTrue({"archives", "archive_items", "research_runs", "ai_results"} <= tables)
                self.conn.commit()
                old = open_catalog(self.path)
                try:
                    commit_page(old, [Post(3, "Still collecting", "", "", 1, 5)])
                    self.assertEqual(old.execute("PRAGMA user_version").fetchone()[0], expected)
                finally:
                    old.close()
                with self.conn:
                    self.conn.execute("DELETE FROM posts WHERE id = 3")

    def test_every_key_field_prevents_reuse_and_calls_save_atomically(self):
        store.migrate(self.conn)
        run_id, folder = store.create_run(self.conn, self.path.parent / "out", "Question?", ["rent"], {},
                                          [1, 2], now=1)
        key = store.ResultKey("verdict", 1, 0, "verdict@v1", "gpt-6-luna", "high", "archive:1@1", "Question?")
        stored = store.save_call(self.conn, run_id, [(key, {"verdict": "relevant"}, [101])],
                                 {"input_tokens": 10}, now=2, statuses=[(1, "relevant", "Yes")])[0]
        self.assertEqual(store.lookup(self.conn, key).id, stored.id)
        changes = {"stage": "analysis", "story_id": 2, "part": 1, "prompt_version": "verdict@v2",
                   "model": "gpt-6-astra", "effort": "max", "input_key": "archive:1@2", "question": "Question!"}
        for field, value in changes.items():
            with self.subTest(field=field):
                self.assertIsNone(store.lookup(self.conn, dataclasses.replace(key, **{field: value})))
        with self.conn:
            self.conn.execute("""CREATE TRIGGER fail_second BEFORE INSERT ON ai_results
                WHEN NEW.story_id = 2 BEGIN SELECT RAISE(ABORT, 'injected failure'); END""")
        first = dataclasses.replace(key, stage="description", question="")
        second = dataclasses.replace(first, story_id=2)
        with self.assertRaisesRegex(sqlite3.IntegrityError, "injected failure"):
            store.save_call(self.conn, run_id, [(first, {}, []), (second, {}, [])], {}, now=2,
                            statuses=[(2, "irrelevant", "No")])
        self.assertIsNone(store.lookup(self.conn, first))
        self.assertEqual(self.conn.execute(
            "SELECT status FROM research_run_stories WHERE run_id = ? AND story_id = 2", (run_id,)).fetchone()[0], "matched")
        self.assertEqual(store.lookup(self.conn, key).id, stored.id)
        self.assertTrue(folder.is_dir())

    def test_run_folder_collision_rolls_back_the_run(self):
        store.migrate(self.conn)
        out = self.path.parent / "out"
        (out / "run-1").mkdir(parents=True)
        with self.assertRaises(FileExistsError):
            store.create_run(self.conn, out, "Question", [], {}, [1], now=1)
        self.assertEqual(self.conn.execute("SELECT count(*) FROM research_runs").fetchone()[0], 0)
