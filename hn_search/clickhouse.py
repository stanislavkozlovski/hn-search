"""Read bounded metadata pages from ClickHouse's historical HN mirror."""

from dataclasses import dataclass
import json
from urllib.parse import urlencode
from urllib.request import urlopen


SOURCE = "play.clickhouse.com/hackernews_history"
PAGE_SIZE = 10_000
SETTINGS = """SETTINGS result_overflow_mode = 'throw',
         timeout_overflow_mode = 'throw',
         read_overflow_mode = 'throw'
FORMAT JSON"""


@dataclass(frozen=True)
class Post:
    id: int
    title: str
    url: str
    text: str
    created_at: int
    descendants: int


def _query(sql, parameters, opener):
    parameters = {f"param_{name}": value for name, value in parameters.items()}
    url = "https://play.clickhouse.com/?" + urlencode(
        {"user": "play", "wait_end_of_query": 1, "query": sql, **parameters}
    )
    with opener(url, timeout=90) as response:
        payload = json.loads(response.read())
    if not isinstance(payload, dict) or any(
        key in payload for key in ("exception", "__exception__")
    ):
        raise ValueError("ClickHouse did not return a successful JSON result")
    data = payload.get("data")
    rows = payload.get("rows")
    if (
        not isinstance(data, list)
        or type(rows) is not int
        or rows != len(data)
        or not all(isinstance(row, dict) for row in data)
    ):
        raise ValueError("ClickHouse returned an invalid data/rows result")
    return data


def _integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"Invalid ClickHouse {name}: {value!r}")
    return value


def max_id(*, opener=urlopen):
    rows = _query(
        "SELECT max(id) AS max_id FROM hackernews_history\n" + SETTINGS, {}, opener
    )
    if len(rows) != 1:
        raise ValueError("ClickHouse did not return one historical bound")
    return _integer(rows[0].get("max_id"), "max_id")


def fetch_page(
    next_id,
    *,
    through_id=None,
    window_start=None,
    window_end=None,
    opener=urlopen,
):
    """Return a fully validated page, or raise before any catalog write."""
    parameters = {"next_id": next_id}
    predicates = ["id >= {next_id:UInt32}"]
    if through_id is not None:
        if window_start is not None or window_end is not None:
            raise ValueError("A page must select either history or a daily window")
        parameters["through_id"] = through_id
        predicates.append("id <= {through_id:UInt32}")
    else:
        if window_start is None or window_end is None:
            raise ValueError("A daily page requires both window bounds")
        parameters.update(window_start=window_start, window_end=window_end)
        predicates.extend(
            [
                "time >= toDateTime({window_start:UInt32}, 'UTC')",
                "time < toDateTime({window_end:UInt32}, 'UTC')",
            ]
        )
    predicates.extend(
        [
            "type IN ('story', 'poll', 'job')",
            "parent = 0",
            "deleted = 0",
            "descendants >= 5",
        ]
    )
    sql = (
        "SELECT id, title, url, text, toUnixTimestamp(time) AS created_at, descendants\n"
        "FROM hackernews_history FINAL\nWHERE "
        + " AND ".join(predicates)
        + f"\nORDER BY id LIMIT {PAGE_SIZE}\n"
        + SETTINGS
    )
    rows = _query(sql, parameters, opener)
    if len(rows) > PAGE_SIZE:
        raise ValueError("ClickHouse returned more than one page")

    posts = []
    previous_id = next_id - 1
    for row in rows:
        post_id = _integer(row.get("id"), "id", minimum=1)
        created_at = _integer(row.get("created_at"), "created_at")
        descendants = _integer(row.get("descendants"), "descendants", minimum=5)
        if post_id <= previous_id or (
            through_id is not None and post_id > through_id
        ):
            raise ValueError("ClickHouse returned unordered or out-of-range IDs")
        if through_id is None and not window_start <= created_at < window_end:
            raise ValueError("ClickHouse returned a post outside the daily window")
        for field in ("title", "url", "text"):
            if not isinstance(row.get(field), str):
                raise ValueError(f"Invalid ClickHouse {field} for post {post_id}")
        posts.append(
            Post(post_id, row["title"], row["url"], row["text"], created_at, descendants)
        )
        previous_id = post_id
    return posts
