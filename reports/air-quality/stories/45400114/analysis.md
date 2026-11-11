# [Measuring My DIY Air Purifier](https://news.ycombinator.com/item?id=45400114)

[[./thread|Discussion]]

## Description

Participants discuss what else to measure when evaluating a DIY air purifier, including particle decay with the purifier off and energy use relative to clean-air delivery. They compare box-fan and PC-fan designs, filter and fan costs, airflow, noise, and performance under different pollution levels, sharing examples from cooking and home setups.
Tags: DIY air purifier, air quality, PM2.5, energy efficiency, home ventilation

## Relevance

Comments discuss DIY purifier performance and power use, and one contributor describes household PM2.5 sensors and readings during cooking. [[./thread#^c45406024|polishdude20]] [[./thread#^c45410030|Rebelgecko]] [[./thread#^c45410820|jerlam]] [[./thread#^c45428808|BizarroLand]] [[./thread#^c45443876|odie5533]] [[./thread#^c45444010|londons\_explore]] [[./thread#^c45444036|BizarroLand]] [[./thread#^c45444131|londons\_explore]] [[./thread#^c45446161|cptskippy]] [[./thread#^c45446328|zbrozek]] [[./thread#^c45450307|homebrewer]]

## Arguments

- Rebelgecko [[./thread#^c45410030|Rebelgecko]] proposes clean-air delivery rate per watt (CADR/W) as a useful comparison, arguing that homemade purifiers can lag dedicated units in energy efficiency. This frames practical performance around both cleaning and operating cost; aesthetics are a separate, explicitly subjective consideration.
- jerlam [[./thread#^c45410820|jerlam]] distinguishes conventional Corsi–Rosenthal boxes from newer PC-fan builds, claiming the latter substantially outperform mainstream HEPA purifiers in energy efficiency. This is a claim supported by a linked review, whose measurements are not reproduced in the supplied evidence.
- londons\_explore [[./thread#^c45444131|londons\_explore]] proposes placing a case fan directly on a cylindrical filter and using a USB-C adapter with selectable 5/9/12 V settings for speed control. Running faster while cooking and quieter while sleeping offers a proposed cleaning–noise tradeoff, but the comment supplies no measured particle-removal results.

## Counterarguments

- homebrewer [[./thread#^c45450307|homebrewer]], replying directly to londons\_explore’s inexpensive single-fan recommendation [[./thread#^c45444010|londons\_explore]], disputes its adequacy under substantial winter pollution. Their stronger commercial purifier reportedly struggles even at maximum speed. This challenges the small-fan recommendation under their conditions, without establishing that every PC-fan purifier is inadequate.
- BizarroLand [[./thread#^c45444036|BizarroLand]] objects that a \$2 fan is not the complete system cost: multiple fans, power supply, and housing can add expense. londons\_explore [[./thread#^c45444131|londons\_explore]] replies that a cylindrical filter can support the fan without a housing, reducing assembly requirements; the filter and power components still remain part of the setup.

## Assumptions

- londons\_explore’s assertion that a \$2 case fan can filter a roomful of air in roughly an hour [[./thread#^c45444010|londons\_explore]] leaves room volume, filter characteristics, pollutant input, and the meaning of 'filter' unspecified. It is not a reported calibrated CADR measurement or demonstrated PM2.5 concentration reduction.
- Comparing energy efficiency requires a cleaning-performance denominator: zbrozek’s reported 6 W consumption [[./thread#^c45446328|zbrozek]] and odie5533’s impression of abundant airflow [[./thread#^c45443876|odie5533]] do not independently establish particle removal or CADR/W. Neither account provides a matched comparison against another purifier.
- Quiet operation is evidence about perceived comfort, not demonstrated sleep improvement. londons\_explore’s bedtime speed recommendation [[./thread#^c45444131|londons\_explore]] and odie5533’s favorable noise assessment [[./thread#^c45443876|odie5533]] include no measured sleep, cognition, or health outcomes.

## Conditions

- BizarroLand [[./thread#^c45428808|BizarroLand]] gives 60–85 W as the consumption range for common 20-inch box fans, depending on speed, and argues that a roughly \$25 purchase can cost more in electricity over time. Their stated 50–100\% electricity penalty lacks an explicit numerical comparator in the comment; runtime and electricity prices are also unspecified.
- BizarroLand [[./thread#^c45428808|BizarroLand]] uses a box-fan filter in a geodesic dome whose large open section occupies about half the home and reaches 18 feet high. They consider its circulation useful for that substantial space and suggest it might be excessive in a more typical home. This is a dwelling-specific judgment, without measured coverage or comparable room tests.

## Lived experiences

- cptskippy [[./thread#^c45446161|cptskippy]], responding to the request for a baseline decay rate, reports PM2.5 sensors beside the stove, in a bedroom above the kitchen, in an office above that bedroom, and in the garage. They link samples from cooking a multi-food meal on a gas stove and frying one breakfast egg, and identify a fan starting at 6:35:37. The supplied text contains no concentration values or readable traces, so the magnitude, movement between rooms, and fan effect cannot be assessed.
- homebrewer [[./thread#^c45450307|homebrewer]] reports that during winter, with windows and doors closed, a Xiaomi purifier at maximum speed barely keeps PM2.5 within '5-10 micrograms.' This is a firsthand concentration report, but the comment omits the volume denominator, sensor details, duration, and location. Their prediction that a PC fan would make essentially no difference is an inference rather than a reported comparison test.
- odie5533 [[./thread#^c45443876|odie5533]], replying under the discussion of newer PC-fan purifiers, reports owning a Luggable and liking its quietness and substantial perceived airflow. This supports satisfaction with noise and airflow in one installation, without quantitative air-quality evidence.
- zbrozek [[./thread#^c45446328|zbrozek]], replying to the energy-efficiency discussion, reports building around an inline duct fan operated at 10\% throttle and consuming 6 W. The comment does not specify how power was measured or provide filtered airflow, particle concentrations, or noise measurements.

## Unresolved disagreements

- polishdude20 [[./thread#^c45406024|polishdude20]] asks how quickly particles decay with the window closed and purifier off. cptskippy’s cooking examples [[./thread#^c45446161|cptskippy]] do not supply that controlled baseline in the available text. Consequently, the contribution of active filtration relative to unassisted decay remains unresolved.
- The adequacy of a tiny inexpensive fan remains contested between londons\_explore [[./thread#^c45444010|londons\_explore]] and homebrewer [[./thread#^c45450307|homebrewer]]. jerlam’s broader claim about newer PC-fan builds [[./thread#^c45410820|jerlam]] need not describe the same configuration. Without comparable filters, room sizes, pollution loads, and measured delivery rates, these accounts neither establish a universal winner nor necessarily contradict one another under identical conditions.
- Sensor reliability is unassessed. cptskippy [[./thread#^c45446161|cptskippy]] describes multiple PM2.5 sensors, while homebrewer [[./thread#^c45450307|homebrewer]] reports a concentration range, but neither supplies sensor models, calibration evidence, or reference comparisons. The export therefore cannot establish reading accuracy or comparability; missing validation does not itself show the readings are wrong.
- Whether opening windows helps or worsens exposure cannot be determined from polishdude20’s baseline question [[./thread#^c45406024|polishdude20]] or homebrewer’s closed-window winter account [[./thread#^c45450307|homebrewer]]: neither provides paired indoor/outdoor readings or a ventilation comparison. cptskippy’s gas-stove account [[./thread#^c45446161|cptskippy]] concerns PM2.5 monitoring and supplies no NO2 or CO2 measurements. These comments also provide no measured outdoor exposure or evidence attributing pollution to traffic or wildfire smoke.
