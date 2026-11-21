# [Cutting through the smog: making an air quality bot with Haskell](https://news.ycombinator.com/item?id=20331873)

[[./thread|Discussion]]

## Description

Discussion branches from an air-quality chatbot tutorial into DIY monitoring projects, sensor choices, and ways to present or share air-quality data. Participants compare technology stacks and home-automation components, offer feedback on how the Haskell tutorial is structured, and reflect on the spread of poor air quality.
Tags: Haskell, air quality, chatbot, DIY sensors, software tutorial

## Relevance

Comments discuss DIY air-quality monitoring and specific PM and CO2 sensor options, including interest in reliability and integrating sensors with home systems. The thread is mainly about tools and software, with little firsthand exposure or health discussion. [[./thread#^c20333368|t0mek]] [[./thread#^c20333694|psandersen]] [[./thread#^c20334038|jsingleton]] [[./thread#^c20418895|psandersen]]

## Arguments

- psandersen [[./thread#^c20333694|psandersen]] proposes affordable DIY monitoring through ESPHome: MH-Z19 for CO2, SDS011 for particles, and CCS811 as a CO2/VOC option. This answers a request for reliable Home Assistant integration with candidate hardware, rather than demonstrated accuracy or evidence of improved air quality.

## Counterarguments

- Replying to bayesian\_horse’s [[./thread#^c20332402|bayesian\_horse]] hope of never moving somewhere that warrants monitoring, yakshaving\_jgt [[./thread#^c20334160|yakshaving\_jgt]] argues that bad air could reach an existing home. This challenges the implied geographic security but supplies no location, pollution source, or measured change.
- After jsingleton [[./thread#^c20334038|jsingleton]] suggests an SGP30, psandersen [[./thread#^c20418895|psandersen]] says its ESPHome integration appears less straightforward and postpones considering it. A favorable sensor recommendation therefore encounters a practical compatibility limitation, rather than an objection supported by accuracy testing.

## Assumptions

- Treating the proposed CO2-related outputs as interchangeable would require an unsupported assumption. psandersen [[./thread#^c20333694|psandersen]] lists MH-Z19 and CCS811, while jsingleton [[./thread#^c20334038|jsingleton]] links an SGP30 labeled VOC/eCO2; the comments do not explain their measurement methods, calibration, or comparability.

## Conditions

- psandersen [[./thread#^c20333694|psandersen]] explicitly favors low-cost sensor options while considering DIY hardware versus Awair. No prices, complete installation costs, or maintenance costs are supplied, so the discussion cannot establish comparative value.
- The geographic exchange between bayesian\_horse [[./thread#^c20332402|bayesian\_horse]] and yakshaving\_jgt [[./thread#^c20334160|yakshaving\_jgt]] identifies no actual place or exposure conditions. It supports a general concern about changing local air quality, not advice about particular regions or homes.

## Lived experiences

- t0mek [[./thread#^c20333368|t0mek]] reports several months developing a page that displays data from DIY Luftdaten detectors. User requests and hosting problems led to a shared, open-source service. This is firsthand experience making monitoring data accessible and supporting deployments; no pollutant readings or exposure outcomes are reported.
- arunarunarun [[./thread#^c20334337|arunarunarun]] reports writing software to retrieve data from Kaiterra Laser Eggs. This establishes experience with data acquisition, but supplies no readings, sensor comparison, or reliability assessment.
- psandersen [[./thread#^c20418895|psandersen]] reports having ordered other sensors before the SGP30 suggestion and describes ESPHome as making previously intimidating DIY electronics approachable. The comment does not report completed measurements or resulting changes to ventilation or filtration.

## Unresolved disagreements

- The original reliability question remains unanswered: psandersen [[./thread#^c20333694|psandersen]] asks whether an SDS011-based approach is preferable to Awair, while jsingleton [[./thread#^c20334038|jsingleton]] suggests alternatives without comparative measurements. Accuracy, drift, calibration needs, and suitability for dependable household decisions remain unestablished.
- The monitoring contributions from t0mek [[./thread#^c20333368|t0mek]], arunarunarun [[./thread#^c20334337|arunarunarun]], and psandersen [[./thread#^c20333694|psandersen]] contain no numerical PM2.5 or CO2 measurements, NO2 findings, or study results. They provide no firsthand evidence about health, cognition, sleep, or comfort, and cannot resolve the effects or tradeoffs of cooking, traffic, wildfire smoke, ventilation, filtration, or opening windows. These are evidence gaps in this source unit, rather than documented disagreements about those outcomes.
