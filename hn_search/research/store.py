"""Additive schema-v3 storage and exact, per-unit result reuse."""

import json
from dataclasses import astuple, dataclass
from pathlib import Path

from hn_search.catalog import migrate_archives


@dataclass(frozen=True)
class ResultKey:
    stage: str
    story_id: int
    part: int
    prompt_version: str
    model: str
    effort: str
    input_key: str
    question: str


@dataclass(frozen=True)
class SavedResult:
    id: int
    key: ResultKey
    result: dict


KEY_COLUMNS = "stage, story_id, part, prompt_version, model, effort, input_key, question"
KEY_WHERE = " AND ".join(column.strip() + " = ?" for column in KEY_COLUMNS.split(","))


def migrate(conn):
    if conn.execute("PRAGMA user_version").fetchone()[0] < 2:
        migrate_archives(conn)
    with conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS research_runs (
            id INTEGER PRIMARY KEY, started_at INTEGER NOT NULL, finished_at INTEGER,
            folder TEXT NOT NULL UNIQUE, question TEXT NOT NULL, keywords TEXT NOT NULL,
            settings TEXT NOT NULL
        )""")
        conn.execute("""CREATE TABLE IF NOT EXISTS research_run_stories (
            run_id INTEGER NOT NULL, story_id INTEGER NOT NULL,
            status TEXT NOT NULL CHECK (status IN (
                'matched', 'not_downloaded', 'unavailable', 'uncertain', 'irrelevant', 'relevant')),
            reason TEXT NOT NULL DEFAULT '', PRIMARY KEY (run_id, story_id)
        )""")
        conn.execute("""CREATE TABLE IF NOT EXISTS ai_results (
            id INTEGER PRIMARY KEY, run_id INTEGER NOT NULL,
            stage TEXT NOT NULL CHECK (stage IN ('description', 'verdict', 'analysis', 'synthesis')),
            story_id INTEGER NOT NULL, part INTEGER NOT NULL, prompt_version TEXT NOT NULL,
            model TEXT NOT NULL, effort TEXT NOT NULL, input_key TEXT NOT NULL, question TEXT NOT NULL,
            result TEXT NOT NULL, cited_ids TEXT NOT NULL, call_usage TEXT NOT NULL, created_at INTEGER NOT NULL,
            UNIQUE (stage, story_id, part, prompt_version, model, effort, input_key, question)
        )""")
        if conn.execute("PRAGMA user_version").fetchone()[0] < 3:
            conn.execute("PRAGMA user_version = 3")


def next_id(conn):
    return conn.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM research_runs").fetchone()[0]


def next_folder(conn, out):
    return Path(out).resolve() / f"run-{next_id(conn)}"


def create_run(conn, out, question, keywords, settings, story_ids, *, now):
    run_id = next_id(conn)
    folder = Path(out).resolve() / f"run-{run_id}"
    made = False
    try:
        with conn:
            conn.execute("""INSERT INTO research_runs
                (id, started_at, folder, question, keywords, settings) VALUES (?, ?, ?, ?, ?, ?)""",
                (run_id, int(now), str(folder), question, json.dumps(keywords), json.dumps(settings)))
            conn.executemany("INSERT INTO research_run_stories (run_id, story_id, status) VALUES (?, ?, 'matched')",
                             ((run_id, story_id) for story_id in story_ids))
            folder.parent.mkdir(parents=True, exist_ok=True)
            folder.mkdir(exist_ok=False)
            made = True
    except BaseException:
        if made:
            folder.rmdir()  # Only our just-created, still-empty folder.
        raise
    return run_id, folder


def lookup(conn, key):
    row = conn.execute(f"SELECT id, result FROM ai_results WHERE {KEY_WHERE}", astuple(key)).fetchone()
    return None if row is None else SavedResult(row[0], key, json.loads(row[1]))


def save_call(conn, run_id, results, usage, *, now, statuses=()):
    """Save a checked call's rows and any completed verdicts in one transaction."""
    saved = []
    with conn:
        for key, result, citations in results:
            cursor = conn.execute(f"""INSERT INTO ai_results
                (run_id, {KEY_COLUMNS}, result, cited_ids, call_usage, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (run_id, *astuple(key), json.dumps(result, ensure_ascii=False),
                 json.dumps(sorted(citations)), json.dumps(usage), int(now)))
            saved.append(SavedResult(cursor.lastrowid, key, result))
        for story_id, status, reason in statuses:
            conn.execute("UPDATE research_run_stories SET status = ?, reason = ? WHERE run_id = ? AND story_id = ?",
                         (status, reason, run_id, story_id))
    return saved


def set_status(conn, run_id, story_id, status, reason=""):
    with conn:
        conn.execute("UPDATE research_run_stories SET status = ?, reason = ? WHERE run_id = ? AND story_id = ?",
                     (status, reason, run_id, story_id))


def coverage(conn, run_id):
    return conn.execute("""SELECT p.id, p.title, r.status, r.reason FROM research_run_stories r
        JOIN posts p ON p.id = r.story_id WHERE r.run_id = ? ORDER BY p.id""", (run_id,)).fetchall()


def finish_run(conn, run_id, *, now):
    with conn:
        conn.execute("UPDATE research_runs SET finished_at = ? WHERE id = ?", (int(now), run_id))
