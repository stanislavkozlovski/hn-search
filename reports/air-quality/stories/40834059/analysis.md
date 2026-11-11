# [We Launched the Largest Real-Time Global CO2 Map](https://news.ycombinator.com/item?id=40834059)

[[./thread|Discussion]]

## Description

Discussion of a crowdsourced real-time map of outdoor CO2 measurements. Participants ask how the network differs from other sensor maps, how measurements and locations are handled, and how accurate low-cost sensors are. The thread covers automatic baseline calibration, interpreting local and daily CO2 variation, adding sensors, upgrade options, and recommended placement.
Tags: CO2-monitoring, crowdsourced-data, air-quality-map, sensor-accuracy, open-source-hardware, environmental-monitoring

## Relevance

The thread focuses on an outdoor CO2 sensor map, including placement, crowdsourced readings, natural local variation, baseline calibration, and disagreements between colocated sensors. The discussion explicitly cautions that low-cost measurements are not reference-grade and are better suited to observing patterns. [[./thread#^c40835457|stemlord]] [[./thread#^c40835553|ahaucnx]] [[./thread#^c40835574|aydyn]] [[./thread#^c40835610|ahaucnx]] [[./thread#^c40835648|t-writescode]] [[./thread#^c40835654|ahaucnx]] [[./thread#^c40836302|Angostura]] [[./thread#^c40836328|ahaucnx]]

## Arguments

- ahaucnx, identifying himself as Achim from AirGradient, argues that inexpensive outdoor CO2 monitoring can reveal useful patterns associated with traffic, wind and nearby sources. He explicitly says the measurements are not reference grade and recommends interpreting patterns rather than treating absolute concentrations as exact. His favorable sensor-test claim and speedboat example refer to linked material whose results are not supplied here [[./thread#^c40835510|ahaucnx]] [[./thread#^c40835610|ahaucnx]].
- Pollutant selection matters when interpreting the map. Following sturza’s map link, ahaucnx explains that the default display is PM2.5 and users must switch to CO2. Observations about the default map therefore cannot automatically be treated as observations about CO2 [[./thread#^c40836360|sturza]] [[./thread#^c40836366|ahaucnx]].

## Counterarguments

- mfrankpb initially challenges the map’s size by comparing sensor.community’s reported 12,236 active sensors with AirGradient’s 500, then explicitly retracts the comparison because sensor.community measures PM2.5. ahaucnx acknowledges that particulate networks such as PurpleAir are larger, while saying he knows no comparable CO2 map. The correction removes this particular objection; it does not independently verify the largest-CO2-map claim [[./thread#^c40835800|mfrankpb]] [[./thread#^c40835829|ahaucnx]].
- t-writescode questions whether automatic calibration around 400 ppm becomes increasingly inaccurate as atmospheric background rises, explicitly distinguishing precision from accuracy. ahaucnx agrees that the adjustment will probably need to increase and says this is easy to implement. The exchange acknowledges the concern without providing a revised target or implementation date [[./thread#^c40835648|t-writescode]] [[./thread#^c40835654|ahaucnx]].
- In response to stemlord’s question about whether a 702 ppm marker indicates a large local emitter, ahaucnx says elevated outdoor CO2 can arise from natural daily cycles, particularly nighttime plant emissions in rural settings. This challenges attribution from a single concentration reading; it does not establish the cause of that particular New Jersey reading [[./thread#^c40835457|stemlord]] [[./thread#^c40835553|ahaucnx]].

## Assumptions

- ahaucnx describes a default seven-day automatic calibration around 400 ppm that typically brings colocated modules close together. This approach implicitly depends on the calibration target being appropriate for the deployment. Agreement between instruments would not independently establish accuracy, especially alongside his description of background around 430 ppm and substantial local variation [[./thread#^c40835610|ahaucnx]] [[./thread#^c40835553|ahaucnx]].
- Attributing CO2 patterns to traffic, boats or other sources requires distinguishing those influences from wind and natural daily cycles. ahaucnx proposes incorporating wind direction and emission inventories, but the supplied comments do not demonstrate that attribution process. They also do not establish that a CO2 pattern quantifies accompanying PM2.5 or NO2 exposure [[./thread#^c40835610|ahaucnx]] [[./thread#^c40835553|ahaucnx]].

## Conditions

- Geographic coverage is uneven in the network t-writescode inspected: he describes excellent sensor.community coverage in Germany and parts of Europe, with almost nothing in the United States. This observation concerns sensor.community’s particulate network; it should not be transferred to AirGradient’s CO2 network or treated as evidence that poorly covered places have cleaner air [[./thread#^c40836158|t-writescode]] [[./thread#^c40835800|mfrankpb]].
- AirGradient participation involves purchasing an Open Air kit or assembled outdoor monitor and opting into public sharing; ahaucnx says the resulting data are freely available through an API. Users supply their own coordinates and may deliberately offset them for privacy, limiting the precision of map-based exposure or source-location inferences. No hardware prices are supplied [[./thread#^c40835553|ahaucnx]] [[./thread#^c40835610|ahaucnx]].
- For Angostura’s proposed London terraced-house and garden setting, ahaucnx recommends mounting at least 1.5 metres above ground, away from HVAC equipment and barbecue grills, and in permanent shade where possible. The stated purposes are reducing ground-dust influence, avoiding nearby sources and improving temperature readings. No comparison establishes whether the house wall or garden bottom is preferable [[./thread#^c40836302|Angostura]] [[./thread#^c40836328|ahaucnx]].
- traspler owns a June 2023 outdoor unit with two particulate modules and no CO2 measurement. ahaucnx says a purchased CO2 module can replace one particulate module, leaving that PM sensor spare. This offers an upgrade path with a hardware tradeoff, but the thread provides neither its price nor a report of a completed upgrade [[./thread#^c40836101|traspler]] [[./thread#^c40836124|ahaucnx]].

## Lived experiences

- aydyn reports placing sensors from two different companies side by side: sometimes their readings agree, but at the time of commenting they differ by 100 ppm. This is firsthand evidence of variable disagreement between instruments, not proof that either instrument is wrong by exactly 100 ppm. Models, calibration settings, location and a reference measurement are unspecified [[./thread#^c40835574|aydyn]].
- stemlord reports seeing a 702 ppm map marker in Moorestown Township, New Jersey, and asks whether its position is exact and whether it identifies substantial emissions. This is a map observation, not a personal exposure measurement or verified source investigation. His subsequent acceptance of ahaucnx’s explanation adds no independent measurement [[./thread#^c40835457|stemlord]] [[./thread#^c40852640|stemlord]].
- ahaucnx reports that his team has observed outdoor peaks up to 800 ppm, which he attributes to natural daily cycles involving nighttime plant emissions. This is an operator’s account of observations and their interpretation; the comment supplies no measurement series, locations or independent verification of that attribution [[./thread#^c40835553|ahaucnx]].

## Unresolved disagreements

- The absolute accuracy of these measurements remains unquantified in the supplied evidence. ahaucnx’s description of weekly calibration and favorable testing does not resolve aydyn’s particular 100 ppm discrepancy or establish which instrument is closer to reality. No reference comparisons, uncertainty bounds or reproduced test results are provided [[./thread#^c40835574|aydyn]] [[./thread#^c40835610|ahaucnx]].
- traspler’s separate question about a TVOC/NOx sensor’s physical compatibility remains unanswered: ahaucnx addresses only the CO2 upgrade. The mention of a NOx-capable module supplies no NO2 concentration, reliability assessment or evidence about personal NO2 exposure [[./thread#^c40836101|traspler]] [[./thread#^c40836124|ahaucnx]].
- grigio makes a sarcastic remark about apparently clean China and Ukraine, but supplies no readings, identified pollutant layer or technical explanation. Its implied objection to the map cannot be evaluated, and the comment does not establish air quality or residents’ exposures in either country [[./thread#^c40839948|grigio]].
- No supplied comment reports health, cognition, sleep or comfort outcomes attributable to air quality. aydyn’s firsthand report concerns instrument agreement, while ahaucnx’s cited testing concerns sensor performance. Neither supplies evidence of a health threshold or a measured benefit from changing exposure [[./thread#^c40835574|aydyn]] [[./thread#^c40835610|ahaucnx]].
- This source unit does not establish when opening windows helps or worsens exposure: it contains no identified indoor–outdoor comparison, numerical PM2.5 or NO2 readings, or intervention reports involving ventilation, filtration, cooking or wildfire smoke. ahaucnx’s references to HVAC equipment and grills concern sensor placement, while his outdoor CO2 observations establish variability without testing indoor consequences [[./thread#^c40836328|ahaucnx]] [[./thread#^c40835553|ahaucnx]].
