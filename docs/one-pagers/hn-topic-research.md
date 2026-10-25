# HN topic research

## Pass 0: Problem or opportunity framing

### Who is the user, what do we know about their behavior, and how correct does the result need to be?

- **User:** Stan.
- **Their behavior:** Stan asks “What does HN think about X?”, searches a local HN archive, and reads a report linked to the discussions.
- **Edge-case tolerance:** Missing relevant eligible posts present in the chosen historical mirror is the main failure; finding them matters more than excluding every irrelevant candidate.

### What is the prevailing user problem or opportunity?

- **Problem or opportunity:** Stan cannot quickly find and synthesize HN discussions across its history, so he misses useful arguments about topics he cares about.

### What is the proposed solution, and why is it right for the user?

- **Solution:** First deliver a resumable metadata catalog from a trusted historical mirror, admitting public top-level HN posts when they have at least five reported total comments and storing HN ID, title, external URL, HN link, original post text when present, creation date, and reported total comment count.
- **Why it fits the user:** One local thread catalog lets Stan start future topic searches without repeating the full HN discovery pass.

Metadata ingestion includes no comment parser or AI integration.

### How would you describe the end-to-end user experience?

- **End-to-end user experience:** Stan starts catalog collection, sees progress through the selected historical range in the chosen mirror, and resumes an interrupted sweep without losing already archived posts.

### What existing data, behavior, or integrations must keep working?

- **Legacy data:** None known; `hn-search` is a new repo with no existing archive.
- **Legacy behavior:** None known.
- **Existing integrations:** None for metadata ingestion; `stan_ai_client` belongs to the deferred reporting stage.
- **Compatibility tolerance:** No old schema needs support, but later runs must retain already archived threads and comments.

### Agent edge-case scan

| Edge case | What happens if ignored | What handling it adds | User decision |
|---|---|---|---|
| When an HN story links to an external article but has no original post text, the catalog stores the article URL without its body. | The catalog retains the external URL but does not download or index the article body, so Stan cannot identify that post using terms found only in the article body. | The project downloads and indexes linked article content with its source URL. | IGNORE |
| When the source reports a deleted story that the catalog has not archived, the collector skips it without preserving a deletion record. | Stan sees fewer usable threads than the crawler checked and cannot tell which items were deleted. | The project records deleted item IDs and reports the gap in archive coverage. | IGNORE |
| When the source reports fewer than five total comments on a public top-level HN post absent from the catalog, the collector skips that post. | The catalog admits low-comment posts and uses disk space outside the intended scope. | The collector checks the source's reported total comment count before admitting a post, excludes new records below five, and fetches no comment bodies to determine eligibility. | HANDLE |
| When a historical sweep stops before finishing the selected range in the chosen mirror, the local catalog contains only part of that range's eligible posts. | Stan sees a partial catalog without knowing that eligible posts in the selected mirror range remain unprocessed. | The project durably records progress, retains previously archived posts, resumes unfinished ranges, and shows coverage as incomplete until it has processed the selected historical range in that mirror. | HANDLE |
| When a mirror omits an eligible public HN post, the catalog cannot discover that post through the mirror. | Stan receives a fully processed mirror catalog that can still omit eligible HN discussions. | The project enumerates the official HN item range to establish coverage independently of the mirror. | IGNORE |

