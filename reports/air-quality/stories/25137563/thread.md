# [How to better ventilate your home](https://news.ycombinator.com/item?id=25137563)

Article: [https://www.theatlantic.com/health/archive/2020/09/diy-ventilation-home-pandemic/616150/](<https://www.theatlantic.com/health/archive/2020/09/diy-ventilation-home-pandemic/616150/>)

arunbahl · 2020-11-18 15:09 UTC · 76 reported comments · archived 2026-11-08 11:28 UTC
Observation: 2026-11-08 11:27 UTC → 2026-11-08 11:28 UTC

## Comments

- **DoofusOfDeath** · [2020-11-18 16:14 UTC](https://news.ycombinator.com/item?id=25138485)
  I started taking IAQ seriously when I soundproofed my home office. The soundproofing made the room nearly airtight, so I had to think about (at the very least) CO2 buildup within the office. ^c25138485

  I've hit an interesting problem regarding CO2 monitoring: calibration and validation.

  Every IAQ CO2 meter I've come across allows self-calibration and/or calibration by exposure to "open air" which is assumed to be about 400 ppm CO2.

  But none of the meters provide any means to calibrate / validate CO2 levels *other than* the reference level.

  For example, suppose I buy two CO2 meters from Amazon. They can both tare to 400 ppm. But once the CO2 in my office builds up, one might read 1200ppm while the other reads 800ppm.

  According to medical literature, 800 ppm vs. 1200 ppm is a pretty significant difference for human mental performance. If the CO2 level is *actually* 1200 ppm, I want to crank the office ventilation system, even though it means higher background noise. At just 800 ppm, I may prefer the quiter work environment.

  Another downside to this difficulty in testing is that it's hard to *truly* evaluate a particular meter's performance. Which seriously limits side-by-side comparisons of different models, and makes it harder to hold manufacturers / retailers accountable for poor performance.

  - **ChuckMcM** · [2020-11-18 18:01 UTC](https://news.ycombinator.com/item?id=25140027)
    Agreed, the difference between "real" CO2 meters and consumer CO2 meters is really stark. Given that you can get nitrogen and CO2 in tanks, I expect one could build a calibration setup with a fixed volume tank, two metered gas ports, and some software. Start by purging the tank with nitrogen, then add CO2 for the 400ppm baseline. Calibrate there, then add increments of 100ppm (or 50ppm) CO2 and record the readings up to say 1500ppm total. Then you have a calibration table for that meter that will let you translate from its indicated ppm to the real ppm. ^c25140027

    - **nickff** · [2020-11-18 21:25 UTC](https://news.ycombinator.com/item?id=25142641)
      That won't necessarily make the meters match. The sensors can be perfectly calibrated for CO2, but still read differently because most of the sensors are sensitive to a variety of other carbon-containing gasses. ^c25142641

      Most consumer CO2 detectors use a sensor which measures the IR absorption of its surroundings. These sensors have varying cross-sensitivities to a bunch of other gasses including carbon monoxide, propane, alcohol, etc. Calibrating them for CO2 will not compensate for different responses to CO, which is much more IR-absorbent in many of the same frequency bands.

    - **GrumpyYoungMan** · [2020-11-18 22:27 UTC](https://news.ycombinator.com/item?id=25143359)
      That's unnecessary since there's pre-calibrated mixtures referred to, unsurprisingly, as "calibration gas" readily available.  Googling for "carbon dioxide calibration gas" will find you what you need as well as the appropriate pressure regulators. ^c25143359

      Note that even the professional meters require calibration on a regular basis; for example the calibration schedule for the Fluke 975 for CO2 is yearly and for carbon monoxide is monthly.

    - **DoofusOfDeath** · [2020-11-18 18:08 UTC](https://news.ycombinator.com/item?id=25140111)
      That's roughly my understanding about how these devices are actually tested in labs. ^c25140111

      Probably not something I'd tackle on my own, but it would be awesome if Consumer Reports or a major newspaper hired a lab to do this. With so many people working from home now, I would think it's an increasingly relevant issue.

  - **joekrill** · [2020-11-18 16:37 UTC](https://news.ycombinator.com/item?id=25138847)
    Not to derail the conversation, but I'm curious about how you soundproofed your home office. Do you have any information about how you went about that and what was involved? I've been looking into this myself recently. ^c25138847

    - **DoofusOfDeath** · [2020-11-18 16:40 UTC](https://news.ycombinator.com/item?id=25138891)
      One of the key takeaways is that the approach depends heavily on the space you're trying to soundproof, and just how much sound reduction you need at various frequencies. ^c25138891

      Feel free to DM me (see my profile) if you'd like to talk specifics.

    - **turtlebits** · [2020-11-18 17:05 UTC](https://news.ycombinator.com/item?id=25139268)
      Depends on what you're looking for but adding an additional layer of drywall (5/8) with acoustical sealant sandwiched is an inexpensive way reduce sound transmission. ^c25139268

  - **throwaway9d0291** · [2020-11-19 09:58 UTC](https://news.ycombinator.com/item?id=25147892)
    \> Every IAQ CO2 meter ^c25147892

    \> For example, suppose I buy two CO2 meters from Amazon

    It sounds like you're looking at retail consumer products, which I think is the problem.

    The Sensirion SCD30 \_sensor\_ \[0\] for example allows forced recalibration \[1\] to an arbitrary concentration.

    Also, since you call it an "IAQ" CO2 meter, it might be that these aren't CO2 meters at all. They could be VOC meters that make up a projected CO2 reading based on the presence of other chemicals in the air. You need to make sure the sensor is NDIR-based and actually measures CO2.

    If you want accuracy, don't buy retail sensors that don't come with spec sheets. I'd find the sensor you want first then find or build a meter based on it. For example the SCD30 can be connected to an ESP32 and connected to WiFi using ESPHome \[2\], which can be set up with some YAML files.

    \> self-calibration

    Just by the way, self-calibration is what you want. Real CO2 sensors drift over time and you definitely want them recalibrated at least once a year. Auto-calibration takes away that pain and when implemented in a suitable way, really works. Many calibration routines are not suitable for residential environments as they're based on the assumption that they will see pure fresh air at least once a day. This is a safe assumption in a business environment because most AC systems have an overnight fresh air purge. In a residential environment though, someone might not open the window once a day.

    Again referencing Sensirion, their auto-calibration cycle looks for two, hour-long valleys in the CO2 readings over the previous two weeks that are within a few percent of each other and uses those as a fresh air reference. In my experience, this works well at home.

    \> Another downside to this difficulty in testing is that it's hard to truly evaluate a particular meter's performance. Which seriously limits side-by-side comparisons of different models, and makes it harder to hold manufacturers / retailers accountable for poor performance.

    You "just" need a reference to compare to. If you have a look at academic literature, they typically use a lab-grade setup to compare. You're right though, it's difficult for a regular home user to evaluate a sensor like this.

    \[0\]: [https://www.sensirion.com/en/environmental-sensors/carbon-di...](<https://www.sensirion.com/en/environmental-sensors/carbon-dioxide-sensors/carbon-dioxide-sensors-co2/>)

    \[1\]: [https://www.sensirion.com/fileadmin/user\_upload/customers/se...](<https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.5_CO2/Sensirion_CO2_Sensors_SCD30_Interface_Description.pdf>)

    \[2\]: [https://esphome.io/](<https://esphome.io/>)

- **ThePadawan** · [2020-11-18 15:40 UTC](https://news.ycombinator.com/item?id=25137966)
  Surprised to read nothing about the German fascination with Stosslüften (opening as many windows as possible as wide as possible for 5 minutes, twice daily. Literally "shock airing" or "surge airing"). ^c25137966

  Every apartment I moved into (in Switzerland) had me sign a waiver that I read the instructions how to do this to avoid mold growth.

  - **subpixel** · [2020-11-18 15:47 UTC](https://news.ycombinator.com/item?id=25138088)
    As an exchange student in Germany I never got accustomed to the urgency with which my host mother would rush into my bedroom and throw open the window exclaiming "Frische Luft! Frische Luft!" ^c25138088

    - **ThePadawan** · [2020-11-18 15:52 UTC](https://news.ycombinator.com/item?id=25138165)
      I personally got into the habit from school, where opening the windows after a double lesson (90min) before the next class came in was just the polite thing to do. ^c25138165

      Nothing worse than walking into a room with air that's been depleted of oxygen (then reading Theodor Fontane).

  - **rsync** · [2020-11-18 16:56 UTC](https://news.ycombinator.com/item?id=25139117)
    We do this in my home. ^c25139117

    We get to cheat a bit since we live in California so it doesn't really mean anything to open the windows for 20-30 minutes in the winter.

    Regardless, I cannot abide stuffy/dead air and I will ventilate any house or apartment we are staying in regardless of outside temperature.

    I believe this to be a *very underrated* disease prevention tool.

    - **unknown** · [2020-11-19 01:44 UTC](https://news.ycombinator.com/item?id=25145278)
      [deleted] ^c25145278

  - **marton78** · [2020-11-18 18:59 UTC](https://news.ycombinator.com/item?id=25140857)
    We do this in Hungary, too. I'd venture to guess this is probably the same at least in all of ex-Habsburg Central Europe. ^c25140857

    I don't know how people in other parts of the world can stand the stench of used up air. You won't notice when you're inside the room, but coming from the outside you feel like suffocating.

    Or maybe where this isn't common, people have active ventilation systems?

  - **post\_break** · [2020-11-18 17:53 UTC](https://news.ycombinator.com/item?id=25139909)
    In Houston you would be bringing the mold inside due to the humidity. ^c25139909

  - **0x1F8B** · [2020-11-18 16:06 UTC](https://news.ycombinator.com/item?id=25138364)
    Do people do this in the winter as well? ^c25138364

    - **ThePadawan** · [2020-11-18 16:21 UTC](https://news.ycombinator.com/item?id=25138583)
      Yes! ^c25138583

      You'd be surprised how little it changes room temperature.

      A lot of the thermal mass is conserved in the walls, furniture and people in the building.

      - **heffer** · [2020-11-18 16:52 UTC](https://news.ycombinator.com/item?id=25139064)
        This is true in Germany, where most in-home heating systems use radiant heat. I have since moved to Canada and my house uses forced air and a gas furnace. I can still feel cold at 21.5°C in my forced air heated house which I never did in Germany.
        Radiant heat does a much better job of heating the things in your house than forced air will. Heating things, and not just the air, is what has them store that warmth across Stoßlüften-Sessions.
        So technically, Stoßlüften works well with radiant heated homes, less so with forced air heated homes. ^c25139064

        - **ThePadawan** · [2020-11-18 17:23 UTC](https://news.ycombinator.com/item?id=25139500)
          That's true! I was also thinking about how German houses also tend to have relatively thick and non-wooden walls (since compared to the US, there's no significant earthquake risk). ^c25139500

          That adds a lot of thermal mass as well.

        - **CyberDildonics** · [2020-11-18 17:38 UTC](https://news.ycombinator.com/item?id=25139695)
          Is it much more likely that there is a difference in how your thermostat is placed or there was better insulation (so that heat ends up more even). ^c25139695

          - **war1025** · [2020-11-18 18:19 UTC](https://news.ycombinator.com/item?id=25140290)
            Over the past few years I've been working on improving the thermal efficiency of our house, which has mainly been strategic air sealing / adding insulation. ^c25140290

            One thing I've definitely noticed is that as I improve the insulation in one area of the house, other areas will get colder.

            The reasoning is that the worst insulated spots in my house were near to the thermostat. Now they they can maintain heat decently, the further way areas are allowed to cool more before the heat kicks on.

            The first tool someone should buy when investigating the thermal efficiency of their house is one of the cheap (\$30- \$50 if I remember right) infrared thermometers.

            The temperature of your house is likely 5-10F off from what your thermostat claims, particularly the further you get from the thermostat.

            - **CyberDildonics** · [2020-11-18 18:55 UTC](https://news.ycombinator.com/item?id=25140787)
              Exactly, you can even get infrared thermometers for less now that they are being used to take people's temperatures when they enter a business. ^c25140787

            - **skoskie** · [2020-11-19 01:44 UTC](https://news.ycombinator.com/item?id=25145277)
              Meanwhile, I can feel an outside gust of cold wind from the middle of my home. I don’t begin to know where to start. ^c25145277

              - **war1025** · [2020-11-19 02:26 UTC](https://news.ycombinator.com/item?id=25145527)
                The biggest issue in my house ended up being that the builders didn't bother to insulate or air-seal the subfloor areas (the space between the floor of one level and the ceiling of the level below). ^c25145527

                Found that out the hard way when three years ago during our first Winter here, the water to the kitchen was frozen for most of the month of January. Thankfully our house has PEX piping, so no burst pipes for us.

                Sealing and insulating those areas has made a tremendous difference, even in the interior areas of the house. Since the subfloor is wide open, a cold breeze from one spot can suck the heat out of the entire floor with surprising effectiveness.

                - **ggcdn** · [2020-11-19 05:09 UTC](https://news.ycombinator.com/item?id=25146426)
                  Perhaps I misunderstood your description of subfloor, but I don’t think it’s common anywhere to insulate between interior floors or walls. ^c25146426

                  - **war1025** · [2020-11-19 15:22 UTC](https://news.ycombinator.com/item?id=25150380)
                    I mean the exterior walls of our house were completely uninsulated in the subfloor area. ^c25150380

                    You're correct that it doesn't make sense to insulate between floors, but you do need to insulate the entire exterior wall area, which includes the wall space between floors.

      - **LeifCarrotson** · [2020-11-18 18:28 UTC](https://news.ycombinator.com/item?id=25140416)
        It changes the perceived room temperature even less than actual temperature! ^c25140416

        As you say, air has little mass and very little thermal mass, solids have a lot more thermal mass so the equalized temperature after briefly exchanging all the air for cold air is basically the same as the original.

        But physiologically and psychologically, human comfort levels are based not on the air temperature and convection or conduction with the air but on the *mean radiant temperature*, the temperature of an ideal enclosure of uniform emissivity and temperature that creates the same radiant heat transfer rates as whatever non-uniform surfaces are in the area.

        Sit with your face in a sunbeam in a cold house, and you'll feel like it's pleasantly warm even if the heating of the sunbeam is doing less than the motion of cold air wicking away heat. Open your garage door on a still winter day, standing in the warm air with one wall removed, exposing you to sub-freezing temperatures, and you'll feel cold even if the air is still warm.  Stand in the high-temp air blast of a torpedo heater in a cold shop, with the ceiling, concrete floor, walls, and other equipment still frigid, and you'll feel cold even as the hot air melts the plastic bits on your clothes.  Blast the AC in a hot car, and you might be breathing air at 40F/5C from the vents, but you'll still feel hot until the vehicle interior trim is cooled by the air.

  - **shostack** · [2020-11-18 17:43 UTC](https://news.ycombinator.com/item?id=25139752)
    Is there any research to back up the practice? ^c25139752

    - **BitwiseFool** · [2020-11-18 17:48 UTC](https://news.ycombinator.com/item?id=25139834)
      And, does it circulate enough air when there isn't a breeze? ^c25139834

      - **olau** · [2020-11-18 21:50 UTC](https://news.ycombinator.com/item?id=25142887)
        No, although if it's cold outside, you might get a sea breeze effect. ^c25142887

        But most of the time (say \> 80\% IIRC) in Northern Europe there is at least some wind, and having a large cross sectional area is just incredibly efficient. You can try the experiment yourself.

        The main problem is that it is a manual process requiring discipline, and if you don't do it, your brain suffers due to elevated CO2 levels.

        - **ThePadawan** · [2020-11-19 08:45 UTC](https://news.ycombinator.com/item?id=25147484)
          Also worth mentioning that the most common kind of window over here is hinged, not double-hung. Meaning you can actually open them to create a gap of 100\% of their area, not \<\= 50\%. ^c25147484

  - **csunbird** · [2020-11-18 16:09 UTC](https://news.ycombinator.com/item?id=25138415)
    It is also a tradition in Turkey too. I have been taught to open windows first thing in the morning to clean up the air. ^c25138415

  - **syntaxing** · [2020-11-18 19:03 UTC](https://news.ycombinator.com/item?id=25140918)
    How do you adjust for this during the winter? Do you turn off your heat or just keep the heat on and open the windows? ^c25140918

    - **ThePadawan** · [2020-11-18 20:11 UTC](https://news.ycombinator.com/item?id=25141811)
      I would do nothing. For 5 minutes, turning off the heat wouldn't do much at all - the big heaters are generally very laggy anyway. ^c25141811

- **doctorhandshake** · [2020-11-18 15:45 UTC](https://news.ycombinator.com/item?id=25138037)
  I’m surprised there’s no mention here of heat recovery ventilators (HRV) or energy recovery ventilators (ERV) here. New buildings are increasingly designed to provide regular air exchange (fresh air replacing indoor air) while retaining thermal energy with these devices, and, in the case of ERV, retaining humidity. ^c25138037

  - **compumike** · [2020-11-18 16:15 UTC](https://news.ycombinator.com/item?id=25138496)
    Agree. HRV / ERV is a powerful concept because it allows you to design better insulated buildings, both with fewer air gaps and thicker wall insulation, while still reducing indoor CO2 and humidity levels by bringing in fresh air. ^c25138496

    On the downside, like much in the HVAC world, it requires new construction or a fairly major retrofit to take advantage of it. My guess is that it's only going to make sense for new higher-end construction where other attention is being paid to energy efficiency. (Though I'd love to see a window box HRV for renters, just like window box air conditioners.)

    If you haven't heard of HRV / ERV yet, this video shows how they work in an impressive but simple demo with the 4 temperature sensors in the last few minutes: [https://www.youtube.com/watch?v\=QOSelUK6dpQ](<https://www.youtube.com/watch?v=QOSelUK6dpQ>) (Also compares aluminum core heat exchanger vs. desiccant enthalpy wheel)

    For the DIYers, here's a forum full of people building their own HRVs: [https://ecorenovator.org/forum/showthread.php?t\=891](<https://ecorenovator.org/forum/showthread.php?t=891>)

    - **amluto** · [2020-11-18 17:18 UTC](https://news.ycombinator.com/item?id=25139447)
      They don’t necessarily need a major retrofit.  Lunos makes clever paired half-HRVs that require two wall penetrations but no ducts. Zehnder makes single-room through-wall HRVs. ^c25139447

  - **turtlebits** · [2020-11-18 17:22 UTC](https://news.ycombinator.com/item?id=25139488)
    I would only recommend an ERV for newer houses.  On older houses, an ERV running 24/7 is just going to pull all the heat out of your house and cause your energy bills to go up. ^c25139488

    Best would to get a blower door test run and see what your ACH50 rating is before considering one.

  - **mherdeg** · [2020-11-18 16:28 UTC](https://news.ycombinator.com/item?id=25138680)
    Yup. Now that I'm measuring how much CO2 I have indoors and can watch what happens when I open a window and it equilibrates, it's really hard to resist 2021+ plans to retool the HVAC to put in a fresh air ventilator. ^c25138680

    There were also a few days this summer where it was 50°F and low-humidity outside, but 78°F inside, my preferred temperature was closer to 72°F, and I wished I had some better way than "open a window and stick in a Lasko box fan" to cycle in cool outdoor air.

  - **dota\_fanatic** · [2020-11-18 16:54 UTC](https://news.ycombinator.com/item?id=25139093)
    Having just built an addition which needed its own HVAC system, I was surprised to find the cost of an American Standard ERV to be several thousand dollars, prohibitively expensive for us given all the other costs. :/ ^c25139093

    - **johnrgrace** · [2020-11-18 19:37 UTC](https://news.ycombinator.com/item?id=25141366)
      Most of the cost is install.  A basement glass block window with a dryer vent (under \$100 for a pro to install around me) makes self installing easy and professional a few hours of labor. ^c25141366

      I've seen new ERV units under \$1,000 and some pop up used on Ebay for great prices.

    - **turtlebits** · [2020-11-18 17:11 UTC](https://news.ycombinator.com/item?id=25139349)
      Not sure the size of your addition, but Panasonic makes a small ERV for around \$400, I use it in my 500sf workshop.  They have a larger model that is around \$1000. ^c25139349

  - **kev009** · [2020-11-18 17:42 UTC](https://news.ycombinator.com/item?id=25139747)
    Was looking to see if anyone had experience with ERV/HRV.  I would like to put these on my new to me home when I replace the HVAC units. ^c25139747

    - **gwd** · [2020-11-18 18:09 UTC](https://news.ycombinator.com/item?id=25140130)
      I retrofitted one on a house we bought a couple of years ago.  I'm really happy with it, although it does add a constant background 'hum'.  It wouldn't have been possible however if we weren't doing major renovation -- we tore out & replaced the downstairs ceiling and completely redid the second floor bathroom; that meant we could run the ducts down the corner of the bathroom and then through the joists in the first floor fairly easily.  And the attic is a bit cluttered with the ducts. ^c25140130

      You definitely notice a difference when you turn it off.

    - **tzs** · [2020-11-19 04:40 UTC](https://news.ycombinator.com/item?id=25146289)
      This report \[1\] suggests that HRVs only actually have a net energy savings in the US in climate zones 4-8 (and such a small amount in zone 4 that it would take several decades to break even). ^c25146289

      Is there a good reason to get them if one is in a place where they won't save energy?

      Here's a US climate zone map \[2\].

      \[1\] [https://www.osti.gov/biblio/1488935](<https://www.osti.gov/biblio/1488935>)

      \[2\] [https://basc.pnnl.gov/images/iecc-climate-zone-map](<https://basc.pnnl.gov/images/iecc-climate-zone-map>)

    - **blacksmith\_tb** · [2020-11-18 17:56 UTC](https://news.ycombinator.com/item?id=25139956)
      I've lived for 8yr now in a home with a Zehnder HRV. It has mostly worked well, though recent wildfires were too much for its MERV-13 filters, forcing me to run it at the very slowest speed and use air purifiers. ^c25139956

  - **jonstewart** · [2020-11-18 16:11 UTC](https://news.ycombinator.com/item?id=25138438)
    Yeah, ERVs are amazing. I want to install one in my house just to provide fresh air all the time. ^c25138438

- **shalmanese** · [2020-11-18 15:24 UTC](https://news.ycombinator.com/item?id=25137745)
  The reason why paperweights exist was because, prior to air conditioning, offices were built to have a constant flow of air through them to cool down workers. ^c25137745

  - **motorbreath** · [2020-11-18 16:38 UTC](https://news.ycombinator.com/item?id=25138858)
    I was going to mention something similar to this! ^c25138858

    We've all experienced first-hand how irritating it can be when your papers start flying all over the place because the windows are open.

    There is a lot of interesting history behind paperweights and I would love to find some of the originals in a museum.
    [https://www.paperweight.org/museums/](<https://www.paperweight.org/museums/>)

- **fatnoah** · [2020-11-18 15:46 UTC](https://news.ycombinator.com/item?id=25138072)
  What an odd article.  I'd love to know more about the author's background where he's just now considering airflow in a home.  Maybe it seems strange to me since I was in my late 30's before I lived anywhere that had air conditioning, so open windows, fans, cross-drafts, and general air flow were the norm. ^c25138072

  I also want to see what happens when the author discovers the whole house fan.  My very first house had one and it was amazing. Crack open a window in each room and activate the fan.  Instant breeze and air circulation in every room with somewhere around 6-8 air changes per hour.

  - **senux** · [2020-11-18 16:10 UTC](https://news.ycombinator.com/item?id=25138430)
    I believe this is related to the number of people locked at home. ^c25138430

  - **war1025** · [2020-11-18 18:14 UTC](https://news.ycombinator.com/item?id=25140201)
    I have been very tempted to buy a whole house fan for a couple years now. ^c25140201

    My compromise has been to put a box fan in our attic access and leave that running, which does more than nothing, but I have to imagine a proper house fan would be much better.

    I've never actually been somewhere with one to know what to expect. I've heard good things though.

    - **EricE** · [2020-11-20 15:05 UTC](https://news.ycombinator.com/item?id=25161077)
      Get the right one and they are quite, effective and cost efficient too! ^c25161077

      I like designs like these: [https://quietcoolsystems.com](<https://quietcoolsystems.com>)

      It took a couple hours to install, mainly because I went back and forth where to install the intake vent.  I had power readily available from a hallway outlet - added a switch above the outlet, carried it up into the attic and to the fan.  If you aren't comfortable doing your own wiring that will be the hardest part of installing the fan.  The rest is simple - cut a hole in the drywall of your ceiling where you want the intake, mount the insulated box with the insulated dampers that close when the fan is not in use, hang the fan with the proper 90 degree bend in the duct, wire it in and finally snap the grate on and you are done.  The only "glitch" I had with my install is I had the fan pointed down a bit too much and my attic has blown in insulation (ugh).  The fan ended up blowing a big "hole" in it.  So I adjusted the fan, raked the insulation back into place and haven't had an issue since.

      My air conditioners each use about 2400 watts each (I have two!), the motor on my whole house fan is around 640 watts.  We had an exceptional fall the year I put it in, and it more than paid for itself.  And I got the benefits of fresh air.  I live in the Mid Atlantic so spring and fall are the biggest time of year I can use it, but this year our summer wasn't too bad with humidity so I used it most of the summer too.  It's amazing how much heat you can tolerate if you have a steady breeze.

      I highly recommend them!  My only complaint is I wish mine had variable speed.  There are many times at night it gets way too cold to run at normal speed, but if off the heat of everything in the house will heat the interior back up again without at least some airflow.  With the size of my house I need to add a second one anyway to get enough airflow/turn over so I'm thinking about one of their units that has two fans - can run just one for a lower amount of air volume.

      One of my best home upgrades, that's for sure!

      - **war1025** · [2020-11-20 15:17 UTC](https://news.ycombinator.com/item?id=25161222)
        This is super helpful. Thanks! ^c25161222

        How often do you leave it running? Is it a continuous thing or just periodically?

        - **fatnoah** · [2020-11-20 17:00 UTC](https://news.ycombinator.com/item?id=25162327)
          The one I had ran on a timer, so it could be run up to 60 minutes at a time.  I usually ran it from 10-20 minutes, depending how cool it was going to get. ^c25162327

    - **fatnoah** · [2020-11-19 16:08 UTC](https://news.ycombinator.com/item?id=25150877)
      It's amazing when it works.  In the summer, once the air outside was cooler than the air in the house, I'd turn it on.  In about 10 minutes, the entire house would be the same temperature as outside. ^c25150877

  - **closeparen** · [2020-11-18 21:28 UTC](https://news.ycombinator.com/item?id=25142664)
    I worked in a theater that had such a fan in the rafters. If we fired it up with the main traveler closed, the curtain would be pushed forward 30 degrees or more by the airflow, like a sail. ^c25142664

  - **johnrgrace** · [2020-11-18 19:40 UTC](https://news.ycombinator.com/item?id=25141409)
    I owned a house in Houston, Tx and New Orleans, LA and each had whole house fans and they were great to use at the right points in the season. ^c25141409

- **ChuckMcM** · [2020-11-18 17:54 UTC](https://news.ycombinator.com/item?id=25139938)
  Fun read, my wife sometimes accuses me of having shark DNA because I can obsess over having fresh air moving past me at all times. :-) For me though the difference is one of comfort versus a vague tension. Some folks have associated this sort of thing with claustrophobia as well. ^c25139938

  That said, we spent a few thousand dollars insulating and sealing our home so that we did not need HVAC assisted climate control. Part of that included finding ways to exchange the house air with outside air so that during the summer months we could pull in cool air at night to lower the house temperature, seal it up when the Sun came up, and then remain cool all day. Similarly with bringing in warmth during the day in winter and minimizing the temperature fall during the evening. This is not particularly great for minimizing COVID in one's home.

- **jkepler** · [2020-11-19 07:29 UTC](https://news.ycombinator.com/item?id=25147068)
  In the early 20th century, British children's educator Charlotte Mason emphasized the importance of air quality, outside air, and frequently changing one's inside air: ^c25147068

  "Unchanged Air.––Parents of pale faced town children, think of these things! The gutter children who feed on the pickings of the streets are better off (and healthier looking) in this one respect than your cherished darlings, because they have more of the first essential of life––air. There is some circulation of air even in the slums of the city, and the child who spends its days in the streets is better supplied with oxygen than he who spends most of his hours in the unchanged air of a spacious apartment. But it is not the air of the streets the children want. It is the delicious life-giving air of the country. The outlay of the children in living is enormously in excess of the outlay of the adult. The endless activity of the child, while it develops muscle, is kept up at the expense of very great waste of tissue. It is the blood which carries material for the reparation of this loss. The child must grow, every part of him, and it is the blood which brings material for the building up new tissues. Again, we know the brain is, out of all proportion to its size, the great consumer of the blood supply, but the brain of the child, what with its eager activity, what with its twofold growth, is insatiable in its demands!" (Charlotte Mason, "Home Education, p. 31. Availible online, 
  [https://www.amblesideonline.org/CM/vol1complete.html\#031](<https://www.amblesideonline.org/CM/vol1complete.html#031>))

- **voisin** · [2020-11-19 01:45 UTC](https://news.ycombinator.com/item?id=25145286)
  I’ve been looking toward building a new house and it seems the latest and greatest concept is the Passive House which seems to be an incredibly airtight envelope combined with a fresh air system to exchange air that includes a heat recovery system. I am left dumbfounded, as you become completely reliant on this technology which may break down or (more likely) fail to perform to spec or (even more likely) be spec’d incorrectly or incompatibly relative to future uses. ^c25145286

  It seems to me it would be far better to have large thermal masses and radiant heat, and then allow for the usual air loss around windows and doors and attics.
  Anyone here have thoughts on this approach vs Passive House?

- **kyledrake** · [2020-11-18 16:56 UTC](https://news.ycombinator.com/item?id=25139125)
  I recently purchased a home and spent some time improving ventilation in it this year. This is a home in Minneapolis, so just "opening a window" is not an option, as it would be too cold in the winter and dramatically reduce energy efficiency. Its effectiveness also changes based on factors like the wind, and the temperature difference between inside and out. ^c25139125

  The general strategy for doing this right now with existing homes is to insulate your home as well as possible for energy efficiency, then install a continuous ventilation fan. This is essentially a bathroom fan, except that it runs all the time at a constant low speed, helping to circulate the air through and out your house by "pulling" a designed amount of air through the cracks.

  I didn't want to punch a new hole in the house just to do this, and already had a bathroom fan installed, so as a hack I just turned it into a whole house ventilation fan with this: [https://www.aircycler.com/pages/smartexhaust](<https://www.aircycler.com/pages/smartexhaust>)

  Basically you calculate how much CFM you need per hour based on the square footage of your house, and then you set it on the fan control. It still acts like a bathroom fan, except every hour it also runs for a set period of time (in my case, about 12 minutes).

  The standard for this is ASHRAE 62.2. Use this to calculate the CFM for code: [https://homes.lbl.gov/ventilate-right/step-3-whole-building-...](<https://homes.lbl.gov/ventilate-right/step-3-whole-building-ventilation-rate>)

  Then the formula for calculating the fan run time is on this sheet: [https://cdn.shopify.com/s/files/1/0221/7316/files/AC\_DOC\_7\_0...](<https://cdn.shopify.com/s/files/1/0221/7316/files/AC_DOC_7_0_SmartExhaust_Cut_Sheet_rs_20ce4f30-fa23-4dc0-a879-ce2e765fc31b.pdf?v=1593031639>)

  And presto, you have a ventilation system without having to do a lot of work. Do \_not\_ try this with a crappy, rusty old bathroom fan - clean or replace the motor first, and for extra credit, use an arc fault circuit interrupter on the breaker so if the motor fails it will blow the fuse instead of potentially causing a fire.

  Note: This is really just to manage general air quality and VOCs. If you want to specifically make ventilation for COVID-19, that's a different problem. They focus on Air Changes per Hour (ACH), and a cubic feet calculation is used rather than square feet. There's no "recommended amount" of ACH for managing COVID-19. You're likely improving the situation by increasing it, but I wouldn't start inviting people over after you did it. ACH is very high in ICUs but staff are still getting sick there.

  RE Humidity - ideal range varies based on region and outside temperature, but this chart roughly shows it: [https://lh3.googleusercontent.com/proxy/mPz-jGdLpnPGgvWR3Egf...](<https://lh3.googleusercontent.com/proxy/mPz-jGdLpnPGgvWR3EgfvrhuT5mPgkKK_AQKZNzekzAyvsOGeFvGKK6Jn0kWGPEYYGkEAFM6CE3-BXLQzDEF_7_lV-H6HAfD5bXAl5HvUGB5rAjH9X1fPLLf8Q>)

  I have an on-furnace humidifier controlled by an ecobee for the winter, it's a huge quality of life improvement if you live in cold climates, but make sure to set it to "frost control" otherwise it won't lower the humidity based on the outside air and you can get mold in your walls. For summer, a standard house A/C combined with continuous ventilation should be sufficient to bring down humidity levels.

  Finally, the "correct" air ventilation is a moving target with trade-offs and concerns of the moment. It was higher in 1925 (30cfm/person) to try to prevent tuberculosis and infectious diseases, then was lowered to 5cfm/person in the 70s during the energy crisis, and is currently at 15cfm/person. I imagine COVID-19 could make us re-consider the current recommendations. [https://homes.lbl.gov/ventilate-right/ashrae-standard-622](<https://homes.lbl.gov/ventilate-right/ashrae-standard-622>)

  - **shostack** · [2020-11-18 17:45 UTC](https://news.ycombinator.com/item?id=25139798)
    I'm in an older home that leaks a sieve but has central air. Would turning on that house fan to circulate without running the AC accomplish the same thing? Also, do any smart thermostats allow this sort of thing to be automated? ^c25139798

    - **kyledrake** · [2020-11-18 18:17 UTC](https://news.ycombinator.com/item?id=25140250)
      I know at least the Ecobee can run the HVAC fan for a fixed period of time per hour. ^c25140250

      Not an expert on this but from what I know, I wouldn't approach it this way. Even with a leaky house, the fan is mostly going to be blowing the air around the house, not pushing it out and sucking in fresh air which is what you want, and it will consume a lot of power doing it while shortening the life of an expensive part. Might help dilute a hot spot, but it's not creating a "stream" of air from the inside to out, it's just blasting the particles all over the place.

      You really do need to have a lower power fan that's actually able to push air directly outside, such as a bathroom fan or a stove vent. If you were going for a "quick hack", I would just use the bathroom fan for this purpose, but as mentioned above they're not designed for continuous operation and usually haven't been cleaned out in ages, so I would clean it out and try not to have it running when I'm not around in case it fails.

      For just filtering air vs ventilation, I read some stuff on filtering using a furnace filter, but in order to filter virus particles you need a very good filter (MERV-13), and almost no older furnace fans are designed for this, so this is a really good way to wreck your fan by making it work too hard. If you went this way, I would just buy a cheap fan from the hardware store and duct tape a MERV-13 filter onto it. Going to be a lot cheaper to replace that fan.

    - **westurner** · [2020-11-18 18:37 UTC](https://news.ycombinator.com/item?id=25140544)
      "Fan control with a Nest thermostat" 
      [https://support.google.com/googlenest/answer/9296419?hl\=en](<https://support.google.com/googlenest/answer/9296419?hl=en>) ^c25140544

      Looks like there could be: (1) an every hour for n minutes schedule; (2) an option to run the fan with the thermostat off; (3) an option to shut off the fan when everyone is gone

- **jonheller** · [2020-11-18 16:26 UTC](https://news.ycombinator.com/item?id=25138646)
  I always assumed running air conditioning with windows open was incredibly wasteful. Is this because Japan's summers are more temperate than where I'm used to (Northeast US)? ^c25138646

  I do find myself sometimes running the AC with windows open when it's cooler outside than indoors. For some reason it can be 65 degrees outside but 75 degrees indoors.

  - **fomine3** · [2020-11-19 03:48 UTC](https://news.ycombinator.com/item?id=25146007)
    It is said by manufacturer like Daikin that stop&start A/C is inefficient than continuously running. (especially on summer, YMMV) ^c25146007

  - **fiddlerwoaroof** · [2020-11-18 16:43 UTC](https://news.ycombinator.com/item?id=25138928)
    Why would it be wasteful? If the house is warmer than the outside air, opening the windows until outside and inside equalize should save a bit of energy. (Assuming that the change to the airflow patterns isn’t relevant) ^c25138928

    - **smegcicle** · [2020-11-18 17:49 UTC](https://news.ycombinator.com/item?id=25139858)
      I have no idea to what degree, but I think humid air reduces the efficiency of AC. ^c25139858

      - **nbutyllithium** · [2020-11-19 02:05 UTC](https://news.ycombinator.com/item?id=25145399)
        A bit of a complicated subject but the short answer is you're correct humidity does reduce the efficiency of air conditioning. ^c25145399

        The reason why(/long answer) is that as it cools the air the humidity in the air (i.e. water vapor) will condense into liquid water. Water requires a fair amount of energy to be removed (known as latent heat) to make this change and none of that energy removed actually changes the temperature of the air (all of it goes into changing the phase of the water). Therefore a high humidity load results in a lot of the cooling potential getting "used" up removing humidity first.

- **turtlebits** · [2020-11-18 17:20 UTC](https://news.ycombinator.com/item?id=25139471)
  Most houses are incredibly leaky/drafty (at least in the US), turning on your bathroom fan(s) a few times a day is an easy way to improve ventilation. ^c25139471

  - **ballenf** · [2020-11-18 17:57 UTC](https://news.ycombinator.com/item?id=25139977)
    Consider replacing the builder grade bathroom fans first, however. The typical ones you'll find are very energy inefficient, intentionally loud, but move relatively little air. They're also probably caked in dust further reducing effectiveness. While you're at it, make sure the fan is not venting into your attic space (I don't think there's any climate where that's still acceptable, but could be wrong). ^c25139977

    - **war1025** · [2020-11-18 18:12 UTC](https://news.ycombinator.com/item?id=25140176)
      \> While you're at it, make sure the fan is not venting into your attic space ^c25140176

      Why wouldn't you vent to the attic?

      Attics are basically "hat that sits on top of your house"

      They are purposefully drafty areas whose main purpose is to keep rain off your ceiling.

      - **tapvt** · [2020-11-18 21:03 UTC](https://news.ycombinator.com/item?id=25142402)
        If the air from within the house is pushed into the attic and that attic is cooler, moisture may condense and collect before being circulated out of the attic space. Could lead to mold issues, etc. ^c25142402

- **bluGill** · [2020-11-18 15:50 UTC](https://news.ycombinator.com/item?id=25138122)
  Only useful if you live in a climate where the outside air is acceptable for indoors. Since this is from Japan I believe that applies.  Where I live the outside temperatures get well below freezing for months at a time so ventilation alone isn't useful ^c25138122

  - **timw4mail** · [2020-11-18 16:13 UTC](https://news.ycombinator.com/item?id=25138461)
    Japan is a very temperate place, but heating is generally not central. Drafts of ventilation would still be cold, but not nearly as wasteful as in a centrally-heating building. ^c25138461

