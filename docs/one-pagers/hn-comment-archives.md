# HN on-demand comment archives

## Pass 0: Problem or opportunity framing

### Who is the user, what do we know about their behavior, and how correct does the result need to be?

- **User:** Stan, researching what HN thinks about a topic.
- **Their behavior:** Stan confirms search keywords and expects every matching catalog story to be downloaded locally before AI decides whether its discussion is relevant.
- **Edge-case tolerance:** Save all obtainable comments with their reply context, show missing content and incomplete downloads honestly, and resume interrupted work without discarding saved items.

### What is the prevailing user problem or opportunity?

- **Problem or opportunity:** Stan has a local catalog of thread metadata but cannot inspect or analyze the discussions without downloading their comments.

### What is the proposed solution, and why is it right for the user?

- **Solution:** Add on-demand archives of selected HN roots and their obtainable comment trees, preserving original content, item IDs, reply relationships, source links, retrieval times, and completion state in local SQLite storage with reusable JSON exports.
- **Why it fits the user:** Stan downloads each selected discussion once and can reuse the same evidence for classification, deep analysis, and future questions.

For “buying versus renting,” the companion [topic pipeline](https://github.com/stanislavkozlovski/hn-search/blob/design/hn-topic-pipeline/docs/one-pagers/hn-topic-pipeline.md) supplies **every deterministic metadata match** to this archive before classification; an already saved snapshot satisfies the download step without another fetch.
The archive owns source evidence and download progress; the topic pipeline owns keyword confirmation, AI decisions, relevant-story folders, and reports.
The archive preserves the root post and comment authors within their thread context, without building cross-thread commenter profiles or fetching linked article bodies.
Automatic refresh stays outside this design, as [previously agreed](hn-topic-research.md#agent-edge-case-scan).

### How would you describe the end-to-end user experience?

- **End-to-end user experience:** Stan requests a set of catalog stories directly or through the topic pipeline, sees each download complete or remain incomplete, and receives reusable local comment trees and exports with links back to the original posts and replies.

### What existing data, behavior, or integrations must keep working?

- **Legacy data:** Preserve schema-v1 `posts`, the historical `collection_progress` checkpoint, and all previously collected metadata while adding archive storage.
- **Legacy behavior:** Keep `python3 -m hn_search --db hn.sqlite3 collect` and its five-comment admission, historical resume, five-day refresh, and retained snapshots unchanged.
- **Existing integrations:** Use the official HN item API for roots and replies and provide archived discussions to the companion topic pipeline; this downloader requires no AI client or model.
- **Compatibility tolerance:** Additive database changes are acceptable, existing collected data must survive, and interrupted archive work must remain resumable.

Grounding at merged commit [`64703b5`](https://github.com/stanislavkozlovski/hn-search/tree/64703b58fedbe19ef8e80612ab1d825e880e2eaf): [`open_catalog`](../../hn_search/catalog.py) creates only `posts` and `collection_progress`, and [`main`](../../hn_search/__main__.py) exposes only `collect`.
The catalog tests and existing schema-v1 smoke database confirm saved metadata and progress but no legacy comment tables.
Preserve the collector's serialized-writer assumption; later passes must specify migration and rollback rather than treating its permissive schema-version handling as proof of compatibility.

The [official API](https://github.com/HackerNews/API#items) exposes individual items, ordered `kids`, reply `parent` IDs, HTML `text`, and deleted/dead flags; poll choices live in separate `parts` items.
Downloading items individually does not provide an atomic historical snapshot, so completeness must describe what was obtainable and observed rather than reconstructing missing text or promising every comment ever posted.
Puerto's local `comment_processor/comment_export.py` and `ARCHITECTURE.md` provide a local precedent for reply-preserving JSON/Markdown artifacts; its refresh-history machinery is not a requirement here.

### Agent edge-case scan

| Edge case | What happens if ignored | What handling it adds | User decision |
|---|---|---|---|
| When HN receives new replies during a download or a later resume, the downloader can miss additions to parents it already fetched. | The archive records its observation interval and keeps the child lists it encountered, accepting missing concurrent additions. | The downloader rechecks parents for additional child IDs before finishing, with an explicit bound on repeated reconciliation agreed in Pass 1. | UNDECIDED — HANDLE / IGNORE |
| When a selected catalog entry is a poll, its comments can refer to choices stored separately from the root and replies. | The archive saves the question and comments without poll-choice text, leaving some replies ambiguous. | The downloader also saves the poll's option text and observed votes as discussion context. | UNDECIDED — HANDLE / IGNORE |
| When Stan directly requests a thread ID absent from the metadata catalog, the catalog-backed archive cannot resolve it. | The CLI rejects the request and explains that this version archives only catalog entries. | The archive accepts explicit roots outside the catalog's admission rule without changing what the metadata collector stores. | UNDECIDED — HANDLE / IGNORE |
