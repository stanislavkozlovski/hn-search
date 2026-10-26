# HN topic search and cited research reports

## Pass 0: Problem or opportunity framing

### Who is the user, what do we know about their behavior, and how correct does the result need to be?

- **User:** Stan, asking “What does HN think about X?”, initially buying versus renting a home.
- **Their behavior:** Stan asks a question in an interactive terminal, answers the AI's proposed keywords in plain language until he approves a list, and expects local search, downloads, classification, relevant-story folders, deep analysis, and a cited report to follow.
- **Edge-case tolerance:** Prioritize relevant-thread recall over avoiding false positives, keep uncertain decisions visible, and ground arguments and quotations in identifiable archived comments rather than unsupported claims about all of HN.

### What is the prevailing user problem or opportunity?

- **Problem or opportunity:** Stan can collect HN metadata but cannot turn a human question into saved relevant discussions and a deep report of what their commenters actually argue.

### What is the proposed solution, and why is it right for the user?

- **Solution:** Build an interactive CLI or TUI in which Stan sets each AI stage's model and effort and refines AI-generated keywords through plain-language conversations before deterministic catalog matching; it archives every matching story before AI classification, saves reusable descriptions and question-specific judgments, and analyzes relevant-story folders, by default with a frontier model at maximum supported effort, to produce a cited report.
- **Why it fits the user:** Stan shapes the search terms by talking to the AI and approves them once, receives the full research workflow, and reuses archived discussions and applicable AI work for future questions.

