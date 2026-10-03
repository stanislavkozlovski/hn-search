# HN metadata sizing

Research evidence for [HN topic research](../one-pagers/hn-topic-research.md), observed on **2026-10-01**. This note records measurements and estimates; it does not approve daily refresh semantics or define a database schema.

## Source

The public [ClickHouse playground](https://play.clickhouse.com/) exposes `hackernews_history`. `SHOW CREATE TABLE hackernews_history` returned a `ReplicatedReplacingMergeTree` keyed by `id`, with `update_time` as its version column. The [provider's description](https://presentations.clickhouse.com/2026-embeddings/) documents the self-updating mirror.

The table has the required `id`, `title`, `url`, `text`, `time`, and `descendants` fields, plus type, parent, and deletion fields. The HN link is derived from the ID. Selecting post metadata does not require reading comment bodies or following `kids`. HN defines `descendants` as total comments for stories and polls. [Official HN item contract](https://github.com/HackerNews/API/blob/8a0528f538bca407c2ceeeefc9bee48bdb99c1c8/README.md#items).

## Reproducible measurement

Run the following read-only query at the playground, or send it as the `query` parameter to `https://play.clickhouse.com/?user=play`. The source is live, so a rerun can return different totals.

```sql
SELECT
    now('UTC') AS observed_at_utc,
    count() AS eligible_posts,
    min(time) AS oldest_post,
    max(time) AS newest_post,
    max(update_time) AS newest_update,
    sum(
        length(title) + length(url) + length(text)
        + length(concat(
            'https://news.ycombinator.com/item?id=', toString(id)
        ))
    ) AS text_bytes,
    avg(
        length(title) + length(url) + length(text)
        + length(concat(
            'https://news.ycombinator.com/item?id=', toString(id)
        ))
    ) AS mean_text_bytes,
    countIf(
        time >= '2025-01-01' AND time < '2026-01-01'
    ) AS eligible_2025
FROM hackernews_history FINAL
WHERE type IN ('story', 'poll', 'job')
    AND parent = 0
    AND deleted = 0
    AND descendants >= 5
FORMAT JSONEachRow
```

Observed output:

```json
{"observed_at_utc":"2026-10-01 09:42:28","eligible_posts":661233,"oldest_post":"2007-02-19 22:05:40","newest_post":"2026-10-01 05:48:56","newest_update":"2026-10-01 09:42:08","text_bytes":174108121,"mean_text_bytes":263.30827560028007,"eligible_2025":41281}
```

`FINAL` selects the mirror's latest available version per ID. The filter excludes comments, poll options, deleted items, and reported counts below five. It does not impose an additional `dead = 0` rule: 2,690 counted posts carried that flag. The estimate therefore does not silently add a new eligibility exclusion. No job rows qualified in the grouped probe.

The text total is **174,108,121 bytes = 166.04 MiB**, averaging **263 bytes per post**. It excludes fixed-width metadata, database pages, indexes, and progress records. It measures this mirror's current records, without verifying omissions or stale fields against official HN data.

## Storage estimate

Choose SQLite for the current local, single-writer catalog. Its transactions suit committing metadata and resume progress together; PostgreSQL's separate service is unnecessary for this workload. [SQLite's database-selection guidance](https://www.sqlite.org/whentouse.html).

Assume an average **512–1,024 bytes per stored post**, allowing for the observed text payload plus numeric fields, row/page overhead, and basic indexes. This is an engineering allowance, not a measurement of an implemented schema.

| Example | Calculation | Estimated main database size |
|---|---|---|
| 100,000 posts | 100,000 × 512–1,024 bytes | 49–98 MiB |
| Observed catalog | 661,233 × 512–1,024 bytes | 323–646 MiB |
| 1,000,000 posts | 1,000,000 × 512–1,024 bytes | 488–977 MiB |
| Observed 2025 cohort | 41,281 × 512–1,024 bytes | 20–40 MiB |

The 2025 cohort illustrates one year's stored metadata, not a forecast. Estimates exclude journals, backups, temporary import space, comment archives, full-text indexes, embeddings, and reports. They set neither a per-post text limit nor a hard disk cap.
