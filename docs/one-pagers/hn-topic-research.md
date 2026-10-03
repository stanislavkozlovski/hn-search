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

None for implementation. At [the checked head](https://github.com/stanislavkozlovski/hn-search/tree/4cd7d1c91e27729b074310fec60854ab742680af), `git ls-tree` and `rg` found only this proposal and `docs/research/hn-metadata-sizing.md`: no source, schema, fixtures, tests, entrypoints, or automation. The files, functions, and commands below are **proposed additions**, not existing interfaces.

### New files expected

Use Python 3.12+ and its standard library (`argparse`, `urllib.request`, `json`, `sqlite3`, and `unittest`); no third-party runtime dependency is needed.

| New file | Responsibility |
|---|---|
| `hn_search/__init__.py`, `hn_search/__main__.py` | Make `python3 -m hn_search` runnable; `main()` parses commands and reports failures. |
| `hn_search/clickhouse.py` | `max_id()` obtains the historical bound; `fetch_page()` issues and validates one metadata query. |
| `hn_search/catalog.py` | `open_catalog()` initializes or reopens SQLite; `commit_page()` commits metadata and progress together; `read_status()` reads saved progress and counts. |
| `hn_search/collect.py` | `collect_history()` resumes saved ID bounds; `collect_daily()` captures and scans one five-day window. |
| `tests/test_clickhouse.py`, `tests/test_catalog.py`, `tests/test_collect.py`, `tests/test_cli.py`, `tests/test_clickhouse_integration.py` | Cover response handling, persistence, collection semantics, CLI behavior, and actual ClickHouse query semantics. |
| `README.md`, `.gitignore` | Document invocation and recovery; exclude local SQLite files and Python caches from Git. |

### Maintainability and refactor call

No preparatory refactor is needed. Share one query adapter and one page-commit path; keep historical insertion and daily upserts explicit. Inject the clock and HTTP transport for tests. Do not introduce an adapter registry, ORM, task queue, migration framework, or run-history archive.

### Collection and commit flow

1. **Historical collection:** On the first `backfill`, choose inclusive bounds, defaulting to `1..max(id)` from the mirror, and commit them before fetching pages. Explicit bounds must be positive UInt32 IDs within that observed range. Subsequent invocations reuse saved bounds; conflicting flags fail without resetting progress. A completed range stays complete.
2. **Daily collection:** Capture UTC time `T` once, to whole seconds. Reset only daily progress and scan creation times `[T - 432000, T)`, starting again at the first ID. Every invocation does this, even after an interrupted daily run; historical progress remains untouched.
3. **Selection:** `fetch_page()` uses the following historical query. Daily queries replace the upper-ID predicate with `time >= toDateTime({window_start:UInt32}, 'UTC') AND time < toDateTime({window_end:UInt32}, 'UTC')`.

```sql
SELECT id, title, url, text, toUnixTimestamp(time) AS created_at, descendants
FROM hackernews_history FINAL
WHERE id >= {next_id:UInt32} AND id <= {through_id:UInt32}
  AND type IN ('story', 'poll', 'job')
  AND parent = 0 AND deleted = 0 AND descendants >= 5
ORDER BY id LIMIT 10000
SETTINGS optimize_move_to_prewhere_if_final = 0,
         result_overflow_mode = 'throw',
         timeout_overflow_mode = 'throw',
         read_overflow_mode = 'throw'
FORMAT JSON
```

Keep eligibility after version selection: `PREWHERE` can otherwise filter a newer ineligible version before `FINAL`. Do not add `dead = 0`; the [checked sizing query](../research/hn-metadata-sizing.md#reproducible-measurement) deliberately includes those posts. [ClickHouse PREWHERE semantics](https://clickhouse.com/docs/sql-reference/statements/select/prewhere).

Send typed parameters through HTTPS GET to `https://play.clickhouse.com/?user=play`, with `wait_end_of_query=1`. Read and validate the entire JSON object before writing: reject HTTP errors, truncated or malformed bodies, an `exception` field, mismatched row counts, invalid required fields, and duplicate, unordered, or out-of-range IDs. HTTP 200 alone does not establish query success. Keep overflow settings at `throw`; if the provider rejects them, stop. [HTTP error behavior](https://clickhouse.com/docs/interfaces/http#http_response_codes_caveats).

The schema and these query settings were rechecked on **2026-10-03**: a historical query returned 10,000 ordered rows, and a UTC-window query succeeded. This verifies the query shape, not a full import or throughput guarantee. [Live schema query](https://play.clickhouse.com/?user=play&query=SHOW%20CREATE%20TABLE%20hackernews_history%20FORMAT%20JSON).

`commit_page()` inserts absent IDs during historical collection and uses `ON CONFLICT(id) DO UPDATE` during daily collection, updating metadata in place. Derive `hn_url` from `id`; preserve source strings, including HTML, Unicode, and empty URL/text. Historical replay never overwrites a saved daily snapshot. Neither path deletes posts.

Commit the page and its next cursor in one SQLite transaction. A full page advances to its last ID plus one; a successful short or empty page also marks the remaining selection complete. Historical completion sets the cursor beyond the retained upper bound. A crash before commit replays that page; a crash after commit resumes after it. For example, failure while fetching page two leaves page one's posts and progress intact.

Fetch one page at a time with a 90-second socket timeout. A transport, quota, decoding, or SQLite failure ends the command with a nonzero exit; Stan reruns it after resolving the failure. No automatic retries or provider fallback are added.

## Validation matrix

`Yes` rows are implementation obligations; `No` rows retain approved limitations; `Defer` rows add no implementation now.

| Validation | Disposition | Behavior or consequence | Reason |
|---|---|---|---|
| V1 — Command arguments and retained historical bounds | Yes | Reject malformed, reversed, out-of-range, or conflicting bounds without resetting saved work; resuming never expands the range when the mirror grows. | Preserve the selected historical sweep. |
| V2 — Catalog initialization and reopening | Yes | Initialize an empty database, reopen v1, and reject unversioned populated databases or other schema versions without replacing data. | No legacy schema exists; saved records must survive reruns. |
| V3 — Latest-version eligibility | Yes | Select the latest version before checking type, parent, deletion, and `descendants >= 5`; four fails and five qualifies regardless of `kids` length. | Enforce the approved admission rule without resurrecting older eligible versions. |
| V4 — Field mapping and content boundary | Yes | Preserve required values and empty strings, construct the HN link, and transfer no comment bodies or linked articles. | Store only approved metadata; treat source text and URLs as values. |
| V5 — Pagination and termination | Yes | Fetch at most 10,000 rows per request in strict ID order; advance only after a validated page and commit, including zero-result completion. | Avoid skipped rows, duplicate records, and false completion. |
| V6 — Incomplete responses and dependency failures | Yes | Reject invalid payloads, HTTP-200 exceptions, timeouts, quota errors, and overflow; leave the failed page and its progress uncommitted. | An error is neither an empty page nor a deletion signal. |
| V7 — Interrupted or failed SQLite commits | Yes | Roll back metadata and progress together; reopening retains earlier commits and safely replays unfinished work. | Provide durable historical resume. |
| V8 — Overlapping historical and daily records | Yes | Keep one row per HN ID; historical insertion leaves existing snapshots intact and daily upsert updates them in place. | Retain archived posts without version history or delete-and-reinsert behavior. |
| V9 — Daily window and restart | Yes | Freeze UTC bounds per invocation, include the lower bound, exclude `T`, and restart with a newly calculated five-day window and cursor. | Use creation time, not update time or the last successful run. |
| V10 — Newly eligible posts and eligible refresh | Yes | Insert a zero-to-five post inside the window; replace saved title, URL, text, and count when still eligible, even if its count decreases from nine to six. | Refresh the eligible snapshot, not the maximum observed count. |
| V11 — Retention and refresh boundary | Yes | Keep saved rows unchanged when omitted, below five, deleted, or outside the daily window; create no new ineligible records. | Preserve the last eligible snapshot. |
| V12 — Status and failure output | Yes | Show source, historical bounds or daily window, committed cursor, catalog-wide saved count, and completion separately for each mode; failures exit nonzero. | Distinguish durable progress from attempted work. |
| Complete HN coverage and real-time freshness | No | Mirror omissions, delayed updates, and changes behind a historical cursor can remain absent; completion describes reads of the selected mirror range. | The mirror is trusted and each page reflects its read time. |
| Catch-up or metadata refresh outside five days | No | Daily runs leave older gaps and saved metadata stale, including after eight days offline. | The fixed daily window is settled. |
| Simultaneous collectors | No | Stan must serialize invocations; overlapping runs are unsupported and can fail on SQLite locking. | Pass 1 assumes one local writer; add no coordination protocol. |
| Hard database, response-byte, or per-post text limits | No | Row-bounded pages still have variable byte sizes; the catalog may exceed planning estimates. | Estimates are not caps; do not truncate approved metadata. |
| Deletion records and metadata version history | No | Newly encountered deleted posts leave no record, and retained posts have one eligible snapshot. | Preserve the explicit storage cap. |
| Independent HN coverage checking | Defer | Revisit official item enumeration in a separate coverage proposal. | Mirror omissions remain accepted in this delivery. |
| Comments, article bodies, search, live parsing, and reports | Defer | Keep these out of the collector; later-stage one-pagers must define their behavior and compatibility. | Preserve the approved stage boundary. |

## Test plan

### Unit tests

Run `python3 -m unittest discover -s tests` from the repository root. `test_clickhouse.py` covers V4–V6 with complete, empty, truncated, malformed, exception-bearing, and wrongly ordered responses. `test_collect.py` uses a fake clock and source to cover V1 and V8–V11, including exact window boundaries, eight-day downtime, and a saved post progressing `5 → 9 → 6 → 4 → deleted`. `test_cli.py` covers V1 and V12, including nonzero errors and status that neither contacts ClickHouse nor creates a missing catalog.

### Integration tests

`test_catalog.py` uses temporary real SQLite databases for V2, V7, V8, and V12: reopen committed pages, replay IDs, and fail before commit and between row writes and cursor updates. A subprocess interruption after a reported commit must preserve both posts and progress.

`test_clickhouse_integration.py` runs the actual adapter SQL against a disposable local ClickHouse `hackernews_history` fixture matching the checked schema. Cover V3–V6 and V9 with duplicate versions, latest deletions/count reductions, stories/polls/jobs versus comments/poll options, `dead` posts, and UTC boundaries. This test must not create fixtures on the public playground. Require an explicit run before implementation acceptance: `HN_SEARCH_TEST_CLICKHOUSE_URL=http://127.0.0.1:8123 python3 -m unittest discover -s tests -p test_clickhouse_integration.py`; ordinary offline runs skip it when that test-only URL is absent.

### End-to-end tests

Exercise `backfill → interruption → backfill → status → daily → status` through `main()` with a test-injected HTTP transport and real SQLite, confirming resume, counts, and retention (V7–V12). Before implementation acceptance, also smoke-test a bounded historical range against the public mirror and rerun it to confirm stable saved IDs and completion. No full historical import is required for the test suite; no tests implement `No` or `Defer` capabilities.

## Other considerations

### Observability

Print progress only after commits. For example, `mode=historical range=1..1000000 next_id=271044 complete=false saved_posts=10000` reports a committed page, not a percentage of HN coverage. `status` reports historical and daily state separately, including `not started`; stderr identifies the failed operation and tells Stan whether rerunning resumes history or starts a fresh daily window.

### User-facing changes

#### Internal API changes

No existing internal API changes. The proposed `fetch_page()` returns one validated page; `commit_page()` owns its single metadata-and-progress transaction. Collection functions select the mode and bounds.

#### Public API changes

**Before:** The repository provides no runnable collector or status command.

**After:** From the repository root, with Python 3.12+:

```bash
python3 -m hn_search --db hn.sqlite3 backfill
python3 -m hn_search --db hn.sqlite3 daily
python3 -m hn_search --db hn.sqlite3 status
```

`--db` is required. First backfill optionally accepts `--from-id` and `--through-id`; rerunning without those flags resumes the stored selection. `daily` has no lookback or catch-up flag. `status` reads local state without initiating collection. Invalid arguments, incompatible catalogs, and collection failures return nonzero with the next action; transient mirror failures call for rerunning later with the same database. There are no renamed entrypoints, HTTP server, or product configuration environment variables.

### Data model changes

#### Database changes

Create schema v1 with `PRAGMA user_version = 1` and two tables:

- `posts`: `id INTEGER PRIMARY KEY`; `title`, `url`, `hn_url`, and `text` as non-null text; `created_at` and `descendants` as non-null integers, with `descendants >= 5`. Store UTC epoch seconds and retain empty source strings. The ID primary key is the only initial index.
- `collection_progress`: `mode TEXT PRIMARY KEY` constrained to `historical` or `daily`, plus `source`, `next_id`, and `complete`; historical rows store inclusive `from_id`/`through_id`, while daily rows store UTC `window_start`/`window_end`. Keep at most these two rows, not an attempt log. Resetting daily progress never resets historical progress or posts.

Use explicit SQLite transactions with default journaling and synchronous settings; bind stored values as parameters. Daily updates use `DO UPDATE`, not SQLite `REPLACE`. There are no existing migrations to run. **Deferred — future schema changes:** A later feature must define migration and rollback requirements before adding comment storage or changing schema v1.

#### File system changes

Persist the catalog and progress only in the selected `--db` database and SQLite's journal files. Do not add raw-response dumps, separate checkpoint files, or new filesystem validation guarantees.

### Deployment

Run the module from the checkout; no database service or global CLI installation is required. Complete the historical sweep and invoke `daily` serially on subsequent days. Host scheduler installation is **deferred** to a separate operational change. Stopping or rolling back the collector leaves the SQLite archive in place; this delivery has no earlier application version or schema to migrate.

-----------------------------------

# Legend (do not delete)

Scope growth labels mean:

- **INCLUDE** accepts the resulting scope;
- **CONSTRAIN** limits the behavior that causes it;
- **EXCLUDE** leaves the broader work outside this proposal.

Each label is valid only when its row also names the repeatable growth
mechanism and a finite, observable cap.