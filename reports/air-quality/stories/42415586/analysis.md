# [How Accurate Is the Sensirion SGP41 TVOC Sensor?](https://news.ycombinator.com/item?id=42415586)

[[./thread|Discussion]]

## Description

Discussion weighs the limits of low-cost TVOC sensors: they react to many unrelated sources, can produce noisy readings, and cannot identify specific chemicals. Participants debate whether persistent changes from new furnishings are still useful signals, and note that dedicated VOC sensors are costly and that some devices estimate CO2 from TVOC rather than measuring it directly.
Tags: air quality sensors, TVOC, sensor accuracy, indoor air

## Relevance

The discussion covers VOC sensor accuracy, noisy readings, and whether TVOC measurements can identify actionable indoor air problems. It includes firsthand observations and conflicting views about the sensors’ usefulness. [[./thread#^c42424947|mkesper]] [[./thread#^c42424997|wkat4242]] [[./thread#^c42425055|macNchz]] [[./thread#^c42425093|ElectRabbit]] [[./thread#^c42425179|kayson]] [[./thread#^c42425292|GeoAtreides]] [[./thread#^c42425634|macNchz]] [[./thread#^c42426214|t0mas88]]

## Arguments

- GeoAtreides [[./thread#^c42425292|GeoAtreides]], replying to criticism of nonspecific TVOC readings, argues that these sensors can reveal departures from a room’s normal conditions. Their proposed diagnostic is whether readings return after airing: transient beer or flatulence spikes should clear, while emissions from new furniture, curtains, or toys should recur. This is a proposed interpretation, not a documented experiment.
- t0mas88 [[./thread#^c42426214|t0mas88]] argues that CO2 sensing can support automatic ventilation even when absolute accuracy is uncertain: relative levels and rates of change are useful for their control system. Their positive assessment concerns ventilation operation, not demonstrated improvements in health or cognition.
- wkat4242 [[./thread#^c42424997|wkat4242]] argues for distinguishing pollutants instead of treating TVOC as a complete safety indicator. They describe formaldehyde as a concerning component worth measuring separately and attribute emissions to inexpensive furniture and fabrics; no formaldehyde measurements accompany those claims.

## Counterarguments

- macNchz [[./thread#^c42425055|macNchz]] considers nonspecific TVOC sensing a net negative in home monitors because ordinary events produce prolonged spikes without revealing whether concerning chemicals are present. Responding directly to GeoAtreides’s proposed persistence test, macNchz [[./thread#^c42425634|macNchz]] says four years of noisy readings and shifting baselines have not made that distinction actionable.
- t0mas88 [[./thread#^c42426214|t0mas88]], despite finding their CO2 sensor useful for ventilation, calls TVOC sensors useless because of noise. This supports macNchz’s skepticism but supplies no separate TVOC dataset or controlled comparison.
- kayson [[./thread#^c42425179|kayson]] cites an AQMD VOC-sensor evaluation page and characterizes sensors as poor even into the thousand-dollar range. The evaluation results are not supplied, so this remains their summary and cannot establish the accuracy of every sensor type, including PM2.5 or NO2 instruments.

## Assumptions

- wkat4242 [[./thread#^c42424997|wkat4242]] says some devices report estimated CO2, or eCO2, derived from TVOC rather than measuring CO2 directly. They describe the underlying assumption as low TVOC indicating recently introduced fresh air and argue that TVOC and CO2 lack a direct relationship. The prompt contains no paired measurements testing that criticism.
- GeoAtreides’s [[./thread#^c42425292|GeoAtreides]] proposed airing test assumes that persistent emissions can be distinguished from transient events despite changing background sources. macNchz [[./thread#^c42425634|macNchz]] challenges that assumption with possible everyday confounders such as discarded banana peels or a loosely capped shampoo bottle; these are suggested explanations, not identified causes.
- djmips [[./thread#^c42426246|djmips]], replying to ElectRabbit’s report of hairspray-triggered peaks [[./thread#^c42425093|ElectRabbit]], speculates that hairspray is unhealthy. That reply raises a possible exposure concern but provides no identified chemical, dose, symptom, or evidence that the observed peaks indicate harmful exposure.

## Conditions

- wkat4242 [[./thread#^c42424997|wkat4242]] claims a TVOC sensor costs a few dollars while direct CO2 sensing costs about \$50. This claimed price difference helps explain the appeal of indirect estimates, but the figures are not verified prices or complete monitor costs.
- GeoAtreides [[./thread#^c42425292|GeoAtreides]] describes individual sensors for specific VOCs as expensive and cumbersome, presenting broad TVOC sensing as a practical compromise. kayson’s [[./thread#^c42425179|kayson]] criticism suggests that spending substantially more may still leave accuracy concerns, although neither commenter supplies a cost-versus-performance comparison.

## Lived experiences

- macNchz [[./thread#^c42425055|macNchz]] reports prolonged TVOC spikes after opening one beer or passing gas. They later describe four years of home use, substantial hour-to-hour variation, and anxiety from ambiguous readings [[./thread#^c42425634|macNchz]]. These are firsthand qualitative device observations and a reported emotional effect, without concentrations, calibration checks, or confirmed hazardous sources.
- ElectRabbit [[./thread#^c42425093|ElectRabbit]] reports that morning hairspray use peaks all sensors in their building. The account suggests a recurring response across devices, but gives no models, numerical readings, independent chemical measurements, or health outcomes.
- t0mas88 [[./thread#^c42426214|t0mas88]] reports using a Sensirion CO2 sensor for automatic home ventilation and says it works well. They explicitly remain unsure about the accuracy of its absolute readings; no CO2 concentrations, reference comparison, or before-and-after exposure measurements are provided.

## Unresolved disagreements

- The usefulness of TVOC trends remains disputed: GeoAtreides [[./thread#^c42425292|GeoAtreides]] sees actionable information in recurring deviations, while macNchz [[./thread#^c42425634|macNchz]] finds ordinary variability overwhelming and t0mas88 [[./thread#^c42426214|t0mas88]] rejects the data as too noisy. No controlled example establishes when persistence reliably identifies an actionable source.
- mkesper [[./thread#^c42424947|mkesper]] warns that some monitors display TVOC or formaldehyde while actually measuring CO2. wkat4242 [[./thread#^c42424997|wkat4242]] explicitly corrects the claimed direction, saying cheap TVOC measurements instead generate estimated CO2. No product documentation is supplied to verify particular devices; wkat4242’s further claims about direct-sensing mechanisms also remain unverified here.
- Opening windows cannot be evaluated comprehensively from this unit. GeoAtreides [[./thread#^c42425292|GeoAtreides]] proposes airing as a way to clear transient VOC spikes, and t0mas88 [[./thread#^c42426214|t0mas88]] reports useful automatic ventilation, but neither provides indoor-versus-outdoor measurements. There is no supplied evidence on PM2.5, NO2, traffic, wildfire smoke, cooking, or filtration, so this discussion cannot establish when outdoor air would improve or worsen exposure.
- Health and functional outcomes remain largely unmeasured. macNchz [[./thread#^c42425634|macNchz]] reports anxiety about ambiguous readings, while djmips [[./thread#^c42426246|djmips]] offers a hairspray-health suspicion and wkat4242 [[./thread#^c42424997|wkat4242]] makes hazard claims about formaldehyde. None supplies clinical outcomes, cognition or sleep measurements, physical-comfort comparisons, or a health-study result establishing effects at the reported exposures.
