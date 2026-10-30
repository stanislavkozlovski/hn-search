import copy
import json
import re
from types import SimpleNamespace
from urllib.error import URLError

from hn_search.archive_export import write_exports
from hn_search.research.render import walk_comments


NOW = 1_803_000_000


def node(item_id, *, text="Buying and renting depend on rates.", parent=1, replies=(), **fields):
    item = {"id": item_id, "type": "comment", "by": f"user{item_id}", "time": NOW,
            "parent": parent, "text": text, "kids": [reply["id"] for reply in replies], **fields}
    return {"id": item_id, "hn_url": f"https://news.ycombinator.com/item?id={item_id}",
            "retrieved_at": NOW, "item": item, "replies": list(replies)}


def snapshot(story_id=1, *, replies=None, title="Buying versus renting", root_null=False):
    if replies is None:
        replies = [node(story_id * 1000 + 1, parent=story_id)]
    root = {"id": story_id, "type": "story", "by": "author", "time": NOW, "title": title,
            "url": "https://example.com/housing", "descendants": max(5, len(replies)),
            "kids": [reply["id"] for reply in replies]}
    return {"root_id": story_id, "status": "complete", "started_at": NOW, "finished_at": NOW + 1,
            "reported_descendants": max(5, len(replies)), "saved_items": len(replies) + 1,
            "comments": len(replies), "unavailable": int(root_null), "poll_options": [],
            "root": {"id": story_id, "hn_url": f"https://news.ycombinator.com/item?id={story_id}",
                     "retrieved_at": NOW, "item": None if root_null else root,
                     "replies": [] if root_null else list(replies)}}


def persist_snapshot(conn, value):
    story_id = value["root_id"]
    with conn:
        conn.execute("INSERT OR IGNORE INTO archives (root_id, started_at, finished_at) VALUES (?, ?, ?)",
                     (story_id, value["started_at"], value["finished_at"]))
        for item in [value["root"], *(node for node, _, _ in walk_comments(value)), *value["poll_options"]]:
            conn.execute("INSERT OR IGNORE INTO archive_items VALUES (?, ?, ?, ?)",
                         (story_id, item["id"], json.dumps(item["item"]), item["retrieved_at"]))


class ArchiveFixture:
    def __init__(self, *, failures=True, large=False):
        self.calls = []
        self.failures = failures
        self.large = large

    def __call__(self, conn, story_id, directory):
        self.calls.append(story_id)
        if self.failures and story_id == 7:
            raise URLError("test network down")
        replies = None
        if self.large and story_id == 4:
            replies = [node(4001 + index, text=("Costs and local housing conditions differ. " * 18),
                            parent=4) for index in range(24)]
        value = snapshot(story_id, replies=replies, root_null=self.failures and story_id == 8)
        persist_snapshot(conn, value)
        write_exports(conn, story_id, directory)
        print(f"archive root={story_id} status=complete")


class FakeClient:
    def __init__(self):
        self.calls = []
        self.settings_replies = []
        self.keyword_replies = []
        self.fail = None
        self.before_call = None
        self.transform = None

    def run_structured(self, prompt, *, schema, options, capture_usage):
        from hn_search.research.ai import DEFAULT_SETTINGS, ANALYSIS_FIELDS

        properties = schema.schema["properties"]
        if "classification" in properties:
            name = "settings"
        elif "keywords" in properties:
            name = "keywords"
        elif "stories" in properties:
            item = properties["stories"]["items"]
            fields = item.get("anyOf", [item])[0]["properties"]
            name = "description" if "description" in fields else "verdict"
        elif prompt.startswith("Analyze"):
            name = "analysis"
        else:
            name = "folder_synthesis" if prompt.startswith("Synthesize the approved question") else "synthesis"
        call = SimpleNamespace(name=name, prompt=prompt, options=options, schema=schema)
        self.calls.append(call)
        if self.before_call:
            self.before_call(call)
        if self.fail and self.fail(call):
            raise RuntimeError("test client failure")
        if name == "settings":
            values = json.loads(prompt.split("\n\nInput:\n", 1)[1])
            output = self.settings_replies.pop(0) if self.settings_replies else {
                "approved": True, **copy.deepcopy(values.get("table", DEFAULT_SETTINGS)), "note": ""}
        elif name == "keywords":
            values = json.loads(prompt.split("\n\nInput:\n", 1)[1])
            output = self.keyword_replies.pop(0) if self.keyword_replies else {
                "approved": bool(values["keywords"]), "question": values["question"],
                "keywords": values["keywords"] or ["renting"], "note": ""}
        elif name in ("description", "verdict"):
            units = [dict(re.findall(r'(\w+)="([^"]*)"', match))
                     for match in re.findall(r"<hn_story ([^>]+)>", prompt)]
            output = {"stories": []}
            for unit in units:
                story_id, part = int(unit["id"]), int(unit["part"])
                item = {"story_id": story_id, "part": part}
                if name == "description":
                    item.update(description=f"Description of {story_id} part {part}", tags=["housing"])
                else:
                    verdict = "uncertain" if story_id == 2 else "irrelevant" if story_id in (3, 5) else "relevant"
                    ids = [story_id * 1000 + 1]
                    if "anyOf" in properties["stories"]["items"]:
                        variant = next(variant for variant in properties["stories"]["items"]["anyOf"]
                                       if variant["properties"]["story_id"]["enum"] == [story_id]
                                       and variant["properties"]["part"]["enum"] == [part])
                        ids = variant["properties"]["comment_ids"]["items"].get("enum", [])[:1]
                    item.update(verdict=verdict, reasons=f"Reason for {story_id} part {part}",
                                comment_ids=[] if verdict == "irrelevant" else ids)
                output["stories"].append(item)
        else:
            comment = re.search(r'<comment id="(\d+)"', prompt)
            citation = int(comment.group(1)) if comment else 1001
            part = re.search(r'<hn_story [^>]*part="(\d+)"', prompt)
            text = f"Part {part.group(1) if part else 'report'} evidence [c{citation}]"
            output = {field: [text] for field in ANALYSIS_FIELDS}
        if self.transform:
            output = self.transform(name, output)
        return SimpleNamespace(structured_output=output, payload=SimpleNamespace(
            usage={"input_tokens": 100, "output_tokens": 20}))
