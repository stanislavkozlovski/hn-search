"""Feed schema and short transactions; no research-catalog writes or bot tokens."""

import json
import sqlite3

from hn_search.feed import MAX_SHOWN_POINTS, Batch, Line, Message

APPLICATION_ID = 0x484E4644
SCHEMA_VERSION = 1
SCHEMA = (
    """CREATE TABLE stories (
        id INTEGER PRIMARY KEY, title TEXT NOT NULL, url TEXT,
        created_at INTEGER NOT NULL, first_seen_at INTEGER NOT NULL)""",
    """CREATE TABLE observations (
        story_id INTEGER NOT NULL REFERENCES stories(id), observed_at INTEGER NOT NULL,
        points INTEGER NOT NULL, PRIMARY KEY (story_id, observed_at))""",
    "CREATE TABLE lenses (name TEXT PRIMARY KEY, added_at INTEGER NOT NULL)",
    """CREATE TABLE decisions (
        lens TEXT NOT NULL REFERENCES lenses(name), story_id INTEGER NOT NULL REFERENCES stories(id),
        title TEXT NOT NULL, url TEXT, categories_digest TEXT NOT NULL,
        categories TEXT NOT NULL, decided_at INTEGER NOT NULL, PRIMARY KEY (lens, story_id))""",
    """CREATE TABLE messages (
        id INTEGER PRIMARY KEY, bot_token_env TEXT NOT NULL, chat_id INTEGER NOT NULL,
        telegram_message_id INTEGER NOT NULL, sent_at INTEGER NOT NULL)""",
    """CREATE TABLE message_lines (
        message_id INTEGER NOT NULL REFERENCES messages(id), position INTEGER NOT NULL,
        lens TEXT NOT NULL, story_id INTEGER NOT NULL REFERENCES stories(id), tags TEXT NOT NULL,
        title TEXT NOT NULL, url TEXT, shown_points TEXT NOT NULL,
        PRIMARY KEY (message_id, position), UNIQUE (lens, story_id))""",
    """CREATE VIEW story_growth AS
        SELECT DISTINCT story_id,
          (first_value(points) OVER w) || ' → ' || (last_value(points) OVER w) || ' points over '
            || ((last_value(observed_at) OVER w - first_value(observed_at) OVER w) / 60) || ' minutes' AS growth
        FROM observations
        WINDOW w AS (PARTITION BY story_id ORDER BY observed_at
                     ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)""",
)


