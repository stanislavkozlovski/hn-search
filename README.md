# hn-search

Collect a local SQLite catalog of Hacker News post metadata from ClickHouse's
[`hackernews_history` mirror](https://play.clickhouse.com/). This implements the
[metadata collection design](https://github.com/stanislavkozlovski/hn-search/pull/1).
Comments, article bodies, search, and AI reports are deferred.

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
SQLite file and journal out of Git. Future schema changes need their own
migration design.

Run the offline suite:

```bash
python3 -m unittest discover -s tests
```
