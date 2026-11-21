# [How Accurate Is the Sensirion SGP41 TVOC Sensor?](https://news.ycombinator.com/item?id=42415586)

Article: [https://www.airgradient.com/blog/accuracy-sensirion-sgp41/](<https://www.airgradient.com/blog/accuracy-sensirion-sgp41/>)

ahaucnx · 2024-12-14 08:39 UTC · 9 reported comments · archived 2026-11-08 13:41 UTC
Observation: 2026-11-08 13:41 UTC → 2026-11-08 13:41 UTC

## Comments

- **macNchz** · [2024-12-15 18:34 UTC](https://news.ycombinator.com/item?id=42425055)
  As the post discusses, being unable to differentiate between the specific VOCs being detected makes these sensors, IMO, a net negative in home air quality devices. Mine will spike for a long time from opening a single beer or a fart (lol), so it doesn’t provide much information about whether there are concerning chemicals present as well. ^c42425055

  - **GeoAtreides** · [2024-12-15 19:12 UTC](https://news.ycombinator.com/item?id=42425292)
    the alternative to tVOC sensors are specific sensors for each VOC, which are expensive and cumbersome. ^c42425292

    Sensors like the Bosch BME680/8, or the Sensirion SGP41 are useful for detecting changes to the norm, and persistent changes to the norm. The fart or the beer spike will be not come back after airing the room, but the spikes from new chinese toys, new (ikea) furniture, new curtains, will be back immediately.

    - **macNchz** · [2024-12-15 20:10 UTC](https://news.ycombinator.com/item?id=42425634)
      I don’t know, having had one in my home for four years I don’t think I’d really be able to tell if I bought some bad furniture or something, there’s just so much noise. The levels are all over the map hour to hour. Could be some banana peels in the kitchen garbage or a loosely capped bottle of shampoo or something? Noisy data with a shifting baseline telling you that you *might* be exposed to some kind of nasty stuff is more just anxiety provoking than actionable, in my opinion. ^c42425634

  - **ElectRabbit** · [2024-12-15 18:40 UTC](https://news.ycombinator.com/item?id=42425093)
    They hate hairspray too. Lol. ^c42425093

    Peaks out all sensors in my building in the morning.

    - **djmips** · [2024-12-15 21:54 UTC](https://news.ycombinator.com/item?id=42426246)
      I bet hairspray isn't good for you. ^c42426246

- **kayson** · [2024-12-15 18:53 UTC](https://news.ycombinator.com/item?id=42425179)
  AQMD \[1\] has a lot of great information about air quality sensors. Turns out that they're all pretty bad up to the thousand dollar range. ^c42425179

  1\. [http://www.aqmd.gov/aq-spec/evaluations/voc/summary](<http://www.aqmd.gov/aq-spec/evaluations/voc/summary>)

- **mkesper** · [2024-12-15 18:17 UTC](https://news.ycombinator.com/item?id=42424947)
  And these are one of the more reliable sensors. Be aware of other sensors that print out a TVOC or even HCHO (formaldehyde) value but really only measure CO2. ^c42424947

  - **wkat4242** · [2024-12-15 18:24 UTC](https://news.ycombinator.com/item?id=42424997)
    Uh no it's the opposite. Measuring TVOC is really cheap, a couple bucks for a sensor. Measuring CO2 directly is really expensive (about 50 bucks) using either lasers (still the most accurate method) or a complex ultrasound method that Sensirion pioneered. ^c42424997

    What is happening is that some CO2 sensors are actually "eCO2" (estimated CO2) and estimate the value based on the TVOC. Which is really just a guesstimate because the two have no direct relation. It's just a presumption that low TVOC means that fresh air has recently entered.

    And formaldehyde is a subset of TVOC. It makes sense to measure it separately because it is emitted a lot by cheap furniture and fabrics and is one of the more dangerous compounds. TVOC sensors also react super heavily to alcohol so just spraying a bit of perfume causes it to jump skyhigh for hours.

    - **t0mas88** · [2024-12-15 21:48 UTC](https://news.ycombinator.com/item?id=42426214)
      I use a Sensirion CO2 sensor for automatic home ventilation. It works well, because ventilation is more about the relative levels of CO2 and rate of change. I'm not sure the exact value as reported by the sensor is very accurate. ^c42426214

      TVOC sensors are indeed useless. They measure so much noise that you can't use the data for anything.

