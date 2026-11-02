# Hugging Face HN mirror

This note evaluates [`open-index/hacker-news`](https://huggingface.co/datasets/open-index/hacker-news) as a replacement for the source `collect` uses. Observations are from **2026-11-02**.

**Verdict: not adopted.** Keep `collect` on `hackernews_history` at `play.clickhouse.com`, read with `FINAL`. Before 2026-08-22, our filter selects 656,509 posts. The HF copy keeps only 579,661 of them; the other 76,848 (11.7%) fall out because their comment counts there are near zero.

## What it is

- Every HN item type as Zstandard Parquet: 239 monthly files under `data/YYYY/YYYY-MM.parquet` (11.6 GiB, 87% comments), 5-minute files under `today/`, and per-file stats in `stats.csv`. License: ODC-BY.
- The columns follow the HN item fields, plus a `words` column. `type` is an integer: 1 story, 2 comment, 3 poll, 4 pollopt, 5 job.
- The dataset card says that history and the nightly month refetch come from ClickHouse's [sql.clickhouse.com](https://sql.clickhouse.com) playground. The 5-minute files come from the HN Firebase API. That playground's `hackernews.hackernews` table has the same `words` column, and every monthly count checked below matches it exactly. So the dataset is a Parquet copy of that table.

## Findings

**Stopped updating.** The card promises an update every 5 minutes. The last commit was 2026-08-23. The newest monthly file (August 2026, committed 2026-08-22) ends at ID 49,395,220. On 2026-11-02, `hackernews_history` reached ID 50,335,410, and its newest item was 10 seconds old.

**Frozen comment counts.** `hackernews.hackernews` is a `SharedMergeTree` with one row per ID. Two periods are affected: November 2022 to December 2023, and December 2025 onward. In those periods, each row keeps the counts from shortly after posting, often 0 comments and 1 point, and never changes. `hackernews_history` instead versions each item by `update_time`, and `FINAL` returns the latest version.

Posts passing our filter (top-level story, poll, or job; not deleted; `descendants >= 5`), by creation month:

| Month | `hackernews_history FINAL` | HF file | `hackernews.hackernews` |
|---|---:|---:|---:|
| 2023-06 | 4,546 | 570 | 570 |
| 2024-01 | 4,752 | 4,751 | 4,751 |
| 2025-07 | 3,416 | 3,469 | 3,469 |
| 2026-01 | 3,870 | 446 | 446 |
| 2026-07 | 4,062 | 412 | 412 |

Outside the two periods, all 212 months since February 2007 differ by at most 2.5%. Inside them, full months keep 10–13% of qualifying posts. The partial edge months keep 84% (2022-11), 39% (2023-12), and 74% (2025-12).

For example, story [48920181](https://news.ycombinator.com/item?id=48920181) has 593 comments and 562 points in `hackernews_history`. In both the HF July file and `hackernews.hackernews`, it has 0 comments and 1 point.

**No coverage gain.** Both sources come from ClickHouse, so the copy can't add posts that our source lacks.

## When to reconsider

- **`play.clickhouse.com` disappears or tightens its limits.** The HF files still have correct counts before November 2022 and from 2024 through November 2025. The other periods would need another source.
- **We want comments in bulk**, for example to search comment text. One Parquet download replaces per-item HN API requests. However, the copy ends in August 2026, and `hackernews_history` serves the same comments with current versions.

## Reproduce

Run this monthly count at `https://play.clickhouse.com/?user=play`. At `https://sql-clickhouse.clickhouse.com/?user=demo`, replace `hackernews_history FINAL` with `hackernews.hackernews`.

```sql
SELECT toStartOfMonth(time) AS month, count() AS eligible
FROM hackernews_history FINAL
WHERE type IN ('story', 'poll', 'job') AND parent = 0 AND deleted = 0
    AND descendants >= 5 AND time >= '2022-01-01'
GROUP BY month
ORDER BY month
```

To count one HF file, run this in DuckDB 2.0.0. The `httpfs` extension reads only the needed columns over HTTPS.

```sql
INSTALL httpfs;
LOAD httpfs;
SELECT count(*)
FROM read_parquet('https://huggingface.co/datasets/open-index/hacker-news/resolve/main/data/2026/2026-07.parquet')
WHERE type IN (1, 3, 5) AND parent = 0 AND deleted = 0 AND descendants >= 5;
```
