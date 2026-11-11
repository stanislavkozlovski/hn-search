# [How to Measure Indoor Air Quality with a Raspberry Pi, RuuviTags and PMS7003](https://news.ycombinator.com/item?id=20640114)

Article: [https://joshefin.xyz/air-quality-with-raspberrypi-pms7003-and-java/](<https://joshefin.xyz/air-quality-with-raspberrypi-pms7003-and-java/>)

joshefin · 2019-08-07 23:03 UTC · 97 reported comments · archived 2026-11-08 11:05 UTC
Observation: 2026-11-08 11:04 UTC → 2026-11-08 11:05 UTC

## Comments

- **throwaway9d0291** · [2019-08-08 09:14 UTC](https://news.ycombinator.com/item?id=20642939)
  I think this is the main way to go if you care about air quality because unfortunately most consumer air quality monitors can be wildly inaccurate (i.e. detect nothing at all) even in day-to-day scenarios like making toast \[0\]. ^c20642939

  It's not limited to particulate matter either. You can get devices with reasonably accurate basics like temperature and humidity but as soon as you get into the actual air quality stuff like CO2, things start to fall apart. There are tons of devices that use wildly inaccurate TVOC sensors or fake their CO2 measurements (they estimate it based on H2 instead).

  If you want anything remotely close to accuracy, I strongly recommend buying something that actually tells you which sensors it has inside it. Get datasheets for the sensors and check that their specs are reasonable for what you want. For example make sure that if you want to actually measure CO2 to buy something with an NDIR sensor like the Senseair S8 inside.

  I wanted something I could plug into my home Prometheus/InfluxDB/Grafana setup so I bought \[1\] from Taobao. It lists all the sensors it uses, which are fairly good for the price. The device has a pretty simple TCP API that gives you JSON. Everything is Chinese but the measurements themselves are labelled in English and Google Translate works pretty well on the documentation.

  0: [https://www.sciencedaily.com/releases/2018/08/180822091022.h...](<https://www.sciencedaily.com/releases/2018/08/180822091022.htm>)

  1: [https://item.taobao.com/item.htm?id\=550317428831](<https://item.taobao.com/item.htm?id=550317428831>)

  - **electriclove** · [2019-08-08 14:48 UTC](https://news.ycombinator.com/item?id=20645081)
    Thanks for posting this! From the millions of air purifiers and filters that are sold, it is clear that people care about air quality in their homes. But there doesn't seem to be a *good* option for accurately measuring air quality. ^c20645081

    I appreciate the option you linked and wish there was an English version of it. If you were to build a consumer product, which air quality sensors would you want in it?

    - **throwaway9d0291** · [2019-08-09 07:15 UTC](https://news.ycombinator.com/item?id=20651988)
      For CO2, which I've researched the most out of the various things that interest me, I'd want a Senseair K30 or S8 Commercial, an Amphenol Telaire T6613 or T6713, or a CozIR-A or CozIR-LP sensor. ^c20651988

      For low cost, I'd go with the Senseair S8 Residential. It's not fantastically accurate but it's still a "real" sensor and you can get it for \$20 from China.

      For other aspects of air quality, I haven't finished researching the options yet.

      - **joshefin** · [2019-08-09 12:23 UTC](https://news.ycombinator.com/item?id=20653644)
        Thanks for sharing. I wanted to get Winsen MH-Z19B, but Senseair S8 (residential) looks like a better, more reliable option, for a DIY project. 
        One comparison: [https://www.letscontrolit.com/forum/viewtopic.php?t\=3736&sta...](<https://www.letscontrolit.com/forum/viewtopic.php?t=3736&start=20>) ^c20653644

        - **throwaway9d0291** · [2019-08-09 13:42 UTC](https://news.ycombinator.com/item?id=20654212)
          If you'd asked me a few days ago I'd have said that the MH-Z19B is okay on a budget but now that I know you can get an S8-0053 for \$20, I don't think I can recommend it. ^c20654212

          If it's difficult for you to get the cheap S8s for some reason though, per that thread it looks like an MH-Z19B with calibration off is a decent choice.

  - **auslander** · [2019-08-08 10:05 UTC](https://news.ycombinator.com/item?id=20643128)
    \[1\] on Aliexpress, in English, \$150 : [https://www.aliexpress.com/item/32759169154.html](<https://www.aliexpress.com/item/32759169154.html>) ^c20643128

    - **throwaway9d0291** · [2019-08-08 13:42 UTC](https://news.ycombinator.com/item?id=20644444)
      It does have English but it's not the same thing at all: It doesn't tell you which sensors are inside it (only the CO2 sensor) and it doesn't have any kind of machine-readable interface. ^c20644444

      - **auslander** · [2019-08-08 16:07 UTC](https://news.ycombinator.com/item?id=20645773)
        "S8 is short for S8-0053 model" from description. It seems like its using sensor you mentioned. ^c20645773

        - **throwaway9d0291** · [2019-08-09 07:09 UTC](https://news.ycombinator.com/item?id=20651952)
          Yes, that's why I said "only the CO2 sensor". It has other sensors but doesn't tell you what those are. ^c20651952

          And the CO2 sensor isn't much use to me without a way to read the sensor with a computer though and the device you linked doesn't have any kind of machine-readable interface.

- **pmg** · [2019-08-08 04:57 UTC](https://news.ycombinator.com/item?id=20641966)
  For this task I absolutely love my Xiaomi Mijia indoor air quality sensor\[1\]. ^c20641966

  Under \$50, nice touch screen, WiFi, TVOC, PM2.5, CO2, temp, humidity. Have one by a laser cutter (particulate), one in a paint booth(TVOC), and one in the office conference room (when the CO2 is higher than 1200 its time for a fresh air). A+ product and so much better than what I could build myself at that price point. If you find yourself in mainland China do yourself a favor and drop into a Xiaomi store.

  \[1\][https://m.mi.com/commodity/detail/1184500007](<https://m.mi.com/commodity/detail/1184500007>)

  - **throwaway9d0291** · [2019-08-08 08:56 UTC](https://news.ycombinator.com/item?id=20642871)
    I'm not sure about this particular sensor but Xiaomi doesn't have a good track record when it comes to accuracy when it comes to air particulates \[0\]. Also they claim to use a combined Sensirion TVOC + CO2 sensor, however the only TVOC + CO2 sensors Sensirion offers (SVM30, SGP30) \[1\] merely estimate CO2 concentration based on  H2 levels, they don't actually measure it directly. These sensors tend to be wildly inaccurate. The spec sheet even says typical accuracy is 15\%, which is pretty bad. ^c20642871

    0: [https://smartairfilters.com/en/blog/xiaomi-particle-counter-...](<https://smartairfilters.com/en/blog/xiaomi-particle-counter-inaccurate-not-control-purifier/>)

    1: [https://www.sensirion.com/en/environmental-sensors/gas-senso...](<https://www.sensirion.com/en/environmental-sensors/gas-sensors/>)

    - **close04** · [2019-08-08 12:25 UTC](https://news.ycombinator.com/item?id=20643824)
      I plan on building something with the CCS811 and SGP30 just for comparison sake. This article was interesting \[0\]. ^c20643824

      \[0\] [https://www.jaredwolff.com/finding-the-best-tvoc-sensor-ccs8...](<https://www.jaredwolff.com/finding-the-best-tvoc-sensor-ccs811-vs-bme680-vs-sgp30>)

    - **magicalhippo** · [2019-08-08 18:59 UTC](https://news.ycombinator.com/item?id=20647463)
      I found this\[1\] article rather interesting, comparing the tVOC and CO2 measured by a consumer device with professional grade equipment. It seems the MOX sensor used in the consumer device (AMS iAQ-CORE-C) did rather well on tVOC, but poorly on CO2 as you mentioned. ^c20647463

      \[1\]: [https://www.j-sens-sens-syst.net/7/373/2018/](<https://www.j-sens-sens-syst.net/7/373/2018/>) (pdf on the right)

      - **throwaway9d0291** · [2019-08-09 11:13 UTC](https://news.ycombinator.com/item?id=20653199)
        The study is interesting but I wouldn't say it "did rather well", as they applied a calibration to it first: ^c20653199

        "A regression analysis was performed to improve the accuracy of the Foobot FBT0002100 data relative to the GrayWolf data. Field calibration equations were then produced from the calibration dataset using the results from the GrayWolf instruments as dependent variables and the Foobot FBT0002100 as independent variables and tested on the validation dataset. An analysis in SPSS of the linear, quadratic, and cubic models was performed individually for each parameter to find the most accurate equation."

        You can't do that unless you happen to have access to a different research quality sensor. If the Foobot had that out of the factory it'd be nice though.

        - **magicalhippo** · [2019-08-09 19:27 UTC](https://news.ycombinator.com/item?id=20657558)
          That's not how I read it. ^c20657558

          "Field calibration equations were then produced *from* the calibration dataset \[...\]" (emphasis mine).

          Table 3 shows the calibration dataset for tVOC, which at least to me looks rather ok except for the outlier E.

    - **unknown** · [2019-08-08 10:04 UTC](https://news.ycombinator.com/item?id=20643118)
      [deleted] ^c20643118

  - **swebs** · [2019-08-08 10:07 UTC](https://news.ycombinator.com/item?id=20643135)
    \>Xiaomi ^c20643135

    Hmmm, does this by chance require an internet connection to operate?

  - **dotancohen** · [2019-08-08 09:22 UTC](https://news.ycombinator.com/item?id=20642959)
    I think that I could get by even with the Chinese menus, but the real problem for me is the mobile app. Is the mobile app strictly \_required\_ or is it an optional feature? I won't use a device that requires an app on my phone to function. ^c20642959

    - **r3bl** · [2019-08-08 10:09 UTC](https://news.ycombinator.com/item?id=20643138)
      I have never touched their air purifier, but I did three other gadgets (TV box, some indoor camera, some light bulbs). ^c20643138

      If privacy is your concern, I wouldn't recommend them. If stability is your concern, I wouldn't recommend them.

      The light bulb works with an app only (probably to remove the need for a separate hub), the camera could be rooted to work offline-only (which is why I bought it, but I gave up after a couple of shots and it's currently sitting in my drawer), and the TV box is *by far* the noisiest device in my local network. It's like 60\% of all DNS requests blocked by my Pi-hole.

      Their devices are also the most unstable devices I own, to the point where I'm considering just throwing them in the trash and re-investing in another camera and a TV box. I've already replaced the bulb I've purchased with a Philips Hue system. Quite more expensive, but truly works locally.

      - **joshefin** · [2019-08-08 10:45 UTC](https://news.ycombinator.com/item?id=20643310)
        I have the same experience - Xiaomi makes good and cheap hardware, but the software and reliability are bad. And if you want to keep your data private, skip them. ^c20643310

        - **dotancohen** · [2019-08-08 12:41 UTC](https://news.ycombinator.com/item?id=20643949)
          Is it linux or freebsd based? Can the firmware be reflashed? ^c20643949

  - **gwilkes** · [2019-08-08 05:21 UTC](https://news.ycombinator.com/item?id=20642060)
    Couldn't tell from the link, is there an English language option on the device? ^c20642060

    - **pmg** · [2019-08-08 05:34 UTC](https://news.ycombinator.com/item?id=20642105)
      Yes as well as Fahrenheit temperature if you prefer. Importing outside of China is a fairly highly mark up - \$80 on BangGood: [https://www.banggood.com/Xiaomi-Mijia-Air-Quality-Tester-Hig...](<https://www.banggood.com/Xiaomi-Mijia-Air-Quality-Tester-High-precision-Sensing-3_97-inch-Screen-Resolution-800480-USB-Inter-p-1381312.html>) ^c20642105

      - **tobtoh** · [2019-08-08 05:55 UTC](https://news.ycombinator.com/item?id=20642202)
        Although on the link you supplied, it does state "Note: Currently only supports Chinese interface display" ^c20642202

      - **throwaway9d0291** · [2019-08-09 07:32 UTC](https://news.ycombinator.com/item?id=20652055)
        You can skip Banggood and save a bit. It's \$52 from Xiaomi's official store \[0\] and \$8 shipping from a forwarder \[1\], so \$60 total. ^c20652055

        \[0\]: [https://detail.tmall.com/item.htm?id\=582112668204](<https://detail.tmall.com/item.htm?id=582112668204>)

        \[1\]: [https://www.superbuy.com/en/page/query/freight/\#areaId\%3D3\%2...](<https://www.superbuy.com/en/page/query/freight/#areaId%3D3%26weight%3D400%26volume%3D15*10*8%26arrType%3DElectrical%26warehouse%3D1%26area%3DUSA%20%E7%BE%8E%E5%9B%BD>)

      - **bentpins** · [2019-08-08 09:01 UTC](https://news.ycombinator.com/item?id=20642893)
        \$64 on AliExpress. Pandacheck is a good tool for price comparison although it doesn't help deal with listings with multiple prices
        [https://www.aliexpress.com/item/32970668564.html](<https://www.aliexpress.com/item/32970668564.html>)
        [https://en.pandacheck.com](<https://en.pandacheck.com>) ^c20642893

  - **throwaway8941** · [2019-08-08 05:52 UTC](https://news.ycombinator.com/item?id=20642189)
    \>when the CO2 is higher than 1200 its time for a fresh air ^c20642189

    That's hilarious. Where I am from, in winter it's always at least 1500 ppm outside, and more than 2000 ppm after \~19:00.

- **AceJohnny2** · [2019-08-08 02:11 UTC](https://news.ycombinator.com/item?id=20641204)
  Tangentially, for nearly a decade I've been looking for consumer-oriented wireless thermometers. ^c20641204

  Something that I can either query over the network (any protocol), or that uploads to some cloud service that I can inspect. This was the original selling point of ZigBee, but it sounds like it only exists for industrial applications. Does anyone know of a \$10-\$30 network-capable thermometer?

  I know they're relatively easy to hack together, as the OP project (and so many others like it) shows, but I'm specifically looking for a turnkey consumer solution, not something I'll have to spend a couple hours and multi-sourced parts to put together.

  - **xnyan** · [2019-08-08 03:20 UTC](https://news.ycombinator.com/item?id=20641562)
    Xiaomi might have what you are looking for: [https://www.aliexpress.com/item/32966216308.html](<https://www.aliexpress.com/item/32966216308.html>). It's zigbee, multi-year battery powered, costs \$10-15, does temperature and humility. No soldering, programming or any other diy. ^c20641562

    You can get a zigbee radio that can serve as a hub for a few bucks, but if you want the turnkey consumer experience, you also need Xiaomi's zigbee hub which runs around 50 bucks. With that you also get an iOS app that integrates with homekit. Xiaomi makes a lot of other zigbee products at a similar price range that work with it.

    You're not going to find any acceptable wifi solutions in the battery powered sensor category (there are a lot of other reasons that make wifi non-ideal for this), so unfortunately a hub is probably in your future for any option.

    EDIT: BTLE devices may also be an option, but IoT applications my tldr option is that BT is too complicated to be worth it unless you need something you can't get elsewhere.

    - **kiseleon** · [2019-08-08 13:30 UTC](https://news.ycombinator.com/item?id=20644333)
      I have a bunch of Xiaomi zigbee sensors (door/window, temperature, and water leak) connected to my SmartThings hub -- You just need to install a device handler and they will work fine (though from what I've heard Xiaomi devices don't work well with most repeaters -- these are pretty much my only Zigbee devices so they are connected directly to my hub and work great). ^c20644333

      I don't trust Xiaomi for anything connected directly to my network, but zigbee devices connected through something that I (kind of) trust works for me.

  - **danimal88** · [2019-08-08 12:06 UTC](https://news.ycombinator.com/item?id=20643713)
    I run a company ([https://flair.co](<https://flair.co>)) that builds a device you could use but is admittedly out of your proposed price range.  That said, it's consumer/prosumer grade and you can network as many as you want together.  You need at least one to be wired so it has enough power to fire up wifi and the rest can be run wired or on batteries.  They mesh over a 915MHz radio and temp/humidity/light/pressure.  We have been contemplating building a cheaper headless unit (these have a fancy little E-ink display) but haven't done it yet. ^c20643713

    The actual device is here: [https://flair.co/products/puck](<https://flair.co/products/puck>)

    There is a full fledged API (api.flair.co), desktop (my.flair.co) and apps of course.  For what you are looking for, there is plenty of plotting built in but you can also export the data from the app as a csv/spreadsheet or grab it from the api.

    Anyhow, it's definitely over your targeted price point but functionality wise, I think it does everything you might want.

    - **electriclove** · [2019-08-08 14:38 UTC](https://news.ycombinator.com/item?id=20644987)
      As a consumer wanting a better HVAC solution, I've been following this space for years and am glad to see your company still here and offering products for sale. ^c20644987

      I think there is an opportunity to grow your market if your Puck (or a new kind of Puck) can incorporate air quality sensors and make the data available. If you go this route, please see the recommendations in this comment as accuracy is key ([https://news.ycombinator.com/item?id\=20642939](<https://news.ycombinator.com/item?id=20642939>)). I would certainly purchase multiple Pucks if they provided accurate data in a format that I could query myself if I wanted (no subscription BS please). People are concerned about air quality yet have no easy way to accurately measure it in their homes.

      The bonus is that if I've got Pucks already, I would be more likely to purchase your Smart Vent products.

  - **aftbit** · [2019-08-08 04:29 UTC](https://news.ycombinator.com/item?id=20641859)
    I also haven't found anything commercial in this space. Luckily it is a pretty easy and cheap (\<\$10 in parts) hack project. ^c20641859

    I made a thermometer/barometer/hydrometer using an ESP-8266 wifi microcontroller (\$5 on ebay) and a single BME280 sensor (\$1 on ebay). Plugged into one of my left-over old 500mA phone chargers, it makes a wireless indoor weather station that speaks HTTP.

    I bought the sensor on a breakout board, soldered a couple of wires, flashed micropython to the ESP-8266 (NodeMCU), and wrote wrote Python to POST my server with the temperature data, schedule a wakeup, then go to sleep.

    But as you say, it took me a weekend of hacking around to build. This seems like exactly the kind of thing that should be available for \$10 on eBay yet I can't find anything at all open.

  - **stevekemp** · [2019-08-08 05:26 UTC](https://news.ycombinator.com/item?id=20642082)
    I bought a bunch of wireless temperature/humidity sensors from AliExpress - they broadcast their readings once a minute via a small 433Mhz radio-transmitter. ^c20642082

    Completely standalone, no WiFi, or other concerns.   And because they're battery powered I think they're safe enough in the sauna!

    From there I can get the readings via a USB-attached SDR dongle, and also sniff the radio-transmissions via a WiFi connected ESP8266 device with a radio-receiver.

  - **a254613e** · [2019-08-08 06:36 UTC](https://news.ycombinator.com/item?id=20642347)
    Xiaomi Aqara temperature and humidity sensor. ^c20642347

    \* Under \$10.

    \* Works with zigbee.

    \* Works out of the box with open source zigbee hubs. I personally have conbee II/deconz.

    And the whole setup of these open source zigbee solutions usually just consists of plugging in the USB device and starting a docker container. It's not not the tedious open source setup as it often is with open source projects.

    As a bonus you can use different zigbee devices from different manufacturers all together.

    - **AceJohnny2** · [2019-08-08 07:37 UTC](https://news.ycombinator.com/item?id=20642578)
      Thanks, sounds perfect, I'll try that. ^c20642578

  - **joshefin** · [2019-08-08 02:19 UTC](https://news.ycombinator.com/item?id=20641235)
    I used RuuviTags ([https://ruuvi.com/](<https://ruuvi.com/>)). They use a battery and send data over Bluetooth to your mobile phone. ^c20641235

    - **glogla** · [2019-08-08 06:31 UTC](https://news.ycombinator.com/item?id=20642330)
      You only get data from those when the phone is in bluetooth range. That's not very useful for long-term measurements. Unless you buy cheap android phone as a basestation I guess. ^c20642330

      - **lemming** · [2019-08-08 07:58 UTC](https://news.ycombinator.com/item?id=20642663)
        I have a bunch of SensorPushes at home which do the same, but they store the data for up to 20 days iirc, so it's effectively continuous data unless both my wife and I go away for a month or so. ^c20642663

      - **throwaway9d0291** · [2019-08-08 08:58 UTC](https://news.ycombinator.com/item?id=20642880)
        It's popular to set up a Raspberry Pi or similar to act as a bridge between Bluetooth and wifi. ^c20642880

  - **alex\_dev** · [2019-08-08 04:26 UTC](https://news.ycombinator.com/item?id=20641845)
    Agreed. Having to set up a raspberry pi or some other microcontroller is time consuming and the end product is ugly. I would like something small that connects to WiFi that operates off battery or could be plugged in permanently. ^c20641845

    I recently purchased Wyze's sensor starter kit and have been quite impressed. The contactless sensors are tiny and have decent range to the corresponding bridge. Now Wyze just needs a documented, public API.

    - **Galaxeblaffer** · [2019-08-08 08:20 UTC](https://news.ycombinator.com/item?id=20642737)
      Pimoroni made this quite easy though if you know a bit of python [https://shop.pimoroni.com/products/enviro-plus](<https://shop.pimoroni.com/products/enviro-plus>) ^c20642737

    - **flo123456** · [2019-08-08 05:54 UTC](https://news.ycombinator.com/item?id=20642196)
      Small and WiFi sound like an ESP8266 could be right for you. Or a Wemos D1 Mini, which uses an ESP but comes with a USB port. ^c20642196

  - **handruin** · [2019-08-08 17:30 UTC](https://news.ycombinator.com/item?id=20646550)
    Have you seen these remote temperature monitors from sensorpush?  They seem to do a decent job and there is an internet gateway device to manage them if you want. ^c20646550

    [http://www.sensorpush.com/\#products](<http://www.sensorpush.com/#products>)

  - **tehlike** · [2019-08-08 03:08 UTC](https://news.ycombinator.com/item?id=20641497)
    I use xiaomi to measure temperature, and send it to homeassistant. ^c20641497

- **simulate** · [2019-08-07 23:22 UTC](https://news.ycombinator.com/item?id=20640270)
  There was a similar post on HN about four months ago describing an air quality monitor with a slightly different stack: ^c20640270

  Build an Air Quality Monitor with InfluxDB, Grafana and Docker on a Raspberry Pi 
  [https://news.ycombinator.com/item?id\=19506983](<https://news.ycombinator.com/item?id=19506983>)

  - **blaser-waffle** · [2019-08-08 15:33 UTC](https://news.ycombinator.com/item?id=20645474)
    Thank you for sharing that. ^c20645474

    This particular article & comments read like a collection of referral links to Taobao and Ali-Express.

- **ShakataGaNai** · [2019-08-08 01:33 UTC](https://news.ycombinator.com/item?id=20641040)
  I love the idea, but why in the name of the Flying Spaghetti Monster, would you use Java on an RPi? There are at least half a dozen python libs for the PMS7003. ^c20641040

  - **bad\_user** · [2019-08-08 09:17 UTC](https://news.ycombinator.com/item?id=20642950)
    Java is great on a RPi. ^c20642950

    Many people don't realize but for a garbage collected language it can be quite efficient in terms of memory used. I have a long running web server that's forced to not exceed 50 MB of heap, having an up time of one year, which means no leaks.

    And the great part of Java processes is that they can be fat and handle multiple things at the same time, so you only need one Java process for anything you'd like to do.

    It's actually hard to achieve such stats with other garbage collected languages, including Python which in my experience is a memory hog and does reference counting AFAIK, along with relying on shitty C libraries, Python processes being leaky.

    The other advantage that Java has, over compiled languages like Rust or Haskell is that you can compile your JAR on your workstation and then distribute just that.

    This is less of a concern with interpreters like Python, however anybody that tried compiling stuff with something like Haskell for RPi knows how challenging that can be. And even for Python you often end up depending on native libraries that need to be compiled from source.

    I mean, every Python beginner hates PostgreSQL just because of how hard it can be to install psycopg2 via pip/easy\_install.

    In my experience Java's ease of deployment is better than anything else. You just copy a JAR and that's it.

  - **joshefin** · [2019-08-08 01:46 UTC](https://news.ycombinator.com/item?id=20641087)
    Python is great for prototyping, but my grand plan with this project is to add more sensors, integrate with some "smart home" devices and create a web UI - and I'm more comfortable coding all that in Java. ^c20641087

    - **JudgeWapner** · [2019-08-08 02:35 UTC](https://news.ycombinator.com/item?id=20641322)
      just be sure to allocate enough swap space for the gigabytes of bloat. ^c20641322

      - **fouc** · [2019-08-08 04:13 UTC](https://news.ycombinator.com/item?id=20641792)
        Should be possible to compile Java such that it runs very efficiently.  Java is commonly used for Android after all. ^c20641792

        - **JudgeWapner** · [2019-08-08 08:02 UTC](https://news.ycombinator.com/item?id=20642676)
          My Android device that runs slower after each "update"? ^c20642676

          - **SeanDav** · [2019-08-08 09:02 UTC](https://news.ycombinator.com/item?id=20642895)
            \> *My Android device that runs slower after each "update"?* ^c20642895

            This is not only an Android problem, Apple is equally guilty of this. Arguably, more so.

            Nor is it a Java problem. Some extremely speed-sensitive high perfomance code used by high speed trading algorithms use Java. This is in an environment where micro-seconds count.

            - **JudgeWapner** · [2019-08-08 13:34 UTC](https://news.ycombinator.com/item?id=20644380)
              When microseconds/frame rates/audio buffers count, you're only one garbage collection away from a complete thread lockup. Those gigabytes of heap aren't going to clean up themselves! ^c20644380

    - **Galaxeblaffer** · [2019-08-08 08:24 UTC](https://news.ycombinator.com/item?id=20642755)
      Python is also great for production, especially for tasks like this ;) ^c20642755

  - **koyote** · [2019-08-08 09:05 UTC](https://news.ycombinator.com/item?id=20642910)
    Java is generally faster than Python and I assume the OP is more familiar with it. I am not quite sure why you are asking that question? ^c20642910

  - **foolfoolz** · [2019-08-08 03:40 UTC](https://news.ycombinator.com/item?id=20641645)
    there’s no reason not to use java. the pi is powerful and runs a full linux os. generally in device programming the language breakdown is C or Everything Else ^c20641645

  - **joshefin** · [2019-08-08 10:33 UTC](https://news.ycombinator.com/item?id=20643255)
    I can just confirm what others are saying here - Java is great for the development of robust and reliable software. If you need even lower memory usage, you can compile the Java app with a GraalVM to a native image. ^c20643255

  - **codinghorror** · [2019-08-08 03:14 UTC](https://news.ycombinator.com/item?id=20641538)
    yeah the Java thing stopped me cold. That's bizarre on a Pi. ^c20641538

    - **edejong** · [2019-08-08 09:56 UTC](https://news.ycombinator.com/item?id=20643087)
      Currently running 4 JVM based solutions on 2 RPi's in our home. One is a fairly heavy one (OpenHAB 2), consuming 700 MB of memory. The others are simple importers (written in Scala), using around 50 MB each. It runs fast, is extremely stable (\> 200 days uptime), very fast response times (\< 100 ms), has a built-in dependency manager and is type-safe. ^c20643087

      With this setup, I have aggregated more than 4 years of in-home data, ranging from radio-thermostats, 15 thermometers, continuous electricity usage, around 10 z-wave devices, 15 zigbee sensors, Philips Hue Lighting (8 bulbs, 8 switches), local weather updates, InfluxDB storage and a fairly complicated setup for climate control (including presence detection using OwnTracks / WiFi and operation of roller-shutters and sunscreens).

    - **swebs** · [2019-08-08 10:14 UTC](https://news.ycombinator.com/item?id=20643166)
      How is it bizarre? Java and Python are both pretty standard for devices like this since they don't require recompilation for ARM. And Java is more performant than Python in general. ^c20643166

- **sumoboy** · [2019-08-08 03:29 UTC](https://news.ycombinator.com/item?id=20641596)
  In the end, you'll still need an air purifier unit to clean a room(s), or the entire house.  Indoor air quality is a much bigger issue than most realize. ^c20641596

  - **rofo1** · [2019-08-08 05:51 UTC](https://news.ycombinator.com/item?id=20642185)
    That depends on your location. I've built something similar to this tool that is discussed here and I've tested in multiple locations. ^c20642185

    For example, Vienna air was so clean (\<\= 10 pm10 ug/m\^3), that you don't need any purifiers or anything like that.

    - **MartinMond** · [2019-08-08 06:22 UTC](https://news.ycombinator.com/item?id=20642298)
      If you think Vienna's air is clean, you didn't measure during winter and/or during an inversion. You absolutely need air purifiers. ^c20642298

  - **agent008t** · [2019-08-08 09:03 UTC](https://news.ycombinator.com/item?id=20642900)
    Are there stand-alone air purifier units that are worth the hassle? ^c20642900

    - **magoon** · [2019-08-08 11:20 UTC](https://news.ycombinator.com/item?id=20643455)
      Yes look at the Coway AP-1512HH. I have one in each bedroom. It also has a good air quality sensor and “auto” mode that’s driven by it. Among the competition, it cleans better than most and has a low TCO. Very quiet on “low” ^c20643455

      - **tareqak** · [2019-08-08 11:54 UTC](https://news.ycombinator.com/item?id=20643638)
        I have one too. I got it based off of the recommendation from the Wirecutter: [https://thewirecutter.com/reviews/best-air-purifier/](<https://thewirecutter.com/reviews/best-air-purifier/>) . ^c20643638

      - **sumoboy** · [2019-08-08 22:07 UTC](https://news.ycombinator.com/item?id=20649338)
        Alot of junk out there so thinking your cleaning the air effectively with a \$100 unit is hilarious. You might filter more dust but not the particles you may really need.  Products like Amaircare can be attached to your entire hvac and clean all the air multiple times an hour depending up on the size.  Other room purifiers can target specific things like chemicals, dander, and dust but these units cost more because you get what you pay for.  If you worked in a salon or paint store all day long, there is a lot of stuff floating around.  Better units have very good filter(s) which is the difference. ^c20649338

    - **electriclove** · [2019-08-08 14:53 UTC](https://news.ycombinator.com/item?id=20645115)
      The Winix C535 from Costco for \$100 is a great deal: [https://www.costco.com/Winix-C535-Air-Cleaner-with-PlasmaWav...](<https://www.costco.com/Winix-C535-Air-Cleaner-with-PlasmaWave-Technology.product.100280290.html>) ^c20645115

  - **chrisbolt** · [2019-08-08 05:44 UTC](https://news.ycombinator.com/item?id=20642151)
    why? ^c20642151

  - **bubblewrap** · [2019-08-08 13:27 UTC](https://news.ycombinator.com/item?id=20644307)
    [flagged] ^c20644307

    Or you could open the windows.

- **softgrow** · [2019-08-08 02:16 UTC](https://news.ycombinator.com/item?id=20641222)
  I’ve looked at building one of these, but what new actionable information do you get? I’ve been wondering if it might say the room is dusty and then I could run the HEPA vacuum cleaner to bring it down. Or is this just for measurement geeks? ^c20641222

  - **joshefin** · [2019-08-08 02:29 UTC](https://news.ycombinator.com/item?id=20641289)
    You can use the PM measurement that the sensor outputs to calculate the Air Quality Index (for Europe: [http://airindex.eea.europa.eu/](<http://airindex.eea.europa.eu/>)) and for example, make it send you a notification when the pollution level goes up, so you can turn on the air purifier or vacuum or open the windows. ^c20641289

- **\_def** · [2019-08-08 10:25 UTC](https://news.ycombinator.com/item?id=20643219)
  Just yesterday I thought of building something similar. I often get tired from being in my small flat and I'm curious if CO2 could have anything to do with it. ^c20643219

- **heyoni** · [2019-08-08 01:47 UTC](https://news.ycombinator.com/item?id=20641095)
  Is there a spec sheet on how accurate/precise the specific recommended sensor is? I'm not even sure exactly how to describe a particle sensor but the aliexpress page is full of typos and I'm just wondering if it'll at least be able to measure the effectiveness of my indoor air purifier. ^c20641095

  - **joshefin** · [2019-08-08 02:41 UTC](https://news.ycombinator.com/item?id=20641352)
    If your air purifier has a screen and shows the air quality, it's most probably using a PM sensor like the one I write about here. ^c20641352

    How accurate is PMS7003? If for example, you need to know the precise and exact concentration of particulate matter in the air - then currently available low-cost PM sensors are not to be considered accurate. But, if you need to know if the air quality in your home is good, fair, moderate, poor or very poor, then it's good enough.

    - **tehlike** · [2019-08-08 03:09 UTC](https://news.ycombinator.com/item?id=20641513)
      These sensors also need calibration every week or so, which basically involves opening the windows to feed fresh air. ^c20641513

- **tareqak** · [2019-08-08 11:57 UTC](https://news.ycombinator.com/item?id=20643659)
  Does anyone know how accurate this set up would be be in comparison with the NetAtmo Indoor Air Quality monitor \[0\]? ^c20643659

  \[0\] [https://www.netatmo.com/en-us/aircare/homecoach](<https://www.netatmo.com/en-us/aircare/homecoach>)

  - **wil421** · [2019-08-08 12:02 UTC](https://news.ycombinator.com/item?id=20643688)
    If you could find out what sensor the NetAtmo is using you could do an apples to apples comparison. ^c20643688

    I bought a cheap soil sensor from microcenter that is absolute garbage. According to a few YouTubers it would corrode in a couple weeks. They recommended some higher quality sensors.

  - **joshefin** · [2019-08-08 12:28 UTC](https://news.ycombinator.com/item?id=20643855)
    Netatmo only measures CO2 and depending on your location it would be more useful to know about particulate matter in the air. ^c20643855

- **sippeangelo** · [2019-08-08 09:25 UTC](https://news.ycombinator.com/item?id=20642966)
  What's the RuuviTag for? I can't see it mentioned in the article. ^c20642966

  - **joshefin** · [2019-08-08 10:02 UTC](https://news.ycombinator.com/item?id=20643109)
    RuuviTag is a sensor capable of measuring the temperature, relative air humidity, and atmospheric pressure and sending the data over Bluetooth. I wrote about it in a linked article - [https://joshefin.xyz/temperature-humidity-pressure-with-ruuv...](<https://joshefin.xyz/temperature-humidity-pressure-with-ruuvitag-raspberry-pi-and-java/>) ^c20643109

- **amingilani** · [2019-08-08 00:05 UTC](https://news.ycombinator.com/item?id=20640543)
  What is the difference between an indoor air quality monitor and an outdoor one? ^c20640543

  Can't I just put this one outdoors in an out-of-the-rain-and-sun area and call it an outdoor air quality monitor?

  - **joshefin** · [2019-08-08 00:52 UTC](https://news.ycombinator.com/item?id=20640819)
    PMS7003, and most probably all other low-cost PM sensors with the same working principle, is not made to be used outdoors. Although used in many DIY projects for outdoor air quality monitoring, researches show that high humidity badly affects the PM measurements. Some have tried to heat the air before entering the sensor or to derive a correction factor, but mostly unsuccessfully. ^c20640819

    These sensors are not as accurate as more expensive professional devices but are good enough to give an idea of the pollution in the air.

    From my experience so far, PMS7003 measurements are comparable to official government air quality measurements available for my neighborhood.

    - **cagenut** · [2019-08-08 01:57 UTC](https://news.ycombinator.com/item?id=20641138)
      whats the next step up then?  the unit you'd buy for an outdoor sensor. ^c20641138

      - **joshefin** · [2019-08-08 02:48 UTC](https://news.ycombinator.com/item?id=20641390)
        Sorry, I can't recommend any. If you just want to know if the air is polluted or not, and humidity does not go over 70\%, any low-cost sensor would be good. ^c20641390

  - **solstice** · [2019-08-08 00:14 UTC](https://news.ycombinator.com/item?id=20640607)
    I assume that humidity messes with the detection of particle size. I have a LaserEgg particulate matter detector and they use a laser beam to count the particles in the air that flows through the device (via a small aspirating fan). So if particles are more clumped due to higher humidity, then I assume that would give you faulty/misleading readings? ^c20640607

    - **leggomylibro** · [2019-08-08 00:43 UTC](https://news.ycombinator.com/item?id=20640772)
      Maybe add another sensor? Humidity and temperature seem like useful readings for these sorts of monitors, and a lot of those sensors include barometric pressure for free. ^c20640772

      Although there is an old joke about their accuracy: "how do you use a cheap pressure sensor to determine altitude? Drop it out the window and count how long it takes to hit the ground."

      There are also affordable gas concentration sensors which can be useful for this sort of thing. Some are even marketed as 'air quality sensors' because they exhibit sensitivity to several different types of gases, but they aren't always useful because the output is usually just the sum of the sensor's response to each individual gas. Still, if you want a project to probably depress you in 10 years, get a CO2 sensor like the MH-Z19B and make yourself a datalogger. (Keep in mind that it's a little power-hungry, up to 150mA @5V \= 0.75W)

      - **joshefin** · [2019-08-08 01:20 UTC](https://news.ycombinator.com/item?id=20640984)
        The CO2 sensor would be a nice addition to my project. Do you have experience with the MH-Z19B, is it accurate enough for indoor use? ^c20640984

        - **leggomylibro** · [2019-08-08 13:50 UTC](https://news.ycombinator.com/item?id=20644517)
          I've only used it briefly, but I have also seen it used in DIY building management projects. The biggest issue I saw with it was power consumption: up to 150mA @5V is 0.75W, and I think it can take a bit of time to 'warm up' so you can't just turn it on for a few milliseconds every hour. But that should be fine if it's plugged into the wall. ^c20644517

          It's also fairly expensive, on the order of \$10 rather than \$1 last I checked.

    - **igor47** · [2019-08-08 01:34 UTC](https://news.ycombinator.com/item?id=20641041)
      Humidity is the biggest confounding variable for pm measurement. A bme280 is recommended to be able to compensate ^c20641041

    - **tyingq** · [2019-08-08 00:26 UTC](https://news.ycombinator.com/item?id=20640683)
      Also likely not made to deal with high and low temps, probably components that rust, etc. ^c20640683

- **Havoc** · [2019-08-08 11:59 UTC](https://news.ycombinator.com/item?id=20643670)
  I've got a rasp + air sensor. ^c20643670

  Quickly turned it off. It has a tiny fan that goes bzzzz. No thanks - my peace & quiet trumps my need to know air particle count

  - **joshefin** · [2019-08-08 12:40 UTC](https://news.ycombinator.com/item?id=20643946)
    The fan inside the PMS7003 sensor is very quiet. ^c20643946

- **693471** · [2019-08-08 19:59 UTC](https://news.ycombinator.com/item?id=20648057)
  The only thing worse than no data is bad data. I wouldn't trust these cheap sensors people keep hawking. ^c20648057

- **klausjensen** · [2019-08-08 12:05 UTC](https://news.ycombinator.com/item?id=20643711)
  I love the way this blog displays code. Just beautiful. ^c20643711

  - **jbeales** · [2019-08-08 13:35 UTC](https://news.ycombinator.com/item?id=20644385)
    Looks like it's using Prism.js: [https://prismjs.com](<https://prismjs.com>) ^c20644385

    - **joshefin** · [2019-08-08 13:56 UTC](https://news.ycombinator.com/item?id=20644592)
      Yes, Prism is great. Most of the blogs cramp the code in width, I let it spread it's wings full width. ^c20644592

- **alexghooper** · [2019-08-08 14:12 UTC](https://news.ycombinator.com/item?id=20644738)
  [flagged] ^c20644738

  You had me up until 'java'.

