# [Google Cloud Public Datasets now hosts EPA and OpenAQ air quality data](https://news.ycombinator.com/item?id=14511777)

Article: [https://cloud.google.com/blog/big-data/2017/06/us-epa-and-openaq-air-quality-data-now-available-in-bigquery](<https://cloud.google.com/blog/big-data/2017/06/us-epa-and-openaq-air-quality-data-now-available-in-bigquery>)

vgt · 2017-06-08 03:46 UTC · 5 reported comments · archived 2026-11-08 10:46 UTC
Observation: 2026-11-08 10:46 UTC → 2026-11-08 10:46 UTC

## Comments

- **panarky** · [2017-06-08 14:45 UTC](https://news.ycombinator.com/item?id=14514525)
  Important context: ^c14514525

  1) US federal government has removed vast troves of public data produced by the EPA, OSHA and the Interior Department.

  Source: [https://www.washingtonpost.com/politics/under-trump-inconven...](<https://www.washingtonpost.com/politics/under-trump-inconvenient-data-is-being-sidelined/2017/05/14/3ae22c28-3106-11e7-8674-437ddb6e813e_story.html>)

  2) Google has now equipped Street View cars with air pollution sensors.

  Source: [https://environment.google/projects/airview/](<https://environment.google/projects/airview/>)

  Conclusion: If we can no longer rely on getting accurate data from federal agencies, private companies with a public mission will need to gather the data and make it available.

  - **Florin\_Andrei** · [2017-06-08 18:05 UTC](https://news.ycombinator.com/item?id=14515899)
    \> *US federal government* ^c14515899

    Well, whoever is in charge of it now, to be more precise.

    This observation might appear specious, but I feel it's appropriate in the current context.

- **adorable** · [2017-06-08 07:44 UTC](https://news.ycombinator.com/item?id=14512605)
  Important note: so-called "live" air quality measurements are in reality never "live" due to the nature of the measuring stations (taking measures takes time) and the way data is compiled and shared by the monitoring agencies. As a result typical delays range from 1 to 6 hours, which means you end up using "old" data or signaling a peak when in reality the pollution peak is already over. ^c14512605

  This is solved by using models that predict air quality levels down to the hour. One option is to use [https://plume.io](<https://plume.io>)

- **vgt** · [2017-06-08 17:26 UTC](https://news.ycombinator.com/item?id=14515628)
  A not on Google Cloud Public Datasets: ^c14515628

  \- Public Datasets are updated almost weekly these days \[0\]

  \- They are hosted in Google BigQuery storage immediately accessible by Standard SQL and easily joined against other public or private datasets

  \- BigQuery has a perpetual free tier - 10GB of storage per month, 1TB of query per month. \[1\]

  \[0\] [https://cloud.google.com/bigquery/public-data/](<https://cloud.google.com/bigquery/public-data/>)

  \[1\] [https://cloud.google.com/free/](<https://cloud.google.com/free/>)

  (work on G)

- **gaetanrickter** · [2017-06-08 06:09 UTC](https://news.ycombinator.com/item?id=14512261)
  I'm thinking of connecting these to public companies [http://54.174.116.134/recommend/datasets/index-hn02.html](<http://54.174.116.134/recommend/datasets/index-hn02.html>) and running a few t-SNE and other clustering algo's for visualizing the dataset. ^c14512261

- **unknown** · [2017-06-08 09:40 UTC](https://news.ycombinator.com/item?id=14513002)
  [deleted] ^c14513002

