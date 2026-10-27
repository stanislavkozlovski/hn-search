"""Immutable, resumable HN item archives with a single SQLite writer."""

from collections import deque
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from dataclasses import dataclass
import json
from pathlib import Path
import time
from urllib.request import urlopen

from hn_search.archive_export import archive_counts, load_items, write_exports
from hn_search.catalog import migrate_archives


class UncataloguedStories(ValueError):
    def __init__(self, roots):
        self.roots = roots
        super().__init__(f"Stories absent from the catalog: {', '.join(map(str, roots))}")


def _invalid_constant(value):
    raise ValueError(f"Invalid JSON constant: {value}")


def fetch_item(item_id, *, opener, clock):
    """Workers perform only HTTP, validation, and retrieval timestamping."""
    url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
    with opener(url, timeout=30) as response:
        item = json.loads(response.read(), parse_constant=_invalid_constant)
    if item is not None:
        if not isinstance(item, dict) or type(item.get("id")) is not int or item["id"] != item_id:
            raise ValueError(f"Invalid HN item {item_id}: expected an object with matching id, or null")
        for key in ("by", "title", "text", "url", "type"):
            if key in item and not isinstance(item[key], str):
                raise ValueError(f"Invalid HN item {item_id}: {key} must be a string")
        for key in ("time", "descendants", "score", "parent"):
            if key in item and (type(item[key]) is not int or item[key] < (1 if key == "parent" else 0)):
                raise ValueError(f"Invalid HN item {item_id}: {key} must be a valid integer")
        for key in ("deleted", "dead"):
            if key in item and type(item[key]) is not bool:
                raise ValueError(f"Invalid HN item {item_id}: {key} must be a boolean")
        for key in ("kids", "parts"):
            if key in item and (not isinstance(item[key], list) or any(type(i) is not int or i <= 0 for i in item[key])):
                raise ValueError(f"Invalid HN item {item_id}: {key} must contain positive integer IDs")
    return item, int(clock())


def children(root, item_id, item):
    if item is None:
        return []
    ids = list(item.get("kids", []))
    if item_id == root and item.get("type") == "poll":
        ids.extend(item.get("parts", []))
    return ids


@dataclass
class _Root:
    items: dict
    pending: deque
    seen: set


def _resume(conn, root):
    items = load_items(conn, root)
    queue = deque([root])
    seen = {root}
    pending = deque()
    while queue:
        item_id = queue.popleft()
        if item_id not in items:
            pending.append(item_id)
            continue
        for child in children(root, item_id, items[item_id][0]):
            if child not in seen:
                seen.add(child)
                queue.append(child)
    return _Root(items, pending, seen)


def _print_progress(root, state, *, paths=None, reused=False):
    counts = archive_counts(root, state.items)
    line = f"archive root={root} status={'complete' if paths else 'incomplete'} comments={counts['comments']}"
    if paths:
        line += f" unavailable={counts['unavailable']} reported_descendants={counts['reported_descendants']}"
        line += f" json={paths[0]} markdown={paths[1]}"
        if reused:
            line += " reused=true"
    else:
        line += f" pending={len(state.pending)}"
    print(line, flush=True)


def archive(conn, roots, export_dir, *, opener=urlopen, clock=time.time):
    """Download batches of up to eight roots; propagate errors after draining."""
    roots = list(dict.fromkeys(roots))
    missing = [root for root in roots if conn.execute("SELECT 1 FROM posts WHERE id = ?", (root,)).fetchone() is None]
    if missing:
        raise UncataloguedStories(missing)
    if not roots:
        return
    migrate_archives(conn)
    waiting = deque(roots)
    active = {}
    in_flight = {}
    first_error = None
    incomplete_finalizations = {}

    def finish(root, state, *, reused=False):
        nonlocal first_error
        completed = reused
        try:
            if not reused:
                with conn:
                    conn.execute("UPDATE archives SET finished_at = ? WHERE root_id = ? AND finished_at IS NULL", (int(clock()), root))
                completed = True
            paths = write_exports(conn, root, Path(export_dir))
            _print_progress(root, state, paths=paths, reused=reused)
        except Exception as error:
            error.add_note(f"archive root={root} export_dir={export_dir}")
            if not completed:
                incomplete_finalizations[root] = state
            if first_error is None:
                first_error = error

    with ThreadPoolExecutor(max_workers=8) as pool:
        while waiting or active:
            if first_error is None:
                while waiting and len(active) < 8 and first_error is None:
                    root = waiting.popleft()
                    row = conn.execute("SELECT status FROM archives WHERE root_id = ?", (root,)).fetchone()
                    if row and row[0] == "complete":
                        finish(root, _resume(conn, root), reused=True)
                    else:
                        with conn:
                            conn.execute("INSERT OR IGNORE INTO archives (root_id, started_at) VALUES (?, ?)", (root, int(clock())))
                        active[root] = _resume(conn, root)

            busy = {root for root, _ in in_flight.values()}
            for root, state in list(active.items()):
                if not state.pending and root not in busy:
                    finish(root, state)
                    del active[root]

            if first_error is None:
                for root, state in active.items():
                    if root not in busy and state.pending:
                        item_id = state.pending[0]
                        future = pool.submit(fetch_item, item_id, opener=opener, clock=clock)
                        in_flight[future] = root, item_id
            else:
                for future in list(in_flight):
                    if future.cancel():
                        del in_flight[future]

            if not in_flight:
                if first_error is not None:
                    break
                continue

            done, _ = wait(in_flight, return_when=FIRST_COMPLETED)
            # Include any other futures already complete before another dispatch.
            done.update(future for future in in_flight if future.done())
            for future in done:
                root, item_id = in_flight.pop(future)
                state = active[root]
                try:
                    item, retrieved_at = future.result()
                    with conn:
                        conn.execute("INSERT INTO archive_items VALUES (?, ?, ?, ?)", (root, item_id, json.dumps(item, ensure_ascii=False), retrieved_at))
                except Exception as error:
                    error.add_note(f"archive root={root} item={item_id}")
                    if first_error is None:
                        first_error = error
                else:
                    state.items[item_id] = item, retrieved_at
                    state.pending.popleft()
                    for child in children(root, item_id, item):
                        if child not in state.seen:
                            state.seen.add(child)
                            state.pending.append(child)

    if first_error is not None:
        for root, state in (active | incomplete_finalizations).items():
            _print_progress(root, state)
        raise first_error


def archive_story(conn, root, export_dir, *, opener=urlopen, clock=time.time):
    """Use the batch scheduler for one root with the caller's connection."""
    return archive(conn, [root], export_dir, opener=opener, clock=clock)
