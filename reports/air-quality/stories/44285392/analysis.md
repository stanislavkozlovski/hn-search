# [Real-time CO2 monitoring without batteries or external power](https://news.ycombinator.com/item?id=44285392)

[[./thread|Discussion]]

## Description

Discussion examines a vibration-powered CO2 monitor, asking what makes the energy-harvesting system useful and whether its power output can support sensor operation and wireless reporting. Participants question sensor accuracy and longevity, compare readings with powered units, consider passive chemical indicators, and branch into indoor air quality, CO2 exposure, and climate monitoring.
Tags: CO2 monitoring, energy harvesting, sensors, measurement accuracy, indoor air quality, environmental monitoring

## Relevance

The discussion examines CO2 sensor accuracy and reliability, including disagreement about expected measurement error. It also raises indoor CO2 levels, possible cognitive effects, and using monitoring to decide when to ventilate; several health statements are claims about research rather than firsthand evidence. [[./thread#^c44286538|dfex]] [[./thread#^c44288391|callmemclovin]] [[./thread#^c44288716|devmor]] [[./thread#^c44288802|ChemSpider]] [[./thread#^c44289481|rkrisztian]] [[./thread#^c44289704|nashashmi]] [[./thread#^c44290983|jobs\_throwaway]] [[./thread#^c44291103|ahaucnx]]

## Arguments

- nashashmi [[./thread#^c44289704|nashashmi]], replying to rkrisztian’s suggestion to open a window [[./thread#^c44289481|rkrisztian]], argues that CO2 monitoring tells occupants when ventilation is needed. They also propose monitoring industrial spaces where ventilation is difficult and readings could indicate when to leave. These are proposed uses, not firsthand accounts of improved exposure.
- tempodox [[./thread#^c44290786|tempodox]] quotes a system that harvests machinery or pipeline vibrations to power periodic CO2 measurements and wireless transmission. mschuster91 [[./thread#^c44289321|mschuster91]] identifies the claimed advance as operating from 0.5 mW of generation when sensors normally require low-single-digit milliwatts. nashashmi [[./thread#^c44288551|nashashmi]] likewise sees value in matching low-power monitoring to available energy sources.
- dfex [[./thread#^c44286538|dfex]] reports seeing a 30–50 ppm difference between adjacent DC-powered and vibration-powered units in the report’s graph. Their follow-up [[./thread#^c44287794|dfex]] emphasizes that one consistently reads higher. This is an observation about published measurements, not a bench experiment conducted by the commenter.
- devmor [[./thread#^c44288716|devmor]] argues that a 50 ppm discrepancy is relatively minor for indoor monitoring, asserting an indoor range of 400–1000 ppm and adverse mental effects near 2000 ppm. The distinction between outdoor background concentrations and indoor exposure is relevant, but the ranges and health threshold are commenter claims.

## Counterarguments

- callmemclovin [[./thread#^c44288391|callmemclovin]] says the 30–50 ppm discrepancy is within ordinary sensor accuracy, citing the Sensirion SCD40 specification of “±50.0 ppm ±5.0 \%m.v.” freeone3000 [[./thread#^c44289469|freeone3000]] adds that sensor error can be consistently biased. zipping1549 [[./thread#^c44286980|zipping1549]] reports that the article calls performance comparable to the DC-powered unit, but explicitly guesses that a difference below 100 ppm is acceptable.
- jtrueb [[./thread#^c44289513|jtrueb]] challenges the assumption that nominal accuracy applies: power must remain stable and within specifications long enough. They describe the graph as a segment two hours into discontinuous collection, cite a 3.6 V maximum for the nRF52832, and suspect variable supply voltage. The comment proposes an explanation without demonstrating that voltage caused the offset.
- jobs\_throwaway [[./thread#^c44290983|jobs\_throwaway]] disputes devmor’s approximately 2000 ppm cognition threshold [[./thread#^c44288716|devmor]], claiming impairment starts at 1000 ppm and linking a paper. This is a claim about research, not a personal symptom report or an independently checked result in the supplied material.
- nikolayasdf123 [[./thread#^c44286484|nikolayasdf123]] questions the breakthrough framing because vibration-powered generation and CO2 monitoring already exist. mschuster91’s response [[./thread#^c44289321|mschuster91]] locates the novelty in the combination’s power requirements, leaving a distinction between familiar components and potentially useful integration.
- ChemSpider [[./thread#^c44288802|ChemSpider]], replying to enthusiasm for low-power monitoring, argues that sensor accuracy and service life matter more than electronics alone. They claim low-power chemical sensors lasting weeks or months are easy to make but generally impractical, and say critical specifications are missing. nradov [[./thread#^c44291196|nradov]] counters that replacement every few weeks can be practical in applications such as life support.
- Gravityloss [[./thread#^c44288611|Gravityloss]] proposes a passive, color-changing chemical indicator, while supportengineer [[./thread#^c44291366|supportengineer]] hopes for a mechanical device requiring no electricity. mschuster91 [[./thread#^c44289303|mschuster91]] objects that such chemical indicators respond to substances besides CO2 and speculates that rapid-test-style alternatives would not be reversible. These are design suggestions and objections, not demonstrated alternatives.

## Assumptions

- The accuracy discussion relies on evidence that should remain distinct: dfex [[./thread#^c44286538|dfex]] interprets a published graph, callmemclovin [[./thread#^c44288391|callmemclovin]] supplies a specification for an example sensor, and zipping1549 [[./thread#^c44286980|zipping1549]] relays the article’s comparison. These comments do not establish that the example specification applies to the prototype or independently validate its measurements.
- Battery-free operation assumes a suitable source of mechanical vibration. tempodox’s quoted description [[./thread#^c44290786|tempodox]] specifies industrial equipment or pipelines and periodic measurements; it does not establish continuous monitoring or reliable operation in an ordinary quiet bedroom or office.
- Indoor deployment is an extrapolated application in this discussion. rkrisztian [[./thread#^c44290731|rkrisztian]] [[./thread#^c44316236|rkrisztian]] objects that indoor monitoring was outside the article’s stated purpose, whereas nashashmi [[./thread#^c44294578|nashashmi]] [[./thread#^c44311819|nashashmi]] argues that the device can serve multiple purposes. Neither position supplies an indoor deployment result.

## Conditions


## Lived experiences

- ahaucnx [[./thread#^c44291103|ahaucnx]], replying to the nominal-accuracy explanation, reports conducting substantial testing against reference-grade sensors and usually finding very good performance and reproducibility, especially with optical NDIR sensors. This is firsthand testing experience, but the supplied comment contains no numerical errors, sample sizes, or protocol and does not establish the vibration-powered prototype’s accuracy.

## Unresolved disagreements

- The cause and practical importance of the consistent 30–50 ppm offset remain unresolved. dfex [[./thread#^c44286538|dfex]] [[./thread#^c44287794|dfex]] finds it concerning; callmemclovin [[./thread#^c44288391|callmemclovin]] and freeone3000 [[./thread#^c44289469|freeone3000]] consider it compatible with ordinary accuracy and bias; jtrueb [[./thread#^c44289513|jtrueb]] suspects power instability. No supplied calibration or electrical test distinguishes these explanations.
- The cognition discussion does not establish a universal impairment threshold. After jobs\_throwaway’s 1000 ppm claim [[./thread#^c44290983|jobs\_throwaway]], devmor [[./thread#^c44301097|devmor]] asks whether the linked paper actually shows increased task focus at 1000 versus 600 ppm. That question receives no supplied answer, leaving both the threshold and interpretation of particular cognitive outcomes unsettled.
- Long-term usefulness remains uncertain because the discussion provides no established prototype service life or sustained accuracy. ChemSpider [[./thread#^c44288802|ChemSpider]] treats those omissions as central, while nradov [[./thread#^c44291196|nradov]] shows that acceptable replacement frequency depends on the application rather than a universal practicality standard.
- The window-opening exchange does not demonstrate when ventilation improves overall exposure. rkrisztian [[./thread#^c44289481|rkrisztian]] proposes opening a window, and nashashmi [[./thread#^c44289704|nashashmi]] proposes using CO2 readings to time action, but neither supplies before-and-after measurements or outdoor pollution conditions. This unit therefore cannot resolve when opening windows would reduce CO2 while worsening PM2.5, NO2, or smoke exposure.
- The supplied exposure discussion concerns cognition claims from devmor [[./thread#^c44288716|devmor]] and jobs\_throwaway [[./thread#^c44290983|jobs\_throwaway]], alongside proposed ventilation uses from nashashmi [[./thread#^c44289704|nashashmi]]. It contains no firsthand health, sleep, or comfort outcomes; PM2.5 or NO2 measurements; or experiences comparing filtration, cooking, traffic, and wildfire smoke. Those parts of the approved question remain unsupported by this source unit.
