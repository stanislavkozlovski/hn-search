# HN topic research

## Pass 0: Problem or opportunity framing

### Who is the user, what do we know about their behavior, and how correct does the result need to be?

- **User:** Stan.
- **Their behavior:** Stan asks “What does HN think about X?”, searches a local HN archive, and reads a report linked to the discussions.
- **Edge-case tolerance:** Missing relevant eligible posts present in the chosen historical mirror is the main failure; finding them matters more than excluding every irrelevant candidate.

### What is the prevailing user problem or opportunity?

- **Problem or opportunity:** Stan cannot quickly find and synthesize HN discussions across its history, so he misses useful arguments about topics he cares about.

### What is the proposed solution, and why is it right for the user?

- **Solution:** First deliver a resumable metadata catalog from a trusted historical mirror, keeping public top-level HN posts with at least five reported total comments and storing HN ID, title, external URL, HN link, original post text when present, creation date, and reported total comment count.
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
| When HN returns a deleted story during the first sweep, the sweep skips it without preserving deletion records. | Stan sees fewer usable threads than the crawler checked and cannot tell which items were deleted. | The project records deleted item IDs and reports the gap in archive coverage. | IGNORE |
| When the source reports fewer than five total comments on a public top-level HN post, the catalog excludes the whole post record. | The catalog stores low-comment posts and uses disk space outside the intended scope. | The catalog checks the source's reported total comment count on each top-level post before persisting it, excludes the whole post record below five, and fetches no comment bodies to determine eligibility. | HANDLE |
| When a historical sweep stops before finishing the selected range in the chosen mirror, the local catalog contains only part of that range's eligible posts. | Stan sees a partial catalog without knowing that eligible posts in the selected mirror range remain unprocessed. | The project durably records progress, retains previously archived posts, resumes unfinished ranges, and shows coverage as incomplete until it has processed the selected historical range in that mirror. | HANDLE |
| When a mirror omits an eligible public HN post, the catalog cannot discover that post through the mirror. | Stan receives a fully processed mirror catalog that can still omit eligible HN discussions. | The project enumerates the official HN item range to establish coverage independently of the mirror. | IGNORE |

