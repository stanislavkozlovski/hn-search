# [Air Quality Monitors Compared: AirGradient vs. Purple Air](https://news.ycombinator.com/item?id=40362848)

Article: [https://www.airgradient.com/blog/airgradient-vs-purple-air/](<https://www.airgradient.com/blog/airgradient-vs-purple-air/>)

ahaucnx · 2024-05-15 03:37 UTC · 54 reported comments · archived 2026-11-08 13:32 UTC
Observation: 2026-11-08 13:32 UTC → 2026-11-08 13:32 UTC

## Comments

- **squarefoot** · [2024-05-15 05:42 UTC](https://news.ycombinator.com/item?id=40363472)
  Does anyone know of a reliable and cheap CO2 monitor (other data about air quality is not needed) for a music room that will be kept almost tight closed with potentially more than 1 person playing music? I need to know when levels will rise above normal so that we can stop and take a pause to exchange air. I've done some research and found complains about fake products coming from the usual suspects, some of which use alcohol sensors disguised as CO2 ones, which of course don't work. 
  I've taken DIY into consideration, then again discovered they sell fake parts too, like some MH-Z19 modules found on Ali\* and elsewhere. ^c40363472

  - **ahaucnx** · [2024-05-15 05:48 UTC](https://news.ycombinator.com/item?id=40363506)
    The most important thing is that you use an NDIR CO2 sensor. The best are in my opinion from SenseAir (e.g. the S8 that we use in our monitors). Then you can also get them from Sensirion, Winsen or Cubic. I believe for normal operations they perform all quite well. ^c40363506

    Important is that you can adjust the automatic baseline calibration duration if you operate the sensor in a closed space that does not regularly get fresh air. Ideally put it into a longer period like 30 or 90 days or switch off and manually calibrate it regularly. I believe not many monitors offer that flexibility out of the box.

    If you have some basic electronic skills, you can actually look at our open source build instructions and just build the basic monitor with the CO2 module \[1\].

    \[1\] [https://www.airgradient.com/documentation/diy-v4/](<https://www.airgradient.com/documentation/diy-v4/>)

    - **summm** · [2024-05-15 19:33 UTC](https://news.ycombinator.com/item?id=40371332)
      Wouldn't a dual-beam NDIR like the SCD30 be much better in that regard, with much fewer calibration issues? ^c40371332

  - **BrianHenryIE** · [2024-05-15 05:47 UTC](https://news.ycombinator.com/item?id=40363503)
    When I did the research: Aranet4 ^c40363503

    [https://www.amazon.com/dp/B07YY7BH2W](<https://www.amazon.com/dp/B07YY7BH2W>)

    I bought one for myself, fine, then two for my siblings. The two I bought them always measured about 100 apart, when right beside each other.

    To say – use the measurements as a comparison of what you know.

    - **xvector** · [2024-05-15 08:05 UTC](https://news.ycombinator.com/item?id=40364296)
      I have this too and it's a lovely device. E-ink screen looks perfect, mine has lasted for months and I don't even think about the battery. ^c40364296

  - **IanCal** · [2024-05-15 09:18 UTC](https://news.ycombinator.com/item?id=40364717)
    You may be over-engineering things. Since there's no specific cutoff or precise value you need before calling a break, you could probably work out what rate things would increase at per typical person given the volume of the room and then just have a timer. Something like "Calm - 120 people-minutes, Energetic - 60 people-minutes, so three people really going for it means we take a break every 20". ^c40364717

    Maybe this isn't enough for you, but I know it's easy for me to get trapped in a rabbit hole of how to solve things in a specific way and at times I need to pull back and say "what am I *actually* trying to solve". I had this with co2 monitors, getting fairly into which one to get then I realised I can deal with this by just regularly opening the window. I don't *need* a specific number.

    edit -

    Air exchange may happen pretty quickly, depending on the room and surroundings, so it could be as easy as "every X minutes we take a moment to open the door and window".

  - **pstrateman** · [2024-05-15 06:42 UTC](https://news.ycombinator.com/item?id=40363802)
    An indoor CO2 meter that never goes outside will be miscalibrated almost immediately. ^c40363802

    They have self calibration routines that assume they see atmospheric CO2 levels at least once either per day or per week

    If it's always inside that assumption is wrong and it will always report lower than true CO2 levels.

    - **D13Fd** · [2024-05-27 11:33 UTC](https://news.ycombinator.com/item?id=40489818)
      This is pretty much irrelevant though. I have a CO2 monitor for a closed space. Heavy exercise with the door closed will set off the 1500 PPM alarm every time. Do I care that it is off by maybe +/- 200 PPM? Not at all. It still absolutely serves its purpose of sounding an alarm when the air gets stale. ^c40489818

    - **squarefoot** · [2024-05-15 08:40 UTC](https://news.ycombinator.com/item?id=40364528)
      Thanks, I read about the need of recalibrating sensors, although didn't imagine that would be needed so often. Thankfully I recently moved to a very clean air area with trees and such, so exposing the sensor to clean air would just involve moving it a few meters outside. ^c40364528

    - **poulpy123** · [2024-05-15 18:32 UTC](https://news.ycombinator.com/item?id=40370636)
      Mine is indeed not perfectly calibrated since it sometimes gives value that are lower than the outside air, but the scheme of things, being off by 20 or 50ppm isn't going to change anything ^c40370636

      - **pstrateman** · [2024-05-15 19:19 UTC](https://news.ycombinator.com/item?id=40371179)
        If you're getting values lower then atmospheric then the readings are if by much more than 20 to 50 ppm. ^c40371179

        - **poulpy123** · [2024-05-16 12:14 UTC](https://news.ycombinator.com/item?id=40377366)
          why ? ^c40377366

    - **poulpy123** · [2024-05-15 18:32 UTC](https://news.ycombinator.com/item?id=40370635)
      Mine is indeed not perfectly calibrated since it sometimes gives value that are lower than the outside air, but the scheme of things, being off by 20 or 50ppm isn't going to change anything ^c40370635

  - **joecool1029** · [2024-05-15 08:34 UTC](https://news.ycombinator.com/item?id=40364483)
    I bought a co2meter.com model RAD-0301 \~6 years ago that was probably the cheapest prebuilt NDIR unit at the time. It just shows CO2 ppm and temperature. ^c40364483

    It looks like they've slightly improved the features and dropped the cost more on their followup model [https://www.co2meter.com/products/co2mini-indoor-air-quality...](<https://www.co2meter.com/products/co2mini-indoor-air-quality-monitor>) this is not going to be lab grade accurate but if it works as well as their old one it's great for the price and fits your requirement.

  - **sofixa** · [2024-05-15 10:53 UTC](https://news.ycombinator.com/item?id=40365211)
    I'm a fan of Apollo Automation's AIR and MSR sensors that do a bunch of things, including CO2. They're ESP32 based, very easy to integrate with Home assistant with good UX. ^c40365211

  - **fifteenforty** · [2024-05-15 09:03 UTC](https://news.ycombinator.com/item?id=40364646)
    \- Aranet4 ^c40364646

    \- AirThings View Plus

    \- Sensiron CO2 Gadget [https://www.sensirion.com/products/catalog/SCD4x-CO2-Gadget/](<https://www.sensirion.com/products/catalog/SCD4x-CO2-Gadget/>)

    \- Kickstarter: AirSpot [https://www.kickstarter.com/projects/airspot/airspot-the-per...](<https://www.kickstarter.com/projects/airspot/airspot-the-personal-and-wearable-fresh-air-monitor>)
     (uses the Sensiron sensor)

    - **nov21b** · [2024-05-15 18:44 UTC](https://news.ycombinator.com/item?id=40370781)
      Happy user of the Airthings Wave Plus (same as View but without a display). Major feature requirement was being able to fetch the sensor values with just a Bluetooth connection. ^c40370781

  - **gnosek** · [2024-05-15 10:56 UTC](https://news.ycombinator.com/item?id=40365228)
    I'm happy with a TFA Dostmann 31.5009.02 Monitor CO2 AIRCO2NTROL Coach. Does what it says and you can get the measurements over USB if you want too. ^c40365228

  - **defrost** · [2024-05-15 07:04 UTC](https://news.ycombinator.com/item?id=40363928)
    As it's come up repeatedly, here's more about ( CO2 ) calibration: [https://www.co2meter.com/en-au/blogs/news/7512282-co2-sensor...](<https://www.co2meter.com/en-au/blogs/news/7512282-co2-sensor-calibration-what-you-need-to-know>) ^c40363928

    .. pretty much all instrumentation requires semi regular calibration, it varies by how often and how serious you are about exact results.

    Many CO2 meters are sensitive to dirt \| dust \| crud build up ( see article ) and should be reset semi regularly as per the manual (or by the linked site guidelines if you've gotten a cheap one with no documentation).

  - **dzhiurgis** · [2024-05-15 07:16 UTC](https://news.ycombinator.com/item?id=40364007)
    Qingping sends me notification once set threshold is reached ^c40364007

    - **pasc1878** · [2024-05-15 07:29 UTC](https://news.ycombinator.com/item?id=40364070)
      Unfortunately my Jinping's temperature sensor does not agree with sensors of 3-4 different makes I have it always reads 3-4 degrees C below the others. ^c40364070

      - **dzhiurgis** · [2024-05-15 11:04 UTC](https://news.ycombinator.com/item?id=40365282)
        Yep same here. Temperature seems weird. It has offset option but didn't work correctly for me. CO2 and PM seem ok, but I don't have anything to calibrate with except outdoors. ^c40365282

        - **pasc1878** · [2024-05-17 18:14 UTC](https://news.ycombinator.com/item?id=40392695)
          I do have CO2 monitors and they agree. ^c40392695

          PM I have something that shows air quality and it shows 0 and high at the same time as the Qingping

- **rcdemski** · [2024-05-15 04:17 UTC](https://news.ycombinator.com/item?id=40363055)
  I appreciate them not trying to upsell their product, but give what seems like an honest comparison to their competitor.
  I have a Purple Air monitor and it’s done me well, but it’s great seeing an alternative with better access to the data.
  I may have to give it a shot! ^c40363055

  - **ahaucnx** · [2024-05-15 04:46 UTC](https://news.ycombinator.com/item?id=40363194)
    Yes and to be honest, most of the air quality monitors use very similar PM modules. ^c40363194

    So often there is not too much difference in the accuracy of the monitors. I wrote about this some time ago \[1\].

    However when it comes to data ownership, API access, costs and repairability that's where there are big differences. In many reviews these aspects are in my opinion not enough covered.

    \[1\] [https://www.airgradient.com/blog/most-aq-monitors-use-same-p...](<https://www.airgradient.com/blog/most-aq-monitors-use-same-pm-modules/>)

    - **nucleardog** · [2024-05-15 07:50 UTC](https://news.ycombinator.com/item?id=40364180)
      Since it seems like I’m the only person that seems to have ever bought one, wanted to mention the AirQ\[0\] as a thing that exists! ^c40364180

      It’s got the PMSA003 which doesn’t seem to be used by anything else on that list, though I’m guessing from a quick glance at the spec sheet is substantially similar.

      Part of why I went with this one was because it was relatively open. They do offer a cloud service and things most people would expect, but the device will work out of the box with no account or internet connection. Mobile app works too. It stores some historical data on the device so you still get nice graphs and charts.

      If you punch the device’s IP in a browser it gives you a page back where it dumps all the data back at you. There’s an actively maintained Home Assistant integration.

      All the sensors are replaceable. Or swappable if you decide you would really rather measure something else later. (Don’t know about buying the component and soldering it on yourself, but they sell the sensors on the little daughter boards that can be swapped.)

      Only real downside I can think of is… it’s not particularly cheap.

      Mostly just mentioning it in case it ends up on some of those charts later. ;) Biggest challenge with any of these measurement devices is… I have no reference to compare to or any way to evaluate the accuracy. (Lemme tell you about the time I tried to measure the humidity around here… I now own a psychrometer as a reference device since I figured that’d be pretty hard for any manufacturer to fuck up \_too\_ badly.) I’d definitely be curious to see how it stacks up.

      \[0\] [https://en.air-q.com/produktvarianten](<https://en.air-q.com/produktvarianten>)

  - **jhot** · [2024-05-15 06:19 UTC](https://news.ycombinator.com/item?id=40363665)
    I, too, am not a fan of their paid API changes, but you can configure your purple air to send the data to any URL you'd like. I have an endpoint that parses the payload and sends the pm25 and temperature to home assistant. ^c40363665

    That said, I have definitely considered an airgradient and the esphome firmware.

  - **poulpy123** · [2024-05-15 09:50 UTC](https://news.ycombinator.com/item?id=40364889)
    they have very interesting articles on the topic, and I'm happy with the monitor I bought from them. Although I can't compare it to a reference, they were tested by the company/institute monitoring the air quality of paris and got a good score. I just which they could register their data on a sd card. ^c40364889

    They are open source, and provide the code source of their software as well as for the hardware, which is very rare. I have plan one day to build my own outdoor monitor based on their plans (as a project I don't have the usage)

- **flacebo** · [2024-05-15 09:40 UTC](https://news.ycombinator.com/item?id=40364843)
  I got a DIY basic kit, and was pretty surprised when I saw that after 8 hours of sleep the CO2 level was 3600 ppm in the bedroom. My wife still jokes about the way I woke her up. I immediately said "We're basically suffocating". Maybe it was a little bit too dramatic sure, but kind of true. ^c40364843

  The levels go above 1000 ppm in less than an hour with both of us in there.

  Opening the windows to ventillate doesn't really solve this, as you'd need to keep opening and closing them every hour. I'm thinking about installing a HRV system, but struggling to find a model that could be integrated into Home Assistant. (ERV not necessary as I live in a european country with temperate climate, the humidity is mostly OK)

  In the meantime I have two windows tilted open permanently in another room with the doors open. This keeps CO2 under 1000 ppm, but pretty bad for energy efficiency.

  Overall pretty happy with the product, definitely made me much more aware of the air quality. I want to build a portable one with a display and logging to check out the car, the office, maybe the hotel rooms on a trip, the plane, etc.

  - **infecto** · [2024-05-15 10:06 UTC](https://news.ycombinator.com/item?id=40364983)
    I don’t believe co2 is as statistically significant of a problem as you are making it out to be. I believe some of the originally literature around this really made it overblown. ^c40364983

    - **sooheon** · [2024-05-15 10:22 UTC](https://news.ycombinator.com/item?id=40365055)
      There's good evidence to think complex cognitive tasks (like strategizing, coding...) suffer with CO2 \> 1000 ppm ^c40365055

      [https://www.sciencedirect.com/science/article/pii/S036013232...](<https://www.sciencedirect.com/science/article/pii/S036013232300358X>)

      - **infecto** · [2024-05-15 12:07 UTC](https://news.ycombinator.com/item?id=40365817)
        I do believe the science is out in areas like the described, it could very well impact high cognitive tasks and can easily imagine that being true. I still don't believe it is suffocating the brain like described by the poster. ^c40365817

    - **gureddio** · [2024-05-15 10:20 UTC](https://news.ycombinator.com/item?id=40365047)
      It really does feel like this is the current worry in the tech sphere, and somewhat unnecessarily ^c40365047

  - **thaumasiotes** · [2024-05-15 10:01 UTC](https://news.ycombinator.com/item?id=40364960)
    \> I immediately said "We're basically suffocating". Maybe it was a little bit too dramatic sure, but kind of true. ^c40364960

    Carbon dioxide is one of just a very few air quality problems for which you have strong inborn biological detection systems. If you don't feel like it's suffocating you, it isn't.

    - **flacebo** · [2024-05-15 10:34 UTC](https://news.ycombinator.com/item?id=40365134)
      Of course, these CO2 levels are smaller by at least one order of magnitude than what could cause suffocation. I overdramatized the fact that the air quality was really, really bad. ^c40365134

      Based on every article I found, above 1000 ppm clearly affects sleep quality, cognitive performance, it causes headaches, etc. so 3600ppm is generally considered really bad.

      Even if CO2 would be harmless in itself, it is a good indicator for bad ventillation.

      - **thaumasiotes** · [2024-05-15 18:17 UTC](https://news.ycombinator.com/item?id=40370482)
        \> Based on every article I found, above 1000 ppm clearly affects sleep quality, cognitive performance, it causes headaches, etc. ^c40370482

        Sleep quality and cognitive performance are often difficult to perceive in yourself.

        Headaches aren't like that at all. If every article you found states that CO2 above 1000 ppm causes headaches, that should reflect poorly on everything else in all of those articles.

        \> Even if CO2 would be harmless in itself, it is a good indicator for bad ventilation.

        This is perfectly true.

- **xnx** · [2024-05-15 04:28 UTC](https://news.ycombinator.com/item?id=40363106)
  [https://www.airthings.com/view-plus](<https://www.airthings.com/view-plus>) isn't included in this comparison, but should be. Very happy with it. ^c40363106

  - **ahaucnx** · [2024-05-15 04:42 UTC](https://news.ycombinator.com/item?id=40363169)
    We plan to compare more monitors. This is the first of this kind of reviews so we want to first see how well it is accepted and then do more. ^c40363169

- **phinnaeus** · [2024-05-15 06:35 UTC](https://news.ycombinator.com/item?id=40363760)
  FYI The "Buy as Kit" link on [https://www.airgradient.com/outdoor/\#comparison](<https://www.airgradient.com/outdoor/#comparison>) actually takes you to the Indoor monitor kit in the shop instead of the Outdoor kit. ^c40363760

  - **ahaucnx** · [2024-05-15 06:47 UTC](https://news.ycombinator.com/item?id=40363831)
    Thanks for letting me know. It's fixed now. ^c40363831

- **jumploops** · [2024-05-15 04:20 UTC](https://news.ycombinator.com/item?id=40363071)
  Does anyone have an opinion on which VOC sensor is better? ^c40363071

  It appears the Purple Air uses the Bosch BME688 while the AirGradient uses the Sensirion SGP41.

  I’ve used the Kaiterra Laser Egg for detecting VOCs previously, as well as some off-brand handheld device off Amazon. They mostly agree.

  - **ahaucnx** · [2024-05-15 04:54 UTC](https://news.ycombinator.com/item?id=40363237)
    I believe that the Sensirion SGP41 is the slightly better VOC sensor and it also gives an NOx signal that can be useful: ^c40363237

    "The testing results show that the SGP41 has a better response for 9/10 tested VOC solvents and can detect the level of NOx gases, which is a unique and important feature for hazardous and toxic gas detection and alarm systems."\[1\]

    In general measuring VOCs is quite challenging and people really need to understand these type of sensors. A couple of months ago, I wrote a whole blog post about these issues. \[2\].

    \[1\] [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9654358/](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9654358/>)

    \[2\] [https://www.airgradient.com/blog/tvoc-explainer/](<https://www.airgradient.com/blog/tvoc-explainer/>)

    - **juntloop** · [2024-05-15 05:22 UTC](https://news.ycombinator.com/item?id=40363361)
      SGP41 requires an external humidity sensor for its algorithm. BME688 has an internal humidity sensor. ^c40363361

      SGP41 algorithm is open source, BME is closed source, requires you to link a binary during compilation.

      In theory BME can sample additional gas profiles (programmable heater waveform), in practice it's useless.

      I agree that the SGP41 has better sensitivity, and also faster response and better stability.

      - **retSava** · [2024-05-15 11:35 UTC](https://news.ycombinator.com/item?id=40365519)
        That's been my experience with the BME688 too. Bosch likes to pitch this as being able to detect many various things, then leaves it up to the customer to experiment with heater profiles and machine learning to reach said goal. ^c40365519

        The results I've seen for methane is discouraging, to say the least. Now moving to a NDIR sensor. A completely different thing, I know. Guess I was under a spell, it sounded too good to be true - a BOM cost reduction of 20x, and it was. I can go on and on about this one and the driverlib for it, but I've spent enough energy already.

  - **dzhiurgis** · [2024-05-15 07:18 UTC](https://news.ycombinator.com/item?id=40364014)
    What are you trying to do with VOC monitoring? One of my devices have it but I don’t pay attention. ^c40364014

    - **jumploops** · [2024-05-15 08:02 UTC](https://news.ycombinator.com/item?id=40364266)
      We were getting headaches but didn't know why. Turns out the building was recently remodeled, and the VOC sensor helped us root cause the air quality (we were opening windows to get rid of the flooring smell, but then inhaling toxic roof off-gases instead). ^c40364266

    - **poulpy123** · [2024-05-15 13:10 UTC](https://news.ycombinator.com/item?id=40366440)
      It's interesting if you have a source of  unhealthy VOC that you want the monitor. ^c40366440

- **KRAKRISMOTT** · [2024-05-15 05:11 UTC](https://news.ycombinator.com/item?id=40363299)
  The biggest missing feature is a radon monitor. Currently only Airthings offers it. ^c40363299

  - **poulpy123** · [2024-05-15 09:47 UTC](https://news.ycombinator.com/item?id=40364877)
    I had a look at radon sensors recently and they look quite expensive, difficult to add in a 150-200€ monitor ^c40364877

    - **defrost** · [2024-05-15 10:01 UTC](https://news.ycombinator.com/item?id=40364959)
      Radon sensors *might* be dedicated and expensive, or they *might* just count clicks in the gamma spectrum. ^c40364959

      If you have a basement \| enclosed space in a granite rich area then you'll probably get radon gas pooling in that space *unless* it's sealed and\|or vented.

      You're *unlikely* to have an unspecified gamma source (lump of uranium, limp of potassium, lump of thorium) in your basement so ...

      A *generic* geiger counter (click counter) should give a reading (low) outside your space in the open air, and another reading (higher) inside that space .. that can vary with time (as gas is expressed, pools, vented).

      That generic click difference is almost entirely radon .. you'll be taking readings within 20 feet, one inside, anothe outside.

      So you can easily get away with a cheap geiger counter to indicate if there's an issue .. if there is, you'll need to either:

      \* minise time spent inside space, and\|or

      \* vent the space (fan blower, + pipe to outside)

      \* accept a cancer risk \~ a pack a day smoking *if* you use space as an office.

      Source: *a couple of decades geophysical surveying making radiometric maps of entire countries*.

      - **poulpy123** · [2024-05-15 11:21 UTC](https://news.ycombinator.com/item?id=40365391)
        \> they might just count clicks in the gamma spectrum. ^c40365391

        but radon is emitting alpha particles ?

        - **defrost** · [2024-05-15 11:33 UTC](https://news.ycombinator.com/item?id=40365510)
          and gamma rays (several energy peaks) and decaying into polonium, bismuth and lead. ^c40365510

          These are *all* indicators.

          *Identifying* radon is either a stochastic puzzle or a job for a mass spectrometer.

          If you're concerned about radon the best bet is to either move or to mitigate

          [https://en.wikipedia.org/wiki/Radon\#Testing\_and\_mitigation](<https://en.wikipedia.org/wiki/Radon#Testing_and_mitigation>)

          it's a heavy gas that "oozes" out of granites and settles in low areas .. valleys until a breeze comes through or basements until pumped out ( floor level extractor fan \| gas sump ).

- **scionthefly** · [2024-05-15 17:01 UTC](https://news.ycombinator.com/item?id=40369538)
  I bought an Extech CO210 CO2/Temp/Humidity datalogger about ten years ago. It's been a very useful, reliable device. Maybe there are newer models or different manufacturers (e.g. the Aranet 4) that make ones that would work for your application case. I didn't just want the readout, I wanted datalogging, and back then it was way more expensive to do datalogging than to just have a readout. ^c40369538

- **alfozan** · [2024-05-15 06:43 UTC](https://news.ycombinator.com/item?id=40363809)
  I've been using the Awair air quality monitor ([https://getawair.com](<https://getawair.com>)) for over 5 years and I'm really happy with it. I've built a simple dashboard to visualize the readings: [https://github.com/alfozan/Air-Quality-Dashboard](<https://github.com/alfozan/Air-Quality-Dashboard>) ^c40363809

- **sanjay\_0508** · [2024-05-15 09:54 UTC](https://news.ycombinator.com/item?id=40364914)
  [flagged] ^c40364914

  \[dead\]

