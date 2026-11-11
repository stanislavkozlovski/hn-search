# [Real-time air pollution map](https://news.ycombinator.com/item?id=18714777)

Article: [https://www.purpleair.com/map\#1/25/-30](<https://www.purpleair.com/map#1/25/-30>)

bookofjoe · 2018-12-19 10:55 UTC · 45 reported comments · archived 2026-11-08 10:56 UTC
Observation: 2026-11-08 10:56 UTC → 2026-11-08 10:56 UTC

## Comments

- **TeMPOraL** · [2018-12-22 10:27 UTC](https://news.ycombinator.com/item?id=18739984)
  I'm saddened by the balkanization of air monitoring space. This map shows few PurpleAir sensors in Poland, but there are in fact many more sensors like this in existence - some under a FOSS project Luftdaten\[0\], others operated by a particular local startup. I recently built a Luftdaten sensor myself (though I'm yet to connect it to the project map). I expect the situation in other countries to be similar. ^c18739984

  I wish all those air monitoring organizations and companies cooperated on a single map. This data really needs to be aggregated together.

  \--

  \[0\] - [https://luftdaten.info/](<https://luftdaten.info/>)

  - **toomuchtodo** · [2018-12-22 18:33 UTC](https://news.ycombinator.com/item?id=18741806)
    Could US users easily buy and deploy these sensors (EDIT: from Luftdaten, since my comment wasn't clear)? Or must one build them? ^c18741806

    - **TeMPOraL** · [2018-12-22 18:47 UTC](https://news.ycombinator.com/item?id=18741875)
      They should be able to easily build them, though someone's probably selling pre-assembled ones (my co-worker actually wanted to start doing this). ^c18741875

      Take a look at the BOM in assembly manual\[0\]. The basics are made from NodeMCU (ESP8266) and SDS011 Fine dust sensor, + optionally DHT22. Plus some pipes. It can be assembled without soldering; it's really a few minutes job.

      Firmware for ESP8266 is OSS. It's set by default to send data to the Luftdaten project, but unlike commercial solutions I've seen, it also allows you to get the data for yourself. I just set up InfluxDB on a Raspberry Pi and gave the sensor the URL to DB's API.

      Copying from my sensor's config page, current firmware has support for following sensors:


      ```
        SDS011 (fine dust sensor)
        Plantower PMS(1,3,5,6,7)003 (fine dust sensor)
        Honeywell fine dust sensor
        PPD42NS (fine dust sensor)
        DHT22 (temperature, humidity)
        HTU21D (temperature, humidity)
        BMP180 (temperature, pressure)
        BMP280 (temperature, pressure)
        BME280 (temperature, humidity, pressure)
        DS18B20 (temperature)
        GPS (NEO 6M)
      ```

      
      I assume it's not hard to fork the firmware and add support for other sensors if needed.

      Building this is a really easy quick project, or an afternoon project to do with your non-tech spouse / kid.

      \--

      EDIT: Testing the sensor indoors led me to discover that ultrasound air humidifiers can pretty efficiently atomize everything that's dissolved in the water you feed them. After seeing PM10 shooting up to 600μg/m³ every time we turned one on, I realized the manual isn't saying "please use distilled water" just to make the humidifier require less cleaning...

      \--

      \[0\] - [https://luftdaten.info/en/construction-manual/](<https://luftdaten.info/en/construction-manual/>)

    - **theptrk** · [2018-12-22 18:41 UTC](https://news.ycombinator.com/item?id=18741844)
      they sell them here [https://www.purpleair.com/sensors](<https://www.purpleair.com/sensors>) ^c18741844

      - **unknown** · [2018-12-22 18:44 UTC](https://news.ycombinator.com/item?id=18741860)
        [deleted] ^c18741860

  - **unicornporn** · [2018-12-22 17:59 UTC](https://news.ycombinator.com/item?id=18741654)
    [https://luftdaten.info/en/](<https://luftdaten.info/en/>) in English. ^c18741654

  - **unknown** · [2018-12-22 18:26 UTC](https://news.ycombinator.com/item?id=18741779)
    [deleted] ^c18741779

- **mschurig** · [2018-12-22 08:34 UTC](https://news.ycombinator.com/item?id=18739642)
  Huge project by the german open data community: [http://maps.luftdaten.info/\#4/44.54/7.52](<http://maps.luftdaten.info/#4/44.54/7.52>) ^c18739642

  - **unicornporn** · [2018-12-22 17:56 UTC](https://news.ycombinator.com/item?id=18741636)
    Available in range of locales. ^c18741636

    [https://luftdata.se/](<https://luftdata.se/>) for us swedes!

- **vackosar** · [2018-12-22 08:24 UTC](https://news.ycombinator.com/item?id=18739612)
  Isn't [http://aqicn.org](<http://aqicn.org>) better? It seems quite real time and uses more stations at least above The Czech Republic. ^c18739612

  - **simongray** · [2018-12-22 16:34 UTC](https://news.ycombinator.com/item?id=18741213)
    I used to use that when I lived in Beijing, but when it comes to visualisation, nothing beats this site:  [https://www.airvisual.com/earth](<https://www.airvisual.com/earth>) ^c18741213

    You don't really get a feel for how the clouds of pollution move around in the other maps.

    - **rsync** · [2018-12-22 17:53 UTC](https://news.ycombinator.com/item?id=18741621)
      "I used to use that when I lived in Beijing, but when it comes to visualisation, nothing beats this site: [https://www.airvisual.com/earth"](<https://www.airvisual.com/earth%22>) ^c18741621

      Which sensor network does that site get data from ?

      Also, as I look at this map today, what is going on just northeast of Mexico city ?

    - **gok** · [2018-12-22 17:18 UTC](https://news.ycombinator.com/item?id=18741442)
      Wow that's great! ^c18741442

  - **hedora** · [2018-12-22 16:34 UTC](https://news.ycombinator.com/item?id=18741217)
    It depends.  You can pay purple air a few hundred dollars for a weather station that measures particulate matter but not ozone, etc. ^c18741217

    The upshot is that in most cities in the US, purple air has much denser coverage.

    For instance, Silicon Valley has \~4 government sensors, and one is shutting down.  It has hundreds of purple air sensors.  This makes a huge difference if you are trying to flee from wildfire smoke.

  - **angled** · [2018-12-22 10:22 UTC](https://news.ycombinator.com/item?id=18739971)
    By far better, with greater coverage. ^c18739971

- **minimaxir** · [2018-12-22 05:03 UTC](https://news.ycombinator.com/item?id=18739019)
  PurpleAir received a lot of notoriety during the California fires last month after the official AIRNow site ([https://airnow.gov/index.cfm?action\=airnow.local\_city&cityid...](<https://airnow.gov/index.cfm?action=airnow.local_city&cityid=317>)) crashed from the traffic. ^c18739019

  The AQIs given by default are higher than what's reported on the AIRNow; you'll have to apply a conversion in the bottom-left to get something closer.

  - **jonathankoren** · [2018-12-22 17:41 UTC](https://news.ycombinator.com/item?id=18741554)
    The AQIs reported by purple air are US EPA PM NowCast\[0\] AQIs for PM 2.5. NowCast, uses weighted averages over the past 12 hours of observations, rather than a simple arithmetic mean over the past 24 hour like the regular EPA AQI standard. NowCast was developed to be more sensitive to current conditions in order to help people make better immediate descisions about their health. The normal AQI standard was developed for long term air quality monitoring. ^c18741554

    The other thing that can effect the numbers is that AQIs are defined across a range of pollutants (usually PM 2.5, PM 10, CO, NO2, O3, and SO2) PurpleAir sensors only measure PM 2.5 and PM 10, but I think the numbers they show are only PM 2.5.

    \[0\] [https://en.wikipedia.org/wiki/NowCast\_(air\_quality\_index)](<https://en.wikipedia.org/wiki/NowCast_%28air_quality_index%29>)

- **clumsysmurf** · [2018-12-22 06:02 UTC](https://news.ycombinator.com/item?id=18739208)
  Since 2015 Google Street View cars have been driving around with Aclima air pollution sensors. The interesting thing, is that pollution varied greatly block to block with no obvious explanation. I think to get a good result, you need a sensor very close to you. ^c18739208

  - **londons\_explore** · [2018-12-22 09:59 UTC](https://news.ycombinator.com/item?id=18739920)
    Could it depend if the car was following a truck at the time? ^c18739920

    On my bicycle on London, I really notice the difference between busses with the tailpipe on the left or right side of the vehicle even.

    - **ndnxhs** · [2018-12-22 10:26 UTC](https://news.ycombinator.com/item?id=18739982)
      Absolutely. I always hold my breath and hit the brakes if a bus gets in front of me. Trucks aren't so bad as they have the exhaust pipe pointing right up in the air. Just the amount of traffic at the time makes a huge difference as well. At peak hour times I have breathing issues but other times its acceptable. ^c18739982

- **ryan\_j\_naughton** · [2018-12-22 05:27 UTC](https://news.ycombinator.com/item?id=18739098)
  One of these sensors is right outside my balcony (specifically one in West Los Angeles / Santa Monica). I set it up as part of a RAND Corporation study, and I've really enjoyed being able to get hyperlocal data. ^c18739098

  - **derrekl** · [2018-12-22 07:23 UTC](https://news.ycombinator.com/item?id=18739446)
    They still giving out sensors?  Not sure I live far enough away from you to merit another for the study, but worth an ask. ^c18739446

  - **swebs** · [2018-12-22 06:02 UTC](https://news.ycombinator.com/item?id=18739207)
    That area looks pretty rough regarding air quality. How is your health? ^c18739207

  - **heyjudy** · [2018-12-22 05:53 UTC](https://news.ycombinator.com/item?id=18739179)
    It's pretty awesome how they made a crowdsourced, for-profit, low-cost laser particle counter appliance. ^c18739179

- **pwarner** · [2018-12-22 05:32 UTC](https://news.ycombinator.com/item?id=18739116)
  It's sad how bad bay area air is at night.  Fireplaces seem fun, but really don't work in California valleys. ^c18739116

  - **ndnxhs** · [2018-12-22 07:19 UTC](https://news.ycombinator.com/item?id=18739430)
    I heard that industrial buildings crank up their pollution at night because people don't see it to complain about. ^c18739430

    - **clumsysmurf** · [2018-12-22 07:56 UTC](https://news.ycombinator.com/item?id=18739529)
      In the city here, I always see those trucks modified to vacuum debris from parking lots. They begin their "cleaning" thing around 12AM. They seem to just shoot the stuff right up into the air and make a huge mess. Not sure if they are supposed to work that way, or the machinery isn't being maintained, etc. ^c18739529

- **Jipazgqmnm** · [2018-12-22 10:58 UTC](https://news.ycombinator.com/item?id=18740057)
  The real time is a nice toy but all together to me it looks like a stripped down version of [https://earth.nullschool.net](<https://earth.nullschool.net>) ^c18740057

  E.g.: [https://earth.nullschool.net/\#current/particulates/surface/l...](<https://earth.nullschool.net/#current/particulates/surface/level/overlay=pm2.5/orthographic=-343.80,43.25,1182>)

  - **edge17** · [2018-12-22 16:50 UTC](https://news.ycombinator.com/item?id=18741294)
    that's wind data, not air pollution ^c18741294

    - **dredmorbius** · [2018-12-24 10:24 UTC](https://news.ycombinator.com/item?id=18751445)
      False. ^c18751445

      Nullschool's visualiser gives wind, yes, but also temperatures, ocean currents, wave heights, and numerous pollutants:  CO, CO2, SO4, and particulate matter.

      It's useful in tracking bushfire evolution, carbon emissions, and even sea lanes visible by the sulfer emissions due to high-sulfer bunker oil burnt by ships:

      [https://earth.nullschool.net/\#current/chem/surface/level/ove...](<https://earth.nullschool.net/#current/chem/surface/level/overlay=so2smass/orthographic=-14.41,-9.10,1345/loc=-18.561,-0.671>)

      [https://earth.nullschool.net/\#current/chem/surface/level/ove...](<https://earth.nullschool.net/#current/chem/surface/level/overlay=so2smass/orthographic=76.13,-1.70,1345/loc=-18.561,-0.671>)

      Also of volcanos:

      [https://earth.nullschool.net/\#current/chem/surface/level/ove...](<https://earth.nullschool.net/#current/chem/surface/level/overlay=so2smass/orthographic=203.11,16.62,2689/loc=-155.353,18.644>)

      There's history as well.  Here's CO emissions during the Camp fire, 10 November 2018:

      [https://earth.nullschool.net/\#2018/11/10/0900Z/chem/surface/...](<https://earth.nullschool.net/#2018/11/10/0900Z/chem/surface/level/overlay=cosc/orthographic=244.46,34.92,3000/loc=-120.915,36.821>)

      And PM2.5:

      [https://earth.nullschool.net/\#2018/11/10/0900Z/particulates/...](<https://earth.nullschool.net/#2018/11/10/0900Z/particulates/surface/level/overlay=pm2.5/orthographic=244.46,34.92,3000/loc=-120.915,36.821>)

- **abido** · [2018-12-25 07:09 UTC](https://news.ycombinator.com/item?id=18756385)
  There are a lot of community initiatives to measure and map air pollution data. They operate independently of each other because of known data quality issues that is characteristic of the low-cost sensors they use. However, would be great if there was an initiative to bring all these measurements in one platform. ^c18756385

  There is OpenAQ ([https://openaq.org/](<https://openaq.org/>)) that aggregates all publicly available air quality data from government and research-grade sources. They don't have the funds to aggregate low-cost sensor data, and one big reason is the poor data quality.

  You will see from the OpenAQ map that much of the world is without government monitoring of air quality.

  I live in one such country, and I run the Pakistan Air Quality Initiative ([http://twitter.com/pakairquality](<http://twitter.com/pakairquality>)) where we work with concerned citizens to monitor air quality in a number of major cities using the IQair AirVisual air quality monitors. Our data currently shows on the (www.airvisual.com)  website, but would be great to have the data available through an aggregation platform similar to OpenAQ

- **londons\_explore** · [2018-12-22 09:56 UTC](https://news.ycombinator.com/item?id=18739911)
  It uses a vector draggable openstreeetmap map...   Never knew that was a thing! ^c18739911

- **jonathankoren** · [2018-12-22 17:57 UTC](https://news.ycombinator.com/item?id=18741648)
  I have a weather station and use WeeWx\[0\] to monitor my Vantage2 Pro, and PurpleAir sensor using an extension\[1\]. ^c18741648

  I’ve been working on an my own extension\[2\] to calculate AQI values for various standards. Right now it supports six.

  \- Canada's Air Quality Health Index

  \- India's National Air Quality Index

  \- Mexico's Índice Metropolitano de la Calidad del Aire

  \- United Kingdom's Daily
   Air Quality Index

  \- United States's Air Quality Index

  \- United States's NowCast Air Quality Index

  I’m always looking to add more (The EU’s standard is high on my list.), and would welcome more people to use it.

  \[0\] [http://weewx.com/](<http://weewx.com/>)

  \[1\] [https://github.com/bakerkj/weewx-purpleair](<https://github.com/bakerkj/weewx-purpleair>)

  \[2\] [https://github.com/jonathankoren/weewx-aqi](<https://github.com/jonathankoren/weewx-aqi>)

- **etxm** · [2018-12-22 17:20 UTC](https://news.ycombinator.com/item?id=18741451)
  This is great. I’ve sworn since I’ve moved to Pasadena that the air has been much fresher than my last neighborhood. ^c18741451

  133 down to 53!

  I’ll have to take my lungs out for a drink to celebrate.

- **craigzucchini** · [2018-12-22 09:44 UTC](https://news.ycombinator.com/item?id=18739874)
  This is really really cool, but seems a little buggy in Firefox on my mac. Took quite a while for the clusters to show up, and then they went away after clicking on one and zooming back out. Would be great to see some more informative UI controls as well. Without existing knowledge, I'm not too sure what the drop box on the right hand side is for example. ^c18739874

  - **jonathankoren** · [2018-12-22 17:45 UTC](https://news.ycombinator.com/item?id=18741571)
    That’s just the PurpleAir site. It’s like that for all browsers for years. By how crappy it is, I think they’re naïvely trying to render ever sensor in the view window. ^c18741571

  - **ndnxhs** · [2018-12-22 09:57 UTC](https://news.ycombinator.com/item?id=18739913)
    For some reason the web gl map was failing to load and the alternative map was super laggy on my desktop. ^c18739913

  - **chris\_st** · [2018-12-22 14:29 UTC](https://news.ycombinator.com/item?id=18740694)
    Problems with Safari as well. ^c18740694

- **amelius** · [2018-12-22 14:36 UTC](https://news.ycombinator.com/item?id=18740723)
  There's also a satellite measuring pollution: ^c18740723

  [https://www.esa.int/Our\_Activities/Observing\_the\_Earth/Coper...](<https://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Sentinel-5P/Sentinel-5P_brings_air_pollution_into_focus>)

- **heyjudy** · [2018-12-22 05:52 UTC](https://news.ycombinator.com/item?id=18739173)
  I used PurpleAir maps during the Camp Fire; small particulates in east Chico were off the charts. ^c18739173

- **ronzensci** · [2018-12-22 09:31 UTC](https://news.ycombinator.com/item?id=18739829)
  Realtime PM2.5 monitoring in India can be seen here: [http://atmos.urbansciences.in/dashboard](<http://atmos.urbansciences.in/dashboard>) ^c18739829

  Many of these sensors are colocated with FEM/FRM grade BAM monitors.

- **fluxty** · [2018-12-22 12:59 UTC](https://news.ycombinator.com/item?id=18740391)
  This is pretty cool.  As a runner, I try to stay indoors when the weather is bad, but I also wonder if there are highly local pollution patterns related to traffic.  Ideally, you could identify something like that with a tool like this. ^c18740391

- **jonathankoren** · [2018-12-22 18:07 UTC](https://news.ycombinator.com/item?id=18741697)
  Does anyone know of an inexpensive sensor that measures other things than particulate matter? ^c18741697

  Once I got a PurpleAir, I started to want to measure ozone and other pollutants, but I haven’t found a sensor (or even sensor component) that measures that.

- **cboy5675** · [2018-12-22 09:25 UTC](https://news.ycombinator.com/item?id=18739796)
  What map is this using? No RTL support for right to left languages ^c18739796

- **afterburner** · [2018-12-22 09:23 UTC](https://news.ycombinator.com/item?id=18739789)
  197 in New Haven, CT. Next to a factory or something? ^c18739789

- **black-tea** · [2018-12-22 08:57 UTC](https://news.ycombinator.com/item?id=18739723)
  I'm surprised that the UK is all green even in London. I'd like to set one of these up near a busy road that connects our biggest port, but they're prohibitively expensive. This surely biases the results towards areas where rich people who have money to burn live. ^c18739723

  - **kingosticks** · [2018-12-22 09:20 UTC](https://news.ycombinator.com/item?id=18739777)
    I'm also surprised to see there are no sensors near the major London airports. ^c18739777

    Northern Italy is all red, what's going on there?!