HN exposes the reported total as `descendants`; `kids` lists direct children, so its length is not the total comment count. [HN API item fields](https://github.com/HackerNews/API/blob/8a0528f538bca407c2ceeeefc9bee48bdb99c1c8/README.md#items).

For example, a public top-level post with `descendants: 5` and two `kids` qualifies; a previously unsaved post with `descendants: 4` gets no catalog record.

A failed or interrupted fetch does not establish that an item is deleted.

**Source coverage:** The MVP trusts historical mirrors such as Hugging Face or ClickHouse, accepting upstream omissions as [decided in review](https://github.com/stanislavkozlovski/hn-search/pull/1#discussion_r4153880716). For example, finishing the selected mirror range can still leave out an eligible HN post that the mirror omitted.

**Source selection:** Pass 1 uses ClickHouse's `hackernews_history` mirror at [play.clickhouse.com](https://play.clickhouse.com/); completion describes the selected mirror range, with no independent HN coverage check.

**Deferred — independent HN coverage:** Official HN item-range enumeration to detect mirror omissions is outside the MVP.

**Deferred — later stages:** Keyword/AI topic selection, on-demand comment archiving, and `stan_ai_client` reports each require a separate one-pager.

**Deferred — live parsing:** Stan [prefers future on-demand parsing](https://github.com/stanislavkozlovski/hn-search/pull/1#discussion_r4158832692); its behavior is reserved for the separate later-stage one-pager.

**Deferred — linked-report experience:** Stan asks “What does HN think about buying versus renting?”, the tool searches its thread catalog and downloads matching comment trees, then gives him a deep report of arguments, counterarguments, and representative linked comments.

**Deferred — later-stage edge cases:** The existing `IGNORE` decisions below apply to those later stages.

| Edge case | What happens if ignored | What handling it adds | User decision |
|---|---|---|---|
| When HN users discuss a topic under a story whose title, URL, and original post do not reveal it, the topic filter skips that story. | Stan's report omits the relevant discussion even though the thread exists in the local catalog. | The project searches comment text beyond the title and URL candidates before final topic selection. | IGNORE |
| When a saved HN thread gains comments after its first download, the local comment tree and report become stale. | Stan reads a report that omits newer arguments in that thread. | The project refreshes saved threads and updates affected analyses with a visible retrieval time. | IGNORE |

**Deferred — saved-comment refresh:** Future sweeps may revisit recent comment trees, potentially those younger than one year; comment refresh and automatic reanalysis remain outside metadata ingestion.

### Daily metadata collection

Stan chose a rolling [five-day window](https://github.com/stanislavkozlovski/hn-search/pull/1#discussion_r4159288445) based on post creation time and [the same window on every invocation](https://github.com/stanislavkozlovski/hn-search/pull/1#discussion_r4159298725), including restart after failure or downtime. Daily collection accepts gaps outside that window. Within it, daily runs refresh eligible saved metadata and [retain the last eligible snapshot](https://github.com/stanislavkozlovski/hn-search/pull/1#discussion_r4173257027) if a saved post later falls below five comments or becomes deleted; older saved metadata may stay stale.

| Edge case | What happens if ignored | What handling it adds | User decision |
|---|---|---|---|
| When the mirror raises a previously skipped post from zero comments to at least five within its first five days, the daily collector encounters newly eligible metadata. | A collector that only advances past new IDs misses the now-eligible post. | The daily collector scans the preceding five days by post creation time on every invocation and inserts qualifying HN IDs absent from the catalog. | HANDLE |
| When a post leaves the five-day creation-time window before daily collection saves it, the daily collector no longer revisits it. | Stan accepts missing posts after downtime and posts that first qualify or reach the mirror outside the window. | The daily collector backfills earlier creation times or catches up missed intervals from the last successful run. | IGNORE |
| When the mirror changes a saved post's metadata within its first five days and the post still qualifies, the daily collector encounters an updated eligible version. | Stan sees the earlier title, text, and reported count in the saved snapshot. | The daily collector replaces the saved metadata with the latest eligible mirror version within the five-day window. | HANDLE |
| When the mirror lowers a saved post's reported count below five, the qualifying query omits that post. | A collector that removes saved rows absent from its results discards an archived discussion. | The catalog keeps the post's last eligible snapshot unchanged. | HANDLE |
| When the mirror marks a saved post deleted, the qualifying query omits that post. | A collector that removes saved rows absent from its results discards an archived discussion. | The catalog keeps the post's last eligible snapshot without adding deletion records. | HANDLE |

## Pass 1: High-level design

**Review status:** The daily five-day window, restart gap acceptance, saved-metadata refresh, and last-eligible-snapshot retention are settled. Stan [approved proceeding to Pass 2](https://github.com/stanislavkozlovski/hn-search/pull/1#issuecomment-5969373305); the low-level design below remains under review.

## Proposal

### In-scope goals

- Import qualifying top-level metadata from the selected ClickHouse mirror into a local catalog.
- Resume unfinished historical ranges while retaining committed records.
- Discover newly eligible posts created within the preceding five days on every daily invocation, including restarts, without automatic catch-up beyond that window.
- Refresh eligible saved metadata within that same window and retain the last eligible snapshot if a post later falls below five comments or becomes deleted.
- Show the source, selected range, saved-post count, and whether collection finished.

### Out-of-scope non-goals

Daily refresh and automatic catch-up outside the five-day window are excluded. Comment downloads, live parsing, article bodies, keyword/AI topic selection, reports, and independent verification against HN remain deferred.

### Potential scope growth

| Risk | Growth mechanism — when it happens in practice | Explicit cap | Decision |
|---|---|---|---|
| Source adapters multiply. | Each extra mirror adds field mappings, coverage rules, and interruption behavior when the collector switches providers. | One adapter for ClickHouse `hackernews_history`; no automatic fallback or upstream reconciliation. | CONSTRAIN |
| Repeated imports multiply saved records. | Replaying metadata after interruptions or during daily refresh can add duplicate records or a new stored version for each run. | One saved snapshot per HN ID, with durable progress for the selected historical range; daily refresh replaces eligible metadata without accumulating version history. | CONSTRAIN |
| Missed daily runs accumulate backfill work. | Catching up from the last successful run adds more historical metadata to scan as failures or downtime accumulate. | Every daily invocation scans only the preceding five days by post creation time, including restarts; no widening or automatic catch-up. | CONSTRAIN |
| Stored content expands beyond metadata. | Following each post's comment tree or external link introduces more downloads and stored bodies. | Only the approved post metadata and collection progress; zero comment bodies, article bodies, or AI outputs. | EXCLUDE |

### Public behavior changes (before / after)

- **Before:** The [repository at this design head](https://github.com/stanislavkozlovski/hn-search/tree/8f6c803ccb5ca0571e50f46c446120b48c74614e) contains only this proposal; Stan has no collection command or archive.
- **After:** Stan starts a historical collection, sees its selected mirror range and saved-post count, and reruns it after interruption to finish the remaining range. Each daily invocation scans only posts created in the preceding five days, inserts newly eligible IDs, and refreshes eligible saved metadata. A saved post that falls below five comments or becomes deleted keeps its last eligible snapshot; restarting after eight days offline uses the same five-day window and leaves the older gap. Exact command names belong to Pass 2.

### Historical source and collection

Use the public ClickHouse `hackernews_history` table. Its server-side selection can return only top-level post metadata meeting `descendants >= 5`. Its versioned rows require selecting the latest available version per HN ID before applying eligibility; the sizing probe used `FINAL`. The provider documents the [self-updating mirror](https://presentations.clickhouse.com/2026-embeddings/), and the [research note](../research/hn-metadata-sizing.md) records the checked schema and live query.

Choose the historical ID range at the start and retain that bound when resuming. Read it in bounded portions, persist qualifying records and progress together, and keep completed portions across failures. For example, if fetching the next portion fails, previously committed posts remain readable and the range stays incomplete; restarting resumes unfinished work without duplicate catalog records.

A previously unsaved post with four reported comments gets no record; five qualifies. Store HN ID, title, external URL, HN link, original post text when present, creation date, and reported total comment count. Read no comment bodies to count them and follow no external article links. Initial metadata reflects when each portion was read; finishing the range does not establish exhaustive upstream coverage.

### Database and expected size

Choose **SQLite** for the metadata catalog and collection progress. Stan's local collector can commit both together without operating a database server, and the measured data fits comfortably in a local file. The workload assumes one local writer; SQLite permits one writer at a time, which is sufficient for this scope. [SQLite guidance](https://www.sqlite.org/whentouse.html).

On **2026-10-01**, the mirror query found **661,233** nondeleted top-level posts with at least five reported comments. Their titles, URLs, HN links, and original text totaled **166 MiB**, excluding numeric fields and database overhead. These are mirror observations, not a count of every qualifying HN post. [Query, filters, and results](../research/hn-metadata-sizing.md).

For planning, assume **0.5–1 KiB per stored post** including row and basic-index overhead:

| Example | Estimated main database size |
|---|---|
| 100,000 qualifying posts | 49–98 MiB |
| The observed 661,233 posts | 323–646 MiB |
| 1,000,000 qualifying posts | 488–977 MiB |

These are estimates, not measured SQLite file sizes or hard limits; journals, backups, temporary space, and future search indexes are additional. Retaining previously eligible posts after their counts fall below five or they become deleted means the catalog can contain more posts than a later query's currently eligible set.

### Daily metadata collection: Rolling five-day window

Every daily invocation scans the preceding five days by post creation time (`time`) in ClickHouse `hackernews_history`, including restart after failure or downtime. The window is relative to that invocation, never widened or anchored to the last successful run; daily collection performs no automatic catch-up.

For example, a post skipped at zero comments on Tuesday is inserted on Wednesday if the mirror then reports at least five and the post remains within the five-day window. Apply the historical query's latest-version and eligibility rules: insert absent HN IDs and replace saved metadata for still-eligible posts within the window.

If a saved two-day-old post moves from five comments to nine, refresh its metadata; if it later drops below five or becomes deleted, keep its last eligible snapshot unchanged. Daily results never remove or clear saved rows whose IDs they omit. The catalog keeps one snapshot per HN ID and does not create deletion records or metadata version history.

After eight days offline, restart scans only posts created in the preceding five days and leaves the older gap. The catalog accepts posts missed after they leave the window, including posts that first qualify or reach the mirror later. This daily limit does not change the historical sweep's guarantee to resume its retained ID range until it finishes.

Saved metadata outside the five-day window stays unchanged, accepting Stan's assumption that older posts receive few new comments. Daily scheduling still inherits mirror delay and cannot promise real-time HN freshness. Live parsing, comment-tree refresh, and report regeneration remain deferred.

## Rejected design alternatives

| Alternative | Why rejected |
|---|---|
| The collector enumerates the entire official HN item-ID range to verify mirror coverage. | The collector would add per-item requests across the shared post/comment ID space for the upstream guarantee Stan explicitly excluded. |
| The collector downloads the entire HN archive before filtering locally. | The collector would transfer comment-bearing data that server-side metadata selection can exclude. |
| The catalog runs PostgreSQL for this first delivery. | PostgreSQL would add a database service and its configuration before this local, single-writer catalog needs them. |

## Pass 2: Low-level design

## Low-level coding implementation

### Existing files likely to change

None. At [design head `615fed7`](https://github.com/stanislavkozlovski/hn-search/tree/615fed79d06fc1740a6a4f38388da885da82ca7a), `git ls-tree -r HEAD` and `cx overview .` list only this proposal and `docs/research/hn-metadata-sizing.md`. With no source, schema, fixture, test, entrypoint, or automation in the repository, every file, function, and command below is a **proposed addition**, not an existing interface.

### New files expected

Use Python 3.12+ and only its standard library, mainly `argparse`, `urllib.request`, `json`, `sqlite3`, and `unittest`.

| New file | Responsibility |
|---|---|
| `hn_search/__init__.py`, `hn_search/__main__.py` | Make `python3 -m hn_search` runnable; `main()` parses commands, dispatches them, and maps failures to exit codes. |
| `hn_search/clickhouse.py` | `max_id()` reads the historical bound; `fetch_page()` sends one parameterized query and returns a validated page. |
| `hn_search/catalog.py` | `open_catalog()` creates or reopens schema v1; `commit_page()` writes one page and its cursor in one transaction. |
| `hn_search/collect.py` | `collect_history()` resumes the retained ID range; `collect_daily()` freezes and scans one five-day window. |
| `tests/test_clickhouse.py`, `tests/test_catalog.py`, `tests/test_collect.py`, `tests/test_cli.py` | Cover response validation, persistence, collection semantics, and CLI behavior. |
| `README.md`, `.gitignore` | Document invocation and recovery; keep local SQLite files and Python caches out of Git. |

### Maintainability and refactor call

No preparatory refactor is needed because no code exists yet. Share one query builder and one page-commit path, but keep historical insert-only writes separate from daily upserts. Inject the clock and the HTTP opener (`urlopen`) for tests. Do not add an adapter registry, ORM, task queue, migration framework, or run-history table.

### Collection and commit flow

1. **Historical collection:** The first `backfill` fixes inclusive bounds and commits them before fetching a page. The default is `1..max(id)`, which was `1..50235582` on 2026-10-25; `max_id()` runs `SELECT max(id) FROM hackernews_history` without `FINAL`, because every version keeps its ID. Explicit bounds replace either default and must satisfy `1 <= from_id <= through_id <= max(id)`. Later runs reuse the saved bounds: repeated flags pass, different flags fail without touching progress, and a complete range prints its saved progress line and exits 0 without contacting ClickHouse.
2. **Daily collection:** `collect_daily()` reads `T = int(time.time())` once and keeps the window `[T - 432000, T)` and its page cursor, starting at `next_id = 1`, in memory. Every invocation, including after a failed or interrupted daily run, scans a fresh window from the start. Daily pages commit posts only, one page per transaction; historical progress is untouched.
3. **Selection:** `fetch_page()` sends the historical query below. Daily pages drop the `through_id` predicate and add `time >= toDateTime({window_start:UInt32}, 'UTC') AND time < toDateTime({window_end:UInt32}, 'UTC')`.

```sql
SELECT id, title, url, text, toUnixTimestamp(time) AS created_at, descendants
FROM hackernews_history FINAL
WHERE id >= {next_id:UInt32} AND id <= {through_id:UInt32}
  AND type IN ('story', 'poll', 'job')
  AND parent = 0 AND deleted = 0 AND descendants >= 5
ORDER BY id LIMIT 10000
SETTINGS result_overflow_mode = 'throw',
         timeout_overflow_mode = 'throw',
         read_overflow_mode = 'throw'
FORMAT JSON
```

**Read-only settings.** The `play` user has `readonly = 1`, so ClickHouse accepts a `SETTINGS` entry only when it matches the current value. On 2026-10-25, server `26.11.1.707` accepted the three `throw` entries but returned HTTP 500 for `optimize_move_to_prewhere_if_final = 0`, because 26.10 changed that default to `1`. [Live profile](https://play.clickhouse.com/?user=play&query=SELECT%20name%2C%20value%20FROM%20system.settings%20WHERE%20name%20IN%20%28%27readonly%27%2C%20%27optimize_move_to_prewhere_if_final%27%2C%20%27max_execution_time%27%2C%20%27max_result_rows%27%29). Send no other settings. If the provider switches an overflow mode to `break`, the pinned `throw` fails the request instead of returning truncated rows.

**Eligibility after version selection.** Write every eligibility filter in `WHERE`, never `PREWHERE`. Before 26.10, automatic `PREWHERE` was off by default for `FINAL`; since then it moves only conditions on the sorting key (`id`), so the type, parent, deletion, and count filters see each ID's latest version. [ClickHouse setting source](https://github.com/ClickHouse/ClickHouse/blob/a3c1418967fb78aced6e1bace70f0611ca15601b/src/Core/Settings.cpp#L1153-L1172). Keep the `type` filter: all 15,906 poll options in the mirror have `parent = 0`. Do not add `dead = 0`; the [sizing query](../research/hn-metadata-sizing.md#reproducible-measurement) counts those 2,690 posts.

**Transport and validation.** `fetch_page()` sends an HTTPS GET to `https://play.clickhouse.com/?user=play` with `wait_end_of_query=1` and typed `param_next_id`, `param_through_id`, `param_window_start`, or `param_window_end` values, and never interpolates values into SQL. It reads and validates the whole JSON object before any write. It rejects HTTP errors, truncated or malformed bodies (including an HTTP 200 body cut off by an `__exception__` block), and invalid required fields. HTTP 200 alone does not prove success. [HTTP response caveats](https://clickhouse.com/docs/interfaces/http#http_response_codes_caveats).

**Live check (2026-10-25).** The [table](https://play.clickhouse.com/?user=play&query=SHOW%20CREATE%20TABLE%20hackernews_history%20FORMAT%20JSON) still matches the [research note](../research/hn-metadata-sizing.md#source): `ReplicatedReplacingMergeTree` versioned by `update_time` and ordered by `id UInt32`. Its `title`, `url`, and `text` columns are non-nullable `String`, so absent values arrive as `""`. The first historical page returned 10,000 posts, IDs 121–271,043, in 0.54 s; the daily window returned 476 posts in 0.33 s. Each probe read at most 64M rows, far inside the `play` limits: per query, 60 s and 1,000,000 result rows; per client each hour, 3,000 queries, 600 s of execution, and 300 billion rows read. The 664,002 posts eligible that day fill about 67 pages. These checks verify query shape and headroom, not throughput.

**Writes.** `open_catalog()` connects with `sqlite3.connect(path, autocommit=False)`, new in Python 3.12, and `commit_page()` runs inside `with conn:`: it writes the page, updates the historical cursor only for historical pages, and commits once. Historical pages use `INSERT ... ON CONFLICT(id) DO NOTHING`, so replay never overwrites a saved snapshot. Daily pages use `ON CONFLICT(id) DO UPDATE SET` for `title`, `url`, `text`, `created_at`, and `descendants`. Neither path deletes rows, and both store source strings unchanged, including HTML, Unicode, and empty URL/text.

**Cursor.** A full page advances `next_id` to its last ID plus one. A short or empty page also sets `complete = 1`, and historical completion leaves `next_id = through_id + 1`. A crash before commit replays that page; a crash after commit resumes after it. For example, a timeout on page two leaves page one's 10,000 posts and `next_id = 271044` intact.

**Failures.** `fetch_page()` requests one page at a time with `urlopen(..., timeout=90)`, above the server's 60-second limit. A transport, HTTP, quota, decoding, validation, or SQLite failure stops the command with exit code 1, and Stan reruns it once the cause clears. There are no automatic retries or provider fallback.

## Validation matrix

`Yes` rows are implementation obligations; `No` rows record approved limitations; `Defer` rows add no implementation now.

| Validation | Disposition | Behavior or consequence | Reason |
|---|---|---|---|
| V1 — Command arguments and retained historical bounds | Yes | `backfill` rejects malformed, reversed, out-of-range, or conflicting bounds without touching saved work; reruns never widen the range as the mirror grows, and a complete range stays complete. | Preserve the selected historical sweep. |
| V2 — Catalog initialization and reopening | Yes | `open_catalog()` initializes an empty file as v1, reopens v1, and rejects unversioned populated files or other versions without modifying them. | No legacy schema exists; saved records must survive reruns. |
| V3 — Latest-version eligibility under the `play` profile | Yes | Four reported comments fail and five qualify regardless of `kids`; a newer deleted or below-five version hides older eligible ones; requests send only settings equal to the profile's values. | Enforce the admission rule; the read-only profile rejects changed settings. |
| V4 — Field mapping and content boundary | Yes | `commit_page()` keeps required values and empty strings, `hn_url` derives from `id`, and the collector requests no comment bodies or linked articles. | Store only approved metadata; treat source strings as values. |
| V5 — Pagination and termination | Yes | Each request asks ClickHouse for at most 10,000 rows ordered by `id`; the cursor advances only after a validated page commits, and a short or empty page completes the selection. | Avoid skipped rows, duplicates, and false completion. |
| V6 — Incomplete responses and dependency failures | Yes | Invalid payloads, HTTP-200 exceptions, rejected settings, timeouts, quota errors, and overflow leave that page and its cursor uncommitted and exit 1. | An error is neither an empty page nor a deletion signal. |
| V7 — Interrupted or failed SQLite commits | Yes | A failure or kill rolls back the page and cursor together; reopening keeps earlier commits and replays unfinished work. | Provide durable historical resume. |
| V8 — Overlapping historical and daily records | Yes | Each HN ID keeps one row; historical inserts leave existing rows untouched, and daily upserts update them in place. | Retain archived posts without version history or delete-and-reinsert. |
| V9 — Daily window and restart | Yes | Each invocation freezes `[T - 432000, T)` in UTC, includes the lower bound, excludes `T`, and scans a fresh window even after a failed or interrupted run. | Use creation time, not update time or the last successful run. |
| V10 — Newly eligible posts and eligible refresh | Yes | A zero-to-five post inside the window is inserted; a still-eligible saved post takes its latest title, URL, text, and count, even when nine drops to six. | Refresh the eligible snapshot, not the maximum count. |
| V11 — Retention and refresh boundary | Yes | Saved rows that are omitted, drop below five, become deleted, or fall outside the window stay unchanged; no ineligible row is created. | Preserve the last eligible snapshot. |
| V12 — Failure output | Yes | Failures name the failed operation. | Distinguish durable progress from attempted work. |
| Complete HN coverage and real-time freshness | No | Mirror omissions, mirror delay, and changes behind a historical cursor can stay absent; completion describes reads of the selected mirror range. | The mirror is trusted, and each page reflects its read time. |
| Catch-up or metadata refresh outside five days | No | Daily runs leave older gaps and older saved metadata stale, including after eight days offline. | The fixed daily window is settled. |
| Automatic retries or provider fallback | No | A failed request stops the command; Stan reruns it, and switching mirrors requires a design amendment. | One ClickHouse adapter without fallback is the approved cap. |
| Simultaneous collectors | No | Stan serializes invocations; an overlapping writer can fail with `database is locked` after SQLite's 5-second timeout. | Pass 1 assumes one local writer; add no coordination. |
| Hard database, response-byte, or per-post text limits | No | Pages are row-bounded, so their byte size varies; the catalog may exceed planning estimates. | Estimates are not caps; approved metadata is not truncated. |
| Deletion records and metadata version history | No | Newly encountered deleted posts leave no record; retained posts keep one eligible snapshot. | Preserve the explicit storage cap. |
| Independent HN coverage checking | Defer | Official item enumeration waits for a separate coverage proposal. | Mirror omissions are accepted in this delivery. |
| Comments, article bodies, search, live parsing, and reports | Defer | These stay out of the collector; later-stage one-pagers define their behavior and compatibility. | Preserve the approved stage boundary. |

## Test plan

### Unit tests

Run `python3 -m unittest discover -s tests` from the repository root for every offline test. `test_clickhouse.py` feeds canned bodies through an injected `urlopen` to cover V4–V6: complete, empty, truncated, malformed, and HTTP-error responses. `test_collect.py` uses a fake clock and source for V1 and V8–V11, including exact window edges and eight days offline; one saved post moving `5 → 9 → 6 → 4 → deleted` must end with its six-comment snapshot. `test_cli.py` covers V1 and V12, including exit codes.

### Integration tests

`test_catalog.py` uses temporary real SQLite files for V2, V7, V8, and V12. It reopens committed pages, replays IDs, and injects failures before commit and between row writes and the cursor update. A subprocess killed after a reported commit must leave both posts and cursor.

### End-to-end tests

Through `main()`, with an injected HTTP opener and a real SQLite file, run `backfill` failing on page two, then `backfill` and `daily`, asserting resume, counts, and retention (V7–V12). Before acceptance, run one bounded smoke test against the live playground:

```bash
python3 -m hn_search --db /tmp/hn-smoke.sqlite3 backfill --through-id 300000
python3 -m hn_search --db /tmp/hn-smoke.sqlite3 backfill
python3 -m hn_search --db /tmp/hn-smoke.sqlite3 daily
```

On 2026-10-25, IDs 1–300,000 held 10,993 eligible posts: one full page, one short page, then `complete=true`. The rerun must leave the saved IDs unchanged, and `daily` must add the current window's eligible posts, 476 on that day. The suite needs no full import and tests no `No` or `Defer` capability.

## Other considerations

### Observability

`collect_history()` and `collect_daily()` print one progress line after each commit, never before it, with the source, the historical range or daily window, the committed cursor, completion, and the catalog-wide saved-post count:

```text
historical source=play.clickhouse.com/hackernews_history range=1..50235582 next_id=271044 complete=false saved_posts=10000
```

These lines report committed progress, not HN coverage. On failure, stderr names the failed operation and says whether a rerun resumes history or starts a fresh daily window.

### User-facing changes

#### Internal API changes

No existing internal API changes. Among the proposed functions, `fetch_page()` returns one validated page or raises, `commit_page()` owns the single page-and-cursor transaction, and `collect_history()` and `collect_daily()` choose the mode and bounds.

#### Public API changes

**Before:** The repository has no runnable collector.

**After:** From the repository root, with Python 3.12+:

```bash
python3 -m hn_search --db hn.sqlite3 backfill [--from-id N] [--through-id N]
python3 -m hn_search --db hn.sqlite3 daily
```

`--db` is required. Bound flags take effect on the first `backfill`; later runs resume the stored bounds. `daily` has no lookback or catch-up flag. `argparse` usage errors exit 2; invalid bounds, incompatible catalogs, and collection failures exit 1 with the next action, such as rerunning later with the same database. No HTTP server or environment variable is added.

### Data model changes

#### Database changes

`open_catalog()` creates schema v1 and sets `PRAGMA user_version = 1` in one transaction:

```sql
CREATE TABLE posts (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  url TEXT NOT NULL,
  text TEXT NOT NULL,
  created_at INTEGER NOT NULL,  -- UTC epoch seconds
  descendants INTEGER NOT NULL CHECK (descendants >= 5),
  hn_url TEXT GENERATED ALWAYS AS ('https://news.ycombinator.com/item?id=' || id) VIRTUAL
);
CREATE TABLE collection_progress (
  source TEXT NOT NULL,
  next_id INTEGER NOT NULL,
  complete INTEGER NOT NULL CHECK (complete IN (0, 1)),
  from_id INTEGER, through_id INTEGER
);
```

`hn_url` keeps the approved HN-link field without storing duplicate bytes: SQLite computes it from `id` on read, saving about 28 MiB at the observed 661,233 posts. Generated columns require SQLite 3.31.0 or newer. [SQLite generated columns](https://www.sqlite.org/gencol.html). `collection_progress` holds at most the one historical row, not an attempt log. The ID primary key is the only index. Bind every stored value as a parameter, keep default journaling and synchronous settings, and never use `REPLACE`, which deletes a row before reinserting it. There are no existing migrations. **Deferred — future schema changes:** a later feature must define migration and rollback before adding comment storage or changing v1.

#### File system changes

The catalog and progress live only in the `--db` file and SQLite's journal. Add no raw-response dumps, checkpoint files, or filesystem validation guarantees.

### Deployment

Run the module from the checkout; no database service, package install, or global CLI is required. Run `backfill`, rerunning after any failure, until it reports `complete=true`. Then run `daily` immediately, so its window covers posts created after the historical bound was fixed, and once a day after that, never alongside another collector. **Deferred — daily scheduler:** installing a host scheduler for `daily` is a separate operational change. Stopping or rolling back the collector leaves the SQLite file in place; there is no earlier version or schema to migrate.

-----------------------------------

# Legend (do not delete)

Scope growth labels mean:

- **INCLUDE** accepts the resulting scope;
- **CONSTRAIN** limits the behavior that causes it;
- **EXCLUDE** leaves the broader work outside this proposal.

Each label is valid only when its row also names the repeatable growth
mechanism and a finite, observable cap.
