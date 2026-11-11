# [Typical CO2 Levels at Home Test](https://news.ycombinator.com/item?id=33312298)

[[./thread|Discussion]]

## Description

Discussion scrutinizes a consumer-oriented article about typical home CO2 levels, including outdated outdoor baselines, sensor calibration, and whether precise readings matter for tracking ventilation changes. Participants describe monitoring CO2 at home and in cars, question claims linking elevated levels to drowsiness or impaired performance, and point to pilot studies. The thread also notes the article’s commercial interest and discusses DIY monitoring with sensors and data dashboards.
Tags: CO2 monitoring, indoor ventilation, sensor calibration, consumer devices, air quality

## Relevance

The discussion directly covers indoor CO2 readings, sensor calibration and reliability, and ventilation. Firsthand accounts describe a home reaching about 1500 ppm and levels falling with a bathroom fan, as well as CO2 rising in a closed car; commenters question measurement accuracy and the strength of claims about drowsiness and cognition. [[./thread#^c33312521|gruez]] [[./thread#^c33312788|D13Fd]] [[./thread#^c33313056|jodrellblank]] [[./thread#^c33313381|lh7777]] [[./thread#^c33313695|shashurup]] [[./thread#^c33315290|tuatoru]] [[./thread#^c33316934|D13Fd]] [[./thread#^c33319199|mshook]] [[./thread#^c33323821|gruez]] [[./thread#^c33328492|kkfx]]

## Arguments

- D13Fd [[./thread#^c33316934|D13Fd]] argues that a household CO2 monitor can usefully show ventilation response and the time needed to approach outdoor levels without precisely calibrated absolute readings. Their practical case rests on environmental responsiveness and correlation with perceived air quality.
- mshook [[./thread#^c33319199|mshook]] quotes a pilot-simulator study reporting a 69\% greater likelihood of passing maneuvers at 700 versus 2,500 ppm, and 52\% greater likelihood at 1,500 versus 2,500 ppm. The overall 700-versus-1,500 comparison was not statistically significant, although some difficult maneuvers favored the lower concentration. Reported adverse effects increased with exposure duration. These are quoted study findings, not firsthand measurements or independently verified results.
- jodrellblank [[./thread#^c33313056|jodrellblank]] raises cabin ventilation and CO2 monitoring as potentially important safety interventions. They quote an account reaching 1,900 ppm after a 15-minute closed-window drive and 2,400 ppm on the return, with a decrease when the door opened. The quoted account describes roughly 70-degree weather and unused heating/air conditioning. They also quote a SenseAir claim of 6,000 ppm with four adults despite fresh-air ventilation. None of these measurements is jodrellblank's own.

## Counterarguments

- brianwawok [[./thread#^c33312552|brianwawok]] questions the independence of advice promoting CO2 monitoring on a site selling CO2 meters. This identifies a commercial incentive, without establishing that every measurement or recommendation is wrong.
- gruez [[./thread#^c33312521|gruez]] challenges the article's purported normal outdoor range of 250–350 ppm by citing NOAA's 414 ppm figure for 2021. antisthenes [[./thread#^c33312956|antisthenes]] suggests that an old marketing article may display a dynamic date, but supplies no evidence establishing its age.
- Replying directly to D13Fd's approximately 1,500 ppm report, tuatoru [[./thread#^c33315290|tuatoru]] challenges confidence in the absolute value without certified calibration and argues that uncalibrated consumer instruments mainly support tentative directional comparisons. The comment supplies no independent test of D13Fd's particular instrument.
- kkfx [[./thread#^c33315703|kkfx]] suspects electronic sensors, including CO2 monitors, may have calibration problems over time. After receiving an explanation of automatic baseline calibration, kkfx [[./thread#^c33328492|kkfx]] objects that outdoor concentrations vary geographically. These are reliability concerns rather than measured sensor failures; kkfx explicitly disclaims knowledge of the sensors' internal operation.

## Assumptions

- gruez [[./thread#^c33323821|gruez]] describes what they believe is common consumer-monitor auto-calibration: treating the lowest concentration observed over several days as 400 ppm. Their justification assumes that homes or offices become vacant regularly and that their minimum indoor concentration consequently represents outdoor air. Neither premise is demonstrated for the particular homes discussed.
- shashurup [[./thread#^c33313695|shashurup]] concludes that their device is probably accurate because reaching approximately 800 ppm after closing the room seems reasonable. Plausible-looking buildup is being used as a calibration check, without an independent reference instrument or known room concentration.
- D13Fd [[./thread#^c33316934|D13Fd]] reports that readings correlate with noticeable air-quality changes. Attributing those subjective changes specifically to CO2 would require an additional assumption: the account does not isolate CO2 from other changes accompanying ventilation.

## Conditions

- lh7777 [[./thread#^c33313381|lh7777]] reports a \$60 SCD-30 sensor board connected to a Raspberry Pi Zero W, with Grafana charts. Their claimed cost advantage depends partly on already owning a Raspberry Pi. The practical tradeoff is reduced portability in exchange for access to historical trends over weeks or months.
- kkfx [[./thread#^c33328492|kkfx]] says their mechanical-ventilation vendor considers an optional CO2-controlled fan-speed module poor value, potentially saving only a few euros in electricity. This is a reported vendor assessment for that installation, without purchase-price details or measured savings.
- antisthenes [[./thread#^c33312956|antisthenes]] treats approximately 400 ppm as a contemporary outdoor floor while allowing occasional lower concentrations under particular conditions. kkfx [[./thread#^c33328492|kkfx]] emphasizes local variation. Neither supplies local outdoor measurements or a location sufficient to establish an appropriate geographic calibration baseline.

## Lived experiences

- D13Fd [[./thread#^c33312788|D13Fd]] reports their house settling around 1,500 ppm and the reading dropping rapidly when a bathroom exhaust fan on the other side of the house runs. In response to calibration criticism, D13Fd [[./thread#^c33316934|D13Fd]] says they used the device's outdoor-baseline self-calibration and observed noticeable air-quality changes. No independent calibration, numerical decay curve, or exchange duration is supplied.
- lh7777 [[./thread#^c33313381|lh7777]] identifies the gas oven as by far the largest CO2 source in their monitored home and signals an intention to retire it. This is a firsthand source observation, without the oven's numerical contribution or results after replacement. It does not establish NO2 or PM2.5 exposure.
- shashurup [[./thread#^c33313695|shashurup]] reports readings well below 400 ppm with a door open and approximately 800 ppm after two to three hours with both door and window closed. Their simultaneous description of 400 ppm as an apparent device lower limit is internally unclear. These readings prompted concern about accuracy before they accepted the device's behavior as reasonable.
- kkfx [[./thread#^c33315703|kkfx]] reports perceiving a difference in a modern home equipped with regulated mechanical ventilation, while lacking a way to calibrate sensors at home. The account does not specify a measured CO2 improvement, a particular symptom, or a controlled comparison.

## Unresolved disagreements

- The calibration exchange leaves unresolved both actual instrument accuracy and the accuracy needed for household decisions. tuatoru [[./thread#^c33315290|tuatoru]] demands stronger support for absolute readings; D13Fd [[./thread#^c33316934|D13Fd]] considers relative response sufficient for observing ventilation. gruez's baseline-calibration explanation [[./thread#^c33323821|gruez]] and kkfx's objection about local variation [[./thread#^c33328492|kkfx]] do not settle either question.
- The proposed connection between cabin CO2 and crashes remains unestablished. jodrellblank [[./thread#^c33313056|jodrellblank]] calls the cabin claims extraordinary and questions whether a quoted 10–30\% drowsiness share also applies to fatal crashes. Their tentative 4,000–12,000 annual deaths extrapolation is neither an observed CO2-attributable toll nor evidence that CO2 caused the drowsiness.
- The supplied accounts do not establish household effects on cognition, headaches, sleep quality, or quantified comfort. mshook's quoted simulator results [[./thread#^c33319199|mshook]] concern a particular performance setting, with insufficient methodological detail here to assess transfer to homes or cars. D13Fd [[./thread#^c33316934|D13Fd]] and kkfx [[./thread#^c33315703|kkfx]] provide subjective air-quality impressions without controlled health or sleep measurements.
- Window-opening benefits and exposure tradeoffs remain largely unanswered. D13Fd [[./thread#^c33312788|D13Fd]] tests an exhaust fan; shashurup [[./thread#^c33313695|shashurup]] changes both door and window closure; jodrellblank [[./thread#^c33313056|jodrellblank]] quotes a car-door opening. These accounts do not isolate opening a household window or establish when polluted outdoor air would make it undesirable. The unit supplies no PM2.5, NO2, wildfire-smoke, roadside-exhaust, or filtration measurements with which to compare that tradeoff.
