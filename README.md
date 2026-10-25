# hn-search

- **Old posts (planned):** `backfill` will import metadata for nondeleted top-level HN posts with at least five reported comments from ClickHouse's `hackernews_history` into SQLite, saving progress so interrupted imports can resume.
- **New posts (planned):** Each `daily` run will rescan posts created in the preceding five days, add newly eligible posts, and refresh eligible saved metadata while retaining the last eligible snapshot of posts that stop qualifying, with no catch-up outside that window.
- **Use:** The planned catalog will let you inspect collection progress and support later topic searches, on-demand comment downloads, and AI reports with linked arguments and counterarguments, as described in the [one-pager](https://github.com/stanislavkozlovski/hn-search/blob/615fed79d06fc1740a6a4f38388da885da82ca7a/docs/one-pagers/hn-topic-research.md).
