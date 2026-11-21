# [Low Cost CO2 Sensors Comparison: Photo-Acoustic vs. NDIR](https://news.ycombinator.com/item?id=41620955)

Article: [https://www.airgradient.com/blog/co2-sensors-photo-acoustic-vs-ndir-updated/](<https://www.airgradient.com/blog/co2-sensors-photo-acoustic-vs-ndir-updated/>)

todsacerdoti · 2024-09-22 23:24 UTC · 76 reported comments · archived 2026-11-08 13:40 UTC
Observation: 2026-11-08 13:40 UTC → 2026-11-08 13:40 UTC

## Comments

- **matznerd** · [2024-09-23 01:48 UTC](https://news.ycombinator.com/item?id=41621685)
  Not sure what people are interested in CO2 sensors for, but I use them as a proxy for ventilation in indoor spaces, which is then a proxy for covid risk. ^c41621685

  It won't tell you if the air is being filtered (need MERV13 or better), but a lot of places for efficiency and/or due to old HVAC equipment don't bring in fresh air, which increases the risk in a more confined and/or crowded space.

  Also, some places like airplanes, which have HEPA filters and have 10-20 air changes per hour (ACH), don't run those systems at full power or bring in outside air at fast enough rate until airborne, so PPM can't build up to 2000 ppm vs the \~420 ambient outdoor CO2 level and approx 800 "good" indoor air rate.

  I use an Aranet4 device, which uses 2 AA batteries that last like a year.

  - **scosman** · [2024-09-23 13:00 UTC](https://news.ycombinator.com/item?id=41625597)
    CO2 can also reduce cognitive capacity. It's useful to monitor, other than just being a proxy for air quality. ^c41625597

    Sidenote: it's a fun project to built your own. You can buy the good sensor from this test (Senseair S8) for about \$20 from AliExpress. Add a ESP32, a case, and EspHome.io software, and have a high quality sensor for \<\$30. Same quality as the Aranet4 device you mention, at about a tenth the price. They also use a senseair sensor with the same accuracy rating, but slightly higher priced one designed for long term use on a battery.

    - **aftbit** · [2024-09-23 14:02 UTC](https://news.ycombinator.com/item?id=41626204)
      I tried this but somehow my sensor got stuck at 500 ppm and never recovered. My Airgradient devices have not yet suffered from this problem. ^c41626204

  - **left-struck** · [2024-09-23 02:18 UTC](https://news.ycombinator.com/item?id=41621851)
    As you said it won’t tell you if the air is being filtered. I think you’re better off measuring the small particle content of air if your concern is viruses, or both. ^c41621851

    - **lucubratory** · [2024-09-23 03:26 UTC](https://news.ycombinator.com/item?id=41622169)
      Devices like the Aranet4 are mainly useful for telling you how well ventilated a space is relative to how many people are breathing into it, which is a very good proxy for viral load and viral risk. It's pretty much only in spaces with high quality air filtration (aka high CADR for cleaning an enclosed environment) or significant far-UVC protective measures that the proxy relationship breaks down, and the breakdown will always be an overestimation of risk from the CO2 monitor, never an underestimation. For those reasons it's a very useful tool to have to put an upper bound on the risk of the space you're in and help you make informed decisions about whether you can e.g. hold your breath and take a drink under far-UVC cover or not. ^c41622169

      PM2.5 sensors or other things like what you're thinking of do have their place, but they also have a bunch of other issues - they'll be detecting VOCs, brake and tire dust that's fine enough, any aerosol whether it's coming out of a mammal or not. I think it's inaccurate to say they're just a generically better solution than CO2 monitors for viral risk.

      - **rallison** · [2024-09-23 04:02 UTC](https://news.ycombinator.com/item?id=41622295)
        Exactly. CO2 is an imperfect proxy, but it's a pretty decent one. And, even for spaces that have high quality air filtration (e.g. a strong commercial central air system with good HEPA/MERV filters), the CO2 measurement can also tell you if the system is configured with a good recirculated to outdoor air ratio (residential systems usually have no such thing, unfortunately). ^c41622295

        But yeah, as you said, the best aspect of a CO2 monitor is that it gives you a useful upper bound for the general respiratory virus risk in a space.

  - **space\_oddity** · [2024-09-23 08:41 UTC](https://news.ycombinator.com/item?id=41623813)
    The Aranet4 sounds like a solid choice for monitoring ^c41623813

    - **telcal** · [2024-09-24 02:35 UTC](https://news.ycombinator.com/item?id=41632612)
      I'd say the AirGradient products are a better choice since they includes VOC, PM and NOx sensors (Aranet4 doesn't), are open source, and Achim Haug who did this study is really dedicated to air quality. ^c41632612

  - **tomaskafka** · [2024-09-24 08:18 UTC](https://news.ycombinator.com/item?id=41634337)
    Aranet is pretty expensive for what it does, there are great NDIR based monitors on aliexpress for much less. ^c41634337

  - **mapt** · [2024-09-23 11:38 UTC](https://news.ycombinator.com/item?id=41624985)
    I'm not sure I believe the extremely dramatic claims made about airplane HEPA filters, having seen normal HEPA air purifiers and various dust collection systems, how much space they take, what they cost, and how loud they are, and seen airplanes & the cost-cutting they undertake. ^c41624985

    What I heard in 2020, here as in many other areas, appeared to be a combination of lies, exaggerations, and wishful thinking that would allow the jet-set to justify not changing anything they were doing.

    Based on chained analysis of R number (some grains of salt there), later variants of COVID were more contagious than measles or just about anything else we deal with using dramatically more intense precautions.  There was a lot of cope.

    - **avianlyric** · [2024-09-23 13:05 UTC](https://news.ycombinator.com/item?id=41625641)
      In modern planes, advanced HVAC systems end up being cheaper than older air management methods. ^c41625641

      The old way of keeping a planes air “fresh” was to bleed air from the compression stage of each engine, because the air there will be at high pressure, and also reasonably high temperature (outdoor air temps at cruising altitude is -40C to -57C). You then just inject that air into the cabin, and let the old air bleed out.

      But it turns out, pulling air like that from the compression stage of a turbine has a material impact on efficiency (you badly disrupt the airflow through the engine), and engine efficiency is so high these days, that removing those air bleeds, and replacing them with sophisticated HVAC systems with dedicated compressors, heaters and filters ends up being cheaper, at least from a total cost of ownership perspective. As a consequence, modern planes from the past 5-10 years have had some pretty capable air management systems. Of course there’s a much larger stock of older planes out there, which you’re more likely to be travelling on. But the claims regarding plane HVAC aren’t crazy when looking at modern planes.

      - **mapt** · [2024-09-23 15:09 UTC](https://news.ycombinator.com/item?id=41627003)
        The dubious claims made were about how aggressive and effective internal filtration was, not about actual fresh air circulation. ^c41627003

- **space\_oddity** · [2024-09-23 08:40 UTC](https://news.ycombinator.com/item?id=41623809)
  Air quality becomes an increasing concern for me. This happened after I went on vacation to the mountains. It seems I hadn't been to the mountains for a very long time and had forgotten how wonderful the air is there. I felt my condition improve. After that, I started thinking about the air quality in my home ^c41623809

  - **monkburger** · [2024-09-23 11:20 UTC](https://news.ycombinator.com/item?id=41624844)
    All homes need fresh air ventilation systems - at least here, all new homes are required by code to have it. ^c41624844

    ERV / HRV or a static one that goes into your air handler.

    Personally, ERV is the way to go. Panasonic makes one that is perfect for the ceilings, and there's Nutone, etc.

    - **Abekkus** · [2024-09-23 12:47 UTC](https://news.ycombinator.com/item?id=41625471)
      If you're in a mostly humid area, like half of the US, It's better money to get a simple ventilation fan and dehumidifier.  ERVs won't work half as well for 3-4x price. ^c41625471

      I'm still not buying the claims made about ERV efficiency. As a passive device, they could only ever remove half of the excess moisture form the fresh air, and there's no way they're approaching that performance when the air passes through the diffuser in a quarter second.

      - **jwong\_** · [2024-09-23 20:01 UTC](https://news.ycombinator.com/item?id=41629873)
        What’s the setup here with a ventilation fan? ^c41629873

        Do you just run a ventilation fan in reverse? And suck outdoor air inside?

        I will sometimes crack a window and leave the ventilation fan on, then later run a dehumidifier. But it’s a lot of steps, and it would be nice to automate some of the steps.

        - **Abekkus** · [2024-09-24 04:18 UTC](https://news.ycombinator.com/item?id=41633079)
          I, actually run a 6 inch snorkel out from the basement with fine metal mesh clamped onto the intake.  Reduces to 4 inch through the wall, then through a filter box, then through a 200cfm fan.  You want 15cfm per person in the building to flush enough CO2.  After the two filters, a 200 cfm fan will not be pulling what it’s rated for.  You can either use a bathroom exhaust fan in reverse, or you can get quiet enough fans from “indoor gardening companies”.  The dehumidifier is standard, nothing fancy. ^c41633079

- **fotta** · [2024-09-23 00:03 UTC](https://news.ycombinator.com/item?id=41621153)
  I have an SCD30 which is a dual-channel NDIR sensor and am pretty happy with it. Once a year I’ll take it outside to recalibrate it and it’s never drifted more than a few ppm. I make sure to turn off the auto-calibration and manually calibrate it because auto-calibration can lead to weird behavior if you don’t know what it’s doing (it re-baselines the lowest observed ppm in a time window as 400ppm). ^c41621153

  - **kayson** · [2024-09-23 00:06 UTC](https://news.ycombinator.com/item?id=41621170)
    FWIW, Sensirion's AEs told me they have empirical data showing that CO2 drops to outdoor levels at least once a week even in closed environments. Based on that they recommend using the auto calibration. ^c41621170

    Anecdotally, I see my CO2 levels hover around 600ppm inside even over night.

    - **fotta** · [2024-09-23 00:09 UTC](https://news.ycombinator.com/item?id=41621186)
      I think that really depends on the environment it’s deployed in. I used to live in a poorly ventilated former warehouse apartment with a mini split for HVAC and at night my levels were around 700. I live in a much better ventilated apartment now and it’s made a noticeable difference in QoL. ^c41621186

      - **\_zoltan\_** · [2024-09-23 05:39 UTC](https://news.ycombinator.com/item?id=41622651)
        700 is great, I see spikes up to 5000 in one of our rooms. ^c41622651

      - **ctenb** · [2024-09-23 06:19 UTC](https://news.ycombinator.com/item?id=41622828)
        levels in the range 400-1000 are considered good quality ^c41622828

      - **dzhiurgis** · [2024-09-23 01:29 UTC](https://news.ycombinator.com/item?id=41621588)
        700 is pretty good, what are you on about? ^c41621588

        - **atoav** · [2024-09-23 06:20 UTC](https://news.ycombinator.com/item?id=41622837)
          If your sensor recalibratws to a baseline of 400 each day and you have a baseline of 700 that is a drift of 300 ppm per day or ca 100 000 ppm per year. ^c41622837

          You see why this is a problem?

          - **bialpio** · [2024-09-23 06:41 UTC](https://news.ycombinator.com/item?id=41622989)
            It's not going to drift by 300ppm per day - it'll pick the lowest value it saw and assume it was 400ppm. If that happens to be 700ppm every day, then it'll be wrong by 300ppm every day. ^c41622989

    - **ahaucnx** · [2024-09-23 02:12 UTC](https://news.ycombinator.com/item?id=41621826)
      There are many cases where the level does not drop to ambient levels, e.g. offices in basements, low-energy houses etc. ^c41621826

      We even saw schools where the classrooms were not able to drop to ambient levels over the whole unoccupied weekend because the ppm levels on Friday afternoon were beyond 3000ppm.

      The automatic baseline calibration period of some of the NDIR CO2 sensors can actually be adjusted through the software. I believe the Aranet allows that and also we do have that feature on the AirGradient dashboard. So you can switch it to a much longer period or switch it off completely.

      - **pixelfarmer** · [2024-09-23 06:20 UTC](https://news.ycombinator.com/item?id=41622842)
        It always comes down to how well you can ventilate. If you can open windows / doors to different sides of a house / building there is usually some natural air flow, and the stronger it is, the faster it will bring CO2 levels down. In the apartment here it can be less than 5 minutes to have CO2 levels to ambient levels, but it also takes longer if the air is "standing" even outside. For that you will need active ventilation then, clearly, same for having windows to the same side of the building only etc. ^c41622842

        There is also another thing: In multi-tenant buildings you may have others airing out their apartments which means you will not get ambient levels, but elevated ones due to added CO2 from the other apartment(s). For example, I see \>500 ppm CO2 then. Also, even the ambient levels are not always the same; I have seen values between 416 and 432 ppm depending on the day, wind, and other factors (living in a larger city).

- **lucubratory** · [2024-09-23 03:14 UTC](https://news.ycombinator.com/item?id=41622120)
  I strongly recommend the Aranet4 Home for personal/home use. Very accurate, very long-lasting, tells you other things like humidity etc, and only 1-2 hundred dollars when we bought it (may be more expensive now, been a couple years of inflation). ^c41622120

  - **SparkyMcUnicorn** · [2024-09-23 03:31 UTC](https://news.ycombinator.com/item?id=41622182)
    I chose the AirGradient\[0\] One. It's slightly more expensive than the aranet4, but has more sensors. It's open source, reports CO2, PM10, PM2.5, temperature, humidity, and more I'm probably forgetting offhand. Loaded it with the esphome firmware, so Home assistant integration is seamless. ^c41622182

    And since it's open source, when a sensor inevitably wears out in a couple years (like the PMS5003), I can just replace the sensor instead of of buying a whole new unit.

    Highly recommend it.

    \[0\] [https://www.airgradient.com/](<https://www.airgradient.com/>)

    Edit: I completely missed that AirGradient blog article

    - **lucubratory** · [2024-09-23 04:05 UTC](https://news.ycombinator.com/item?id=41622310)
      That sounds fantastic, I really love open source stuff. ^c41622310

  - **jval43** · [2024-09-23 06:14 UTC](https://news.ycombinator.com/item?id=41622792)
    It's crazy how optimized the Aranet 4 Home is. It runs on AA batteries for a whole year, no need to plug it in. ^c41622792

    That's unique in the space, and a case where e-ink makes a real difference. And very convenient in practice.

    - **teekert** · [2024-09-23 14:06 UTC](https://news.ycombinator.com/item?id=41626269)
      Also love my aranet4. Would be killer if there was a zigbee version to couple to home assistant. I’d put one in every room if that was the case. ^c41626269

      - **throwaranay4933** · [2024-09-23 17:04 UTC](https://news.ycombinator.com/item?id=41628205)
        If your Home Assistant has Bluetooth, and the Aranet4 has the "smart home" integration enabled (via the app settings), then HA will pick up ambient broadcasts of the sensors out of the box. You don't need Zigbee or explicit pairing. ^c41628205

        - **teekert** · [2024-09-23 19:42 UTC](https://news.ycombinator.com/item?id=41629735)
          But I don’t have a large enough BT “network”, my zigbee networks spans my house (and entire premise). ^c41629735

  - **ctenb** · [2024-09-23 06:17 UTC](https://news.ycombinator.com/item?id=41622817)
    I bought one a year ago for 200 bucks. I'm still happy with the purchase, and I haven't had to change the batteries yet. ^c41622817

- **breput** · [2024-09-22 23:49 UTC](https://news.ycombinator.com/item?id=41621089)
  I've used both the SenseAir S8 and Sensirion SCD41 sensors, and the SenseAir is clearly my favorite. ^c41621089

  The SCD41 seems to require a lot more manual calibration while the S8 is very stable - maybe once every 3 months or so, I'll see it reporting \~380 ppm in fresh air (which is actually within spec).

  The venerable MH-Z19 is probably my second favorite sensor, ahead of the SCD40-series.

  - **ahaucnx** · [2024-09-23 02:03 UTC](https://news.ycombinator.com/item?id=41621770)
    The MH-Z19 is similar from the performance of the S8 but we do see more noise in the readings and the MH-Z19 also seem to have less life time. We see some of them dying after around 5 years whereas the S8 has a ten year warranty and so far have been rock solid for us. ^c41621770

    - **imjonse** · [2024-09-23 04:48 UTC](https://news.ycombinator.com/item?id=41622460)
      I see all these three (SD40/41, MH-Z19 and S8) on Aliexpress, but in yesterday's discussion on the sibling post it was said that the SD40 is likely a fake since Switzerland based Sensirion do not distribute there. Do you have a blog about sourcing these sensors and those needed for other air measurements? The cheaper options on AliExpress look attractive for someone willing to try a small hobby project but if there's a risk of getting malfunctioning fakes that option may need to be scratched. Thank you ^c41622460

      - **ius** · [2024-09-23 07:06 UTC](https://news.ycombinator.com/item?id=41623171)
        I'm not convinced the mere fact that AliExpress sellers are not Sensirion distributors is sufficient to assume these sensors are counterfeit. Obviously there's precedence - buy a 'stm32' and you'll likely receive a counterfeit chip, but that's because these chips have been cloned by many. The Sensirion SCD40 is fairly niche and has an odd form factor - doesn't seem trivial to produce a convincing clone. ^c41623171

        AliExpress sellers sell these at €14,99/1 whereas DigiKey is at €16,38/600 (excl. VAT). Price seems 'right' to me.

        I have been looking for a comparison between sensors sourced from AliExpress and a reputable distributor, but sadly couldn't find any.

        Anyway, I did get a few of these sensors off AliExpress for my personal projects. They definitely measure CO₂ (not eCO₂) - the only issues I've been having with them is the default calibration being off and a struggle to get the temperature reporting right (the sensor suffers from self-heating).

        - **bubulina** · [2024-10-01 20:55 UTC](https://news.ycombinator.com/item?id=41714049)
          I ordered one SCD40 and two SCD41 sensor modules from AliExpress and I received them today. ^c41714049

          According to [https://sensirion.com/media/documents/48C4B7FB/64C134E7/Sens...](<https://sensirion.com/media/documents/48C4B7FB/64C134E7/Sensirion_SCD4x_Datasheet.pdf>) (page 24) "All SCD4x sensors include a laser marking on the sidewall of the sensor cap. The laser marking contains the product variant (i.e., SCD40 or SCD41) and the product serial number within a data matrix".

          The SCD40 sensor that I received has the laser marking on the sidewall of the sensor cap, but none of the two SCD41 sensors has it.

          The price was \~€14 for SCD40 and \~€16 for SDC41. On Digikey they are currently €16.26 for one SCD40 (in a batch of 600) and €21.10 for one SCD41 (also in a batch of 600).

          What do you think is the lilelihood the SDC41s I received are fake?

    - **breput** · [2024-09-23 03:45 UTC](https://news.ycombinator.com/item?id=41622227)
      That is good confirmation.  I bought a MH-Z19 as a pandemic project so I might be approaching that timeframe. ^c41622227

- **vegetablepotpie** · [2024-09-23 13:45 UTC](https://news.ycombinator.com/item?id=41626020)
  One of the things I’ve been wanting to do is make a batch of SAO style circuit boards with a CO2 sensor hooked up to a 7-segment display and hand them out to people at conferences. This would give people a way to witness ambient CO2 levels first hand, and how much it’s increasing. I’d have a QR code on the back, write something like “getting hot enough for you?” and have it link to non-profits doing work on climate change. ^c41626020

  The idea would be to build a batch of a few hundred of these. If co2 sensors get down to the \$5 price point, this idea starts to get feasible. Right now sensors are getting cheap, which is impressive, but not cheap enough yet to hand them out to strangers for free.

- **amoshebb** · [2024-09-23 00:32 UTC](https://news.ycombinator.com/item?id=41621312)
  I’ve never heard of any of these. What’s going on in low cost oxygen sensors? What should I google? I can only find \$100+ galvanic sensors that need to be replaced after a few dozen months ^c41621312

  - **brok3nmachine** · [2024-09-23 07:02 UTC](https://news.ycombinator.com/item?id=41623139)
    The cheapest 02 sensors that I know of are around \$50 each, and have a shelf life of 1-2 years. Average price for a decent sensor is closer to \$90. And digital solid state O2 sensors go for \$400+. ^c41623139

    \*Edit\*: google dive gear express O2 sensors to see these.

    I use them for technical scuba diving. In particular with a rebreather, which is capable of mixing oxygen with other gases such as nitrogen and helium. And as the gas is recirculated CO2 is scrubbed  away.

    CO2 sensors are also available for rebreathers but are not always reliable (same for O2 sensors, so a minimum of 3 are used). The human body is actually quite sensitive to CO2, and it determines our breathing rate. So there are ways to know if you're likely being exposed to elevated CO2 levels by being aware of your breathing rate, paranoia, etc.

    - **amoshebb** · [2024-09-23 17:29 UTC](https://news.ycombinator.com/item?id=41628464)
      Yes, these are the galvanic ones I was rounding up to \$100. I was curious if some other technology or sensing technique I wasn't aware of existed that was less expensive, more reliable, or lasted longer. ^c41628464

    - **joseda-hg** · [2024-09-23 18:19 UTC](https://news.ycombinator.com/item?id=41628972)
      Completely off-topic, but do you happen to use text-to-speech for comments? ^c41628972

      The usage of 02 and O2 interchangeably piqued my interest; it seems like a way for such an error to occur.

  - **unknown** · [2024-09-23 06:26 UTC](https://news.ycombinator.com/item?id=41622877)
    [deleted] ^c41622877

  - **para\_parolu** · [2024-09-23 01:54 UTC](https://news.ycombinator.com/item?id=41621724)
    This. There are plenty of co2 but what I really need is to measure o2 level (plus co presence). ^c41621724

- **tomaskafka** · [2024-09-24 08:26 UTC](https://news.ycombinator.com/item?id=41634389)
  To everyone considering \$150 NDIR sensors to be cheap: Look up quingping co2 monitor on Aliexpress, the white one with BW screen. Goes for around \$70, is NDIR based, and I absolutely recommend it after having it for more than year. ^c41634389

  Can be usb c powered, or last over a month on battery and then sync the measurements to the cloud, if you want to leave it somewhere, eg to monitor a school, or some remote house.

- **8f2ab37a-ed6c** · [2024-09-23 00:51 UTC](https://news.ycombinator.com/item?id=41621410)
  Is there a consumer model that you would recommend that one can use at home? ^c41621410

  - **caseyy** · [2024-09-23 04:27 UTC](https://news.ycombinator.com/item?id=41622386)
    The cheapest one that is not eCO2 (estimated) will do the job of telling you when you’ve not ventilated enough just fine. No need to spend hundreds to thousands on lab-grade tech. ^c41622386

    \+- 50ppm, or even 100 or 200 is nothing. You will mainly care if the ppm is around 500 or around 1000-2000 (depending on preference).

    The devices that have alarms are quite nice. Leave them on a desk and they’ll tell you when to open the window. The ergonomics of how you’ll use it are maybe more important than accuracy when it’s \<200ppm off.

  - **domoritz** · [2024-09-23 01:40 UTC](https://news.ycombinator.com/item?id=41621653)
    Aiegradient is great and they make indoor and outdoor monitors. Fully open source. They are the authors of this article and to a lot of research and advocacy which is great. ^c41621653

  - **danw1979** · [2024-09-23 12:19 UTC](https://news.ycombinator.com/item?id=41625297)
    TFA Dostmann make an “Airco2ntrol mini” which is USB powered (and you can pull the readings over USB too) and has a nice little red-amber-green light system on the front (as well as the LCD) for easy reference.  It’s about £85.  It has a dual NDIR sensor (not sure which one exactly) which the article says are usually the most accurate type of consumer-grade sensors. ^c41625297

    I’ve had mine for years, very pleased with it… just sits on my desk and lets me know when it’s time to open the windows.

  - **rallison** · [2024-09-23 01:16 UTC](https://news.ycombinator.com/item?id=41621517)
    For NDIR sensors, the Aranet4 Home is an often recommended one. I have a couple, and they are great little units. A number of scientists recommended them during the heart of covid as a proxy for covid risk in indoor spaces (obviously, an imperfect proxy, but since there are no cheap, portable devices to measure viral concentrations in the air, you work with what you've got). ^c41621517

  - **MetaWhirledPeas** · [2024-09-23 01:36 UTC](https://news.ycombinator.com/item?id=41621627)
    I use the Airthings (the \$300 one). It detects more than just CO2, has an e-ink display, and has a decent app. ^c41621627

  - **tomaskafka** · [2024-09-24 08:22 UTC](https://news.ycombinator.com/item?id=41634370)
    Yes. Look up quingping co2 monitor on Aliexpress, the white one with BW screen. It’s NDIR based, and can last a month on battery and then sync the measurements to the cloud, if you want to leave it somewhere. Around \$70. ^c41634370

  - **an\_account** · [2024-09-23 00:54 UTC](https://news.ycombinator.com/item?id=41621420)
    When I looked a few years ago the Await element was best consumer grade one on the market at a good price. I’ve been happy with it so far. ^c41621420

  - **dzhiurgis** · [2024-09-23 01:31 UTC](https://news.ycombinator.com/item?id=41621601)
    I like my qingping - works with both - homekit and home assistant. ^c41621601

- **thousand\_nights** · [2024-09-23 00:45 UTC](https://news.ycombinator.com/item?id=41621377)
  a lot of these seem to be making the front page lately, i assume these are pointless if you regularly keep the windows open and air out the house? ^c41621377

  - **llm\_trw** · [2024-09-23 00:49 UTC](https://news.ycombinator.com/item?id=41621399)
    In a small enough unventilated room you can fill it with enough co2 to make it unpleasant to be in with an hour. E.g. a study in the usual suburban house. ^c41621399

    - **rallison** · [2024-09-23 01:12 UTC](https://news.ycombinator.com/item?id=41621498)
      Yep. Even if the building as a whole is generally well ventilated, particular spaces in a building can still build up CO2 pretty quickly. It's actually quite dramatic to see the rise in chart form at times. ^c41621498

      These sensors are really nice to help validate ventilation anywhere.

      - **twothamendment** · [2024-09-23 01:28 UTC](https://news.ycombinator.com/item?id=41621579)
        Yeah, location matters a ton. I have 2 Awair Elements and we ran them in different places until we knew what "normal" looked like, then move them on. ^c41621579

        Because of what I saw in my house we switched from a gas stove/oven to electric induction, installed an air exchanger and set our central air/heat to recirculate more often (only important for us during spring and fall when we aren't heating or cooling much).

        I don't like noise when sleeping, so I liked the bedroom door shut. CO2 gets way too high, so I switched to using an earplug and leaving the door open more.

        It is so nice to have the data, make informed choices and see measurable results.

        - **rallison** · [2024-09-23 03:52 UTC](https://news.ycombinator.com/item?id=41622253)
          Yep, I also run central air in fan only mode much more often now. Since I'm in coastal California, I don't need to run heating/cooling for much of the year, so previously that meant central air was rarely on. ^c41622253

          Now, I'll run it fairly often for the recirculation. And, since my house is old and leaky, aside from evening out levels, it no doubt results in more indoor:outdoor air exchange too. That alone made a massive difference at night, since I will usually have the bedroom door closed.

          And, while I haven't switched the range over to induction yet (it's on the list to eventually do), I did get a portable induction burner that I use fairly often instead of the gas range. Induction is pretty amazing, so I look forward to eventually going all the way.

  - **kupfer** · [2024-09-23 07:47 UTC](https://news.ycombinator.com/item?id=41623438)
    Sure if you are already airing every hour you don't need it. Then for me it was surprising how often I have to air and for how long (also depends on draft and temperature difference). Once you take into account the more harmful particulate matter coming in from outside, it's about finding a  compromise, and without measuring you are tapping in the dark. But in the end people get old without all that stuff. ^c41623438

  - **breput** · [2024-09-23 01:45 UTC](https://news.ycombinator.com/item?id=41621664)
    Let's be honest - the AirGradiant people/person are submitting these. ^c41621664

    Which is fine - they seem like a good company with a strong open source commitment, but they do go a little overboard on HN submissions.

    - **ahaucnx** · [2024-09-23 02:05 UTC](https://news.ycombinator.com/item?id=41621785)
      Achim, founder of AirGradient here. Just want to clarify that this submit was not done by me or our team. ^c41621785

      - **caseyy** · [2024-09-23 04:29 UTC](https://news.ycombinator.com/item?id=41622394)
        Maybe not this one but look at your other submissions :) ^c41622394

  - **imhoguy** · [2024-09-23 07:56 UTC](https://news.ycombinator.com/item?id=41623492)
    Winter is coming, some won't keep windows open regularly. ^c41623492

- **tmulc** · [2024-09-23 00:47 UTC](https://news.ycombinator.com/item?id=41621386)
  Welp, I just ordered \$1500 worth of the Cisco ones, so I hope they are the right type. ^c41621386

- **transcriptase** · [2024-09-23 05:22 UTC](https://news.ycombinator.com/item?id=41622591)
  Nitpicky but isn’t R correlation and R\^2 coefficient of determination? ^c41622591

- **aulin** · [2024-09-23 05:25 UTC](https://news.ycombinator.com/item?id=41622597)
  What do you use these for? for indoor home use I cannot see the point. We have plenty of biochemical sensors in our body telling you when it's time to ventilate the room... ^c41622597

  I mean, I can understand CO, maybe Radon, but CO2 really seems pointless and only driven by the modern green trends.

  - **zik** · [2024-09-23 05:54 UTC](https://news.ycombinator.com/item?id=41622701)
    Higher levels of CO2 impair cognitive function \[1\]. ^c41622701

    In fact there's no floor - even small increases in CO2 have small but measurable effects.

    \[1\] [https://www.hsph.harvard.edu/healthybuildings/2021/09/09/imp...](<https://www.hsph.harvard.edu/healthybuildings/2021/09/09/impacts-of-indoor-air-quality-on-cognitive-function/>)

    - **aulin** · [2024-09-23 06:18 UTC](https://news.ycombinator.com/item?id=41622824)
      Sure, point is we as humans are already equiped with efficient ways to detect it. Only home use I can imagine is to drive some ventilation automation. ^c41622824

  - **Aachen** · [2024-09-23 17:20 UTC](https://news.ycombinator.com/item?id=41628382)
    What sensor in my body detects CO2? ^c41628382

    Unless you mean headache-inducing levels of CO2 which, per my actual sensor, is upwards of 3000 because at that level I still didn't notice anything. The air feels warmer, but that's attributable to me breathing in a small and enclosed space

    Genuinely curious if there's something in our bodies that has been shown to serve as CO2 detector, or if you just mean "I can smell stale air and why *don't you just* do the same" (which I'm pretty certain relies on proxy factors like dust, mould smells like in a moist cellar, temperature, a combination, and/or perhaps other stuff that didn't come to mind)

- **glub103011** · [2024-09-23 02:49 UTC](https://news.ycombinator.com/item?id=41622020)
  [flagged] ^c41622020

  \[dead\]

- **unknown** · [2024-09-23 13:13 UTC](https://news.ycombinator.com/item?id=41625709)
  [deleted] ^c41625709

- **Rayaan22** · [2024-09-23 05:01 UTC](https://news.ycombinator.com/item?id=41622514)
  [flagged] ^c41622514

  \[flagged\]

- **bikezen** · [2024-09-22 23:50 UTC](https://news.ycombinator.com/item?id=41621098)
  Repost, [https://news.ycombinator.com/item?id\=41611965](<https://news.ycombinator.com/item?id=41611965>) ^c41621098

  - **tzs** · [2024-09-23 00:28 UTC](https://news.ycombinator.com/item?id=41621289)
    I don't see how it is a repost. That submission was to an article that talks about a new model of photo-acoustic sensor from Infineon. ^c41621289

    This submission is to an article that compares photo-acoustic sensors to NDIR sensors. Its only connection to the earlier submission is that the author of the comparison participated in the discussion of about the new Infineon sensor, updated the comparison article, and linked to it in one of their comments.

    - **dylan604** · [2024-09-23 00:42 UTC](https://news.ycombinator.com/item?id=41621365)
      It's one of the fun things of internet forums in how you can see where someone gets nerd sniped but is able to bring back something from their trip down the rabbit hole. ^c41621365

