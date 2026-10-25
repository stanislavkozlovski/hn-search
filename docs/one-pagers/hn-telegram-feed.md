# HN Telegram feed

## Pass 0: Problem or opportunity framing

### Who is the user, what do we know about their behavior, and how correct does the result need to be?

- **User:** Stan.
- **Their behavior:** Stan configures filters ("lenses") over one HN feed and receives links worth posting through each lens's Telegram bot.
- **Edge-case tolerance:** Fewer irrelevant alerts matter more than missed stories, and hourly delivery is fine even when a post only becomes interesting after two hours.

### What is the prevailing user problem or opportunity?

- **Problem or opportunity:** Stan wants good posting material without constantly checking HN.

### What is the proposed solution, and why is it right for the user?

- **Solution:** Each hour, search Algolia's HN index for stories created in the preceding ten hours with at least five points, save their titles, links, and score observations, and send lens matches to configured Telegram destinations.
- **Why it fits the user:** One saved feed serves independently configurable lenses and bots, while compact batches and cached relevance decisions keep AI usage low.

Use a configurable lightweight model, initially Luna, and reuse classifications while title/URL inputs and lens rules remain unchanged.

The feed uses points for admission, while PR #1 uses five comments to select discussions for research.

Record `N → M points over X minutes` from successive observations, starting at first discovery at five points; prior observations are not required for admission.

The first delivery uses hourly overlapping search; zero-point watchlists and specialized flat-hour retirement remain deferred.

Keep every saved story without pruning, including stories no lens matched, along with its score observations and lens decisions, so Stan can [revisit a story later](https://github.com/stanislavkozlovski/hn-search/pull/3#discussion_r4372384723).

**Deferred — shared storage:** Stan [keeps the feed's storage separate from the research archive for now](https://github.com/stanislavkozlovski/hn-search/pull/3#discussion_r4372390552); merging them is outside the first delivery.

**Deferred — revisiting saved stories:** Commands that search saved stories, re-run lenses over them, or resend them are outside the first delivery.

### How would you describe the end-to-end user experience?

- **End-to-end user experience:** Each hour, Stan receives one message or batch per configured Telegram destination with matching titles, article/HN links, categories, points, and any observed score growth.

For example, a two-hour-old story at six points and zero comments can reach a matching bot; the next result at nineteen points updates growth without repeating classification.

### What existing data, behavior, or integrations must keep working?

- **Legacy data:** Assume PR #1 is implemented and preserve its archived posts and collection progress.
- **Legacy behavior:** Preserve PR #1's resumable backfill, rolling five-day daily collection, status command, and separate five-comment archive admission rule.
- **Existing integrations:** Reuse `stan_ai_client`; no existing Telegram bot integration is required.
- **Compatibility tolerance:** Keep PR #1 data and commands usable while admitting feed candidates independently of their comment counts.

**Assumed baseline:** [PR #1 at `5bdf928`](https://github.com/stanislavkozlovski/hn-search/blob/5bdf928d213c012f43e5204030d077f6f9989a9c/docs/one-pagers/hn-topic-research.md) proposes a SQLite research archive whose `posts` table requires `descendants >= 5`, with collection checkpoints and no score history; implementation is assumed here.

**Reference checked:** Local OFFNews code at `/home/ops/code/albufera.js/src/scraper/news/offnews/classify_titles.py` uses structured title classification through `stan_ai_client` and reusable batch checkpoints.

**Source and sizing checked:** The [HN Search API](https://hn.algolia.com/api) supports the proposed filters and pagination; probes on 2026-10-25 found an average of 238 five-point stories per day for October 18–24, using current scores rather than a first-ten-hour replay.

### Agent edge-case scan

| Edge case | What happens if ignored | What handling it adds | User decision |
|---|---|---|---|
| When Stan feeds five-point, low-comment stories into PR #1's research archive, the archive's `posts.descendants >= 5` check rejects them. | The feed needs separate storage while the research archive stays unchanged. | The feed extends the research archive's schema while preserving its records and checkpoints and defining upgrade and older-collector behavior. | IGNORE |
| When the hourly job stays offline for more than ten hours, its next rolling query excludes older missed stories. | Stan misses those older stories after restart. | The feed catches up missed intervals beyond the normal lookback. | UNDECIDED — HANDLE / IGNORE |
| When Stan adds a lens, saved candidates already have decisions for existing lenses. | The new lens only sees newly discovered candidates. | The feed evaluates saved candidates still within the lookback for the new lens. | UNDECIDED — HANDLE / IGNORE |
| When two lenses select one story for the same bot and chat, both enqueue it. | Stan receives duplicate links in that destination. | The feed deduplicates delivery across lenses for each bot and chat. | UNDECIDED — HANDLE / IGNORE |
| When Telegram accepts a send but its response is lost, the feed cannot confirm delivery. | The sender may duplicate links when retrying. | The feed records uncertain sends and defines retry behavior. | UNDECIDED — HANDLE / IGNORE |