The approved order is **default model settings → Stan's plain-language setting replies, each read by AI as a revision or an approval → question → AI keyword proposal → Stan's plain-language keyword replies, read the same way → deterministic database search on the approved list → archive every matched story → classify each archived discussion → save each relevant story in its own folder → deep thread analysis → cross-thread report**.
A saved archive or matching AI result can satisfy its stage, but title-only AI rejection must not prevent a keyword-matched story from being archived.
The [archive design](https://github.com/stanislavkozlovski/hn-search/blob/design/hn-comment-archives/docs/one-pagers/hn-comment-archives.md) supplies reusable source snapshots and download status.
This design owns the terminal interaction, AI stages, cache, relevant-story folders, per-thread analyses, and final report.

For “buying versus renting,” the AI might propose `buy vs rent`, `home ownership`, `mortgage`, and `renting`.
Stan replies “these are good, but add landlord, property tax, and down payment, and more,” and the CLI shows ten terms: the original four, Stan's three, and three the AI added, such as `closing costs`.
Every reply, approval included, goes to the AI through `CodexClient.run_structured`, which returns either a revised list for another round or an approval.
Approval searches exactly the list on screen, so a reply that edits and approves at once, such as “add rent control and go,” shows the revised list first.

The report should distinguish arguments, counterarguments, assumptions, financial or geographic conditions, lived experiences, and unresolved disagreements, with links to supporting comments and an index of every relevant thread.
Interpret comments within their thread and reply ancestry, without cross-thread commenter profiles or claims that anecdotes establish population-wide consensus.

The AI brief calls for separate versioned prompts for **model-setting revisions from Stan's replies**, **keyword proposals and revisions from Stan's replies**, **question-independent discussion descriptions/tags**, **question-specific relevance with reasons and comment IDs**, **deep per-thread arguments**, and **a cross-thread synthesis with source citations**.
Later passes must specify prompt contracts, output shapes, and a worked buying-versus-renting example.

### How would you describe the end-to-end user experience?

- **End-to-end user experience:** Stan keeps or changes the model settings in plain language, asks whether buying or renting is better, tells the AI how to adjust its suggested keywords until he approves them, watches matching discussions download and receive classifications, then opens relevant-story folders and a deep report linking its claims to the original threads and comments.

### What existing data, behavior, or integrations must keep working?

- **Legacy data:** Preserve schema-v1 metadata and collection checkpoints plus the companion archive's saved discussions, and retain reusable descriptions separately from topic-specific judgments in SQLite.
- **Legacy behavior:** Keep `collect` and the catalog's five-comment admission unchanged, reuse saved comment snapshots without automatic refresh, and accept the previously agreed limits of metadata-only discovery.
- **Existing integrations:** Use Python `stan_ai_client` from installed `stan-ai-client==0.1.19`, explicitly through `CodexClient`, `CodexRunOptions`, and `StructuredSchema`, alongside the companion archive and existing SQLite catalog.
- **Compatibility tolerance:** Additive database changes are acceptable without discarding collected data, while changed source content, topic meaning, prompts, output schemas, models, or reasoning settings must prevent stale AI results being presented as current.

Grounding on 2026-10-26 checked the installed [v0.1.19 client](https://github.com/stanislavkozlovski/stan_ai_client/tree/e423a5548292e51c5ffab1b8420a67ae38d7f4a2) and found that it runs local `codex exec` with the CLI's authentication and supports synchronous calls, explicit model/effort/timeout settings, locally schema-validated JSON, session metadata, typed failures, optional rate-limit handling, and usage normalization.
The application owns caching, batching, scheduling, and progress; the client has no native streaming API.
For the settings and keyword conversations, the client can [resume a Codex session](https://github.com/stanislavkozlovski/stan_ai_client/blob/e423a5548292e51c5ffab1b8420a67ae38d7f4a2/src/stan_ai_client/codex.py#L514-L522) across replies through `CodexRunOptions.session_id`, but `run_structured` [reports that session's `thread_id`](https://github.com/stanislavkozlovski/stan_ai_client/blob/e423a5548292e51c5ffab1b8420a67ae38d7f4a2/src/stan_ai_client/codex.py#L375-L383) only when called with `capture_usage=True`.
**Deferred — conversation state:** later passes choose between resuming that session and resending the short exchange each round.
JSON validation does not verify truth or citations; HN text remains source evidence, not executable instructions.
Later passes must explicitly constrain the client’s permissive default execution settings.

**Proposed default model settings for review:** When a run starts, the CLI shows these four defaults, and Stan keeps or changes them in plain language, as he does for keywords.

| AI work | Model | Reasoning effort |
|---|---|---|
| Keyword proposals and revisions | `gpt-6-luna` | `medium` |
| Reusable thread descriptions and topic relevance | `gpt-6-luna` | `high` |
| Deep per-thread analysis | `gpt-6-astra` | `max` |
| Final report synthesis | `gpt-6-astra` | `max` |

Stan replies “use Astra at high effort for classification,” and the CLI shows the table with the “Reusable thread descriptions and topic relevance” row changed to `gpt-6-astra` at `high`; “looks good” then approves it.
As in the keyword conversation, every reply, approval included, goes through `CodexClient.run_structured`, which returns either a revised table or an approval, and approval uses exactly the table on screen, so “use Astra for classification and go” shows the revised table first.
**Deferred — settings-reply model:** later passes choose which model and effort read these replies, which run before Stan approves any setting; left unset, `CodexClient` [falls back to `gpt-6.1-sol` at `max`](https://github.com/stanislavkozlovski/stan_ai_client/blob/e423a5548292e51c5ffab1b8420a67ae38d7f4a2/src/stan_ai_client/codex.py#L152-L153).

The local `/home/ops/.codex/models_cache.json` checked that day advertises Astra as a frontier model; recheck available frontier choices at implementation, record the actual model used, and expose any substitution.
The [installed client declares](https://github.com/stanislavkozlovski/stan_ai_client/blob/e423a5548292e51c5ffab1b8420a67ae38d7f4a2/src/stan_ai_client/types.py#L8) `max` as its highest supported reasoning effort; do not assume the underlying CLI's `ultra` option is a supported client contract.

Persist the question and approved keywords, the source snapshot used, prompt text/version, model and effort, structured result, explanation, cited IDs, and completion state so a future search can establish which work is reusable.
A question-independent description can help a differently worded search, but “irrelevant to buying versus renting” must never become “irrelevant to mortgage rates”; reuse a final judgment only when its actual question and other inputs still match.
Albufera's local classifier already records prompt/model/effort and input identity with batch checkpoints; Anecdote Miner's profile/comment/text cache omits some of those inputs and must not be copied unchanged.
Concrete cache keys and migration mechanics belong to the later design passes.

Compatibility grounding checked the catalog, CLI, tests, and existing schema-v1 database against merged commit [`64703b5`](https://github.com/stanislavkozlovski/hn-search/tree/64703b58fedbe19ef8e80612ab1d825e880e2eaf); no legacy AI records exist.
Preserve the companion archive's record contract and the collector's serialized-writer assumption.
The [Telegram feed design](https://github.com/stanislavkozlovski/hn-search/pull/3) is separate and must not supply its different retention, relevance-cache, or eligibility rules to this research pipeline.
This design adds no daily collection schedule, external article fetching, or discovery of topics hidden only in comments beneath otherwise unrelated metadata.

### Agent edge-case scan

| Edge case | What happens if ignored | What handling it adds | User decision |
|---|---|---|---|
| When an archived discussion exceeds the selected model's usable context, the classifier or deep-analysis call cannot inspect the whole discussion at once. | The pipeline stops that story with a visible oversized-input status rather than silently truncating it or claiming full coverage. | The pipeline splits the discussion with reply ancestry, tracks which comments were considered, and combines the partial analyses with explicit bounds agreed in Pass 1. | HANDLE |
| When confirmed keywords match many thousands of stories, the promised download-and-analysis pipeline can require substantial time and AI usage. | The pipeline processes the full matched set without an additional size or spending approval and never silently replaces it with a top-N sample. | The terminal shows the candidate count and estimated work and asks for a separate proceed-or-refine decision before downloading and spending AI usage. | HANDLE |
| When AI marks an archived story uncertain, Stan can see its classification but the story has no settled relevance decision. | The pipeline leaves it in the visible uncertain set outside the relevant-story analysis and names that exclusion in report coverage. | The terminal asks Stan to include or exclude uncertain stories before deep analysis and records those decisions for the report. | IGNORE |
| When a matched story remains incomplete or unavailable after download, the pipeline lacks the complete discussion expected by classification. | The pipeline stops before producing the final report and retains completed work for a later resume. | The pipeline can continue with complete archives and explicitly list the omitted or incomplete stories in report coverage. | HANDLE |
| When individually small [thread analyses](https://github.com/stanislavkozlovski/hn-search/blob/62ee115d5210823fc82e3723d8c8757ab74efeea/docs/one-pagers/hn-topic-pipeline.md#L20-L29) exceed the model’s input limit together, the report writer cannot finish. | Stan receives separate thread analyses without the combined report. | The report writer reads the story folders itself in one read-only Codex session that compacts its context as it goes, while the pipeline still writes the comment links and the index of every relevant thread. | HANDLE |
| When Stan's reply narrows the question itself, such as “focus on Europe,” the AI changes only the keyword list. | The classifier and report keep judging Stan's original question, so the narrower intent reaches only the search terms. | The AI also proposes a revised question for Stan to approve with the keywords, and classification and the report use that question. | HANDLE |
| When a run stops partway, such as after a failed AI call or Ctrl-C, the pipeline keeps its finished work but has no way to continue that run. | Stan repeats both conversations in a new run, and the pipeline reuses saved results only if he approves the identical question and settings. | `research` resumes the stopped run from its saved question, keywords, settings, and matched stories, skipping both conversations and all finished work. | IGNORE |
| When one story's AI call fails, such as on a timeout or on output that fails its schema, the pipeline has no result for that story's stage. | The pipeline stops the run with the client's error and keeps every finished result. | The pipeline records the failure, continues with the other stories, and lists the story in report coverage, while failures that hit every call, such as an expired Codex login, still stop the run. | IGNORE |
| When Codex reports a usage limit mid-run, every remaining AI call fails until the limit resets. | The pipeline stops the run like any failed call and prints the reset time when Codex reports one. | The pipeline waits until the reported reset, printing when it will continue, and then retries the same call. | IGNORE |

## Pass 1: High-level design

**Review status:** Stan decided the six original Pass 0 rows: oversized discussions [HANDLE](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4375867878), the proceed-or-refine gate [HANDLE](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4375871767), uncertain stories [IGNORE](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4375873345), failed downloads [HANDLE](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4375879777), analyses too large for one report call [IGNORE](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4375890125), which he later changed to [HANDLE](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4376618684) with a report session that reads the story folders, and question narrowing [HANDLE](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4375892056). He then [requested Pass 1](https://github.com/stanislavkozlovski/hn-search/pull/6#issuecomment-6413090819). He has since decided the three rows this pass added: resuming a stopped run [IGNORE](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4376474218), skipping a failed AI call [IGNORE](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4376478074), and waiting out a Codex usage limit [IGNORE](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4376481256), so every Pass 0 row now has his decision. Command, flag, table, and file names are proposals that Pass 2 finalizes.

## Proposal

### In-scope goals

- `research` runs the approved order in one terminal session and shows live progress: a spinner and clock while an AI reply or the search is pending, then a stage checklist that redraws in place with counts and the call in flight. When output is not a terminal, it prints one line per story at each stage instead.
- Search matches each approved keyword as a whole-word phrase in catalog titles, URLs, and post text.
- After every search, a gate shows the matches, each keyword's three largest matches, and the work ahead; nothing downloads or calls AI until Stan proceeds.
- A keyword reply can also revise the question, and the approved question drives every later stage.
- Downloads go through the [archive design](https://github.com/stanislavkozlovski/hn-search/blob/design/hn-comment-archives/docs/one-pagers/hn-comment-archives.md#topic-pipeline-handoff)'s `archive_story()`; a story that fails to download, or whose root HN returns as `null`, is skipped and listed in coverage.
- Classification saves a reusable description and a verdict on the question: `relevant`, `uncertain`, or `irrelevant`. Only relevant stories get folders and deep analysis.
- A discussion too large for one call is split into parts, analyzed part by part, and combined.
- The synthesis writes the report's cross-thread arguments in one call when every relevant analysis fits the report model's input budget, and otherwise in one read-only Codex session that reads the story folders itself; the pipeline writes the links, thread index, and coverage either way.
- Every AI result is saved with its inputs and reused only when all of them match.

### Out-of-scope non-goals

- Asking Stan about uncertain stories, as he decided.
- Resuming a stopped run, skipping a story whose AI call failed, and waiting for a Codex usage limit to reset, as he decided.
- Boolean, stemmed, fuzzy, or semantic search.
- Parallel AI calls or downloads, and settings remembered between runs.
- Changes to `collect` or `archive`, plus Pass 0's exclusions: archive refresh, a daily schedule, article fetching, comment-only topic discovery, and commenter profiles.

### Potential scope growth

| Risk | Growth mechanism — when it happens in practice | Explicit cap | Decision |
|---|---|---|---|
| AI calls multiply with matched stories. | When Stan approves the four sample keywords, [461 stories match](https://play.clickhouse.com/?user=play&query=SELECT%20count%28%29%20AS%20stories%2C%20sum%28descendants%29%20AS%20comments%2C%20countIf%28match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29buy%5B%5E0-9a-z%5D%2Bvs%5B%5E0-9a-z%5D%2Brent%28%5B%5E0-9a-z%5D%7C%24%29%27%29%29%20AS%20buy_vs_rent%2C%20countIf%28match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29home%5B%5E0-9a-z%5D%2Bownership%28%5B%5E0-9a-z%5D%7C%24%29%27%29%29%20AS%20home_ownership%2C%20countIf%28match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29mortgage%28%5B%5E0-9a-z%5D%7C%24%29%27%29%29%20AS%20mortgage%2C%20countIf%28match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29renting%28%5B%5E0-9a-z%5D%7C%24%29%27%29%29%20AS%20renting%20FROM%20%28SELECT%20lower%28concat%28title%2C%20%27%20%27%2C%20url%2C%20%27%20%27%2C%20text%29%29%20AS%20t%2C%20descendants%20FROM%20hackernews_history%20FINAL%20WHERE%20type%20IN%20%28%27story%27%2C%20%27poll%27%2C%20%27job%27%29%20AND%20parent%20%3D%200%20AND%20deleted%20%3D%200%20AND%20descendants%20%3E%3D%205%29%20WHERE%20match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29%28buy%5B%5E0-9a-z%5D%2Bvs%5B%5E0-9a-z%5D%2Brent%7Chome%5B%5E0-9a-z%5D%2Bownership%7Cmortgage%7Crenting%29%28%5B%5E0-9a-z%5D%7C%24%29%27%29%20FORMAT%20JSON) in the mirror `collect` reads, so classification alone needs 922 calls before any deep analysis, and each relevant story adds an analysis call. | Each story gets at most one description per archive, prompt version, model, and effort, reused across questions, plus one verdict and at most one deep analysis per approved question; each run makes one synthesis call or one folder session; calls run one at a time and only after the gate. | CONSTRAIN |
| Calls multiply with thread size. | When a discussion like `42057647` outgrows one call, each part adds a call per stage, and the part results can outgrow the combining call. | Parts hold whole reply subtrees and cover each comment once; at most one combining call for a split description or analysis, with no second merge level; part results that do not fit one call leave the story `oversized`. | CONSTRAIN |
| Folder reads and compactions multiply with relevant stories. | When a few hundred relevant analyses outgrow one call, the folder session spends a tool call on each file it reads, and each time its context reaches 90% of the window, Codex replaces earlier reads with a summary, so later arguments can rest on summaries of analyses. | One folder session per run, only when the inline input exceeds the budget; it reads only the run folder, cannot write or reach the network, and returns one schema-checked answer whose cited IDs the pipeline checks; a failed or timed-out session stops the run like any other AI call. | CONSTRAIN |
| Saved results multiply with wording and settings. | When Stan rephrases a question or changes a model, effort, or prompt, every matched story gets a new result instead of reusing one. | Reuse requires an exact match of stage, prompt version, model, effort, archive, and, for verdicts and analyses, the approved question text; questions are never matched by similarity, and nothing is deleted automatically. | CONSTRAIN |
| Prompts multiply with stages. | When a stage gains a variant, such as combining part results, it adds a versioned prompt, an output schema, and a reuse key for Pass 2 to specify. | Nine prompts: settings, keywords and question, description, verdict, deep analysis, synthesis, folder synthesis, description combining, and analysis combining. | CONSTRAIN |
| Output files multiply with runs. | When Stan reruns or asks a new question, each run writes another folder tree. | One folder per run, holding `report.md` and one `stories/<id>/` folder per relevant story with `thread.json`, `thread.md`, and `analysis.md`; `thread.md` converts only paragraphs, italics, code, links, and HTML entities; no HTML or PDF. | CONSTRAIN |

### Public behavior changes (before / after)

- **Before:** With the archive design in place, `collect` and `archive` are the only commands; neither needs a package, and nothing searches the catalog or calls AI.
- **After:** `collect` and `archive` behave the same and still need no package. `research` needs `stan-ai-client==0.1.19` and a logged-in `codex` CLI. `research` reads `hn.sqlite3` in the current directory, the path the README already uses, and writes run folders under `research/`; `--db` and `--out` override either. If that catalog file does not exist, `research` exits with `error: no catalog at hn.sqlite3; run collect first or pass --db` instead of creating an empty catalog that matches nothing. `collect` and `archive` still require `--db`, so a bare `collect` still exits 2 instead of starting a full historical sweep wherever it runs. If Stan keeps the defaults and approves the AI's first four keywords, a run starts like this:

```text
$ python3 -m hn_search research
Model settings:
  keywords         gpt-6-luna   medium
  classification   gpt-6-luna   high
  thread analysis  gpt-6-astra  max
  report           gpt-6-astra  max
> looks good
Question?
> Is buying a home better than renting?
Question: Is buying a home better than renting?
Keywords: buy vs rent, home ownership, mortgage, renting
> go
461 stories match (28,281 reported comments): buy vs rent 3 · home ownership 27 · mortgage 265 · renting 176
Top matches by reported comments:
  buy vs rent     48595251    19  Renting vs. Buying – A case study for Bangalore
                   3408816    15  Buy (and rent) vs buy: a hacker's view on housing
                   1781264     8  Ask HN: When to buy vs rent servers?
  home ownership  40490610  1245  Priced out of home ownership
                  48281611   866  The real cost of owning a home
                  26871164   482  Home ownership is the West’s biggest economic-policy mistake
  mortgage        31279809   740  Homes in 97% of U.S. cities are overvalued, Moody's says
                  31189088   493  Rocket Mortgage to trim 8% of workforce as home-loan market shrinks
                  46673809   433  Show HN: I quit coding years ago. AI brought me back
  renting         29696653   500  The absurdity of renting a car will no longer be tolerated
                  30132560   496  Ask HN: At a peak of my dev career, I hate my life
                  16899541   478  Renting is Throwing Money Away, Right? (2015)
Next: download 461 stories, then 922 classification calls (0 reused), one analysis per relevant story, and one report.
Proceed, or say how to change the keywords?
> proceed
relevant 40490610 "Priced out of home ownership"
✓ search    461 stories
✓ download  461/461
⠼ classify  212/461 · 31 relevant · 6 uncertain · 175 irrelevant
            verdict 31279809 · gpt-6-luna high · 41s
· analyze
· report
```

The last six lines redraw in place; their tallies here are illustrative. When the run finishes, the checklist stays on screen with every row checked, and `report research/run-1/report.md` prints below it.

```text
research/run-1/
├── report.md            # synthesis, thread index, coverage, with Obsidian links
└── stories/
    └── 40490610/
        ├── thread.md    # story link and every saved comment, in Markdown
        ├── thread.json  # the archive's JSON export
        └── analysis.md  # story link, description, verdict reasons, deep analysis
```

If an AI call fails, `research` prints the story and stage, then exits 1 with the client's typed error, such as `CodexTimeoutError` or `CodexRateLimitError`; Ctrl-C also stops it. A Codex usage limit stops the run the same way, without waiting for the reset; the printed error is Codex's own message, which [names the reset time](https://github.com/openai/codex/blob/970111f6cb62cc02fe36a82ea7d71b37a2889c97/codex-rs/protocol/src/error.rs#L836-L852), such as “try again at 3:15 PM,” when Codex reports one. Every finished result stays saved, but no command resumes the stopped run: Stan starts a new run and repeats both conversations, and that run reuses saved descriptions when the settings match and saved verdicts and analyses only when he also approves the identical question.

### Conversations and the gate

Each round of the settings and keyword conversations resends the short exchange so far to `CodexClient.run_structured`, so no round depends on a stored Codex session; this settles Pass 0's deferred conversation state. Settings replies always go to `gpt-6-luna` at `medium`, the keyword row's default, which settles the deferred settings-reply model.

Each keyword round returns a question and a list, and the CLI shows both. If Stan replies “focus on Europe,” the question becomes “Is buying a home better than renting in Europe?” Classification does the narrowing: every matched story's verdict is judged against that question, so [a thread on overvalued homes in U.S. cities](https://news.ycombinator.com/item?id=31279809) should come back `irrelevant` unless its comments discuss Europe, while the BBC's [`40490610`](https://news.ycombinator.com/item?id=40490610) “Priced out of home ownership” stays `relevant`. Deep analysis and the report then weigh the European arguments within each relevant thread, such as [a reply there](https://news.ycombinator.com/item?id=40494752) comparing dwellings per person in EU countries. A keyword can only widen the search, so for a narrowed question the keyword prompt adds one only when it expects the keyword to find relevant stories the list misses without many unrelated ones: [`rent control` matches 31 eligible stories and `social housing` 7, none of which the four sample keywords match, while `europe` matches 3,777](https://play.clickhouse.com/?user=play&query=SELECT%20countIf%28match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29europe%28%5B%5E0-9a-z%5D%7C%24%29%27%29%29%20AS%20europe%2C%20countIf%28match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29rent%5B%5E0-9a-z%5D%2Bcontrol%28%5B%5E0-9a-z%5D%7C%24%29%27%29%29%20AS%20rent_control%2C%20countIf%28match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29rent%5B%5E0-9a-z%5D%2Bcontrol%28%5B%5E0-9a-z%5D%7C%24%29%27%29%20AND%20NOT%20s%29%20AS%20rent_control_new%2C%20countIf%28match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29social%5B%5E0-9a-z%5D%2Bhousing%28%5B%5E0-9a-z%5D%7C%24%29%27%29%29%20AS%20social_housing%2C%20countIf%28match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29social%5B%5E0-9a-z%5D%2Bhousing%28%5B%5E0-9a-z%5D%7C%24%29%27%29%20AND%20NOT%20s%29%20AS%20social_housing_new%20FROM%20%28SELECT%20t%2C%20match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29%28buy%5B%5E0-9a-z%5D%2Bvs%5B%5E0-9a-z%5D%2Brent%7Chome%5B%5E0-9a-z%5D%2Bownership%7Cmortgage%7Crenting%29%28%5B%5E0-9a-z%5D%7C%24%29%27%29%20AS%20s%20FROM%20%28SELECT%20lower%28concat%28title%2C%20%27%20%27%2C%20url%2C%20%27%20%27%2C%20text%29%29%20AS%20t%20FROM%20hackernews_history%20FINAL%20WHERE%20type%20IN%20%28%27story%27%2C%20%27poll%27%2C%20%27job%27%29%20AND%20parent%20%3D%200%20AND%20deleted%20%3D%200%20AND%20descendants%20%3E%3D%205%29%29%20FORMAT%20JSON), so the prompt would add the first two and skip `europe`. After a gate, the resent exchange includes that gate's per-keyword counts, so later rounds judge an addition's volume from real numbers, and the next gate shows its cost before anything downloads. Approval covers the question and the list on screen, and classification, analysis, the report, and reuse all use the approved question.

After each approval, the CLI searches and shows the gate, with no size threshold, because the per-keyword counts help even on small runs. Under the counts, the gate lists each keyword's three matches with the most reported comments, with ID, count, and title, so Stan sees what a keyword pulls in before anything downloads. In the [2026-10-26 mirror](https://play.clickhouse.com/?user=play&query=SELECT%20kw%2C%20id%2C%20descendants%2C%20title%20FROM%20%28SELECT%20id%2C%20descendants%2C%20title%2C%20arrayFilter%28%28k%2C%20m%29%20-%3E%20m%2C%20%5B%27buy%20vs%20rent%27%2C%20%27home%20ownership%27%2C%20%27mortgage%27%2C%20%27renting%27%5D%2C%20%5Bmatch%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29buy%5B%5E0-9a-z%5D%2Bvs%5B%5E0-9a-z%5D%2Brent%28%5B%5E0-9a-z%5D%7C%24%29%27%29%2C%20match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29home%5B%5E0-9a-z%5D%2Bownership%28%5B%5E0-9a-z%5D%7C%24%29%27%29%2C%20match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29mortgage%28%5B%5E0-9a-z%5D%7C%24%29%27%29%2C%20match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29renting%28%5B%5E0-9a-z%5D%7C%24%29%27%29%5D%29%20AS%20kws%20FROM%20%28SELECT%20id%2C%20descendants%2C%20title%2C%20lower%28concat%28title%2C%20%27%20%27%2C%20url%2C%20%27%20%27%2C%20text%29%29%20AS%20t%20FROM%20hackernews_history%20FINAL%20WHERE%20type%20IN%20%28%27story%27%2C%20%27poll%27%2C%20%27job%27%29%20AND%20parent%20%3D%200%20AND%20deleted%20%3D%200%20AND%20descendants%20%3E%3D%205%29%29%20ARRAY%20JOIN%20kws%20AS%20kw%20ORDER%20BY%20kw%2C%20descendants%20DESC%20LIMIT%203%20BY%20kw%20FORMAT%20JSON), `buy vs rent`'s third match was “Ask HN: When to buy vs rent servers?” and `renting`'s two largest were a car-rental thread and an Ask HN about hating a dev career. Nothing is classified yet, so the ranking uses reported comments, which also drive the work ahead; a story appears under each keyword it matches, and a keyword with fewer than three matches lists them all. Stan's reply goes to the keyword prompt: an approval proceeds, and a change shows the revised list, whose approval searches again.

### Progress display

Stan [asked for progress like kibox's](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4376514177). After the gate, `research` keeps a checklist at the bottom of the terminal, one row per stage, and redraws it in place: `✓` marks a finished stage, a spinner the running one, and `·` the stages ahead. The running row shows its count and, during classification, the verdict tallies; the line under it names the call in flight, its model and effort, and the seconds since it started. `run_structured` blocks without streaming, so a ticker thread redraws once a second to keep the spinner and clock moving. Lines worth keeping, such as each relevant verdict, each story that did not download, and each `oversized` story, print above the checklist and scroll normally. While a conversation round or the search waits, one spinner line with a clock shows instead, and nothing redraws while Stan types.

The redraw uses ANSI escape codes, so `research` adds no dependency. `archive_story()` [prints its own line per story](https://github.com/stanislavkozlovski/hn-search/blob/69a87347260824bd030383fec7f00c7609106c16/docs/one-pagers/hn-comment-archives.md?plain=1#L141-L145), so the pipeline captures that line and shows it as an event instead of changing the archive. When stdout is not a terminal, nothing redraws: each event and each story's finished stage prints as one plain line. On a failure or Ctrl-C, the checklist keeps its last state and the error prints below it.

### Search

Search lowercases text, treats each run of characters other than letters and digits as one space, and matches each keyword as a whole phrase; a story matches if any keyword does. `rent` matches “Rent vs. buy” and `/buy-vs-rent`, but not “current” or “renting.” The keyword prompt therefore receives this matching rule word for word and is told to add, without waiting for Stan to ask, every form it wants matched: plurals and verb forms such as `rent`, `rents`, `renting`, and `renters`, and closed compounds such as `homeownership` beside `home ownership`. Those forms find stories the base words miss: [`mortgages` matches 54 eligible stories and `homeownership` 24 that none of the four sample keywords match](https://play.clickhouse.com/?user=play&query=SELECT%20countIf%28match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29mortgages%28%5B%5E0-9a-z%5D%7C%24%29%27%29%29%20AS%20mortgages%2C%20countIf%28match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29mortgages%28%5B%5E0-9a-z%5D%7C%24%29%27%29%20AND%20NOT%20s%29%20AS%20mortgages_new%2C%20countIf%28match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29homeownership%28%5B%5E0-9a-z%5D%7C%24%29%27%29%29%20AS%20homeownership%2C%20countIf%28match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29homeownership%28%5B%5E0-9a-z%5D%7C%24%29%27%29%20AND%20NOT%20s%29%20AS%20homeownership_new%20FROM%20%28SELECT%20t%2C%20match%28t%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29%28buy%5B%5E0-9a-z%5D%2Bvs%5B%5E0-9a-z%5D%2Brent%7Chome%5B%5E0-9a-z%5D%2Bownership%7Cmortgage%7Crenting%29%28%5B%5E0-9a-z%5D%7C%24%29%27%29%20AS%20s%20FROM%20%28SELECT%20lower%28concat%28title%2C%20%27%20%27%2C%20url%2C%20%27%20%27%2C%20text%29%29%20AS%20t%20FROM%20hackernews_history%20FINAL%20WHERE%20type%20IN%20%28%27story%27%2C%20%27poll%27%2C%20%27job%27%29%20AND%20parent%20%3D%200%20AND%20deleted%20%3D%200%20AND%20descendants%20%3E%3D%205%29%29%20FORMAT%20JSON). The gate's per-keyword counts then show what each form adds. Search reads every `posts` row and adds no index. The run saves the matched IDs when Stan proceeds.

### Downloads and classification

The pipeline calls `archive_story()` for each matched story, so an already archived story costs no request. If the call raises, or HN returned the root as `null`, the story goes into coverage as `not downloaded` or `unavailable` with its reason, and the pipeline moves on; a later run resumes that download. If the network drops, every remaining story fails into that list.

Every other archived story gets a description, saved per archive and reused across questions, and a verdict on the approved question with reasons and supporting comment IDs. The pipeline checks that every cited ID belongs to the discussion it sent; Pass 2 settles what happens to a result that cites another ID, as the [Pass 0.1 review](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4375494805) left it. Relevant stories get folders. Uncertain stories skip deep analysis and appear in coverage with their reasons.

### Oversized discussions

Before each call, the pipeline estimates the input size. If a discussion does not fit the stage model's input budget, which Pass 2 sets below the context window, the pipeline splits it:

1. Each part takes whole top-level comment threads, a comment with all its replies, in display order. A thread too large for one part is split the same way at its replies.
2. Each part opens with the story and the chain of parent comments above its first comment, marked as context. Every comment keeps its ancestry, and its own text appears in exactly one part.
3. The pipeline records each part's comment IDs and checks that the parts together cover every saved comment.
4. Verdicts combine without a call: `relevant` if any part is relevant, otherwise `uncertain` if any part is uncertain, otherwise `irrelevant`. Descriptions and deep analyses get one combining call that reads only the part results.
5. If the part results do not fit one combining call, the story goes into coverage as `oversized`. The pipeline never truncates a discussion.

[85,076 comments](https://play.clickhouse.com/?user=play&query=SELECT%20count%28%29%20AS%20comments%2C%20round%28avg%28length%28text%29%29%29%20AS%20avg_chars%20FROM%20hackernews_history%20FINAL%20WHERE%20type%20%3D%20%27comment%27%20AND%20deleted%20%3D%200%20AND%20id%20BETWEEN%2042000000%20AND%2042100000%20FORMAT%20JSON) with IDs from 42,000,000 to 42,100,000 average 369 characters, roughly 92 tokens at four characters per token. At that rate, the largest buy-versus-rent match, [`40490610`](https://news.ycombinator.com/item?id=40490610) “Priced out of home ownership,” needs about 115,000 tokens for its 1,245 reported comments, under half of the [272,000-token window](https://github.com/openai/codex/blob/970111f6cb62cc02fe36a82ea7d71b37a2889c97/codex-rs/models-manager/models.json#L34) that Codex gives `gpt-6-astra` and [`gpt-6-luna`](https://github.com/openai/codex/blob/970111f6cb62cc02fe36a82ea7d71b37a2889c97/codex-rs/models-manager/models.json#L553) by default. [`42057647`](https://news.ycombinator.com/item?id=42057647) “Trump wins presidency for second time” needs about 855,000 tokens for 9,274 comments, so it splits into several parts.

Stan [asked for tests](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4375867878). Pass 2's test plan must cover splitting at top-level and nested replies, the context chain, exactly-once coverage, both kinds of combining, and the `oversized` fallback.

### Folders, analyses, and the report

Each relevant story's folder gets the archive's JSON export as `thread.json` and a Markdown rendering of the same saved snapshot as `thread.md`. Deep analysis then writes `analysis.md`: links to the story on HN and to `thread.md`, the description and verdict reasons, followed by the arguments, counterarguments, assumptions, conditions, lived experiences, and unresolved disagreements, each linked to its comments. The model returns comment IDs, and the pipeline renders each as an Obsidian link to that comment's block in the story's `thread.md`, such as `[[./thread#^c40494448|tmnvix]]`; the comment's bullet there links on to HN.

`thread.md` opens with the story title linked to its HN page, the article link, the author, the posting date, the reported comment count, and the archive date. Every saved comment follows as a nested bullet in display order, one level per reply, with its author, its time linked to the comment on HN, and its text converted from HN's HTML. Deleted, flagged, and unavailable items keep their place as `[deleted]`, `[flagged]`, or `[unavailable]`, so the reply tree stays intact. Each comment's bullet ends with an Obsidian block ID such as `^c40494448`, so a link can point at one comment; Obsidian [allows block IDs on list lines but not inside quotations](https://obsidian.md/help/Linking+notes+and+files/Internal+links), so replies nest as bullets rather than `>` quotes.

```markdown
# [Priced out of home ownership](https://news.ycombinator.com/item?id=40490610)

[bbc.co.uk](https://www.bbc.co.uk/news/articles/cmj66r4lvzzo) · user20180120 · 2024-05-27 · 1,245 reported comments · archived 2026-10-26

- **tmnvix** · [2024-05-27 20:38 UTC](https://news.ycombinator.com/item?id=40494448)
  (tmnvix's comment, in Markdown) ^c40494448
  - **dan-robertson** · [2024-05-27 21:11 UTC](https://news.ycombinator.com/item?id=40494752)
    (dan-robertson's reply, in Markdown) ^c40494752
```

The archive design [keeps Markdown exports out of `archive`](https://github.com/stanislavkozlovski/hn-search/blob/69a87347260824bd030383fec7f00c7609106c16/docs/one-pagers/hn-comment-archives.md?plain=1#L71), so the pipeline renders `thread.md` from the archive's saved records, and `archive` does not change. HN comments carry only [paragraphs, italics, code, and links](https://news.ycombinator.com/formatdoc), so the conversion handles those four plus HTML entities; Pass 2 specifies it, including escaping comment text that Obsidian would read as a link, tag, or heading.

The synthesis reads every relevant analysis and writes the cross-thread sections of `report.md`, in one call or one folder session as described below. The pipeline then appends the thread index and coverage from saved state. The index links each relevant story's title to its `analysis.md`, adds links to its `thread.md` and its HN page, and gives its description, and the synthesis cites comments the same way the analyses do. Coverage lists every other matched story under `not downloaded`, `unavailable`, `oversized`, `uncertain`, or `irrelevant`, each with its reason. Coverage entries link to HN, because those stories have no folders.

```markdown
## Arguments

Cheap credit, not too little building, drove prices, argues [[./stories/40490610/thread#^c40494448|tmnvix]]; [[./stories/40490610/thread#^c40494752|dan-robertson]] answers that rates alone don't explain the gaps between countries, citing dwellings per person in EU countries.

## Thread index

- [[./stories/40490610/analysis|Priced out of home ownership]] · [[./stories/40490610/thread|thread]] · [HN](https://news.ycombinator.com/item?id=40490610) — (description)
```

Every link starts with `./` because every story folder repeats `analysis.md` and `thread.md`. Obsidian reads folder paths in links [from the vault root](https://obsidian.md/help/Linking+notes+and+files/Internal+links) and resolves a bare `[[analysis]]` by name across the vault, while a [forum report](https://forum.obsidian.md/t/absolute-link-path-has-higher-precedence-than-relative-path/69542) shows `[[./A|A]]` resolving relative to the linking note, so the links keep working wherever Stan puts the run folder in a vault. Pass 2 checks each link form in Obsidian.

Before the synthesis, the pipeline estimates the size of every relevant analysis. When they fit the report model's input budget, one call receives them all in its prompt, as every other stage does. When they do not, which Stan [expects to be the usual case](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4376618684), one folder session replaces that call: Codex runs with the report row's model and effort, starts in the run folder with `--sandbox read-only` and no network, gets the question and the thread index in its prompt, reads each `stories/<id>/analysis.md` itself, and opens a `thread.md` only to check a quote. When its context fills, Codex's [automatic compaction](https://github.com/openai/codex/blob/970111f6cb62cc02fe36a82ea7d71b37a2889c97/codex-rs/protocol/src/openai_models.rs#L534-L545) summarizes the conversation at 90% of the 272,000-token window, so the session keeps reading. Its final answer uses the inline synthesis's output schema, so the pipeline checks its cited IDs and writes the index and coverage the same way. Pass 2's test plan must cover the switch at the budget boundary, the session's sandbox options, and the cited-ID check on its answer.

When no story is relevant, the pipeline skips the synthesis, and `report.md` holds only coverage.

### Saved state and AI calls

This design lands after the archive design, and its tables join the same `--db` file as schema v3, after the archive's v2:

- A run record holds the question, keywords, settings, matched IDs, and each story's stage status.
- An AI result record holds the stage, story, part, prompt version, model, effort, archive, the question where the stage depends on it, the result, and the cited IDs.

`collect` keeps working on a v3 file, because `open_catalog()` [never overwrites a non-zero `user_version`](https://github.com/stanislavkozlovski/hn-search/blob/64703b58fedbe19ef8e80612ab1d825e880e2eaf/tests/test_catalog.py#L44-L48). Pass 2 defines the migration and rollback. `research` shares the file, so Stan runs one command at a time, as `collect` already requires.

AI calls run one at a time with each stage's model and effort. They drop the client's default [`bypassPermissions` mode](https://github.com/stanislavkozlovski/stan_ai_client/blob/e423a5548292e51c5ffab1b8420a67ae38d7f4a2/src/stan_ai_client/codex.py#L152-L155) and run from an empty scratch directory with the HN text inside the prompt, so the model needs no tool, file, or network access. The folder session is the one exception, because it reads files in the run folder. Codex's read-only sandbox blocks writes and network but [can read the whole disk](https://github.com/openai/codex/blob/970111f6cb62cc02fe36a82ea7d71b37a2889c97/codex-rs/protocol/src/protocol.rs#L1334-L1336), and the analyses quote HN text that could tell the model to open other files, so the session must read nothing outside the run folder. Codex [has read-deny rules](https://github.com/openai/codex/blob/970111f6cb62cc02fe36a82ea7d71b37a2889c97/codex-rs/protocol/src/permissions.rs#L315-L321) for this; Pass 2 confirms that the installed `codex` enforces a run-folder-only read rule and stops for Stan's decision if it cannot. They pass no `rate_limit_policy` to `run_structured`, so on a usage limit it [raises `CodexRateLimitError` at once](https://github.com/stanislavkozlovski/stan_ai_client/blob/e423a5548292e51c5ffab1b8420a67ae38d7f4a2/src/stan_ai_client/_retry.py#L30-L31) instead of sleeping until the reset, and `research` retries no failed call. Pass 2 pins the Codex sandbox flags and sets per-stage timeouts in place of the client's 120-second default.

## Rejected design alternatives

| Alternative | Why rejected |
|---|---|
| Search matches keywords as substrings. | In eligible titles, [substring `renting` matches 145 stories](https://play.clickhouse.com/?user=play&query=SELECT%20countIf%28positionCaseInsensitive%28title%2C%20%27renting%27%29%20%3E%200%29%20AS%20substring_renting%2C%20countIf%28match%28lower%28title%29%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29renting%28%5B%5E0-9a-z%5D%7C%24%29%27%29%29%20AS%20word_renting%2C%20countIf%28positionCaseInsensitive%28title%2C%20%27parenting%27%29%20%3E%200%29%20AS%20parenting%2C%20countIf%28positionCaseInsensitive%28title%2C%20%27rent%27%29%20%3E%200%29%20AS%20substring_rent%2C%20countIf%28match%28lower%28title%29%2C%20%27%28%5E%7C%5B%5E0-9a-z%5D%29rent%28%5B%5E0-9a-z%5D%7C%24%29%27%29%29%20AS%20word_rent%20FROM%20hackernews_history%20FINAL%20WHERE%20type%20IN%20%28%27story%27%2C%20%27poll%27%2C%20%27job%27%29%20AND%20parent%20%3D%200%20AND%20deleted%20%3D%200%20AND%20descendants%20%3E%3D%205%20FORMAT%20JSON), 63 of them containing “parenting,” while whole-word `renting` matches 70; substring `rent` matches 5,071 stories, against 439 for the whole word. |
| Search uses an SQLite FTS5 index with stemming. | FTS5 needs a schema migration and a full-text index over every post, and its tokenizer and stemmer decide matches that the gate's keyword list does not show. |
| The conversations resume one Codex session through `CodexRunOptions.session_id`. | `run_structured` returns the session's `thread_id` only with `capture_usage=True`, and the session keeps hidden state in Codex's own store; resending the exchange keeps each round self-contained. |
| `research` is a full-screen TUI. | A TUI framework would add a dependency and take over the screen, while a few ANSI escape codes redraw the progress checklist in place between the line-based prompts. |
| The synthesis model writes the thread index and coverage. | The model could drop or miscount threads; the pipeline writes both from saved state, so every relevant thread and every omission appears. |
| The report writer merges analyses in smaller groups, then merges the group results. | Each merge level adds another lossy summary, prompt, and cap; Stan [chose](https://github.com/stanislavkozlovski/hn-search/pull/6#discussion_r4376618684) a session that reads the analyses themselves. |
| Several AI calls run at once. | Parallel calls would shorten runs but add coordination and reach Codex usage limits sooner. |

-----------------------------------

# Legend (do not delete)

Scope growth labels mean:

- **INCLUDE** accepts the resulting scope;
- **CONSTRAIN** limits the behavior that causes it;
- **EXCLUDE** leaves the broader work outside this proposal.

Each label is valid only when its row also names the repeatable growth
mechanism and a finite, observable cap.
