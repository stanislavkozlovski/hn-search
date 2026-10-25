"""Run the retained historical sweep before a fresh five-day scan."""

import time
from urllib.request import urlopen

from hn_search import catalog, clickhouse


def _progress(conn, mode, selection, next_id, complete):
    saved_posts = conn.execute("SELECT count(*) FROM posts").fetchone()[0]
    print(
        f"{mode} source={clickhouse.SOURCE} {selection} next_id={next_id} "
        f"complete={str(complete).lower()} saved_posts={saved_posts}",
        flush=True,
    )


def collect_history(conn, *, opener=urlopen):
    progress = conn.execute(
        "SELECT next_id, complete, through_id FROM collection_progress"
    ).fetchone()
    if progress is None:
        through_id = clickhouse.max_id(opener=opener)
        next_id, complete = 1, False
        with conn:
            conn.execute(
                "INSERT INTO collection_progress (next_id, complete, through_id) "
                "VALUES (?, ?, ?)",
                (next_id, complete, through_id),
            )
    else:
        next_id, complete, through_id = progress
        complete = bool(complete)

    selection = f"range=1..{through_id}"
    if complete:
        _progress(conn, "historical", selection, next_id, complete)
        return
    while not complete:
        posts = clickhouse.fetch_page(next_id, through_id=through_id, opener=opener)
        complete = len(posts) < clickhouse.PAGE_SIZE
        next_id = through_id + 1 if complete else posts[-1].id + 1
        catalog.commit_page(conn, posts, next_id=next_id, complete=complete)
        _progress(conn, "historical", selection, next_id, complete)


def collect_daily(conn, *, opener=urlopen, clock=time.time):
    window_end = int(clock())
    window_start = window_end - 432_000
    next_id = 1
    complete = False
    while not complete:
        posts = clickhouse.fetch_page(
            next_id,
            window_start=window_start,
            window_end=window_end,
            opener=opener,
        )
        complete = len(posts) < clickhouse.PAGE_SIZE
        if posts:
            next_id = posts[-1].id + 1
        catalog.commit_page(conn, posts)
        _progress(
            conn,
            "daily",
            f"window=[{window_start},{window_end})",
            next_id,
            complete,
        )
