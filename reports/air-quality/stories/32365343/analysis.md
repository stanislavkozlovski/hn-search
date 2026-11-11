# [Measuring dust with a Dylos air quality monitor (2012)](https://news.ycombinator.com/item?id=32365343)

[[./thread|Discussion]]

## Description

Discussion compares an older particle monitor with newer low-cost laser-scattering sensors. Topics include sensor calibration, particle-size ranges, humidity effects, airflow and enclosure design, and the limits of low-cost readings as indicators rather than precise concentration measurements; participants also ask about suitable devices for fine dust.
Tags: air quality monitoring, particulate matter, sensors, calibration, DIY

## Relevance

The discussion focuses on particulate sensor capabilities and reliability, including calibration to particular dust types, humidity effects, airflow and enclosure design, and the limits of low-cost sensors for estimating absolute concentrations. It also relays measurement and comparison experience from sensor use. [[./thread#^c32365631|walterbell]] [[./thread#^c32376329|ahaucnx]] [[./thread#^c32376470|ahaucnx]] [[./thread#^c32376719|walterbell]] [[./thread#^c32378020|ahaucnx]] [[./thread#^c32381824|porknubbins]]

## Arguments

- Affordable sensors may help track changing particulate conditions. Writing in 2022, ahaucnx describes newer laser-scattering modules as reliable; walterbell quotes a review reporting that many inexpensive sensors can follow environmental PM changes. These comments support monitoring trends, with qualifications about absolute accuracy. [[./thread#^c32376329|ahaucnx]] [[./thread#^c32376719|walterbell]]
- walterbell quotes Dylos’s manufacturer claiming that its focused laser detects individual particles and estimates their size, providing small/large particle counts with greater resolution than simple air-cleaner indicator lights. This is a manufacturer’s explanation, not an independent comparison with the newer inexpensive laser sensors discussed by ahaucnx. [[./thread#^c32365631|walterbell]] [[./thread#^c32376329|ahaucnx]]
- ahaucnx proposes improving measurement quality through humidity compensation or preheating sampled air, and through PCB/enclosure designs that provide appropriate airflow and prevent internal heat from biasing temperature readings. The discussion supplies no quantified before-and-after results for these measures. [[./thread#^c32376329|ahaucnx]] [[./thread#^c32378020|ahaucnx]]

## Counterarguments

- Factory calibration has contextual limits: ahaucnx says sensors may be calibrated for a particular dust, giving Arizona road dust as an example, so measuring another material such as wood dust can reduce accuracy. They also identify high humidity as a measurement influence. Their endorsement of sensor reliability therefore includes explicit qualifications. [[./thread#^c32376329|ahaucnx]]
- walterbell quotes a 2020 review of 50 sensors reporting R² values up to 0.99 under some conditions, but values below 0.5 without calibration against a reference in the operating environment. These are reported statistical results, not firsthand readings or proof of 99\% concentration accuracy. A second, 2021 paper excerpt cautions that inexpensive indoor PM readings should indicate changes or approximate concentrations. Both findings are presented through quoted excerpts, not independently examined studies. [[./thread#^c32376719|walterbell]]

## Assumptions

- ghostpepper explains choosing consumer temperature/humidity devices partly because they assumed these would offer more confidence in accuracy than bare components, distinguishing precision from accuracy. In reply, ahaucnx says their DIY-kit modules are factory calibrated. That addresses the calibration concern for those modules, but supplies no validation of ghostpepper’s installed devices or of consumer devices generally. [[./thread#^c32377424|ghostpepper]] [[./thread#^c32378020|ahaucnx]]
- ahaucnx explicitly presents as an opinion that many inexpensive sensors prioritize PM2.5 accuracy because standards emphasize PM2.5, despite some offering channels down to 0.3 microns. The discussion provides no size-by-size performance measurements establishing that explanation or the accuracy of the smaller-particle channels. [[./thread#^c32376470|ahaucnx]]

## Conditions

- ahaucnx reports a typical Plantower PMS5003 module price of USD 15–20, making component-level monitoring relatively accessible; this is not a complete monitor’s price. walterbell’s quoted Dylos marketing invokes \$8,000 clean-room counters as a technological comparison, without establishing comparable performance or providing the Dylos purchase price. No geographic comparison or maintenance-cost evidence is supplied. [[./thread#^c32376329|ahaucnx]] [[./thread#^c32365631|walterbell]]

## Lived experiences

- ahaucnx reports substantial use of Plantower PMS5003 modules in their organization’s open-source kits. Responding to ghostpepper, they say their DIY and commercial products use the same factory-calibrated modules, that the commercial monitor underwent RESET Air certification, and that side-by-side comparisons showed no accuracy differences. This is firsthand experience from someone involved in making the products; no reference instrument, numerical errors, test conditions, or exposure concentrations are reported. [[./thread#^c32376329|ahaucnx]] [[./thread#^c32378020|ahaucnx]]
- ghostpepper reports installing 433 MHz AcuRite temperature/humidity sensors and integrating them with Home Assistant. This is firsthand home-monitoring experience, but the comment reports uncertainty about calibration rather than measured sensor error, PM2.5 exposure, or health effects. [[./thread#^c32377424|ghostpepper]]

## Unresolved disagreements

- porknubbins directly questions why different dust materials require different calibration if particle sizes are measured in microns. No supplied reply explains the mechanism, leaving the distinction between particle size and material-dependent measurement accuracy unresolved within this discussion. [[./thread#^c32381824|porknubbins]] [[./thread#^c32376329|ahaucnx]]
- walterbell asks for a sensor covering approximately 0.5–2.5 microns, later connecting that need to metal- and wood-working dust in workshops and garages. ahaucnx mentions the Sensirion SPS30’s channels down to 0.3 microns, while walterbell concludes that only the Dylos Pro attempts the desired range among the options they examined. The exchange supplies no comparative measurements that settle which device accurately serves that workshop use case. [[./thread#^c32376425|walterbell]] [[./thread#^c32376470|ahaucnx]] [[./thread#^c32376719|walterbell]]
- There is an unresolved difference in evidentiary strength between ahaucnx’s confidence based on calibration, shared components, certification, and side-by-side agreement, and walterbell’s quoted warnings about indoor concentration accuracy. These claims can coexist: agreement between devices does not establish accuracy against a reference across dust types and humidity conditions. No common test resolves their applicability here. [[./thread#^c32378020|ahaucnx]] [[./thread#^c32376329|ahaucnx]] [[./thread#^c32376719|walterbell]]
- This source unit cannot answer the broader exposure and intervention questions. ahaucnx’s comparisons and ghostpepper’s installation provide no actual indoor-versus-outdoor PM2.5 concentrations or reported effects on health, cognition, sleep, or comfort. The supplied discussion contains no NO2 or CO2 evidence and no measured experiences comparing ventilation, filtration, cooking, traffic, wildfire smoke, or opening windows. Consequently, it establishes no circumstances in which opening windows improves or worsens personal exposure. [[./thread#^c32378020|ahaucnx]] [[./thread#^c32377424|ghostpepper]]
