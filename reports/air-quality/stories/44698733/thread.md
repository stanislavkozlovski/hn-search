# [Smallest particulate matter air quality sensor for ultra-compact IoT devices](https://news.ycombinator.com/item?id=44698733)

Article: [https://www.bosch-sensortec.com/news/worlds-smallest-particulate-matter-sensor-bmv080.html](<https://www.bosch-sensortec.com/news/worlds-smallest-particulate-matter-sensor-bmv080.html>)

Liftyee · 2025-07-27 03:34 UTC · 54 reported comments · archived 2026-11-08 13:56 UTC
Observation: 2026-11-08 13:56 UTC → 2026-11-08 13:56 UTC

## Comments

- **zevon** · [2025-07-27 07:05 UTC](https://news.ycombinator.com/item?id=44699413)
  Does anybody know how they actually do it without a fan and a defined volume around it? The marketing fluff says "It applies sophisticated algorithms to measure the PM2.5 concentration directly in free space, without requiring a fan", so I assume the main difference to traditional PM sensors is the software? ^c44699413

  - **dist-epoch** · [2025-07-27 07:28 UTC](https://news.ycombinator.com/item?id=44699492)
    They have some tech specs:
    [https://www.bosch-sensortec.com/media/boschsensortec/downloa...](<https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmv080-ds000.pdf>) ^c44699492

    \> Laser light is emitted from the sensor and focused by the sensor lens at approximately 5 mm from the top of the
    sensor’s lens surface.

    \> Particles traveling in free space due to the natural ambient airflow are detected when passing through the laser focal (sensitive) region.

    \> Due to the interaction between particles and light, the light scatters in different directions; a fraction is back-scattered towards the sensor, where the integrated photo-detectors detect it.

    \> The back-scattered signal is processed by unique algorithms (based on particle counts, particle relative velocity, probed air volume during measurement) to derive the particulate matter mass concentration.

    - **trailbits** · [2025-07-27 08:11 UTC](https://news.ycombinator.com/item?id=44699686)
      That's pretty much how all laser particle counters work... except the good ones use a fan and a chamber. Guess we'll have to wait and see how this compares to the reference sensors. ^c44699686

      - **ImaCake** · [2025-07-27 08:16 UTC](https://news.ycombinator.com/item?id=44699707)
        Yep, I suspect this is all marketing fluff and no substance. I see a lot of superlatives but no substantial technical breakthrough here. ^c44699707

        - **hakonjdjohnsen** · [2025-07-27 13:12 UTC](https://news.ycombinator.com/item?id=44701092)
          I think there is at least some plausible interpretation of this that points to more than marketing fluff. ^c44701092

          You want to count particles per volume of air, so conventional sensors use a fan to have a constant volumetric flow and then count particles per second to infer particles per volume.

          The way I interpret the above marketing language is that they use the optical sensor not only to count particles but also to measure the particle movement and infer airflow. So as long as there is some natural movement in the air, they can measure both particle count and volumetric flow, and thus infer particles per volume.

        - **felixg3** · [2025-07-29 14:49 UTC](https://news.ycombinator.com/item?id=44724125)
          This is Bosch and not some random startup. It’s for sure a substantial technical breakthrough of integration, miniaturization, and if coming from Bosch, certainly enterprise and clinical-grade ready. ^c44724125

        - **f1shy** · [2025-07-27 10:13 UTC](https://news.ycombinator.com/item?id=44700196)
          I’m pretty pretty sure it is just marketing ^c44700196

  - **ethan\_smith** · [2025-07-27 11:38 UTC](https://news.ycombinator.com/item?id=44700562)
    These fanless PM sensors typically use thermal convection to create natural airflow across the sensing area, combined with advanced signal processing to compensate for variable flow rates and environmental conditions. ^c44700562

  - **svilches** · [2025-07-28 10:25 UTC](https://news.ycombinator.com/item?id=44709300)
    Insider here: the technology inside is very cool and uses completely novel HW. I asked my PR colleagues for the release of more technical information. ^c44709300

  - **trailbits** · [2025-07-27 07:21 UTC](https://news.ycombinator.com/item?id=44699470)
    Also wonder how the sensor can stay clean without a fan. I suppose mounting upside down would help. Other fanless designs require periodic cleaning. ^c44699470

    - **dist-epoch** · [2025-07-27 07:29 UTC](https://news.ycombinator.com/item?id=44699502)
      The integration picture shows an "optical cover" transparent surface. I guess it's not meant to be used in highly contaminated areas. ^c44699502

  - **TimByte** · [2025-07-27 09:00 UTC](https://news.ycombinator.com/item?id=44699908)
    My guess is they're relying on natural air convection and using a more sensitive optical setup to compensate for the lack of forced airflow ^c44699908

    - **f1shy** · [2025-07-27 10:12 UTC](https://news.ycombinator.com/item?id=44700190)
      They don’t give lots of heat, so convection is negligible. ^c44700190

  - **f1shy** · [2025-07-27 10:11 UTC](https://news.ycombinator.com/item?id=44700187)
    Lying? ^c44700187

    - **rurban** · [2025-07-27 17:57 UTC](https://news.ycombinator.com/item?id=44703168)
      Marketing. Still a good sensor, just not as good as the ones with a fan. We didn't use this one ^c44703168

- **9dev** · [2025-07-27 06:07 UTC](https://news.ycombinator.com/item?id=44699219)
  Waiting for Achim Haug of AirGradient! What’s your thoughts on this? ^c44699219

  - **ahaucnx** · [2025-07-27 09:37 UTC](https://news.ycombinator.com/item?id=44700047)
    Hahah. Thanks for calling me! ^c44700047

    We actually have a sample of the Bosch in our office but haven’t come along to test it yet. Maybe with this call, I will get our team onto it.

    The form factor has pros and cons in my opinion. The size and lower energy consumption definitely opens new applications but the problem is that it needs a clear field of view to do the measurements.

    This could in turn restrict the applicability, eg as a wearable sensor.

    In general I think it’s great to see innovations in the PM sensor field but often minimizations go on costs of accuracy.

    We saw that for example with the Sensirion photo acoustic CO2 SCD4x sensor that is tiny but needs more black box algorithms to compensate for certain environmental conditions that then limits the range of applications.

    - **Liftyee** · [2025-07-27 14:55 UTC](https://news.ycombinator.com/item?id=44701772)
      Interesting points - I wasn't aware of the accuracy tradeoffs with smaller sensors, though as an engineer I should probably have anticipated it. ^c44701772

      I've been messing around with air quality measurement for a while but haven't got anything for the day to day yet.

      Been a long time admirer of the Airgradient project. What are your thoughts on the SEN5x Vs Plantower PM sensors?

      - **ahaucnx** · [2025-07-27 21:09 UTC](https://news.ycombinator.com/item?id=44704715)
        We don’t have enough experience with the SEN5x yet to give an opinion but it’s definitely a good sensor. ^c44704715

        It might be better than the Plantower but on the other hand we know the Plantower really well now after 10s of thousands of units going through our test chamber. This allows us to tweak the Plantower to really good performance.

    - **westurner** · [2025-07-27 15:48 UTC](https://news.ycombinator.com/item?id=44702175)
      I was looking at Radon sensors the other day. FWIU it isn't possible to detect radon with even a PM 2.5 sensor. ^c44702175

      I bought a 10-in-1 air quality sensor with USB-C, and it won't do USB-C PD.

      Batteries for when the power is out make sense.

      Which air quality sensor integrates the most sensors of all?

    - **noahjk** · [2025-07-27 16:10 UTC](https://news.ycombinator.com/item?id=44702315)
      Does the "Everything Presence One" and (hopefully) upcoming Pro model fall under things you review? Any thoughts on how it stacks up for a smart home device? ^c44702315

      - **ahaucnx** · [2025-07-27 18:36 UTC](https://news.ycombinator.com/item?id=44703445)
        Can you please clarify what you mean with “Everything Presence One” and the “Pro Model”? ^c44703445

    - **mrlonglong** · [2025-07-27 12:18 UTC](https://news.ycombinator.com/item?id=44700778)
      Airthings View Plus is £250! ^c44700778

- **pppone** · [2025-07-27 07:40 UTC](https://news.ycombinator.com/item?id=44699551)
  I've been running multiple Sensirion SPS30 PM sensors for years, and I'm honestly amazed how well they've held up.  Particularly with respect to, within their spec'd error, how new/unused SPS30s report similar values to my heavily used ones. ^c44699551

  Curious if there are any maintenance requirements for the bosch sensor.

  - **quickthrowman** · [2025-07-27 13:29 UTC](https://news.ycombinator.com/item?id=44701192)
    Do you actually do anything with the data you collect? ^c44701192

    As someone who manages commercial building automation system installations, I have never understood the obsession that HN has with residential IAQ sensors. The number will go up if you cook, burn a candle, use a hairdryer, or if there’s wildfire smoke outside and you have a ducted HVAC installation with an outdoor air intake.

    In a commercial BAS, IAQ sensors (CO/NO to be more specific) are used to turn on exhaust and make-up air fans to increase the air quality in a space, but in every single thread about IAQ monitoring on HN, nobody ever seems to use the sensor readings to automate their HVAC equipment to do anything. In fact, almost all commercial BAS systems have zero IAQ sensors (especially in offices), the vast majority of them are use for turning on exhaust fans and make-up air units in buildings where cars are driving inside, like a parking ramp or drive-in warehouse.

    I guess my question is, why collect this information and do nothing with it? Maybe you actually do something with it, or you monitor local outdoor air quality as a hobby. I’m asking a more general audience than you specifically.

    Lastly, ensuring your house is positively pressurized by paying a testing and balancing contractor to come over and adjust your HVAC system will do more to keep out particulate matter than measuring it ever will.

    - **Implicated** · [2025-07-27 16:20 UTC](https://news.ycombinator.com/item?id=44702390)
      I use co2 measurements in my home to do just what you're describing here - automate control of a DIY fresh air intake (through a custom built filter box/fan enclosure w/ 5" merv 14 filter). ^c44702390

      It's rather dumb at the moment, but when number gets too high, it kicks on for 1 hour and if it's back below threshold it shuts off. There's also a human presence detector that will "pause" it for 5 minutes since it's in my kitchen window.

      It's built out of cardboard (laminated, with wheat paste) as a proof of concept/tinker with design and placement of things and also serves as a platform for the cats to nap in the window.

      This, mainly, helps from bringing in all the outside humidity during the summer and the bitter cold during the winter. Otherwise, prior, I'd just keep an exhaust fan running all the time (eating the losses on air conditioning/heat) but we'd end up closing the window when it was super hot/cold and then the iaq would get terrible.

      Lots and lots of people are automating their various systems due to monitoring these values. An application I've seen lots of is to just kick on the hvac systems fans when the aq drops below a particular threshold in one room or another.

      \> Lastly, ensuring your house is positively pressurized by paying a testing and balancing contractor to come over and adjust your HVAC system will do more to keep out particulate matter than measuring it ever will.

      Sadly, it took me a while to figure out that having this window fan in my kitchen on "exhaust" rather than "intake" was creating a negative pressure environment and that was.. not optimal.

      - **quickthrowman** · [2025-07-29 19:31 UTC](https://news.ycombinator.com/item?id=44727366)
        \> I use co2 measurements in my home to do just what you're describing here - automate control of a DIY fresh air intake (through a custom built filter box/fan enclosure w/ 5" merv 14 filter). ^c44727366

        That’s awesome! A cardboard POC that actually works is a cool project.

        \> Sadly, it took me a while to figure out that having this window fan in my kitchen on "exhaust" rather than "intake" was creating a negative pressure environment and that was.. not optimal.

        Maintaining positive pressure is tricky, one thing that can help is monitoring outdoor air pressure and duct static pressure in the supply duct and controlling fans/dampers to maintain positive pressure by keeping indoor higher than outdoor.

    - **macNchz** · [2025-07-27 15:00 UTC](https://news.ycombinator.com/item?id=44701813)
      I bought an Awair device in 2020 when my wife and I were working from home full time in the same room, out of curiosity as to whether our office area air was accumulating lots of CO2 during the workday (turns out this is not really an issue in drafty 120 year old houses). ^c44701813

      In the time since I’ve found it helpful for: confirming my DIY air purifier was effective during wildfire smoke periods, having a reminder to open the windows generally when the air gets stale and particularly after cooking, learning that cracking a window for makeup air for the range hood makes it much more effective, getting better about trimming candle wicks and snuffing them instead of blowing them out, getting a sense of our actual temp and humidity comfort ranges and how they differ from thermostat settings, and realizing that induction really might be preferable to gas whenever we’re looking to buy a stove in the future.

    - **pppone** · [2025-07-27 15:37 UTC](https://news.ycombinator.com/item?id=44702099)
      I used to run [https://www.open-seneca.org/](<https://www.open-seneca.org/>).  But, personally, it's nice to know the PM value whilst cooking, before going on a run, etc.  Permits you to take informed decisions. ^c44702099

    - **shawabawa3** · [2025-07-27 14:28 UTC](https://news.ycombinator.com/item?id=44701570)
      I use it to send an alert when CO2 is too high too open some windows ^c44701570

      I live in an old 1930s house in the UK so no HVAC or anything more automatable sadly

  - **bobmcnamara** · [2025-07-27 14:10 UTC](https://news.ycombinator.com/item?id=44701423)
    What's your measurement reference? Canned? ^c44701423

    - **pppone** · [2025-07-27 15:40 UTC](https://news.ycombinator.com/item?id=44702118)
      We've colocated many SPS30s with government reference stations, and the low cost sensor have always performed relatively well.  But, more importantly for my use case, they are exceptionally inter-comparable. ^c44702118

- **Catbert59** · [2025-07-27 07:41 UTC](https://news.ycombinator.com/item?id=44699559)
  Many particle sensors are useless in foggy/hazy conditions, which   ruins many citizen science projects in terms of data quality. Currently, the best solution is to calculate the dew point and then switching them off once you hit a specified limit. ^c44699559

  How does this model deal with this?

  - **pppone** · [2025-07-27 07:49 UTC](https://news.ycombinator.com/item?id=44699583)
    I don't think it would.  Data in these instances would have to be ignored. ^c44699583

    You can detrend for high humidities, but once water condenses, the only way round this would be to add a drying instrument.

    - **HPsquared** · [2025-07-27 08:47 UTC](https://news.ycombinator.com/item?id=44699856)
      I wonder if a radiant heat source beside the sensor, maybe also somehow focused in the same area, could get rid of the condensed water. ^c44699856

      - **Catbert59** · [2025-07-27 08:49 UTC](https://news.ycombinator.com/item?id=44699861)
        The problem is not condensed water. This can be solved with heating. ^c44699861

        It's that fog is being detected as a particle. This distorts the measured values.

        - **HPsquared** · [2025-07-27 09:41 UTC](https://news.ycombinator.com/item?id=44700068)
          Fog is condensed water droplets suspended in the air. Radiant heat , especially if it's optically focused, could remove them in the area where the PM sensor is looking. ^c44700068

  - **TimByte** · [2025-07-27 09:03 UTC](https://news.ycombinator.com/item?id=44699918)
    I didn't see anything in the article about humidity compensation ^c44699918

- **alliao** · [2025-07-27 06:41 UTC](https://news.ycombinator.com/item?id=44699335)
  love this... while the politicians busy angle themselves over stances on whether air filtration is required for public space during a pandemic engineers and companies come up with products and solutions ready to deploy.. it is my dream that our last generation gave us clean-ish water, and we can somehow pass down clean-ish air... ^c44699335

- **smingo** · [2025-07-27 07:32 UTC](https://news.ycombinator.com/item?id=44699511)
  The entire device is tiny: 20mm x 5mm x 5mm approx.  It looks to work using a small laser and a lens which focuses the beam about 5mm above the device.  The sensor unit contains a photodiode(s), and algorithms count the particulates.  It looks to need a heat sink. ^c44699511

- **ck2** · [2025-07-27 17:57 UTC](https://news.ycombinator.com/item?id=44703175)
  I wish everyone had an air-quality sensor on their smartphone ^c44703175

  it might make people give a darn how bad it typically is everywhere now

  But won't trust this sensor until there are tech comparisons by AirGradient and BreatheSafeAir.com

- **arnejenssen** · [2025-07-27 06:02 UTC](https://news.ycombinator.com/item?id=44699198)
  Cool. So we could get air quality apps for the phone or smartwatch? ^c44699198

  - **shagie** · [2025-07-27 13:29 UTC](https://news.ycombinator.com/item?id=44701194)
    Chasing through to [https://www.bosch-sensortec.com/products/environmental-senso...](<https://www.bosch-sensortec.com/products/environmental-sensors/particulate-matter-sensor/bmv080/>) ^c44701194

    \> Discover the PurpleAir PIXEL, one of the first end devices featuring the BMV080 particulate matter sensor for precise local air quality measurement. This user-friendly device provides real-time PM2.5 readings with a quick response time, clearly displayed via LED indicators. The BMV080‘s fanless design ensures completely silent operation, making it both effective and unobtrusive.

    [https://www2.purpleair.com/products/purpleair-pixel](<https://www2.purpleair.com/products/purpleair-pixel>)

    That's the form factor you'd be looking at when its included with the rest of the supporting circuitry and logic.

    So... possibly might be able to get it into a smaller package if the data display is externalized (Purple Air uses LEDs).

    My parents are interested in this as one of their use cases is to put it on their e-bike so that they can be made aware of worsening air conditions after they've left the house.

  - **mjs** · [2025-07-27 06:50 UTC](https://news.ycombinator.com/item?id=44699360)
    Might need to wait a few generations. It costs \~30€ for a single unit (maybe half that at volume?). And not waterproof. ^c44699360

    - **progbits** · [2025-07-27 08:36 UTC](https://news.ycombinator.com/item?id=44699805)
      It needs an external lens anyway so you could shove it into the camera assembly, waterproofing is not an issue. ^c44699805

      Cost is one, but this isn't something you can measure quickly on demand, you want to keep averaging multiple measurements over time. So unless you want to hold out your phone for minutes to get a measurement it doesn't seem practical.

    - **user\_7832** · [2025-07-27 10:32 UTC](https://news.ycombinator.com/item?id=44700274)
      Where did you see 30 euros? If so that's quite good I think - I remember (a long time ago when I was researching air sensors) Honeywell's laser sensors were similarly priced. A low price point will absolutely help Bosch drive adoption. ^c44700274

      - **mjs** · [2025-07-27 21:20 UTC](https://news.ycombinator.com/item?id=44704789)
        Re price, there's links to retailers from [https://www.bosch-sensortec.com/products/environmental-senso...](<https://www.bosch-sensortec.com/products/environmental-sensors/particulate-matter-sensor/bmv080/>) ^c44704789

- **progbits** · [2025-07-27 08:32 UTC](https://news.ycombinator.com/item?id=44699778)
  I mean this is cool but the size claims are somewhat misleading. They only sell you a sensor element on flatflex PCB, then you need to add own metal cage for thermal dissipation and a lens, so the overall size is significantly larger. ^c44699778

  This is great for flexibility but very impractical especially for DIY space. Hopefully small fully integrated modules on something like edgeconnector PCB come out soon enough.

  - **joshvm** · [2025-07-27 09:50 UTC](https://news.ycombinator.com/item?id=44700104)
    Unless I misread, the lens is integrated, but Bosch recommends an optical window to protect the device. The integration guide is pretty comprehensive. Many fan-based air sensors require some specific enclosure considerations to separate the in/outflow. ^c44700104

    Sparkfun sell a module with a ground plane + thermal pad as heat sink. This is suggested as OK by Bosch, though adding a small heatsink is probably a good idea, or just mount the enclosure on a metal surface.

    [https://www.sparkfun.com/sparkfun-air-quality-pm1-pm2-5-pm10...](<https://www.sparkfun.com/sparkfun-air-quality-pm1-pm2-5-pm10-sensor-bmv080-qwiic.html>)

    [https://www.bosch-sensortec.com/media/boschsensortec/downloa...](<https://www.bosch-sensortec.com/media/boschsensortec/downloads/handling_soldering_mounting_instructions/bst-bmv080-hs000.pdf>)

    - **progbits** · [2025-07-27 10:39 UTC](https://news.ycombinator.com/item?id=44700304)
      Ah I was looking at the integration guide but just skimmed it and I thought the window was a required lens. Thanks for the correction. (Can no longer storage edit my comment unfortunately) ^c44700304

- **benbojangles** · [2025-07-27 16:49 UTC](https://news.ycombinator.com/item?id=44702601)
  What use case would miniaturisation of dust sensors have, i mean i am unsure if it is going inside smartphones or smartwatches? What can it do that others cannot? ^c44702601

- **TimByte** · [2025-07-27 08:57 UTC](https://news.ycombinator.com/item?id=44699893)
  The fact that it's fanless and still works reliably makes me curious how well it handles airflow variability in real-world settings though ^c44699893

- **dzhiurgis** · [2025-07-27 20:43 UTC](https://news.ycombinator.com/item?id=44704536)
  Wish macbooks came with air sensors. Already has a fan, on when you use it can be woken up every 5 minutes if you need continuous monitoring. ^c44704536

- **SideburnsOfDoom** · [2025-07-27 09:29 UTC](https://news.ycombinator.com/item?id=44700016)
  FYI, it is a "Smallest sensor, for particulate matter", not "sensor, of Smallest particulate matter" ^c44700016

