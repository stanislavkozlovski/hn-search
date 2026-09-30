# HN topic research

## Pass 0: Problem or opportunity framing

### Who is the user, what do we know about their behavior, and how correct does the result need to be?

- **User:** Stan.
- **Their behavior:** Stan asks “What does HN think about X?”, searches a local HN archive, and reads a report linked to the discussions.
- **Edge-case tolerance:** Missing relevant public threads is the main failure; finding them matters more than excluding every irrelevant candidate.

### What is the prevailing user problem or opportunity?

- **Problem or opportunity:** Stan cannot quickly find and synthesize HN discussions across its history, so he misses useful arguments about topics he cares about.

### What is the proposed solution, and why is it right for the user?

- **Solution:** Save every public HN thread's title, content link, HN link, original post, and date first, then filter by keywords and AI, download matching comments, and analyze them with `stan_ai_client`.
- **Why it fits the user:** One local thread catalog lets Stan start new topic searches without repeating the full HN discovery pass.

### How would you describe the end-to-end user experience?

- **End-to-end user experience:** Stan asks “What does HN think about buying versus renting?”, the tool searches its thread catalog and downloads matching comment trees, then gives him a deep report of arguments, counterarguments, and representative linked comments.

### What existing data, behavior, or integrations must keep working?

- **Legacy data:** None known; `hn-search` is a new repo with no existing archive.
- **Legacy behavior:** None known.
- **Existing integrations:** The analysis uses `stan_ai_client`; no existing cross-project integration is required.
- **Compatibility tolerance:** No old schema needs support, but later runs must retain already archived threads and comments.

### Agent edge-case scan

| Edge case | What happens if ignored | What handling it adds | User decision |
|---|---|---|---|
| When HN users discuss a topic under a story whose title, URL, and original post do not reveal it, the topic filter skips that story. | Stan's report omits the relevant discussion even though the thread exists in the local catalog. | The project searches comment text beyond the title and URL candidates before final topic selection. | IGNORE |
| When an HN story links to an external article but has no original post text, the catalog stores the article URL without its body. | Stan cannot find the story using terms that appear only in the linked article. | The project downloads and indexes linked article content with its source URL. | UNDECIDED — HANDLE / IGNORE |
| When HN returns a deleted story during the first sweep, the catalog has no title or post text to save. | Stan sees fewer usable threads than the crawler checked and cannot tell which items were deleted. | The project records deleted item IDs and reports the gap in archive coverage. | UNDECIDED — HANDLE / IGNORE |
| When a historical sweep stops before reaching the oldest HN items, the local catalog contains only part of HN history. | Stan's topic report can miss older threads without showing that the archive is incomplete. | The project records completed ID ranges, resumes the sweep, and shows coverage before reporting results. | UNDECIDED — HANDLE / IGNORE |
| When a saved HN thread gains comments after its first download, the local comment tree and report become stale. | Stan reads a report that omits newer arguments in that thread. | The project refreshes saved threads and updates affected analyses with a visible retrieval time. | UNDECIDED — HANDLE / IGNORE |
