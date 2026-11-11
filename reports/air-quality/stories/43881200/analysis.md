# [Show HN: Live Air Quality Monitor](https://news.ycombinator.com/item?id=43881200)

[[./thread|Discussion]]

## Description

Discussion compares a DIY ESP32 air quality monitor with existing projects and platforms, including ESPHome, Home Assistant, Prometheus, and AirGradient. Topics include claimed sensor capabilities and accuracy, relative price, whether a custom PCB is needed, and the tradeoff between tidy construction and the flexible placement possible with wired components.
Tags: DIY, air quality monitor, ESP32, sensors, Home Assistant

## Relevance

The project measures indoor CO2, VOCs, NOx, and particulate matter. The discussion compares sensor hardware and includes claims about component accuracy and sensing capability, though it provides no firsthand air-quality readings. [[./thread#^c43883019|sneak]] [[./thread#^c43884519|ssuds]] [[./thread#^c43896829|benbojangles]]

## Arguments

- benbojangles argues that the DIY monitor’s ESP32, SCD41, and SGP41 components provide newer technology, better accuracy, and additional VOC/NOx sensing compared with AirGradient. This is explicitly a specification-based comparison, without reported comparative measurements. [[./thread#^c43896829|benbojangles]]
- benbojangles presents control over sensor code and adjustment, remote monitoring, and compatibility with ESPHome as practical advantages. These are implementation claims rather than demonstrated improvements in personal air exposure. [[./thread#^c43885471|benbojangles]]
- benbojangles argues that a PCB avoids chaotic wiring and potential failure points; wkat4242 also acknowledges that a board makes construction cleaner. [[./thread#^c43885731|benbojangles]] [[./thread#^c43885682|wkat4242]]

## Counterarguments

- sneak questions whether a separate implementation is necessary, suggesting that ESPHome can perform the monitoring and feed Home Assistant or Prometheus without creating another web interface. benbojangles responds that this board could also use ESPHome. [[./thread#^c43883019|sneak]] [[./thread#^c43885471|benbojangles]]
- ssuds challenges the apparent distinction from AirGradient: following benbojangles’s price comparison, ssuds points out that AirGradient already has a basic DIY design that can be assembled without a PCB, and asks what missing functionality motivated this project. [[./thread#^c43884519|ssuds]] [[./thread#^c43885480|benbojangles]] [[./thread#^c43890493|ssuds]]
- wkat4242 argues that directly wiring the sensors can eliminate the need for a custom board. After acknowledging benbojangles’s reliability concern, wkat4242 emphasizes the resulting flexibility in sensor placement. [[./thread#^c43885682|wkat4242]] [[./thread#^c43885731|benbojangles]] [[./thread#^c43885756|wkat4242]]

## Assumptions

- benbojangles’s accuracy argument assumes that the selected components’ specifications translate into better performance in the assembled monitor. The comment supplies no calibration procedure, reference instrument, or side-by-side results establishing that inference. [[./thread#^c43896829|benbojangles]]
- benbojangles claims NOx sensing, not demonstrated NO2-specific concentration measurement. Treating that claim as evidence of reliable quantitative NO2 exposure monitoring would exceed what the comment establishes. [[./thread#^c43896829|benbojangles]]
- benbojangles presents monitoring beyond the local network as a differentiator, but the exchange with sneak does not establish that ESPHome-based alternatives lack remote access. [[./thread#^c43883019|sneak]] [[./thread#^c43885471|benbojangles]]

## Conditions

- benbojangles says the DIY board is roughly 150 cheaper than AirGradient, without specifying currency or the compared configuration. ssuds’s reminder that AirGradient also offers DIY construction leaves the equivalent-cost comparison uncertain. [[./thread#^c43885480|benbojangles]] [[./thread#^c43890493|ssuds]]
- wkat4242 describes Chinese PCB fabrication as inexpensive but tentatively qualifies that for US shipping. Component availability remains unspecified: Emmarof asks where parts were purchased, and benbojangles replies with a clarification question and 'YMMV' rather than supplier information. [[./thread#^c43885682|wkat4242]] [[./thread#^c43914212|Emmarof]] [[./thread#^c43915303|benbojangles]]

## Lived experiences

- wkat4242 reports building sensor boards using Dallas one-wire temperature sensors at different locations in central-heating systems and frequently using wires for one-off projects. This supports firsthand construction and placement experience, but provides no firsthand PM2.5, NO2, or CO2 measurements or associated health outcomes. [[./thread#^c43885682|wkat4242]] [[./thread#^c43885756|wkat4242]]

## Unresolved disagreements

- The balance between PCB reliability and wired placement flexibility remains unresolved. benbojangles identifies wires as failure points, while wkat4242 accepts the concern but values flexibility; neither supplies comparative failure data. [[./thread#^c43885731|benbojangles]] [[./thread#^c43885756|wkat4242]]
- Whether the project offers a meaningful accuracy or functionality advantage over existing DIY monitors remains unsettled: ssuds asks for the missing functionality, and benbojangles answers through component specifications rather than measured performance. [[./thread#^c43890493|ssuds]] [[./thread#^c43896829|benbojangles]]
- This unit cannot resolve the approved question’s exposure and outcome comparisons. benbojangles supplies hardware claims and wkat4242 supplies temperature-sensor construction experience; no supplied comment reports pollutant readings, health, cognition, sleep, or comfort effects, study findings, or experiences comparing ventilation, filtration, cooking, traffic, wildfire smoke, or opening windows. Consequently, it provides no evidence for when outdoor air would improve or worsen indoor exposure. [[./thread#^c43896829|benbojangles]] [[./thread#^c43885682|wkat4242]] [[./thread#^c43885756|wkat4242]]
