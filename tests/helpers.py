from io import BytesIO
import json
from threading import Lock
from urllib.parse import parse_qs, urlsplit

from hn_search.clickhouse import Post


NOW = 1_800_000_000


def row(post_id=1, **changes):
    record = dict(
        id=post_id,
        title="A post",
        url="https://example.com/article",
        text="",
        created_at=NOW - 60,
        descendants=5,
    )
    record.update(changes)
    return record


def post(post_id=1, **changes):
    return Post(**row(post_id, **changes))


def result(records, **changes):
    payload = {"data": records, "rows": len(records)}
    payload.update(changes)
    return json.dumps(payload, ensure_ascii=False).encode("utf-8")


class ScriptedOpener:
    """Serve complete responses or failures, recording every HTTP request."""

    def __init__(self, *responses):
        self.responses = iter(responses)
        self.requests = []
        self.timeouts = []

    def __call__(self, url, *, timeout):
        parts = urlsplit(url)
        if (parts.scheme, parts.netloc, parts.path) != (
            "https", "play.clickhouse.com", "/"
        ):
            raise AssertionError(f"Unexpected HTTP destination: {url}")
        self.requests.append(
            {key: values[0] for key, values in parse_qs(parts.query).items()}
        )
        self.timeouts.append(timeout)
        response = next(self.responses)
        if isinstance(response, BaseException):
            raise response
        return BytesIO(response if isinstance(response, bytes) else result(response))


class HNOpener:
    """ID-keyed HN fixtures, including event-controlled concurrent responses."""

    def __init__(self, responses=None):
        self.responses = responses or {}
        self.requests = []
        self.timeouts = []
        self.lock = Lock()

    def __call__(self, url, *, timeout):
        parts = urlsplit(url)
        item_id = int(parts.path.removeprefix("/v0/item/").removesuffix(".json"))
        if url != f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json":
            raise AssertionError(f"Unexpected HTTP destination: {url}")
        with self.lock:
            self.requests.append(item_id)
            self.timeouts.append(timeout)
        response = self.responses[item_id]
        if callable(response):
            response = response()
        if isinstance(response, BaseException):
            raise response
        return BytesIO(response if isinstance(response, bytes) else json.dumps(response, ensure_ascii=False).encode())


def start_history(conn, *, next_id=1, complete=False, through_id=100):
    with conn:
        conn.execute(
            "INSERT INTO collection_progress VALUES (?, ?, ?)",
            (next_id, complete, through_id),
        )
