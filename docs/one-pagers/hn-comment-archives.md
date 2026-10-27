# HN on-demand comment archives

## Pass 0: Problem or opportunity framing

### Who is the user, what do we know about their behavior, and how correct does the result need to be?

- **User:** Stan, researching what HN thinks about a topic.
- **Their behavior:** Stan confirms search keywords and expects every matching catalog story to be downloaded locally before AI decides whether its discussion is relevant.
- **Edge-case tolerance:** Save all obtainable comments with their reply context, show missing content and incomplete downloads honestly, and resume interrupted work without discarding saved items.

### What is the prevailing user problem or opportunity?

- **Problem or opportunity:** Stan has a local catalog of thread metadata but cannot inspect or analyze the discussions without downloading their comments.

### What is the proposed solution, and why is it right for the user?

- **Solution:** Add on-demand archives of selected HN roots and their obtainable comment trees, preserving original content, item IDs, reply relationships, source links, retrieval times, and completion state in local SQLite storage with reusable JSON and Markdown exports.
- **Why it fits the user:** Stan downloads each selected discussion once and can reuse the same evidence for classification, deep analysis, and future questions.

For “buying versus renting,” the companion [topic pipeline](https://github.com/stanislavkozlovski/hn-search/blob/design/hn-topic-pipeline/docs/one-pagers/hn-topic-pipeline.md) supplies **every deterministic metadata match** to this archive before classification; an already saved snapshot satisfies the download step without another fetch.
The archive owns source evidence and download progress; the topic pipeline owns keyword confirmation, AI decisions, relevant-story folders, and reports.
The archive preserves the root post and comment authors within their thread context, without building cross-thread commenter profiles or fetching linked article bodies.
Automatic refresh stays outside this design, as [previously agreed](hn-topic-research.md#agent-edge-case-scan) and [reconfirmed](https://github.com/stanislavkozlovski/hn-search/pull/5#discussion_r4375376461) because there is no need for the complexity: once a thread older than 30 days is downloaded, it stays there.

### How would you describe the end-to-end user experience?

- **End-to-end user experience:** Stan requests a set of catalog stories directly or through the topic pipeline, sees each download complete or remain incomplete, and receives reusable local comment trees and exports with links back to the original posts and replies.

### What existing data, behavior, or integrations must keep working?

- **Legacy data:** Preserve schema-v1 `posts`, the historical `collection_progress` checkpoint, and all previously collected metadata while adding archive storage.
- **Legacy behavior:** Keep `python3 -m hn_search --db hn.sqlite3 collect`, its explicit `--db` requirement, and its five-comment admission, historical resume, five-day refresh, and retained snapshots unchanged.
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

- `archive` downloads requested catalog stories and their reply trees from the official HN item API into the selected SQLite catalog and writes one JSON file and one Markdown file per complete story to the selected export directory.
- Each fetched item is saved unchanged with its retrieval time; `kids` order defines the reply tree, and deleted, dead, and unavailable items stay visible as such.
- A story stays `incomplete` until nothing is pending, then becomes `complete`; reruns resume incomplete stories without refetching saved items and reuse complete ones with zero requests.
- A poll also saves each option's text and vote count, as Stan [decided](https://github.com/stanislavkozlovski/hn-search/pull/5#discussion_r4375390350).
- The topic pipeline downloads its matches through the same per-story function and reads the same records.

### Out-of-scope non-goals

- Refreshing or re-downloading a saved story at any age, as Stan [reconfirmed](https://github.com/stanislavkozlovski/hn-search/pull/5#discussion_r4375376461). HN [closes threads to new comments after two weeks](https://news.ycombinator.com/newsfaq.html), so a thread older than 30 days cannot gain replies after its download; a story archived within its first two weeks keeps only the replies present at download time.
- Rechecking parents for replies added during a download, [ignored](https://github.com/stanislavkozlovski/hn-search/pull/5#discussion_r4375384280) because the archive targets historical threads; each parent keeps the `kids` list from its own fetch.
- Archiving IDs absent from `posts`, [ignored](https://github.com/stanislavkozlovski/hn-search/pull/5#discussion_r4375395034) in favor of a visible error.
- Linked article bodies, user profiles, HTML exports, AI calls, and any change to `collect`.

### Potential scope growth

| Risk | Growth mechanism — when it happens in practice | Explicit cap | Decision |
|---|---|---|---|
| Item requests multiply with matched comments. | When the topic pipeline archives every keyword match, each reported comment adds one HN request. On 2026-10-26, a case-insensitive title probe for the four buying-versus-renting keywords matched 318 eligible stories with 24,538 reported comments, and the largest eligible story, `42057647`, reports 9,274. | At most eight active roots and eight item requests in flight, with one request per root and one SQLite writer; no parallel requests within a root, sampling, or per-story item limit. | CONSTRAIN |
| Failure states multiply with request count. | When one of roughly 25,000 requests times out, automatic retries would add backoff, give-up, and skipped-item states. | No automatic retries: the first network, HTTP, or JSON failure stops dispatching requests; already-running successes commit before exit 1, and a rerun resumes from saved items. | CONSTRAIN |
| Snapshots multiply per story. | When Stan or a later topic requests an archived story again, a fresh download would add another version and a choice of which one to cite. | One archive per root ID; a `complete` archive is reused with zero requests. | CONSTRAIN |
| Export formats multiply. | When each consumer wants its own layout, each format adds a renderer that must stay consistent with SQLite. | Exactly two fixed formats per complete story: one JSON file and one Markdown file, both rebuilt from SQLite. | CONSTRAIN |
| Downloads spread beyond the thread. | When comments link articles or name users, following them adds unrelated fetches and storage. | Only the root, items reachable through `kids`, and a poll root's `parts`; no URL, `user` endpoint, or article fetches. | EXCLUDE |

### Public behavior changes (before / after)

- **Before:** `python3 -m hn_search --db hn.sqlite3 collect` is the only command, and the file holds schema-v1 metadata with no comments.
- **After:** `collect` behaves the same and still requires explicit `--db`, as [PR #6 preserves](https://github.com/stanislavkozlovski/hn-search/blob/c3963bb752d278052beacd2a4b9dd654cc57fb85/docs/one-pagers/hn-topic-pipeline.md#L131-L134). `archive` defaults to `hn.sqlite3` for the catalog and `exports/` for exports, both relative to the current working directory; explicit `--db` and `--export-dir` override the corresponding paths. Stan archives catalog stories by ID and sees one line per story:

```bash
python3 -m hn_search archive 4517440
```

```text
archive root=4517440 status=complete comments=5 unavailable=0 reported_descendants=5 json=exports/4517440.json markdown=exports/4517440.md
```

The equivalent invocation with both paths explicit is:

```bash
python3 -m hn_search --db hn.sqlite3 archive --export-dir exports 4517440
```

With several IDs, such as `python3 -m hn_search archive 4517440 126809`, up to eight roots download concurrently; story lines can appear in completion order. A single root still sends one request at a time.

Rerunning the command sends no request, rebuilds both exports from SQLite, and prints the same line with `reused=true`. Requesting `99999999`, which has no `posts` row, prints `error: 99999999 is not in the catalog; archive accepts only catalog stories` and sends no request.

**Deferred to Pass 2:** Implement the parser changes in `hn_search/__main__.py`; the archive defaults and override flags above are settled.

### Archive record and compatibility

Archive data lives in the selected catalog: `hn.sqlite3` in the current working directory unless `--db` supplies another path. Exports go to `exports/` in the current working directory unless `--export-dir` supplies another path. `archives` holds one row per root with `status` (`incomplete` or `complete`), `started_at`, and `finished_at`. `archive_items` holds one row per fetched ID with its root, the API's JSON object unchanged (or `null`), and `retrieved_at`. Exports use this saved root, not the `posts` row that `collect` may later refresh.

Only a `complete` story gets exports. The JSON nests `replies` in `kids` order, adds each item's `hn_url`, and reports the status, observation interval, saved and unavailable counts, and HN's reported `descendants` without treating a mismatch as failure. Both exports list a poll's options in `parts` order with text and vote `score`; option `126810` of poll `126809` reads "Users would create too many, and new arrivals would think News.YC was a poll site." with 73 votes.

`<root>.md` follows [the topic pipeline's `thread.md` layout](https://github.com/stanislavkozlovski/hn-search/blob/c3963bb752d278052beacd2a4b9dd654cc57fb85/docs/one-pagers/hn-topic-pipeline.md#L231-L246): it opens with the title linked to HN, article link when present, author, posting date, reported comment count, and archive date, followed by the root text when present. Every saved comment follows as a nested bullet in `kids` order with its author, timestamp linked to HN, and Obsidian block ID such as `^c4517521`; deleted, flagged, and unavailable items keep their place with visible markers. The renderer handles paragraphs, italics, code, links, and HTML entities and escapes source text that would otherwise become Obsidian syntax; SQLite and JSON retain the original HTML.

The first `archive` run adds both tables and moves `user_version` from 1 to 2 in one transaction. Rolling back to `64703b5` keeps `collect` working on that file: its `open_catalog()` creates only missing v1 tables and never overwrites a non-zero `user_version`, as `test_existing_nonzero_schema_version_is_never_overwritten` checks; the archive tables stay unused. `archive` and `collect` share one file, so Stan runs them one at a time, as `collect` already requires.

### Download algorithm

`archive` admits roots in input order and runs up to eight concurrently, with at most one HN request per root. Python's [`ThreadPoolExecutor`](https://docs.python.org/3.12/library/concurrent.futures.html#threadpoolexecutor-example) runs only the HTTP fetches and JSON parsing. The calling thread keeps the connection opened by [`open_catalog()`](https://github.com/stanislavkozlovski/hn-search/blob/2b8acfde5e4f56645f1d7936d0a9043842a299d8/hn_search/catalog.py#L6-L7), commits each response, and schedules that root's next request after the commit; Python's [SQLite connection defaults](https://docs.python.org/3.12/library/sqlite3.html#sqlite3.connect) require using the connection in its creating thread.

Saved items remain the checkpoint: pending IDs are reconstructed from SQLite on resume, so no separate queue has to survive a crash.

**Request pacing:** Checked on 2026-10-26, the [official Firebase HN API documentation](https://github.com/HackerNews/API/blob/6b8d4500a0c4c4a880a678928cc6d5e20e764015/README.md#uri-and-versioning) states that there is currently no rate limit and supplies no numeric requests-per-second quota. `archive` adds no fixed sleep or automatic retry; the eight-request cap bounds concurrency. An HTTP failure, including HTTP 429 if encountered, follows step 5.

1. **Check the catalog.** Drop repeated IDs, keeping their order. If any ID has no `posts` row, print one error per missing ID and stop before any request.
2. **Admit up to eight roots.** Take roots in input order as slots become free. A root whose archive is `complete` sends no request and goes straight to step 6. Do not submit the entire input list to the thread pool.
3. **Open or resume.** Create an admitted root's `archives` row as `incomplete` with `started_at`, or keep its existing incomplete row. Pending IDs are the root if it is unsaved, plus every ID listed in a saved item's `kids`, or in a saved poll root's `parts`, that has no `archive_items` row. Keep a deduplicated pending queue per active root.
4. **Fetch and commit one item per root.** For each idle root, take its oldest pending ID and request `https://hacker-news.firebaseio.com/v0/item/<id>.json`. Other roots' requests may overlap. Each worker returns the response and its retrieval time; the calling thread commits that item before scheduling another request for the same root:
   - A JSON object is saved unchanged; its unsaved `kids` join that root's pending queue in display order, and so does a poll root's `parts`.
   - A deleted item such as `45544678` arrives without author or text, and a flagged dead item such as `38311526` arrives with the text `[flagged]`; both are saved as returned, and their `kids` are still followed.
   - `null` is saved as unavailable and has nothing to follow; a story whose root is `null` completes with no comments and `unavailable=1`.
5. **Stop dispatching on failure, then save successes.** On the first observed network, HTTP, or invalid-JSON failure, leave that ID pending and stop admitting roots or dispatching requests. Cancel submitted fetches that have not started; wait for the already-running requests to return or time out and commit every successful response, including its child lists, without fetching newly discovered children. As successes commit, finish roots that have no pending IDs through step 6; after draining, print an `incomplete` line for each remaining active root and exit 1. Roots not yet admitted stay untouched. A rerun fetches only IDs still missing from SQLite. Previously committed items survive an interrupt; a forced stop can lose responses that have not committed.
6. **Finish each root independently.** Once a root has neither pending IDs nor a request in flight, mark it `complete` with `finished_at`. For every complete story, including reused ones and roots completed during shutdown, rebuild `<export-dir>/<root>.json` and `<export-dir>/<root>.md` from SQLite, each through its own temporary file and rename, then print the story's line after both writes succeed. If either write fails, the SQLite archive stays complete; stop dispatching, drain successful fetches already in flight, and raise the error. Rerunning rebuilds both exports without HN requests.

The pseudocode shows the calling thread's scheduler; only `fetch_one()` runs in a pool thread. Request timeouts and the concrete helper names are deferred to Pass 2.

```python
def archive(conn, requested_ids, export_dir):
    roots = list(dict.fromkeys(requested_ids))              # 1. keep order, drop repeats
    missing = [r for r in roots if not in_posts(conn, r)]
    if missing:
        fail_before_any_request(missing)

    waiting = deque(roots)
    active = {}                                             # root -> deque of pending IDs
    in_flight = {}                                          # future -> (root, item ID)
    first_error = None

    def export_and_print(root, reused=False):
        nonlocal first_error
        try:
            write_export_atomically(conn, root, export_dir / f"{root}.json")
            write_markdown_export_atomically(conn, root, export_dir / f"{root}.md")
            print_line(conn, root, reused=reused)
        except OSError as error:
            first_error = first_error or error              # keep draining fetched successes

    with ThreadPoolExecutor(max_workers=8) as pool:
        while waiting or active:
            if first_error is None:
                while waiting and len(active) < 8 and first_error is None:
                    root = waiting.popleft()                # 2. admit in input order
                    if archive_status(conn, root) == "complete":
                        export_and_print(root, reused=True) # zero requests
                    else:
                        start_or_resume(conn, root, started_at=now())
                        active[root] = deque(pending_ids(conn, root))  # 3.

            busy = {root for root, item_id in in_flight.values()}
            for root in list(active):
                if not active[root] and root not in busy:
                    mark_complete(conn, root, finished_at=now())  # 6. also during drain
                    export_and_print(root)
                    del active[root]

            if first_error is None:
                for root, pending in active.items():
                    if root not in busy and pending:
                        item_id = pending.popleft()
                        future = pool.submit(fetch_one, item_id)  # 4. HTTP only
                        in_flight[future] = (root, item_id)

            if first_error is not None:
                for future in list(in_flight):
                    if future.cancel():                     # cancel fetches not yet started
                        root, item_id = in_flight.pop(future)
                        active[root].appendleft(item_id)

            if not in_flight:
                if first_error is not None:
                    break
                continue                                    # admit the next roots

            done, _ = wait(in_flight, return_when=FIRST_COMPLETED)
            for future in done:                             # inspect the batch before dispatching again
                root, item_id = in_flight.pop(future)
                try:
                    item, retrieved_at = future.result()
                except Exception as error:                  # 5. fetch or JSON failure
                    first_error = first_error or error
                    active[root].appendleft(item_id)        # failed ID stays pending
                else:
                    save_item(conn, root, item_id, item, retrieved_at=retrieved_at)  # commit
                    for child in children(root, item_id, item):
                        if not item_saved(conn, root, child) and child not in active[root]:
                            active[root].append(child)      # saved lists survive shutdown

    if first_error is not None:
        for root in active:
            print_line(conn, root)                          # status=incomplete, after draining
        raise first_error                                   # CLI exits 1


def archive_story(conn, root, export_dir):
    archive(conn, [root], export_dir)                        # same scheduler, one root


def fetch_one(item_id):
    item = fetch_item(item_id)                              # dict, or None for HN's null
    return item, now()                                      # retrieval time, before writer delay


def children(root, item_id, item):
    if item is None:
        return []                                           # unavailable: nothing to follow
    ids = list(item.get("kids", []))                        # replies in display order
    if item_id == root and item.get("type") == "poll":
        ids += item.get("parts", [])                        # poll options
    return ids


def pending_ids(conn, root):
    saved = saved_items(conn, root)                         # {id: dict or None}
    listed = [root] + [c for i, item in saved.items() for c in children(root, i, item)]
    return [i for i in dict.fromkeys(listed) if i not in saved]
```

For story `4517440`, HN returned this tree on 2026-10-26:

```text
4517440  story  "Trulia Rent vs. Buy Map Visualizes How Mortgage Rates, Taxes Timing Change Costs"  descendants=5
├── 4517521  Daisy
│   ├── 4517587  DamnYuppie
│   └── 4517797  pc86
│       └── 4517878  malyk
└── 4520037  Evbn
```

A first run sends six requests for this root, in order: `4517440`, `4517521`, `4520037`, `4517587`, `4517797`, and `4517878`, then completes with five comments. Requests for other roots can overlap. If `4517797` times out, the scheduler stops dispatching and saves the other roots' successful in-flight responses before printing `archive root=4517440 status=incomplete comments=3 pending=1` and exiting 1. The rerun recomputes pending as `[4517797]` from the saved `kids` lists, sends two requests for this root, and completes with both exports; later requests for this root send none.

If another root's last request succeeds during that shutdown, its archive completes and gets both exports. If its response instead lists an unsaved child, the response commits but the child remains pending for the rerun; no further request is dispatched after the failure is observed.

### Topic pipeline handoff

The topic pipeline calls `archive_story(conn, root, export_dir)` for each matched catalog ID after keyword confirmation; a `complete` story costs no request. `archive_story()` wraps the same scheduler for one root and raises on a failed request, preserving the pipeline's own stop-or-continue policy. Batch callers use `archive(conn, roots, export_dir)` to share the eight-root cap and the single writer; they do not share `conn` between concurrent `archive_story()` calls. Defaults apply only to the `archive` CLI; both functions take the connection and export directory explicitly. The Markdown export uses the pipeline's `thread.md` layout and `^c<ID>` anchors; the pipeline continues to own story-folder names and links from analyses and reports. The archive adds no AI client, model setting, or relevance state.

## Rejected design alternatives

| Alternative | Why rejected |
|---|---|
| The downloader fetches each story's nested tree from Algolia's `items` endpoint in one request. | Algolia [returns 404](https://hn.algolia.com/api/v1/items/38311526) for the flagged comment `38311526` and for the deleted comment `45544678`, and its nodes carry no dead or deleted fields, so the archive could not show that missing content honestly. |
| The downloader reads comments from ClickHouse `hackernews_history` with one `id IN (...)` query per reply depth. | Pass 0 names the official HN item API as the source. The mirror stores the same `kids`, `dead`, and `deleted` fields and would replace one request per item with one query per depth, but it serves its last ingested version and carries the omissions the catalog accepted only for metadata. |
| The downloader launches every root at once or fetches several replies within one root concurrently. | Eight active roots bound the requests and responses awaiting a commit; one request per root keeps that root's checkpoint sequential while other roots make progress. |

-----------------------------------

# Legend (do not delete)

Scope growth labels mean:

- **INCLUDE** accepts the resulting scope;
- **CONSTRAIN** limits the behavior that causes it;
- **EXCLUDE** leaves the broader work outside this proposal.

Each label is valid only when its row also names the repeatable growth
mechanism and a finite, observable cap.
