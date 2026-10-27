from contextlib import closing
from pathlib import Path
import select
import sqlite3
import subprocess
import sys
import tempfile
import unittest

from hn_search.catalog import commit_page, migrate_archives, open_catalog
from tests.helpers import post, start_history


ROOT = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "catalog.sqlite3"
        self.conn = open_catalog(self.path)
        self.addCleanup(lambda: self.conn.close())

    def reopen(self):
        self.conn.close()
        self.conn = open_catalog(self.path)

    def progress(self):
        return self.conn.execute("SELECT * FROM collection_progress").fetchall()

    def test_initialization_and_reopening_preserve_committed_posts_and_progress(self):
        self.assertFalse(self.conn.autocommit)
        self.assertEqual(self.conn.execute("PRAGMA user_version").fetchone()[0], 1)
        self.assertEqual(self.conn.execute("SELECT * FROM posts").fetchall(), [])
        self.assertEqual(self.progress(), [])
        start_history(self.conn)
        commit_page(self.conn, [post(1)], next_id=2)
        self.reopen()
        self.assertEqual(self.conn.execute("SELECT id FROM posts").fetchall(), [(1,)])
        self.assertEqual(self.progress(), [(2, 0, 100)])
        self.assertEqual(self.conn.execute("PRAGMA user_version").fetchone()[0], 1)

    def test_existing_nonzero_schema_version_is_never_overwritten(self):
        with self.conn:
            self.conn.execute("PRAGMA user_version = 7")
        self.reopen()
        self.assertEqual(self.conn.execute("PRAGMA user_version").fetchone()[0], 7)

    def test_archive_migration_is_additive_repeatable_and_preserves_higher_versions(self):
        start_history(self.conn, next_id=3)
        commit_page(self.conn, [post(1), post(2)])
        before = self.conn.execute("SELECT * FROM posts").fetchall()
        migrate_archives(self.conn)
        migrate_archives(self.conn)
        self.assertEqual(self.conn.execute("PRAGMA user_version").fetchone()[0], 2)
        self.assertEqual(self.conn.execute("SELECT * FROM posts").fetchall(), before)
        self.assertEqual(self.progress(), [(3, 0, 100)])
        with self.conn:
            self.conn.execute("PRAGMA user_version = 9")
            self.conn.execute("INSERT INTO archives (root_id, started_at) VALUES (1, 10)")
        migrate_archives(self.conn)
        self.reopen()
        self.assertEqual(self.conn.execute("PRAGMA user_version").fetchone()[0], 9)
        self.assertEqual(self.conn.execute("SELECT status FROM archives").fetchone()[0], "incomplete")
        with self.conn:
            self.conn.execute("UPDATE archives SET finished_at = 20")
        self.assertEqual(self.conn.execute("SELECT status FROM archives").fetchone()[0], "complete")

    def test_failed_migration_rolls_back_ddl_and_version(self):
        def authorizer(action, arg1, arg2, database, trigger):
            if action == sqlite3.SQLITE_CREATE_TABLE and arg1 == "archive_items":
                return sqlite3.SQLITE_DENY
            return sqlite3.SQLITE_OK

        self.conn.set_authorizer(authorizer)
        with self.assertRaises(sqlite3.DatabaseError):
            migrate_archives(self.conn)
        self.conn.set_authorizer(None)
        self.reopen()
        self.assertEqual(self.conn.execute("PRAGMA user_version").fetchone()[0], 1)
        self.assertEqual(self.conn.execute("SELECT name FROM sqlite_master WHERE name IN ('archives', 'archive_items')").fetchall(), [])

    def test_old_collector_runs_against_migrated_catalog_without_changing_archives(self):
        # Execute the exact merged v1 modules in isolation against this database.
        start_history(self.conn, next_id=101, complete=True)
        commit_page(self.conn, [post(1)])
        migrate_archives(self.conn)
        with self.conn:
            self.conn.execute("INSERT INTO archives (root_id, started_at, finished_at) VALUES (1, 10, 20)")
            self.conn.execute("INSERT INTO archive_items VALUES (1, 1, 'null', 15)")
        self.conn.commit()
        legacy = Path(self.directory.name) / "legacy"
        package = legacy / "hn_search"
        package.mkdir(parents=True)
        for filename in ("__init__.py", "__main__.py", "catalog.py", "clickhouse.py", "collect.py"):
            content = subprocess.check_output(["git", "show", f"64703b5:hn_search/{filename}"], cwd=ROOT)
            (package / filename).write_bytes(content)
        script = """
from io import BytesIO
import sys
from hn_search.__main__ import main
def opener(url, *, timeout):
    return BytesIO(b'{"data": [], "rows": 0}')
main(['--db', sys.argv[1], 'collect'], opener=opener, clock=lambda: 1800000000)
"""
        run = subprocess.run([sys.executable, "-c", script, str(self.path)], cwd=legacy, capture_output=True, text=True, timeout=10)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.reopen()
        self.assertEqual(self.progress(), [(101, 1, 100)])
        self.assertEqual(self.conn.execute("SELECT * FROM archive_items").fetchall(), [(1, 1, "null", 15)])
        self.assertEqual(self.conn.execute("SELECT finished_at FROM archives").fetchone()[0], 20)
        self.assertEqual(self.conn.execute("PRAGMA user_version").fetchone()[0], 2)

    def test_mapping_preserves_html_unicode_empty_strings_and_generates_hn_link(self):
        record = post(42, title="雪 & <b>café</b>", url="", text="<p>hi &#39; \n🙂</p>")
        commit_page(self.conn, [record])
        self.reopen()
        self.assertEqual(
            self.conn.execute("SELECT * FROM posts").fetchone(),
            (42, record.title, "", record.text, record.created_at, 5,
             "https://news.ycombinator.com/item?id=42"),
        )

    def test_upsert_refreshes_in_place_without_deleting_rows_or_changing_history(self):
        start_history(self.conn, next_id=101, complete=True)
        commit_page(self.conn, [post(1, descendants=9), post(2)])
        # Observe UPDATE versus deletion/reinsertion, including SQLite's REPLACE.
        with self.conn:
            self.conn.execute("PRAGMA recursive_triggers = ON")
            self.conn.execute("""CREATE TRIGGER forbid_delete BEFORE DELETE ON posts
                BEGIN SELECT RAISE(ABORT, 'saved posts must not be deleted'); END""")
        updated = post(1, title="new", url="", text="changed", created_at=123, descendants=6)
        commit_page(self.conn, [updated])
        commit_page(self.conn, [])
        self.reopen()
        self.assertEqual(self.conn.execute("SELECT count(*) FROM posts").fetchone()[0], 2)
        self.assertEqual(
            self.conn.execute("SELECT title, url, text, created_at, descendants FROM posts WHERE id=1").fetchone(),
            ("new", "", "changed", 123, 6),
        )
        self.assertEqual(self.progress(), [(101, 1, 100)])

    def test_failure_during_row_writes_rolls_back_the_whole_page(self):
        start_history(self.conn)
        commit_page(self.conn, [post(1)], next_id=2)
        with self.assertRaises(sqlite3.IntegrityError):
            commit_page(self.conn, [post(2), post(3, descendants=4)], next_id=4)
        self.reopen()
        self.assertEqual(self.conn.execute("SELECT id FROM posts").fetchall(), [(1,)])
        self.assertEqual(self.progress(), [(2, 0, 100)])

    def test_cursor_write_failure_also_rolls_back_new_posts(self):
        start_history(self.conn)
        commit_page(self.conn, [post(1)], next_id=2)
        with self.conn:
            self.conn.execute("""CREATE TRIGGER fail_cursor BEFORE UPDATE ON collection_progress
                BEGIN SELECT RAISE(ABORT, 'cursor failure'); END""")
        with self.assertRaises(sqlite3.IntegrityError):
            commit_page(self.conn, [post(2)], next_id=3, complete=True)
        self.reopen()
        self.assertEqual(self.conn.execute("SELECT id FROM posts").fetchall(), [(1,)])
        self.assertEqual(self.progress(), [(2, 0, 100)])

    def test_failed_sqlite_commit_rolls_back_posts_and_cursor(self):
        start_history(self.conn)
        commit_page(self.conn, [post(1)], next_id=2)
        self.conn.execute("PRAGMA busy_timeout = 1")
        with closing(sqlite3.connect(self.path, autocommit=False)) as reader:
            reader.execute("SELECT * FROM posts").fetchall()
            with self.assertRaisesRegex(sqlite3.OperationalError, "locked"):
                commit_page(self.conn, [post(2)], next_id=3)
        self.reopen()
        self.assertEqual(self.conn.execute("SELECT id FROM posts").fetchall(), [(1,)])
        self.assertEqual(self.progress(), [(2, 0, 100)])

    def test_keyboard_interrupt_during_a_page_rolls_back_its_rows(self):
        start_history(self.conn)

        def interrupted_page():
            yield post(1)
            raise KeyboardInterrupt

        with self.assertRaises(KeyboardInterrupt):
            commit_page(self.conn, interrupted_page(), next_id=2)
        self.reopen()
        self.assertEqual(self.conn.execute("SELECT * FROM posts").fetchall(), [])
        self.assertEqual(self.progress(), [(1, 0, 100)])

    def test_killed_process_retains_reported_commit_and_rolls_back_uncommitted_page(self):
        script = """
import sys
from hn_search.catalog import open_catalog, commit_page
from hn_search.clickhouse import Post
conn = open_catalog(sys.argv[1])
with conn:
    conn.execute('INSERT INTO collection_progress VALUES (1, 0, 100)')
commit_page(conn, [Post(1, 'saved', '', '', 1, 5)], next_id=2)
if sys.argv[2] == 'during_page':
    def page():
        yield Post(2, 'pending', '', '', 2, 5)
        print('ready', flush=True)
        sys.stdin.read(1)
    commit_page(conn, page(), next_id=3)
else:
    print('ready', flush=True)
    sys.stdin.read(1)
"""
        for mode in ("after_commit", "during_page"):
            with self.subTest(mode=mode):
                path = Path(self.directory.name) / f"{mode}.sqlite3"
                proc = subprocess.Popen(
                    [sys.executable, "-c", script, str(path), mode], cwd=ROOT,
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    text=True,
                )
                try:
                    readable, _, _ = select.select([proc.stdout], [], [], 10)
                    self.assertTrue(readable, "child did not reach the commit boundary")
                    self.assertEqual(proc.stdout.readline().strip(), "ready")
                finally:
                    proc.kill()
                    proc.communicate(timeout=5)
                with closing(open_catalog(path)) as reopened:
                    self.assertEqual(reopened.execute("SELECT id FROM posts").fetchall(), [(1,)])
                    self.assertEqual(reopened.execute("SELECT * FROM collection_progress").fetchall(), [(2, 0, 100)])
