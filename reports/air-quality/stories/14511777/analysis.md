# [Google Cloud Public Datasets now hosts EPA and OpenAQ air quality data](https://news.ycombinator.com/item?id=14511777)

[[./thread|Discussion]]

## Description

Participants discuss access to EPA and OpenAQ datasets through Google BigQuery, including data availability, query capabilities, and possible analysis such as clustering. The thread also raises concerns about the removal of public government data, the role of private data collection, and delays in air quality measurements.
Tags: public datasets, air quality data, Google BigQuery, data access, environmental monitoring

## Relevance

The discussion addresses air quality data reliability, including delays in supposedly live readings and concerns about access to accurate monitoring data. [[./thread#^c14512605|adorable]] [[./thread#^c14514525|panarky]]

## Arguments

- adorable [[./thread#^c14512605|adorable]] claims that supposedly live air-quality feeds typically lag by 1–6 hours because measurement, compilation, and publication take time. A reported pollution peak may therefore have ended already. They recommend hourly prediction models, mentioning Plume, but provide no measured example or validation.
- panarky [[./thread#^c14514525|panarky]] argues that private companies should gather and publish environmental data when federal sources become unreliable or unavailable. They cite alleged removal of public federal data and Google's deployment of air-pollution sensors on Street View cars; no sensor results accompany the argument.
- vgt [[./thread#^c14515628|vgt]] describes SQL access and joins with other datasets as practical benefits of BigQuery hosting. gaetanrickter [[./thread#^c14512261|gaetanrickter]] proposes linking these datasets to public companies and exploring them with t-SNE and clustering. These are analysis capabilities and proposed work, not findings about personal exposure.

## Counterarguments

- Replying to panarky [[./thread#^c14514525|panarky]], Florin\_Andrei [[./thread#^c14515899|Florin\_Andrei]] attributes the federal-data problem more specifically to the administration then in charge. This qualifies institutional responsibility without disputing the removal claim or establishing anything about measurement accuracy.

## Assumptions

- panarky [[./thread#^c14514525|panarky]] moves from reduced public-data availability to doubts about obtaining accurate government data. Availability and accuracy are distinct, and the comment does not demonstrate inaccurate measurements or establish that private replacements would remain accurate and accessible.
- adorable [[./thread#^c14512605|adorable]] assumes prediction models can resolve the practical problem of delayed observations. That depends on forecast accuracy at the relevant time and location; the comment does not establish that modeled conditions reliably represent current personal exposure.

## Conditions

- panarky [[./thread#^c14514525|panarky]] explicitly discusses U.S. federal data access. The comment provides no geographic coverage details for Google's vehicle-mounted sensors, so their usefulness for a particular neighborhood cannot be assessed.
- vgt [[./thread#^c14515628|vgt]], who discloses working at Google, reports a free BigQuery allowance of 10 GB of storage and 1 TB of queries per month. These are reported terms from this 2017 discussion, not verified current prices or evidence about the affordability of household monitoring.

## Lived experiences


## Unresolved disagreements

- The relationship between publication schedules remains unclear: adorable [[./thread#^c14512605|adorable]] describes typical monitoring-feed delays of 1–6 hours, while vgt [[./thread#^c14515628|vgt]] says Public Datasets are updated almost weekly. The latter statement does not establish the refresh cadence of the specific EPA/OpenAQ datasets, and the comments need not contradict one another.
- Neither adorable [[./thread#^c14512605|adorable]]'s discussion of monitoring delays nor panarky [[./thread#^c14514525|panarky]]'s mention of mobile sensors supplies numerical PM2.5, NO2, or CO2 readings, calibration information, sensor comparisons, or prediction errors. Measurement reliability and the accuracy of the proposed modeling solution remain untested within this source.
- The contributions concern data access, timeliness, and prospective analysis—illustrated by adorable [[./thread#^c14512605|adorable]], vgt [[./thread#^c14515628|vgt]], and gaetanrickter [[./thread#^c14512261|gaetanrickter]]. They provide no firsthand exposure accounts or evidence about health, cognition, sleep, comfort, ventilation, filtration, cooking, traffic pollution, or wildfire smoke. This unit therefore cannot establish when opening windows helps or worsens exposure.