HN exposes the reported total as `descendants`; `kids` lists direct children, so its length is not the total comment count. [HN API item fields](https://github.com/HackerNews/API/blob/8a0528f538bca407c2ceeeefc9bee48bdb99c1c8/README.md#items).

For example, a public top-level post with `descendants: 5` and two `kids` qualifies; one with `descendants: 4` gets no catalog record.

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

Stan chose a rolling [five-day window](https://github.com/stanislavkozlovski/hn-search/pull/1#discussion_r4159288445) based on post creation time and [the same window on every invocation](https://github.com/stanislavkozlovski/hn-search/pull/1#discussion_r4159298725), including restart after failure or downtime. Daily collection accepts gaps outside that window.

| Edge case | What happens if ignored | What handling it adds | User decision |
|---|---|---|---|
| When the mirror raises a previously skipped post from zero comments to at least five within its first five days, the daily collector encounters newly eligible metadata. | A collector that only advances past new IDs misses the now-eligible post. | The daily collector scans the preceding five days by post creation time on every invocation and inserts qualifying HN IDs absent from the catalog. | HANDLE |
| When a post leaves the five-day creation-time window before daily collection saves it, the daily collector no longer revisits it. | Stan accepts missing posts after downtime and posts that first qualify or reach the mirror outside the window. | The daily collector backfills earlier creation times or catches up missed intervals from the last successful run. | IGNORE |

**Deferred — saved-metadata refresh review:** The separate [request to refresh saved metadata](https://github.com/stanislavkozlovski/hn-search/pull/1#discussion_r4159288445) revisits the earlier `IGNORE` decision for archived rows. This timing decision does not choose replacement, deletion, or retention semantics; those remain for that review.

## Pass 1: High-level design

**Review status:** The daily five-day window and restart gap acceptance are settled. Pass 1 remains under review; saved-metadata refresh semantics remain a separate review concern.

## Proposal

### In-scope goals

- Import qualifying top-level metadata from the selected ClickHouse mirror into a local catalog.
- Resume unfinished historical ranges while retaining committed records.
- Discover newly eligible posts created within the preceding five days on every daily invocation, including restarts, without automatic catch-up beyond that window.
- Show the source, selected range, saved-post count, and whether collection finished.

### Out-of-scope non-goals

Automatic daily catch-up outside the five-day window is excluded. Saved-metadata refresh remains deferred to its separate review concern. Comment downloads, live parsing, article bodies, keyword/AI topic selection, reports, and independent verification against HN remain deferred.

### Potential scope growth

| Risk | Growth mechanism — when it happens in practice | Explicit cap | Decision |
|---|---|---|---|
| Source adapters multiply. | Each extra mirror adds field mappings, coverage rules, and interruption behavior when the collector switches providers. | One adapter for ClickHouse `hackernews_history`; no automatic fallback or upstream reconciliation. | CONSTRAIN |
| Restarted imports multiply saved records. | Replaying fetched metadata after an interruption can create duplicate posts and repeat finished work. | One catalog record per HN ID, with durable progress for the selected historical range. | CONSTRAIN |
| Missed daily runs accumulate backfill work. | Catching up from the last successful run adds more historical metadata to scan as failures or downtime accumulate. | Every daily invocation scans only the preceding five days by post creation time, including restarts; no widening or automatic catch-up. | CONSTRAIN |
| Stored content expands beyond metadata. | Following each post's comment tree or external link introduces more downloads and stored bodies. | Only the approved post metadata and collection progress; zero comment bodies, article bodies, or AI outputs. | EXCLUDE |

### Public behavior changes (before / after)

- **Before:** The [repository at this design head](https://github.com/stanislavkozlovski/hn-search/tree/8f6c803ccb5ca0571e50f46c446120b48c74614e) contains only this proposal; Stan has no collection command or archive.
- **After:** Stan starts a historical collection, sees its selected mirror range and saved-post count, and reruns it after interruption to finish the remaining range. Each daily invocation scans only posts created in the preceding five days and discovers newly eligible, absent IDs; restarting after eight days offline uses the same five-day window and leaves the older gap. Exact command names belong to Pass 2.

### Historical source and collection

Use the public ClickHouse `hackernews_history` table. Its server-side selection can return only top-level post metadata meeting `descendants >= 5`. Its versioned rows require selecting the latest available version per HN ID before applying eligibility; the sizing probe used `FINAL`. The provider documents the [self-updating mirror](https://presentations.clickhouse.com/2026-embeddings/), and the [research note](../research/hn-metadata-sizing.md) records the checked schema and live query.

Choose the historical ID range at the start and retain that bound when resuming. Read it in bounded portions, persist qualifying records and progress together, and keep completed portions across failures. For example, if fetching the next portion fails, previously committed posts remain readable and the range stays incomplete; restarting resumes unfinished work without duplicate catalog records.

A post with four reported comments gets no record; five qualifies. Store HN ID, title, external URL, HN link, original post text when present, creation date, and reported total comment count. Read no comment bodies to count them and follow no external article links. Metadata reflects when each portion was read; finishing the range does not establish exhaustive upstream coverage.

### Database and expected size

Choose **SQLite** for the metadata catalog and collection progress. Stan's local collector can commit both together without operating a database server, and the measured data fits comfortably in a local file. The workload assumes one local writer; SQLite permits one writer at a time, which is sufficient for this scope. [SQLite guidance](https://www.sqlite.org/whentouse.html).

On **2026-10-01**, the mirror query found **661,233** nondeleted top-level posts with at least five reported comments. Their titles, URLs, HN links, and original text totaled **166 MiB**, excluding numeric fields and database overhead. These are mirror observations, not a count of every qualifying HN post. [Query, filters, and results](../research/hn-metadata-sizing.md).

For planning, assume **0.5–1 KiB per stored post** including row and basic-index overhead:

| Example | Estimated main database size |
|---|---|
| 100,000 qualifying posts | 49–98 MiB |
| The observed 661,233 posts | 323–646 MiB |
| 1,000,000 qualifying posts | 488–977 MiB |

These are estimates, not measured SQLite file sizes or hard limits; journals, backups, temporary space, and future search indexes are additional.

### Daily metadata collection: Rolling five-day window

Every daily invocation scans the preceding five days by post creation time (`time`) in ClickHouse `hackernews_history`, including restart after failure or downtime. The window is relative to that invocation, never widened or anchored to the last successful run; daily collection performs no automatic catch-up.

For example, a post skipped at zero comments on Tuesday is inserted on Wednesday if the mirror then reports at least five and the post remains within the five-day window. Daily discovery inserts qualifying HN IDs absent from the catalog; saved-row refresh semantics remain in the separate review concern.

After eight days offline, restart scans only posts created in the preceding five days and leaves the older gap. The catalog accepts posts missed after they leave the window, including posts that first qualify or reach the mirror later. This daily limit does not change the historical sweep's guarantee to resume its retained ID range until it finishes.

Daily scheduling still inherits mirror delay and cannot promise real-time HN freshness. Live parsing, comment-tree refresh, and report regeneration remain deferred.

## Rejected design alternatives

| Alternative | Why rejected |
|---|---|
| The collector enumerates the entire official HN item-ID range to verify mirror coverage. | The collector would add per-item requests across the shared post/comment ID space for the upstream guarantee Stan explicitly excluded. |
| The collector downloads the entire HN archive before filtering locally. | The collector would transfer comment-bearing data that server-side metadata selection can exclude. |
| The catalog runs PostgreSQL for this first delivery. | PostgreSQL would add a database service and its configuration before this local, single-writer catalog needs them. |

-----------------------------------

# Legend (do not delete)

Scope growth labels mean:

- **INCLUDE** accepts the resulting scope;
- **CONSTRAIN** limits the behavior that causes it;
- **EXCLUDE** leaves the broader work outside this proposal.

Each label is valid only when its row also names the repeatable growth
mechanism and a finite, observable cap.