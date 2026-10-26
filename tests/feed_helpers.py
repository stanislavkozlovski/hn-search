"""Offline HTTP and executable fixtures for the independent feed."""

from contextlib import redirect_stdout
from io import BytesIO, StringIO
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import urlsplit

from hn_search.__main__ import main
from hn_search.feed.lenses import load_settings

NOW = 1793008800
TOKEN = "123456:test-secret-token"
CONFIG = '''[[lens]]
name = "ai-agents"
bot_token_env = "HN_FEED_TEST_TOKEN"
chat_id = 123456789
[lens.categories]
agents = "AI agents, agent frameworks, and tool use"
'''


def hit(story_id=50234108, *, points=6, title="Agent frameworks", url="https://example.com/agents", created_at=None):
    return {"objectID": str(story_id), "title": title, "url": url, "points": points,
            "created_at_i": NOW - 7200 if created_at is None else created_at}


def window(*hits):
    return {"hits": list(hits), "nbHits": len(hits)}


def sent(message_id=812):
    return {"ok": True, "result": {"message_id": message_id}}


class RecordingOpener:
    def __init__(self, *responses):
        self.responses = list(responses)
        self.requests = []

    def __call__(self, request, *, timeout):
        url = request if isinstance(request, str) else request.full_url
        if urlsplit(url).hostname not in {"hn.algolia.com", "api.telegram.org"}:
            raise AssertionError("Unexpected request host")
        record = {"url": url, "timeout": timeout,
                  "payload": None if isinstance(request, str) else json.loads(request.data)}
        self.requests.append(record)
        if not self.responses:
            raise AssertionError("Unexpected request")
        response = self.responses.pop(0)
        if callable(response):
            response = response(record)
        if isinstance(response, Exception):
            raise response
        return BytesIO(json.dumps(response).encode())


def write_fake_codex(directory):
    path = Path(directory) / "codex"
    path.write_text(f"#!{sys.executable}\n" + r'''
import json
import os
from pathlib import Path
import re
import sys

argv = sys.argv[1:]
prompt = sys.stdin.read()
directory = Path(argv[argv.index('--cd') + 1])
schema = json.loads(Path(argv[argv.index('--output-schema') + 1]).read_text())
with open(os.environ['FAKE_CODEX_LOG'], 'a') as log:
    log.write(json.dumps({'argv': argv, 'prompt': prompt, 'cwd': str(directory),
                         'files': list(directory.iterdir()), 'schema': schema}, default=str) + '\n')
mode = os.environ.get('FAKE_CODEX_MODE', '')
if mode == 'fail':
    print('usage limit reached', file=sys.stderr)
    sys.exit(1)
stories = json.loads(prompt.split('Stories:\n', 1)[1])
categories = re.findall(r'^- ([a-z0-9/-]+):', prompt, re.MULTILINE)
reply = {str(story['id']): [category for category in categories if category.endswith('/agents')]
         if 'agent' in story['title'].lower() else [] for story in stories}
if mode == 'unknown-story':
    reply['999'] = []
elif mode == 'missing-story':
    reply.pop(next(iter(reply)))
elif mode == 'unknown-category':
    reply[next(iter(reply))] = ['ai-agents/unknown']
elif mode == 'invalid-json':
    print('{')
    sys.exit(0)
print(json.dumps(reply))
''')
    path.chmod(0o700)
    return path


class FeedCase(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.directory = Path(directory.name)
        self.path = self.directory / "feed.sqlite3"
        self.config = self.directory / "lenses.toml"
        self.config.write_text(CONFIG)
        self.log_path = self.directory / "codex.jsonl"
        write_fake_codex(self.directory)
        environment = patch.dict(os.environ, {
            "PATH": f"{self.directory}:{os.environ['PATH']}", "HN_FEED_TEST_TOKEN": TOKEN,
            "FAKE_CODEX_LOG": str(self.log_path), "FAKE_CODEX_MODE": "",
        })
        environment.start()
        self.addCleanup(environment.stop)

    def settings(self):
        return load_settings(self.config, os.environ)

    def calls(self):
        if not self.log_path.exists():
            return []
        return [json.loads(line) for line in self.log_path.read_text().splitlines()]

    def run_feed(self, *responses, now=NOW):
        opener = RecordingOpener(*responses)
        self.output = StringIO()
        with redirect_stdout(self.output):
            main(["--db", str(self.path), "feed", "--config", str(self.config)], opener=opener, clock=lambda: now)
        self.assertEqual(opener.responses, [])
        return opener
