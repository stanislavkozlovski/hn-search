"""Deterministic metadata matching and the mandatory work gate."""

import html
from dataclasses import dataclass
from types import SimpleNamespace


def normalize(text):
    words = "".join(char if char.isalnum() else " " for char in html.unescape(text).lower())
    return " ".join(words.split())


def normalize_keywords(keywords):
    return list(dict.fromkeys(value for keyword in keywords if (value := normalize(keyword))))


@dataclass(frozen=True)
class SearchResult:
    posts: dict
    by_keyword: dict


def search(conn, keywords):
    keywords = normalize_keywords(keywords)
    found = {keyword: [] for keyword in keywords}
    posts = {}
    cursor = conn.execute("SELECT id, title, url, text, descendants FROM posts ORDER BY id")
    for story_id, title, url, text, descendants in cursor:
        fields = tuple(" " + normalize(value) + " " for value in (title, url, text))
        matched = [keyword for keyword in keywords if any(" " + keyword + " " in field for field in fields)]
        if matched:
            posts[story_id] = {"id": story_id, "title": title, "descendants": descendants}
            for keyword in matched:
                found[keyword].append(story_id)
    return SearchResult(posts, found)


def gate_lines(matches, *, room, reused=()):
    from .threads import pack

    if room <= 0:
        raise ValueError("the question and prompt leave no input budget for stories")
    reused = set(reused)
    total_comments = sum(post["descendants"] for post in matches.posts.values())
    counts = " · ".join(f"{keyword} {len(ids)}" for keyword, ids in matches.by_keyword.items())
    lines = [f"{len(matches.posts)} stories match ({total_comments:,} reported comments): {counts}",
             "Top matches by reported comments:"]
    for keyword, ids in matches.by_keyword.items():
        for index, story_id in enumerate(sorted(ids, key=lambda sid: (-matches.posts[sid]["descendants"], sid))[:3]):
            post = matches.posts[story_id]
            lines.append(f"  {keyword if index == 0 else '':20} {story_id:10} {post['descendants']:6}  {post['title']}")
    estimates = []
    for story_id, post in matches.posts.items():
        if story_id not in reused:
            size = post["descendants"] * 92
            part = 0
            while size:
                estimates.append(SimpleNamespace(size=min(size, room), story_id=story_id, part=part))
                size -= min(size, room)
                part += 1
    calls = len(pack(estimates, room)) * 2
    lines.extend([
        f"Next: download {len(matches.posts)} stories, then about {calls} batched classification calls "
        f"({len(reused)} stories reused), one analysis per relevant story, and one report.",
        "Proceed, or say how to change the keywords?",
    ])
    return lines
