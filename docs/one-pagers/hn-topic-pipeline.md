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
| When an archived discussion exceeds the selected model's usable context, the classifier or deep-analysis call cannot inspect the whole discussion at once. | The pipeline stops that story with a visible oversized-input status rather than silently truncating it or claiming full coverage. | The pipeline splits the discussion with reply ancestry, tracks which comments were considered, and combines the partial analyses with explicit bounds agreed in Pass 1. | UNDECIDED — HANDLE / IGNORE |
| When confirmed keywords match many thousands of stories, the promised download-and-analysis pipeline can require substantial time and AI usage. | The pipeline processes the full matched set without an additional size or spending approval and never silently replaces it with a top-N sample. | The terminal shows the candidate count and estimated work and asks for a separate proceed-or-refine decision before downloading and spending AI usage. | UNDECIDED — HANDLE / IGNORE |
| When AI marks an archived story uncertain, Stan can see its classification but the story has no settled relevance decision. | The pipeline leaves it in the visible uncertain set outside the relevant-story analysis and names that exclusion in report coverage. | The terminal asks Stan to include or exclude uncertain stories before deep analysis and records those decisions for the report. | UNDECIDED — HANDLE / IGNORE |
| When a matched story remains incomplete or unavailable after download, the pipeline lacks the complete discussion expected by classification. | The pipeline stops before producing the final report and retains completed work for a later resume. | The pipeline can continue with complete archives and explicitly list the omitted or incomplete stories in report coverage. | UNDECIDED — HANDLE / IGNORE |
| When individually small [thread analyses](https://github.com/stanislavkozlovski/hn-search/blob/62ee115d5210823fc82e3723d8c8757ab74efeea/docs/one-pagers/hn-topic-pipeline.md#L20-L29) exceed the model’s input limit together, the report writer cannot finish. | Stan receives separate thread analyses without the combined report. | The report writer combines analyses in smaller groups while preserving comment links and an index of every relevant thread. | UNDECIDED — HANDLE / IGNORE |
| When Stan's reply narrows the question itself, such as “focus on Europe,” the AI changes only the keyword list. | The classifier and report keep judging Stan's original question, so the narrower intent reaches only the search terms. | The AI also proposes a revised question for Stan to approve with the keywords, and classification and the report use that question. | UNDECIDED — HANDLE / IGNORE |
