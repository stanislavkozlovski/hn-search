# hn-search

- **Old posts:** `collect` saves metadata for nondeleted top-level HN posts with at least five reported comments from ClickHouse into SQLite, resuming interrupted imports.
- **New posts:** Each run then rescans posts created in the preceding five days, adds newly eligible posts, and refreshes eligible saved metadata. Posts that stop qualifying keep their last eligible snapshot; there is no catch-up outside that window.
- **Discussions:** `archive` downloads catalog stories and their comments into SQLite with reusable JSON and Markdown exports.
- **Use:** Build a local catalog and save discussions now; topic searches and AI reports with linked arguments come later, as described in the [one-pager](docs/one-pagers/hn-topic-research.md).

## Usage and collection details

Collect a local SQLite catalog of Hacker News post metadata from ClickHouse's
[`hackernews_history` mirror](https://play.clickhouse.com/). This implements the
[metadata collection design](https://github.com/stanislavkozlovski/hn-search/pull/1).
Use `archive` below to save comments. Article bodies, search, and AI reports are deferred.

Use Python 3.12+ with SQLite 3.31+ from the repository root. No dependencies or
package installation are needed:

```bash
python3 -m hn_search --db hn.sqlite3 collect
```

The first run retains the inclusive historical range `1..max(id)` in the mirror.
It saves public top-level stories, polls, and jobs with at least five reported
total comments (`descendants`, rather than the number of direct children). Each
page selects the latest available version before applying eligibility and saves
up to 10,000 posts and its historical cursor in one transaction. Later runs keep
that original bound and resume from the last committed cursor.

Once history completes, the same command scans posts created in the preceding
five days, freezing one UTC window `[now - 432000, now)` for that invocation.
Every run that reaches this step starts a fresh window from ID 1, even after
failure or downtime. Eligible saved metadata is refreshed in place, including
lower comment counts that still qualify. Omitted, deleted, below-five, and older
posts retain their last eligible snapshot. A post first qualifying outside the
window can remain absent; eight days offline leaves the older three-day gap.

After each page commits, a flushed progress line shows the source, selected
range or window (UTC epoch seconds), next cursor, completion, and catalog-wide
saved-post count. Completed history prints its saved line on every run without
fetching history again:

```text
historical source=play.clickhouse.com/hackernews_history range=1..50235582 next_id=271044 complete=false saved_posts=10000
```

Completion describes processing the selected mirror range, accepting mirror
omissions, delayed updates, and changes behind the historical cursor.

After any failure, rerun `collect` with the same `--db`. Errors propagate as
tracebacks (exit 1); invalid command usage exits 2. A failed or interrupted page
leaves its posts and cursor uncommitted, while earlier pages remain saved. Daily
pages already committed also remain saved; the next daily scan uses a fresh
window. There are no automatic retries or fallback providers.

Run the command once a day and serialize invocations. No scheduler is installed;
overlapping writers can fail with `database is locked` after SQLite's default
five-second timeout. Stopping the collector leaves the database in place.

The schema stores one snapshot per HN ID: title, external URL, original post
text, creation timestamp, and reported total comment count. `hn_url` is generated
from the ID on read. Source strings, including HTML, Unicode, and empty URL or
text, are preserved. Collection progress holds one historical row; it is not a
run log. Expect roughly 0.5–1 KiB per post (about 323–646 MiB for 661,233 posts),
plus journals and temporary space; these are estimates, not limits. Keep the
SQLite file and journal out of Git.

Install the feed dependency before running the complete offline suite:

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests
```

## Comment archives

Download discussions for stories already present in the metadata catalog:

```bash
python3 -m hn_search archive 4517440 126809
python3 -m hn_search --db hn.sqlite3 archive --export-dir exports 4517440
```

`archive` defaults to `hn.sqlite3` and `exports/`, relative to the current working
directory. `collect` and `feed` still require an explicit top-level `--db`.
Repeated IDs are ignored. Every requested ID must exist in `posts`; missing IDs
are all reported before any archive migration or HTTP request.

The downloader saves the official HN API's root and observed reply tree, including
poll choices and their vote counts. Original JSON fields, HTML, reply relationships,
and UTC retrieval times remain in SQLite. Deleted, flagged, and unavailable items
stay visible; their obtainable children are followed. A mismatch with HN's reported
comment count does not prevent completion. This is an observation interval, not
an atomic historical snapshot: replies added behind a saved parent are not fetched.

Up to eight stories download concurrently, with one item request per story and
one SQLite writer. Each response commits before that story's next request.
There is a 30-second blocking-operation HTTP timeout, with no automatic retries
or fixed pacing. On a request failure, dispatch stops, successful requests already
running are saved, and independently completed stories still receive exports.
Unadmitted stories remain untouched. Rerun the same command after a failure or
interruption to fetch only missing items.

Only complete stories get `<id>.json` and `<id>.md`. JSON contains the unchanged
API value under each node's `item`, ordered `replies`, HN links, retrieval times,
poll options, observation timestamps, and counts. `comments` counts non-null reply
items including deleted/flagged placeholders, excluding the root and poll options;
`unavailable` counts null responses and `saved_items` includes them. The Markdown
opens with the saved root and metadata, then nests comments with HN links and
Obsidian `^c<ID>` anchors. Source HTML stays unchanged in SQLite and JSON while
Markdown renders paragraphs, emphasis, code, links, and entities.

```text
archive root=4517440 status=complete comments=5 unavailable=0 reported_descendants=5 json=exports/4517440.json markdown=exports/4517440.md
archive root=4517440 status=incomplete comments=3 pending=1
```

Each file is replaced through its own temporary file and rename. Success is printed
only after both writes. If an export fails, the archive stays complete; rerunning
rebuilds both files with zero HN requests and prints `reused=true`. Every completed
archive is reused forever, including recent stories; there is no refresh command.
Request/export failures exit 1; malformed arguments exit 2.

The first valid archive request atomically adds `archives` and `archive_items` and
raises schema v1 to v2 without changing posts or collection progress. Higher
versions are preserved. Rolling code back leaves these tables intact and unused
by the old collector. Serialize `archive`, `collect`, and other commands sharing
the catalog; overlapping writers can fail with SQLite locking errors.

Library callers use `hn_search.archive.archive(conn, roots, export_dir)` for a
batch or `archive_story(conn, root, export_dir)` for one story. Both require explicit
paths and a catalog connection owned by the calling thread. Failures propagate
after running responses drain; callers choose their own continuation policy.
Downloads require only the Python standard library.

## Telegram feed

The independent hourly feed searches Algolia for stories created in the last
ten hours with at least five points, including stories with no comments. It
keeps every story and score observation in a separate SQLite database and
classifies only titles and article URLs against your lenses. Never use the
research catalog's path for `feed`: it refuses that database without changing it.

Install `stan-ai-client==0.1.19` with Python 3.12+ (prefer a virtual environment)
and put a logged-in `codex` on `PATH`. Save lenses in `lenses.toml`:

```toml
[classifier] # optional defaults
model = "gpt-6-luna"
effort = "high"

[[lens]]
name = "ai-agents"
bot_token_env = "HN_FEED_AI_AGENTS_BOT_TOKEN"
chat_id = 123456789

[lens.categories]
agents = "AI agents, agent frameworks, and tool use"
evals = "Benchmarks and evaluations of language models"
```

Create each bot with BotFather and send it `/start` from the target chat. Set
each `bot_token_env` variable in the environment from a private file outside
Git; tokens are never stored in SQLite or printed in feed errors. Then run:

```bash
python3 -m pip install -r requirements.txt
python3 -m hn_search --db feed.sqlite3 feed --config lenses.toml
```

Each lens needs a distinct lowercase name, nonempty categories with lowercase
IDs and descriptions, an integer chat ID, and a token environment variable.
Unknown configuration keys are errors. Change the optional classifier model
and effort to switch Codex models. `collect` still requires no installed package.

One call classifies up to 20 stories across lenses using ephemeral Codex
sessions with commands, web search, images, MCP apps, plugins, and other tools
disabled. It never fetches articles or HN comments. Decisions, including
nonmatches, stay cached until a title, URL, or lens's categories change;
points, model, effort, and prompt changes reuse them. A new or renamed lens
only judges newly discovered stories. Keep the same lens name to retain its
history; removing it stops its calls and sends.

Matching stories arrive grouped by bot and chat with titles, categories,
article/HN links, and points. Later runs edit only the points, for example
`6 points` becomes `<s>6 points</s> 19 points` in Telegram HTML. Earlier
observations appear on a delayed first send, too. Each message reserves room
for at most ten shown values per story. Points stop updating when the story
leaves the search window. Two matching lenses in one chat can repeat a story.

Each run attempts a pending send once while its story is still in the current
search. A lost send response can cause a duplicate next hour. A failed
classifier batch stops further classification but still permits pending sends
and edits. Config, source, SQLite, classifier, and send failures exit 1;
edit failures alone are logged and exit 0. Usage errors exit 2. There are no
in-run retries, catch-up beyond ten hours, or saved-story search/resend commands.
Stories, observations, decisions, and message records are never pruned.

The offline suite uses scripted HTTP and a fake Codex executable. An opt-in
live probe checks Luna's structured reply, disabled features, and absence of
command, file, MCP, and web events, without contacting Telegram:

```bash
HN_FEED_LIVE_CODEX=1 python3 -m unittest tests.test_feed_live
```

On uzealot, use the companion `hn-feed.service` and hourly timer, which push
Kuma only after a successful run. Start manual runs with
`systemctl --user start hn-feed.service` to serialize them. Deployment,
credentials, rollback, and the three-hour heartbeat monitor are documented
in the uzealot repository's `docs/hn-feed.md`. Consistent SQLite backups are
deferred; copying a live database alone does not guarantee a consistent backup.
