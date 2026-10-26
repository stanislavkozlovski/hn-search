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
Automatic refresh stays outside this design, as [previously agreed](hn-topic-research.md#agent-edge-case-scan) and [reconfirmed](https://github.com/stanislavkozlovski/hn-search/pull/5#discussion_r4375376461) because there is no need for the complexity: once a thread older than 30 days is downloaded, it stays there.

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
| When HN receives new replies during a download or a later resume, the downloader can miss additions to parents it already fetched. | The archive records its observation interval and keeps the child lists it encountered, accepting missing concurrent additions. | The downloader rechecks parents for additional child IDs before finishing, with an explicit bound on repeated reconciliation agreed in Pass 1. | IGNORE |
| When a selected catalog entry is a poll, its comments can refer to choices stored separately from the root and replies. | The archive saves the question and comments without poll-choice text, leaving some replies ambiguous. | The downloader also saves the poll's option text and observed votes as discussion context. | HANDLE |
| When Stan directly requests a thread ID absent from the metadata catalog, the catalog-backed archive cannot resolve it. | The CLI rejects the request with a visible error that names each uncatalogued ID and explains that this version archives only catalog entries. | The archive accepts explicit roots outside the catalog's admission rule without changing what the metadata collector stores. | IGNORE |

## Pass 1: High-level design

**Review status:** Pass 0 is settled: concurrent reply additions are `IGNORE`, polls are `HANDLE`, and uncatalogued IDs are `IGNORE` with a visible error. Stan [requested Pass 1](https://github.com/stanislavkozlovski/hn-search/pull/5#issuecomment-6411907529); function and table names below are proposals that Pass 2 finalizes.

## Proposal

### In-scope goals

- `archive` downloads requested catalog stories and their reply trees from the official HN item API into the `--db` file and writes one JSON export per complete story.
- Each fetched item is saved unchanged with its retrieval time; `kids` order defines the reply tree, and deleted, dead, and unavailable items stay visible as such.
- A story stays `incomplete` until nothing is pending, then becomes `complete`; reruns resume incomplete stories without refetching saved items and reuse complete ones with zero requests.
- A poll also saves each option's text and vote count, as Stan [decided](https://github.com/stanislavkozlovski/hn-search/pull/5#discussion_r4375390350).
- The topic pipeline downloads its matches through the same per-story function and reads the same records.

### Out-of-scope non-goals

- Refreshing or re-downloading a saved story at any age, as Stan [reconfirmed](https://github.com/stanislavkozlovski/hn-search/pull/5#discussion_r4375376461). HN [closes threads to new comments after two weeks](https://news.ycombinator.com/newsfaq.html), so a thread older than 30 days cannot gain replies after its download; a story archived within its first two weeks keeps only the replies present at download time.
- Rechecking parents for replies added during a download, [ignored](https://github.com/stanislavkozlovski/hn-search/pull/5#discussion_r4375384280) because the archive targets historical threads; each parent keeps the `kids` list from its own fetch.
- Archiving IDs absent from `posts`, [ignored](https://github.com/stanislavkozlovski/hn-search/pull/5#discussion_r4375395034) in favor of a visible error.
- Linked article bodies, user profiles, Markdown or HTML exports, AI calls, and any change to `collect`.

### Potential scope growth

| Risk | Growth mechanism — when it happens in practice | Explicit cap | Decision |
|---|---|---|---|
| Item requests multiply with matched comments. | When the topic pipeline archives every keyword match, each reported comment adds one HN request. On 2026-10-26, a case-insensitive title probe for the four buying-versus-renting keywords matched 318 eligible stories with 24,538 reported comments, and the largest eligible story, `42057647`, reports 9,274. | One request per root, reply, and poll option, sent one at a time; no parallel requests, sampling, or per-story item limit. | CONSTRAIN |
| Failure states multiply with request count. | When one of roughly 25,000 requests times out, automatic retries would add backoff, give-up, and skipped-item states. | No automatic retries, as in `collect`: the first network, HTTP, or JSON failure stops the run with exit 1, and rerunning the same command resumes from saved items. | CONSTRAIN |
| Snapshots multiply per story. | When Stan or a later topic requests an archived story again, a fresh download would add another version and a choice of which one to cite. | One archive per root ID; a `complete` archive is reused with zero requests. | CONSTRAIN |
| Export formats multiply. | When each consumer wants its own layout, each format adds a renderer that must stay consistent with SQLite. | One JSON file per complete story, rebuilt from SQLite. | CONSTRAIN |
| Downloads spread beyond the thread. | When comments link articles or name users, following them adds unrelated fetches and storage. | Only the root, items reachable through `kids`, and a poll root's `parts`; no URL, `user` endpoint, or article fetches. | EXCLUDE |

### Public behavior changes (before / after)

- **Before:** `python3 -m hn_search --db hn.sqlite3 collect` is the only command, and the file holds schema-v1 metadata with no comments.
- **After:** `collect` behaves the same. Stan archives catalog stories by ID and sees one line per story:

```bash
python3 -m hn_search --db hn.sqlite3 archive --export-dir exports 4517440
```

```text
archive root=4517440 status=complete comments=5 unavailable=0 reported_descendants=5 export=exports/4517440.json
```

Rerunning the command sends no request, rebuilds the export from SQLite, and prints the same line with `reused=true`. Requesting `99999999`, which has no `posts` row, prints `error: 99999999 is not in the catalog; archive accepts only catalog stories` and sends no request. Exact flag names belong to Pass 2.

### Archive record and compatibility

Archive data lives in the catalog's `--db` file. `archives` holds one row per root with `status` (`incomplete` or `complete`), `started_at`, and `finished_at`. `archive_items` holds one row per fetched ID with its root, the API's JSON object unchanged (or `null`), and `retrieved_at`. Exports use this saved root, not the `posts` row that `collect` may later refresh.

Only a `complete` story gets a JSON export. It nests `replies` in `kids` order, adds each item's `hn_url`, and reports the status, observation interval, saved and unavailable counts, and HN's reported `descendants` without treating a mismatch as failure. A poll export lists options in `parts` order with text and vote `score`; option `126810` of poll `126809` reads "Users would create too many, and new arrivals would think News.YC was a poll site." with 73 votes.

The first `archive` run adds both tables and moves `user_version` from 1 to 2 in one transaction. Rolling back to `64703b5` keeps `collect` working on that file: its `open_catalog()` creates only missing v1 tables and never overwrites a non-zero `user_version`, as `test_existing_nonzero_schema_version_is_never_overwritten` checks; the archive tables stay unused. `archive` and `collect` share one file, so Stan runs them one at a time, as `collect` already requires.

### Download algorithm

`archive_story()` downloads one catalog story; the `archive` command adds steps 1 and 8 around it, and the topic pipeline calls it directly.

1. **Check the catalog.** `main()` opens the `--db` file with `open_catalog()`, and `archive` looks up every requested ID in `posts`. If any ID has no row, `archive` prints the error for each such ID and stops before sending a request.
2. **Reuse or start.** `archive_story()` reads the root's `archives` row and returns at once, with zero requests, when it is `complete`. Otherwise it commits a new `incomplete` row with `started_at`, or keeps an existing `incomplete` row and its original `started_at`.
3. **Rebuild pending from SQLite.** `archive_story()` starts pending as `[root_id]` while the root has no `archive_items` row. After that, pending holds every ID listed in a saved item's `kids`, or in a saved poll root's `parts`, that has no row yet, so a rerun starts where the last commit stopped.
4. **Fetch one item.** `archive_story()` takes the next pending ID, skips it if it is already saved, and sends one `GET https://hacker-news.firebaseio.com/v0/item/<id>.json`. A network, HTTP, or JSON failure raises at once, with no retry.
5. **Save it.** `archive_story()` stores the response unchanged (a JSON object, or `null` for an unavailable ID) with `root_id` and `retrieved_at`, and commits it before the next request.
6. **Queue its children.** `archive_story()` appends a saved object's `kids` to pending in order, plus the poll root's `parts`; deleted and dead items still contribute their `kids`. Steps 4–6 repeat until pending is empty.
7. **Mark complete.** `archive_story()` commits `status = 'complete'` and `finished_at` in one transaction.
8. **Export and print.** `archive` writes `<export-dir>/<root_id>.json` from SQLite and prints the story's line, adding `reused=true` when step 2 returned early. `comments` counts saved reply objects, `unavailable` counts `null` responses, and `reported_descendants` is the saved root's `descendants`.

```text
archive(ids, export_dir):                                # CLI command
    missing = [id for id in ids if id not in posts]      # step 1
    if missing: print the error for each missing ID; stop
    for root_id in ids:                                  # command-line order
        result = archive_story(root_id)                  # a raise exits 1
        write export_dir/<root_id>.json from SQLite      # step 8
        print the summary line, plus reused=true if result == reused

archive_story(root_id):
    row = archives[root_id]                              # step 2
    if row and row.status == "complete": return reused
    if not row: commit archives[root_id] = {status: "incomplete", started_at: now}
    if root_id not in archive_items:                     # step 3
        pending = [root_id]
    else:
        pending = [id for id in kids of saved items + parts of a saved poll root
                   if id not in archive_items]
    while pending:                                       # steps 4-6
        id = pending.pop_front()
        if id in archive_items: continue
        item = GET https://hacker-news.firebaseio.com/v0/item/<id>.json   # object or null; raises
        commit archive_items[id] = {root: root_id, item: item, retrieved_at: now}
        if item is not null:
            pending.extend(item.kids)
            if id == root_id and item.type == "poll": pending.extend(item.parts)
    commit archives[root_id] = {status: "complete", finished_at: now}    # step 7
    return downloaded
```

For `4517440`, pending starts as `[4517440]`. The root lists `4517521` and `4520037`, `4517521` lists `4517587` and `4517797`, and `4517797` lists `4517878`, so pending empties after six requests: the root and its five replies. If the request for `4517797` times out, `archive` exits 1 with four items saved, the story still `incomplete`, and no export; the rerun rebuilds pending as `[4517797]` and finishes in two requests.

Poll `126809`'s first response queues its 25 `kids` and three `parts`, `126810` through `126812`. The dead comment `38311526` is saved with `dead: true` and its `[flagged]` text, and its four replies are still fetched; the deleted comment `45544678` is saved exactly as HN returns it, with no author or text.

### Topic pipeline handoff

The topic pipeline calls `archive_story()` for each matched catalog ID after keyword confirmation; a `complete` story costs no request. `archive_story()` raises on the first failed request, and the pipeline's own design decides whether to stop or continue with other stories. The archive adds no AI client, model setting, or relevance state.

## Rejected design alternatives

| Alternative | Why rejected |
|---|---|
| The downloader fetches each story's nested tree from Algolia's `items` endpoint in one request. | Algolia [returns 404](https://hn.algolia.com/api/v1/items/38311526) for the flagged comment `38311526` and for the deleted comment `45544678`, and its nodes carry no dead or deleted fields, so the archive could not show that missing content honestly. |
| The downloader reads comments from ClickHouse `hackernews_history` with one `id IN (...)` query per reply depth. | Pass 0 names the official HN item API as the source. The mirror stores the same `kids`, `dead`, and `deleted` fields and would replace one request per item with one query per depth, but it serves its last ingested version and carries the omissions the catalog accepted only for metadata. |
| The downloader keeps several item requests in flight. | Parallel requests would shorten long downloads but add thread coordination and out-of-order commits to the resume logic. |

-----------------------------------

# Legend (do not delete)

Scope growth labels mean:

- **INCLUDE** accepts the resulting scope;
- **CONSTRAIN** limits the behavior that causes it;
- **EXCLUDE** leaves the broader work outside this proposal.

Each label is valid only when its row also names the repeatable growth
mechanism and a finite, observable cap.
