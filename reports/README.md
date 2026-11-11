# Saved research reports

## Air quality

[Read the report](air-quality/report.md) on indoor and outdoor air quality,
especially PM2.5, NO₂, and CO₂. It covers reported experiences, measurements,
ventilation, filtration, and disagreements across Hacker News discussions.

This is the completed research run 8 from November 8–9, 2026. It matched 378
discussions, downloaded 377, and analyzed 297 relevant threads. The report's
coverage section also records 28 uncertain threads, 52 irrelevant threads, and
one download timeout.

### Takeaways

- **CO₂ and cognition:** The studies discussed in the [HN summary](https://news.ycombinator.com/item?id=19863319) and [submarine-research exchange](https://news.ycombinator.com/item?id=34658142) do not consistently show that elevated CO₂ at typical indoor concentrations directly impairs cognition.

## Read in Obsidian

Clone or pull this repository locally. In Obsidian, choose **Open folder as
vault**, select this `reports/` directory, and open `air-quality/report.md`.
Alternatively, copy the entire `air-quality/` folder into an existing vault.

Keep each report beside its `stories/` directory. Its Obsidian links open
per-thread analyses and jump to individual archived comments. Generic Markdown
viewers may display these links as text.

## Snapshot contents

The air-quality folder contains 595 Markdown files, about 17.8 MiB: one report,
297 analyses, and 297 archived discussions. These files are unchanged copies of
the Markdown output in `/home/ops/services/hn-search/research/run-8/` on uzealot.
The report records the research question, keywords, and model settings.

The SQLite catalog, AI cache, and raw JSON exports remain in the service data
directory. New CLI runs still write to the ignored `research/` output directory;
`reports/` holds selected completed Markdown snapshots.
