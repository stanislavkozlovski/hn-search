# [IKEA launches VINDSTYRKA – a smart sensor to measure indoor air quality](https://news.ycombinator.com/item?id=34796784)

[[./thread|Discussion]]

## Description

Discussion evaluates an IKEA indoor air quality sensor’s features, price, measurement reliability, calibration, and compatibility with smart home systems. Participants compare it with other monitors and discuss missing CO2 measurement, fan noise, and ways to integrate or modify devices for Home Assistant. A side thread debates brand quality and another examines whether a linked product URL is promotional.
Tags: air quality sensors, IKEA, smart home, Home Assistant, product evaluation

## Relevance

The discussion addresses indoor PM2.5 monitoring, missing CO2 measurement, sensor accuracy and recalibration, and firsthand readings during outdoor smoke and indoor cooking. It also notes usability tradeoffs such as fan noise. [[./thread#^c34797827|Tijdreiziger]] [[./thread#^c34797828|makeitdouble]] [[./thread#^c34798796|makeitdouble]] [[./thread#^c34799235|mc32]] [[./thread#^c34799646|mdmglr]] [[./thread#^c34801365|slaw]] [[./thread#^c34801961|wkat4242]]

## Arguments

- Participants want CO2 monitoring alongside other air measurements. makeitdouble regrets its omission from the announced IKEA device [[./thread#^c34797828|makeitdouble]], while starky reports disappointment that Amazon's monitor measures CO rather than the CO2 they wanted [[./thread#^c34800904|starky]]. These are feature preferences; neither commenter supplies CO2 measurements or associated health outcomes.
- Readable, accessible measurements matter for practical use: makeitdouble welcomes the screen and hub support [[./thread#^c34797828|makeitdouble]]; jerlam rejects Amazon's app-dependent data access [[./thread#^c34798490|jerlam]]; and Larrikin makes Home Assistant compatibility a purchase condition [[./thread#^c34798931|Larrikin]]. Their comments support usability and integration as selection criteria, without demonstrating improved air quality.
- makeitdouble sees the apparent lack of automatic control for IKEA's new purifier as a missed opportunity [[./thread#^c34797828|makeitdouble]]. This suggests interest in connecting monitoring to filtration, but the comment provides no test of automatic control, particle removal, or exposure reduction.

## Counterarguments

- Low readings alone do not establish sensor failure. Responding directly to slaw's concern about nearly constant readings of 002–003 [[./thread#^c34801365|slaw]], wkat4242 reports similarly low readings from a Xiaomi purifier that nevertheless responded strongly to a nearby fire [[./thread#^c34801961|wkat4242]]. That offers a plausible alternative explanation, but does not verify slaw's particular unit.
- Brand reputation is disputed as evidence of sensor quality. Am4TIfIsER0ppos extrapolates dissatisfaction with IKEA's wood and metal products to its electronics and software [[./thread#^c34798468|Am4TIfIsER0ppos]] [[./thread#^c34807160|Am4TIfIsER0ppos]]. makeitdouble acknowledges rough edges and personal investment in IKEA home automation [[./thread#^c34798839|makeitdouble]], but argues that quality across different product lines need not correlate [[./thread#^c34813215|makeitdouble]]. Neither position establishes this sensor's accuracy.

## Assumptions

- wkat4242 explicitly frames the idea that most fine dust comes from outdoors as a guess, while also reporting increases during frying and 3D printing [[./thread#^c34801961|wkat4242]]. The supplied observations do not quantify the relative contributions of outdoor infiltration and indoor sources.
- Agreement between consumer devices is implicitly reassuring, but does not establish absolute accuracy. makeitdouble explicitly calls the IKEA–Sharp comparison unscientific [[./thread#^c34798796|makeitdouble]], and wkat4242 reports similar Xiaomi and Awair trends without a calibrated reference [[./thread#^c34801961|wkat4242]] [[./thread#^c34808238|wkat4242]]. Shared trends can support event detection while leaving numerical accuracy unresolved.
- mc32 claims that most monitors need cleaning and recalibration through several minutes in clean air, especially after heavy pollution exposure [[./thread#^c34799235|mc32]]. No model-specific instructions or verification accompany that claim; this part does not establish it as a generally valid maintenance procedure.

## Conditions

- Affordability is discussed with different levels of certainty. Answering anigbrowl's request for pricing [[./thread#^c34796959|anigbrowl]], CharlesW reports a rumored price below \$50 for the new device and \$16 for the screenless model [[./thread#^c34798303|CharlesW]]. slaw reports actually paying \$24.99 for a Xiaomi PM2.5 sensor [[./thread#^c34801365|slaw]]. These are contemporaneous comments, not verified current prices.
- CO2 capability may increase cost: makeitdouble poses that explanation as a question [[./thread#^c34797828|makeitdouble]], and russianGuy83829 claims a decent CO2 sensor alone costs more than \$20 [[./thread#^c34805837|russianGuy83829]]. No manufacturer cost breakdown establishes why either discussed product omitted CO2.
- Integration can carry additional cost and effort. wkat4242 says the new device requires the more expensive Dirigera rather than the Tradfri hub despite both using Zigbee [[./thread#^c34801942|wkat4242]]. gedy links a modification for integrating the previous IKEA model with Home Assistant, explicitly describing it as suitable for technically inclined users [[./thread#^c34799552|gedy]]; that is not evidence of native support in the new model.
- Noise creates a usability tradeoff. In response to Tijdreiziger's complaint about the older sensor's cycling fan [[./thread#^c34797827|Tijdreiziger]], wkat4242 proposes constant fan power, optionally at 3.3 V rather than 5 V for quieter operation [[./thread#^c34799407|wkat4242]]. The supplied exchange contains no measured noise reduction or verification of sensing performance after that modification.
- The only specific outdoor-source distance is wkat4242's account of a bin fire about 100 metres away [[./thread#^c34801961|wkat4242]]. No city, region, season, window position, or ventilation arrangement is given, limiting geographic and building-specific conclusions.

## Lived experiences

- makeitdouble owns the previous IKEA colour-indicator monitor and regularly compares it with a Sharp purifier's display in the same room. They generally react together, with timing differences and substantial apparent airflow effects; the purifier seems steadier because it generates airflow. They have not seen the Sharp react dramatically while IKEA remains green, but explicitly disclaim a scientific comparison [[./thread#^c34798796|makeitdouble]].
- slaw reports buying a Xiaomi PM2.5 sensor that displays 002–003 consistently and expresses uncertainty about whether it works correctly [[./thread#^c34801365|slaw]]. A later reply confirms having bought and received the linked product [[./thread#^c34806029|slaw]]. The supplied account gives no units, reference measurement, or deliberate response test.
- wkat4242 reports that a Xiaomi purifier normally shows readings similar to slaw's low values, but jumped immediately to 200+ during a slight outdoor burning smell associated with a bin fire roughly 100 metres away, despite no visible smoke [[./thread#^c34801961|wkat4242]]. This is a firsthand report of sensor response; units and independently measured concentrations are absent.
- In the same household, wkat4242 reports that frying and 3D printing raise readings and that a second monitor follows the Xiaomi's graph fairly closely [[./thread#^c34801961|wkat4242]]. Their follow-up corrects that second device's name to Awair Lite [[./thread#^c34808238|wkat4242]]. No cooking fuel, printer material, peak values, or exposure durations are supplied.
- Tijdreiziger finds the previous VINDRIKTNING's audible fan repeatedly spinning up and down extremely distracting and often unplugs it [[./thread#^c34797827|Tijdreiziger]]. This directly documents discomfort and interrupted monitoring, but not sleep disruption or a physiological effect of polluted air.
- starky bought Amazon's monitor and reports dissatisfaction with both the app's presentation of data and its inclusion of CO instead of CO2. That experience prompted efforts to get an AirGradient working with Home Assistant [[./thread#^c34800904|starky]]. No comparative sensor readings or resulting exposure improvement are reported.

## Unresolved disagreements

- The announced VINDSTYRKA's measurement quality remains unestablished in this part. mdmglr asks which sensor IC it uses and questions calibration [[./thread#^c34799646|mdmglr]]; mc32 asks whether periodic recalibration will be needed and supported [[./thread#^c34797945|mc32]]. makeitdouble's reassuring comparison concerns the previous model, so it cannot resolve those questions about the new product [[./thread#^c34798796|makeitdouble]].
- Interoperability remains tentative. Tijdreiziger initially infers Zigbee and existing-hub compatibility [[./thread#^c34797827|Tijdreiziger]]; wkat4242 narrows official hub support and says third-party operation depends on the particular Zigbee stack [[./thread#^c34801942|wkat4242]] [[./thread#^c34810048|wkat4242]]. euroderf's Conbee/Matter question [[./thread#^c34809988|euroderf]] and tecleandor's tentative claim of Matter support [[./thread#^c34817860|tecleandor]] are not accompanied by successful installation reports.
- This source unit cannot establish effects of PM2.5, NO2, or CO2 on health, cognition, or sleep: it supplies no such outcome measurements or study discussion. CO2 appears as a missing feature and an unanswered recommendation request from makeitdouble and ralfd [[./thread#^c34797828|makeitdouble]] [[./thread#^c34809521|ralfd]]; NO2 measurements are absent. Tijdreiziger's distraction report concerns equipment noise rather than pollutant exposure [[./thread#^c34797827|Tijdreiziger]].
- The window-opening and ventilation tradeoff remains untested. wkat4242's outdoor-fire and indoor-source observations identify circumstances in which particulate readings rose, but do not compare open versus closed windows, ventilation rates, filtration settings, or CO2 changes [[./thread#^c34801961|wkat4242]]. makeitdouble discusses purifier automation without removal measurements [[./thread#^c34797828|makeitdouble]]. This part therefore supplies no tested window strategy, traffic-exposure comparison, or wildfire account; the reported fire was a nearby bin fire.
