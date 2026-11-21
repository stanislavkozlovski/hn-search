# [AirGradient: DIY Air Quality Monitoring with Open-Source Hardware & Firmware](https://news.ycombinator.com/item?id=27124671)

Article: [https://www.airgradient.com/diy/](<https://www.airgradient.com/diy/>)

walterbell · 2021-05-11 22:57 UTC · 74 reported comments · archived 2026-11-08 11:39 UTC
Observation: 2026-11-08 11:39 UTC → 2026-11-08 11:39 UTC

## Comments

- **ahaucnx** · [2021-05-12 01:47 UTC](https://news.ycombinator.com/item?id=27125763)
  Hi, founder of AirGradient here. Great to see that somebody submitted our open source DIY sensor instructions here! ^c27125763

  As last time I am more than happy to send free PCBs to anybody who wants to build this sensor. It makes the build much easier as you don't have a lot of cables to handle. You just need to paypal me the postage fees.

  If you like to get some, please press the orange button on the website and send me a message.

  - **DoingIsLearning** · [2021-05-12 07:43 UTC](https://news.ycombinator.com/item?id=27127755)
    I have a question about calibration, have you tried measuring the CO2 sensor and PM sensor against a known calibrated sensor? ^c27127755

    They will always give a useful 'relative change' indication but how does the SenseAir and the Plantower sensors compare with more expensive measurement equipment?

  - **pugio** · [2021-05-12 04:29 UTC](https://news.ycombinator.com/item?id=27126592)
    Thank you for this. As someone who lived through the hellish airscape of last year's Australian bushfires, and spent quite a bit of time discussing, advising, and publicizing air quality concerns, efforts like this are sorely needed. ^c27126592

    At this point I've been recommending people buy PurpleAir monitors for grassroots air quality monitoring, but this looks like a really great DIY option.

    I'm particularly excited about the CO2 sensor, since until this point I've been focused mostly on PM2.5 and PM10 particles, but am really keen to figure out if my stuffy apartment bedroom (and  baby's room) is reaching too high CO2 levels at night (with corresponding headaches and impact on cognitive performance).

    - **ahaucnx** · [2021-05-12 04:37 UTC](https://news.ycombinator.com/item?id=27126640)
      Yes, often when you seal your house to keep PM2.5 low, your CO2 values go up. ^c27126640

      We measures this in classrooms \[1\] and I also wrote about the benefits of positive pressure systems to have near zero PM2.5 and low CO2 at the same time \[2\] even on heavily polluted days.

      \[1\] [https://www.airgradient.com/resources/we-measured-the-co2-le...](<https://www.airgradient.com/resources/we-measured-the-co2-level-in-a-classrooms-this-is-what-we-found-out/>)

      \[2\] [https://www.airgradient.com/resources/positive-pressure-syst...](<https://www.airgradient.com/resources/positive-pressure-systems-for-clean-air/>)

      - **metb** · [2021-05-12 09:52 UTC](https://news.ycombinator.com/item?id=27128501)
        Are the CO2 levels mentioned in \[2\] above from an air conditioned room? This detail is not mentioned in the article. I am trying to understand if air exchange provided by the air conditioner makes any difference on reducing CO2 levels in the room. ^c27128501

    - **clairity** · [2021-05-12 16:29 UTC](https://news.ycombinator.com/item?id=27132159)
      being largely human-made and relatively recently created, pm (particulate matter) and voc’s (volatile organic compounds), and perhaps rarer (but potent) pollutants like ozone, carbon monoxide, and radon, are important to monitor for health. note that co2, while fashionable to be concerned about these days, is not a significant health concern (life evolved in relatively significant concentrations of co2) beyond suffocations at extremely high concentrations. ^c27132159

  - **walterbell** · [2021-05-12 02:10 UTC](https://news.ycombinator.com/item?id=27125881)
    Are you able to share the AirGradient business model, which allows the company to support publication of open-source docs, software and hardware for DIY air sensors? ^c27125881

    The guide is much appreciated!

    - **ahaucnx** · [2021-05-12 02:41 UTC](https://news.ycombinator.com/item?id=27126024)
      We are based in Northern Thailand which is impacted by seasonal wildfires with very high levels of PM2.5. ^c27126024

      AirGradient originally developed out of our desire to help our school to manage the air quality during this time of the year more effectively and to ensure that our kids breathe healthy air inside the classroom.

      Most of the benefits come from our cloud platform that analyses the air quality data sent from the sensors and provides real time alerts and communication to the relevant staff (e.g. PE teachers when air quality gets worse).

      It has also some unique features like integration of the school air quality policy. More information is on our website \[1\].

      This service comes with our professional air quality monitor which has additional hardware components to achieve a very high degree of reliability.

      We provide the open source version due to a desire to empower as many people as possible to measure the air quality in their environment and thus reduce their health risks due to bad air.

      It also helps us to get customers onto our air monitoring platform in countries where our sensor is not available yet. A day care center in California for example build 12 DIY sensors and connected them to our platform to measure the indoor air quality in its classrooms.

      Currently we have a strong focus on schools and if anyone of you has a connection to a school and is interested to learn more about how our platform could help, please get in touch with me.

      \[1\] [https://www.airgradient.com/schools/](<https://www.airgradient.com/schools/>)

      - **spamalot159** · [2021-05-12 06:13 UTC](https://news.ycombinator.com/item?id=27127215)
        Very cool that this got posted today! I am visiting Chiang Mai this week from the province of Phichit where I teach English. I sent you an email at the support address. ^c27127215

  - **saltcured** · [2021-05-12 23:51 UTC](https://news.ycombinator.com/item?id=27136657)
    Can you share any thoughts on a similar DIY project for outdoor air monitoring? ^c27136657

    I.e. is it feasible to make something battery powered and connected to an indoor base station or gateway via some low power radio link (bluetooth low-energy?  z-wave?).  Would these same sensors work outdoors or quickly fail due to harsh environment?

    How complex would it be to make a housing that is sufficiently weather proof yet coupled to the environment to read ambient environmental conditions?  I can imagine sun exposure, wind, high dust loads, rain, and condensing humidity all being very challenging for a DIY device to stick out in a yard or balcony.

  - **TedDoesntTalk** · [2021-05-12 02:33 UTC](https://news.ycombinator.com/item?id=27125975)
    Serious question: what happens to air quality while I’m soldering all of those components? I have always wondered how toxic solder and flux fumes are. ^c27125975

    - **ahaucnx** · [2021-05-12 02:46 UTC](https://news.ycombinator.com/item?id=27126045)
      When I solder, PM2.5 goes into very unhealthy territory. There are solder smoke absorbers with carbon filters that I would recommend to use. ^c27126045

      - **TedDoesntTalk** · [2021-05-12 02:57 UTC](https://news.ycombinator.com/item?id=27126098)
        Any solder smoke absorber recommendations? I’ve never heard of those. ^c27126098

        - **jfim** · [2021-05-12 03:18 UTC](https://news.ycombinator.com/item?id=27126220)
          I bought the Aven 17701 recently, it seems to do the job. It's just a fan with an activated carbon filter. ^c27126220

        - **sizzle** · [2021-05-12 07:40 UTC](https://news.ycombinator.com/item?id=27127735)
          Yeah just do it outside if possible with a makeshift work bench ^c27127735

          - **TedDoesntTalk** · [2021-05-12 12:04 UTC](https://news.ycombinator.com/item?id=27129302)
            That's fine this time of year but not in winter. ^c27129302

    - **cinntaile** · [2021-05-12 02:40 UTC](https://news.ycombinator.com/item?id=27126007)
      Breathing in fumes is never healthy. That's why you have filters that suck the solder fumes away. ^c27126007

  - **sberder** · [2021-05-12 08:45 UTC](https://news.ycombinator.com/item?id=27128150)
    How would you say this fares against a kaiterra or tongdy machine for example?
    With diy projects, I'm always concerned about managing temperature and humidity impact on readings, especially on sensors like the plantower.
    I've had issues in the past with monitors in very humid environments like Thailand and Singapore. ^c27128150

    Disclaimer: I also run an environment data platform business

  - **sundvor** · [2021-05-12 10:48 UTC](https://news.ycombinator.com/item?id=27128778)
    Amazing work, and I love how you have a focus on schools. My son's old school was adjacent to a major thoroughfare here in Melbourne, Victoria, and it was the biggest negative with it for me. Only for a year, but I'm hopeful too much damage wasn't done. ^c27128778

    Would love a full package sensor like this for our own house (I have three purifiers..) so I'll get in touch once I've learned soldering, which requires acquiring the necessary tools.

  - **sniglom** · [2021-05-21 15:21 UTC](https://news.ycombinator.com/item?id=27235205)
    How does this project compare to luftdaten? Have you considered if the projects could share data? ^c27235205

    [https://sensor.community/en/sensors/airrohr/](<https://sensor.community/en/sensors/airrohr/>)

  - **amatecha** · [2021-05-12 05:07 UTC](https://news.ycombinator.com/item?id=27126798)
    Hey there, I sent a contact on the site but I didn't get any response.  Same username @ a common email provider.  Would love a free PCB if possible!  No worries if you've run out or anything, of course.  :) ^c27126798

    - **losvedir** · [2021-05-12 13:28 UTC](https://news.ycombinator.com/item?id=27130066)
      Just FYI for others, I also sent a contact on the site last time around, but I actually did get a response. It took maybe a week or so, but they're probably very busy! ^c27130066

    - **ahaucnx** · [2021-05-12 05:35 UTC](https://news.ycombinator.com/item?id=27126976)
      I got your message. Will reply to all messages later tonight. ^c27126976

      - **amatecha** · [2021-05-12 05:37 UTC](https://news.ycombinator.com/item?id=27126987)
        no worries!  Cheers :) ^c27126987

  - **cinntaile** · [2021-05-12 02:35 UTC](https://news.ycombinator.com/item?id=27125989)
    I might take you up on this offer, where are you sending from? ^c27125989

    - **ahaucnx** · [2021-05-12 02:42 UTC](https://news.ycombinator.com/item?id=27126027)
      We are based in Thailand. Normally it takes around 3 weeks to arrive. ^c27126027

- **2bluesc** · [2021-05-12 00:53 UTC](https://news.ycombinator.com/item?id=27125444)
  I built a similar thing last year affectionately named "Sniffer"\[0\].  My build uses the newer PMSA003. ^c27125444

  \* Uses an ESP32 + ESPHome + PMSA003 + BME680.

  \* Data collection is via MQTT -\> HomeAssistant -\> InfluxDB -\> Grafana.

  \* Software and PCB design files are on Github\[1\].

  Looks like adding the SenseAir CO2 module would be trivial with ESPHome\[2\]

  \[0\] [https://blog.kylemanna.com/hardware/sniffer-air-quality-moni...](<https://blog.kylemanna.com/hardware/sniffer-air-quality-monitor-aqi-using-esp32-pmsa003-bme680/>)

  \[1\] [https://github.com/kylemanna/sniffer](<https://github.com/kylemanna/sniffer>)

  \[2\] [https://esphome.io/components/sensor/senseair.html](<https://esphome.io/components/sensor/senseair.html>)

  - **jfim** · [2021-05-12 03:09 UTC](https://news.ycombinator.com/item?id=27126170)
    Haha, did something similar too, except it logs to a server written in Elixir and has a Phoenix live view dashboard, which I check on an eink display and on my phone. Data is also logged to CSV at 1Hz and can be analyzed in R. ^c27126170

    Code is also on GitHub.

    [https://blog.jean-francois.im/2021/05/08/building-a-simple-a...](<https://blog.jean-francois.im/2021/05/08/building-a-simple-air-quality-monitor/>)

    [https://github.com/jfim/air-quality-server](<https://github.com/jfim/air-quality-server>)

    [https://github.com/jfim/air-quality-monitor-firmware](<https://github.com/jfim/air-quality-monitor-firmware>)

  - **beachy** · [2021-05-12 01:16 UTC](https://news.ycombinator.com/item?id=27125586)
    Nice. I chose the TTGO Display for my project to measure levels in my water tanks. It's a great board, though the ADC is rubbish. ^c27125586

    Unfortunately prices are on the move now (presume the chip shortage) and they now cost 2x what they were a few weeks ago.

  - **ahaucnx** · [2021-05-12 02:02 UTC](https://news.ycombinator.com/item?id=27125843)
    Nice project! ^c27125843

    How was your experience with the PMSA003? We used it before but believe that the PMS5003 has more stable readings and a longer life time.

    - **2bluesc** · [2021-05-13 05:16 UTC](https://news.ycombinator.com/item?id=27138665)
      Never bought a PMS5003, couldn't find any real data suggesting it was better.  The only indication I had was the PMSA003 was newer, so I ran with it. ^c27138665

      I've had one running 24/7 for 9 months now with no issues.  I checked the accuracy outdoors relative to PurpleAir sensors in the area and they were with a percent or two which was pretty close for such a simple experiment.

  - **jfim** · [2021-05-12 05:19 UTC](https://news.ycombinator.com/item?id=27126880)
    Nice compact board, by the way, and it's pretty cool that you got it working with grafana! ^c27126880

- **acidburnNSA** · [2021-05-12 05:07 UTC](https://news.ycombinator.com/item?id=27126802)
  I made a set of DIY weather station/air quality monitors at the beginning of COVID. ^c27126802

  I have lots of little noises for various things that trigger via Home Assistant. Like when outdoor air quality spikes, I get one noise (usually neighbor having a cigar, leaf blower nearby, someone with a wood stove, etc.) If indoor air quality spikes I get another one (dry shampoo, burned pancakes, etc really set it off).

  During fire seasons, balancing CO2 with PM2.5 is hard. Best move after many days was to put the box fan with filter in the window to blow filtered air in. I figure it's basically a mini version of those huge HVAC intake fans on skyscrapers.

  Home assistant talks to the stations over MQTT over local wifi, no cloud, remote access over vpn when needed. Lots of fun! Happy to see fancier and better put together packages like this out there to spread the joy of ambient air quality monitoring.

  [https://partofthething.com/thoughts/weather-and-air-quality-...](<https://partofthething.com/thoughts/weather-and-air-quality-monitoring-station-with-esp8266-and-home-assistant/>)

  - **PietdeVries** · [2021-05-12 05:43 UTC](https://news.ycombinator.com/item?id=27127025)
    For the (north) Europeans here, there is a German project Luftdaten (also available in English) that does more or less the same \[1\]. Provides guides for air quality measurement devices \[2\], firmware and a 'worldwide' map that shows the location and measurement of each device. They have around 14.000 at the moment, mainly in Germany and the Netherlands. The device works with Domoticz, so you can get the read-out integrated in your dashboard. Shows temperature, humidity and PM10 & PM2.5 - very happy with mine! ^c27127025

    \[1\] [https://sensor.community/en/](<https://sensor.community/en/>)
    \[2\] [https://sensor.community/en/sensors/airrohr/](<https://sensor.community/en/sensors/airrohr/>)

    - **bodo11** · [2021-05-12 07:15 UTC](https://news.ycombinator.com/item?id=27127606)
      I second this! I've been sending sensor data into the [https://sensor.community](<https://sensor.community>) cloud for over a year now, with dead simple setup and forget-about-it attitude since then. For the lazy there is also an option of spending \~50€ for a plug-and-play version \[1\]. Independently of that, you also get a grafana web GUI after registering your chip, e.g. \[2\].
      On another note, I hope these databases from similar projects stay mergable or the projects even merge. ^c27127606

      \[1\] [https://nettigo.eu/products/sensor-community-kit-sds011-bme2...](<https://nettigo.eu/products/sensor-community-kit-sds011-bme280-english-language>)
      \[2\] [https://api-rrd.madavi.de/grafana/d/q87EBfWGk/temperature-hu...](<https://api-rrd.madavi.de/grafana/d/q87EBfWGk/temperature-humidity-pressure?orgId=1&var-chipID=esp32-115a65334fc4>)

- **rauhallinen** · [2021-05-12 05:41 UTC](https://news.ycombinator.com/item?id=27127008)
  There's an ongoing trend in miniaturizing optical spectrometers \[1\]. MEMS-FTIRs should have interesting application in air analysis \[2,3\]. ^c27127008

  Real-time gas measurements are quite routine and mandatory in industry \[4\]. Wider spread of analytical chemistry technology to consumers will lead to a better world - pregnancy tests, insulin meters, breathalyzers are just the beginning :)

  1\. Z. Yang, T. Albrow-Owen, W. Cai, T. Hasan, Miniaturization of optical spectrometers. Science. 371 (2021), doi:10.1126/science.abe0722.

  2\. M. Erfan, Y. M. Sabry, M. Sakr, B. Mortada, M. Medhat, D. Khalil, On-Chip Micro–Electro–Mechanical System Fourier Transform Infrared (MEMS FT-IR) Spectrometer-Based Gas Sensing. Appl. Spectrosc. 70, 897–904 (2016).

  3\. A. Fathy, Y. M. Sabry, S. Nazeer, T. Bourouina, D. A. Khalil, On-chip parallel Fourier transform spectrometer for broadband selective infrared spectral sensing. Microsystems & Nanoengineering. 6, 10 (2020).

  4\. Eg. [https://www.gasmet.com/](<https://www.gasmet.com/>)

- **Havoc** · [2021-05-11 23:52 UTC](https://news.ycombinator.com/item?id=27125060)
  Is that Co2 sensor reliable? I've been googling sensors lately and CO2 seems to be a mine field. Hard to tell what is a CO2 sensor and what is a VOC/CO2 equivalent sensor... ^c27125060

  - **ahaucnx** · [2021-05-12 01:50 UTC](https://news.ycombinator.com/item?id=27125785)
    Yes the senseair S8 is very reliable. Our professional air quality sensor uses the same CO2 sensor and we have hundreds of them deployed without a single one failing so far. ^c27125785

    Only need to keep in mind that the baseline calibration sometimes needs 1-2 weeks to kick in but you can also force a manual calibration.

    In general NDIR CO2 sensors are quite reliable but you should stay away from TVOC sensors that give an eCO2 (estimated CO2) value. These are often very off and I would not recommend to use TVOC sensors for CO2 measurement.

    - **nmaggioni** · [2021-05-12 11:10 UTC](https://news.ycombinator.com/item?id=27128936)
      Have you ever experienced spikes in the S8's readings? Mine seems to underflow and wraparound every once in a while for no apparent reason or when exposed to fresh air for prolonged periods of time. I tried recalibrating it on the 400ppm baseline a few times but the issue hasn't gone away. ^c27128936

    - **SilverRed** · [2021-05-12 03:45 UTC](https://news.ycombinator.com/item?id=27126360)
      How does the calibration work? I saw comments saying you have to get a canister with a known co2 content and run it through to calibrate. Do these home sensors just assume the outside level is a fixed value and calibrate to that? ^c27126360

      - **jfim** · [2021-05-12 04:49 UTC](https://news.ycombinator.com/item?id=27126706)
        It assumes that the sensor is exposed to fresh air every once in a while, and that fresh air is at 400 ppm CO2. It'll basically slowly lower its baseline calibration over several days, and if the value ever drops below 400 ppm it'll increase the baseline calibration relatively rapidly. ^c27126706

        It can be disabled via a command IIRC.

        - **agurk** · [2021-05-12 08:06 UTC](https://news.ycombinator.com/item?id=27127919)
          Isn't this approach flawed as it look like seasonal lows of CO2 \[0\] are above 400ppm are are going to continue rising making the alignment drift even further out. Is there any way to adjust the calibration with the expected low CO2 readings? ^c27127919

          \[0\] [https://www.co2.earth/seasonal-co2-cycle](<https://www.co2.earth/seasonal-co2-cycle>)

          - **jfim** · [2021-05-12 13:37 UTC](https://news.ycombinator.com/item?id=27130165)
            In theory yes, but in practice any sensor that's not regularly calibrated against a well known reference (eg. a chamber with 0 ppm CO2) will always be off somewhat. ^c27130165

            This automatic calibration just ensures that the sensor is in the right ballpark, but if a 10-20 ppm absolute difference in CO2 concentration is important for your application, you'll need a better sensor and/or calibration procedure than the automatic background calibration.

            Realistically, for home applications, it'll be more like CO2 \< 500 ppm, things are good, above 700, might be time to consider opening the windows, above 1000, definitely time to open the windows. For that kind of application, being off by 10-20 ppm doesn't really matter too much.

            On a side note, it is pretty disheartening to think that the 400 ppm CO2 background level was accurate a few years ago when the sensors were designed, and that in the span of a few years that background reference is now off.

    - **Havoc** · [2021-05-13 19:04 UTC](https://news.ycombinator.com/item?id=27145998)
      \>Yes the senseair S8 is very reliable. Our professional air quality sensor uses the same CO2 sensor ^c27145998

      Thanks!

  - **dheera** · [2021-05-12 01:40 UTC](https://news.ycombinator.com/item?id=27125722)
    You want an NDIR CO2 sensor such as an SCD30 or a T6713 and not an electrochemical sensor. ^c27125722

    Electrochemical sensors respond to CO2 and other VOC gases and give you an "eCO2" reading, and you can never be really sure if it measured CO2 or something else, and require frequent calibration. They suck.

    NDIR CO2 sensors work by emitting IR light and measuring the CO2 by its IR absorption band, and are much more accurate at singling out only CO2 among other gases.

  - **parsecs** · [2021-05-11 23:59 UTC](https://news.ycombinator.com/item?id=27125110)
    Pardon my lack of knowledge, but what's wrong about an equivalent type sensor? ^c27125110

    - **NortySpock** · [2021-05-12 00:08 UTC](https://news.ycombinator.com/item?id=27125167)
      VOC: Volatile organic compounds -- aerosolized oils, greases, perfumes, "bad smells", solvents, exhaled breath which would contain normal biological material, or anything else having to do with carbon compounds ^c27125167

      A VOC/CO2 equivalent sensor is measuring VOCs and using them as a proxy to estimate CO2 concentration levels. 
      CO2 is of course fairly non-reactive so it'd difficult (read: expensive) to make a chemical sensor for this. VOCs are more reactive and easier to make a sensor for.

      Basically, you're getting a sensor for VOCs that, based on some assumptions about outdoor or indoor air quality, is then being used to estimate CO2 levels.

      This is fine if all you want is a loose estimate, but if you have reason to think your VOC/CO2 ratios are going to be different than "usual" (e.g. a CO2 storage facility, next to a poorly maintained combustion system) or where CO2 detection is of paramount importance (e.g. life-or-death situations), then a VOC detector is not acceptable.

      EDIT: tried to improve the VOC examples

      - **parsecs** · [2021-05-12 00:20 UTC](https://news.ycombinator.com/item?id=27125245)
        Some of the CO2 sensors that I worked with use separate signals for deriving estimated VOC and CO2. For example the Senserion SGP30 \[1\] measures ethanol and H2, and uses H2 to determine eCO2 value. Indeed the Senseair S8 \[2\] used in AirGradient seem to feature a "more direct" NDIR CO2 sensor, so there's not really any issues there. ^c27125245

        Is using H2 to detect CO2 "good enough" for all non life-or-death situations?

        Edit: And to clarify, I was mainly asking the parent comment as to what is their application that demand NDIR or "more direct" CO2 sensors.

        \[1\] [https://www.sensirion.com/fileadmin/user\_upload/customers/se...](<https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9_Gas_Sensors/Datasheets/Sensirion_Gas_Sensors_Datasheet_SGP30.pdf>)
        \[2\] [https://rmtplusstoragesenseair.blob.core.windows.net/docs/pu...](<https://rmtplusstoragesenseair.blob.core.windows.net/docs/publicerat/PSP107.pdf>)

        - **jfim** · [2021-05-12 05:45 UTC](https://news.ycombinator.com/item?id=27127028)
          It seems alright if you do use the humidity compensation. It might be off by 100 ppm or so, and wildly off if there are a lot of VOCs in the air, but if you're just using it as a "should I open the windows" kind of thing it'll do fine IMHO. ^c27127028

          For example, the two sensors I have right now, with the windows open, the S8s report 478 and 455 ppm of CO2, while the SGP30s report 400 and 405 respectively. Without having calibrated instruments it's hard to know if any of these values are good, but they seem at least not too wildly off.

          The SGP30 is a lot more compact and much less of an energy pig than the S8; the S8 will actually take so much current on the 5V rail that it'll cause the voltage to sag if you're powering it through USB with other devices connected ([https://blog.jean-francois.im/2021/05/08/building-a-simple-a...](<https://blog.jean-francois.im/2021/05/08/building-a-simple-air-quality-monitor/images/5v-rail-scope.jpg>)). It's also a lot cheaper.

          However, the SGP30 approximation can be off by a bit, and the calculation of the humidity value to give the sensor is a bit gnarly ([https://github.com/jfim/air-quality-monitor-firmware/blob/ma...](<https://github.com/jfim/air-quality-monitor-firmware/blob/master/src/main.cpp#L478>)). It's also pretty obvious that the SGP30 has a hardcoded floor of 400 ppm CO2eq and that it won't ever return a value lower than that.

      - **ahaucnx** · [2021-05-12 01:54 UTC](https://news.ycombinator.com/item?id=27125803)
        Sometimes even the loose estimates are totally off because most of the time the eCO2 correlates with the TVOC measurement. For example I triggered a TVOC sensor with suncream smell in a very low CO2 room and the CO2 wenth through the roof. ^c27125803

    - **the\_pwner224** · [2021-05-12 00:02 UTC](https://news.ycombinator.com/item?id=27125125)
      Those basically measure VOCs and use that to guess what the CO2 concentration is (the two are often correlated, or something like that). So the 'CO2' reading they give is often inaccurate, and can be heavily manipulated by the presence of certain gases/VOCs. The one that AirGradient has chosen is a true CO2 sensor, AFAIK. ^c27125125

- **dheera** · [2021-05-12 01:36 UTC](https://news.ycombinator.com/item?id=27125710)
  I built one as well, and with a whole bunch of other sensors (CO, CO2, alcohol/VOC, O3, PM2.5, PM10, humidity, magnetic field, IMU to detect earthquakes, and even a Geiger counter). ^c27125710

  [https://dheera.net/projects/airmonitor/](<https://dheera.net/projects/airmonitor/>)

  Only problem is I found the PMSA003I always reports PM2.5 \= 0 when actual values are anywhere below 100ish. It only begins to detect after that.

  - **ahaucnx** · [2021-05-12 02:11 UTC](https://news.ycombinator.com/item?id=27125890)
    We also had issues with the PMSA003. Better use the PMS5003 that is code compatible and has a better reliability. ^c27125890

    - **dheera** · [2021-05-12 02:57 UTC](https://news.ycombinator.com/item?id=27126097)
      Thanks, I didn't realize that. Will give it a try. ^c27126097

- **hanniabu** · [2021-05-12 00:08 UTC](https://news.ycombinator.com/item?id=27125164)
  What are other decentralized open science collection projects like this that we can participate in? ^c27125164

  Edit: Site finally loaded (HN HoD), is this actually a decentralized monitoring program? From reading, it kinda sounds like it's just for your own monitoring rather than aggregating the data to give a broader picture across the globe.

  - **ahaucnx** · [2021-05-12 02:09 UTC](https://news.ycombinator.com/item?id=27125877)
    Our main product is a platform for indoor air quality monitoring targeting schools \[1\] and offices. ^c27125877

    We have a professional sensor but also the open source/open hardware version that can be connected to our platform.

    Alternatively you can send the data to any other platform or use it as an offline monitor. There are many citizen science projects that have open API's that you could send data to.

    \[1\] [https://www.airgradient.com/schools/](<https://www.airgradient.com/schools/>)

  - **MattRix** · [2021-05-12 00:41 UTC](https://news.ycombinator.com/item?id=27125366)
    There are already many sources of outdoor air quality data, you can find maps like this, for example: [https://aqicn.org/map/world/](<https://aqicn.org/map/world/>) ^c27125366

    Monitoring household/office/school indoor air quality seems to be a relatively new trend, but the impact of indoor air quality is actually quite strong so it makes sense.

    - **bumby** · [2021-05-17 17:38 UTC](https://news.ycombinator.com/item?id=27185987)
      It’s not a terribly new idea. Demand-controlled ventilation has been around for decades (where ventilation is governed by air sampling, usually CO2). The reasoning seems to be a recent trend is that it’s more economical to implement ^c27185987

  - **unknown** · [2021-05-12 01:34 UTC](https://news.ycombinator.com/item?id=27125698)
    [deleted] ^c27125698

  - **hpb42** · [2021-05-12 14:07 UTC](https://news.ycombinator.com/item?id=27130484)
    There's one for radiation monitoring: [https://radmon.org](<https://radmon.org>) ^c27130484

- **smnv** · [2021-05-12 11:21 UTC](https://news.ycombinator.com/item?id=27129014)
  From the consumer side: ^c27129014

  I've bought a Qingping ClearGrass Air Monitor (CGS1). It costs about \$100, but has CO2, tVoc, PM 2.5, PM 1.0, temperature and humidity sensors. From what I've read, sensors are quite good, people only sometimes complaining for bad fans, that need to be fixed after a year or so of use. Everything in one nice USB-C powered case with a sensor screen. A bit too much animation once a minute, that can't be disabled. Data is sent by WiFi.

  There is a Qingping App for Android and IOS with some graphs and insight into values, but not much. It also can be integrated with Mi Home, but doesn't work for my region, and I can't get token to talk to it with python-miio, as in this habr example \[1\]. This example doesn't work too \[2\], looks like the api has changed.

  So after a bit of sniffing I've made a simpler solution:

  1\. Installed Mosquitto MQTT Broker on my home gateway

  2\. Made a DNAT redirect of qing.cleargrass.com requests to this broker:


  ```
    iptables -t nat -A PREROUTING -i br-lan -p tcp -d qing.cleargrass.com --dport 11883 -j DNAT --to-destination 127.0.0.1:11883
  ```

  
  3\. Added a cron job of periodic subscribing for air monitor data. Without this message it doesn't push the data. The topic consists of some base64 uid and air monitor MAC address, I wrote it in square brackets, should be changed by end user:


  ```
    */5 * * * * /usr/bin/mosquitto_pub -h 127.0.0.1 -p 11883 -t '/[uid]/[mac]/user/get' -m '{"duration":"303","up_itvl":"2","type":"12"}'
  ```

  
  4\. Configured a mqtt\_consumer in telegraf:


  ```
    [[inputs.mqtt_consumer]]
      servers = ["tcp://127.0.0.1:11883"]
      name_override = "air_monitor"
      topics = [
        "/+/+/user/update",
      ]
      data_format = "json"
      tag_keys = [
        "mac",
      ]
  ```

  
  5\. Created graphs and alerts in grafana. It was easier for me to create a further automation from there.

  It is sad that there are still no easy way to connect everything in a "smart" home.

  \[1\] [https://habr.com/en/post/482352/\#comment\_21085236](<https://habr.com/en/post/482352/#comment_21085236>)
  \[2\] [https://habr.com/ru/post/493220/](<https://habr.com/ru/post/493220/>)

  Edit: formatting

- **antoniuschan99** · [2021-05-12 03:15 UTC](https://news.ycombinator.com/item?id=27126212)
  The new generation Co2 Sensors use Photoacoustic (instead of Ndir). Sensirion just released theirs and I remember seeing one from Kemet? ^c27126212

  [https://www.sensirion.com/en/environmental-sensors/carbon-di...](<https://www.sensirion.com/en/environmental-sensors/carbon-dioxide-sensors/carbon-dioxide-sensor-scd4x/>)

  Also, Sensirion just announced an all in one pm2.5, temperature, humidity, and voc sensor probably will be released next year

  [https://www.sensirion.com/en/environmental-sensors/environme...](<https://www.sensirion.com/en/environmental-sensors/environmental-sensor-node-sen5x/>)

  - **KEMETelectronic** · [2021-05-13 16:04 UTC](https://news.ycombinator.com/item?id=27143706)
    Here's some KEMET sensor info
    Gas Detection Sensors: [https://www.kemet.com/en/us/sensors.html?t\=960](<https://www.kemet.com/en/us/sensors.html?t=960>) 
    Environmental Sensors Info: [https://www.kemet.com/en/us/applications/sensing.html](<https://www.kemet.com/en/us/applications/sensing.html>) 
    There's more, too. Tag me if you want more info. ^c27143706

  - **jfim** · [2021-05-12 03:21 UTC](https://news.ycombinator.com/item?id=27126243)
    Plantower also has the PTQS1005, although I'm not sure if there's actual English documentation for it. ^c27126243

    - **sberder** · [2021-05-12 09:44 UTC](https://news.ycombinator.com/item?id=27128468)
      The PTQS1005 is a fun machine, TVOC is always a bit of a troublesome sensor but the packaging and data access are very convenient. ^c27128468

- **adamjb** · [2021-05-12 00:07 UTC](https://news.ycombinator.com/item?id=27125148)
  The person was who runs this occasionally pops up around here ^c27125148

  [https://news.ycombinator.com/user?id\=ahaucnx](<https://news.ycombinator.com/user?id=ahaucnx>)

- **throwaway32231** · [2021-05-12 10:26 UTC](https://news.ycombinator.com/item?id=27128678)
  HINT: if you want a particulate sensor and don't want to solder anything, buy an SDS011 with USB interface. ^c27128678

  15 euros on aliexpress.

  - **weberer** · [2021-05-12 11:25 UTC](https://news.ycombinator.com/item?id=27129034)
    Do you have any recommendations on software to interface with it? ^c27129034

    - **robterrell** · [2021-05-12 14:34 UTC](https://news.ycombinator.com/item?id=27130793)
      Last year I was able to get it working by looking at examples like [https://github.com/lewapek/sds-dust-sensors-arduino-library](<https://github.com/lewapek/sds-dust-sensors-arduino-library>) and the datasheet [https://cdn.sparkfun.com/assets/parts/1/2/2/7/5/Laser\_Dust\_S...](<https://cdn.sparkfun.com/assets/parts/1/2/2/7/5/Laser_Dust_Sensor_Control_Protocol_V1.3.pdf>) ^c27130793

      There's a nice walkthrough here: [https://www.hackster.io/taunoerik/using-sds011-dust-sensor-0...](<https://www.hackster.io/taunoerik/using-sds011-dust-sensor-01f019>)

- **doggodaddo78** · [2021-05-12 00:52 UTC](https://news.ycombinator.com/item?id=27125433)
  I have 5 of the Plantower PMS5003. It's what PurpleAir uses (2x) too. ^c27125433

  I used one on an arduino to measure the 2020 Bear Creek fire PM / AQI measurements in Paradise CA. PM 2.5 and 10 were pushing 900+.

  Inside, with 2 3M Filtrete 2900 filters with the fan on constantly and a BlueAir 680 the AQI was about 5.

- **prvc** · [2021-05-12 08:16 UTC](https://news.ycombinator.com/item?id=27127978)
  Bit of a lazy question, but: is there a pre-made option available for general consumers to buy? ^c27127978

  - **sundvor** · [2021-05-12 10:41 UTC](https://news.ycombinator.com/item?id=27128748)
    Good question. ^c27128748

    I've never soldered a thing in my life, would be willing to learn it to get this sensor package built however. Looks like an awesome project.

    I'm in Australia, which would likely make shipping a fair bit harder.

- **igor47** · [2021-05-12 07:22 UTC](https://news.ycombinator.com/item?id=27127651)
  Plug for my write-up on an even simpler system: [https://igor.moomers.org/minimal-viable-air-quality](<https://igor.moomers.org/minimal-viable-air-quality>) ^c27127651

- **ashtonkem** · [2021-05-12 13:35 UTC](https://news.ycombinator.com/item?id=27130126)
  Heh, I thought about making one of these myself; Adafruit had some instructions on mounting this gear in a waterproof enclosure with downward facing holes for rain-resistant exterior mounting. But when I brought it up to my wife, her point was that air quality is always extremely good here, what would another sensor tell me? ^c27130126

- **thewizardofaus** · [2021-05-12 03:11 UTC](https://news.ycombinator.com/item?id=27126185)
  Great initiative! Look forward to hopefully making one soon. ^c27126185

