# [Add \$4 WiFi Logging to IKEA’s \$12 Air Quality Sensor (Wemos and Vindriktning)](https://news.ycombinator.com/item?id=36282294)

[[./thread|Discussion]]

## Description

Discussion covers adding Wi-Fi logging to IKEA's particle sensor and alternatives such as newer Matter devices, ESPHome, and Tasmota. Participants compare local and cloud-free smart-home integration, Home Assistant usability, sensor noise and capability, and consumer CO2 monitors, including the distinction between true NDIR readings and estimated CO2 values.
Tags: air-quality sensors, DIY electronics, ESPHome, Matter, Home Assistant, CO2 monitoring

## Relevance

The discussion covers a PM2.5 sensor’s noise and possible accuracy tradeoff, the distinction between true NDIR CO2 sensing and estimated readings, and firsthand use of CO2 monitors to guide window opening. It also notes that outdoor pollution or wildfire smoke can make additional outside air undesirable. [[./thread#^c36283060|xgbi]] [[./thread#^c36283212|Mutlut]] [[./thread#^c36283463|eric-hu]] [[./thread#^c36284124|crazygringo]] [[./thread#^c36291873|lathiat]] [[./thread#^c36466399|Mutlut]]

## Arguments

- Mutlut [[./thread#^c36283212|Mutlut]] argues that CO2 monitoring adds something the IKEA particle sensor lacks: a visible prompt to ventilate. Their reported benefit is a lasting change in window-opening habits; they do not report measured improvements in health, cognition, or sleep.
- crazygringo [[./thread#^c36284124|crazygringo]] recommends turning on an air purifier when indoor particulate readings rise. This is practical advice, without accompanying before-and-after measurements or evidence about a particular purifier.
- Commenters describe ways to make monitoring easier to maintain: PaulBGD\_ [[./thread#^c36283183|PaulBGD\_]] recommends ESPHome and network firmware updates, while tga [[./thread#^c36285041|tga]] recommends Tasmota for standalone operation with a web interface. In response to vardump's cloud-dependence concern [[./thread#^c36284426|vardump]], omnicognate [[./thread#^c36284555|omnicognate]] says Matter requires cloud-free operation, and cassianoleal [[./thread#^c36284663|cassianoleal]] quotes support for local operation during internet outages. These concern monitoring infrastructure, not measurement accuracy.

## Counterarguments

- Opening windows or increasing outdoor-air intake is not presented as universally beneficial. Replying to quickthrowman's proposed PM-triggered exhaust and filtered-intake sequence [[./thread#^c36283235|quickthrowman]], crazygringo [[./thread#^c36284124|crazygringo]] warns against increasing outside air when pollution or wildfire smoke causes elevated readings. The reply does not assess whether the proposed intake filtration would adequately address that exposure.
- A cheap device advertised as measuring CO2 may not measure it directly: lathiat [[./thread#^c36291873|lathiat]] warns that some derive an estimate from VOC readings and recommends checking for an NDIR sensor. However, their claim that most NDIR devices cost \$100 or more has a specific counterexample: Mutlut [[./thread#^c36466399|Mutlut]] identifies their approximately \$60 model as NDIR. Mutlut also says it measures only CO2, limiting crazygringo's earlier suggestion that such devices usually include PM2.5 sensing [[./thread#^c36284070|crazygringo]].
- Noise claims conflict. shrx [[./thread#^c36284142|shrx]] reports that the newer Vindstyrka is silent, while Havoc [[./thread#^c36299854|Havoc]] objects that a device containing a small fan cannot be silent. Neither supplies sound measurements; perceived silence and literal absence of sound remain different possible standards.

## Assumptions

- Claims about common components and price premiums are not demonstrated. parhamn [[./thread#^c36283748|parhamn]] says the component parts of these monitors are broadly similar, and crazygringo [[./thread#^c36285214|crazygringo]] characterizes the Awair Element as essentially a \$60 sensor with additional WiFi and phone integration. Neither provides a component comparison establishing equivalent sensing performance.
- NDIR identification is treated as an important purchasing criterion, but this thread does not establish a particular device's accuracy merely from that label. lathiat [[./thread#^c36291873|lathiat]] recommends the technology; AirGradient project maintainer ahaucnx [[./thread#^c36286635|ahaucnx]] describes their kits' Senseair NDIR sensor as high quality. The latter is a supplier-associated recommendation, without calibration results or an independent comparison.

## Conditions

- The approximately \$60 recommendation concerns a CO2-only device: Mutlut [[./thread#^c36466399|Mutlut]] says their NDIR model measures nothing else and suggests that obtaining both CO2 and particulate measurements may require \$100 or more. These are June 2023 price reports, not a demonstrated universal price floor.
- Awair pricing varies substantially within the discussion. eric-hu [[./thread#^c36284531|eric-hu]] reports listings at \$230 on Walmart and \$275 on Amazon; crazygringo [[./thread#^c36285214|crazygringo]] reports a direct-site promotional price of about \$157, discounted from \$209. Even the discounted connected monitor costs considerably more than Mutlut's suggested \$60 budget [[./thread#^c36283212|Mutlut]].
- Other quoted options involve different capabilities and costs. lathiat [[./thread#^c36283114|lathiat]] describes a roughly US\$50 newer IKEA model as Matter capable; ck2 [[./thread#^c36283206|ck2]] identifies it as Vindstyrka, and shrx [[./thread#^c36284142|shrx]] reports built-in Zigbee. abawany [[./thread#^c36284647|abawany]] recommends the approximately US\$100 Netatmo Indoor Air Quality Monitor, listing CO2, humidity, temperature, and noise monitoring. These comments do not establish that the products measure an identical set of pollutants.

## Lived experiences

- Mutlut [[./thread#^c36283212|Mutlut]] says CO2 monitoring made them more aware of ventilation and that the resulting window-opening habit persisted for years. They identify their device as the TFA Dostmann AirControl Mini 31.5006 and say they bought a second one a year later [[./thread#^c36284695|Mutlut]]. No CO2 concentrations, window-opening durations, or paired outdoor readings accompany the account.
- xgbi [[./thread#^c36283060|xgbi]] reports completing the IKEA WiFi modification easily with components and solder and integrating it successfully with Home Assistant. Their main complaint is noticeable noise. They also say the sound mode reduces accuracy, linking an issue discussion, but provide no numerical accuracy comparison in the supplied comment.
- Awair owners report satisfaction with usability: parhamn [[./thread#^c36283748|parhamn]] says their Element has been fine, and crazygringo [[./thread#^c36284087|crazygringo]] praises its appearance, phone history, and alerts. abawany [[./thread#^c36284647|abawany]] similarly praises Netatmo's app and web data access. These are favorable product experiences rather than validation against reference instruments.
- The effort required to sustain a monitoring setup varies between accounts. Replying under xgbi's Home Assistant experience, lannisterstark [[./thread#^c36286842|lannisterstark]] describes frustrating YAML configuration; vGPU [[./thread#^c36287153|vGPU]] reports roughly a year of trouble-free use except for migration after a Zigbee stick failed. Larrikin [[./thread#^c36287295|Larrikin]] suggests programming-language alternatives while acknowledging that YAML cannot be entirely avoided.

## Unresolved disagreements

- Actual measurement performance remains unestablished: this unit supplies no numerical PM2.5 or CO2 readings, reference-instrument comparisons, or quantified calibration errors. xgbi's accuracy concern [[./thread#^c36283060|xgbi]], lathiat's warning about VOC-derived CO2 estimates [[./thread#^c36291873|lathiat]], and Mutlut's NDIR specification correction [[./thread#^c36466399|Mutlut]] identify issues to distinguish, but do not quantify device performance.
- The account does not resolve the CO2-versus-outdoor-pollution ventilation tradeoff in a measured setting. Mutlut [[./thread#^c36283212|Mutlut]] reports sustained window opening, while crazygringo [[./thread#^c36284124|crazygringo]] warns about polluted or smoke-filled outdoor air. Neither provides paired indoor/outdoor measurements, geographic circumstances, or a tested rule for deciding when opening windows helps overall exposure.
- Evidence about health, cognition, sleep, NO2, cooking, and traffic is absent from this unit. The relevant firsthand outcomes are ventilation awareness from Mutlut [[./thread#^c36283212|Mutlut]] and monitor noise from xgbi [[./thread#^c36283060|xgbi]]; crazygringo's wildfire reference [[./thread#^c36284124|crazygringo]] is advice about a possible situation, not a firsthand wildfire account. These comments cannot establish physiological benefits or harms.
- Practical detection and automation questions remain open. quickthrowman [[./thread#^c36283235|quickthrowman]] asks whether people use PM2.5 readings for active ventilation control or merely logging; no tested setpoints, intake-filter performance, or control results are supplied. deepspace [[./thread#^c36299087|deepspace]] asks whether the IKEA sensor detects cigarette smoke and whether inexpensive smoking or vaping detection is available, with no answer in this export.
