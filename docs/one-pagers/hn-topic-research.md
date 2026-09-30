# HN topic research

## Pass 0: Problem or opportunity framing

### Who is the user, what do we know about their behavior, and how correct does the result need to be?

- **User:** Stan.
- **Their behavior:** Stan asks “What does HN think about X?”, searches a local HN archive, and reads a report linked to the discussions.
- **Edge-case tolerance:** Missing relevant public top-level posts with at least five reported total comments is the main failure; finding them matters more than excluding every irrelevant candidate.

### What is the prevailing user problem or opportunity?

- **Problem or opportunity:** Stan cannot quickly find and synthesize HN discussions across its history, so he misses useful arguments about topics he cares about.

### What is the proposed solution, and why is it right for the user?

- **Solution:** First deliver a resumable metadata catalog of public top-level HN posts with at least five reported total comments, storing HN ID, title, external URL, HN link, original post text when present, creation date, and reported total comment count.
- **Why it fits the user:** One local thread catalog lets Stan start future topic searches without repeating the full HN discovery pass.

Metadata ingestion includes no comment parser or AI integration.

### How would you describe the end-to-end user experience?

- **End-to-end user experience:** Stan starts catalog collection, sees coverage of the selected historical range, and resumes an interrupted sweep without losing already archived posts.

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
| When a historical sweep stops before reaching the oldest HN items, the local catalog contains only part of HN history. | Stan sees a partial catalog without knowing that older eligible posts remain unprocessed. | The project durably records progress, retains previously archived posts, resumes unfinished ranges, and shows coverage as incomplete until it has processed the selected historical range. | HANDLE |
| When a mirror omits an eligible public HN post, the catalog cannot discover that post through the mirror. | Stan receives a fully processed mirror catalog that can still omit eligible HN discussions. | The project enumerates the official HN item range to establish coverage independently of the mirror. | UNDECIDED — HANDLE / IGNORE |

HN exposes the reported total as `descendants`; `kids` lists direct children, so its length is not the total comment count. [HN API item fields](https://github.com/HackerNews/API/blob/8a0528f538bca407c2ceeeefc9bee48bdb99c1c8/README.md#items).

For example, a public top-level post with `descendants: 5` and two `kids` qualifies; one with `descendants: 4` gets no catalog record.

A failed or interrupted fetch does not establish that an item is deleted.

**Deferred — source selection:** The choice of data source remains pending [comment 5915555393](https://github.com/stanislavkozlovski/hn-search/pull/1#issuecomment-5915555393).

**Deferred — later stages:** Keyword/AI topic selection, on-demand comment archiving, and `stan_ai_client` reports each require a separate one-pager.

**Deferred — linked-report experience:** Stan asks “What does HN think about buying versus renting?”, the tool searches its thread catalog and downloads matching comment trees, then gives him a deep report of arguments, counterarguments, and representative linked comments.

**Deferred — later-stage edge cases:** The existing `IGNORE` decisions below apply to those later stages.

| Edge case | What happens if ignored | What handling it adds | User decision |
|---|---|---|---|
| When HN users discuss a topic under a story whose title, URL, and original post do not reveal it, the topic filter skips that story. | Stan's report omits the relevant discussion even though the thread exists in the local catalog. | The project searches comment text beyond the title and URL candidates before final topic selection. | IGNORE |
| When a saved HN thread gains comments after its first download, the local comment tree and report become stale. | Stan reads a report that omits newer arguments in that thread. | The project refreshes saved threads and updates affected analyses with a visible retrieval time. | IGNORE |

**Deferred — saved-thread refresh:** Future sweeps may revisit recent threads, potentially those younger than one year; the MVP adds no refresh schedule, recent-thread heuristic, or automatic reanalysis.
