# [Ask HN: What indoor CO2 monitor do you recommend?](https://news.ycombinator.com/item?id=40749275)

nequo · 2024-06-21 13:13 UTC · 68 reported comments · archived 2026-11-08 13:35 UTC
Observation: 2026-11-08 13:35 UTC → 2026-11-08 13:35 UTC

Those of you who have used CO2 monitors to track your air quality indoors, what product do you recommend?

## Comments

- **JSDevOps** · [2024-06-21 13:54 UTC](https://news.ycombinator.com/item?id=40749675)
  [https://aranet.com/products/aranet4-home](<https://aranet.com/products/aranet4-home>) ^c40749675

  - **agwa** · [2024-06-21 14:15 UTC](https://news.ycombinator.com/item?id=40749857)
    These are great.  I have two of them and access the readings over Bluetooth using some Python code: [https://github.com/Anrijs/Aranet4-Python](<https://github.com/Anrijs/Aranet4-Python>) (there's also a mobile app which I've never used) ^c40749857

    The eink display is really nice and if you disable Bluetooth the battery seems to last forever.

    It's 40\% off right now which makes me tempted to pick up a third!

    - **jdoss** · [2024-06-21 15:47 UTC](https://news.ycombinator.com/item?id=40750775)
      This python code looks fantastic. Worked right out of the gate. Thanks! ^c40750775

      Also I was not aware of the Aranet Radiation sensor. There goes some of my fun budget towards picking one of these up.

      - **throwaranay4933** · [2024-06-21 16:57 UTC](https://news.ycombinator.com/item?id=40751438)
        Also there is a Go equivalent ([https://pkg.go.dev/sbinet.org/x/aranet4](<https://pkg.go.dev/sbinet.org/x/aranet4>)) which works well on Linux and [https://github.com/ryansouza/aranet4-exporter-go](<https://github.com/ryansouza/aranet4-exporter-go>) can be used to export the data to prometheus. ^c40751438

    - **hipadev23** · [2024-06-21 15:43 UTC](https://news.ycombinator.com/item?id=40750740)
      That 40\% off is a bit misleading, more like 10\% off, as you've been able to get them for \~\$165 on Amazon forever. ^c40750740

  - **zerojames** · [2024-06-21 14:22 UTC](https://news.ycombinator.com/item?id=40749941)
    The Aranet is wonderful. I have had mine (Aranet 4) running for at least a year on a single charge. ^c40749941

  - **joeyagreco** · [2024-06-21 14:27 UTC](https://news.ycombinator.com/item?id=40749988)
    I've had mine for 3 years now and it's great. Highly recommend. ^c40749988

  - **Mountain\_Skies** · [2024-06-21 14:34 UTC](https://news.ycombinator.com/item?id=40750057)
    Looks like it got the Hug of Death. Amazon sells it so just search for Aranet4 if the manufacturer's site is still struggling. ^c40750057

  - **EA-3167** · [2024-06-21 14:59 UTC](https://news.ycombinator.com/item?id=40750330)
    I have one of these and have had zero problems, it's easy to use and seemingly very accurate. Incredible battery life too. ^c40750330

  - **blankx32** · [2024-06-21 16:03 UTC](https://news.ycombinator.com/item?id=40750920)
    Does the app require any clouds to work? ^c40750920

    - **agwa** · [2024-06-21 16:16 UTC](https://news.ycombinator.com/item?id=40751019)
      No, for the home version the app just connects over Bluetooth. The protocol is documented and there are robust open source implementations such as [https://github.com/Anrijs/Aranet4-Python](<https://github.com/Anrijs/Aranet4-Python>) ^c40751019

  - **unsupp0rted** · [2024-06-22 09:28 UTC](https://news.ycombinator.com/item?id=40757637)
    I'd love to buy one, but it costs \`undefined\` USD and won't add to cart ^c40757637

  - **aloisdg** · [2024-06-21 14:06 UTC](https://news.ycombinator.com/item?id=40749792)
    Second this one. I own it and it is great ^c40749792

  - **packetlost** · [2024-06-21 14:14 UTC](https://news.ycombinator.com/item?id=40749842)
    Yeah, I have this one and it's fantastic ^c40749842

- **phinnaeus** · [2024-06-21 14:07 UTC](https://news.ycombinator.com/item?id=40749800)
  I picked up a pair (indoor+outdoor) of [https://www.airgradient.com](<https://www.airgradient.com>) monitors a few months ago. Happy with them so far though I have not decided on their final positions. ^c40749800

  - **troydavis** · [2024-06-21 20:38 UTC](https://news.ycombinator.com/item?id=40753555)
    I bought an AirGradient indoor meter and ran into 3 significant undocumented problems, 2 of which affect CO2: ^c40753555

    1\. The VOC readings use a relative scale and it's relative to a floating value: the last 24 hours. If a VOC source is present for more than 24 hours, it will quietly become part of the baseline value (100). You can read more here: [https://forum.airgradient.com/t/measurement-values-for-the-a...](<https://forum.airgradient.com/t/measurement-values-for-the-airgradient-one-tvoc-readings/1027>) , [https://forum.airgradient.com/t/measurement-values-for-the-a...](<https://forum.airgradient.com/t/measurement-values-for-the-airgradient-one-tvoc-readings/1027/13>)

    2\. The CO2 measurements re-calibrate to the lowest value detected every week (as \~400 ppm clean air). If it's not exposed to clean air every week, the readings will drift. When users asked how this worked, calibration hadn't been thought about much, if at all: [https://forum.airgradient.com/t/model-number-for-co2-calibra...](<https://forum.airgradient.com/t/model-number-for-co2-calibration/1478>) , [https://forum.airgradient.com/t/model-number-for-co2-calibra...](<https://forum.airgradient.com/t/model-number-for-co2-calibration/1478/17>)

    3\. The graphs don't show reboots, even though reboots (always?) reset the baselines. Reboots happen relatively frequently due to software updates. So, even the relative scale can change without any entry on the graph.

    I was pretty annoyed because it didn't seem like the company had thought through the user experience enough to even encounter these questions, let alone consider the best implementation (or at least document the flaws in whatever they're able to implement). This is the whole purpose of the product. The company means well and tries hard, but at some point good intentions matter less than the product.

    - **ahaucnx** · [2024-06-25 05:30 UTC](https://news.ycombinator.com/item?id=40784825)
      Achim, founder of AirGradient here. ^c40784825

      These are all valid points that came up at the beginning of the year and we took this feedback very seriously.

      I'm happy to let you know that we have implemented already point 1) and 2) in the latest firmware version.

      You can now set the "learning gain offset" for TVOC and NOx from the default 24h to basically 1 year. As a result the monitor will behave much more like an absolute TVOC monitor as the baseline reset is much longer.

      We have also implemented the automatic baseline calibration period, which you can now set to a much longer period than one week.

      We are also looking into feeding the last vale back into the sensor to avoid the reboot issue but this is more tricky to implement.

      By the way, if you compare the granularity that we offer now to fine tune the sensor modules, I'm not aware of any competitor offering the same feature set. But we won't stop here. We currently working on fine tuning compensation algorithms for PM.

  - **mtlynch** · [2024-06-21 15:49 UTC](https://news.ycombinator.com/item?id=40750789)
    I also own an indoor AirGradient, and I like supporting open-source, open hardware, but I've been pretty disappointed with the product. ^c40750789

    There were no instructions in the box, and I had to dig around a while until I found this PDF from three years ago.\[0\] I normally can figure out a gadget without reading instructions, but this wasn't self-explanatory, as there are no inputs on the device itself, and I had to figure out how to connect it to my WiFi.

    It's open-source, but there are no official instructions for re-flashing the device. I had to piece the process together from third-party blog posts.

    The code itself is pretty low quality. They use tons of globals that could trivially be local variables, and they throw away precision of floats by casting them to ints.

    I fixed a bunch of bugs in my fork\[1\] and started contributing them upstream, and the maintainer told me that they just did a giant rewrite, so I'd have to re-do all my changes.\[2\] I get that it happens, but I would have preferred they announce in the README that the code is deprecated and not to work on it until this rewrite is complete.

    I still think it's fine overall and I'd probably buy it again for other rooms in my house, but I hope they get their act together a bit more.

    \[0\] [https://www.airgradient.com/documents/AirGradient\%20Manual\%2...](<https://www.airgradient.com/documents/AirGradient%20Manual%2012APR2021.pdf>)

    \[1\] [https://github.com/mtlynch/airgradient-arduino](<https://github.com/mtlynch/airgradient-arduino>)

    \[2\] [https://github.com/airgradienthq/arduino/pull/45](<https://github.com/airgradienthq/arduino/pull/45>)

    - **ahaucnx** · [2024-06-25 05:40 UTC](https://news.ycombinator.com/item?id=40784887)
      Achim from AirGradient here. I fully understand your frustration. ^c40784887

      Maybe a bit of background information to put this into perspective.

      Until around a year ago, the open-source DIY kits where a seperate 'side project' as we focused on our (now retired) closed source air quality monitors.

      However last year we decided to go fully open-source hardware and started to merge the closed source features into the open-source firmware. Because we needed a much better code base, a complete re-write was required (also supporting two different MCUs).

      So the last 6 months was really a transition period and things were a bit messy but I believe we have a much better onboarding and instructions \[1\] now available on the website and are continuing to work on it.

      \[1\] [https://www.airgradient.com/documentation/](<https://www.airgradient.com/documentation/>)

      - **mtlynch** · [2024-06-26 16:34 UTC](https://news.ycombinator.com/item?id=40801790)
        Hi Achim, thanks for the response! ^c40801790

        Would it be possible for you to document somewhere how to flash from source?
        The website currently kind of explains it under "Flashing Of The AirGradient  Firmware," but step two is to flash the "ONE\_V9.ino" file, but there's no explanation of where to get that file.

        I know it used to exist on AirGradient's Github\[0\], but now I don't see it anywhere after the v3 rewrite.

        \[0\] [https://github.com/airgradienthq/arduino/blob/2.4.15/example...](<https://github.com/airgradienthq/arduino/blob/2.4.15/examples/ONE_V9/ONE_V9.ino>)

        - **ahaucnx** · [2024-06-29 09:13 UTC](https://news.ycombinator.com/item?id=40828893)
          It's now called "OneOpenAir.ino". We are still in the process to update the help files. ^c40828893

  - **tomek\_ycomb** · [2024-06-21 14:11 UTC](https://news.ycombinator.com/item?id=40749820)
    Excellent information from the person(s?) running air gradient with regards to pm sensor tech and design. Blog posts, etc. ^c40749820

    Ranges of kits from pre assembled to solder-yourself, that HN might like.

    (I am happy with my unit I gave to a friend with a wood fire stove heated house, and built one from kit to save some \$ another time.)

    - **ds\_opseeker** · [2024-06-21 14:32 UTC](https://news.ycombinator.com/item?id=40750031)
      I'll second air gradient. Founder is really cool and supportive. Tech works. I bought some boards from him a while back, ordered the parts of off alibaba, and had a working ESP32 setup in short order. ^c40750031

- **mrsirduke** · [2024-06-21 14:05 UTC](https://news.ycombinator.com/item?id=40749781)
  I've been happy with the awair element\[1\] for years.  It also measures PM2 and temp/humidity/voc. ^c40749781

  \[1\]: [https://www.getawair.com/products/element](<https://www.getawair.com/products/element>)

  - **huevosabio** · [2024-06-21 14:12 UTC](https://news.ycombinator.com/item?id=40749827)
    I was happy with my awair until it died after a mere year and a half from purchase. Now its just an expensive brick. ^c40749827

    - **ailurooo** · [2024-07-01 20:01 UTC](https://news.ycombinator.com/item?id=40849997)
      yeah that was my experience as well : ( ^c40849997

- **leemck** · [2024-06-21 21:01 UTC](https://news.ycombinator.com/item?id=40753759)
  The AZ-0001 Co2 meter. Vendor of a CO2 meter with zero to 2000 ppm co2, 30 or 50 ppm accuracy, serial data output, humidity, and temperature. The meter appears on a big name cheap sales website for a little under \$200. ^c40753759

  [https://www.co2meter.com/collections/handheld/products/az-ha...](<https://www.co2meter.com/collections/handheld/products/az-ha-portable-co2-temp-and-rh-meter>)

  One problem with the yellow AZ-0001 CO2 meter is the meter has to be manually restarted if the 9 volt input DC power is interrupted. A second problem is the CO2 value is quite sensitive to my breath  when the meter is running on the garage workbench. For outdoor readings the mechanical problem is to put the meter at least 8 feet away from passing humans and also have the meter accessible for restarting.

  The same vendor sells a hockey puck device which I have also used. I stopped using the hockey puck due to it's humidity measure device. That was about 4 years ago.

  [https://lessco2essay.blogspot.com/2015/08/carbon-dioxide-met...](<https://lessco2essay.blogspot.com/2015/08/carbon-dioxide-meter-mapper-and-logger.html>)

  Contact me for a copy of my Python CO2 meter software. The output of the software is lines of unixtime, GPS position, CO2, humidity, and temperature.  leemck at gmail dot com.

  My CO2 interest is in the global excess CO2 problem.

- **sschueller** · [2024-06-21 14:10 UTC](https://news.ycombinator.com/item?id=40749812)
  I really like the airthings view plus which also measures radon. ^c40749812

  [https://www.airthings.com/en/view-plus](<https://www.airthings.com/en/view-plus>)

  - **sliken** · [2024-06-21 19:37 UTC](https://news.ycombinator.com/item?id=40752891)
    They have a github if you want to use it with your own graphana without requiring any cloud access:
      [https://github.com/Airthings](<https://github.com/Airthings>) ^c40752891

    I've got one per floor in a 3 floor house and all get to the BT -\> wifi gateway reliably.

  - **xnx** · [2024-06-21 14:16 UTC](https://news.ycombinator.com/item?id=40749859)
    Seconded. Nice app that has good historical views and easy export of all data. ^c40749859

  - **azamba** · [2024-06-21 14:30 UTC](https://news.ycombinator.com/item?id=40750012)
    \+1 Airthings as long as you don't need any customer support. ^c40750012

  - **pawelduda** · [2024-06-21 15:42 UTC](https://news.ycombinator.com/item?id=40750725)
    Been running the wave plus for 2 years and can recommend ^c40750725

- **kingsloi** · [2024-06-21 15:43 UTC](https://news.ycombinator.com/item?id=40750739)
  I have a [https://www.birdie.design/en-us](<https://www.birdie.design/en-us>) (I think it was previously called a Canary) mounted in my living room, and it's a great lil device! Overly dramatic, fun, and easy to know whether air quality is good or bad - would recommend! ^c40750739

- **crazygringo** · [2024-06-21 14:46 UTC](https://news.ycombinator.com/item?id=40750186)
  If you want something that looks attractive in your room and has an app to view history (so the opposite of "hacker"), I highly recommend Awair, been using it for years: ^c40750186

  [https://www.getawair.com/products/element](<https://www.getawair.com/products/element>)

  You can configure the device display to just show numerical CO2 (that's what I do).

  Seeing the CO2 history graphed on your phone might not seem like it's all that necessary, but I find it really is -- you can see how it falls when you're out, you can see how quickly it skyrockets when you turn on the oven, you can see how long it takes to settle into a steady state overnight. Seeing CO2 over time gives me a conceptual understanding of what's actually happening, which I didn't have with my previous CO2 monitor that just showed the current value.

- **huseyinkeles** · [2024-06-21 14:09 UTC](https://news.ycombinator.com/item?id=40749809)
  If you want to go DIY route; I use MH-Z19 sensor along with an ESP-32 which has ESP-Home installed on it, works very well and I log the data on Home Assistant. ^c40749809

- **mambo\_giro** · [2024-06-21 15:19 UTC](https://news.ycombinator.com/item?id=40750534)
  I have a handful of these in my home and really appreciate the small form factor, long battery life, and options for accessing the data (on-screen live values via eInk display, encoded recent history displayed via QR code, or simple http server endpoint over wifi): [https://github.com/davidkreidler/OpenCO2\_Sensor](<https://github.com/davidkreidler/OpenCO2_Sensor>). It was straightforward to integrate the accessories into my homebridge instance for ongoing monitoring and notifications as well. ^c40750534

  You can make one yourself from the information in the repository or buy one from the author at their Tindie storefront: [https://www.tindie.com/products/davidkreidler/open-co2-senso...](<https://www.tindie.com/products/davidkreidler/open-co2-sensor/>).

- **amluto** · [2024-06-21 15:16 UTC](https://news.ycombinator.com/item?id=40750512)
  The main thing I would consider is that you want a sensor that actually measures CO2, which is usually an NDIR device. A lot of cheaper monitors and even some very fancy professional HVAC devices use “TVOC” meters and calculate a “CO2 equivalent”, and the performance of these devices is wildly variable. ^c40750512

  (The AirGradient devices are often configured with CO2 and separate SGP41 TVOC/NOx sensors.  It’s entertaining to plot both raw TVOC and CO2 and to observe that they’re clearly showing similar diurnal variation, but the CO2 data is much cleaner.)

  Aside: the SGP41 data sheet doesn’t really recommend looking at the raw data, but you can. I have an esphome fork that does this.

- **hedora** · [2024-06-21 14:31 UTC](https://news.ycombinator.com/item?id=40750027)
  If you *don't* want to go the DIY route, and also are interested in a weather station, Ambient Weather is great.  It just works out of the box (the CO2 sensor is an add on), and supports a large pile of local APIs and cloud service integrations. ^c40750027

  We went with one of the fancier models, including a nice LCD display and a solid state (ultrasonic) wind monitor, since we get hurricane-level gusts around here.  It's held up fine so far.  One annoyance:  At least the last time I checked, all the sensors have to be in radio range of the base station.  It'd be nice if they had WiFi bridges so we could monitor multiple buildings, etc, with one system.

  - **AtlasBarfed** · [2024-06-21 15:52 UTC](https://news.ycombinator.com/item?id=40750812)
    The sad reality of consumer IoT is that you will diy eventually. If you start out with a magically integrated system, well, just wait a few years. ^c40750812

    Hope you thoroughly document your house for its next owner!

- **taf2** · [2024-06-21 13:51 UTC](https://news.ycombinator.com/item?id=40749644)
  I had fun with this one ^c40749644

  [https://www.adafruit.com/product/5187](<https://www.adafruit.com/product/5187>)

  I used a tiny pico and display to make a little clock/sensor

- **whalesalad** · [2024-06-21 14:23 UTC](https://news.ycombinator.com/item?id=40749946)
  I have been using one of these for years and it is quite nice. [https://www.hydrofarm.com/p/autopilot-desktop-co2-monitor-da...](<https://www.hydrofarm.com/p/autopilot-desktop-co2-monitor-data-logger/apcem2>) ^c40749946

  - **OutOfHere** · [2024-06-21 14:26 UTC](https://news.ycombinator.com/item?id=40749972)
    A simple setting needs to be configured in it to change the threshold for alerts from that of an indoor marijuana farm to a regular home :-) ^c40749972

    - **whalesalad** · [2024-06-21 14:27 UTC](https://news.ycombinator.com/item?id=40749989)
      I'm at 1500ppm right now. Time to open all the windows and let the heat in :\\ ^c40749989

      - **OutOfHere** · [2024-06-21 14:29 UTC](https://news.ycombinator.com/item?id=40750005)
        If using an AC, it is okay to keep the AC running with the window slightly open. This slows down the CO2 buildup while preserving most of the cooling. I would never go over 770 ppm though. Also, the Energy Saver mode of an AC obviously results in a much worse indoor CO2 level. ^c40750005

- **sebazzz** · [2024-06-21 18:04 UTC](https://news.ycombinator.com/item?id=40752115)
  I have an Awair, which is generally good and has a locally accessible API. However, one dick move they did when they shut down (cloud) support for the old Awair, they shut down local API access too. Unfortunately, I was only aware of that after buying the Awair. ^c40752115

- **sofixa** · [2024-06-21 14:35 UTC](https://news.ycombinator.com/item?id=40750076)
  I have Apollo Automation MSR-1 (it does multiple things, including CO2 and mmWave movement/presence detection; they also have AIR-1 which tracks all sorts of air quality metrics such as VOC etc), flashed with ESPHome reporting to my Home Assistant setup. ^c40750076

  It's main advantage is that it's extremely affordable compared to the competition, and entirely local.

  Also I have a Netatmo Indoor Air Quality Monitor (requires their cloud service to work, but there's a Home Assistant integration too) which, alongside PM2.5 and CO2, also does sound and alerts me when music/etc. is too loud.

  - **radicality** · [2024-06-21 16:19 UTC](https://news.ycombinator.com/item?id=40751048)
    That looks like a nice all-in-one.
    If anyone from Apollo Automation reading it, perhaps you could also offer a version with the improved scd41 sensor vs the scd40. ^c40751048

- **blankx32** · [2024-06-21 14:51 UTC](https://news.ycombinator.com/item?id=40750242)
  Some good input on this thread such as that from brendangregg - [https://news.ycombinator.com/item?id\=34648021](<https://news.ycombinator.com/item?id=34648021>) ^c40750242

- **unknown** · [2024-06-21 19:35 UTC](https://news.ycombinator.com/item?id=40752873)
  [deleted] ^c40752873

- **ashish01** · [2024-06-21 16:08 UTC](https://news.ycombinator.com/item?id=40750956)
  I made two using scd41, esp32 and esphome.
   [https://shop.m5stack.com/products/co2l-unit-with-temperature...](<https://shop.m5stack.com/products/co2l-unit-with-temperature-and-humidity-sensor-scd41>) ^c40750956

- **shagie** · [2024-06-21 14:18 UTC](https://news.ycombinator.com/item?id=40749888)
  There's a couple things here and it depends on your needs. ^c40749888

  The word "track" suggests history.

  I've got a [https://www.amazon.com/gp/product/B0861777SL](<https://www.amazon.com/gp/product/B0861777SL>) which does what it says on the box and works.  I've got one in my WFH office and one in my bedroom.  There are times when I've woken up from a restless sleep to see that at a higher number (especially in the winter when the house is a bit more closed up).  Also the *track* where I can look at the history and see things "oh yea, last about 4h after I cooked dinner the CO2 went up a bit."

  However, that's only the standard sensor stuff (temp, humidity, CO2).

  If you've got amazon devices, I've got [https://www.amazon.com/gp/product/B08W8KS8D3](<https://www.amazon.com/gp/product/B08W8KS8D3>) ( Amazon Smart Air Quality Monitor ) which sits in my kitchen because I'm interested in other things there too.

  I've had some [https://milacares.com](<https://milacares.com>) air purifiers in the house.  They work as air monitors and purifiers.  I had some issues with them, but they worked for a good while.

  Consider if you want instant or historical data.  Do you want *other* data too?  What integrations do you have in the house with other home automation?  How much DIY are you going to engage in?

- **mrweasel** · [2024-06-21 14:34 UTC](https://news.ycombinator.com/item?id=40750058)
  I've been looking at the Eve Room, but haven't gotten it yet. It's one of the only devices I found that seems to work with HomeKit. ^c40750058

  - **danudey** · [2024-06-21 16:07 UTC](https://news.ycombinator.com/item?id=40750949)
    I have an Eve Room and I quite like it. The little e-ink display is incredibly easy to read in most lighting conditions (i.e. any condition where there's some light), and the battery life is really fantastic. ^c40750949

    I also have an air monitor from Qingping\[0\] which I got from Amazon, and I quite like that as well. Instead of VOCs, it reports pm2.5 and pm10 particulate, which was important for us (in Vancouver) because of the advent of 'wildfire season' in the past few years.

    I think I would prefer to have the pm2.5/pm10 sensors in the living room and bedrooms (which have windows and where people spent the most time) and the VOC sensors in the kitchen (where cooking/burning happens) and bathroom (where cleaning products are used but ventilation is poor) but I haven't gotten around to buying more of everything yet.

    \[0\] [https://www.amazon.ca/gp/product/B092HK4BB1/](<https://www.amazon.ca/gp/product/B092HK4BB1/>)

- **londons\_explore** · [2024-06-21 14:44 UTC](https://news.ycombinator.com/item?id=40750165)
  MH-Z19 module and a WiFi Arduino (esp32) which dumps co2 and temperature into Prometheus. ^c40750165

  It's like 20 lines of code and very rewarding to write.

- **anfractuosity** · [2024-06-21 14:18 UTC](https://news.ycombinator.com/item?id=40749887)
  I've used a Sensirion SCD30 (NDIR) sensor attached to a Pi running Grafana, which can be connected to via a web browser. ^c40749887

- **subtlemuffins** · [2024-06-21 18:45 UTC](https://news.ycombinator.com/item?id=40752415)
  Airgradient: [https://www.airgradient.com](<https://www.airgradient.com>) ^c40752415

- **zeke\_the\_cat** · [2024-06-21 14:48 UTC](https://news.ycombinator.com/item?id=40750209)
  The GQ Electronics GMC-520 has been very reliable for me. It has a Geiger counter and other functionality also. ^c40750209

- **radicality** · [2024-06-21 15:36 UTC](https://news.ycombinator.com/item?id=40750680)
  I have a uHoo for a few years, and it’s still working fine, but the app is pretty bad and the device paywalls the raw data behind a subscription which always felt scammy to me. Also the refresh interval is 1min. ^c40750680

  So recently I went the diy route and pretty happy with a setup from m5stack: an SCD41 sensor plugged in to an AtomS3, running EspHome. I set the resolution to 5 seconds (can go down to 1 second), and then data goes to HomeAssistant -\> InfluxDB and I plot it in Grafana. Cool to see the quick changes when using gas stove or opening up window.

  [https://shop.m5stack.com/products/co2l-unit-with-temperature...](<https://shop.m5stack.com/products/co2l-unit-with-temperature-and-humidity-sensor-scd41>)

  [https://shop.m5stack.com/products/atoms3-dev-kit-w-0-85-inch...](<https://shop.m5stack.com/products/atoms3-dev-kit-w-0-85-inch-screen>)

- **kkfx** · [2024-06-21 15:58 UTC](https://news.ycombinator.com/item?id=40750872)
  Honestly? I recommend a VMC. Simply because monitoring allow to let you know something you can already know enough from your feelings, a VMC allow to breathe more oxygenated air. ^c40750872

  - **danudey** · [2024-06-21 16:20 UTC](https://news.ycombinator.com/item?id=40751067)
    It's still useful to know to what extent your air is unpleasant (especially if it degrades over a long period of time and you acclimatize) as well as seeing historical trends. ^c40751067

  - **nequo** · [2024-06-21 16:20 UTC](https://news.ycombinator.com/item?id=40751074)
    I have search for "VMC" but I am not sure what you mean. Do you have an example of a VMC that you recommend? ^c40751074

    - **kkfx** · [2024-06-21 17:35 UTC](https://news.ycombinator.com/item?id=40751837)
      Where possible a double flux one, passive if you are in a mild climate, active (a small "inverted" heat pump) otherwise. ^c40751837

      VMCs are essentially one or two ventilators in a device designed to push and/or extract air from a closed space to the exterior. Simple flux generally extract, then since you do not vacuum a home external air enter the home from various passages, it's good to exchange air, but not much in energy consumption terms. The double flux suck air out of humid places like kitchens and bathrooms, push exterior air in rooms etc balancing the volumes, with a central point to exchange heat. The passive one is roughly simple, essentially air flux are divided by a set of passages and the dividers allow the heat to pass from the outgoing air to the incoming. They can't recover all the heat/freshness but they still help because you get let's say hot exterior air in summer that get cooled in the device by the outgoing interior air, the opposite in the winter, a small extras to dump condensation, some filters to protect the ventilator etc. The active one is a heat pump, like a minisplit, where the exterior side is in the outgoing flux and the interior side on the incoming, so in winter you pick heat from the outgoing air, witch is normally MUCH "hot" than the incoming, and in summer you push heat in the outgoing air witch is normally much "cooler" allow for a significant COP.

      In mild climate and insulated homes an active (also called thermodynamic) VMC suffice to ventilate, heat and cool the home, in less mild climate can be integrated with others appliances too heat/cool the home.

      Personally in the Alps I have an active one in a new (5 years) home and with \~10kWh/day suffice for most spring and autumn alone, integrate minisplit in summer and water-water heat pump in the winter. A passive double flux VMC can be just 1-2kWh/day but of course it can't regulate humidity and can heat/cool the home, just allow to waste much less heat/cool while exchanging air.

      They are normally present in cold climate home where insulation was a thing since decades, so we need to exchange air anyway, they start to appear in hotter and mild climate since many have started to realize that a home for cold climate works as well in hot climate, because insulation is the same, you only need to tune the thickness and choose elements to shield the Sun in summer/allow it to penetrate as much as possible in winter. The same overall design from the arctic to tropic.

      - **forbiddenlake** · [2024-06-21 18:57 UTC](https://news.ycombinator.com/item?id=40752538)
        Please, define your acronyms on first use. I read all that and still had no idea what you were talking about. But the context was enough to search. ^c40752538

        VMC stands for controlled mechanical ventilation in French.

        - **kkfx** · [2024-06-21 19:32 UTC](https://news.ycombinator.com/item?id=40752841)
          Sorry, seems to be the common name in many countries, not just in France and Italy and I do not know any specific translation. ^c40752841

          In more broad terms a modern home is composted of:

          \- a compact design to minimize surface dispersion of heat, a sphere would be ideal but obviously it's not much practical so we tend to the "cube" instead;

          \- aligned to the north-south axe to maximize the Sun intake in winter, so with more or less large windows to capt as much as possible with something to cover them and most of the exteriors in Summer when heating is not needed. This part obviously vary depending on the latitude; at arctic/antarctic I doubt we want to cover the Sun more than the minimum to sleep in summer, at equatorial latitudes I imaging heating in the winter is not much needed so large windows are just a choice there and Sun shields are the more shielding possible all of the year, in any case though the design still hold;

          \- with big insulation, as much as is reasonable, thermal simulation at hand, witch obviously the maximum thickness at boot too cold and too hot climate and the opposite in the most mild climate, again still the same design;

          \- air-tightness to keep the most separated possible the inside and the outside, but obviously it we do not exchange air we die inside... So airtight ok, but with a mean to exchange air keeping heat/humidity separated as much as possible. Still the same design, with some extras: in coldest climate we need pre-heating the incoming air, eventually get via a Canadian well (essentially a tube, around Ø200mm, laid out underground at a various depth and length to use the ground temperature to mitigate the incoming air), eventually with a classic resistive heating or a combination of both, and the same Canadian well not with a heating but a pre-cooling systems for most hot climate. Same principle and mostly the same tools all over the world;

          \- the way to exchange air is just pushing outside the internal air, sucking inside the exterior keeping the same pressure inside and outside, possibly regulating the humidity as well. This could be done passively or actively depending on the climate but the general principle is the same and the aeraulic (pipes) network is the same as well, we have some "different" solutions using multiple devices on perimetral walls, some grabbing air, some pushing, with some internal heat exchanger but they are not much effective and costly, used in general only to retrofit this system on pre-existing buildings where creating a pipe network is not much doable;

          \- the rest is direct air cooling, minisplit or centralized, the heat-pump principle is the same, only much bigger then the small one of the ventilation, and instead of exchanging air they make interior and exterior air turn in the interior and exterior unites without exchange, at a much bigger rate (let's say a home ventilation could be 300m³/h, while an aircon is at least 3000).

          \- the winter heating tend to be low inertia, low temperature, liquid to liquid or air (exterior) to liquid (interior) heat pump, the similar compressor of all the overs, but home side you get a long pipe under the flooring, rarely with some wall elements near the floor, where mildly hot water slowly flow releasing heat inside, while outside it's or a similar pipe underground, spread or deep in the soil, or an air-unit like the aircon.

          The goal of all the above is achieving the largest scale possible to lower the price of anything an the ability to guarantee an electrical absorption from the grid low enough to been able to aliment homes for potentially all humans given our generation capacity, this means normally around 1kW per home in mild climate, 4-6-8kW maximum in "extreme" climate. Another measure is the theoretical amount of energy the home need per internal walkable surface per year used as a generic "rating guideline".

          That's my best to avoid naming specific machines or acronyms, I hope it's clearer now.

          - **LUmBULtERA** · [2024-06-22 11:23 UTC](https://news.ycombinator.com/item?id=40758171)
            Thanks for all the info! It's not necessary to avoid acronyms or initialisms, just the first time it is used put what it is short for in parenthesis.  For example, Federal Bureau of Investigation (FBI), then you can use the FBI in the rest of the text. ^c40758171

- **licebmi\_\_at\_\_** · [2024-06-21 15:10 UTC](https://news.ycombinator.com/item?id=40750439)
  Genuinely curious, what are the advantages of a CO2 monitor? ^c40750439

  I mean, I get you can “track air quality” but what exactly does that mean on day to day basis?

  - **crazygringo** · [2024-06-21 15:41 UTC](https://news.ycombinator.com/item?id=40750722)
    It means you know when to open the windows more to maintain fresh air. ^c40750722

    I think much better and am in a better mood when CO2 levels are lower, or when air is fresher generally (the two generally correlate).

    But I don't want to keep my windows wide open all the time because that wastes AC or heat.

    So if the monitor is reading above 650, I open windows a little bit. If it's reading over 800, I open them wider. If it's under 550, I'll go back to closing them.

    It's just a few times a day, but it really helps. And it's not something I can "tell" otherwise easily, because if I have brain fog or am in a bad mood then high CO2 is just one of many possible reasons -- is my blood sugar low? Did I get enough sleep? Etc.

    A CO2 monitor feels just as essential to my health as weighing myself every day, no bright or blue lights two hours before bed, not overeating carbs, and so forth. It really helps with my overall alertness and productivity in a major way.

    - **moooo99** · [2024-06-23 11:32 UTC](https://news.ycombinator.com/item?id=40766646)
      I‘m genuinely curious, but isn’t a CO2 sensor an unnecessary high tech solution considering you could just open your window once a day for a few minutes and let the air exchange? ^c40766646

  - **zefhous** · [2024-06-21 18:46 UTC](https://news.ycombinator.com/item?id=40752428)
    DHH gave a talk about this a while ago with good citations to studies about CO2 concentration and other VOCs. ^c40752428

    [https://www.youtube.com/watch?v\=MRqh8oLY7Ik](<https://www.youtube.com/watch?v=MRqh8oLY7Ik>)

- **stefantalpalaru** · [2024-06-21 23:58 UTC](https://news.ycombinator.com/item?id=40755052)
  [flagged] ^c40755052

  \[dead\]

