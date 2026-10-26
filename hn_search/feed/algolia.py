"""One complete Algolia response, validated before any feed writes."""

import json
import re
from urllib.parse import urlencode

from hn_search.feed import Story

LOOKBACK_SECONDS = 36000


def _integer(value, name, minimum):
    if type(value) is not int or not minimum <= value < 2**63:
        raise ValueError(f"Invalid Algolia {name}")
    return value


def fetch_window(now, *, opener):
    query = urlencode({
        "tags": "story",
        "numericFilters": f"created_at_i>{now - LOOKBACK_SECONDS},points>=5",
        "hitsPerPage": 1000,
    })
    with opener(f"https://hn.algolia.com/api/v1/search_by_date?{query}", timeout=30) as response:
        body = json.load(response)
    if not isinstance(body, dict) or not isinstance(body.get("hits"), list):
        raise ValueError("Invalid Algolia hits")
    hits = body["hits"]
    if _integer(body.get("nbHits"), "nbHits", 0) > len(hits) or len(hits) > 1000:
        raise ValueError("Truncated Algolia window")
    stories, seen = [], set()
    for hit in hits:
        if not isinstance(hit, dict):
            raise ValueError("Invalid Algolia hit")
        object_id = hit.get("objectID")
        if not isinstance(object_id, str) or not re.fullmatch(r"[0-9]+", object_id):
            raise ValueError("Invalid Algolia objectID")
        story_id = _integer(int(object_id), "objectID", 1)
        if story_id in seen:
            raise ValueError("Repeated Algolia objectID")
        seen.add(story_id)
        title = hit.get("title")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Invalid Algolia title")
        url = hit.get("url")
        if url is not None and not isinstance(url, str):
            raise ValueError("Invalid Algolia url")
        created_at = _integer(hit.get("created_at_i"), "created_at_i", now - LOOKBACK_SECONDS + 1)
        points = _integer(hit.get("points"), "points", 5)
        stories.append(Story(story_id, title, url or None, created_at, points))
    return stories