def open_feed(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        application_id = conn.execute("PRAGMA application_id").fetchone()[0]
        version = conn.execute("PRAGMA user_version").fetchone()[0]
        has_tables = conn.execute("SELECT 1 FROM sqlite_master WHERE type = 'table' LIMIT 1").fetchone()
        if application_id == APPLICATION_ID:
            if version != SCHEMA_VERSION:
                raise ValueError(f"Unsupported feed user_version: {version}")
        elif has_tables or application_id != 0 or version != 0:
            raise ValueError("Refusing a database that is not an HN feed")
        else:
            with conn:
                conn.execute("BEGIN")
                for statement in SCHEMA:
                    conn.execute(statement)
                conn.execute(f"PRAGMA application_id = {APPLICATION_ID}")
                conn.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
    except BaseException:
        conn.close()
        raise
    return conn


def save_window(conn, lenses, stories, now):
    new = 0
    with conn:
        for lens in lenses:
            conn.execute("INSERT INTO lenses VALUES (?, ?) ON CONFLICT DO NOTHING", (lens.name, now))
        for story in stories:
            new += conn.execute("SELECT 1 FROM stories WHERE id = ?", (story.id,)).fetchone() is None
            conn.execute("""INSERT INTO stories VALUES (?, ?, ?, ?, ?)
                ON CONFLICT (id) DO UPDATE SET title = excluded.title, url = excluded.url""",
                (story.id, story.title, story.url, story.created_at, now))
            conn.execute("""INSERT INTO observations VALUES (?, ?, ?)
                ON CONFLICT (story_id, observed_at) DO UPDATE SET points = excluded.points""",
                (story.id, now, story.points))
    return new


def _current_tags(conn, lens, story):
    """Return the saved tags if the lens judged this title, URL, and categories; otherwise None."""
    row = conn.execute("""SELECT categories FROM decisions WHERE lens = ? AND story_id = ?
        AND title = ? AND url IS ? AND categories_digest = ?""",
        (lens.name, story.id, story.title, story.url, lens.categories_digest)).fetchone()
    return None if row is None else tuple(json.loads(row[0]))


def batches_to_judge(conn, lenses, stories, size=20):
    waiting = []
    needed = set()
    for story in sorted(stories, key=lambda story: story.id):
        first_seen = conn.execute("SELECT first_seen_at FROM stories WHERE id = ?", (story.id,)).fetchone()[0]
        for lens in lenses:
            added_at = conn.execute("SELECT added_at FROM lenses WHERE name = ?", (lens.name,)).fetchone()[0]
            if first_seen >= added_at and _current_tags(conn, lens, story) is None:
                needed.add((lens.name, story.id))
        if any((lens.name, story.id) in needed for lens in lenses):
            waiting.append(story)
    for offset in range(0, len(waiting), size):
        selected = tuple(waiting[offset:offset + size])
        ids = {story.id for story in selected}
        pairs = frozenset(pair for pair in needed if pair[1] in ids)
        yield Batch(selected, tuple(lens for lens in lenses if any(pair[0] == lens.name for pair in pairs)), pairs)


def save_decisions(conn, decisions, now):
    with conn:
        for decision in decisions:
            conn.execute("""INSERT INTO decisions VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT (lens, story_id) DO UPDATE SET title = excluded.title, url = excluded.url,
                categories_digest = excluded.categories_digest, categories = excluded.categories,
                decided_at = excluded.decided_at""", (
                decision.lens, decision.story.id, decision.story.title, decision.story.url,
                decision.categories_digest, json.dumps(decision.categories), now,
            ))


def _points(conn, story_id):
    values = []
    for row in conn.execute("SELECT points FROM observations WHERE story_id = ? ORDER BY observed_at", (story_id,)):
        if not values or values[-1] != row[0]:
            values.append(row[0])
    # Retain first discovery and the most recent observations on manual reruns.
    return tuple(values if len(values) <= MAX_SHOWN_POINTS else [values[0], *values[1 - MAX_SHOWN_POINTS:]])


def pending_lines(conn, lenses, stories):
    destinations = {}
    for lens in lenses:
        destination = (lens.bot_token_env, lens.chat_id)
        for story in sorted(stories, key=lambda story: story.id):
            tags = _current_tags(conn, lens, story)
            if not tags:
                continue
            if conn.execute("SELECT 1 FROM message_lines WHERE lens = ? AND story_id = ?", (lens.name, story.id)).fetchone():
                continue
            destinations.setdefault(destination, []).append(Line(
                lens.name, story.id, tags, story.title, story.url, _points(conn, story.id),
            ))
    return [Message(bot, chat, tuple(lines)) for (bot, chat), lines in destinations.items()]


def record_message(conn, message, telegram_message_id, now):
    with conn:
        message_id = conn.execute("""INSERT INTO messages (bot_token_env, chat_id, telegram_message_id, sent_at)
            VALUES (?, ?, ?, ?)""", (message.bot_token_env, message.chat_id, telegram_message_id, now)).lastrowid
        for position, line in enumerate(message.lines):
            conn.execute("INSERT INTO message_lines VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (
                message_id, position, line.lens, line.story_id, json.dumps(line.tags),
                line.title, line.url, json.dumps(line.shown_points),
            ))


def messages_to_edit(conn, lenses, stories):
    destinations = {(lens.bot_token_env, lens.chat_id) for lens in lenses}
    current = {story.id: story.points for story in stories}
    for row in conn.execute("SELECT * FROM messages ORDER BY id"):
        if (row["bot_token_env"], row["chat_id"]) not in destinations:
            continue
        lines, changed = [], False
        for saved in conn.execute("SELECT * FROM message_lines WHERE message_id = ? ORDER BY position", (row["id"],)):
            points = tuple(json.loads(saved["shown_points"]))
            if saved["story_id"] in current and len(points) < MAX_SHOWN_POINTS and current[saved["story_id"]] != points[-1]:
                points += (current[saved["story_id"]],)
                changed = True
            lines.append(Line(saved["lens"], saved["story_id"], tuple(json.loads(saved["tags"])), saved["title"], saved["url"], points))
        if changed:
            yield Message(row["bot_token_env"], row["chat_id"], tuple(lines), row["telegram_message_id"], row["id"])


def record_edit(conn, message):
    with conn:
        for position, line in enumerate(message.lines):
            conn.execute("UPDATE message_lines SET shown_points = ? WHERE message_id = ? AND position = ?",
                         (json.dumps(line.shown_points), message.id, position))
