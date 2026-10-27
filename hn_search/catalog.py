"""SQLite metadata and atomic historical checkpoints."""

import sqlite3


def open_catalog(path):
    conn = sqlite3.connect(path, autocommit=False)
    try:
        with conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                url TEXT NOT NULL,
                text TEXT NOT NULL,
                created_at INTEGER NOT NULL,
                descendants INTEGER NOT NULL CHECK (descendants >= 5),
                hn_url TEXT GENERATED ALWAYS AS (
                    'https://news.ycombinator.com/item?id=' || id
                ) VIRTUAL
            )""")
            conn.execute("""CREATE TABLE IF NOT EXISTS collection_progress (
                next_id INTEGER NOT NULL,
                complete INTEGER NOT NULL CHECK (complete IN (0, 1)),
                through_id INTEGER
            )""")
            if conn.execute("PRAGMA user_version").fetchone()[0] == 0:
                conn.execute("PRAGMA user_version = 1")
    except BaseException:
        conn.close()
        raise
    return conn


def commit_page(conn, posts, *, next_id=None, complete=False):
    """Upsert a page and, for history only, advance its cursor atomically."""
    with conn:
        conn.executemany(
            """INSERT INTO posts (id, title, url, text, created_at, descendants)
               VALUES (?, ?, ?, ?, ?, ?)
               ON CONFLICT(id) DO UPDATE SET
                   title = excluded.title,
                   url = excluded.url,
                   text = excluded.text,
                   created_at = excluded.created_at,
                   descendants = excluded.descendants""",
            (
                (p.id, p.title, p.url, p.text, p.created_at, p.descendants)
                for p in posts
            ),
        )
        if next_id is not None:
            conn.execute(
                "UPDATE collection_progress SET next_id = ?, complete = ?",
                (next_id, complete),
            )


def migrate_archives(conn):
    """Add archive storage atomically without changing the metadata collector."""
    with conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS archives (
            root_id INTEGER PRIMARY KEY,
            status TEXT GENERATED ALWAYS AS (
                CASE WHEN finished_at IS NULL THEN 'incomplete' ELSE 'complete' END
            ) VIRTUAL,
            started_at INTEGER NOT NULL,
            finished_at INTEGER
        )""")
        conn.execute("""CREATE TABLE IF NOT EXISTS archive_items (
            root_id INTEGER NOT NULL,
            item_id INTEGER NOT NULL,
            item_json TEXT NOT NULL,
            retrieved_at INTEGER NOT NULL,
            PRIMARY KEY (root_id, item_id)
        )""")
        if conn.execute("PRAGMA user_version").fetchone()[0] < 2:
            conn.execute("PRAGMA user_version = 2")
