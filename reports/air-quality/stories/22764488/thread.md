# [CO2meter: A Python interface to USB CO2 monitor devices](https://news.ycombinator.com/item?id=22764488)

Article: [https://github.com/vfilimonov/co2meter](<https://github.com/vfilimonov/co2meter>)

fanf2 · 2020-04-02 22:18 UTC · 41 reported comments · archived 2026-11-08 11:18 UTC
Observation: 2026-11-08 11:17 UTC → 2026-11-08 11:18 UTC

## Comments

- **joecool1029** · [2020-04-02 23:02 UTC](https://news.ycombinator.com/item?id=22764771)
  This library is for the RAD-0301 meter, marketed as a the co2meter.com mini CO2 meter. I don't know if it works with any other models but as I have one of these, I can tell you it works from my linux machines. ^c22764771

  You're probably going 'Wow that's expensive for a CO2 meter when I can goto Aliexpress and get one for \$10!' This is actually pretty cheap for a NDIR sensor which is what one should use for CO2 monitoring. The cheapo \$10 sensors are all VOC sensors that require calibration and can be affected by airborne pollutants like alcohol.

  I believe this is only 100ppm accuracy, the 5-10ppm resolution sensors are many hundreds of dollars. It's fine enough for casual air quality measurements.

  - **Hasz** · [2020-04-03 05:01 UTC](https://news.ycombinator.com/item?id=22766415)
    For \$20, you can get the MH Z-19, which is a NDIR type. You can talk to it over UART, and it comes in a 5000ppm and 2000ppm model IIRC. Decent documentation, and a good little sensor. ^c22766415

    The S8-0053 looks interesting, but I have no experience with it. Also NDIR, boasts +- 40ppm accuraxy -- the room air might not even be that homogeneous...

    The cheap ones are electrochemical, and they're not even that cheap.

    [https://sandboxelectronics.com/files/SEN-000007/MG811.pdf](<https://sandboxelectronics.com/files/SEN-000007/MG811.pdf>)

    - **polskibus** · [2020-04-03 13:37 UTC](https://news.ycombinator.com/item?id=22768994)
      Problem with it is that it autorecalibrates itself every 24hrs as far as I remember. It is a problem in room monitoring where you have constant high CO2- you'd have to take the sensor outside to fix it's reference level. ^c22768994

  - **petsfed** · [2020-04-02 23:16 UTC](https://news.ycombinator.com/item?id=22764862)
    The core device is typically on the order of \$50-\$150 US, but with many of the sensors that CO2meter sells, you're also getting a microcontroller, display, power supply, etc. You'll frequently find temperature and humidity sensors and also barometric pressure sensors rolled into that, since NDIR is affected by all those things. ^c22764862

    So the price of a good, fully realized NDIR CO2 meter is comparable with any low-volume, moderate precision, moderate complexity electronic device.

  - **Klinky** · [2020-04-02 23:38 UTC](https://news.ycombinator.com/item?id=22765005)
    Andreas Spiess has a good video on VOC vs CO2 sensors. ^c22765005

    [https://www.youtube.com/watch?v\=FL0L-nic9Vw](<https://www.youtube.com/watch?v=FL0L-nic9Vw>)

    - **Rebelgecko** · [2020-04-03 05:05 UTC](https://news.ycombinator.com/item?id=22766432)
      His channel is a goldmine for anyone who plays around with ESP-32 microcontrollers or similar devices ^c22766432

- **lhoff** · [2020-04-02 22:35 UTC](https://news.ycombinator.com/item?id=22764603)
  Iam looking to build my own CO2 Meter for a while know. I even thought about making a little series as christmas presents. 
  My struggle always was to pick the right module. Its so hard to pick one and really trust it when you don't have a reference. ^c22764603

  So i thought maybe i give this sensor a shot but i can't find a reputable source for it. Does someone knows where to buy it or uses another module that works good?

  - **petsfed** · [2020-04-02 22:51 UTC](https://news.ycombinator.com/item?id=22764695)
    I'm fond of the Sensirion SCD30. Its low cost, low power, and easy to interface with. A lot of NDIR CO2 sensors pull 5V, so the sensirion's 3.3v power is nice. Digikey is currently out of them, but SparkFun has them in stock. Nice for hobbyists! ^c22764695

    CO2meter.com is a good source for buying OEM CO2 sensors, although a little too coy with manufacturer's data sheets, in my opinion.

    Virtually all NDIR CO2 sensors use some sort of automatic calibration, where the lowest reading in a certain period of time is assigned the value 450ppm. If that's accurate for your area and you can guarantee that the space the sensor is monitoring is unoccupied during that period of time, its not bad. Otherwise, a reference gas is the only way to really trust the readings.

    - **unknown** · [2020-04-03 01:48 UTC](https://news.ycombinator.com/item?id=22765687)
      [deleted] ^c22765687

  - **411111111111111** · [2020-04-03 05:54 UTC](https://news.ycombinator.com/item?id=22766628)
    i was shopping around last year as well. i finally went with \`TFA Dostmann AirControl Mini CO2 Meter\`, you can get the data pretty easily \[1\] if you connect it to a raspberry pi (or any linux system, really), so i'm currently pushing it through MQTT to my HomeAssistant.
    i was really surprised when i started monitoring it how closely related my concentration is to the co2 ppa in my home. ^c22766628

    \[1\] [https://github.com/maddindeiss/co2-monitor](<https://github.com/maddindeiss/co2-monitor>)

    - **Arkanosis** · [2020-04-03 21:10 UTC](https://news.ycombinator.com/item?id=22773980)
      This is a great device. We've never had windows open as much as since we have it, and believe me, it means a lot of headaches that go away every week without any coffee or paracetamol. ^c22773980

      The next time we move house, proper ventilation is definitely one of the first things we'll check.

    - **xenonite** · [2020-04-06 06:36 UTC](https://news.ycombinator.com/item?id=22791363)
      This device is a rebranded RAD-0301 meter. In Germany, this brand seems to be the easiest way for purchasing the RAD-0301. ^c22791363

  - **gsich** · [2020-04-02 22:58 UTC](https://news.ycombinator.com/item?id=22764746)
    mh-z14 or mh-z19. ^c22764746

    Automatic calibration can be disabled.

    - **ClumsyPilot** · [2020-04-03 01:46 UTC](https://news.ycombinator.com/item?id=22765682)
      I use those, on ESPHome and connected to homeassistant. 
      They seem to provide reasonable readings ^c22765682

  - **throwaway9d0291** · [2020-04-03 08:48 UTC](https://news.ycombinator.com/item?id=22767368)
    \+1 for Sensirion's SCD30 \[0\], or even better when it comes out, SCD40. ^c22767368

    I've tested a lot of different sensors and the SCD30 is more expensive than the Chinese sensors but in my experience it's much more accurate. The problem with all of these sensors is calibration. They naturally drift over time so you need some way to compensate for that. There are a few common approaches:

    \- Assume that every single day, the sensor is completely immersed in fresh air at some point - this is the way the MH-Z19 series of sensors works. It can make sense in business HVAC systems where it's common to do a fresh air purge every 24h but in a residential environment it's unreliable because there's no guarantee that a room will return to fresh air levels of CO2 (e.g. if a room only has 3-4h unoccupied and the windows aren't open, it might not return to 400ppm). To be clear, this isn't a problem unique to the Chinese sensors. There are also expensive sensors from major and reputable manufacturers that act this way, again, because it's common in commercial HVAC systems to do a daily fresh-air purge.

    \- The above but a bit more intelligent - this is the SCD30's method: it looks at the previous 7 days of data and only if there were at least 5 days where the baselines are within 50ppm of each other, treats the average of those baselines as the fresh air concentration. This makes it fantastic for residential applications. Even if your room's CO2 levels don't return to 400ppm every day, as long as they don't consistently return to another baseline, the auto-calibration cycle won't run and mess up your data.

    \- Manually do a baseline calibration every few months: make the user take the sensor outside into fresh air (or vent a building with fresh air) and tell the sensor "the CO2 concentration right now is 400ppm" - this is the only way the MH-Z19 and similar sensors can really be made anything close to accurate.

    Also, make sure to avoid anything other than NDIR sensors. There are a lot of "eCO2" sensors that give you **estimated** CO2 levels based on VOCs, which always results in garbage readings.

    Finally, you can usually buy the SCD30 very easily. It's routinely stocked by electronic component distributors so you can just look it up in OctoPart\[1\]. Make sure to avoid the eval kits though.

    \[0\]: [https://www.sensirion.com/en/environmental-sensors/carbon-di...](<https://www.sensirion.com/en/environmental-sensors/carbon-dioxide-sensors/carbon-dioxide-sensors-co2/>)

    \[1\]: [https://octopart.com/search?q\=Sensirion+SCD30&currency\=USD&s...](<https://octopart.com/search?q=Sensirion+SCD30%C2%A4cy=USD&specs=0>)

    - **toasted\_flakes** · [2020-04-03 08:54 UTC](https://news.ycombinator.com/item?id=22767391)
      \> it looks at the previous 7 days of data and only if there were at least 5 days where the baselines are within 50ppm of each other, treats the average of those baselines as the fresh air concentration. ^c22767391

      Is that documented anywhere? I couldn't figure out why mine is reading garbage, it could be that it didn't see fresh air every day for a full week

      - **throwaway9d0291** · [2020-04-03 10:16 UTC](https://news.ycombinator.com/item?id=22767793)
        The main public information is page 13 of the interface description \[0\]. I got some more specifics from Sensirion directly when I contacted them (the 50ppm minima thing in particular). ^c22767793

        Not seeing fresh air for a week isn't enough to throw it off, it needs to not have seen fresh air for a week \_and\_ the baselines that it has seen have to be within 50ppm of each other.

        Have you allowed it to calibrate even once? It needs 7d of uninterrupted power and daily fresh air for the initial calibration.

        You can also do forced calibration against a known value using the process on page 14 of \[0\].

        It can also give iffy results if the temperature/humidity values are totally out of whack, which could happen if it's put in an enclosure or something like that. You can set an offset using the instructions on page 15 of \[0\].

        There's also altitude compensation but unless you're doing something really weird that shouldn't affect you so much.

        Finally, there's sensor placement \[1\]. It shouldn't be placed in such a way that there's a lot of air flowing over it directly (e.g. exposed to the air). If it's in front of a fan or something it's going to do weird things.

        I'd suggest placing it outside for a few minutes and see what the readings are. If they're far from 400ppm it definitely needs calibrating.

        \[0\]: [https://www.sensirion.com/fileadmin/user\_upload/customers/se...](<https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.5_CO2/Sensirion_CO2_Sensors_SCD30_Interface_Description.pdf>)

        \[1\]: [https://www.sensirion.com/fileadmin/user\_upload/customers/se...](<https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.5_CO2/Sensirion_SCD30_Design-In_Guidelines_D1.pdf>)

        - **petsfed** · [2020-04-03 15:49 UTC](https://news.ycombinator.com/item?id=22770452)
          "There's also altitude compensation but unless you're doing something really weird that shouldn't affect you so much." ^c22770452

          Disagree. I've moved co2 sensors between sea level and 2000m, and measured reference 400ppm gas and seen quite large differences (\~150ppm). So it can matter. That's the reason why the SCD30 allows you to set an altitude or pressure.

          But its not important enough to constantly feed it pressure data, a once-a-day pressure reading from the NWS would be sufficient.

        - **toasted\_flakes** · [2020-04-03 14:05 UTC](https://news.ycombinator.com/item?id=22769227)
          Brilliant, thanks. I didn't realise the threshold was 5 days out of a full week, and didn't remember reading about the 50ppm minima. ^c22769227

      - **lorenzhs** · [2020-04-03 09:41 UTC](https://news.ycombinator.com/item?id=22767616)
        It's mentioned in the data sheet: [https://www.sensirion.com/fileadmin/user\_upload/customers/se...](<https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.5_CO2/Sensirion_CO2_Sensors_SCD30_Datasheet.pdf>) and you can disable it: [https://www.sensirion.com/fileadmin/user\_upload/customers/se...](<https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.5_CO2/Sensirion_CO2_Sensors_SCD30_Interface_Description.pdf>) ^c22767616

  - **mataug** · [2020-04-02 22:39 UTC](https://news.ycombinator.com/item?id=22764620)
    \+1 on this, ^c22764620

    Where does one buy a reliable indoor sensor ?

- **foobarbecue** · [2020-04-03 00:42 UTC](https://news.ycombinator.com/item?id=22765349)
  Hunh. I've been working with gas monitoring for years (mostly during my volcanology PhD) and written lots of code to interface with many CO2 sensors, usually as part of packages that talked to many other sensors. Other than some weird binary protocols, it was all straightforward, brainless code so I never thought it needed to be published. LMK if anybody wants a hand with anything specific. ^c22765349

  - **bjelkeman-again** · [2020-04-03 05:54 UTC](https://news.ycombinator.com/item?id=22766627)
    What would be a good oxygen air sensor? ^c22766627

    - **foobarbecue** · [2020-04-03 15:07 UTC](https://news.ycombinator.com/item?id=22769946)
      I've used a few multigas sensors that had O2 when mapping volcanic caves -- Draeger Multiwarn, MultiRAE, National... Safety (?), and CrowCon GasMan. The CrowCon was my favorite by far. Disclosure: they gave us equipment for free as sponsorship for our expedition, but it was also honestly just way better than the Draeger or RAE. Great datalogger built-in with good serial interface, small, waterproof enough for our uses (the others said IP68 and still died of water damage). I suspect all CrowCon products are quite good and cheaper than the competition. ^c22769946

    - **foobarbecue** · [2020-04-04 12:58 UTC](https://news.ycombinator.com/item?id=22777979)
      Or, if you're building your own unit, then I remember citytech (welcome to city tech!) was pretty much the only option when I was doing it. The circuits to run electrochemical gas sensors are a little annoying to set up. ^c22777979

- **smcleod** · [2020-04-02 23:20 UTC](https://news.ycombinator.com/item?id=22764888)
  I had a good play with MH-Z19 Co2 sensors and some basic python, here's some photos (and some old crappy code): [https://github.com/sammcj/CO2-Logger\#photos](<https://github.com/sammcj/CO2-Logger#photos>) ^c22764888

- **platz** · [2020-04-03 00:14 UTC](https://news.ycombinator.com/item?id=22765191)
  I'd be more interested in VOC sensors or PM2.5 sensors. ^c22765191

  I feel like PM sensors are easy to understand.  I wish i had a better grasp on VOC/TVOC though.

  It's hard to interpret what an elevated VOC from my foobot actually means.

  - **gh02t** · [2020-04-03 13:48 UTC](https://news.ycombinator.com/item?id=22769082)
    I've used the Plantower PMS7003 sensors for some DIY particulate sensors. I don't have a lab reference to calibrate against, but they should be pretty accurate as they are a laser sensor and the readings I got out of them were very sensible and consistent. Plus they include a tiny fan, which is important to get good readings. They are easy to use as well, it's just a simple UART digital interface. I also experimented with the cheaper Sharp IR dust sensors, but these were much less stable and also require constant calibration; they were ok for doing simple relative readings but they were clearly very inaccurate and unstable. ^c22769082

    Sensing VOC's accurately is really difficult because most sensors have radically different (orders of magnitude) sensitivities to multiple compounds but can't actually distinguish between them. The readings typically get heavily skewed by the presence of minute amounts of some compound the sensor is very sensitive to. I tried several sensors and the best I could get out of them was a relative "good / bad" reading.

    - **platz** · [2020-04-03 17:12 UTC](https://news.ycombinator.com/item?id=22771626)
      The PMS7003 looks like a great option, thanks! ^c22771626

- **gh02t** · [2020-04-02 22:59 UTC](https://news.ycombinator.com/item?id=22764748)
  Interesting, but does anybody know which USB meter is this meant to be used with? I can't actually find it in any of the docs or links, but maybe I'm overlooking it. ^c22764748

  - **warp** · [2020-04-03 01:04 UTC](https://news.ycombinator.com/item?id=22765471)
    This one I think: ^c22765471

    [https://www.amazon.com/CO2Meter-RAD-0301-Mini-Monitor-White/...](<https://www.amazon.com/CO2Meter-RAD-0301-Mini-Monitor-White/dp/B00H7HFINS/>)

  - **lhoff** · [2020-04-02 23:02 UTC](https://news.ycombinator.com/item?id=22764772)
    There is a link to a manual for the ZG01 CO2 Module at the bottom of the page. So i guess the lib is for that module. But i couldn't find a source to buy that. ^c22764772

- **xenonite** · [2020-04-03 09:51 UTC](https://news.ycombinator.com/item?id=22767661)
  Great, this works instantly with my recently purchased TFA AirCO2ntrol Mini \[1\]. Moderately priced for EUR 65, this gives relatively accurate readings (the maximum of ±7\% or ±100ppm for values \<\=2000ppm, and ±10\% for values \>2000ppm). ^c22767661

  \[1\] [https://www.tfa-dostmann.de/en/produkt/co2-monitor-airco2ntr...](<https://www.tfa-dostmann.de/en/produkt/co2-monitor-airco2ntrol-mini/>)

  - **xenonite** · [2020-04-06 06:35 UTC](https://news.ycombinator.com/item?id=22791361)
    This device probably is a rebranded RAD-0301 meter. ^c22791361

- **toasted\_flakes** · [2020-04-03 08:46 UTC](https://news.ycombinator.com/item?id=22767359)
  I have a scd30 from Sensirion, hooked up to a raspberry pi GPIO pins, with a python script pushing the measurement to InfluxDB and Grafana. ^c22767359

  It's super cool how open source projects make it easy to get a great UI, built-in basic statistics etc, with a few hours of datasheet reading.

  Word of warning though: make a proper enclosure for the sensor. Mine is now perpetually reading 1400 ppm or above after a fairly rough move, even outside (where it should be about 415 ppm).

- **doitLP** · [2020-04-03 03:19 UTC](https://news.ycombinator.com/item?id=22766054)
  Great to see this here. I started monitoring the CO2 levels in my new apartment after waking up with headaches every night since moving in. ^c22766054

  Plugged it in and the alarm started going off immediately at 3000ppm. I use this package to graph out the readings.

  Recently started at a new job and had to educate everyone on the issues with CO2 build up in meeting rooms. We got each meeting room outfitted with a sensor and custom monitoring with grafana now.

- **awinter-py** · [2020-04-03 00:49 UTC](https://news.ycombinator.com/item?id=22765398)
  cool that it has a timeseries! I'm not familiar with this space but 'timeseries for iot' is a consumer category that I would be a consumer of ^c22765398

  (really could be just me though)

- **tito** · [2020-04-02 23:32 UTC](https://news.ycombinator.com/item?id=22764970)
  Gut check here, could you share what you want to use a CO2 monitor for? ^c22764970

  - **losteric** · [2020-04-03 00:20 UTC](https://news.ycombinator.com/item?id=22765227)
    Monitoring CO2 levels? Personally, I want a discrete meter for monitoring levels in meetings... especially large design/product discussions. I suspect some of our meeting rooms have poor ventilation and CO2 build up contributes to increasingly dumb discussions. ^c22765227

    - **tito** · [2020-04-03 00:45 UTC](https://news.ycombinator.com/item?id=22765373)
      Awesome! That's what I figured but wanted to check. Yes, indoor air in meeting rooms gets crazy, easily above 1000 ppm. ^c22765373

  - **gbear605** · [2020-04-03 00:24 UTC](https://news.ycombinator.com/item?id=22765258)
    [https://slatestarcodex.com/2018/08/23/carbon-dioxide-an-open...](<https://slatestarcodex.com/2018/08/23/carbon-dioxide-an-open-door-policy/>) gives a decent reason why you should care about controlling (and thus monitoring as a first step) internal CO2 levels. ^c22765258

  - **bjelkeman-again** · [2020-04-03 06:01 UTC](https://news.ycombinator.com/item?id=22766646)
    Indoor growing, CO2 levels drop and so does the plants ability to grow. ^c22766646

