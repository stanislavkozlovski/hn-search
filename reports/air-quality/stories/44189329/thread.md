# [Show HN: Air Lab – A portable and open air quality measuring device](https://news.ycombinator.com/item?id=44189329)

Article: [https://networkedartifacts.com/airlab/simulator](<https://networkedartifacts.com/airlab/simulator>)

256dpi · 2025-06-05 07:42 UTC · 186 reported comments · archived 2026-11-08 13:55 UTC
Observation: 2026-11-08 13:53 UTC → 2026-11-08 13:55 UTC

Hi HN!

I’ve been working on an air quality measuring device called Air Lab for the past three years. It measures CO2, temperature, relative humidity, air pollutants (VOC, NOx), and atmospheric pressure. You can log and analyze the data directly on the device — no smartphone or laptop needed.

To better show what the device can do and how it feels like, I spent the past week developing a web-based simulator using Emscripten. It runs the stock firmware with most features available except for networking. Check it out and let me know what you think!

The firmware will be open-source and available once the first batch of devices ships. We’re currently finishing up our crowdfunding campaign on CrowdSupply. If you want to get one, now is the time to support the project: [https://www.crowdsupply.com/networked-artifacts/air-lab](<https://www.crowdsupply.com/networked-artifacts/air-lab>)

We started building the Air Lab because most air quality measuring devices we found were locked-down or hard to tinker with. Air quality is a growing concern, and we’re hoping a more open, playful approach can help make the topic more accessible. It is important to us that there is a low bar for customizing and extending the Air Lab. Until we ship, we plan to create rich documentation and further tools, like the simulator, to make this as easy as possible.

The technical: The device is powered by the popular ESP32S3 microcontroller, equipped with a precise CO2, temperature, and relative humidity sensor (SCD41) as well as a VOC/NOx (SGP41) and atmospheric pressure sensor (LPS22). The support circuitry provides built-in battery charging, a real-time clock, an RGB LED, buzzer, an accelerometer, and capacitive touch, which makes Air Lab a powerful stand-alone device. The firmware itself is written on top of esp-idf and uses LVGL for rendering the UI.

If you seek more high-level info, here are also some videos covering the project:
\- [https://www.youtube.com/watch?v\=oBltdMLjUyg](<https://www.youtube.com/watch?v=oBltdMLjUyg>) (Introduction)
\- [https://www.youtube.com/watch?v\=\_tzjVYPm\_MU](<https://www.youtube.com/watch?v=_tzjVYPm_MU>) (Product Update)

Would love your feedback — on the device, hardware choices, potential use cases, or anything else worth improving. If you want to get notified on project updates, subscribe on Crowd Supply.

Happy to answer any questions!

## Comments

- **ronakjain90** · [2025-06-05 10:43 UTC](https://news.ycombinator.com/item?id=44190308)
  Your product looks so good, congratulations on your launch. ^c44190308

  Have you considered making a standalone devices with just sensors (think data only mode) and letting the users hook up their data on any eink dashboard of their choice.

  Below are some of the example of community created Air Quality dashboards\[1\] installable on any e-ink hardware\[2\].

  \[1\] [https://usetrmnl.com/recipes/62233](<https://usetrmnl.com/recipes/62233>), [https://usetrmnl.com/recipes/23306](<https://usetrmnl.com/recipes/23306>)

  \[2\] [https://github.com/usetrmnl/firmware/](<https://github.com/usetrmnl/firmware/>)

  Disclosure: I work at TRMNL.

  - **256dpi** · [2025-06-05 11:07 UTC](https://news.ycombinator.com/item?id=44190437)
    Thank you! Yes, that's something we'd like to prototype soon for supporting multiple rooms/locations. Integrating with other dashboards including TRMNL would be awesome too. ^c44190437

    - **InsOp** · [2025-06-06 11:14 UTC](https://news.ycombinator.com/item?id=44199692)
      like ZigBee compatible with home assistant ^c44199692

- **tomhow** · [2025-06-06 11:45 UTC](https://news.ycombinator.com/item?id=44199867)
  I just wanted to draw attention to this detail in one of the comments \[1\] from the author. ^c44199867

  This post \[2\] details the process they went though to port their device firmware to Wasm for their interactive demo. As a colleague put it, could be a pretty solid Show HN in its own right.

  \[1\] [https://news.ycombinator.com/item?id\=44190541](<https://news.ycombinator.com/item?id=44190541>)

  \[2\] [https://www.crowdsupply.com/networked-artifacts/air-lab/upda...](<https://www.crowdsupply.com/networked-artifacts/air-lab/updates/firmware-simulator>)

  - **256dpi** · [2025-06-08 13:32 UTC](https://news.ycombinator.com/item?id=44216902)
    Thanks tomhow! The idea for building the Air Lab simulator was very much inspired by the feedback I got from you. Here is a bit of background for the other readers: ^c44216902

    I reached out to HN by mail (as suggested on their tips page) to gauge whether my story/product was allowed to be posted as a Show HN post. They pointed out that HN requires a more "direct" demo of things. Their suggestion was to create a "raw" video showing how the device works and feels. It made a lot of sense to me. However, as a designer by training, it’s hard for me to produce something like that, as I naturally gravitate towards polishing it too much. When discussing this dilemma with my colleague, we remembered an idea I had some time ago about creating interactive renderings for the Air Lab website. Quickly, we agreed that this would be worth testing, as the whole goal of the video was to give the HN community a feel for the device.

    As mentioned in my comment and the Crowd Supply update, I used emscripten to compile the stock firmware to WASM. Luckily, by that time, I was already mostly done with extracting a hardware abstraction-layer from the firmware. This meant that I already had a nice API that I needed to ”mock” and connect to the fake sensors and controls on the website. So most of the work for that week was to actually build the simulator app using Ember.js around the compiled firmware and integrate it. By doing that, I also found a couple of bugs in the firmware itself that have been much easier to debug with the simulator than with a real device.

    I can recommend to anyone to reach out to the HN moderators and validate their post. Especially, if it is not a software thing that one can immediately try out. But also then, I think most posts/projects could profit from a more interactive demo.

- **homebrewer** · [2025-06-05 09:47 UTC](https://news.ycombinator.com/item?id=44190020)
  JFYI: a (hopefully much) cheaper stripped down version of the device would be useful. Air quality is the worst in poorer regions of the world, and as someone who suffers from horrible air pollution, but who's also living a relatively cushy life (by our standards), I can assure you that \$200+ for an air quality sensor puts it into the "unobtainable" bucket. Add shipping and it probably gets closer to \$300, which is roughly equal to the median monthly salary over here. ^c44190020

  Your NO₂ measurements make it a really interesting device compared to most alternatives that only measure particulate matter. All gas sensors that are theoretically possible for me to obtain cost hundreds of dollars by themselves.

  - **scottlamb** · [2025-06-05 16:27 UTC](https://news.ycombinator.com/item?id=44193184)
    I'm a big fan of the AirGradient. They used to have really cheap DIY kits available: either \$19 for the PCB + enclosure alone (with the assumption you already have the other parts or will buy them off aliexpress) or \$96 for everything. Looks like the current kit is \$138. If that's too much, you might be able to make it cheaper by downloading the KiCad and STL files off their website \[1\], getting PCBs printed elsewhere, 3D printing the case, and sourcing the rest of the parts from aliexpress. When you do it that way, you can also omit any sensors that are not of interest to save money, and perhaps add them in later. ^c44193184

    \[1\] [https://www.airgradient.com/documentation/overview/](<https://www.airgradient.com/documentation/overview/>)

    - **jadbox** · [2025-06-05 18:22 UTC](https://news.ycombinator.com/item?id=44194281)
      Ya, my AirGradient ONE is \$200 and has been one of the best investments in my home. Using it, I discovered how the drying polyester clothes wrecks the indoor air quality and how not to burn baking oils by controlling temps better. ^c44194281

      - **sizzle** · [2025-06-06 07:23 UTC](https://news.ycombinator.com/item?id=44198565)
        Drying polyester clothes releases CO2 to unhealthy levels? ^c44198565

        - **eddyfromtheblok** · [2025-06-06 07:32 UTC](https://news.ycombinator.com/item?id=44198609)
          Probably referring to particulate matter. The AirGradient measures PM2.5. I happen to have an air purifier near my W/D and it catches a lot of lint in the prefilter. ^c44198609

    - **cyberax** · [2025-06-05 21:14 UTC](https://news.ycombinator.com/item?id=44195854)
      I've been having problems with my devices, though. The reliability sucks, they lock up all the time. ^c44195854

      Additionally, the OLED screen needs to shut down in the dark. I added a VEML  lithgt sensor to my devices for that.

      - **ted\_dunning** · [2025-06-06 00:34 UTC](https://news.ycombinator.com/item?id=44196842)
        Interesting. I have been running three of their devices of different generations in my house for several years now with no hangs. ^c44196842

        - **cyberax** · [2025-06-06 05:25 UTC](https://news.ycombinator.com/item?id=44198023)
          No idea why. I tried to change the power supply, and even slightly overvolt the power (to 6V from nominal 5V). ^c44198023

      - **andyfleming** · [2025-06-06 06:13 UTC](https://news.ycombinator.com/item?id=44198232)
        I haven't had any issues with lock-ups. ^c44198232

        The LEDs and screens can be adjusted (or turned off) on a schedule with the latest firmware.

      - **Aeolun** · [2025-06-05 22:46 UTC](https://news.ycombinator.com/item?id=44196386)
        The light strip they added to the new devices is fun. You get a free nightlight too. ^c44196386

    - **isatty** · [2025-06-06 01:36 UTC](https://news.ycombinator.com/item?id=44197113)
      I have one that uses these sensors though I made a variation of this in a different layout and with a different power system (usb c and one that is powered off 12v). Wonder if JLPCB is affected by tariffs. I’d love to do a new board. ^c44197113

  - **crtified** · [2025-06-05 10:07 UTC](https://news.ycombinator.com/item?id=44190123)
    I'll preface this by saying that product design and manufacturing and public-proofing is long, hard work, and the retail price of this product is likely to be well justified for all kinds of reasons. ^c44190123

    That said, looking at the main active components that are listed, we have -

    ESP32S3 IC : \$4 retail,
    SCD41 Sensor : \$21 retail,
    SGP41 Sensor : \$8 retail,
    LPS22 Sensor : \$4 retail

    Which is very hopeful, in the sense that some key functionality of this kind of device could potentially be open sourced and pared back to a minimal cost where hobbyists could build versions suitable for the economics of developing countries.

    - **iamflimflam1** · [2025-06-05 10:54 UTC](https://news.ycombinator.com/item?id=44190373)
      Tariffs are having a big impact on people outside the US using CrowdSupply. ^c44190373

      CrowdSupply ships everything via Mouser US - so if you are outside of the US you need to export your products to Mouser. That hits you with tariffs and the tariffs are charged on what CrowdSupply are paying you for the products.

      If the majority of your product is manufactured in China (e.g. PCBA) then it's very likely that the COO for your product will be China. So, you will get stung with whatever crazy tariffs are currently in place.

      - **256dpi** · [2025-06-05 12:14 UTC](https://news.ycombinator.com/item?id=44190872)
        This has been very tricky to navigate for us. We almost launched the campaign right before the Tariffs got announced.  Luckily, we had the opportunity to wait it out. While CrowdSupply is an awesome platform, and I would use it again, the requirement to export everything to the US is a problem in such situations. ^c44190872

        - **iamflimflam1** · [2025-06-05 15:18 UTC](https://news.ycombinator.com/item?id=44192519)
          Yep, it's bitten me - just about to ship my boxes off. I'll still probably break even fortunately (or at least not lose a massive amount of money). ^c44192519

          - **256dpi** · [2025-06-05 15:33 UTC](https://news.ycombinator.com/item?id=44192671)
            Uff, that's hard! I'm sorry to hear that. What projects is yours? ^c44192671

            - **iamflimflam1** · [2025-06-05 15:44 UTC](https://news.ycombinator.com/item?id=44192789)
              ESP32 Rainbow - [https://www.crowdsupply.com/atomic14/esp32-rainbow](<https://www.crowdsupply.com/atomic14/esp32-rainbow>) ^c44192789

              I'm seeing if I can argue for a UK country of origin. But also, I want to get the boxes shipped and out to people - so think I'll just swallow it.

    - **FlyingSnake** · [2025-06-05 14:52 UTC](https://news.ycombinator.com/item?id=44192252)
      \> ESP32S3 IC : \$4 retail, SCD41 Sensor : \$21 retail, SGP41 Sensor : \$8 retail, LPS22 Sensor : \$4 retail ^c44192252

      I am not an expert but if I get these components, how easy would it be to build a hacked version out of these?

      I’m not in the US and unaffected by the tarrifs.

      - **crtified** · [2025-06-06 21:25 UTC](https://news.ycombinator.com/item?id=44205143)
        The basic connections are easy in theory, especially if you get a ready-to-use, breakout-board version (e.g. Adafruit modules) of each, for perhaps double or triple the price. Then it's just a matter of wiring each sensor to data lines of the controller chip, and giving everything the power it requires. ^c44205143

        Programming libraries contain the basic functions necessary to access to sensors' readings with simple lines of code.

        But the devil is in the details - to go from that to an actual practical, working model and physical build is quite a lot of work. Expect months, in hobbyist terms.

      - **nerdsniper** · [2025-06-05 15:03 UTC](https://news.ycombinator.com/item?id=44192371)
        Pretty simple. You can find lots of examples of getting each sensor working by googling "site:github.com ESP32 SCD41" etc. ^c44192371

        There are libraries which make it extra-easy:

        SCD41: SparkFun\_SCD4x\_Arduino\_Library.h

        SGP41: SensirionI2CSgp41.h

        LPS22: Adafruit\_LPS2X.h

        Take a look through the past HN discussions of this and similar air quality monitors. Can also search HN for chip names themselves (like 'SCD41'). Many people note that the sensors drift over time, and buying "calibration bottles" of low-concentration CO2 is a slight hurdle for many - they're not that crazy expensive, but they're expensive enough to be a bit of a block for some.

        - **FlyingSnake** · [2025-06-05 16:19 UTC](https://news.ycombinator.com/item?id=44193110)
          Sounds great! ^c44193110

          I’ll give it a try and see how far I go. Do you know any discord channels where such folks hang out?

          P.S. Apt username BTW.

          - **ajolly** · [2025-06-06 02:41 UTC](https://news.ycombinator.com/item?id=44197379)
            Super easy, use esphome.  There's a few vendors out there that sell pre built devices, and they usually make their configs available if you want to DIY it.  For example Apollo automation. ^c44197379

      - **DoingIsLearning** · [2025-06-05 14:59 UTC](https://news.ycombinator.com/item?id=44192330)
        Hardware companies design breakout boards for most semi popular sensors (including the SCD41 and the SGP41) so arguably if you can put things together on a breadboard and can setup I²C comms (for example with an Arduino library) then it is certainly accessible to a hobbyist. ^c44192330

  - **256dpi** · [2025-06-05 11:53 UTC](https://news.ycombinator.com/item?id=44190711)
    Thanks for the feedback that I can totally understand! We hoped to offer the product at a lower price, but as I mentioned in other replies, it's hard to be competitive when planning for small quantities. That said, I can totally see us offering a simplified and cheaper version in the future that is affordable to more people. ^c44190711

- **SeasonalEnnui** · [2025-06-05 20:56 UTC](https://news.ycombinator.com/item?id=44195693)
  I really like this.
  Did you investigate the options regarding CO2 sensors?
  I'm interested to know if you compared SCD30 to SCD41? The dual-channel design of SCD30 is supposed to offer lower drift and longer stability compared to the SCD41 (which claims to need taking outside once a week). That's the deal on paper, I'm wondering if you got any real data on this. ^c44195693

  - **256dpi** · [2025-06-05 21:39 UTC](https://news.ycombinator.com/item?id=44196052)
    Thanks! The SCD30 is a great sensor and obviously better than the SCD41. But we did not look at it in more detail, as we chose the SCD41 primarily for its small size. We believe that an accuracy of +/-50ppm is enough for a device like the Air Lab. Also, we'll actively look into reminding the user to take the device outside if automatic calibration is used. On top of that, it's our plan to either factory calibrate the devices and/or offer manual recalibration that should extend beyond the 1-week interval with automatic calibration. ^c44196052

    - **tyeth** · [2025-06-19 12:18 UTC](https://news.ycombinator.com/item?id=44317948)
      Maybe contact Sensirion about the STCC4, better form factor and due for release any moment...They have a contact sales option and are usually helpful.
      [https://sensirion.com/products/catalog/STCC4](<https://sensirion.com/products/catalog/STCC4>)
       (Not sure but thought maybe used in the SEN66 which is available now and covers most things including PPM/CO2/VOC/NOx) ^c44317948

- **silversmith** · [2025-06-05 08:31 UTC](https://news.ycombinator.com/item?id=44189618)
  I use Aranet devices myself - [https://www.aranet.com/en/home/products/aranet4-home](<https://www.aranet.com/en/home/products/aranet4-home>) ^c44189618

  What you could take from them is how prominent the current measurement is on the screen. I can glance over from a distance and instantly see the number. The colours get inverted if it goes into the red zone, so I can glance at it from across the room without my glasses and still see whether it's bad or not.

  From what the simulator shows, with your device I'd need to lean in pretty close to understand what's going on. And blinking light indicators are tricky - you can easily catch it between blinks and look away content that everything's alright.

  - **256dpi** · [2025-06-05 09:29 UTC](https://news.ycombinator.com/item?id=44189916)
    Yes, that's something I want to improve. ATM, if you rotate the (real) device, it will show a vertical layout in stand-by mode that uses a large font to display the values. I still need to add this to the simulator. A horizontal layout with bigger fonts is on the to-do list! ^c44189916

- **zevon** · [2025-06-05 08:37 UTC](https://news.ycombinator.com/item?id=44189653)
  Nice work! 
  Are you aware of [https://sensor.community](<https://sensor.community>) ? They have sensor designs as well but I mainly mention them because they have open infrastructure to aggregate sensor data on a public map. ^c44189653

- **xvfLJfx9** · [2025-06-05 09:20 UTC](https://news.ycombinator.com/item?id=44189861)
  I wish it would have support for Zigbee so I can pair it with other open data aggregation systems like Home Assistant.
  AirGradient, another cool air quality monitor, for example, does not have this. ^c44189861

  - **scottlamb** · [2025-06-05 16:32 UTC](https://news.ycombinator.com/item?id=44193222)
    The trick with the AirGradient is to use one of the ESPHome configs available \[1\] instead of their crappy Arduino sketch. Then it integrates with Home Assistant perfectly. ^c44193222

    \[1\] e.g. [https://github.com/MallocArray/airgradient\_esphome](<https://github.com/MallocArray/airgradient_esphome>)

  - **patrickk** · [2025-06-05 09:38 UTC](https://news.ycombinator.com/item?id=44189973)
    They integrate with Home Assistant via MQTT: ^c44189973

    [https://www.crowdsupply.com/networked-artifacts/air-lab/upda...](<https://www.crowdsupply.com/networked-artifacts/air-lab/updates/a-deep-dive-into-integrating-air-lab-with-home-assistant>)

  - **westurner** · [2025-06-05 21:35 UTC](https://news.ycombinator.com/item?id=44196026)
    Matter protocol support would also be a useful feature. ^c44196026

    Potential integration: Run HVAC fans and/or an attic fan and/or a crawlspace fan if indoor AQI is worse than outdoor AQI

    This says that Air Quality Sensor support was added to matter protocol in 2023: [https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-ne...](<https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/>) :

    \> *Air Quality Sensors – Supported sensors can capture and report on: PM1, PM2.5, PM10, CO2, NO2, VOC, CO, Ozone, Radon, and Formaldehyde. Furthermore, the addition of the Air Quality Cluster enables Matter devices to provide AQI information based on the device’s location*

    /? matter protocol Air Quality Cluster: [https://www.google.com/search?q\=matter+protocol+Air+Quality+...](<https://www.google.com/search?q=matter+protocol+Air+Quality+Cluster>)

    - **256dpi** · [2025-06-05 22:17 UTC](https://news.ycombinator.com/item?id=44196269)
      We'll definitely look into supporting Matter in the future, as it would allow integration with the most common home automation platforms/apps out there. ^c44196269

      - **westurner** · [2025-06-07 14:47 UTC](https://news.ycombinator.com/item?id=44210003)
        FWIU Thread and Matter work better when there is a "Border Router" ('hub') in the system; [https://news.ycombinator.com/item?id\=32167256\#32186688](<https://news.ycombinator.com/item?id=32167256#32186688>) ^c44210003

- **stared** · [2025-06-05 08:58 UTC](https://news.ycombinator.com/item?id=44189771)
  I like your design, especially the e-ink display! ^c44189771

  I am curious, what are pros and cons (connectivity, measurement quality) with  Qingping Air Monitor 2 ([https://qingping.co/air-monitor-2/](<https://qingping.co/air-monitor-2/>))?

- **hereme888** · [2025-06-05 09:00 UTC](https://news.ycombinator.com/item?id=44189774)
  If only 1\% of products were as honest in their presentation. Your page has the actual device, and users can "use" it just the way it works. ^c44189774

  No bikini models, no pretentious fancy screenshot, no dark patterns. The product speaks for itself.

  The thoughtfulness behind the website's UI speaks of who's behind it.

  - **unknown** · [2025-06-05 14:25 UTC](https://news.ycombinator.com/item?id=44192042)
    [deleted] ^c44192042

  - **ninetyninenine** · [2025-06-06 03:43 UTC](https://news.ycombinator.com/item?id=44197654)
    Whats wrong with bikini models? I want the product and the bikini model. ^c44197654

- **poisonborz** · [2025-06-05 08:44 UTC](https://news.ycombinator.com/item?id=44189693)
  Very cool project, we need more competition in this space - other option is like Air Gradient One, also open source. ^c44189693

  Famous HN "but": I find it baffling that by default we are shown this cutesy animation, that gets boring real fast, and actual measurement values in tiny font in the corner, which must be manually switched to for each sensor? Why not just show all sensor values in large font?

  - **Timshel** · [2025-06-05 09:41 UTC](https://news.ycombinator.com/item?id=44189988)
    There is a screen saver which display time/temp/ppm/rh. ^c44189988

    And:

    \> The official firmware for the Air Lab will be open-source and available on GitHub. Extend it and customize it to your needs.

  - **256dpi** · [2025-06-05 11:10 UTC](https://news.ycombinator.com/item?id=44190457)
    Thanks! As other commenters suggested, there is a screen saver (after 30s idle) that shows all values (horizontal and vertical) at a glance. The layout is not final yet and something I want to improve (make bigger). You can try it in the simulator. ^c44190457

  - **rokkamokka** · [2025-06-05 09:09 UTC](https://news.ycombinator.com/item?id=44189816)
    Yeah the display design seems to put the emphasis on fun rather than functional ^c44189816

  - **pcl** · [2025-06-05 09:32 UTC](https://news.ycombinator.com/item?id=44189942)
    I guess this is one of the cool things about an open stack, right? ^c44189942

  - **unknown** · [2025-06-05 14:26 UTC](https://news.ycombinator.com/item?id=44192050)
    [deleted] ^c44192050

- **burnt-resistor** · [2025-06-06 09:35 UTC](https://news.ycombinator.com/item?id=44199220)
  Needs a particle sensor like a PlanTower PMS5003 or it's not really worth the effort. ^c44199220

  I made an Arduino + PMS5003 + LCD for use during the NorCal fires of 2020 when the readings were 900+ μg/m\^3. At that time, I was wearing a full-face P100 respirator outdoors because the visibility was down to about 100' / 30m. That was about the same time I bought an overpriced BlueAir 680i because Consumer Reports rated the similar BlueAir 605 as the best air purifier they ever tested. (Unfortunately, that whole line they used cheap bearings in the fan motors that fail after a few years without replacement parts that you have to disassemble the motors and swap yourself. The bearings, thankfully, are generic parts: 608ZZ.)

- **pppone** · [2025-06-05 09:57 UTC](https://news.ycombinator.com/item?id=44190073)
  A really nice way of experiencing a hardware product!  I wish we had done the same for our air quality monitor when we were operational. \[0\] ^c44190073

  \[0\] - [https://www.open-seneca.org/](<https://www.open-seneca.org/>)

- **Eextra953** · [2025-06-05 14:41 UTC](https://news.ycombinator.com/item?id=44192158)
  Cool product! I come from a measurement/calibration background, so I'm curious about the accuracy of your system. Have you tested this against lab equipment, or do you have plans to specify accuracy with proper tolerance intervals? ^c44192158

  What about measurement uncertainty and unit-to-unit variability? I know this is consumer hardware, so I dont expect a full blown evaluation but have you characterized expected performance?

  - **256dpi** · [2025-06-05 14:53 UTC](https://news.ycombinator.com/item?id=44192268)
    Thanks and good question! We have planned to do a proper lab test soon. The Swiss Federal Office for the Environment is a project partner and has such equipment. During the design phase, we used a software to model the air flow and particle movements through the enclosure. Until then, we can only state what is already specified in the SCD41 and SGP41 datasheets. ^c44192268

- **mihaaly** · [2025-06-06 07:20 UTC](https://news.ycombinator.com/item?id=44198553)
  The simulation is an excellent idea! Very good it can be explored so easily, excellent. ^c44198553

  I find the usage of it suboptimal. Showing the main information in small and tucked away in corners while the rest of the screen is filled with short time amusing animation or nothing. Things happen automatically after a short period of time, and so far I wasn't able to get to the dasboard (tiny characters, not using the full screen) on will, only by waiting. Not quickly obvious what and when the buttons will do (indication sometime sqeezed into tiny parts of the animation), needs quite a bit of practice, and so can be forgotten later, needing relearn. It is nice having a plethora of funcionality but the core functionality suffers a bit in my view. This is just personal observation. A device like this is a very useful one, but not like this. It is demanding to use for the few most important things.

- **256dpi** · [2025-06-06 16:06 UTC](https://news.ycombinator.com/item?id=44202249)
  Dear HN community, thank you for the great feedback on my project! All comments, from honest remarks on the price to personal anecdotes on handling air quality issues, will help me, and others in this space, improve the product and raise awareness for this important global topic. Enjoy the weekend! ^c44202249

- **red523** · [2025-06-05 09:32 UTC](https://news.ycombinator.com/item?id=44189936)
  Good idea, but not cheap compared to Aranet4 \~200USD.
  Not sure ESP32 is a good choice for power consumption. ^c44189936

  - **benchly** · [2025-06-05 10:58 UTC](https://news.ycombinator.com/item?id=44190387)
    What's a good alternative? ^c44190387

    My understanding (which may be wrong, so I am open to being corrected) is that the greatest power consumption you'll see from ESP32 is connecting to a network and uploading data, the idea being less connections mean less power consumption. The ePaper display should be nice and low power consumption, too. I'd expect a common pocket battery bank to power it for a few weeks if one were using it to gather data for later use.

    Again, happy to be corrected. It's really fortunate that this post showed up on HN since just last month, I ordered a few components to start making my own air quality sensors, the goal being to create some units that I can strap on my car and gather data while I travel for work (personal curiosity, mostly). There's tons of great projects and info being referenced in this thread.

    - **256dpi** · [2025-06-05 11:42 UTC](https://news.ycombinator.com/item?id=44190642)
      OP is probably comparing the ESP32 to a NRF chip. These offer Bluetooth connectivity while running from a coin cell with \<1mA power consumption, compared to the ESP32s \~50mA when not sleeping. Luckily, we can stay in deep sleep most of the time to save battery. ^c44190642

      We mainly went with an ESP32 because of the great SDK and software support through Arduino etc. That way, people that want to customize the firmware or build their own can get started quickly.

      - **benchly** · [2025-06-05 13:53 UTC](https://news.ycombinator.com/item?id=44191734)
        It's a sensible choice. From a newbie perspective, it's certainly easy to work with and there's no shortage of documentation when I'm trying to figure something out. I'd pull the trigger on one of your devices right now because of that if funds weren't currently an issue (sadly, I am between jobs, atm). ^c44191734

        - **256dpi** · [2025-06-05 14:27 UTC](https://news.ycombinator.com/item?id=44192054)
          We're always looking for beta testers and would be happy to send you a device. Find your contact details here: [https://networkedartifacts.com/about](<https://networkedartifacts.com/about>) ^c44192054

- **raudette** · [2025-06-05 15:57 UTC](https://news.ycombinator.com/item?id=44192920)
  General feedback:
  \- I want something like this
  \- I have built crude air quality monitors (sensors + micro-controller) but would prefer something I can buy
  \- I love the openness
  \- I love the form factor.  I would like the ability to carry it around, the loop on this is great.  eg: what is this meeting room like after 45 minutes?
  \- Would like to see PM2.5 - the AirGradient is probably closer to what I want ^c44192920

  - **Havoc** · [2025-06-05 16:21 UTC](https://news.ycombinator.com/item?id=44193127)
    PM2.5 is quite challenging to miniaturize for a mobile & compact form factor like this - you need a fan of some sort. ^c44193127

    - **formerly\_proven** · [2025-06-05 16:46 UTC](https://news.ycombinator.com/item?id=44193341)
      Not necessarily: [https://www.bosch-sensortec.com/products/environmental-senso...](<https://www.bosch-sensortec.com/products/environmental-sensors/particulate-matter-sensor/bmv080/>) (fits in an USB key: [https://www2.purpleair.com/products/purpleair-pixel](<https://www2.purpleair.com/products/purpleair-pixel>)) ^c44193341

      - **Havoc** · [2025-06-05 17:40 UTC](https://news.ycombinator.com/item?id=44193892)
        Oh that's fun. Been meaning to get PM2.5 for my place but the one I've got has a whiny fan ^c44193892

        Thanks for linking

- **bhouston** · [2025-06-06 12:21 UTC](https://news.ycombinator.com/item?id=44200118)
  I recently upgraded to an EcoBee Premium and it has a lot of overlap with this device: ^c44200118

  \- Temperature (we have multiple sensors, one per major area of the house)

  \- Presence (the multiple sensors also record occupancy)

  \- Humidity

  \- CO2

  \- VOx

  What is nice is we can use the CO2/VOX to drive our HRV (heat recovery ventilation) to get fresh air from the outside into the house, but we only need to do this on demand, thus saving significant energy as compared to just constant HRV usage.

  We can also use the humidity sensor to drive our humidifier.

  We can use the occupancy + temperature to guide the AC / furnace.

  And we have an external temperature sensor to allow us to smartly use the heat pump versus furnace.

  I view this as a little more practical than just recording values - it makes them actionable and automatic.

  - **sedgjh23** · [2025-06-06 13:36 UTC](https://news.ycombinator.com/item?id=44200780)
    Just a heads up, the EcoBee doesn’t use a CO2 sensor, it just guesses what the value is. I have the same thermostat and was getting wildly different readings than my more expensive AirThings View Plus. Checked the EcoBee support website\[1\] and it made a lot more sense. ^c44200780

    “Based on the VOC measurement, it can also estimate carbon dioxide (CO2) levels. The sensor doesn’t directly measure CO2 but assesses CO2 levels based on the average correlation between VOCs and CO2 in exhaled human breath.”

    \[1\] [https://support.ecobee.com/s/articles/air-quality-sensor-faq...](<https://support.ecobee.com/s/articles/air-quality-sensor-faqs>)

    - **bhouston** · [2025-06-06 15:31 UTC](https://news.ycombinator.com/item?id=44201864)
      Which seems fair, because I live in a normal home with breathing humans and not an industrial setting where VOCs are produced in other ways. ^c44201864

      How wildly off were the readings btw?  And were you doing things related to VOCs?  Which reading was erroneously under reported compared to actual, CO2 or VOC?

      - **jaharmi** · [2025-06-11 00:35 UTC](https://news.ycombinator.com/item?id=44243051)
        [flagged] ^c44243051

        \[dead\]

- **deanc** · [2025-06-05 12:38 UTC](https://news.ycombinator.com/item?id=44191082)
  Can someone please tell me why it's so expensive to measure the quality of air? Literally all of these devices (ones that actually give accurate measurements) cost a fortune. What makes the sensors so expensive? ^c44191082

  - **est** · [2025-06-05 14:32 UTC](https://news.ycombinator.com/item?id=44192091)
    I guess it's the CO₂ sensor ^c44192091

    - **deanc** · [2025-06-05 19:19 UTC](https://news.ycombinator.com/item?id=44194890)
      Yes, but why are CO2 sensors so expensive? ^c44194890

      - **ted\_dunning** · [2025-06-06 00:43 UTC](https://news.ycombinator.com/item?id=44196889)
        Check out how they work. ^c44196889

        One kind emits light through a folded optic path through the test gas and detects the difference in the absorption between wavelengths of light are used. The difference in absorption is minute so the optical path needs to be as long as possible which makes it hard to make the detector small.

        The other kind detects the sound emitted when a precise frequency of IR is transmitted through a gas. If the frequency of the light is just right, it will be absorbed by the CO2 causing it to heat up ever so slightly which causes a tiny bit of sound.

        Both of these are incredibly ticklish devices to design and build in mass.

        That you can get these for as low as about \$20 in quantity is actually mind bogglingly cheap.

- **orion138** · [2025-06-05 15:14 UTC](https://news.ycombinator.com/item?id=44192480)
  What effect, if any, did you notice on sensor outputs from heat generated by other system components? e.g., constant temperature offset after reaching thermal steady state ^c44192480

  - **256dpi** · [2025-06-05 15:21 UTC](https://news.ycombinator.com/item?id=44192545)
    We have not tested this properly (see my other comment on lab testing), but so far we have observed no effect during normal operation and only saw a slight increase when charging the device (\~1°). We took great care to move the sensors far away from power management. Luckily, the display cutout also helps here. ^c44192545

    You can find more infos here: [https://www.crowdsupply.com/networked-artifacts/air-lab/upda...](<https://www.crowdsupply.com/networked-artifacts/air-lab/updates/hardware-details>)

- **pkdpic** · [2025-06-05 15:48 UTC](https://news.ycombinator.com/item?id=44192827)
  I love it and I want to buy one for every on of my family and friends. ^c44192827

  Just curious though does it cover finer particles and if not just curious why? Same question I guess for a general AQI rating. The one random (probably poor quality) portable AQI monitor I have covers different levels of fine particles and that seems really useful during fire season when its bad (in Nor Cal). But of course I'm not super knowledgeable about any of this.

  Anyway fantastic project, I absolutely love it.

  - **256dpi** · [2025-06-05 21:45 UTC](https://news.ycombinator.com/item?id=44196091)
    As the sibling commenter pointed out correctly, there is no PM sensor built-in at the moment. However, we added an extension port at the back that allows connecting PM sensors like the SEN54. We also plan to support this natively in the firmware and perhaps even offer a kit sometime soon that matches the design language. ^c44196091

  - **colechristensen** · [2025-06-05 15:50 UTC](https://news.ycombinator.com/item?id=44192843)
    It does not have any particle detection ^c44192843

- **clvx** · [2025-06-05 12:41 UTC](https://news.ycombinator.com/item?id=44191104)
  Ok, This is interesting. I need something alike that can measure whatever marijuana grow facilities generate.
  A neighbor lives in disbelief their facility doesn't produce any smell but neighbors in a mile radius disagree with it. He is willing to set up measurements to reduce any impact but I don't have a way to collect real data beyond it's smelling. I always depends on where the wind is blowing but it's constant. ^c44191104

  - **hedora** · [2025-06-05 17:36 UTC](https://news.ycombinator.com/item?id=44193857)
    Voc might work.  It covers most things you can smell. ^c44193857

    If it’s a sulfur smell, it’s probably sewer gas from something decomposing or fertilizer (or an unrelated sewer problem near the facility), and a natural gas / propane detector should work.  They also pick up methane, which is odorless, but is probably being produced by the same source.

  - **dbacar** · [2025-06-05 18:58 UTC](https://news.ycombinator.com/item?id=44194692)
    You sound like you are asking for a friend :). ^c44194692

- **Siecje** · [2025-06-05 10:48 UTC](https://news.ycombinator.com/item?id=44190335)
  Any plans for power over Ethernet? ^c44190335

  - **jonah** · [2025-06-05 16:44 UTC](https://news.ycombinator.com/item?id=44193329)
    There exist little adapters that take in PoE and output power (and potentially networking) over USB-C. ^c44193329

    Something like that could be employed to power this.

- **aurelwu** · [2025-06-05 09:49 UTC](https://news.ycombinator.com/item?id=44190033)
  Hi, I developed indoorco2map.com which is a an app-supported crowd-data-science project where users can submit CO2-Data they measure when going shopping or to restaurants or wherever using a simple-to-use App*. I'd like to support your Device - is there documentation available about how to read the Data via BLE? All I need is the CO2-History (either with timestamp, or just ordered + information about update interval). ^c44190033

  *MIT Licensed: [https://github.com/AurelWu/IndoorCO2AppMAUI](<https://github.com/AurelWu/IndoorCO2AppMAUI>)

  PS: do you use the air pressure to correct the CO2-readings like the Aranet4 does or would users need to manually recalibrate when the move to higher/lower elevations compared to when the sensor was calibrated?

  - **256dpi** · [2025-06-05 22:14 UTC](https://news.ycombinator.com/item?id=44196261)
    We love indoorco2map.com and would be happy to ensure that data from the Air Lab can be exported to it! We plan to expose simple BLE characteristics for all sensor values (similar to the Aranet). On top of that, we already have an API that would allow reading the full history from temporary storage (timestamped). Keep an eye on our website; we'll soon add a manual section with more details on that. ^c44196261

    We have not integrated compensation of CO2-readings yet, but will certainly look into it before shipping the device.

  - **unknown** · [2025-06-05 14:27 UTC](https://news.ycombinator.com/item?id=44192063)
    [deleted] ^c44192063

- **benbojangles** · [2025-06-05 13:16 UTC](https://news.ycombinator.com/item?id=44191416)
  [https://github.com/benb0jangles/Air\_Quality\_monitor](<https://github.com/benb0jangles/Air_Quality_monitor>) ^c44191416

  - **benbojangles** · [2025-06-05 13:18 UTC](https://news.ycombinator.com/item?id=44191424)
    I think this one has a BOM of about \$50 ^c44191424

    - **benbojangles** · [2025-06-05 13:20 UTC](https://news.ycombinator.com/item?id=44191447)
      and it displays github pages as well as the oled ^c44191447

- **bethekidyouwant** · [2025-06-05 14:54 UTC](https://news.ycombinator.com/item?id=44192274)
  I have these (inexpensive) sensors (except the barometer) hooked up to esp32’s in my home. After reviewing several months of the graph output I don’t have any confidence in the voc or co2 sensors accuracy. Additionally there is no good way to calibrate them outside of a lab. Imo the technology on the more interesting cheap sensors is not there yet. ^c44192274

  - **vosper** · [2025-06-05 15:38 UTC](https://news.ycombinator.com/item?id=44192723)
    For the AirGradient device I think the way to calibrate CO2 is to expose it to fresh air at some point, which has a known CO2 level. It’s supposed to auto-calibrate. But if you don’t do that regularly then the readings will drift (without anyway of telling they’re drifting). You also can’t tell when the sensor has calibrated. ^c44192723

    IIUC VOC is way more complicated and hard to both calibrate and interpret. I’m not sure I have any faith in that value.

    I do think a lot of people are going to be mislead by these monitors, the sensors and devices come with a bunch of caveats that aren’t clearly communicated.

    For me what people should most care about is particulates, and at least as far as I know those sensors don’t come with the calibration issues of CO2 and VOC. That’s the sensor my AirGradient is set to alert on.

    - **formerly\_proven** · [2025-06-05 16:43 UTC](https://news.ycombinator.com/item?id=44193319)
      Reasonable CO2 NDIR sensors use two chambers: one sampling ambient air for the measurement and a sealed chamber with a reference gas for autocal. ^c44193319

      edit: It seems AirGradient uses one of the cheap sensors.

    - **Aspos** · [2025-06-05 16:32 UTC](https://news.ycombinator.com/item?id=44193219)
      I have a CO2 sensor mounted right next to the vent of my ERV which pulls in fresh air regularly so the sensor gets calibrated automatically. ^c44193219

      - **ajolly** · [2025-06-06 02:43 UTC](https://news.ycombinator.com/item?id=44197390)
        What erv are you using? ^c44197390

        - **Aspos** · [2025-06-07 02:38 UTC](https://news.ycombinator.com/item?id=44206982)
          I use Broan ERVS100S and Panasonic FV-04VE1 ^c44206982

    - **hedora** · [2025-06-05 15:50 UTC](https://news.ycombinator.com/item?id=44192851)
      I was worried our sensors had that autocalibration mode.  Our house has new concrete floors.  They alternate between absorbing + outgassing CO2 (depending on room temperature), so sometimes our living room reads below 400 ppm. ^c44192851

      From what I can tell, the sensors haven't drifted, so they're not using the "below 420 ppm \=\> recalibrate" heuristic.

      - **unknown** · [2025-06-05 16:42 UTC](https://news.ycombinator.com/item?id=44193308)
        [deleted] ^c44193308

  - **GeoAtreides** · [2025-06-05 23:17 UTC](https://news.ycombinator.com/item?id=44196522)
    I have running for years both SCD30 and SCD41, and they're very much in-sync, although the technology is different. SCD41 is very sensitive to voltage, so you need to keep it as stable as possible. SCD30 is NDIR, so it doesn't need calibration (mostly...). ^c44196522

    For VOC also run SEN55, BME680 with BSEC 2.0 and BME688 with BSEC 2.6, they mostly agree, with the SEN55 being more sensitive to 'chemicals' (think industrial chemicals vs living entities chemicals), and BME688 more 'agressive/sensitive' to changes than BME680.

  - **hedora** · [2025-06-05 15:48 UTC](https://news.ycombinator.com/item?id=44192825)
    Obviously, it's not as good as a lab, but I have an Ambient Weather indoor PM 2.5/10/CO2 meter, and the numbers it's produced over the last few years are extremely plausible.  Someone might end up correlating the two. ^c44192825

    Overall, their whole setup is a nice plug and play experience.  My only complaint is that I want a 900MHz \<-\> WiFi / PoE bridge so that I can place temp + humidity sensors further from the house.  e.g., in cellars, forested spots, etc.

    Here's what would make me consider replacing / augmenting my system with Air Lab devices:

    \- Weather proofing
     \- Integrated solar panel charging solution so the 7.5 day battery life turns into 7.5 days without sun.
     \- Battery life estimates for WiFi mode that mean the solar panel would work, or a (weatherproof) BLE \<-\> WiFi/PoE bridge, assuming the BLE range (through a wood wall) is at least 100 feet.
     \- PoE on the sensor board would be nice to have.
     \- I like that these have VOC/NOX sensors, which my current setup is missing.  I don't like that they're missing PM sensors.
     \- I don't care about the screen; a blinking LED for debugging would too.
     \- If it were small enough to go in my pocket, I'd care about the screen.  I wonder if cell phones will eat that use case though.

  - **256dpi** · [2025-06-05 15:05 UTC](https://news.ycombinator.com/item?id=44192391)
    I'm curious, what's the range/variability you're seeing? ^c44192391

  - **radicality** · [2025-06-05 16:03 UTC](https://news.ycombinator.com/item?id=44192960)
    Oh yeah? That’s surprising, I’m doing something similar - with esp32s from M5stack, specifically their SCD41 sensor for co2 (same as in the device in the post), with an AtomS3 to drive it, and it’s super responsive and I think very accurate. Perhaps you have the scd40? It’s rated for high accuracy up to 2000ppm, while scd41 maintains accuracy up to 5000ppm. ^c44192960

    Using with esphome and homeAssistant, I grab the data every 5 seconds (I did 1s too but seemed unnecessary), and push it to HomeAssistant. The moment I turn on the oven, or open a window, or just enter the room after the night from the bedroom, the graph moves very very visibly and very quickly. I like this setup much more than my uHoo Air sensor.

    - **Havoc** · [2025-06-05 16:55 UTC](https://news.ycombinator.com/item?id=44193420)
      Have a similar setup. Unfortunately the open a window thing isn't all that reliable as test. Even sensors cheaper than the SDC40/41 will happily do that. ^c44193420

      The issue is more drift and that its a very localised measurement. The sharp spikes in the graphs are often more about the air is moving than the room's total CO2 changing. Like on mine (also sdc41) I can see when I wake up on the bedroom one. Being awake produces more CO2 sure but it's marginal. 80\% sure the spike is simply more turbulence in room. Lying still for hours vs getting up and making bed etc

  - **ajolly** · [2025-06-06 02:53 UTC](https://news.ycombinator.com/item?id=44197434)
    Really? I've got a few cheap sensors and while they're not always accurate in an absolute sense they are in an directional sense. It's extremely evident for Windows opened if someone is cooking if I turn on an air purifier, etc ^c44197434

- **Tepix** · [2025-06-06 10:57 UTC](https://news.ycombinator.com/item?id=44199604)
  Here is a (much cheaper \~50€) DIY project "airrohr" that measures particulates: [https://sensor.community/en/sensors/airrohr/](<https://sensor.community/en/sensors/airrohr/>) ^c44199604

  The project was formerly known as luftdaten.info

  They are collecting data from more than 10,000 sensors world-wide!

- **neves** · [2025-06-05 12:02 UTC](https://news.ycombinator.com/item?id=44190767)
  I'm always lost when it comes to air quality meters. There are so many specifications, and in general, they're quite expensive—especially for people in third-world countries. Does anyone know a good air quality monitor that costs less than 100 dollars? Preferably one that can be purchased on a Chinese website like AliExpress. ^c44190767

  - **xvilka** · [2025-06-05 12:05 UTC](https://news.ycombinator.com/item?id=44190797)
    Devices below 100 usually have bad sensors so they do some black magic and a lot of approximation in the firmware/software. Good air quality meter with good sensors simply cannot cost this low, even in the economy of scale. ^c44190797

  - **Rebelgecko** · [2025-06-05 12:12 UTC](https://news.ycombinator.com/item?id=44190851)
    If you're willing to DIY a bit you can put together an Airgradient for under \$100. Especially if you're making multiple ^c44190851

- **knowitnone** · [2025-06-05 16:07 UTC](https://news.ycombinator.com/item?id=44192998)
  IMHO, since laptops and smartphones are so ubiquitous, it would have been better and cheaper to build just the sensor with bluetooth connectivity. I guess your market is different. I know my local library has something similar mounted on their walls. ^c44192998

- **benob** · [2025-06-05 14:09 UTC](https://news.ycombinator.com/item?id=44191880)
  It looks pretty and featureful, but I'd love a cheaper version, maybe without a display. ^c44191880

- **whiplash451** · [2025-06-05 09:31 UTC](https://news.ycombinator.com/item?id=44189928)
  Very cool product. Am wondering if there exists an equivalent of this for physical activity, i.e. device you could attach to your physical keys and would measure footsteps/biking/running (while doing the switching automatically)? ^c44189928

  - **vallode** · [2025-06-05 09:34 UTC](https://news.ycombinator.com/item?id=44189950)
    Certain smartwatches offer a "pebble mode" feature like the Xiaomi band 9, you can get a keyring case for it and just attach it like that. I don't think it has automatic switching between exercise modes just tracking for steps etc. ^c44189950

    - **whiplash451** · [2025-06-05 09:37 UTC](https://news.ycombinator.com/item?id=44189968)
      Thanks. I don't want a smartwatch (I have a great "dumb" watch that I love). I'm rather looking for a device like this Air Lab but for physical activity. ^c44189968

- **mozvalentin** · [2025-06-05 11:16 UTC](https://news.ycombinator.com/item?id=44190481)
  I really appreciate having an open source solution. I hope the production costs can come down over time. I currently have an Airthings Wave and a Plus - which are roughtly in the same price range but additionally measure Radon. ^c44190481

  - **pooloo** · [2025-06-05 15:43 UTC](https://news.ycombinator.com/item?id=44192775)
    Yeah I am in the same boat, I have a lot of airthings products primarily for the radon measurements, which is at the same price point. ^c44192775

- **Havoc** · [2025-06-05 16:41 UTC](https://news.ycombinator.com/item?id=44193301)
  Looks slick & portability is a neat trick, but that's going to be a tough sell at the price. ^c44193301

  Anyone with ability to customize & extend this would know that a ESP and SCD41 sensor are around 10 bucks each.

- **bflesch** · [2025-06-05 09:05 UTC](https://news.ycombinator.com/item?id=44189800)
  Nice device, but too playful for my needs. I'm still looking for a good sensor like Aranet but without the display and the vendor lock-in. Maybe if display is removed from this one it would work? ^c44189800

  - **aurelwu** · [2025-06-05 09:59 UTC](https://news.ycombinator.com/item?id=44190085)
    you can get a ESP32 and a CO2-Sensor, easiest would be to use a development kit like a m5-stickC and the Sensirion SCD41 and with some small arduino scripts you are good to go to send the data via WLAN or BLE for something like 70€. Can be even cheaper if you don't use a development kit but it makes things a lot easier and the small display helps with debugging. ^c44190085

  - **yreg** · [2025-06-05 09:11 UTC](https://news.ycombinator.com/item?id=44189826)
    You can cover it with some tape. :) ^c44189826

    - **bflesch** · [2025-06-05 09:51 UTC](https://news.ycombinator.com/item?id=44190044)
      ;) the thought was more about reduce energy consumption and cost ^c44190044

      - **silversmith** · [2025-06-05 13:17 UTC](https://news.ycombinator.com/item?id=44191420)
        Aranet runs on e-ink, with silly low energy refresh rate. The two (or was it one? ages since I last checked) AA batteries last me well over two years. ^c44191420

        As for vendor lock-in, the basic readings get broadcast over bluetooth advertisments, and you can establish connection to get all the data. I have couple of them working nicely with HomeAssistant.

        The cost, yeah, I'd love it to be cheaper.

- **miiiiiike** · [2025-06-05 08:29 UTC](https://news.ycombinator.com/item?id=44189612)
  You made the simulator in a week..? Am I bad at what I do? ^c44189612

  - **256dpi** · [2025-06-05 11:27 UTC](https://news.ycombinator.com/item?id=44190541)
    I have written a bit about the process here: [https://www.crowdsupply.com/networked-artifacts/air-lab/upda...](<https://www.crowdsupply.com/networked-artifacts/air-lab/updates/firmware-simulator>). ^c44190541

    TLDR: It compiles the stock firmware to WASM using emscripten. Thus, I did not build all of it in one week and rather just the web app around the firmware.

- **jvanderbot** · [2025-06-05 12:08 UTC](https://news.ycombinator.com/item?id=44190823)
  I get that particle counters are a bit bulky, but with wildfires all over USA at the moment, that'd be a big draw. It's \$30 more. ^c44190823

  - **256dpi** · [2025-06-05 21:50 UTC](https://news.ycombinator.com/item?id=44196124)
    You can easily hook a PM sensor like the SEN54 to the extension port at the back. We're also thinking about offering an "upgrade kit" to match the design. ^c44196124

- **JKCalhoun** · [2025-06-05 14:12 UTC](https://news.ycombinator.com/item?id=44191914)
  See the lanyard thing going on ... thinking a watch config would be preferable (if it could be scaled down to that size). ^c44191914

- **ajolly** · [2025-06-06 02:49 UTC](https://news.ycombinator.com/item?id=44197419)
  It's cute but unless you really need the size+ onboard screen, I don't see the big win of this over an Apollo air-1.  (Esphome based, easy HA integration. ^c44197419

  Or an inkbird - I paid \$99 for one with co2, HCHO, AQI, PM2.5 PM10, TVOC, Temperature, Humidity. It has a display and integrates with home assistant. Built in battery if you want to move it around.

  I own both of those. A DIY it but I haven't seen a good reason to.

  The big advantage of the ESP home devices out there is they are extremely easy to tinker with if you want to change anything

  - **unknown** · [2025-06-06 05:29 UTC](https://news.ycombinator.com/item?id=44198044)
    [deleted] ^c44198044

- **jhlee525** · [2025-06-07 11:17 UTC](https://news.ycombinator.com/item?id=44208909)
  It may vary by region, but there are certainly places around the world where it is needed. ^c44208909

- **Eduard** · [2025-06-05 11:22 UTC](https://news.ycombinator.com/item?id=44190518)
  I would find it more natural when the positions of the AB buttons area was switched with the D-pad area. ^c44190518

  - **256dpi** · [2025-06-05 12:02 UTC](https://news.ycombinator.com/item?id=44190770)
    Good catch! Unfortunately, we realized a bit too late that we flipped the standard console layout (e.g. Game Boy). Luckily, most people that notice get used to it quickly. ^c44190770

- **abcd\_f** · [2025-06-09 13:12 UTC](https://news.ycombinator.com/item?id=44224159)
  Very Teenage Engineering-like aesthetics, super cool! ^c44224159

- **jdalgetty** · [2025-06-06 11:40 UTC](https://news.ycombinator.com/item?id=44199834)
  Is there any sort of case option for this? How resistant is it to moisture? ^c44199834

- **touwer** · [2025-06-05 08:30 UTC](https://news.ycombinator.com/item?id=44189617)
  Cool project! And much needed ^c44189617

- **Isn0gud** · [2025-06-05 09:53 UTC](https://news.ycombinator.com/item?id=44190052)
  The ikea vindstyrka sensor is 50\$, how is this 4x the price? ^c44190052

  - **256dpi** · [2025-06-05 11:20 UTC](https://news.ycombinator.com/item?id=44190496)
    We added many components that are not strictly needed to measure air quality but make the device an interesting platform for custom projects. Also, the enclosure is more premium, being made from aluminum. Finally, IKEA can leverage economy of scale and probably gets a much better price on most parts. ^c44190496

  - **rspoerri** · [2025-06-05 10:00 UTC](https://news.ycombinator.com/item?id=44190093)
    Any co2 measuring device costs at least 70\$. All devices i know with internet connectivity costs 150\$+. ^c44190093

    - **djrj477dhsnv** · [2025-06-06 01:43 UTC](https://news.ycombinator.com/item?id=44197149)
      My Qingping Monitor Lite with SenseAir S8 co2 sensor, pm2.5, wifi, and oled display seems to be accurate enough and was only \$45. ^c44197149

- **TheonlyJem** · [2025-06-09 06:49 UTC](https://news.ycombinator.com/item?id=44221989)
  kudos for sticking with it for three years and still pushing to make it more open and accessible ^c44221989

- **snvzz** · [2025-06-06 04:28 UTC](https://news.ycombinator.com/item?id=44197804)
  \>ESP32S3 ^c44197804

  Unfortunately predates the switch to RISC-V.

- **savrajsingh** · [2025-06-05 12:14 UTC](https://news.ycombinator.com/item?id=44190874)
  No pm2.5? ^c44190874

  - **256dpi** · [2025-06-05 12:30 UTC](https://news.ycombinator.com/item?id=44191021)
    Not yet. Unfortunately, these are usually quite big, and we didn't want to sacrifice the portability. But you can add a PM sensor through the extension port. We'll document this in our upcoming manual. ^c44191021

    A fellow Crowd Supply project, Polverine\[1\], uses a new Bosch sensor that is very small. If we do a refresh of the device, we'll certainly look into adding it.

    \[1\]: [https://www.crowdsupply.com/blackiot/polverine](<https://www.crowdsupply.com/blackiot/polverine>)

    - **haarolean** · [2025-06-05 13:00 UTC](https://news.ycombinator.com/item?id=44191281)
      IMO, PM2.5 sensors are essential nowadays. What's the point of a device without one? Especially for \$229. I can get a chinese thingy like qingping for \~\$115 with PM2.5 and other stuff. ^c44191281

- **ge96** · [2025-06-05 14:56 UTC](https://news.ycombinator.com/item?id=44192290)
  the clickable image is a nice touch (buttons) ^c44192290

- **Timot05** · [2025-06-05 09:32 UTC](https://news.ycombinator.com/item?id=44189938)
  Nice kickstand! ^c44189938

  - **256dpi** · [2025-06-05 11:20 UTC](https://news.ycombinator.com/item?id=44190506)
    Thanks! Our engineer invested a lot of time to get the feeling just perfect! :-) ^c44190506

- **tremarley** · [2025-06-05 10:11 UTC](https://news.ycombinator.com/item?id=44190146)
  The website is broken ^c44190146

  - **256dpi** · [2025-06-05 11:22 UTC](https://news.ycombinator.com/item?id=44190515)
    Sorry to hear that! I'm happy to investigate if you let me know your browser/platform. ^c44190515

- **flawn** · [2025-06-05 09:49 UTC](https://news.ycombinator.com/item?id=44190035)
  love this! ^c44190035

- **voxlax** · [2025-06-05 10:09 UTC](https://news.ycombinator.com/item?id=44190132)
  You can get the same measurements and even more from AirGradient. Those are a bit cheaper and much more solid devices. Not so focused on design, but rather on accuracy:
  [https://www.airgradient.com](<https://www.airgradient.com>) ^c44190132

  I´m not affiliated with them in any way, but I´m using their indoor and outdoor sensors since a few years by now, and I am very satisifed. Btw. their HW is opensource and you can choose between their SW or can flash anything else. 
  The measurement data of my outdoor sensor is publicly available: 
  [https://explore.openaq.org/?location\=2070168\#13.21/48.22244/...](<https://explore.openaq.org/?location=2070168#13.21/48.22244/16.37334>)

  - **technotarek** · [2025-06-05 11:05 UTC](https://news.ycombinator.com/item?id=44190425)
    A sincere question : In a home environment, what information do devices like this provide that you regularly act upon and how? Can you give some examples? I’m trying to understand the use case given I already have a thermostat with humidity readings and look at the weather for air quality. Is it more than after cooking, the PPMs are high, open the window or turn on the vent fan (which I do out of habit anyways)? ^c44190425

    I self imposed a rule when I went through the process of having a child — to avoid (negative) information that I couldn’t or wouldn’t really act upon (e.g. learning about genetic markers/hints that couldn’t be prevented and wouldn’t make me think about extreme measures, such as blindness). For me it’s an issue of anxiety management.

    - **Modified3019** · [2025-06-05 12:18 UTC](https://news.ycombinator.com/item?id=44190917)
      I mostly use mine just for monitoring humidity (I use a humidifier, but don’t want the humidity going up past 60\% or bad things can start to grow) and CO2 which I try to keep below 800-ish PPM by keeping the window slightly open (except during pollen season, which is now) ^c44190917

      There was an initial effort of doing things and seeing the effects and eventually finding a nice equilibrium. I now have a feel for what’s needed and it’s not something I put any thought into. I basically check it when the seasons change. Rather than contributing to anxiety, I am now *relieved* of unknowns.

      I’m quite allergic to pollen, and very sensitive to things like smoke, so I’ve already someone more focused on managing my environment than a normal person. A wick based humidifier (don’t use ultrasonic, those breed bacteria *and* launch them into the air) and large air filter with a big but quiet fan are the most important things in my room. Yes, even the bed.

      These devices can also be a good way to catch localized air pollution that exceeds safety limits, though where I live that’s not an issue. Citizens capable of checking air and water quality is a positive in my opinion.

      - **dylan604** · [2025-06-05 14:03 UTC](https://news.ycombinator.com/item?id=44191825)
        \>I use a humidifier, but don’t want the humidity going up past 60\% ^c44191825

        out of curiosity, what part of the globe do you live (or when was your home built) that you need a humidifier? I have a dehumidifier as it is quite often \> 50\% humidity in my home, easily as much as 65\%, but that's due to the high humidity outside where it can easily be 85\%. Just looked at my sensor, it is currently 81\% outside and 55\% inside. That 55\% is where it really starts to become uncomfortable. I struggle to keep it \<50\% inside. At these indoor humidity levels, it limits some of the things that I can do indoors as it has a negative affect on things I make/do. So adding humidity is just one of those things that makes me tilt my head sideways and go huh? like a dog because it is so out of my experience.

        - **Modified3019** · [2025-06-05 17:12 UTC](https://news.ycombinator.com/item?id=44193601)
          The Pacific Northwest, where today’s humidity is 70\%. ^c44193601

          However that’s basically irrelevant because the place I rent has a 20+ year old central heating and cooling system, so inside the humidity can drop below 40\% and I’ll get painfully dry sinuses and nose bleeds.

          55-60\% is my own comfort zone

        - **rolfus** · [2025-06-05 14:27 UTC](https://news.ycombinator.com/item?id=44192061)
          In cold climates the humidity can drop to uncomfortable levels during the winter (sub 30\% where I live). Especially when combined with wood fired stoves. ^c44192061

    - **joker99** · [2025-06-05 11:23 UTC](https://news.ycombinator.com/item?id=44190519)
      Not the OP, but my airgradients are part of my home assistant setup. They measure the temperature and humidity, and the values are used for controlling the radiators and the humidifiers. Whenever the co2 or ppm count is too high, I flash some leds red to remind whoever is in the room to open a window - which is extremely important because a lot of people don’t have a natural reflex for getting fresh air. This is especially important when we have guests over, in our small living room, the air goes bad fast. ^c44190519

      I was able to improve my sleep because I found out that my waking up in the night was correlated with high co2 values. Same thing with performance in my home office. It’s a small room and the reminder to open a window while I’m in the flow is just amazing.

      But: my airgradient devices were anything but “rock solid“. Constant reboots, hung ESPs, I had to swap out the senseair sensors because apparently they go bad, etc.

      - **kiliankoe** · [2025-06-05 12:30 UTC](https://news.ycombinator.com/item?id=44191023)
        \> I was able to improve my sleep because I found out that my waking up in the night was correlated with high co2 values. ^c44191023

        What did you change? I assume it's non-trivial to automatically open windows based on sensor data? Or do you mean you've been able to improve it by knowing about it and opening a window before going to sleep, which now that I write it sounds much more sensible :D

        - **joker99** · [2025-06-06 10:18 UTC](https://news.ycombinator.com/item?id=44199400)
          Haha, opening a window automatically was my initial idea, but like you I quickly converged on the latter! In addition, I just keep the bedroom door open as well, which helps a little bit too ^c44199400

    - **m4r1k** · [2025-06-05 11:43 UTC](https://news.ycombinator.com/item?id=44190650)
      I'm also an AirGradient user. AirGradient prioritizes accuracy and it's fully OSS. The sensors are fully replaceable; not if but when they eventually lose accuracy. I'd argue that monitoring PM2.5 levels indoors is even more crucial than outdoors. In our home, we have good air recirculation and HEPA filters in every room. Since we began keeping indoor air clean, our spring allergies (and general allergy issues throughout the year) have become much less severe. IMO AirGradient is the best way verify current levels and ultimately ensure the filtration works.
      [https://imgur.com/a/UIkkANL](<https://imgur.com/a/UIkkANL>) ^c44190650

    - **technotarek** · [2025-06-05 11:19 UTC](https://news.ycombinator.com/item?id=44190494)
      Not a fan of my own medical example there. If I knew my kid was going to be blind, there are lots of actions I would take: Educating myself, potentially preparing the home environment etc. ^c44190494

    - **jvanderbot** · [2025-06-05 12:10 UTC](https://news.ycombinator.com/item?id=44190835)
      During wildfire season (which was never a thing for most the USA, but now is thanks to Canadian wildfires and climate change), it's really helpful to get instant particle counts indoors and outdoors. Indoors, you can mitigate with "circulation" mode on your hvac system (to filter through the furnace fitler), or by running air purifiers. Outdoors you can just avoid exposure by coming inside / avoiding trips. ^c44190835

      - **dylan604** · [2025-06-05 13:18 UTC](https://news.ycombinator.com/item?id=44191428)
        That seems like at strange dig at Canada. Since I was a kid, we’ve known about California wildfires even though I’m not from California. Your comment makes it sound like Americans have never had to deal with wildfire smoke pollution until Canada caught fire. That’s just not true ^c44191428

        - **jvanderbot** · [2025-06-05 13:46 UTC](https://news.ycombinator.com/item?id=44191671)
          "Thanks to" was never meant to be a dig! It's certainly not their fault that their forests are drying out, probably from climate change. Wildfires are a tough ecological management problem. ^c44191671

          But yes, the upper midwest and east coast essentially never have had to deal with wildfire smoke like we have now. It's as bad as when I lived in LA, but there we expected it. People in Minnesota, for example, are totally unaccustomed to woodsmog for days on end. The current air quality is very unhealthy - also unheard of. Particle counts in the 100s ppm!

    - **voxlax** · [2025-06-05 20:14 UTC](https://news.ycombinator.com/item?id=44195369)
      I´m living in the middle of a city, and PM2.5 levels get very high at times. We are way above the yearly 5ug/m3 recommendation. So I just bought a lot of air purifiers (just HEPA, everything else commercially available is useless) and they get switched on if the levels get high (via HomeAssistant). I have a device in the garden and another inside, so I am monitoring the difference on a regular basis. I optimize (manually, no fancy data crunching) for low noise produced by the filters and low \<2-3ug/m3 PM2.5 values indoors. I don´t have forced ventilation, so I need to know how much do I open the windows to get humidity and VOCs down, while not letting in too much smog. Sounds more complicated than it really is. ^c44195369

      - **ajolly** · [2025-06-06 10:10 UTC](https://news.ycombinator.com/item?id=44199360)
        If you want quiet, look into a diy computer fan based corsirosenthal box. Also ends up being far cheaper ^c44199360

    - **markasoftware** · [2025-06-05 15:25 UTC](https://news.ycombinator.com/item?id=44192592)
      If you live in a part of the country where wildfire smoke is common, you can use a PM2.5 sensor (which airgradient has -- and air lab does not) to determine if you're effectively keeping the smoke out of your home and can help you determine whether or not to eg use air purifiers. ^c44192592

    - **strogonoff** · [2025-06-05 13:58 UTC](https://news.ycombinator.com/item?id=44191770)
      Among the probably most important and universally relevant measurements offered by air quality monitors is carbon dioxide/monoxide. Humans are not really built for realising when these are elevated, other than feeling sleepy and generally experiencing reduced mental capacity, which by its self-referential nature is not conducive to understanding that you are experiencing reduced mental capacity or being motivated to take measures about it (such as opening windows). ^c44191770

      These are all of the ways in which air monitoring information is actionable for me:

      — Excessive carbon dioxide: as mentioned, it’s a call to open windows and possibly doors, depending on wind direction and window/door configuration in the flat and the building. It can reach surprising, and in my case unsafe by at least one country’s standards, levels overnight if your flat has decent insulation and little airflow. Besides, it just feels nice to have more oxygen knocking about your internals.

      — Excessive (which should really mean non-zero, but in today’s ecology let’s say “elevated”) PM2.5 means I should *close* windows (usually this pollution comes from outside) and ramp up air filtering, and potentially postpone exercise while particulate matter is too high. I have a separate cheap air filter but lately it turned out that a Mitsubishi dehumidifier does a great job at this—which, by the way, I have realized only thanks to an air monitor.

      — If both carbon dioxide and particulate matter are high, I’d most likely open the windows first to lower the former then close the windows and run air filtering while hanging out at the office or having a walk (potentially with an N95 mask on if it’s *really* bad outside).

      — VOC, which often originate from chemicals used in furniture or flooring, if your monitor measures those, could probably be addressed by adding activated carbon layer to your air filter (and by opening windows). I think they are filtered slowly and this might take months, but my monitor did not measure VOCs so I don’t have first-hand experience. An air quality monitor could help you understand whether you are wrong or right in thinking your new floor made your air full of VOCs when all you can go by otherwise is just a vague chemical smell.

      — Elevated background radiation means you should probably just move, usually it is building materials or something not easily removable anyway.

      I would say that with these numbers available there is a danger you’d stress over and min/max them. It’s probably better to just use the measurements to understand the patterns and see if something is really out of ordinary or elevated for prolonged periods of time. I did that first (and did not expect to see how quickly carbon dioxide builds up, how quickly everything deteriorates with any cooking, including when done by a neighbour if I open windows and the wind blows the wrong way, the speed with which outside pollution permeates the indoor space, how effective my air filtering is, etc.), now my air monitor is broken and I am not overly concerned until I have to move to a new place.

  - **RivieraKid** · [2025-06-05 12:35 UTC](https://news.ycombinator.com/item?id=44191058)
    I have AirGradient but this product seems appealing too. It's smaller, portable, doesn't need external power supply and looks better. I also like how the UI looks, it's clearly designed by someone with a visual / artistic taste, the UX could be improved though. ^c44191058

    The big question is accuracy, that's possibly a major advantage of AirGradient.

    - **256dpi** · [2025-06-05 12:48 UTC](https://news.ycombinator.com/item?id=44191164)
      Thanks! AirGradient is great! They do a very good job and served as an inspiration to us! ^c44191164

      On CO2-Sensor Accuracy: Based on AirGradients own research\[1\], the SCD41 (which Air Lab uses) and SenseAir S8 (which AirGradient uses), compare well indoors. In outdoor environments, the AirGradients sensor is generally better. As the Air Lab is primarily focused on indoor environments, we chose the smaller SCD41 to fit the portable design. But yes, If you're looking for an outdoor air quality monitor, AirGradient will be more accurate.

      \[1\]: [https://www.airgradient.com/blog/co2-sensors-photo-acoustic-...](<https://www.airgradient.com/blog/co2-sensors-photo-acoustic-vs-ndir-updated/>)

      - **RivieraKid** · [2025-06-05 19:03 UTC](https://news.ycombinator.com/item?id=44194744)
        How about temperature accuracy? AirGradient did a bunch of tests and adjustments to mitigate effects of insufficient air circulation and heat from electronics. ^c44194744

  - **elif** · [2025-06-05 13:02 UTC](https://news.ycombinator.com/item?id=44191308)
    Likewise I use uHoo sensors which add carbon monoxide, ozone, and PM2.5 and has a full app with phone alerts etc. I have been only satisfied with the sensors which have great algorithms for handling sensor calibration drift ^c44191308

    - **jonah** · [2025-06-05 16:51 UTC](https://news.ycombinator.com/item?id=44193386)
      I'm really surprised more systems don't offer carbon monoxide sensing. To me, it's one that is really important to be aware of. ^c44193386

  - **esskay** · [2025-06-05 10:12 UTC](https://news.ycombinator.com/item?id=44190156)
    Another vote for AirGradient's devices which are great IMO, got a few of them now and they've been very easy to integrate into my setup. ^c44190156

  - **badmorale** · [2025-06-05 10:43 UTC](https://news.ycombinator.com/item?id=44190310)
    AirGradient is fantastic! ^c44190310

  - **unknown** · [2025-06-05 14:25 UTC](https://news.ycombinator.com/item?id=44192036)
    [deleted] ^c44192036

- **unknown** · [2025-06-05 07:42 UTC](https://news.ycombinator.com/item?id=44189330)
  [deleted] ^c44189330

- **finnjohnsen2** · [2025-06-05 10:07 UTC](https://news.ycombinator.com/item?id=44190122)
  Semi off-topic. Anyone know why radon sensor modules are absent as modules one can buy and use in your own arduino-thing? ^c44190122

  - **unknown** · [2025-06-05 14:27 UTC](https://news.ycombinator.com/item?id=44192059)
    [deleted] ^c44192059

- **tgtweak** · [2025-06-06 06:47 UTC](https://news.ycombinator.com/item?id=44198371)
  The price seems very high for the components.  The top airthings with pm2.5, pm1, CO2, radon, humidity, temperature, pressure and full WiFi + cloud connectivity is \$250. ^c44198371

  - **unknown** · [2025-06-06 07:19 UTC](https://news.ycombinator.com/item?id=44198538)
    [deleted] ^c44198538

- **Fnoord** · [2025-06-06 05:40 UTC](https://news.ycombinator.com/item?id=44198090)
  I made my own with Pimoroni (with a small OLED), a Raspberry Pi Zero, a UPS Lite, and a PoE hat (I could switch between these options). Then I updated the OS, Python 2 to 3 and RIP. They sell a Pico version nowadays. It cost me approx 100 EUR with all mats, during Covid pandemic. It worked nice in Prometheus, Grafana, HomeAssistent. Put one outside, too. ^c44198090

  After I bricked it I bought two Switchbot Co2 meter (these got e-paper, though I got those also lying around), for 60 EUR each, used some nanotape to attach these on a spot I like. I use one upstairs and one downstairs. If we sleep with all 4 in same bed, during cooking, or bday parties these go high. Otherwise not. Is it needed? Not really. You physically notice the air quality and take action. Except when you don't. My mother in law doesn't notice her fumes in house (she lost some smelling ability) so I bought her a Switchbot, too.

  There's no way I would pay more than 200 EUR for such a device. Not even 100 EUR. I get it, you're from Switzerland with a high cost of living, but that isn't my problem.

  - **sizzle** · [2025-06-06 06:17 UTC](https://news.ycombinator.com/item?id=44198255)
    How have I never heard of Switchbot, their products look really great and I’m desperately trying to get off the Alexa ecosystem for native apple HomeKit. Do you still recommend them or is there a better HomeKit enabled brand you prefer? ^c44198255

    - **Fnoord** · [2025-06-06 17:02 UTC](https://news.ycombinator.com/item?id=44202866)
      Cannot comment on that as I don't use HomeKit. ^c44202866

  - **unknown** · [2025-06-06 07:19 UTC](https://news.ycombinator.com/item?id=44198539)
    [deleted] ^c44198539

- **tigrezno** · [2025-06-05 12:08 UTC](https://news.ycombinator.com/item?id=44190820)
  I don't get this. My current air purifier (philips) costs like 150€, includes an air quality sensor and the app reports shows graphs with PPM, VOC, whatever.
  Why would I pay double for a device that doesn't even filter the air of my room? ^c44190820

  - **snickmy** · [2025-06-05 12:13 UTC](https://news.ycombinator.com/item?id=44190859)
    different use cases. I don't expect you to go around with your air purifier attached to your neck :) ^c44190859

    - **bravesoul2** · [2025-06-06 13:12 UTC](https://news.ycombinator.com/item?id=44200506)
      Sure but same tech. It'll boil down to economies of scale. ^c44200506

      Also indoor AQ where you spend most of your time is more useful to know. Dust and CO2 are something you can actively reduce.

  - **unknown** · [2025-06-05 14:45 UTC](https://news.ycombinator.com/item?id=44192194)
    [deleted] ^c44192194

- **ceva** · [2025-06-05 13:14 UTC](https://news.ycombinator.com/item?id=44191402)
  Well there is free open source version developed from Serbia [https://klimerko.org/](<https://klimerko.org/>) ^c44191402

  - **unknown** · [2025-06-05 14:27 UTC](https://news.ycombinator.com/item?id=44192055)
    [deleted] ^c44192055

- **net01** · [2025-06-05 09:21 UTC](https://news.ycombinator.com/item?id=44189864)
  I find the specs a bit expensive for what it is, but the software looks really good. ^c44189864

  Specs:

  \- Microcontroller: ESP32-S3

  \- Air sensors: SCD41, SGP41 & LPS22

  \- Display: 296×128 e-paper

  \- Battery: 1500 mAh Li-Po

  \- Anodized aluminium enclosure

  \- Real-time clock

  \- Accelerometer

  \- Wi-Fi & Bluetooth LE

  \- \~7.5 days of battery life

  - **256dpi** · [2025-06-05 09:37 UTC](https://news.ycombinator.com/item?id=44189971)
    That's correct if you just look at the component costs. Unfortunately, to make these in a small series, a lot of other costs come together. If we could, we would offer it a better price. Maybe some time soon! ^c44189971

  - **snickmy** · [2025-06-05 12:25 UTC](https://news.ycombinator.com/item?id=44190980)
    I really feel for the creators here. I was thinking exactly like that before trying to build an electronic device myself. ^c44190980

    Later on I talked to people working in the hardware industry for small production scale, and pretty much told me that a fair pricing is usually 5x to 7x the total BOM (bill of materials).

    After going through that experience myself, I couldn't agree more.
    This device in particular has some extra well thought design and style which might be worth a premium (on top of that 5x/7x multiplier).

  - **unknown** · [2025-06-05 14:28 UTC](https://news.ycombinator.com/item?id=44192069)
    [deleted] ^c44192069

- **Dusksky** · [2025-06-06 05:21 UTC](https://news.ycombinator.com/item?id=44198002)
  [flagged] ^c44198002

  \[dead\]

- **Dkumpikolo** · [2025-06-05 09:49 UTC](https://news.ycombinator.com/item?id=44190031)
  [flagged] ^c44190031

  \[dead\]

- **Y\_Y** · [2025-06-05 08:35 UTC](https://news.ycombinator.com/item?id=44189643)
  [https://www.crowdsupply.com/networked-artifacts/air-lab](<https://www.crowdsupply.com/networked-artifacts/air-lab>) ^c44189643

  \$230 ain't cheap!

  Also, I parsed this as: (open air) (quality measuring device)

  - **unknown** · [2025-06-05 14:28 UTC](https://news.ycombinator.com/item?id=44192065)
    [deleted] ^c44192065

- **unknown** · [2025-06-05 07:46 UTC](https://news.ycombinator.com/item?id=44189344)
  [deleted] ^c44189344

- **Henadz** · [2025-06-06 02:57 UTC](https://news.ycombinator.com/item?id=44197456)
  [flagged] ^c44197456

  \[dead\]

- **unknown** · [2025-06-05 08:16 UTC](https://news.ycombinator.com/item?id=44189535)
  [deleted] ^c44189535

- **wuming2** · [2025-06-05 09:14 UTC](https://news.ycombinator.com/item?id=44189838)
  To be honest, if you have to look at a display to be alerted about bad air quality it’s likely either you know about it already or you are needlessly obsessing. Either way it is the reason I built a service to remote push notify myself. Peace if mind. ^c44189838

  - **samuraijack** · [2025-06-05 09:17 UTC](https://news.ycombinator.com/item?id=44189847)
    Or you are just used to poor air quality so you don’t even notice it anymore. ^c44189847

    - **hazn** · [2025-06-05 09:25 UTC](https://news.ycombinator.com/item?id=44189891)
      and the fact that air quality usually gradually worsens over time. i think it's easier to tell bad air quality when you move in between rooms/spaces. ^c44189891

      but i agree with the op that 'looking' at a display already subconsciously tells you something about the air quality and your relation to it. my air quality sensor \[0\] has a green/orange/red light system though, so i can sometimes just tell that the air quality is bad by a red led flaring up in the corner of my eye.

      \[0\] [https://www.tfa-dostmann.de/en/product/co2-monitor-airco2ntr...](<https://www.tfa-dostmann.de/en/product/co2-monitor-airco2ntrol-mini-31-5006/>)

      previous discussion on the above meter: [https://news.ycombinator.com/item?id\=22764603](<https://news.ycombinator.com/item?id=22764603>)

      - **imp0cat** · [2025-06-06 05:15 UTC](https://news.ycombinator.com/item?id=44197986)
        The AIRCO2NTROL MINI is a great little device to have in a bedroom or living room, the green/orange/led lights are easy to understand (think traffic lights) even by non-technical people. ^c44197986

    - **wuming2** · [2025-06-05 09:36 UTC](https://news.ycombinator.com/item?id=44189964)
      I was referring to looking at a display to be timely informed about an event, crossing the threshold out of acceptable air quality, that can occur at any time of the day. If air quality is consistently bad you don’t need a measuring device but a good air filter. If instead it is not then relying on constantly looking at it is a poor solution. ^c44189964

