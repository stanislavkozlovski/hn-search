# [Ask HN: Indoor air quality sensors and other IoT that's local-first and not DIY?](https://news.ycombinator.com/item?id=33773786)

TeMPOraL · 2022-11-28 14:08 UTC · 132 reported comments · archived 2026-11-08 12:27 UTC
Observation: 2026-11-08 12:26 UTC → 2026-11-08 12:27 UTC

I've recently been looking into assembling an indoor air quality monitoring system, and so far have failed to found any solution that would meet the following criteria simultaneously:

1\. Connected for data logging, but local-first. That is, no mandatory Internet connection to vendor cloud. Ability to point to my own server (in my local network), or at least download a data dump off device every now and then (even if over a wire, as a last resort).

2\. Not strictly industrial-use. I.e. one that doesn't require me to become a large corporation to buy some, and that doesn't require some proprietary, expensive, and/or old-school industrial protocols to talk to.

3\. Not DIY at the hardware level. I'm not that good with a soldering iron, and with small children, I have neither time nor workshop space to solder and assemble anything less trivial than "plug a sensor into an ESP32 and screw both into a box".

(EDIT: shmaybe I can solder a few through-hole components into a PCB, but can't do SMD nor make a custom PCB.)

4\. Quality components. With sensors, I mean measuring what it says on a tin (vs. measuring something else and using a factory-provided lookup table to synthesize approximations), and doing it with reasonable accuracy and precision. If there's a calibration step to be done, it should be one that doesn't require me to incorporate myself to perform it.

I've spent some time looking at available options and past HN threads, and so far I discovered that:

\- Most products that fit \#2 and \#3 fail at \#1 - they're predominantly cloud-connected bullcrap, and going by review, they often fail at \#4. Occasionally, I find something that fits \#2, \#3, and \#4, but then it fails at \#1 by... providing *no* data export option altogether - apparently, it's enough for the consumer to see traffic lights instead of numbers, or browse the readings from the device control panel.

\- The DIY stuff I saw (failing \#3 to smaller or greater degree) is weak in \#4 - in some cases, I recognize the sensors as rather poor and tricky to use right (infamous DHT11 comes to mind), and in all cases, I don't know how one would go about calibrating anything.

My questions thus are:

\- Does anyone here have a setup that solves for these four points, and if yes, could you share some details?

\- How one would go about looking for vendors meeting those criteria, if they exist *at all*?

\- In a broader sense, how do you go looking for any IoT-adjacent vendor that meets those criteria? It really seems to me that everyone wants me to install their godawful stupid app to connect to their broken cloud, and there's such a flood of those products that reviewers can't keep up with quality testing, and hackers can't keep up with reversing the proprietary protocols and firmwares.

## Comments

- **akoutmos** · [2022-11-28 15:25 UTC](https://news.ycombinator.com/item?id=33774735)
  Hey there! My co-authors and I actually wrote a book on this topic earlier this year. It walks you though setting up a weather station with Elixir and Nerves using a Raspberry Pi and the following sensors: ^c33774735

  \- VEML6030 light sensor
  \- BME680 environmental sensor
  \- SGP30 air quality sensor

  After you set up the hardware side of things, you put together a very simple Elixir Phoenix REST API and persist the sensor data into Postgres (with the TimescaleDB extension).

  And to wrap up the book, you learn how to create Grafana dashboards to visualize all your time-series data.

  Everything is meant to be set up on your LAN and everything can be run either natively or in Docker (there is a Docker compose file in the repo).

  Hope that helps!

  GitHub Repo: [https://github.com/akoutmos/nerves\_weather\_station](<https://github.com/akoutmos/nerves_weather_station>)
  Book: [https://pragprog.com/titles/passweather/build-a-weather-stat...](<https://pragprog.com/titles/passweather/build-a-weather-station-with-elixir-and-nerves/>)

  - **Terretta** · [2022-11-28 15:28 UTC](https://news.ycombinator.com/item?id=33774768)
    Since OP mentioned not wanting to DIY, if people are looking for weather system with incredibly rich API and no moving parts (no Raspberry PIs either), this system is fantastic for people without workshop build time: ^c33774768

    [https://weatherflow.com/tempest-weather-system/](<https://weatherflow.com/tempest-weather-system/>)

    - **akoutmos** · [2022-11-28 15:35 UTC](https://news.ycombinator.com/item?id=33774854)
      To clarify, the OP said: "I have neither time nor workshop space to solder and assemble anything more trivial than "plug a sensor into an ESP32 and screw both into a box"." ^c33774854

      The book is very much "plug in a sensor" style as everything is connected via Qwiic cables.

    - **shkkmo** · [2022-11-28 17:05 UTC](https://news.ycombinator.com/item?id=33776138)
      That looks like it doesn't have any local-first functionality? Their API documentation only talks about how to retrieve data from their server, even if you are just trying to get the data from your own station. ^c33776138

      - **Terretta** · [2022-11-28 18:30 UTC](https://news.ycombinator.com/item?id=33777497)
        The device has an API, as does their "Hub" that reports the device to cloud.  You may find tools under different names like tempestwx or etc. ^c33777497

        That said, the point of this system is microcell climate computation, and it works best when part of the public grid of sampling points.

        - **shkkmo** · [2022-11-28 21:49 UTC](https://news.ycombinator.com/item?id=33780307)
          Does it? I couldn't find any documentation on those features, if you have links to any documentation that doesn't require going through their servers I'd love to see it since I've been looking for something just like that. Everything I have found, even for querying a single devices, requires making a request to swd.weatherflow.com via an internet connection. ^c33780307

          EDIT:
          I was eventually able to find this: [https://apidocs.tempestwx.com/reference/tempest-udp-broadcas...](<https://apidocs.tempestwx.com/reference/tempest-udp-broadcast>)

          So it is possible to get the data locally, but it seems like they are pretty strongly discouraging its use.

          - **circularfoyers** · [2022-11-29 01:37 UTC](https://news.ycombinator.com/item?id=33782565)
            Having said that, there's plenty of people using this method\[1\]. I particularly like the work this person did presenting that data in Grafana\[2\]. ^c33782565

            \[1\] [https://community.weatherflow.com/c/developers/5](<https://community.weatherflow.com/c/developers/5>)

            \[2\] [https://github.com/lux4rd0/weatherflow-dashboards-aio](<https://github.com/lux4rd0/weatherflow-dashboards-aio>)

            - **shkkmo** · [2022-11-29 15:39 UTC](https://news.ycombinator.com/item?id=33788860)
              Thanks for those links, I'll check them out! ^c33788860

    - **unknown** · [2022-11-30 06:23 UTC](https://news.ycombinator.com/item?id=33797611)
      [deleted] ^c33797611

    - **rngname22** · [2022-11-28 17:27 UTC](https://news.ycombinator.com/item?id=33776460)
      Confused here, isn't 'indoor air quality' primarily about CO2 levels, particulate matter, VOCs, etc.? I don't see any of that in there. ^c33776460

      - **Terretta** · [2022-11-28 18:29 UTC](https://news.ycombinator.com/item?id=33777481)
        Please note I replied to a comment about a book about a weather station. ^c33777481

        Top level, I replied about CO2 levels, VOCs, etc:

        [https://news.ycombinator.com/item?id\=33774695](<https://news.ycombinator.com/item?id=33774695>)

    - **anxrn** · [2022-11-28 17:09 UTC](https://news.ycombinator.com/item?id=33776202)
      This looks good, but this is an outdoor weather station.  OP is asking for an indoor air quality monitory. ^c33776202

      - **Terretta** · [2022-11-28 18:24 UTC](https://news.ycombinator.com/item?id=33777400)
        \> *This looks good, but this is an outdoor weather station. OP is asking for an indoor air quality monitory.* ^c33777400

        I replied with an indoor no-DIY suggestion and code at top level: [https://news.ycombinator.com/item?id\=33774695](<https://news.ycombinator.com/item?id=33774695>)

        \> *I actually wrote a book on this topic earlier this year. It walks you though setting up a* weather *station*...

        ... and replied to this from immediately above with a similarly no-DIY weather option.

      - **TeMPOraL** · [2022-11-28 17:46 UTC](https://news.ycombinator.com/item?id=33776769)
        True. That said, it's still interesting to me, because an outdoor weather station is something I've also been eyeing, and also having trouble to find something that a) logs data, but b) not to a cloud. ^c33776769

  - **Havoc** · [2022-11-28 15:35 UTC](https://news.ycombinator.com/item?id=33774853)
    Have you actually gotten any reliable co2 data out of the bme680? ^c33774853

    Even with the Bosch library and their calibration the values seem rather odd at times

    - **Youden** · [2022-11-28 18:23 UTC](https://news.ycombinator.com/item?id=33777386)
      It's not capable of CO2 measurement, it only estimates CO2 levels based on measurements of VOCs. These estimated readings are garbage and have close to zero correlation with CO2 levels. ^c33777386

      - **Havoc** · [2022-11-28 20:22 UTC](https://news.ycombinator.com/item?id=33779001)
        Unless I've got another source of VOCs around there should be at least some correlation with actual CO2 levels though? I don't have a reliable way of checking this, but the bottom end seemed well calibrated...outside air leads to a reading consistent with ambient co2 ^c33779001

        - **ahaucnx** · [2022-11-29 00:20 UTC](https://news.ycombinator.com/item?id=33781877)
          We tested a lot of VOC sensor modules and the estimated CO2 values they give is -in our experience- 80\% of the time totally wrong. Also the absolute ppb values of the TVOC are most often not to be trusted. ^c33781877

          What they are good at is detecting spikes, e.g. from cleaning liquids, desinfection etc. but I would not trust the absolute value at all.

          The big sensor manufacturers recognized that and newer generations of the Sensirion sensors are now just displaying an "index" instead of absolute measurements.

    - **bsder** · [2022-11-28 21:25 UTC](https://news.ycombinator.com/item?id=33779938)
      Thank you for asking this question because all of my experience so far with "environmental sensors" that aren't laboratory grade has been that they are absolute *garbage* and only barely correlated to anything. ^c33779938

      How are companies like Bosch allowed to pass this crap off as functional?  They don't meet even basic fitness for purpose criteria.

    - **akoutmos** · [2022-11-28 17:33 UTC](https://news.ycombinator.com/item?id=33776552)
      When developing the book, I didn't have any additional meters or sensors to cross reference measurements with so I can't comment on the accuracy unfortunately. But I did notice that the changes in measurements made sense when the environment changed. I.e when I would exhale on the sensor, the measurement would rise and fall. ^c33776552

      Another example was when I opened my window in my office. CO2 immediately dropped off (15:42 timestamp): [https://twitter.com/akoutmos/status/1443233937015418891/phot...](<https://twitter.com/akoutmos/status/1443233937015418891/photo/1>)

      - **Havoc** · [2022-11-28 21:08 UTC](https://news.ycombinator.com/item?id=33779670)
        Yeah same - there is definitely a practical cause & effect practical correlation, but also a lot of effect without obvious cause in an environment that should be relatively stable. (one person, small apt, no co2 sources) ^c33779670

        \> additional meters or sensors

        I've got a CCS811 as well but no luck yet. Acquired 2nd hand so unsure if broken from shipping or I'm being stupid with code or I broke it while soldering

        - **TeMPOraL** · [2022-11-29 02:25 UTC](https://news.ycombinator.com/item?id=33782912)
          This reminds me how my DIY build of Luftdaten kit (PM sensor) started reporting huge particulate spikes indoors, with no obvious cause. Took me \~2 days to figure out they're being caused by our ultrasonic humidifier, and another 2 days of looking through blogs and scientific papers to finally learn that one shouldn't be putting tap water into them (as they efficiently aerosolise the minerals and contaminants dissolved in it). ^c33782912

      - **buran77** · [2022-11-28 19:16 UTC](https://news.ycombinator.com/item?id=33778166)
        Both the SGP30 and the BME680 have a big weakness that I experienced some years ago when I trying putting an air quality sensor together. They correlated the TVOC readings with the temperature. And sometimes it was bad, like a difference of just 1 or 2 degrees Celsius could double or triple the TVOC readings at the lower end of the scale (\~50ppb), and add maybe \~50\% at the upper end (\~500ppb). ^c33778166

        Are you seeing the same behavior?

    - **gsich** · [2022-11-28 15:56 UTC](https://news.ycombinator.com/item?id=33775168)
      Yeah, it's only a propietary approximation. ^c33775168

- **Terretta** · [2022-11-28 15:22 UTC](https://news.ycombinator.com/item?id=33774695)
  We use these at office in conference rooms or 1:1 rooms, and encourage people to keep CO2 levels below 700-800 (an empty room 450-550).  Very high quality, a half dozen all agree perfectly on all sensors. They support API. ^c33774695

  \# *SAF Aranet4 Home*

  *Wireless Indoor Air Quality Monitor for Home, Office or School (CO2, Temperature, Humidity and More) Portable, Battery Powered, E-Ink Screen, App for Configuration & Data History*

  \- *The perfect companion for indoor environments, allowing you to monitor CO2 levels, temperature, relative humidity, and atmospheric pressure in real-time*

  \- *Easy for anyone to use – the color coding and the optional buzzer warns you when the CO2 concentration gets too high*

  \- *Power-efficient e-ink display ensures super long battery life for this wireless device (up to 4 years)*

  \- *Smartphone app for viewing and analyzing historical data up to 14 days history (supports iPhone and iPad with iOS 12 or later, Android devices with Oreo 8.0 or later, compatible with Bluetooth 4.1 or later)*

  \- *Uses nondispersive infrared sensor (NDIR) technology for most precise and reliable CO2 measurements*

  [https://smile.amazon.com/gp/product/B07YY7BH2W/](<https://smile.amazon.com/gp/product/B07YY7BH2W/>)

  [https://github.com/Anrijs/Aranet4-Python](<https://github.com/Anrijs/Aranet4-Python>) \*

  \* *Note: Smart Home Integrations must be enabled in Aranet4 mobile app for full support*

  - **dawnerd** · [2022-11-28 15:49 UTC](https://news.ycombinator.com/item?id=33775051)
    I love mine too. Been meaning to set up some longer term logging since the app only holds two weeks (and I've noticed it often wipes out data faster than that). ^c33775051

    Only thing I wish it had was voc monitoring.

  - **AceJohnny2** · [2022-11-28 20:19 UTC](https://news.ycombinator.com/item?id=33778962)
    Another vote for this. We saw it at friends over Thanksgiving, and immediately got our own. ^c33778962

    It's local, and does logging. That's what I really want.

  - **xolox** · [2022-11-29 00:44 UTC](https://news.ycombinator.com/item?id=33782125)
    Here's another upvote for the Aranet4 device, I first found it recommended on HN and have been happy with it ever since purchasing it a couple of months ago. Integrated into Home Assistant using a couple of lines of Python code scheduled by AppDaemon. ^c33782125

  - **unknown** · [2022-11-28 18:53 UTC](https://news.ycombinator.com/item?id=33777838)
    [deleted] ^c33777838

- **mvarrieur** · [2022-11-28 17:29 UTC](https://news.ycombinator.com/item?id=33776486)
  I have an Airthings Wave Plus \[1\] which measures CO₂, Radon, VOCs, and some others but until recently I could only get the data out via the cloud integration. ^c33776486

  Home Assistant recently added a BLE integration \[2\] with the device and it works great, way better than the Airthings app actually. So now I'm automatically logging and tracking all the data on a regular basis instead of hoping the app is still running in the background on my phone and updating the cloud.

  I am not sure about initial setup since I had to go with the cloud integration to get it working in the first place a year or so ago, but maybe now you could skip that and just start reading the data off the BLE? It's possible but I cannot say for sure.

  1\. [https://www.airthings.com/wave-plus](<https://www.airthings.com/wave-plus>)

  2\. [https://www.home-assistant.io/integrations/airthings\_ble/](<https://www.home-assistant.io/integrations/airthings_ble/>)

  - **sliken** · [2022-11-28 22:00 UTC](https://news.ycombinator.com/item?id=33780469)
    I've got a few of the airthings bluetooth units and a wifi gateway that handles bluetooth -\> wifi.  Works well, sensors seem to be accurate and correlate with things like radon (which dropped once mitigated), CO2 peaks (when more people are around or gas oven is on), temp, humidity etc. ^c33780469

    They have a github repo at [https://github.com/Airthings](<https://github.com/Airthings>) and have code for things like uploading data to a local grafana.

    It was basically turnkey, the gateway works on batteries or *gasp* a usb-c.  Batteries on the BT only widgets do last a good fraction of a year.  I'm using the cloud hosted dashboard, but bought it because I could migrate local when I have the time to setup.

    EDIT: I have the viewplus (not waveplus), that acts as a Bluetooth \<-\> WIFI gateway and has a PM2.5 sensor the view plus does not, and does *NOT* have any code I've found to read it for non-cloud use.

  - **colonelxc** · [2022-11-28 18:25 UTC](https://news.ycombinator.com/item?id=33777415)
    Thanks for mentioning this. I had looked at these before, but was holing off due to the cloud-polling home assistant integration. ^c33777415

    - **westende** · [2022-11-29 15:49 UTC](https://news.ycombinator.com/item?id=33789009)
      ESPHome has an integration for the Airthings Wave Plus: [https://esphome.io/components/sensor/airthings\_ble.html](<https://esphome.io/components/sensor/airthings_ble.html>) 
      This is working well for me on a NodeMcu ESP32 with WiFi and Bluetooth. No soldering required. This makes it possible to integrate with Home Assistant without sending your data to Airthings HQ. ^c33789009

- **christiangenco** · [2022-11-28 16:06 UTC](https://news.ycombinator.com/item?id=33775308)
  I think it's difficult to make an electronic sensing device that logs data locally but isn't a little DIY. There's not a great standard for passing around data on a local network. Perhaps the best way to do this from a consumer device would be to log to a USB stick. ^c33775308

  You asked for something that's not DIY at the *hardware* level, though, so I think something like the AirGradient Pre-Soldered kit would be perfect for you\[1\].

  You'll get an Arduino connected to top-of-the-line sensors that can be flashed with your SSID to connect to your local WiFi network. Once connected, the device exposes an HTTP endpoint you can GET for the status of each sensor\[2\].

  I've been thinking a lot about indoor air quality\[3\] so if this setup works for you I'd love to know!

  1\. [https://www.airgradient.com/open-airgradient/shop/\#!/DIY-Pro...](<https://www.airgradient.com/open-airgradient/shop/#!/DIY-Pro-Kit-Pre-Soldered/p/476627519/category=0>)

  2\. [https://youtu.be/Cmr5VNALRAg?t\=444](<https://youtu.be/Cmr5VNALRAg?t=444>)

  3\. [https://gen.co/air](<https://gen.co/air>)

  - **TeMPOraL** · [2022-11-29 02:34 UTC](https://news.ycombinator.com/item?id=33782991)
    \> *I think it's difficult to make an electronic sensing device that logs data locally but isn't a little DIY. There's not a great standard for passing around data on a local network. Perhaps the best way to do this from a consumer device would be to log to a USB stick.* ^c33782991

    I was a bit surprised by that, but ultimately guessed at the same thing - even ignoring the (IMHO repugnant) cloud-based business model, there isn't one obvious way to record data off-device in local-first way that would be useful for non-tech / non-industrial users. It's kind of similar to the problem of transferring files between two computers: there are so many ways you could do it, with different requirements and tradeoffs\[0\], that there is no one universal way everyone can rely on. See also \[0\].

    WRT. DIY, I don't mind extensive software-level DIY (especially that I'm DIY-ing the data storage, analysis and reporting side), but I currently want to avoid hardware DIY.

    Thanks for your thoughts and the links; I found your analysis under\[3\] particularly useful and insightful. I'm actually looking into this space for health reasons - we don't have regular wildfires where I live, but I do have allergies, and now children with allergies too, so I want to better understand and control our indoor air.

    \----

    \[0\] - [https://xkcd.com/949/](<https://xkcd.com/949/>)

    - **eternityforest** · [2022-11-29 03:25 UTC](https://news.ycombinator.com/item?id=33783335)
      Zigbee 3.0 has reports of being fussy and cutting out, but it seems like they are as close as anyone's ever gotten to a proper standard. ^c33783335

      I suppose time will tell if CHIP/Thread/Matter will finally solve the issue once and for all, but I think it looks promising.

- **oger** · [2022-11-28 16:12 UTC](https://news.ycombinator.com/item?id=33775378)
  I have several IKEA Vindriktning air quality sensors (measuring PM2.5 but not CO, CO2 or VOC) equipped with an ESP32 with Tasmota on it. The level of soldering is trivial and the hardware looks really nice. It feeds a Grafana dashboard via MQTT, Node RED and InfluxDB. All is well documented and easy to do - you will find lots of resources online. And the Tasmota toolchain can be used for many other sensors as well. ^c33775378

  [https://www.hackster.io/news/ikea-vindriktning-air-quality-s...](<https://www.hackster.io/news/ikea-vindriktning-air-quality-sensor-mod-adds-sensors-and-indicators-aac85d80c7c9>)

  - **runjake** · [2022-11-28 17:16 UTC](https://news.ycombinator.com/item?id=33776319)
    From the article, it looks like it involves a significant investment in DIY time and parts acquisition. ^c33776319

    Are you using the custom PCB and 3D-printed LED mounts in the instructions? What are you doing differently?

    - **TeMPOraL** · [2022-11-28 18:20 UTC](https://news.ycombinator.com/item?id=33777325)
      I've seen articles about it; my understanding it that at minimum, it only involves a small amount of simple soldering to connect an ESP8266 (or ESP32)-equipped board to the IKEA PCB, which is about the limit of what I can do in my current conditions. It also fits into the original enclosure without damaging it, which is a nice bonus. ^c33777325

      I keep it on my list as a last-resort option, because of two factors:

      1\. That's only a particulate sensor, and I'm hoping I can find something more comprehensive - at least with TVOC, but a legitimate CO₂ would be nice too.

      2\. Unless immediately hacked, it's just a paperweight - I'm not going to bother manually recording the two-bit measurement it displays, and my wife isn't fond of colorful indicator lights illuminating the apartment at night.

- **nathan\_f77** · [2022-11-28 15:56 UTC](https://news.ycombinator.com/item?id=33775178)
  I recommend looking at Zigbee devices. They are local-first and don't require an internet connection (or any network at all.) If you don't have any existing home automation software or hardware, then the easiest way to get started is probably with a Home Assistant Yellow: [https://www.home-assistant.io/blog/2021/09/13/home-assistant...](<https://www.home-assistant.io/blog/2021/09/13/home-assistant-yellow>) ^c33775178

  I've been very happy with my \$20 Zigbee air quality sensors that I bought from AliExpress \[1\]. No DIY required, just plug them in and pair them with Home Assistant. These cheap sensors don't really have quality components or accurate readings, but they're accurate enough to get a good sense of my air quality and set thresholds to automate extractor fans and air purifiers.

  If you really need a commercial-grade and highly accurate sensor, you could look at this iQi Zigbee sensor for \$300 \[2\]. But I would recommend the \$20 ones from AliExpress for home use.

  \[1\] [https://www.aliexpress.com/item/1005003815133870.html](<https://www.aliexpress.com/item/1005003815133870.html>)

  \[2\] [https://www.trutechtools.com/iqi-air-quality-monitor-v1-with...](<https://www.trutechtools.com/iqi-air-quality-monitor-v1-with-zigbee-and-hardwire.html>)

  - **RobotToaster** · [2022-11-28 16:22 UTC](https://news.ycombinator.com/item?id=33775547)
    In my experience the CO2 readings from these cheap devices are estimated from VOC levels. ^c33775547

  - **christiangenco** · [2022-11-28 16:08 UTC](https://news.ycombinator.com/item?id=33775329)
    Were you able to get accurate CO2 readings from the AliExpress Zigbee sensors? I got two of them and the CO2 values from each were wildly wrong. I'm curious if I'm missing a calibration step. ^c33775329

    - **nathan\_f77** · [2022-11-28 16:19 UTC](https://news.ycombinator.com/item?id=33775490)
      I'm not sure how accurate it is but the values seem reasonable. It hovers around 360ppm for fresh air. I can see it creep up if I'm in my office with the windows and door closed, and it spikes up if I breathe onto it. ^c33775490

- **HTresearch** · [2022-11-28 18:20 UTC](https://news.ycombinator.com/item?id=33777330)
  It sounds like you are looking for something like the air monitor I have been developing over the last two years.  It is about the size of a deck of cards and fits in a shirt pocket.  The Lithium Polymer battery powers it for 12-16 hours and is recharged with USB-C. ^c33777330

  It uses a high-accuracy CO2 sensor (±(40 ppm + 5 \%) and you can manually calibrate it to 420 PPM outdoor air.  A key innovation is reporting via a dynanmic QR code on its 128x64 OLED display.  Just point your phone camera at the QR code and it takes you to a site showing a report with graphs and data tables of recent measurements. There is no app to install or web site to log into.  The web page is context-free and all of the measurement data is in the query string.  It is nearly ready for production and likely to sell in the \$150 price range.

  - **TeMPOraL** · [2022-11-28 18:32 UTC](https://news.ycombinator.com/item?id=33777519)
    That sounds neat, and I love the idea of displaying a QR code, even though I'm not sure how practical it would be. Is it there to allow viewing more data than would otherwise fit on the display in human-readable form? ^c33777519

    For my use case, I *could* hack a system with a spare phone reading the code on a timer and uploading the results, but this feels like an overkill. How much more complex would it have to be to use that same USB-C charging port for data and power delivery? I'm imagining attaching an ESP32 board to it, which would be powered by your device, and would occasionally wake up, read a CSV file or a data stream over that USB connection, upload it to my home server, and go back into deep sleep. With an option to turn the OLED display off, I imagine it could even extend the battery life.

    (Please don't take this as criticism - I fully understand my use case is most likely out of scope of your project, but I'm wondering how close it is to be supported.)

  - **BetterGeiger** · [2022-11-28 18:29 UTC](https://news.ycombinator.com/item?id=33777479)
    Sounds interesting! If I may ask out of curiosity: ^c33777479

    Why OLED?

    Why this QR thing and not Bluetooth, or is it both?

    Is it storing long-term data or just while battery is on?

    - **HTresearch** · [2022-11-28 19:41 UTC](https://news.ycombinator.com/item?id=33778516)
      OLED is the cheapest display with enough resolution. ^c33778516

      No Bluetooth.  A previous version had it, but the development effort was much higher, given it then needed an App also.  I wanted something simple for say a school teacher to report values in their classroom.

      Data is not stored long term currently.  Just since last power on.

  - **mdp2021** · [2022-11-28 19:22 UTC](https://news.ycombinator.com/item?id=33778246)
    I hope you can also do without the QR code, and directly display the URL... ^c33778246

    Also, that the basic data can be seen directly on the display.

    - **HTresearch** · [2022-11-28 19:38 UTC](https://news.ycombinator.com/item?id=33778471)
      The current readings are on the display. The QR code encodes 40 previous values of CO2 plus 40 of the VOC index.  I have a debug mode that can display the whole URL, but it is so long that it would be impractical to type it in instead of the simple QR scan. ^c33778471

  - **christiangenco** · [2022-11-28 18:23 UTC](https://news.ycombinator.com/item?id=33777381)
    Link? ^c33777381

    - **HTresearch** · [2022-11-28 19:43 UTC](https://news.ycombinator.com/item?id=33778529)
      No link yet.  Still working on a web site for it. ^c33778529

      - **christiangenco** · [2022-11-28 23:11 UTC](https://news.ycombinator.com/item?id=33781219)
        When you've got one I'd love to link to it from gen.co/air! ^c33781219

- **ahaucnx** · [2022-11-28 23:58 UTC](https://news.ycombinator.com/item?id=33781691)
  We are maintaining a popular open source / open hardware air quality kit that is also available as a pre-soldered version \[1\]. ^c33781691

  It incorporates many of the features of our commercial monitor, e.g. high quality and accurate sensor components, professional looking plastic enclosure, air flow optimized PCB for accurate measurements etc.

  Since it is open source it is very easy to point it to your own server. We do also have an active forum where you can get help and discuss specific things around the monitor \[2\].

  On the pre-soldered kit that we sell, we test all components before shipping and preflash the MCU. It only consists of a few components that need to be plugged onto sockets already on the PCB. I am able to assemble it in less than five minutes (no soldering iron required).

  We spend a lot of time and resources to get this open hardware kit right and you are correct that many -if not most- DIY air quality monitor project that you find on the internet have significant weaknesses (e.g. poor sensor selection, internal overheating of the temperature sensor) that leads to very inaccurate measurements.

  Why do we do this? AirGradient started as a volunteer project to help a school in Thailand better manage air quality during wild fire season and from the start we worked with students building sensors. So this is part of our DNA and also an offical part of our company \[3\].

  \[1\] [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>)

  \[2\] [https://forum.airgradient.com/](<https://forum.airgradient.com/>)

  \[3\] [https://www.airgradient.com/open-airgradient/](<https://www.airgradient.com/open-airgradient/>)

  - **TeMPOraL** · [2022-11-29 02:21 UTC](https://news.ycombinator.com/item?id=33782879)
    Thanks for replying! I actually saw you mentioned (and IIRC you posting) on a bunch of other HN threads during my research, which put AirGradient was on the top of my list so far. I'm considering the DIY Pro pre-soldered kit + the TVOC extension. ^c33782879

    Since you are responding on HN, a question: what's the noise level of the PM sensor? I assume that, like all PM sensors of this type, it has an internal fan that spins up when taking a measurement. When I did a Luftdaten kit build a few years ago, one of the issues I had indoors was that the fan spinning up was audible enough to be annoying, particularly to my wife, and particularly at night (with no background noises to drown it out). Do you know of any effective means of reducing that noise without impeding airflow to the sensor? Also, I remember reading someone hacking such a sensor to run its fan slower (and thus quieter), but continuously - but I'm not sure if that won't compromise the sensor readings.

    - **ahaucnx** · [2022-11-29 04:49 UTC](https://news.ycombinator.com/item?id=33783825)
      The fan in the Plantower PMS5003 monitor we use is actually very silent and you can hear it only if you put your ear directly at the sensor. ^c33783825

      I have a few of our monitors in the bedroom less than 1m away from my ears and I cannot hear them at all.

  - **sails** · [2022-11-29 11:13 UTC](https://news.ycombinator.com/item?id=33786105)
    Just FYI: ^c33786105

    The checkout is very confusing, no cart button in the top UX, need to find it in the actual product page.

    Also difficult to find shipping details.

- **sigio** · [2022-11-28 15:18 UTC](https://news.ycombinator.com/item?id=33774642)
  The [https://operame.nl/Operame](<https://operame.nl/Operame>) project made some designs/kits for CO² monitoring (in dutch classrooms). While this is mostly a DIY thing, assembly was really easy, and there were some volunteers even pre-assembling kits for third parties. ^c33774642

  I have 2 of these sensors myself, and they report over mqtt (local), and I've connected them to homeassistant for live insight and possibly triggeging other events based on CO² levels.

  The Operame project is currently on hold, but all designs/code are open and free to use.

- **thinkmcfly** · [2022-11-28 15:40 UTC](https://news.ycombinator.com/item?id=33774927)
  For any readers who need hand soldering for a project like this, you're welcome to dm me. Ship it to my house and I'll put it together. I'll do it for free 
  (USA only) ^c33774927

  Can do through hole + smd, but no bga

- **d12bb** · [2022-11-28 16:11 UTC](https://news.ycombinator.com/item?id=33775375)
  Anything HomeKit is local-first. That's one thing Apple actually got right, and thankfully has pushed into the new Matter industry standard too. Won't work without some Apple device though of course. ^c33775375

  - **Thews** · [2022-11-28 18:18 UTC](https://news.ycombinator.com/item?id=33777288)
    I'm curious to see how matter will be adopted,  it looks like almost everything will have a local method of control.   I'm already using zigbee and z-wave and some local wifi interfaces.  I love automating everything how I want and not worrying about any online services. ^c33777288

    - **TeMPOraL** · [2022-11-29 02:35 UTC](https://news.ycombinator.com/item?id=33783002)
      Is it local but fully delegated to Apple, or local as in I can actually get my hands on raw data and the control plane? ^c33783002

- **diblasio** · [2022-11-28 17:45 UTC](https://news.ycombinator.com/item?id=33776753)
  I also had this same problem to solve about a year ago. What I ended up doing was to build an iaq\_board, and then plot the data in grafana. ^c33776753

  [https://esphome.io/cookbook/iaq\_board.html](<https://esphome.io/cookbook/iaq_board.html>)
  [https://github.com/nkitanov/iaq\_board](<https://github.com/nkitanov/iaq_board>)

- **Confiks** · [2022-11-28 15:27 UTC](https://news.ycombinator.com/item?id=33774755)
  I bought the Aranet4 a while ago, and that seems to meet all your requirements. Keeps measurement history local, but can be paired via Bluetooth (with a pairing code) through their (somewhat flaky) app or open source options. Has a hardware switch to disable Bluetooth. Good quality sensor. Very good battery live due to e-ink screen. Looks pretty neat as well. Quite expensive though, but almost every quality sensor is. ^c33774755

- **themacks** · [2022-11-28 15:45 UTC](https://news.ycombinator.com/item?id=33774993)
  I'm just starting a similar project to monitor my home. I decided on using esphome.io based devices connected to my Home Assistant setup. Spark Fun has a great ecosystem \[1\] of sensors and carriers \[2\] that are just plug and play as far as the hardware goes (no soldering). You would just need to DIY a case. ^c33774993

  You could probably also find off the shelf Bluetooth sensors that would interface with Home Assistant for data logging and visualization.

  \[1\]: [https://www.sparkfun.com/categories/tags/qwiic](<https://www.sparkfun.com/categories/tags/qwiic>)
  \[2\]: [https://www.sparkfun.com/products/17724](<https://www.sparkfun.com/products/17724>)

- **Toutouxc** · [2022-11-28 19:55 UTC](https://news.ycombinator.com/item?id=33778671)
  Probably not at the level that OP is asking about, but the IKEA Starkvind air purifier, aside from being a good-looking, cheap and effective home purifier, is a Zigbee device that exposes the raw PM2.5 sensor reading. ^c33778671

  One Starkvind (or more if space and budget allow) and few temperature/humidity sensors (I have a few \$10 ones from Sonoff), combined with a Raspberry or an HTPC running Home Assistant and any Zigbee gateway, can give you a better idea about what the air is like in your apartment than most people have.

  I'm still looking for a non-DIY CO2 sensor solution I could add to my Zigbee based network, most of the stuff I've found is either totally DIY or industrial.

  - **xolox** · [2022-11-29 00:50 UTC](https://news.ycombinator.com/item?id=33782178)
    The Aranet4 device is a non-DIY CO2 sensor however it operates over Bluetooth instead of Zigbee, not sure how much of a deal breaker that is for you. I had no trouble hooking it up to my Home Assistant setup though, and the device is fairly affordable (for a "proper" CO2 sensor that is, not one of those Ali Express devices that estimates CO2 by VOC measurements). ^c33782178

  - **spockz** · [2022-11-28 21:17 UTC](https://news.ycombinator.com/item?id=33779832)
    Interesting! I was looking into the starkvind and didn’t know it exposes the metrics via zigbee. ^c33779832

    I do wonder where to place it. Middle of the room seems best. Would it be useful to mount it on the ceiling?

- **janalsncm** · [2022-11-28 15:12 UTC](https://news.ycombinator.com/item?id=33774585)
  Are there any high quality local-first IoT brands out there at all? I would be interested in a home assistant with some basic offline-only (or limited online) skills. For example, set a timer by voice, check the weather by voice, add something to a locally-synced calendar. ^c33774585

- **birdman3131** · [2022-11-28 18:03 UTC](https://news.ycombinator.com/item?id=33777051)
  Its not no soldering but it is low effort soldering. Pulling from a couple guides here. ^c33777051

  Tasmota is local first.

  Get a wemos D1 and a [https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor...](<https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor-60515911/>)

  [https://tasmota.github.io/install/](<https://tasmota.github.io/install/>) flash the unofficial all sensors build.

  [https://github.com/Hypfer/esp8266-vindriktning-particle-sens...](<https://github.com/Hypfer/esp8266-vindriktning-particle-sensor/blob/master/img/board.jpg>) Solder as follows GND to GND on ESP, 5V to 5V on ESP and finally the last one to D2 on the ESP.

  Guides I am stealing from. [https://github.com/Hypfer/esp8266-vindriktning-particle-sens...](<https://github.com/Hypfer/esp8266-vindriktning-particle-sensor>) Has most of the hardware side. But its using a different software.

  [https://blakadder.com/vindriktning-tasmota/](<https://blakadder.com/vindriktning-tasmota/>) is where I got most of the rest of the info but he uses a separate voltage regulator. If you use the Wemos D1 Mini you should not need that.

  After that the internet has plenty of info for hooking tasmota and say home assistant together.

- **iamacyborg** · [2022-11-28 15:33 UTC](https://news.ycombinator.com/item?id=33774840)
  This should fit all yours needs. ^c33774840

  [https://www.evehome.com/en/eve-room](<https://www.evehome.com/en/eve-room>)

  - **quartz** · [2022-11-28 18:06 UTC](https://news.ycombinator.com/item?id=33777114)
    Nice. This seems like the perfect solution and fits OP's requirements! ^c33777114

    - **TeMPOraL** · [2022-11-28 18:49 UTC](https://news.ycombinator.com/item?id=33777771)
      Almost. Unless I'm missing something, the only way I can get the data for my own storage and processing is by manual export of an Excel sheet from their app. Unless HomeKit allows some other way, but I'm not familiar with it (I'm not an iOS user). ^c33777771

- **wintermutestwin** · [2022-11-28 18:52 UTC](https://news.ycombinator.com/item?id=33777833)
  I am generally not into "connect it all to the cloud" either, but I want to point out that cloud connected outdoor air quality sensors like Purpleair are tremendously valuable to society. Living in a wildfire prone CA, I am constantly monitoring PA sensors in my area to determine if it is safe to exercise outdoors. ^c33777833

  - **TeMPOraL** · [2022-11-28 19:08 UTC](https://news.ycombinator.com/item?id=33778065)
    I agree, and am happy to see this data out there and (mostly) in the open. In my area, there's a bunch of such stations operated by a certain local startup, so I have all the outdoor data I need. I might one day add a sensor of my own to that map (in the past, I briefly used to run a sensor for Luftdaten project) - but at this point, I want to measure *indoor* data, and adding those to the public maps will only introduce noise, providing negative value to the public. ^c33778065

    - **wintermutestwin** · [2022-11-28 20:11 UTC](https://news.ycombinator.com/item?id=33778861)
      \>indoor data, and adding those to the public maps will only introduce noise, providing negative value to the public. ^c33778861

      Well, seeing my neighbor's indoor air quality might explain why he is such a jerk. It also might help spot local methlabs...

      (just kidding - I totally agree with you)

- **awwww7229** · [2022-11-29 07:50 UTC](https://news.ycombinator.com/item?id=33784768)
  Hello, ^c33784768

  I would recommend taking a look and talking with this Finland-based company, they utilise a global 0G IoT network, and their devices are fully plug-and-play free from any electrical supply - thus just stick their device on your walls or place them where you want, and they'll support any data configuration needs.

  no internet connection required, and they have their own working data software platform for all essential monitoring data, or your own platform via API.

  From all your points, they seem to actually fit your needs from \#1 to \#4.

  Here are their contact links: [https://connectedinventions.com/about-us/](<https://connectedinventions.com/about-us/>)
  And here are their devices: [https://connectedinventions.com/all-devices/](<https://connectedinventions.com/all-devices/>)

- **omh** · [2022-11-28 15:23 UTC](https://news.ycombinator.com/item?id=33774700)
  I have the Awair Element and I'm reasonably happy with it. ^c33774700

  The primary interface is through their app and I think you might need to use this to get it up and running initially.
  But they have a supported local API feature\[1\] that has so far worked as I'd expect.
  In the end I've been happy with their app so have primarily used that so far. The data seems good.

  They're quite expensive new.
  But they were involved in some sort of cryptocurrency (!) that failed. So there are a *lot* of them available as nearly-new on eBay. In the UK I picked one up for about £60, I think.

  \[1\] [https://support.getawair.com/hc/en-us/articles/360049221014-...](<https://support.getawair.com/hc/en-us/articles/360049221014-Awair-Element-Local-API-Feature>)

  - **zapt02** · [2022-11-28 15:26 UTC](https://news.ycombinator.com/item?id=33774737)
    Awair recently deprecated some of their devices making them into bricks instead of allowing them to continue working locally. I'd stay away. ^c33774737

    [https://old.reddit.com/r/Awair/comments/y7i5ku/awair\_discont...](<https://old.reddit.com/r/Awair/comments/y7i5ku/awair_discontinues_support_for_v1_devices/>)

    - **cvp** · [2022-11-28 16:16 UTC](https://news.ycombinator.com/item?id=33775444)
      The v1 devices never supported a real local API. The v2 devices like the Awair Element do have a local API built-in. It does have to be enabled via the app but it lets you hit the device's LAN address and get back real time JSON with the sensor data. Not to say they couldn't figure out a way to brick those devices in the future, but you could theoretically turn on the Local API and then firewall the devices to your network to prevent future firmware updates. ^c33775444

      - **zapt02** · [2022-11-28 16:31 UTC](https://news.ycombinator.com/item?id=33775672)
        That would work for a while but if you ever needed to set it up on a new Wifi network you would be screwed, as the app is required for initial setup. ^c33775672

        - **TeMPOraL** · [2022-11-29 02:39 UTC](https://news.ycombinator.com/item?id=33783024)
          One thing I've learned over the years is that it's good to "own" your SSID, and preferably stick to pro-grade routers that let you configure local network addressing. As long as you stick to Internet providers that let you run their hardware in "bridge" mode, it means you don't have to set up new WiFi networks at all. ^c33783024

  - **KaiserPro** · [2022-11-28 20:44 UTC](https://news.ycombinator.com/item?id=33779337)
    I have some of them. They are expensive new, *but* well calibrated, with decent components. ^c33779337

    The local API is easy to interface to telegraf, so its trivial to dump to your graphing system of choice.

- **moepstar** · [2022-11-28 15:22 UTC](https://news.ycombinator.com/item?id=33774691)
  I think your best bet is ditching \#3, go with ESPHome and use one of their sensors here: [https://esphome.io/\#air-quality](<https://esphome.io/#air-quality>) ^c33774691

  I've a few with PMS5003 sensors and have been satisfied so far...

  - **kamaradclimber** · [2022-11-28 17:06 UTC](https://news.ycombinator.com/item?id=33776170)
    I'm using [https://esphome.io/components/sensor/mhz19.html](<https://esphome.io/components/sensor/mhz19.html>) which is super simple to use with esphome. Using a solderless breadboard allows to avoid soldering. ^c33776170

- **tlavoie** · [2022-11-28 20:11 UTC](https://news.ycombinator.com/item?id=33778856)
  I did minimal hardware DIY for temp/humity/pressure, with some Adafruit ESP32 boards and BME280 sensors. The inside unit has one of their e-paper displays to show inside/outside info, and sits in a box from the dollar store. I'd think that adding the other sensors would be minimal other soldering for added bits, but I haven't gone there (yet). \[Edit: this could be non-soldering with a breadboard, which my outside unit is still in, with a battery and in a soap dish with holes added.\] ^c33778856

  The more DIY side of mine is all the software, with MQTT as the glue. Both ESP32s publish to that, one subscribes (to show both), and a little daemon on the Pi with Mosquitto writes it all to an Sqlite database.

- **jvanderbot** · [2022-11-28 15:02 UTC](https://news.ycombinator.com/item?id=33774455)
  I'm happy to set something up and sell you a few, but my experience making these is that the cost gets pretty steep for small batch, high quality runs. ^c33774455

  It's been a side project of mine to set up a local-first IoT shop. But haven't gotten a lot of traction yet.

  - **glasss** · [2022-11-28 15:14 UTC](https://news.ycombinator.com/item?id=33774604)
    If you're willing I'd love to know what you use / would use for something like this. ^c33774604

    I've had some very similar ideas and stalled out at the hardware stage, but admittedly haven't tried in a while.

  - **Lienetic** · [2022-11-28 15:32 UTC](https://news.ycombinator.com/item?id=33774825)
    I'd love to hear more about your shop and why you think it's been difficult to get a lot of traction! ^c33774825

  - **unknown** · [2022-11-28 15:30 UTC](https://news.ycombinator.com/item?id=33774800)
    [deleted] ^c33774800

  - **TeMPOraL** · [2022-11-28 15:18 UTC](https://news.ycombinator.com/item?id=33774633)
    Can you give some ballpark estimates, either here or privately (my e-mail is in the profile)? ^c33774633

    - **jvanderbot** · [2022-11-28 16:41 UTC](https://news.ycombinator.com/item?id=33775803)
      Sure, I will email you later this week. ^c33775803

    - **jvanderbot** · [2022-12-01 15:53 UTC](https://news.ycombinator.com/item?id=33817903)
      Sent! ^c33817903

- **anigbrowl** · [2022-11-28 17:47 UTC](https://news.ycombinator.com/item?id=33776803)
  m5stack.com ^c33776803

  Highly modular components aimed at tinkerers (connect electronically with grove connectors rather than soldering (unless you want to), Lego-compatible, programmable in C, micropython, or via blockly. It's very, very easy to get up and running. Also they're still doing 10-20\% off today.

  Cons: documentation is a bit mediocre, you're kinda expected to read datasheets/figure it out yourself past the basics. If you are OK with looking up chip/component numbers to see exactly what they do you'll be fine.

  - **TeMPOraL** · [2022-11-28 19:03 UTC](https://news.ycombinator.com/item?id=33778002)
    Thanks! That's something I always hoped to see gain traction (I've seen several failed attempts in the past, and was tangentially involved in testing one aimed at kids). I'm fine with chasing data sheets and uC programming. I'll look into this for several projects I've been meaning to do. ^c33778002

- **gozdal** · [2022-11-28 15:16 UTC](https://news.ycombinator.com/item?id=33774618)
  I have [https://blebox.eu/product/airsensor/?lang\=en](<https://blebox.eu/product/airsensor/?lang=en>) and [https://aranet.com/products/aranet4/](<https://aranet.com/products/aranet4/>) ^c33774618

  Unfortunately don't have the skills to measure the accuracy and precision but both are well reviewed in the Internets.

- **flyinghamster** · [2022-11-28 19:27 UTC](https://news.ycombinator.com/item?id=33778341)
  Whoops, this is a bit DIY-ish, but an SDR stick and rtl\_433\[1\] can pick up many remote weather instruments, from simple temperature/humidity sensors to weather stations (and a wide variety of other devices as well). ^c33778341

  \[1\] [https://www.triq.org/rtl\_433/](<https://www.triq.org/rtl_433/>)

  - **heywire** · [2022-11-28 19:31 UTC](https://news.ycombinator.com/item?id=33778385)
    I use a handful of Acurite 6044M temperature and humidity sensors strewn throughout my house and an Acurite 0829 outside for this purpose with rtl\_433, influx DB, and Grafana for viewing. These sensors last a long time on battery and transmit frequently (\~30s IIRC) ^c33778385

    - **flyinghamster** · [2022-11-28 21:12 UTC](https://news.ycombinator.com/item?id=33779741)
      I've got a couple of sensors set up, one in the basement and one in the porch, with MRTG/rrdtool and a hacked CGI script doing likewise, running on a Raspberry Pi 3. There are a few neighboring units that I have to filter out as well. ^c33779741

      - **heywire** · [2022-11-28 21:22 UTC](https://news.ycombinator.com/item?id=33779898)
        Nice. I’ve been wanting to go with something simpler and lighter than Influx and Grafana, but the setup was so dang easy, and rtl\_433 as InfluxDB support built in, so I went the lazy route :) ^c33779898

- **chaostheory** · [2022-11-28 15:23 UTC](https://news.ycombinator.com/item?id=33774707)
  I haven’t kept up with commercial solutions. Full home automation even with the easy solutions eat up a lot of time especially with light switches. I remember only one brand that might meet the local first requirement. UI was clunky. [https://hubitat.com/](<https://hubitat.com/>) ^c33774707

  Imo I’d go open source for the hub. Installing it on an older laptop shouldn’t take as much DIY

  [https://www.home-assistant.io/](<https://www.home-assistant.io/>)

  [https://www.openhab.org/](<https://www.openhab.org/>)

  Sadly, you’re probably going to need to do some DIY if local first and air monitoring are your highest priorities

  Edit: I forgot that Apple HomeKit is local first

- **colechristensen** · [2022-11-28 23:54 UTC](https://news.ycombinator.com/item?id=33781649)
  Hey I’m working on exactly this! ^c33781649

  Still brewing at the moment but send me an email at cole.christensen@gmail.com if you’re interested in updates, perhaps a free prototype in a few months.

  The general idea is open hardware sensors you can do whatever you want with along with an optional paid cloud service.

- **ctoth** · [2022-11-28 18:05 UTC](https://news.ycombinator.com/item?id=33777093)
  The Ecowitt series of sensors work well for this, and then you can get the GW1100 gateway to get their readings in Home Assistant. ^c33777093

  \[0\]: [https://smile.amazon.com/ECOWITT-Temperature-Humidity-Partic...](<https://smile.amazon.com/ECOWITT-Temperature-Humidity-Particle-Detection/dp/B08TMC66B1/>)

  \[1\]: [https://smile.amazon.com/Ecowitt-Temperature-Humidity-Atmosp...](<https://smile.amazon.com/Ecowitt-Temperature-Humidity-Atmospheric-Pressure/dp/B0978XLG8T>)

  \[2\]: [https://www.home-assistant.io/integrations/ecowitt/](<https://www.home-assistant.io/integrations/ecowitt/>)

- **yobbo** · [2022-11-28 20:33 UTC](https://news.ycombinator.com/item?id=33779170)
  You could try searching for "air quality sensor" on aliexpress. I have experience with this one \[0\] which purports to measure particles in various units, and I suspect it to be 20-30\% inaccurate. The figure it gives for humidity is about 10-20\% off from other cheap devices, but the sensor might be more accurate given that the device runs on USB and emits a non-zero amount of heat, which affects the local measurement. It supports data exports in real time over USB serial. ^c33779170

  \[0\] [https://www.aliexpress.com/item/4001127955294.html](<https://www.aliexpress.com/item/4001127955294.html>)

- **bithaze** · [2022-11-28 15:42 UTC](https://news.ycombinator.com/item?id=33774955)
  I have a couple Eve Room air quality monitors\[0\] and like them. You do need the iOS app to view and export (XLSX format) historical data, but there's no cloud service or anything to sign up for. I charge them about once a month and usually look at the graphs every couple of days so I'll see then when a battery is getting low. The only other "smart" devices I have in my home are some lightbulbs, though, so I don't have any automation set up using the temperature or air quality. ^c33774955

  \[0\] [https://www.evehome.com/en-us/eve-room](<https://www.evehome.com/en-us/eve-room>)

- **troysk** · [2022-11-28 18:11 UTC](https://news.ycombinator.com/item?id=33777173)
  I have found sensors of air purifiers to be better than DIY or standalone ones. Dyson and Xiaomi have local endpoints which can be used to access data without access to internet. Home Assistant makes the process of collecting and storing data easy with HACS and some plugins. ^c33777173

  You may also try Tuya based solutions which maybe flashed with ESPHome but they mostly use DHT11/14 based sensors and need some soldering.

  Another approach is using a BLE based sensor and then using a BLE to WiFi bridge to get the data into HomeAssistant or similar product which can log the values.

- **stevenhubertron** · [2022-11-29 01:52 UTC](https://news.ycombinator.com/item?id=33782659)
  Home Assistant and Air things devices.  My raspberry Pi uses BTLE to read data off sensor and it's logged there.  I have 3 years of air quality measurements there. ^c33782659

- **Corrspt** · [2022-11-28 15:24 UTC](https://news.ycombinator.com/item?id=33774715)
  Not really what you want, but the Awair Quality sensors have a local API that you can use to fetch the data (not local-first, as you asked, but it works locally and you can disable internet connection) ^c33774715

  [https://support.getawair.com/hc/en-us/articles/360049221014-...](<https://support.getawair.com/hc/en-us/articles/360049221014-Awair-Element-Local-API-Feature>)

- **digitalsushi** · [2022-11-28 15:35 UTC](https://news.ycombinator.com/item?id=33774862)
  I'd kill for a Dylos-to-ESP32 cheat kit. That would be extremely valuable for my woodshop to monitor when I can resume a post-disaster activity. ^c33774862

- **unknown** · [2022-11-28 15:17 UTC](https://news.ycombinator.com/item?id=33774630)
  [deleted] ^c33774630

- **INTPenis** · [2022-11-28 18:28 UTC](https://news.ycombinator.com/item?id=33777465)
  Well, what is it that you're measuring? co2? Particle density? ^c33777465

  You say that you want the sensor to measure what it says on the tin, but maybe you should start by defining what "air quality" means.

  And then maybe you can find some simple one-off components that do all the individual measurements. I for example found a cheap and simple USB connected co2 sensor, that just changes colors based on co2 levels.

  - **TeMPOraL** · [2022-11-28 18:43 UTC](https://news.ycombinator.com/item?id=33777694)
    Particle density, TVOC, CO₂, temperature, humidity. With the first two being most important, the rest being extra. ^c33777694

    My experience so far involved playing with sensors for all of these, except CO₂, that are popular with hobby electronics crowd. Back then I didn't really care about measurement accuracy, I was just goofing around. Since then, I've read all these sensors require significant work to get them to produce stable and reasonably accurate readings.

    As for CO₂, I've only read about the options recently, but apparently the actual sensor is pricey-ish, so even in mass market products, the CO₂ measurement is inferred from TVOC, temp, Rh, and a magic lookup table supplied by the vendor (and accurate only in their test lab). This is the main example of what I meant by not reporting what it says on the tin.

    Now, I'm not necessarily after high-quality absolute measurement values, as long as the relative change is detected correctly. But I don't know the space well enough to go around Aliexpress shopping for components myself, and every company that seems to have done some work to validate results and calibrate their devices also wants to shove their app down my throat, which is a no-go.

- **MisterTea** · [2022-11-28 16:12 UTC](https://news.ycombinator.com/item?id=33775387)
  \> , and that doesn't require some proprietary, expensive, and/or old-school industrial protocols to talk to. ^c33775387

  why is old-school a problem?

  - **mrspuratic** · [2022-11-28 17:20 UTC](https://news.ycombinator.com/item?id=33776367)
    I guess he might mean not working out how to encode EBCDIC into ASN.1 in order to issue command PDUs using modbus-over-IP, or something equally barking... ^c33776367

    - **TeMPOraL** · [2022-11-28 17:40 UTC](https://news.ycombinator.com/item?id=33776666)
      I can deal with it if it's *only* an issue of decoding a byte stream with a simple structure in software, though it would be annoying. But I don't want to get into dealing with some obscure industrial protocols that would require me to spend 3+ digit amounts on specifications, or proprietary clients / servers, or - heaven forbid - some industrial *hardware* for routing or ingesting data. ^c33776666

      I don't have anything against those technologies per se - but I'm just a person doing this for a household, not a plant operator, so I don't want anything that's assuming it'll be a part of 5-digit procurement budgets and multi-person installation projects.

      EDIT: I've *heard of* modbus, my impression is that it's accessible for a hobbyist to read/write/work with, so that by itself is *not* off the table. I suppose I could even deal with OPC UA (I worked with it professionally, and IIRC, there are some open source implementations for client/servers). I don't know much about other protocols used in the industry.

    - **MisterTea** · [2022-11-28 17:35 UTC](https://news.ycombinator.com/item?id=33776579)
      I knew modbus was going to be mentioned. As someone who has written low level modbus software, there's nothing wrong with modbus. The only people who complain about it are people who are bad at data marshaling. ^c33776579

- **dburch1980** · [2022-11-30 17:53 UTC](https://news.ycombinator.com/item?id=33804610)
  Please visit buildinglens.com.  If you would like to talk further, reach out to me via LinkedIn. ^c33804610

  [https://www.linkedin.com/in/david-burchfield-pe-cem-83920233...](<https://www.linkedin.com/in/david-burchfield-pe-cem-83920233/>)

- **igor47** · [2022-11-28 17:34 UTC](https://news.ycombinator.com/item?id=33776577)
  I wrote a thing about this: [https://igor.moomers.org/minimal-viable-air-quality](<https://igor.moomers.org/minimal-viable-air-quality>) ^c33776577

  I still have a few of those pms7003s, if you're in the bay let me know and you can come grab some

  - **TeMPOraL** · [2022-11-28 18:54 UTC](https://news.ycombinator.com/item?id=33777859)
    I'm unfortunately on the other side of the world, but thanks for the offer. The blog post is very informative, I haven't even considered you could query a sensor directly like this from your laptop. I'm going to have a look at the code you posted! ^c33777859

- **latchkey** · [2022-11-28 17:10 UTC](https://news.ycombinator.com/item?id=33776227)
  Since you don't want DIY... I bought a Mila air filter. Has the sensors and the additional benefit of not just monitoring, but also cleaning the air. ^c33776227

  [https://milacares.com/](<https://milacares.com/>)

  - **TeMPOraL** · [2022-11-28 19:14 UTC](https://news.ycombinator.com/item?id=33778131)
    I definitely don't want an air purifier in the same package as the air quality sensors, because they'll be measuring the "microclimate" around the active air purifier, which is not representative of the air quality elsewhere in the room. ^c33778131

    - **latchkey** · [2022-11-28 21:55 UTC](https://news.ycombinator.com/item?id=33780410)
      Air moves all over the place. On almost the lowest setting, Mila filters ALL of the air in my condo several times an hour. If you have a larger house, get more Mila's. ^c33780410

      - **TeMPOraL** · [2022-11-29 02:44 UTC](https://news.ycombinator.com/item?id=33783054)
        What's your SQM and how are you sure that the air on the other side of the condo actually gets cycled through the purifier? I mean, the particulates will diffuse over time, but if there's a steady source of particulates (like outside air, or some accumulation in the house), the steady state will be a gradient, and you won't know that if you rely only on sensors built into the purifier. ^c33783054

        - **latchkey** · [2022-11-29 04:26 UTC](https://news.ycombinator.com/item?id=33783682)
          My place is small and open enough that I only need one Mila. I know it is working because when it senses AQI indoors, eventually the AQI goes to zero. I moved the Mila to another part of the house and the AQI was still zero. ^c33783682

          It is currently running at 20\% fan speed and reporting that it changes the air in the room it is in, 4.2 times per hour.

          A friend of mine, with a much larger house, has 4 Milas. The solution is to get more filters so you're changing the air in the place on a regular enough basis that it keeps the AQI near zero all the time.

          After I got the Mila, there was a noticeable difference in the amount of dust that collected all over the house on a regular basis. I can see it in the filter sock, which I take outside and regularly clean as well.

          The Mila app also integrates with a 3rd party local AQI sensor to show me the 'outdoor' view of things. My indoor AQI is always lower than the outdoor AQI. I consider that a win.

          If I open the windows, the AQI goes up. If I close the windows, the AQI goes down. I live near the ocean, the AQI here is already pretty low.

          Mila definitely does a lot more than just an AQI sensor, it cleans the air.

          - **TeMPOraL** · [2022-11-29 10:10 UTC](https://news.ycombinator.com/item?id=33785696)
            Thanks for being very specific about your environment and use patterns. ^c33785696

            I think a lot depends on how air naturally flows through your apartment. In my case, I doubt one purifier would suffice even for the \~60m² we live in, as I can already tell we have at least four different "zones" that don't want to exchange air unless forced to (e.g. by running the AC fans to stir things up) - I can tell by observing how heat and smells move. It's something that I believe could be corrected, but I need to find a HVAC specialist (or learn enough myself) for it\[0\]. In the meantime, I want to monitor the air quality parameters in all those zones separately, to quantify both how much stuff accumulates in each, and how bad the circulation actually is.

            \> *After I got the Mila, there was a noticeable difference in the amount of dust that collected all over the house on a regular basis. I can see it in the filter sock, which I take outside and regularly clean as well.*

            I very much hope to get that effect. I'm allergic to dust mites, and my children most likely are too (observing them seems to hint at it, but they're too young for it to show up on tests), and I hope that adding air purifiers with HEPA filters will help reduce the household cleaning workload a bit.

            Anyway, I've looked at Mila website, and I'm torn. On the one hand, even if pricey, it's nicely designed and tick the right boxes. Two filters, including the carbon one that seems actually loaded with carbon instead of just pretending. On the other hand, they condemn other vendors for bullshit marketing... and then literally do the same thing. Don't know what to think of that.

            \----

            \[0\] - There's an extra constraint here in that it's an apartment in a block of flats that's been designed primarily for natural/"gravity" ventilation. I've been explicitly told by the HOA operating it that I absolutely cannot put fans into existing grilles and ventilate mechanically, as it will mess up the airflow for the whole building.

            - **latchkey** · [2022-11-29 16:15 UTC](https://news.ycombinator.com/item?id=33789421)
              My background is in running large scale data centers. I've had a lot of experience with airflow management for cooling very hot computers. Airflow is critical. Moving air around is critical. ^c33789421

              If you have 'zones', then you'll need more filters for sure.

              It sounds like you're in a warm environment. I used to live in Vietnam where the air is generally terrible. Do you have one of those AC units in the house on the walls? When was the last time you had them cleaned? I ask because those AC units are horrid... they collect huge amounts of dust and mold and nobody thinks to clean them properly (it isn't easy)... they are basically spraying out nasty shit. If you can, turn them off and get used to the heat. I did that and stopped getting sick all the time. People say running AC makes you sick... it isn't the cold air, it is these nasty units. If it is central AC for your HOA, I'm sure they've never been cleaned... or at least not often enough...

              Mila is definitely a bit of a marketing gimmick, that said, the product is quite nice (noise, design and visual) and another good thing is that their support is excellent. I'm actually on my 3rd unit now because of production defects they've had (and since resolved). Being able to just email them and have them ship me a new unit in a couple days is a really nice aspect of paying a bit of extra money for these things.

              I've also built the 3 filters to a box fan \[0\]. That works extremely well too, but is a lot louder and takes up a lot more space than the Mila, and doesn't look as nice. (The link I give you is kind of the extreme version, you can go a lot simpler than that.)

              I bought the Mila highest end filter. It is excellent. Heavy (clearly full of dense carbon). Well made. The optional, also over priced, sock really helps keep it clean (you could probably make your own with similar fabric). I'm sure the filter will last a couple years in my current relatively clean environment. I also vacuum the filter when I clean the sock, to help it last longer since these things are kind of expensive.

              \[0\] [https://www.youtube.com/watch?v\=lbWiZSsEqPg](<https://www.youtube.com/watch?v=lbWiZSsEqPg>)

- **hedora** · [2022-11-28 15:24 UTC](https://news.ycombinator.com/item?id=33774722)
  I think Ambient Weather weather stations hit all your requirements.  They can log to SD card, come with a display, and expose local only network endpoints.   They can also upload to various web services. ^c33774722

- **ianai** · [2022-11-29 01:53 UTC](https://news.ycombinator.com/item?id=33782670)
  Sensors offline first, but datacenter pricing: infrasensing.com ^c33782670

  - **TeMPOraL** · [2022-11-29 02:11 UTC](https://news.ycombinator.com/item?id=33782810)
    Thanks for the link! Prices are crazy, and some parts look built around the same sensors I could get for 1/10th of the price, but then again it's also plug-and-play and offline-first. Given the alternatives, I'm actually considering it. ^c33782810

    (If they're as robust as they look, it makes me wonder if I could score some second-hand units; something I haven't even considered as a possibility before.)

- **nicpottier** · [2022-11-28 15:17 UTC](https://news.ycombinator.com/item?id=33774627)
  [https://canair.io/index.html](<https://canair.io/index.html>) ^c33774627

  - **TeMPOraL** · [2022-11-28 15:27 UTC](https://news.ycombinator.com/item?id=33774756)
    Thanks! ^c33774756

    Some years ago, I built a sensor kit for a similar project (Luftdaten), but IIRC, the measurement quality of the hardware was... questionable (it did led me to discover that ultrasonic air purifiers will disperse as particulates anything and everything that's dissolved in the water you feed them, though).

    At this point, my area is somewhat saturated with (cloud-connected, proprietary, with penalties for opening up) air quality sensors leased by a local startup - I have access to more outside-air data than I need right now. I'm looking for setup optimized for indoor air in various rooms - so even public clouds are kind of a mismatch here: I don't want to publish this data, and it would only make their aggregate results less accurate.

- **francis-io** · [2022-11-28 18:23 UTC](https://news.ycombinator.com/item?id=33777388)
  Where would you start if you knew nothing about electronics but wanted to create this as a way to learn? ^c33777388

  - **eternityforest** · [2022-11-29 03:52 UTC](https://news.ycombinator.com/item?id=33783497)
    Start with Arduino/ESP32, tons of great tutorials.  Learn how i2c works, kirchoff's circuit law, and ohm's law, and play around in the Falstad simulator that runs in a browser ([https://www.falstad.com/circuit/](<https://www.falstad.com/circuit/>)) ^c33783497

    Then find an appropriate sensor module breakout board and connect things up.

    Other that the very basics, what you should focus on highly depends on whether you're a "Mad science analog tinkerer" or "Ultra modern high tech" kind of person.

    If you're serious about this stuff you probably want to learn 3D printing to make cases.

    I think the most important thing is reasonable expectations. Commercial products take months to design and large teams to handle all the companion apps and stuff.   Either keep your project very simple, use off the shelf stuff wherever possible, or be prepared to spend a lot of time on it.

    And be aware of the time and effort required in physically assembling things.

    Despite having done this stuff for years, I still don't actually have any custom hardware in use at home, because commercial stuff is 80\% good enough, and has warrantee support and all kinds of features that would be a bit time consuming to DIY.

- **brainzap** · [2022-11-28 21:14 UTC](https://news.ycombinator.com/item?id=33779771)
  all HomeKit devices can be controlled locally ^c33779771

- **vonnieda** · [2022-11-28 17:18 UTC](https://news.ycombinator.com/item?id=33776347)
  TL;DR: Zwave and Zigbee are (almost) always local first. Home Assistant is great. Almost all CO2 sensors are bad. ^c33776347

  I have the same goals with my setup, and I've been tinkering with home automation for a couple decades now, so I'll share what I've learned so far.

  First, specifically for indoor air quality, and especially for real CO2, the options are terrible. eCO2 sensors are a dime a dozen, but they are awful. For real CO2 everything seems to be super industrial or cloud junk.

  I'm using a variation on [https://hackaday.io/project/186682-co2-buddy](<https://hackaday.io/project/186682-co2-buddy>) for CO2. It uses a high quality sensor and is really just three parts, or two if you don't want LEDs. You flash the ESP32 with esphome and then Home Assistant does the rest. Someone, maybe me, should build and sell these.

  For PM2.5 I use a bunch of modified Vindriktning from IKEA. I added a tiny ESP32 board, soldered four wires, and installed esphome. I modified four in about an hour one evening. Someone, maybe me, should build and sell these.

  For temperature and humidity I love the "Aqara Temperature and Humidity Sensor". I sprinkle these liberally around the house. They are Zigbee, so local by default. In fact, when shopping for home automation stuff, if you see something that "requires Hub" it usually means its either Zwave or ZigBee and will work just fine directly.

  Home Assistant for control, data storage, graphing, dashboards, etc. It's free, open source, gets high quality monthly updates, good looking and responsive iOS and Android apps, great web interface, and most important to your question: has extremely good documentation when it comes to what is supported.

  Take a look at the Integration page for Phillips Hue, for instance: [https://www.home-assistant.io/integrations/hue/](<https://www.home-assistant.io/integrations/hue/>). It's marked as "Local Push" which is the keyword you want for stuff that doesn't need someone else's cloud.

  [https://www.home-assistant.io/blog/2016/02/12/classifying-th...](<https://www.home-assistant.io/blog/2016/02/12/classifying-the-internet-of-things/#classifiers>)

  So, when I am shopping for a new class of device, I always first check the Home Assistant integration page for it and see what the support is like. There will often be helpful comments and FAQs on the page.

  In general, if something is Zwave or Zigbee it will be trivial to get it working local first. If it's WiFi there's probably going to at least be an app and a cloud that you have to use to setup and it's a toss up whether you can then use it without a constant cloud connection.

  If you've made it this far, here's some other recommendations for solid local first Home Assistant compatible goodies:

  \- Hue lights. I've tried Feit, Sengled, LiFX, Hue, and various big box store white label junk. Hue just works. They are expensive, but they work great and I never, ever have a single problem with them. Phillips doesn't make it obvious but Hue's hub is just Zigbee and you can talk Zigbee directly from Home Assistant to Hue lights. You can do the initial setup over Bluetooth using their app and then never use it again. LiFX are WiFi and are a solid runner up, but basically the same price.

  \- Zooz wall switches and dimmers.

  \- Zooz 4-in-1 Sensor is a great temperature, humidity, illuminance, and motion sensor. I use these in places where I want motion sensing in place of the Aqara temperature and humidity.

  \- Zooz Water Leak Sensors.

  \- Zooz window and door open sensors.

  \- Bond Bridge for 400MHz RF remotes - ceiling fans in my case. Like Hue, set it up using the app, then just run it with Home Assistant.

  \- Minoston Z-Wave Plug with Energy Monitor for plug in switches with energy monitoring.

  - **TeMPOraL** · [2022-11-28 19:20 UTC](https://news.ycombinator.com/item?id=33778221)
    Thanks for sharing! That's tremendously helpful. What you describe sounds exactly like the system I want to build up over time. I'll look into Zwave and Zigbee options. ^c33778221

    I've actually stumbled on the images of that "CO₂ Buddy" a day or two ago, but dismissed it because I thought it's fundamentally designed around the LEDs, which I don't want.

- **bobleeswagger** · [2022-11-28 16:12 UTC](https://news.ycombinator.com/item?id=33775377)
  YoLink isn't "local first" yet but they are aware it is an issue to be solved. They use LoRa. ^c33775377

- **siyang\_z** · [2022-11-28 18:38 UTC](https://news.ycombinator.com/item?id=33777613)
  [flagged] ^c33777613

  \[dead\]

- **siyang\_z** · [2022-11-28 18:39 UTC](https://news.ycombinator.com/item?id=33777631)
  [flagged] ^c33777631

  \[dead\]

