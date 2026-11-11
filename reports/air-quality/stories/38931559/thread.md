# [Contra Wirecutter on the IKEA air purifier (2022)](https://news.ycombinator.com/item?id=38931559)

Article: [https://dynomight.net/ikea-purifier/](<https://dynomight.net/ikea-purifier/>)

drdeca · 2024-01-09 20:22 UTC · 220 reported comments · archived 2026-11-08 13:27 UTC
Observation: 2026-11-08 13:26 UTC → 2026-11-08 13:27 UTC

## Comments

- **Mister\_Snuggles** · [2024-01-10 21:53 UTC](https://news.ycombinator.com/item?id=38943789)
  I really like this purifier's big brother, the IKEA STARKVIND, which is available in both regular\[0\] and table\[1\] versions. ^c38943789

  The table version is nice because, assuming you place it somewhere you want a table, it takes up no room.  The regular version is awkwardly large, so placement is a bit more of a challenge.

  The killer feature for me is that its air quality measurements and controls are all exposed via Zigbee, and it works very well with Zigbee2MQTT and Home Assistant.

  Related to this, IKEA has recently brought out the VINDSTRYKA\[2\] air quality sensor.  Unfortunately the PM2.5 measurement (as reported by Zigbee2MQTT/Home Assistant) doesn't seem to match up with the same measurement reported by the STARKVIND.  To be fair this is just a feeling, I have NOT conducted head-to-head testing.

  \[0\] [https://www.ikea.com/ca/en/p/starkvind-air-purifier-white-sm...](<https://www.ikea.com/ca/en/p/starkvind-air-purifier-white-smart-00461949/>)

  \[1\] [https://www.ikea.com/ca/en/p/starkvind-table-with-air-purifi...](<https://www.ikea.com/ca/en/p/starkvind-table-with-air-purifier-stained-oak-veneer-white-smart-80461974/>)

  \[2\] [https://www.ikea.com/ca/en/p/vindstyrka-air-quality-sensor-s...](<https://www.ikea.com/ca/en/p/vindstyrka-air-quality-sensor-smart-30498239/>)

  - **liminalsunset** · [2024-01-11 08:19 UTC](https://news.ycombinator.com/item?id=38949288)
    The real "hack" lies in the IKEA STARKVIND air filters. ^c38949288

    They're from a reputable manufacturer, are HEPA filters, and best of all, they only cost \$14.99 CAD (price may vary in your country). This makes them great as \*replacement filters for other air purifiers\*. This is one of the things I love the most about IKEA - hackable IKEA products are available worldwide and can be easily sourced and adapted as "materials" instead of "products".

    The Starkvind air purifier appears to be airflow-constrained on the fan, and not the filters they used. I put its filter (with some cardboard glued to the edges to seal the difference in size) in a Coway Mighty AP-1512HH (often recommended) and have not noticed a huge decrease in airflow at all, even though technically there is less filter area. Based on rudimentary measurements with an anemometer, the airflow is acceptable, and after about a year or more of continuous use, it's lost about 10\% of the airflow after I recently changed it.

    Even better, if you are so inclined, you can buy several STARKVIND filters and cut them to size/merge multiple if your purifier takes different size filters. And if you have a smaller purifier, IKEA also has the FORNUFTIG (thinner) filter for \$7 that you can similarly hack.

    - **sundvor** · [2024-01-11 08:54 UTC](https://news.ycombinator.com/item?id=38949570)
      Starkvind means Strong wind, Fornuftig means Reasonable. ^c38949570

      Got to love their product names, as a Norwegian.

      Meanwhile I have 2x AX90s in my place. Love them! Got the 2nd when I realised the special it was on was not too far from a single filter change, so it'll be fun when they're both up for refresh.

      I'm addition to appreciating clean indoor air, I'm kind of preparing for the next bushfire in Melbourne - can still remember the last one, which was very very bad. I think it might happen next year, and be even worse than last time given current fuel build up. I might check out the IKEA ones to keep the AX90 filters fresh, if the IKEA filters are much cheaper to replace / run on an everyday basis.

      (The Samsung units have an amazing ability to go from a very silent idle to a really bloody high CFM, on auto - currently mainly experienced when cooking).

      Edit: They are stupidly cheap, found the Australian prices! Will definitely pick up a few in due time. [https://www.ikea.com/au/en/cat/air-purifiers-filters-49081/](<https://www.ikea.com/au/en/cat/air-purifiers-filters-49081/>)

    - **l33tman** · [2024-01-11 12:28 UTC](https://news.ycombinator.com/item?id=38951321)
      Hacking them to fit another purifier reminds me of the Apollo 13 incident, which included the astronauts having to do a McGyver hack to fit a square CO2 filter into a socket designed for a round one... using tape, hoses and other plastic items they had lying around :) ^c38951321

    - **unknown** · [2024-01-11 10:14 UTC](https://news.ycombinator.com/item?id=38950206)
      [deleted] ^c38950206

  - **kettleballroll** · [2024-01-11 07:28 UTC](https://news.ycombinator.com/item?id=38948929)
    In terms of air quality sensors, what really made a difference for me was getting a CO2 sensor. "Fresh air" (low CO2) behaves way different than what j was taught. I live in a newly constructed building, which apparently is almost hermetically sealed. And we have no AC, since we're in Europe. As a result, air quality (in terms of co2) goes downhill unexpectedly FAST. And opening the windows for 5 to let in fresh air is definitely not enough to restore quality to sensible levels. EU norms say that public building should have less than 800ppm CO2, as anything above might affect cognitive abilities. However, reaching that level is almost impossible without constantly cracking the window (or an AC). I'd never have expected this.... ^c38948929

    - **BHSPitMonkey** · [2024-01-11 08:21 UTC](https://news.ycombinator.com/item?id=38949302)
      This is one of the reasons why newer, "sealed" buildings need to be mechanically ventilated (ideally with a HRV or ERV to keep your HVAC waste to a minimum). ^c38949302

    - **Gare** · [2024-01-11 07:32 UTC](https://news.ycombinator.com/item?id=38948947)
      Most home AC systems in Europe don't provide fresh air, that's a common misconception. ^c38948947

    - **wayfinder** · [2024-01-11 10:06 UTC](https://news.ycombinator.com/item?id=38950134)
      I own the Aranet4 sensor (highly recommend) and I’m in the US with not particularly great sealing and my sensor will read a 600ppm jump in a matter of 30 minutes. ^c38950134

      I basically have to keep the window in my bedroom open 24/7, even when it’s cold outside, just to keep my CO2 levels in the healthy range otherwise it will be pushing 2000ppm in the morning.

    - **timc3** · [2024-01-11 08:22 UTC](https://news.ycombinator.com/item?id=38949315)
      That really sucks. Sounds like the ventilation system is poorly designed. ^c38949315

      I wish that all modern buildings had properly sized FTX / air handling units. These exchange the old air with new air using the heat from the old to warm up the new air and at the same time can have HEPA filters for cleaning the air.

      - **bborud** · [2024-01-11 09:25 UTC](https://news.ycombinator.com/item?id=38949798)
        Some years ago I ran a department that did a lot of prototyping and research. One of the things we experimented with was CO2 sensors.  Not hugely expensive sensors, but mostly cheap ones since we were mostly interested in relative changes (rather than absolute values) - and seeing what kind of performance you could get out of relatively inexpensive sensors\[1\]. ^c38949798

        (This is from memory)

        We got a lot of interesting results placing sensors in a bunch of commercial buildings. Most rooms in all buildings we measured couldn't keep the CO2 levels below 1000ppm. In fact, most meeting rooms we measured would struggle to keep below 1200-1300ppm when in use and we regularly saw much worse numbers. In one building all meeting rooms we measured would quickly blow past 1200ppm when in use -- except the meeting room management used.  Which tended to hover between 600ppm when not in use and about 800ppm when used (though it was big and rarely more than at 1/4 capacity). I guess that explains why complaints about low air quality fell on deaf ears.

        We also discovered why the meeting rooms in the basement were so awful for late meetings. At around 1800  hours or so in the evening, the HVAC shuts down.  From what I gather, in a tall building, there are supposed to be mechanisms to prevent air from moving back and CO2 dropping down the HVAC system and pooling in the basement.  This one didn't. (In fact, ALL the buildings on the campus had the same problem since they were all built at the same time by the same company).  So over a few hours CO2 levels would rise to a level where the sensors max out their range and get saturated. They would stay that way until a couple of hours after the HVAC got switched on in the morning.

        People would sometimes use those meeting rooms until late in the evening.

        If you use consumer air quality measurement devices, beware that they're not terribly good.  CO2 sensors tend to have cross sensitivity to lots of other gases.  And cheap (eg less than \$400 for just the sensor component) particle sensors tend to be fairly crap.

        A lot of sensors we found in HVAC systems are even lower quality than consumer grade stuff I've seen in products.

        \[1\] The sensors we used are often found in premium consumer air quality measurement products.  So they aren't dirt cheap, but they also aren't that great.

      - **unknown** · [2024-01-11 11:40 UTC](https://news.ycombinator.com/item?id=38950913)
        [deleted] ^c38950913

    - **imp0cat** · [2024-01-11 09:17 UTC](https://news.ycombinator.com/item?id=38949740)
      Seconded. A CO2 sensor is a gentle reminder to open the windows every now and then and get some fresh air in. ^c38949740

  - **mschuster91** · [2024-01-10 23:56 UTC](https://news.ycombinator.com/item?id=38945377)
    \> I really like this purifier's big brother, the IKEA STARKVIND, which is available in both regular\[0\] and table\[1\] versions. ^c38945377

    I got one of these as well, and I recommend them with the extra carbon filter. Very, very nice thing to have in a kitchen, if you're a smoker or if you have cats. The carbon filter takes out *a lot* of nasty smells, enough to not smell anything food-y even in a directly adjacent room while running a frying pan and chopping onions, or when smoking a cigarette on the open window. And the "plain" filter picks up a loooot of the fur that you'd find everywhere including in your food when your cat decides it's time to go and shed everywhere she can.

    - **Doxin** · [2024-01-11 08:13 UTC](https://news.ycombinator.com/item?id=38949244)
      How long do the carbon filters last in your experience? Does it have an indication of when you should? ^c38949244

      - **liminalsunset** · [2024-01-11 08:23 UTC](https://news.ycombinator.com/item?id=38949326)
        The carbon filters in this machine are fairly sparsely filled and don't have a significant amount of carbon in them. Typically replacement is recommended after about 6 months or so, but I've found that with heavy use, similar filters last only a month or so before losing effectiveness. It has to do with how much odor and VOC is present in the area you are using the filter in, as well as how much it is running. ^c38949326

        I made my own filters with over 2-3x the carbon by weight (bought from Amazon) in them, and they last about 2-3 months before they start emitting an odd smell (but they still seem to reduce odor, but they are no doubt trading new smells for older ones as they fill up).

        I usually change the filters as soon as the smell becomes odd, in my case, the smell is like a slightly sour and damp version of the fresh and dry chocolatey smell that they sometimes have when new.

        - **Doxin** · [2024-01-11 09:27 UTC](https://news.ycombinator.com/item?id=38949814)
          Hmm, that'll not work very well for my use-case then. I've not got a great nose, and I would like to keep smells at bay for visitors. Not planning on replacing a filter monthly "just in case" though. ^c38949814

          Thanks for the info!

  - **greggsy** · [2024-01-11 02:41 UTC](https://news.ycombinator.com/item?id=38946787)
    A recent air quality comparison demonstrated that there wild fluctuations across most brands. Nonetheless, I think it’s still helpful to see the changes in the environment, and to understand and observe how leaving a window open, or doing some activity, or handling some volatile substance, or how seasonal dust and pollen can affect hay fever in your own little microcosm. ^c38946787

    - **wkat4242** · [2024-01-11 03:52 UTC](https://news.ycombinator.com/item?id=38947352)
      Yeah I noticed that when I clean my washing basket with a little bit of alcohol the VOC jumps from 200 to 20000 in a matter of minutes and doesn't go back to normal for a day or so. ^c38947352

      Even though I don't even smell it. These sensors are just incredibly sensitive.

      Another example: burning one candle increases PM 2.5 considerably and after blowing it out the wick gives a little wisp of smoke that makes it peak from a normal 1 to 50 or so.

      - **imp0cat** · [2024-01-11 06:22 UTC](https://news.ycombinator.com/item?id=38948493)
        I almost entirely stopped using candles after getting an air purifier with a particle and VOC monitoring sensor (Electrolux/AEG Pure A9). ^c38948493

        It's very enlightening. Even a single push of spray deodorant releases a crazy amount of particles and makes the purifier go crazy for a short while.

        - **bennyg** · [2024-01-11 07:47 UTC](https://news.ycombinator.com/item?id=38949060)
          Is that short burst of deodorant actually harmful or do the numbers just go up a lot? ^c38949060

          - **theshrike79** · [2024-01-11 09:16 UTC](https://news.ycombinator.com/item?id=38949738)
            It measures the amount of particles in the air, it doesn't analyse their content. ^c38949738

            Just having an ultrasonic humidifier in the bedroom makes the PM25 counter jump from 1-2 to 200-250.

            - **amluto** · [2024-01-11 15:11 UTC](https://news.ycombinator.com/item?id=38953212)
              An ultrasonic humidifier turns whatever impure water you feed in into tiny aerosols, from which most of the water quickly evaporates, leaving even smaller aerosols behind. Those likely consist of soluble salts (likely not terribly harmful) and bacteria (possibly quite harmful). ^c38953212

              I would avoid using them unless, perhaps, I ran the output through a filter. Or I would use an evaporative humidifier instead.

              - **leguminous** · [2024-01-11 15:25 UTC](https://news.ycombinator.com/item?id=38953443)
                From the same site as this air purifier article: ^c38953443

                "The case against ultrasonic humidifiers."

                [https://dynomight.net/humidifiers/](<https://dynomight.net/humidifiers/>)

                - **imp0cat** · [2024-01-17 17:00 UTC](https://news.ycombinator.com/item?id=39030338)
                  This! Don't use an ultrasonic humidifier unless you fill it with distilled water. Tap water will just create a ton of white dust everywhere. ^c39030338

                  If you absolutely need more humidity in your home, get something like the Venta LW45 which has a half-submerged rotating disk and blows air over the still wet surface. Works with tap water (requires regular cleaning and a special additive).

            - **unknown** · [2024-01-11 10:45 UTC](https://news.ycombinator.com/item?id=38950453)
              [deleted] ^c38950453

          - **wasmitnetzen** · [2024-01-11 09:26 UTC](https://news.ycombinator.com/item?id=38949804)
            Alcohols are VOC's and many deodorants contain them. They are probably among the less harmful VOC's. ^c38949804

  - **timenova** · [2024-01-10 22:16 UTC](https://news.ycombinator.com/item?id=38944150)
    Where do you keep the air quality sensor? ^c38944150

    I suspect that if you keep it away from the purifier, and closer to where you sit in the room, it's a more real representation of the air quality. Usually the air around the purifier would be purer than other parts of the room until an equilibrium has reached.

    I haven't done extensive testing to validate this theory either, just a hunch. Let me know if my hunch is incorrect.

    - **Mister\_Snuggles** · [2024-01-10 22:39 UTC](https://news.ycombinator.com/item?id=38944455)
      Right now the air quality sensor is in the basement, and the purifiers I'm comparing it to are upstairs.  It's not a fair comparison, it just "seems" to be reporting using a different scale. ^c38944455

      My plan is to put the sensor near one of my STARKVINDs and see how the numbers compare.  This will tell me if they're measuring the same thing and reporting it at the same scale.  Once I understand what the sensor is telling me a bit better, I'll put it in a more useful place.  Your suggestion of putting it closer to where you sit is a very good one.

      - **KennyBlanken** · [2024-01-10 22:53 UTC](https://news.ycombinator.com/item?id=38944629)
        Humidity has a huge effect on the non-lab-grade sensors and that, combined with the fact that upstairs will have all the dander, fabric fibers, etc...of course they're different values. ^c38944629

  - **\_yeiy** · [2024-01-12 00:45 UTC](https://news.ycombinator.com/item?id=38961920)
    Really neat how easy IKEA products data can be gleaned, especially thanks to the online community. ^c38961920

    I wanted to add a screen to the VINDRIKTNING\[0\] air quality sensor, and thanks to an existing project\[1\] I was able get it working\[2\].

    \[0\] [https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor...](<https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor-60515911/>)

    \[1\] [https://github.com/Hypfer/esp8266-vindriktning-particle-sens...](<https://github.com/Hypfer/esp8266-vindriktning-particle-sensor>)

    \[2\] [https://github.com/zvakanaka/vindriktning-oled-no-wifi](<https://github.com/zvakanaka/vindriktning-oled-no-wifi>)

  - **jansan** · [2024-01-11 07:24 UTC](https://news.ycombinator.com/item?id=38948903)
    I do not understand why IKEA makes it so hard to attach a FÖRNUFTIG purifier to a wall or under a table. I bought one to attach it under my son's room table, which fit perfectly, but putting four screw holes into the FÖRNUFTIG was a pain in the ass. It would make those things so much more versatile if scrwholew were already perpared. ^c38948903

    - **Mister\_Snuggles** · [2024-01-11 15:04 UTC](https://news.ycombinator.com/item?id=38953088)
      I'm a bit confused by this comment.  The assembly instructions\[0\] clearly show screw holes on the back of the unit and it appears to even include a template for putting the screw holes into the wall you're mounting it to.  It doesn't look like the holes would be suitable for mounting under a table though, they'd probably prefer that you replace the table with a STARKVIND. ^c38953088

      \[0\] [https://www.ikea.com/ca/en/assembly\_instructions/foernuftig-...](<https://www.ikea.com/ca/en/assembly_instructions/foernuftig-air-purifier-white__AA-2250649-3-100.pdf>)

  - **TylerE** · [2024-01-10 23:49 UTC](https://news.ycombinator.com/item?id=38945316)
    The table version sounded interesting until I looked at the dimensions. 22" is way too low to be useful as anything besides a bedside table. Anywhere slse I'd describe it as more of a tripping hazard. That's lower than the seat height of a lot of chairs. A typical table is more like 30-32". ^c38945316

    - **mschuster91** · [2024-01-10 23:57 UTC](https://news.ycombinator.com/item?id=38945393)
      It makes for a perfect bedside table though, the place where you'd actually want clean air the most. Virtually inaudible in the low speed modes. ^c38945393

      - **Marsymars** · [2024-01-11 02:42 UTC](https://news.ycombinator.com/item?id=38946792)
        I have, unfortunately, found "low speed" mode on air purifiers to be not very effective at improving air quality. ^c38946792

        Measured with an Airthings sensor, in my 1970s house, low-speed mode just clears temporary indoor-source pollutants marginally faster than having no air purifiers. In the case of exterior-source pollutants (i.e. wildfire smoke), low-speed mode is insufficient to keep PM2.5 in an acceptable range.

        And this is with five air purifiers throughout the house that are sized for a significantly larger space.

        - **jfim** · [2024-01-11 03:20 UTC](https://news.ycombinator.com/item?id=38947101)
          This really depends on the rate at which air inside the house gets exchanged with air from the outside. ^c38947101

          In my 2008 house, two air purifiers on low are sufficient to keep AQI at 0 and in the single digits during wildfires. They're rated for about 350 square feet each, while the house is about 1500 square feet.

          - **Marsymars** · [2024-01-11 19:31 UTC](https://news.ycombinator.com/item?id=38957582)
            Yes, completely true - if you had a home with positive pressure and a filtered HRV/ERV with sufficient volume, one wouldn't need internal air purifiers at all. ^c38957582

            I've long wished for "smart" inwards-blowing window fans that took filters and conditionally only turned on when the air outside was an appropriate temperature - wouldn't be appropriate in all climates/seasons/times, but in my geography would pump clean air in into the house for months out of the year.

            [https://naturescoolingsolutions.com/ecobreeze-2-1-smart-wind...](<https://naturescoolingsolutions.com/ecobreeze-2-1-smart-window-fan/>) exists, but is pricey and isn't from a major-enough manufacturer to make me confident of after-sales support.

      - **poulsbohemian** · [2024-01-11 01:52 UTC](https://news.ycombinator.com/item?id=38946389)
        This is to me one of the reasons for CPAP - you get filtered air all night long! ^c38946389

        - **mook** · [2024-01-11 08:02 UTC](https://news.ycombinator.com/item?id=38949179)
          Unless you have a Phillips Respironics, in which case it helpfully adds bits of foam (pre-recall) or formaldehyde (post-recall) to your air stream. I realize that Phillips says it's under limits, but they aren't really trust inducing right now… ^c38949179

        - **TylerE** · [2024-01-11 02:02 UTC](https://news.ycombinator.com/item?id=38946482)
          I do wish the filters were better though, they're really not very good, just basic cellulose. They're mainly to catch big stuff like pet hair. Nowhere near a HEPA. ^c38946482

          - **poulsbohemian** · [2024-01-11 06:10 UTC](https://news.ycombinator.com/item?id=38948413)
            That's a very fair point - I still find that they've made a difference for me, even with the limitations. ^c38948413

            - **TylerE** · [2024-01-11 06:26 UTC](https://news.ycombinator.com/item?id=38948527)
              Yeah, I'm sure they do. I've got so many low-moderate level allergies that it's kinda hard to establish what normal even really feels like. I got a round of shots as a teen that helps, but it's still some level of congestion at the best of times. Actually the biggest difference I found when I first started on it (almost 10 years ago now), besides the obvious sleep stuff, is that the humidifier keeps me from getting nosebleeds about 3 times a week in the winter. ^c38948527

    - **Mister\_Snuggles** · [2024-01-11 00:16 UTC](https://news.ycombinator.com/item?id=38945549)
      I’ve got two of the table version and find the heights to be fine.  The one in my living room, used as an end table, seems to be slightly higher than my non-IKEA end table.  It’s definitely not a table for doing “stuff” (working, eating, etc) at. ^c38945549

      The other one is in my home office and serves mostly as a step to help the cats get to the window, the short height is a definite benefit here!

      - **TylerE** · [2024-01-11 00:32 UTC](https://news.ycombinator.com/item?id=38945707)
        I’ve developed some mobility issues as I’ve gotten older. I’m tall enough/not overly long armed enough that 22” means I can’t pick stuff up off it without having to bend/stoop, which I can do but aren’t ideal. Actually just measures my bedside table and it’s 27” and just about right. 22” would absolutely be too low, putting it about 6 inches below the top of my mattress, which means I can’t see or reach the CPAP machine without basically getting half way out of bed. ^c38945707

        - **wlesieutre** · [2024-01-11 01:35 UTC](https://news.ycombinator.com/item?id=38946265)
          This of course depends on how high your bed frame is, and how thick thick your mattress (and potentially box spring) are. ^c38946265

          22” is pretty typical for an end table next to a sofa. For someone with a relatively low height bed it might make sense as a bedside table too.

    - **kansface** · [2024-01-11 17:56 UTC](https://news.ycombinator.com/item?id=38955917)
      That’s a good height for a desk or dining table.  Coffee tables, end tables, and side tables are commonly much lower.  Very low coffee tables are less than one foot.  Most of my living room is 15-17” for comparison. ^c38955917

  - **KennyBlanken** · [2024-01-10 22:51 UTC](https://news.ycombinator.com/item?id=38944602)
    I don't have the link handy, but many/most of the inexpensive particle sensors are junk in one way or another. They're only good for relative measurements at best. ^c38944602

- **croes** · [2024-01-10 21:34 UTC](https://news.ycombinator.com/item?id=38943539)
  \>So it seems Wirecutter is using “true-HEPA” to mean “H13”. ^c38943539

  \>Except—what’s the logic here? This difference is core to Wirecutter’s dismissal of the IKEA purifier.

  According to this

  [https://en.m.wikipedia.org/wiki/HEPA\#Specifications](<https://en.m.wikipedia.org/wiki/HEPA#Specifications>)

  H13 is HEPA, everything below is EPA. Or simpler, if it starts with an H it's HEPA, if it starts with an E it's EPA.

  - **makomk** · [2024-01-10 22:28 UTC](https://news.ycombinator.com/item?id=38944324)
    Which is a distinction which basically doesn't matter for air purifiers like this one - it's only really relevant to stuff like whole-room positive or negative pressure systems which ensure all of the air goes through the filter. With a standalone air purifier, the main limiting factor is how quickly the room air gets exchanged through the filter. It's pretty much irrelevant whether the filter removes 99.95\% of particles or merely 99.5\% since that's outweighed by all the pollution in air that hasn't been through the filter at all yet. The claims about why true HEPA filters are better are nonsense. ^c38944324

    - **jerlam** · [2024-01-11 00:26 UTC](https://news.ycombinator.com/item?id=38945651)
      As the article says, CADR (Clean Air Delivery Rate) is what matters, not whether the filters are HEPA or not. CADR takes into account both the filter rating and the airflow through the purifier. ^c38945651

      The infamous Corsi–Rosenthal Box uses filters which are far below HEPA standards (MERV-13) but since it's moving so much air, it performs better overall with a higher CADR.

      - **wincy** · [2024-01-11 00:32 UTC](https://news.ycombinator.com/item?id=38945704)
        Haha we bought 4 box fans and buy 4 filters at once at Home Depot, so we get them for half off with a bulk discount. They’ve helped my wife’s asthma substantially. ^c38945704

        - **genewitch** · [2024-01-11 12:32 UTC](https://news.ycombinator.com/item?id=38951369)
          K&N and possibly others make *dense* washable filters - much better than the green or blue style you see at big box stores. You can spray simple green (or another safe cleanser like that) on the back, and then quickly hit it with hot tap water and let it soak. ^c38951369

          20"x20" is \~\$30 iirc. for people interested in this style of filter the fans don't last very long, maybe a year or two. They are \~\$20+ each. I was buying the highest MERV without carbon for a long time, then i switched to carbon and fiber washable ones, then K&N.

          Not an endorsement of K&N in particular, i just know the brand and use them.

    - **santoshalper** · [2024-01-11 00:55 UTC](https://news.ycombinator.com/item?id=38945919)
      Yeah, but in an article this pedantic, you'd expect the author to know something that basic. ^c38945919

      - **rootusrootus** · [2024-01-11 01:06 UTC](https://news.ycombinator.com/item?id=38946039)
        Exactly.  The author of the article uses little details to call into question the Wirecutter write-up, but overlooking something like this does exactly the same thing about their own write-up.  It was the first thing I thought when I saw H13.  "Well, H13 has an H, E12 does not, what are the odds that HEPA starts at 13?"  I'm surprised this didn't occur to the writer. ^c38946039

        - **epcoa** · [2024-01-11 03:15 UTC](https://news.ycombinator.com/item?id=38947063)
          Hardly "little details". They give a fairly broad explanation about the high level flaws in Wirecutter's analysis. The point they make about the issue of marketing speak "true HEPA" is a bit out of place and sort of irrelevant but it isn't even wrong. ^c38947063

          \>  call into question the Wirecutter write-up

          Nothing is being questioned, it is thoroughly debunked.

  - **schiffern** · [2024-01-10 22:21 UTC](https://news.ycombinator.com/item?id=38944228)
    That's the definition for "HEPA," but what IKEA/Wirecutter said is "true-HEPA" which is undefined. Usually "true-HEPA" is just a marketing term used when selling non-HEPA filters. ^c38944228

    I also feel these semantics are evading the real point of the "what's the logic" comment, which was

    \> we are never given a reason why H13 is good enough, but E12 isn’t. Surely it’s not just that higher numbers are better?

    - **wolpoli** · [2024-01-11 00:08 UTC](https://news.ycombinator.com/item?id=38945480)
      \> Usually "true-HEPA" is just a marketing term used when selling non-HEPA filters. ^c38945480

      I don't understand how companies are allowed to add an intensifying or strengthening adjectives to a noun and ends up with a weaken definition of the noun. For example, Full Self Driving is less than Self Driving and now true-HEPA is less than HEPA. Could I advertise that a product as Perfect-HIPPA compliant then?

      - **delecti** · [2024-01-11 00:22 UTC](https://news.ycombinator.com/item?id=38945598)
        Similarly, "genuine leather" is the leather equivalent of American "cheese" (much of which isn't legally cheese). ^c38945598

        - **CharlesW** · [2024-01-11 00:29 UTC](https://news.ycombinator.com/item?id=38945679)
          Another personally-painful example is "podcasting", which Spotify appropriated while creating a closed equivalent of our open web medium. Now everyone's forced to say "standards-based podcasting" or "open podcasting" to use its original meaning. ^c38945679

          - **kelnos** · [2024-01-11 05:12 UTC](https://news.ycombinator.com/item?id=38947978)
            Podcasting is an Apple-created marketing term.  A podcast is just a pre-recorded, audio-only talk show. ^c38947978

            - **rjmunro** · [2024-01-11 12:28 UTC](https://news.ycombinator.com/item?id=38951318)
              No, Apple did not create it, they supported the standard for an RSS feed of audio files that was created by others. It's true that the name is an homage to the iPod, though: [https://en.wikipedia.org/wiki/Podcast\#Etymology](<https://en.wikipedia.org/wiki/Podcast#Etymology>) ^c38951318

          - **somat** · [2024-01-11 04:59 UTC](https://news.ycombinator.com/item?id=38947842)
            On that note WTF even is "podcasting" ^c38947842

            I mean I know what it is. affected apple marketing fluff for "an audio file that is not music.", basically, "we created a category for talk shows on the ipod. and gave it a stupid appleesque name". but i find it weird that people don't just call them talk shows.

            - **krisoft** · [2024-01-11 09:29 UTC](https://news.ycombinator.com/item?id=38949828)
              \> weird that people don't just call them talk shows ^c38949828

              Talk show to me feels like it describes the content and not the format. And the dictionaries I have checked agree: “a radio or television programme on which famous guests are asked questions about themselves, or members of the public discuss a particular subject” (cambridge dictionary)

              Some podcasts are documentaries content wise, some podcasts are newsreels, some are actual play ttrpg, some are radio drama. And yeah, many are indeed talk shows, but that doesn’t mean it is one and the same.

              It kind of like how many TV shows are sitcoms, but not all TV shows are sitcom.

            - **genewitch** · [2024-01-11 12:37 UTC](https://news.ycombinator.com/item?id=38951406)
              podcast is audio files and an RSS/atom feed *somewhere*. That's all that's required. podcasting is what a podcaster who publishes podcasts does. ^c38951406

              the "spec" was made so that itunes - or whatever else - could fetch new content by itself and load it onto your portable music device the next time you synced it with your computer.

              Now it's a push notification on an app on your phone that a new file is available to listen to.

            - **Karliss** · [2024-01-11 09:46 UTC](https://news.ycombinator.com/item?id=38949969)
              I would say important part of podcasts is delivery process. Which at this point due to wide spread of on demand streaming services has somewhat lost many of it's unique features. ^c38949969

              Some years ago if someone said a talk show I would think TV or radio which might be prerecorded but was still broadcasted at specific time.

              Not all podcasts are talk shows. Some podcasts have more of news update format, they are still called podcasts due to technical format, but you wouldn't call them talk shows. There are also more educational podcasts, with single person informing people about some topic that isn't news.

              When podcasts started a distinguishing feature was that you would download them (at time of your chose) and later play them at time of your choice. Another factor is since it isn't radio or TV, medium was a lot more accessible to many creators. This allows creation of much wider variety of shows for niche interests compared to what you would get on TV or radio.

              Now that a lot of media is consumed on demand through various streaming services like Youtube, Netflix, Spotify but TV and Radio usage has significantly decreased that's not unique anymore. Even traditional media companies might be publishing parts of their shows either on their own or existing platforms after the initial broadcast, thus allowing on demand access to their content.

              One more change that has reduced podcast standout features is overall internet speed access. Internet largely has become fast enough that directly streaming audio is easy, there is little need to predownload it. Not only it has become fast, through the mobile networks it's accessible on the go. For a long while even if internet speed was fast enough for audio streaming, mobile internet was quite expensive thus encouraging to download stuff at home for later listening on the go.

              On the topic ease of creation. While there might some podcasts which are now quite popular and the budget that exceeds smaller talk shows on TV and many on radio, the lower bound for podcasts is still much lower. TV and radio has limited broadcast time available, so there will always be some lower bound of budget (depending on size of TV channel) which will likely be above most podcasts (in terms of amount published, not necessary amount of listeners).

              Limited broadcast time has another interesting implication - limits on length. You will unlikely see talk show on TV that's much longer than an 1.5 hours, and anything shorter than 15min will likely be part of bigger show. Podcasts can be as short as 5 minutes (usually for news update style podcasts) and up to 2.5h or longer. Even a single podcast can significantly vary in length between episodes depending on guest, you can't do that on TV or radio where you have specific time slot.

              Names aren't always about content but often also various technical details and loosely defined common properties. Why do we need separate words for CD, vinyl record or Radio, for saying "I was listening a CD", when we could just say listening a song regardless of how it happens. Having more words allows expressing more information. An when you say that you listened a vinyl record that implies a lot more than listening a song.

        - **elicksaur** · [2024-01-11 04:49 UTC](https://news.ycombinator.com/item?id=38947760)
          My typical grocery store these days has ^c38947760

          \- Kraft and maybe a couple other brands of “not cheese” slices and blocks

          \- A larger selection of real cheese blocks and pre-sliced, pre-shredded options (I know dust parm and some shredded have filler that we’d probably also not count as real cheese)

          \- A whole deli counter on the other side of the store of all “real” cheese options.

          Now, maybe consumption is 80\% those Kraft slices, idk the stats, but just in terms of shelf space, it’s like 80-90\% real cheeses.

          - **kelnos** · [2024-01-11 05:11 UTC](https://news.ycombinator.com/item?id=38947968)
            I think the person you're replying to put the quotes in the wrong place.  They weren't talking about all cheese in America, they were talking about a specific product called "American Cheese", which... well, it technically has cheese in it, but some of its components are not-cheese, and it's made in a mass-produced way that turns off many cheese aficionados. ^c38947968

          - **delecti** · [2024-01-11 19:02 UTC](https://news.ycombinator.com/item?id=38957076)
            The other reply was correct. I'm not talking about all cheese in America, I'm talking specifically about the fact that Kraft slices are ostensibly "American cheese", but in reality are not legally "cheese". ^c38957076

        - **lukas099** · [2024-01-11 02:40 UTC](https://news.ycombinator.com/item?id=38946774)
          Why isn't it cheese? That seems like someone redefining cheese to gatekeep it out. ^c38946774

          - **mrguyorama** · [2024-01-11 21:36 UTC](https://news.ycombinator.com/item?id=38959479)
            Everyone trying to add some sort of cheese snobbery but the actual answer is that it legally literally isn't cheese. That's the only reason it is labeled "processed cheese product". It's the same kind of nonsense around "Frozen dairy dessert" instead of something being ice cream. ^c38959479

            Guess what, I KNOW this tub of mostly cookie dough isn't made out of just cream and sugar and cold. I prefer it that way in fact!

            Be assured, Americans buy A LOT of cheese and Wisconsin will have strong words to say if you act like Americans don't "know" cheese

            Give it another decade or so and people will have the same false snobbery around whether their canned alcoholic beverage of choice is a "real seltzer" or a "spiked soda" or....

            It's made out of real cheese though.

            - **lukas099** · [2024-01-14 08:24 UTC](https://news.ycombinator.com/item?id=38988544)
              So it's legally "pasteurized process American cheese". That is still legally cheese. ^c38988544

          - **delecti** · [2024-01-11 17:17 UTC](https://news.ycombinator.com/item?id=38955250)
            In a typical American grocery store, many of the individually wrapped orange slices in the "cheese" section do not legally meet the requirements to be considered cheese. They still have their uses though (it's great for grilled cheese sandwiches, and contains emulsifiers that makes it great in soups or mac & cheese). There's also "American cheese" which *is* cheese, usually along the lines of a very mild cheddar, it's also a totally fine product. ^c38955250

            This goes into detail better than I could without just quoting it: [https://en.wikipedia.org/wiki/American\_cheese\#Regulation](<https://en.wikipedia.org/wiki/American_cheese#Regulation>)

            - **lukas099** · [2024-01-14 08:24 UTC](https://news.ycombinator.com/item?id=38988541)
              To me, the label "pasteurized process American cheese" still says that it's cheese. Just the "pasteurized process American" kind. So it's still legally cheese. ^c38988541

          - **kelnos** · [2024-01-11 05:16 UTC](https://news.ycombinator.com/item?id=38948009)
            Some of it is certainly gatekeeping, but part of it is that it contains components that are definitely not cheese, and it's mass-produced, which turns a lot of people off. ^c38948009

            It's fine as a thing to eat, if it's a flavor and texture you like.  Personally I avoid it, but it's passably ok as a part of a sandwich where there are other flavors around it.  If I just want to eat some cheese (with or without some delivery mechanism like a cracker), American Cheese is the farthest thing from my mind.

            - **epcoa** · [2024-01-11 12:05 UTC](https://news.ycombinator.com/item?id=38951128)
              There's a bit more to it. What most identify as American "Cheese" is the Kraft Single or its equivalent competitors, a product without enough cheese in it (\< 51\%) to even legally label as cheese, and per the FDA at least is not legally "American Cheese". It must be labeled as a cheese "food" or "product". But the branding emphasizes American, Singles, and Calcium, the rest is the fine print. ^c38951128

              There are higher quality actual American Cheeses, that can actually call themselves cheese unqualified, brands such as Kretshcmar, Boar's Head, etc. Kraft does make a somewhat lower end version under the Deli Deluxe label. They are produced from a combination of Cheddar and Colby.

              But its not just gatekeeping there is a wide latitude in the quality and constitution of the various products marketed as "American" cheese ..., some of them don't contain any milk! This type of market segmentation isn't as common with better quality cheese varieties for a number of reasons. At the extreme the "American" label gets put on dollar store imitation "cheese" singles. Whereas I don't know of much imitation provolone sold anywhere.

              And mass-produced has little to do with it. Most deli cheeses are mass produced but people tend to have strong preferences for alternatives to American irrespective.

        - **Marsymars** · [2024-01-11 02:36 UTC](https://news.ycombinator.com/item?id=38946743)
          Hey, American "cheese" and "American cheese" are different things! ^c38946743

          - **genewitch** · [2024-01-11 12:38 UTC](https://news.ycombinator.com/item?id=38951425)
            cheese and cheese food?
            American cheese should just be american cheddar that's been made pliable for easy slicing. I forget the extra step or two, offhand. ^c38951425

            Growing up i always heard "cheese food" isn't cheese, but if it's made from curds and whey...

            - **Marsymars** · [2024-01-11 15:25 UTC](https://news.ycombinator.com/item?id=38953453)
              "American cheese" is specifically a type of processed cheese: [https://en.wikipedia.org/wiki/American\_cheese](<https://en.wikipedia.org/wiki/American_cheese>) ^c38953453

              (I guess "cheese food" as you call it - I'm not familiar with that term, but also not American.)

        - **pbj1968** · [2024-01-11 02:18 UTC](https://news.ycombinator.com/item?id=38946611)
          What’s “legally cheese?” ^c38946611

          - **jeroen** · [2024-01-11 11:40 UTC](https://news.ycombinator.com/item?id=38950923)
            Given that we're talking about the US, this: ^c38950923

            [https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/CFR...](<https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/CFRSearch.cfm?CFRPart=133>)

      - **gumby** · [2024-01-11 01:06 UTC](https://news.ycombinator.com/item?id=38946036)
        It’s like those old “People’s Democratic Republics” which never actually are. ^c38946036

    - **CharlesW** · [2024-01-10 23:24 UTC](https://news.ycombinator.com/item?id=38945045)
      "True HEPA" is an unfortunate side-effect of companies like BlueAIR, which use names like "HEPASilent" to refer to filtration which doesn't meet HEPA requirements. (Note that I'm not saying that HEPASilent is better or worse than HEPA H13, just that the name is designed to obfuscate.) ^c38945045

      Companies need some way to help consumers differentiate filters which meet HEPA requirements from those which don't.

    - **unknown** · [2024-01-10 23:59 UTC](https://news.ycombinator.com/item?id=38945410)
      [deleted] ^c38945410

  - **jerlam** · [2024-01-10 23:06 UTC](https://news.ycombinator.com/item?id=38944802)
    The idea that "only HEPA-rated filters are acceptable" is bonkers and also internally inconsistent. ^c38944802

    Two of their "also great" recommendations are Blueair purifiers, which do not have HEPA-rated filters.

    - **wtallis** · [2024-01-11 00:28 UTC](https://news.ycombinator.com/item?id=38945666)
      Did you mean to imply that Blueair filters as a rule don't have HEPA-rated filters? ^c38945666

      - **stavros** · [2024-01-11 00:56 UTC](https://news.ycombinator.com/item?id=38945937)
        I read the sentence as "their two specific Blueair recommendations don't have HEPA-rated filters". ^c38945937

        - **wtallis** · [2024-01-11 01:17 UTC](https://news.ycombinator.com/item?id=38946115)
          That's what seemed to be the most likely intended meaning, but the comma throws it off. ^c38946115

          - **j33zusjuice** · [2024-01-11 02:08 UTC](https://news.ycombinator.com/item?id=38946522)
            No it doesn’t. The comment’s syntax is correct. Commas before “which,” and not before “that.” 
             [https://www.dictionary.com/e/that-vs-which/\#](<https://www.dictionary.com/e/that-vs-which/>) ^c38946522

            The actual problem is the usage of “which.” If they’re Blueair purifiers that happen to not have HEPA filters, they should have made the clause essential/restrictive. If all Blueair filters lack a HEPA filter, then adding that they don’t have HEPA filters as clarification is non-essential.

            So I understand your confusion, it’s just not for the reason you said it was.

  - **quasse** · [2024-01-10 22:19 UTC](https://news.ycombinator.com/item?id=38944197)
    I came here to say this. For a blog post accusing the Wirecutter of being "rife with factual errors, \[and\] misleading statements" the author could have, ya know, not gotten basic facts wrong about filtering standards? ^c38944197

    Just a few sentences later the author states "This passage implies that a (“true”?) HEPA filter is designed to capture particles that are 0.3 microns or larger. But an H13 filter must, by definition, capture 99.95\% of particles of all sizes."

    This is explicitly wrong! According to the author's own source that they linked above! "HEPA filters, as defined by the United States Department of Energy (DOE) standard adopted by most American industries, remove at least 99.97\% of aerosols 0.3 micrometers (μm) in diameter."

    - **schiffern** · [2024-01-10 22:24 UTC](https://news.ycombinator.com/item?id=38944272)
      99\.95\% is the ISO (international) standard, 99.97\% is the ASME (US) standard. ^c38944272

      [https://www.ossila.com/pages/hepa-filter-size-chart](<https://www.ossila.com/pages/hepa-filter-size-chart>)

    - **ska** · [2024-01-10 22:51 UTC](https://news.ycombinator.com/item?id=38944592)
      Both they and the wirecutter appear to be using the international, not US, HEPA standards. ^c38944592

- **cqqxo4zV46cp** · [2024-01-10 22:25 UTC](https://news.ycombinator.com/item?id=38944285)
  As informative as I’m sure this blog post is, I had to stop reading it a paragraph or two in because its overly aggressive and snarky tone makes it completely unemployable. I am not Wirecutter. I am a nobody reading a blog post. I am not the subject of this ridicule yet I am somehow the recipient of it. If you’ve got a good point to make the proof will be in the pudding without having to be overly vitriolic on the Internet. If there was an iota of intent to have someone at Wirecutter see this, being this aggressive only serves to have them dig their heels in. It’s needlessly emotional and self-indulgent when the subject is…air purifiers? Christ. ^c38944285

  - **atombender** · [2024-01-10 22:42 UTC](https://news.ycombinator.com/item?id=38944497)
    I don't see your criticism at all, and I don't think there's anything aggressive or vitriolic here. ^c38944497

    The article is specifically a rebuttal to a Wirecutter review, so the target audience is really anyone who cares what Wirecutter thinks about purifiers (a lot of people rely on it to guide their buying decisions, after all), and perhaps the staff at Wirecutter.

    I can't speak to the article's technical accuracy, but it appears to do a good job of systematically breaking down their analysis using technical arguments, visualizations, and math.

    - **santoshalper** · [2024-01-11 01:03 UTC](https://news.ycombinator.com/item?id=38946012)
      Really? You don't think there is anything aggressive or vitriolic? ^c38946012

      "Well, perhaps we should, I don’t know, read the IKEA website?"

      "...that totally coincidentally happens to pay affiliate marketing commissions."

      "Maybe we should be generous and ignore all the errors and misstatements above."

      "...then congratulations—you understand air filters better than the Wirecutter."

      - **imajoredinecon** · [2024-01-11 03:23 UTC](https://news.ycombinator.com/item?id=38947125)
        Not to me, no. Snarky, yes; aggressive and vitriolic, no. ^c38947125

      - **yellow\_lead** · [2024-01-11 07:40 UTC](https://news.ycombinator.com/item?id=38948995)
        This is extremely aggressive. I thought the author might jump out from my monitor and attack me after I read such statements. ^c38948995

      - **baq** · [2024-01-11 12:56 UTC](https://news.ycombinator.com/item?id=38951603)
        is it polite? no. ^c38951603

        is it not accurate? also no.

        is it vulgar or offensive? no. unless you get easily offended, in which case you probably shouldn't spend too much time on the internet?

      - **jononomo** · [2024-01-11 11:00 UTC](https://news.ycombinator.com/item?id=38950581)
        This is not aggressive or vitriolic, lol -- this is just a writer with a point of view and a voice. ^c38950581

      - **atombender** · [2024-01-11 10:01 UTC](https://news.ycombinator.com/item?id=38950103)
        Not at all. I just see some mild sarcasm. ^c38950103

  - **hungariantoast** · [2024-01-11 01:19 UTC](https://news.ycombinator.com/item?id=38946144)
    I agree with you completely. This blog post could be useful and informative, but its writing is weirdly aggressive and annoying that it becomes way harder to read rather than just roll my eyes at and move on with my life. ^c38946144

    It's this kind of writing that is unfortunately endemic in the "internet rationalist" space, which doubly unfortunately has a lot of crossover with users on hn. Hence why you're being dogpiled by the most annoying people online.

    More importantly though, writing like this is self-defeating, for the author, for wirecutter, and for everyone else who has to inflict it upon themselves just so the author can get to the point.

    There are much better ways to communicate about issues, about anything, if you're actually interested in helping an organization do better ("Wirecutter, let me help you.") or even just want to inform people that wirecutter might not be the most reliable source for product recommendations.

    This kind of writing though is about the same tier of bad as the loud and annoying youtube takedown videos where they put somebody "on blast". It doesn't surprise me at all that such writing is equally popular on hn. Outrage drives engagement, no matter how far up their own asses your audience is. (Example one: me and my comment).

    \> I am not the subject of this ridicule yet I am somehow the recipient of it.

    This line though is really what I wanted to write a comment about. I love this. Some weirdos will try to twist this feeling into being "personally offended by reading" but no, your feelings are valid. This kind of writing is *exhausting*. It's a waste of my time. The author clearly has a point to make, and everyone would be better served if they would just make it and leave the shitflinging out. Could you imagine having to be around someone who communicated this way irl?

    All that to say, thanks for sharing. I'll take my beating now.

    - **ink\_13** · [2024-01-11 03:15 UTC](https://news.ycombinator.com/item?id=38947061)
      You could tell a rationalist wrote it from the title alone.  No one else writes blog entries titled "Contra X". ^c38947061

    - **unknown** · [2024-01-11 03:24 UTC](https://news.ycombinator.com/item?id=38947129)
      [deleted] ^c38947129

  - **itsgrimetime** · [2024-01-11 04:00 UTC](https://news.ycombinator.com/item?id=38947399)
    I think the snark & combative tone is warranted - the wirecutter used to be a great resource for finding unbiased & thoroughly technical reviews on consumer products. Since they were bought by NYT the review quality has fallen off significantly. I think the writer (and many others) hold some justified resentment toward it now. I can see how some might find that tone to be a turnoff but it seems apt given their history. ^c38947399

  - **wilg** · [2024-01-10 22:31 UTC](https://news.ycombinator.com/item?id=38944353)
    It does include a "\[Content warning: Polemic\]" right up top! Also honestly it's not that spicy. ^c38944353

    \> If there was an iota of intent to have someone at Wirecutter see this, being this aggressive only serves to have them dig their heels in.

    That's their problem, though!

    - **cqqxo4zV46cp** · [2024-01-10 22:40 UTC](https://news.ycombinator.com/item?id=38944468)
      Well…I found it to be?
       One can put as many disclaimers as one wants on something, but Michael Bluth will always be right in being a tad confused as to why there was a dead dove in his fridge. ^c38944468

      - **wilg** · [2024-01-10 22:44 UTC](https://news.ycombinator.com/item?id=38944521)
        Yeah, well, only so much you can do. Tone is subjective. ^c38944521

        - **santoshalper** · [2024-01-11 01:05 UTC](https://news.ycombinator.com/item?id=38946031)
          Not really. How much you care about tone is certainly personal, but it's extremely easy to consistently analyze tone and sentiment from written or spoken text. This stuff is not mysterious. ^c38946031

          - **thaumaturgy** · [2024-01-11 01:59 UTC](https://news.ycombinator.com/item?id=38946441)
            Tone is not subjective? I had no problem with the writing style of the article and wouldn't've even noticed it were it not for this thread. Even after reading the couple of complaints about it, *I* still prefer it to the endlessly dry, academic monotone that HN promotes. ^c38946441

          - **wilg** · [2024-01-11 01:51 UTC](https://news.ycombinator.com/item?id=38946383)
            The conversation is about whether the tone is appropriate, not whether it is parseable. ^c38946383

  - **danfoxley** · [2024-01-11 06:19 UTC](https://news.ycombinator.com/item?id=38948472)
    Wirecutter seems to "lean", where the original site, before NYT purchase, was (much) more balanced. Knowing this, I thought the blog post write-up dove tailed nicely. ^c38948472

  - **TuringNYC** · [2024-01-10 22:48 UTC](https://news.ycombinator.com/item?id=38944557)
    The blog provides good evidence-based snarkiness. ^c38944557

  - **seru** · [2024-01-12 16:00 UTC](https://news.ycombinator.com/item?id=38969640)
    Ahh, you want to kill some content, aye? Lets see, which hatchet will work best - can't immediately find flaws in the logic, so that one's out; same deal with the math. Let's look broader - let's just say, ah, this content may be sensible, useful, it may even be *accurate*, but we'll just accuse it of poor tone - specifically we'll kinda gesture at workplace norms and say that it's *unemployable* (why not add in a bit of implied ad hominem to spice things up?) That'll do the trick\~ ^c38969640

  - **EasyMark** · [2024-01-11 17:33 UTC](https://news.ycombinator.com/item?id=38955537)
    Maybe you can drop the text of the article in chatgpt and tell it to make it less snarky? :) ^c38955537

  - **santoshalper** · [2024-01-11 00:58 UTC](https://news.ycombinator.com/item?id=38945956)
    Yeah, the tone was a huge turnoff for me too. I just kept wondering how one human could care so much about something so trivial. Not even air purifiers themselves, but the fact that wirecutter didn't choose the "right" air purifier from his standpoint. ^c38945956

    - **LeonidasXIV** · [2024-01-11 13:46 UTC](https://news.ycombinator.com/item?id=38952095)
      I don't think it's about just air purifiers. If their air purifier review is so obviously low quality, how do the other reviews fare? Do I need to read a debunking review of Wirecutter recommendations for every category I read? Why read Wirecutter at all then, if they're not trustworthy? Is it actually a review or an ad for the winner of the comparison? ^c38952095

      I think a lot of our mainstream media is so bad because nobody is calling out the shoddy reporting.

      - **wildzzz** · [2024-01-11 18:06 UTC](https://news.ycombinator.com/item?id=38956082)
        I think the fact that their \#1 pick was an affiliate product shows what could really be behind the curtain. Is Wirecutter being paid to bump up their reviews for products or at least being paid to trash other products in comparison? It's like doing a review on a Toyota Corolla while at the same time comparing it to a Mercedes E63 AMG. Yes, I'm sure the Mercedes is better looking, more comfortable, much faster, and can overall out perform the Corolla but it costs 4x as much and cost you much more in gas. If you need the absolute best in performance, buy the AMG. If you just need something to get to work at the best value, buy the Corolla. Just about every shootout-style review worth it's salt will have different categories: best overall laptop, best gaming laptop, best 17in laptop, best compact, and best value. In this case, the IKEA air purifier should have been compared to something of similar price and something of similar performance. As a consumer, I'm interested in those two metrics, either I've got a general idea of how much I'm willing to spend and looking to get the best performance at that price or I'm looking for a certain level of performance due to health issues and want to get the cheapest thing that can do it. Features can come into play but most of these purifiers are dead simple: a fan, a filter, a speed controller, and a timer to change the filter. Obviously Wirecutter can't survive on being totally independent and taking no money from anyone but it is incredibly disingenuous if they are accepting money to promote one product and trash any competition. IKEA is a very popular brand and lots of people are going to be looking at online reviews. Slipping in what could potentially be an advertisement into the review is worthy of involving the FTC if it's not being clearly disclaimed. ^c38956082

  - **physPop** · [2024-01-10 23:31 UTC](https://news.ycombinator.com/item?id=38945119)
    I found it fun to read. Maybe it says something about you that you're personally offended by reading? ^c38945119

- **DannyBee** · [2024-01-10 23:40 UTC](https://news.ycombinator.com/item?id=38945220)
  Filters also have loading specs which seems everyone ignored. ^c38945220

  The guarantee is not that they remove x\% of particles at y size, instantly, but that they settle at that efficiency after z level of loading

  That also likely accounts for differences in some results - nobody seems to have taken this into accounts

  (There are filter rating systems where z\=0, for example n95 filters.  That is rare in HVAC and general air purification though)

- **poidos** · [2024-01-10 21:47 UTC](https://news.ycombinator.com/item?id=38943710)
  After reading this article when it was posted in 2022 and the author's other post on particulates\[0\] I bought the sqair\[1\], which we are very happy with. Allergies and morning congestion are nearly 0 after using it. We live on a very busy road so I run it all the time and with the carbon filter as well. I would like to get a second one eventually -- it only cleans 430 sqft of air and our condo is 730. ^c38943710

  \[0\]: [https://dynomight.net/air/\#things-that-create-particles-indo...](<https://dynomight.net/air/#things-that-create-particles-indoors>)

  \[1\]: [https://smartairfilters.com/en/product/sqair-air-purifier/](<https://smartairfilters.com/en/product/sqair-air-purifier/>)

  - **mac-mc** · [2024-01-10 23:46 UTC](https://news.ycombinator.com/item?id=38945280)
    An issue I've found is outdoor air ventilation vs. air filtration vs. humidity management is a tricky thing to balance overall when you don't have a central HVAC system with an ERV installed, especially when you live near a busy road or have allergy issues.  If you add a CO2 monitor to your air monitoring, you'll start to see where this becomes a hard thing to balance without a large ERV or other specialized ventilation systems. ^c38945280

    On top of that, living near a highway might not show issues on your PM2.5 / PM10 monitor, but it still shows in health statistics according to studies.

    - **7thaccount** · [2024-01-11 03:52 UTC](https://news.ycombinator.com/item?id=38947351)
      I assume it shows up on health statistics because virtually nobody has multiple MRV13 filters in their house running all day. They probably don't even have a decent air filter for their homes AC. ^c38947351

    - **christiangenco** · [2024-01-11 07:45 UTC](https://news.ycombinator.com/item?id=38949038)
      ERVs are crucial for keeping CO2 and VOCs low. You can install one in a window! [https://gen.co/air](<https://gen.co/air>) ^c38949038

  - **gniv** · [2024-01-11 07:29 UTC](https://news.ycombinator.com/item?id=38948934)
    After reading all this talk about HEPA filters and 99.95\% vs 99.5\%, it's funny to read on that Sqair page "H12 HEPA (99.5\%)". There's no such thing as H12 according to that wikipedia page for HEPA standards. ^c38948934

- **timenova** · [2024-01-10 22:14 UTC](https://news.ycombinator.com/item?id=38944120)
  I bought this air purifier after reading this article and researching more. The biggest advantage of this air purifier compared to others on the market is its cost of replacing the air filter. It's significantly cheaper than others. ^c38944120

  I stay in a city with considerably high air pollution 2/3rds of the year, and this has done a wonderful job of cleaning the air.

  Plus, Ikea sells a tiny air quality sensor separately, so you can measure the quality of the air near where you're sitting, not where the purifier is.

- **thadk** · [2024-01-10 22:02 UTC](https://news.ycombinator.com/item?id=38943948)
  I owned that IKEA purifier and it didn't clear the dust sufficiently for my dust mite allergy compared to similarly sized Coway filters. Also it wasn't as straightforward to clean off large pre-filtered dust particles. Avoid. ^c38943948

  Maybe try the STARKVIND one instead.

  - **amluto** · [2024-01-11 15:37 UTC](https://news.ycombinator.com/item?id=38953638)
    Dust mite allergens are *huge* compared to all the PM2.5 crud that air filters mostly worry about. Almost any filter will remove dust mite allergens that actually get in the filter. ^c38953638

    Try the usual low-tech stuff: wash bedding in hot water. Encase your mattress and pillows in appropriate material (very fine mesh or a membrane — there are products sold for this exact purpose, and mattress spill protectors work too).  Wash those protectors occasionally in hot water as well.

    Fit a HEPA filter on your vacuum and vacuum regularly.  Wear a mask while cleaning.

    Also, dust mites need quite high relative humidity to grow and moderately high RH to even survive.  This is relative humidity *where the dust mites are*.  So if you can arrange to keep any rugs and carpets that you have warm, they will have lower RH and fewer dust mites.

    - **thadk** · [2024-01-11 19:29 UTC](https://news.ycombinator.com/item?id=38957534)
      The original article's unit flow rate must have been underpowered then. Or the filter had insufficient holding capacity before passing the dust mite allergen particles back into the air. It never seemed to catch enough of what it passed through. Regardless, it was completely insufficient for the palpable relief I was accustomed to. ^c38957534

      I use the Wirecutter's Coway unit recommendation mostly. I have not tried the larger IKEA unit but at least it seemed to mitigate the above.

      Good notes, thanks for sharing, I do already take those precautions, mop weekly, no rugs, prefer ample fresh air (ERV or window), and now mostly rely on HEPA filters for extra relief during exercise (kicked up dust), when I'm struggling, or in pollen season. The new nasal azelastine antihistamine also helpful.

      Even true HEPA filters can also get inundated a bit too quickly (1-5 mo) in my house otherwise and if I don't notice that, it's worse than nothing. So excepting pollen season, fresh air has a better failure mode.

      To affect relative humidity to \<50\% for mites, unfortunately as far as I can tell, high humidity requires kilowatts of electricity to drop in older buildings in rainy climates, esp. without sealing and compromising air quality in other ways (CO2 too).

      - **amluto** · [2024-01-11 20:36 UTC](https://news.ycombinator.com/item?id=38958636)
        No ordinary filter should pass dust mite allergens (or pretty much any particle) just because it’s overloaded. Electrostatic precipitators will, but those are essentially worthless for residential applications. ^c38958636

        Maybe the Coway throws the filtered air in a more useful place for your use case?

        (Also, and this is utterly silly but I’ve gotten this wrong myself: the IKEA filters come with a plastic wrap on the filter. You need to open it up and remove the plastic.  If you skip this step, you have a somewhat noisier than expected think that looks like a filter but provides no filtration whatsoever.  Whoops.)

        P.S. Azelastine is not new at all. What is new is “Astepro”, which is the same thing, plus sucralose, and it’s OTC.  The version without sucralose can be purchased pretty much anywhere in the US with a prescription, as a generic or a name brand product.

  - **Toutouxc** · [2024-01-11 08:01 UTC](https://news.ycombinator.com/item?id=38949174)
    I don’t understand, the cheaper IKEA purifier (FÖRNUFTIG) uses its entire front side, covered with fabric, as the pre-filter. To clean it, you stop the purifier and vacuum clean the front side, which takes 15 seconds. ^c38949174

    The more expensive round one (STARKVIND) doesn’t use its fabric covered front as the pre-filter (it’s actually solid) and instead has a separate fine mesh (not that fine though) layer underneath. To clean that, you have to take the front side off first, which takes a bit longer.

    - **thadk** · [2024-01-11 19:30 UTC](https://news.ycombinator.com/item?id=38957560)
      Thanks, see the sibling comment response below. I use the Wirecutter's Coway unit recommendation mostly. I have not tried the larger IKEA unit but at least it seemed to mitigate what I mention there. I did try washing the article's unit "prefilter" but it didn't seem to catch anything vs. the Coway. ^c38957560

- **chpatrick** · [2024-01-10 22:17 UTC](https://news.ycombinator.com/item?id=38944165)
  The only people I trust for recommendations nowadays are obsessive specialist subreddits and Stiftung Warentest. ^c38944165

  I haven't trusted Wirecutter since they were offering recommendations for kickbacks.

  - **crazygringo** · [2024-01-10 23:33 UTC](https://news.ycombinator.com/item?id=38945141)
    \> *I haven't trusted Wirecutter since they were offering recommendations for kickbacks.* ^c38945141

    Do you have a source for that? I don't think that's ever been true.

    They've always had affiliate links, but they've also always been clear that doesn't affect their recommendations.

    You might be referring to this: [https://www.xdesk.com/wirecutter-standing-desk-review-pay-to...](<https://www.xdesk.com/wirecutter-standing-desk-review-pay-to-play-model>)

    But it was pretty totally debunked. The NYT made a lengthy reply explaining:

    [https://www.nytimes.com/wirecutter/our-response-to-nextdesk/](<https://www.nytimes.com/wirecutter/our-response-to-nextdesk/>)

    - **annexrichmond** · [2024-01-11 00:41 UTC](https://news.ycombinator.com/item?id=38945781)
      It may or may not affect their recommendation, but it may affect what products they review in the first place.  So instead of the "The Best TV you can buy", it's more like "The Best TV you can buy from a company with an affiliate program" ^c38945781

    - **chpatrick** · [2024-01-11 00:32 UTC](https://news.ycombinator.com/item?id=38945711)
      Can you call it a debunking when it's written by the accused? ^c38945711

      That reply just says "no we don't, trust me bro".

      - **crazygringo** · [2024-01-11 00:44 UTC](https://news.ycombinator.com/item?id=38945805)
        The reply says a *ton* more than that. It goes into quite a lot of detail. ^c38945805

        Of course you're free to come to whatever conclusion you want. But I don't really know what more you could ask for.

        - **chpatrick** · [2024-01-11 00:53 UTC](https://news.ycombinator.com/item?id=38945895)
          I think the very fact that the CEO of a review site contacted the makers of a reviewed product and asked for money is bad enough. ^c38945895

          - **SamBam** · [2024-01-11 03:06 UTC](https://news.ycombinator.com/item?id=38946985)
            They asked if they have an affiliate program, or were willing to set one up. ^c38946985

            That's the standard business arrangement for almost any review site. It's how they pay their reviewers.

            When nextdesk said no, they still kept it as their recommended desk for a year, and then, when they switched it, they switched to one that *also* didn't have an affiliate program, and still kept nextdesk as the "upgrade" pick.

            It's really hard to see *any* evidence that the money affected their editorial decisions.

          - **metadaemon** · [2024-01-11 01:50 UTC](https://news.ycombinator.com/item?id=38946373)
            As someone who had zero knowledge of this and isn't trying to be snarky, do you have a link to that? I searched around and found some stuff, but it's pretty old. ^c38946373

            - **chpatrick** · [2024-01-11 02:55 UTC](https://news.ycombinator.com/item?id=38946903)
              The same thing linked above: ^c38946903

              [https://www.xdesk.com/wirecutter-standing-desk-review-pay-to...](<https://www.xdesk.com/wirecutter-standing-desk-review-pay-to-play-model>)

              - **d3w4s9** · [2024-01-11 05:11 UTC](https://news.ycombinator.com/item?id=38947967)
                I don't know what you are trying to argue but the facts are abundantly clear about what happened -- 1, nytimes/wirecutter did f\*ck up the whole thing -- The editorial team and the business team weren't on the same page 2, despite all that happened, editorial team acted independently and their pick still stood. If you don't trust their editorial independence, you shouldn't trust any other review by another publication or random Internet user either. ^c38947967

                - **chpatrick** · [2024-01-11 10:57 UTC](https://news.ycombinator.com/item?id=38950557)
                  That's just what I said though. I trust a non-profit publication that does reviews as a public service (Stiftung Warentest), and I trust random internet users who just want the best product with no skin in the game (Reddit). ^c38950557

                  I don't trust for-profit review sites that have a financial incentive to pick one product over the other, like Wirecutter.

  - **KennyBlanken** · [2024-01-10 22:55 UTC](https://news.ycombinator.com/item?id=38944656)
    90\% of the stuff written is just utter trash. ^c38944656

    I'm not joking when I say the hairdryer article amounted to "trust this person because she's used hair dryers for a long time."

    She was measuring airflow speed out of the hair dryers but not volume. Absolute moron.

    - **sushid** · [2024-01-11 00:24 UTC](https://news.ycombinator.com/item?id=38945623)
      That's the impression I get from Wirecutter. They're not unethical per se, but these reviewers appear to have picked up a task from their long list of products to reviews and have done the bare minimum at best. ^c38945623

    - **somat** · [2024-01-11 06:48 UTC](https://news.ycombinator.com/item?id=38948681)
      I am not really arguing as you are correct about the low quality, however, that is how you measure air volume. Measure the air speed and multiply it by vent area. Hopefully(i doubt it) they included how big the vent was. ^c38948681

      Additionally. I am a bit weak on my physics but I think air speed has a direct relationship with evaporating liquids. I would have to see some controlled tests. but hypothesis: given the same volume of air per minute. a higher speed will evaporate water faster, with specific testing on high surface area targets(like hair) for example: them stupid dyson dryers that project a super high speed low area stream of air

    - **annexrichmond** · [2024-01-11 00:39 UTC](https://news.ycombinator.com/item?id=38945764)
      And now they want you to be subscriber for their trash content that likely only reviews products from companies with affiliate programs ^c38945764

  - **progbits** · [2024-01-10 23:19 UTC](https://news.ycombinator.com/item?id=38944987)
    Unfortunately many subreddits are already being targeted with astroturfing. It still works for niche things but be careful and review the account age and posting history of those who praise a product. ^c38944987

  - **LeanderK** · [2024-01-10 22:56 UTC](https://news.ycombinator.com/item?id=38944678)
    \> Stiftung Warentest ^c38944678

    does something like this exist outside of germany? Having a Stiftung Warentest subscription always strikes me particularly german.

    - **Tijdreiziger** · [2024-01-10 23:13 UTC](https://news.ycombinator.com/item?id=38944906)
      [https://en.wikipedia.org/wiki/The\_European\_Consumer\_Organisa...](<https://en.wikipedia.org/wiki/The_European_Consumer_Organisation#Members>) ^c38944906

    - **haizhung** · [2024-01-11 07:40 UTC](https://news.ycombinator.com/item?id=38948996)
      On the one hand, yes. ^c38948996

      On the other hand, if you want unbiased, quasi-scientific tests, who is gonna pay for it?

      It is actually in your best interest if YOU are paying for it, since then you are the customer and not the product.

      That said, it isn’t even that expensive. When I buy a washing machine, I just buy the Warentest article on washing machines first which makes the overall purchase, like, 0.5\% more expensive.

      - **epups** · [2024-01-11 08:16 UTC](https://news.ycombinator.com/item?id=38949264)
        I think the problem for people who are not in Germany is that manufacturers often release different versions for each market. So, for example, you might find that \>50\% of the models being tested by Stiftung Warentest exist only in Germany or other parts of Western Europe. ^c38949264

    - **LeonidasXIV** · [2024-01-11 13:51 UTC](https://news.ycombinator.com/item?id=38952143)
      Tænk\[1\] in Denmark is a bit like that, which is not surprising given their customer is the consumer, not the advertiser. However they're not quite as much of an institution as Stiftung Warentest is in Germany. ^c38952143

      \[1\]: [https://taenk.dk/](<https://taenk.dk/>)

    - **odiroot** · [2024-01-11 11:51 UTC](https://news.ycombinator.com/item?id=38951021)
      Which? in UK is sorta like it. ^c38951021

  - **thaumaturgy** · [2024-01-11 02:07 UTC](https://news.ycombinator.com/item?id=38946518)
    You might be thinking about Wirecutter pre- and post-NYTimes acquisition, although it's a bit more complicated than that: [https://archive.is/5JDw0](<https://archive.is/5JDw0>) ^c38946518

    (I also like Project Farm, although I don't think of them as comprehensive.)

- **js2** · [2024-01-09 22:38 UTC](https://news.ycombinator.com/item?id=38933287)
  Previous discussion (1474 points by Ariarule on June 20, 2022 \| 708 comments): ^c38933287

  [https://news.ycombinator.com/item?id\=31812259](<https://news.ycombinator.com/item?id=31812259>)

- **grobbyy** · [2024-01-09 22:15 UTC](https://news.ycombinator.com/item?id=38933012)
  My experience is Wirecutter recommended process products most of the time, and isn't very clueful in how it evaluates them. It's that's Sharper Image vibe. ^c38933012

  Best air filter would use standard home furnace filters. Those are cheap and good enough. Most of the money should be on the fan. High efficieny, high load, low noise fans are expensive.

  - **hyperbovine** · [2024-01-10 21:54 UTC](https://news.ycombinator.com/item?id=38943819)
    The Wirecutter model is to take what Consumer Reports reports used to do and eliminate all the hard parts like actually learning the science behind the product, performing serious long-term evaluations, and building funky stress testing machines. (And the big one, not accepting advertiser dollars.) ^c38943819

    What's left? Some underqualified millenials doing a bunch of Googling, buying some products off Amazon, chatting about them on a Slack thread, and then summarizing all the anecdata using no fewer than 10000 referral-generating words.

    Suffice it to say I find their recommendations basically useless. And in several cases aggressively wrong, like they recommend a product I know from personal experience to be among the worst in its category.

    - **TylerE** · [2024-01-10 22:02 UTC](https://news.ycombinator.com/item?id=38943944)
      You've got people like Project Farm over on YT. He does really good, rigourous stuff. He did a test on wiper blades where tested them new, then left them on the roof of his house in the sun for a full year, and then did all the tests again. He also rarely states firm conclusions, just presents objective data. The only real exception is when one, or a few products standout as either exceptionally good (especially when they're NOT the most expensive) or they do so poorly as to be totally unfit for purpose or even unsafe. ^c38943944

      The products he reviews tend to be sort of workshop oriented (tools - from basic open end wrenches up to fairly capable welders and chainsaws, lubricants, that kind of thing), but he's also done a fair bit of automotive stuff, jeans, gloves, and things like that.'

      For the jeans, he tested stuff like puncture force (with a nail), abrasion resistance, belt loop strength, and breathability. He also commented on but did not score fit and comfort.

      - **bombcar** · [2024-01-10 22:25 UTC](https://news.ycombinator.com/item?id=38944284)
        Project Farm is good, but it's still mostly entertainment. You have to know how to filter out the things that matter versus the things that are more just for amusement, and whether the stated test is a "good test". ^c38944284

        A more scientific (but more limited) would be Torque Test: [https://www.youtube.com/watch?v\=JKXuFwB6lo0](<https://www.youtube.com/watch?v=JKXuFwB6lo0>) and even they're mainly for entertainment.

        - **TylerE** · [2024-01-11 03:03 UTC](https://news.ycombinator.com/item?id=38946961)
          I consider that a feature, not a bug. Different people have different priorities. That's part of what went wrong with Consumer Reports... they started leaning too much on sort of softer things like "noise" and "vibration" and gimmicky features with limited utility, while deemphasizing wether the thing is worth a damn at the task it's supposed to do in the first place. ^c38946961

      - **83** · [2024-01-10 22:28 UTC](https://news.ycombinator.com/item?id=38944319)
        I really appreciate Project Farm's reviews, and regularly watch them, but I often wish he had more of an engineering background.  Some of the tests he comes up with fall in the worthless to downright misleading category. Not a lot of them, but enough that I wish there were someone more rigorous making these videos. ^c38944319

    - **ska** · [2024-01-10 22:58 UTC](https://news.ycombinator.com/item?id=38944704)
      \> Suffice it to say I find their recommendations basically useless. ^c38944704

      This is a are in general that has become pretty useless over the last years - the shills have won out.  I'd go so far as to say that on average the first few pages of any web search for product advice result in negative value overall.

- **heeen2** · [2024-01-11 08:42 UTC](https://news.ycombinator.com/item?id=38949473)
  I don't really care about airborne germs, spores or exhaust particulates, but our basement collects a TON of dust that looks like dryer lint and requires a daily sweep with a vacuum cleaner. I wonder if the ikea and similar air purifiers are overkill for that and if there's a solution that is more effective for this kind of dust but with less noise/less power. ^c38949473

  - **callalex** · [2024-01-11 09:14 UTC](https://news.ycombinator.com/item?id=38949716)
    A box fan with the cheapest furnace filter you can find at the hardware store. Just one on its lowest setting will handle large particulates in a  basement. If that’s inadequate, since you mentioned noise as a concern, two box fans with filters on low is better than one box fan with a filter on medium, and filters even more air. ^c38949716

    Edit: if you really are cleaning DAILY then there is something else wrong that really should be addressed. Either a clogged dryer vent, a horribly leaky HVAC system, or a completely failed building seal somewhere. The filters will certainly solve your problem but even with the cheap stuff you will be going through a lot of filters if you don’t solve the underlying issue.

  - **Doxin** · [2024-01-12 07:59 UTC](https://news.ycombinator.com/item?id=38965347)
    You might want to check the relative humidity in your basement. Mold can create a rather silly quantity of spores if left unchecked. ^c38965347

- **free\_bip** · [2024-01-09 21:33 UTC](https://news.ycombinator.com/item?id=38932414)
  What's funny is this article is a much better advertisement for IKEA air filters than IKEA themselves do... ^c38932414

  - **bacheaul** · [2024-01-10 22:24 UTC](https://news.ycombinator.com/item?id=38944271)
    Yep, we actually bought a bunch for our house after reading this article. Bang for buck for the device, filters, and power usage is difficult to beat. ^c38944271

- **unknown** · [2024-01-10 21:10 UTC](https://news.ycombinator.com/item?id=38943193)
  [deleted] ^c38943193

- **quickthrower2** · [2024-01-11 02:02 UTC](https://news.ycombinator.com/item?id=38946483)
  I didn't know this much about filters before. ^c38946483

  Let's look at 2 situations.

  One is you are running the same air through the filter all day.

  The other is you are using a vacuum cleaner that is sucking up dust from the floor and pumping out that air.

  I assume in the vacuum cleaner case, you are better off with a higher performing filter since you need to trap that dust on first pass through, whereas with the filter that is circulating the air all day, you get a "second chance" to capture a given particle?

- **whazor** · [2024-01-10 22:36 UTC](https://news.ycombinator.com/item?id=38944419)
  The cheap IKEA air purifier has another huge benefit: you can control it with a smart socket. So hook it up to a tasmota smart plug and you will have a smart purifier. ^c38944419

  - **mgradowski** · [2024-01-10 23:58 UTC](https://news.ycombinator.com/item?id=38945403)
    UNIX philosophy is alive and well. ^c38945403

  - **ska** · [2024-01-10 22:52 UTC](https://news.ycombinator.com/item?id=38944617)
    From this thread, the bigger IKEA one seems to have smarts built in. ^c38944617

    - **Toutouxc** · [2024-01-11 08:21 UTC](https://news.ycombinator.com/item?id=38949310)
      It does and it works great, but it’s about twice as expensive. The cheaper one, on the other hand, has zero smart features, and the only dial on the top directly controls the speed of the fan, with nice mechanical steps. So you can preselect the speed and then cut power as needed with your smart outlet. That’s, unfortunately, not the norm anymore. My cheap dehumidifier has no smart features, but is sufficiently complicated with its programs and buttons that it resets after a power cut. ^c38949310

- **brunoqc** · [2024-01-10 21:41 UTC](https://news.ycombinator.com/item?id=38943618)
  How good is to tape a hepa filter to a box fan? I think I recall a marketplace episode where a scientific or whatever said that it was better than some shitty products and good enough for the small price. ^c38943618

  - **KennyBlanken** · [2024-01-10 23:17 UTC](https://news.ycombinator.com/item?id=38944961)
    Box fans have very low static pressure so airflow drops, very rapidly, as the filter starts to accumulate dust and its resistance to airflow goes up. ^c38944961

    This is mitigated by using four filters - constructing a frame that holds them top and sides - and the box fan goes on the bottom, with legs to hold it off the floor.

    Box fans are also very noisy. The box-fan design was intended mostly for people in wildfire areas who needed something to mitigate smoke inside their homes.

  - **londons\_explore** · [2024-01-10 21:49 UTC](https://news.ycombinator.com/item?id=38943728)
    For PM10/PM2.5, it's very good.      Most filters and box fans are oversize for even a large house - you can typically get away with a CPU fan and much smaller filter and still have it clear the air to pretty much zzero PM2.5 in a few hours. ^c38943728

    Probably minimal impact on other pollutants (VOC's, NOX, CO, etc)...   Many professional air purifiers don't make any claims about those either tho.

  - **Bloating** · [2024-01-11 00:09 UTC](https://news.ycombinator.com/item?id=38945491)
    I made these for
    1) for a post construction clean-up project - lost of dust getting kicked around. Worked like a charm
    2) wildfire smoke - Happened to have the material from 1, & it did seem to help ^c38945491

    The trick is that the box fan turns over the air much faster than a conventional hepa.

    [https://aghealth.ucdavis.edu/news/corsi-rosenthal-box-diy-bo...](<https://aghealth.ucdavis.edu/news/corsi-rosenthal-box-diy-box-fan-air-filter-covid-19-and-wildfire-smoke>)

    Still, \$10 for the ikea filter seems like a good deal if you get good life out of it. 20x20x2 at filterbuy is about \$16.5 x4.

  - **AlexErrant** · [2024-01-11 00:32 UTC](https://news.ycombinator.com/item?id=38945709)
    Let me introduce you to a YouTube channel all about DIY air filters [https://www.youtube.com/watch?v\=XAJ\_\_E-hIJc](<https://www.youtube.com/watch?v=XAJ__E-hIJc>) ^c38945709

  - **ska** · [2024-01-10 22:38 UTC](https://news.ycombinator.com/item?id=38944444)
    For home use it should work fine, after all it's functionally basically what most of the systems, especially the cheaper ones, are.  Especially if you add a pre-filter of some sort. ^c38944444

    The main downsides are comparatively ugly and noisy.

  - **thaumasiotes** · [2024-01-10 21:56 UTC](https://news.ycombinator.com/item?id=38943847)
    [https://smartairfilters.com/en/product/diy-1-1-air-purifier/](<https://smartairfilters.com/en/product/diy-1-1-air-purifier/>) ^c38943847

  - **unknown** · [2024-01-10 22:42 UTC](https://news.ycombinator.com/item?id=38944488)
    [deleted] ^c38944488

- **0x53** · [2024-01-11 05:36 UTC](https://news.ycombinator.com/item?id=38948179)
  My wire cutter disagreement is their flashlight recommendation. They recommend a AA battery flashlight from Amazon that in my opinion is terrible ([https://www.nytimes.com/wirecutter/reviews/best-flashlight/](<https://www.nytimes.com/wirecutter/reviews/best-flashlight/>)). This article indicates that maybe the referral money is a factor. I wonder how much influence that has. ^c38948179

- **kwertyoowiyop** · [2024-01-09 23:45 UTC](https://news.ycombinator.com/item?id=38934031)
  Seems like the author knows their stuff,  but I’d trust it even more without the snarky tone. ^c38934031

  - **santoshalper** · [2024-01-11 01:07 UTC](https://news.ycombinator.com/item?id=38946045)
    I wouldn't be an annoyed as he is if I had personally designed the IKEA air purifier. ^c38946045

- **tptacek** · [2024-01-11 00:55 UTC](https://news.ycombinator.com/item?id=38945923)
  Fun sequence of posts from the same author: ^c38945923

  [https://dynomight.net/thanks-3/](<https://dynomight.net/thanks-3/>)

- **jofla\_net** · [2024-01-10 21:16 UTC](https://news.ycombinator.com/item?id=38943281)
  what i like about the ikea model featured here is the size, can fit almost anywhere.
  I also bought several to replace a couple 20 year old foot-stool size units. ^c38943281

  Yes its not a rolls royce, but it gets \%85 the way there.

  - **Kon-Peki** · [2024-01-10 22:05 UTC](https://news.ycombinator.com/item?id=38943981)
    If it were like a Rolls Royce, the spec sheet would simply say "Performance: Adequate" ^c38943981

- **BarbaryCoast** · [2024-01-11 06:53 UTC](https://news.ycombinator.com/item?id=38948703)
  Most of this guy's questions could have been answered by reading the very Wikipedia article he cites.  For example, "a HEPA air filter must remove—from the air that passes through—at least 99.95\% (ISO, European Standard) or 99.97\% (ASME, U.S. DOE) of particles whose diameter is equal to 0.3 μm".  So, yes the H13 filter meets this spec (99.95\%), and the E12 does not.  If he didn't trust the Wikipedia authors, he could always follow their references to check for himself. ^c38948703

  The question of whether H13 vs E12 actually matters is likely to depend on application and environment.  Providing factual information, perhaps taking the position that the IKEA filter is "good enough" despite the review, would have been welcome.  Then each reader can evaluate all those factors for themselves.

  Whenever I checked his quotes from The Wirecutter, I found that WC had it right, and blogger had it wrong.  I stopped reading in detail after the first two sections, then just skimmed the rest.

- **rapind** · [2024-01-11 01:55 UTC](https://news.ycombinator.com/item?id=38946409)
  If you don’t care about looks, grab yourself four 20x20x2” furnace filters of your preferred rating (merv 13), a 20” box fan for \$20 and some duct tape. Assemble into a cube with the fan on top and filters on the sides. Add a cardboard cutout to the bottom if you want. Make sure you orient the fan and filters so that airflow comes into the filters (sucked) and out through the fan. Replace filters every year or less if you use it constantly. ^c38946409

- **genman** · [2024-01-09 23:38 UTC](https://news.ycombinator.com/item?id=38933975)
  Go with the one that has lower actual operating noise levels. ^c38933975

  - **Toutouxc** · [2024-01-10 21:27 UTC](https://news.ycombinator.com/item?id=38943419)
    The IKEA one has three power levels, the first one is virtually inaudible, the second one hard to ignore even just being in the room during the day, the third one is really loud. Very good purifier though, looks nice, filters well. They even have a more expensive model that has Zigbee and integrates with Home Assistant. ^c38943419

    - **firecall** · [2024-01-10 22:45 UTC](https://news.ycombinator.com/item?id=38944534)
      Yes, I have the IKEA STARKVIND Table and 100\% agree with that. ^c38944534

      I hate fan noise!

      Even in my computers. As I get older the more I'm irritated by fan noise.

      I cant run the IKEA on anything by the first setting without wearing noise cancelling headphones.

      The loudness level and tone of the fan is horrible!

      I'd pay more for an air filter with fans that were less obnoxious! :-)

      - **elabajaba** · [2024-01-11 06:54 UTC](https://news.ycombinator.com/item?id=38948709)
        I also hate fan noise and ended up DIYing an air purifier with computer fans as you end up with a much quieter air purifier than commercial offerings for a given CADR. If you're going this route I suggest paying a bit more and getting the noctua pwm adapter ([https://noctua.at/en/products/accessories/na-fc1](<https://noctua.at/en/products/accessories/na-fc1>)) so you can control the fan speed, and designing it (or using an existing design, see [https://www.cleanairkits.com/products/fanless-kits](<https://www.cleanairkits.com/products/fanless-kits>) and [https://www.reddit.com/r/crboxes/](<https://www.reddit.com/r/crboxes/>) for inspiration) built around filters you can pick up locally. (I built mine around ikea starkvind filters, but in Canada I've never been able to get them shipped online, and the nearest ikea is annoyingly far away) ^c38948709

        For fan choice, Arctic P12/P14 fans tend to be recommended because they're cheap and are good on paper, but they're pretty terrible acoustically (super annoying hum in the 800-1300RPM range which tends to be the optimal level just below where you can hear 120/140mm fans). I'm also irritated by fan noise and have tried a lot of different fans over the years in computers, and I've ended up just paying the Noctua tax and buying nf-a12x25s because they're one of the quietest fans, they move a lot of air with pretty good static pressure, and they don't have any humming or other acoustic issues, just the air noise as you ramp their speeds up. Phanteks T30s are even better than the noctuas and a bit less expensive, but have a bit worse noise profile (a slight drone at higher RPMs that only super picky people will even notice).

        For mine I made an uglier 3 fan version of the slim 5 fan cleanairkits design using hardboard, fan grills, wood glue, a hacksaw, a drill, and a drywall knife. I'd recommend just getting it laser/waterjet cut though instead of suffering trying to cut fan holes in hardboard with a drywall knife and a small drill bit (it takes forever, and ends up being ugly AF). For power I ended up using a USB SATA adapter (noctua PWM adapter takes SATA power, need to get one that uses an external power adapter so it can output enough power, can also steal it from the air purifier if you ever actually need a usb sata adapter) and an old UL listed 12V 1.2A barrel plug power supply I found in a box of old electronics.

        - **firecall** · [2024-01-13 01:13 UTC](https://news.ycombinator.com/item?id=38976367)
          Thanks for the links and info! ^c38976367

  - **karaterobot** · [2024-01-10 21:17 UTC](https://news.ycombinator.com/item?id=38943293)
    Some people (well, me at least) like the air purifier to make some white noise. Mine doesn't turn on automatically if, for example, the power cuts out and then comes on again, and I always notice it within a few minutes because the house feels weird without any background noise. ^c38943293

    - **staplers** · [2024-01-10 21:23 UTC](https://news.ycombinator.com/item?id=38943359)
      White noise is proven to degrade sleep and focus *unless masking more distracting noise* ^c38943359

      - **cqqxo4zV46cp** · [2024-01-10 22:32 UTC](https://news.ycombinator.com/item?id=38944365)
        I always love it with someone proclaims that my benefit / enjoyment of something is invalid because Science declared it so. This isn’t even how academics talk about things like this. ^c38944365

        - **CharlesW** · [2024-01-10 23:11 UTC](https://news.ycombinator.com/item?id=38944881)
          \> *I always love it with someone proclaims that my benefit / enjoyment of something is invalid because Science declared it so.* ^c38944881

          Also, this is not proven. I suspect the parent is thinking about [https://www.theguardian.com/lifeandstyle/2020/oct/18/white-n...](<https://www.theguardian.com/lifeandstyle/2020/oct/18/white-noise-as-sleep-aid-may-do-more-harm-than-good-say-scientists>), which cites [https://www.sciencedirect.com/science/article/abs/pii/S10870...](<https://www.sciencedirect.com/science/article/abs/pii/S1087079220301283>), which found 1 study out of 38 which "*suggested* the noise may lead to more disrupted sleep" and concludes that more research is needed.

          Of course, individuals may find white noise personally irritating or distracting, and continuous loud noise of any sort is bad. But for others, noise can also help with relaxation, concentration, and sound masking.  (I personally find white noise irritating, but I like brown noise.)

        - **staplers** · [2024-01-13 00:37 UTC](https://news.ycombinator.com/item?id=38976130) ^c38976130

          ```
            proclaims that my benefit / enjoyment of something is invalid
          ```

          
          I did no such thing.

  - **lathiat** · [2024-01-10 01:35 UTC](https://news.ycombinator.com/item?id=38935010)
    Indeed, slightly or even double better performance won't help if you turn it off :) ^c38935010

  - **CharlesW** · [2024-01-10 22:01 UTC](https://news.ycombinator.com/item?id=38943922)
    IKEA FÖRNUFTIG is 28 dB at lowest fan speed. Wirecutter's pick (Coway Airmega AP-1512HH Mighty) is 24 dB. ^c38943922

    - **imp0cat** · [2024-01-11 06:29 UTC](https://news.ycombinator.com/item?id=38948550)
      If you are really bothered by noise in a bedroom, Electrolux Pure A9/AEG AX9 is 17dB at it's lowest setting (goes up to 49dB at it's maximum speed as opposed to IKEA's 60dB). ^c38948550

      But it's obviously not as cheap as the IKEA one.

- **turtlebits** · [2024-01-10 23:14 UTC](https://news.ycombinator.com/item?id=38944921)
  My only issue with the IKEA filter is that it's sized too small to run quietly for any of my rooms - IKEA says 85sf on low.  (My smallest room is 110sf)  I guess it's okay for closets? ^c38944921

  Also if I'm going to add an appliance to my home, why not pick the highest filtration possible? (if not unreasonably expensive)

  - **Aurornis** · [2024-01-11 00:04 UTC](https://news.ycombinator.com/item?id=38945449)
    Those ratings are somewhat arbitrary. ^c38945449

    If you run it long enough and you’re not cycling the room air with external air constantly, it will be fine.

    - **turtlebits** · [2024-01-11 00:33 UTC](https://news.ycombinator.com/item?id=38945719)
      Ratings are important.  For allergies, 4x air changes per hour is recommended. ^c38945719

      - **Aurornis** · [2024-01-11 01:59 UTC](https://news.ycombinator.com/item?id=38946444)
        \> Ratings are important. ^c38946444

        Yes, but they're not binary. Being slightly undersized doesn't mean it stops working altogether.

        \> For allergies, 4x air changes per hour is recommended.

        If you have an allergy problem, the last thing you want to do is replace the filtered inside air with outside air every 15 minutes.

        - **SamBam** · [2024-01-11 03:14 UTC](https://news.ycombinator.com/item?id=38947045)
          I think the implication is 4 full filtrations per hour, not 4 air changes. ^c38947045

          Air purifiers still sometimes call this "air changes" or sometimes "equivalent air changes" (e-AC/hr).

- **Bluescreenbuddy** · [2024-01-11 13:04 UTC](https://news.ycombinator.com/item?id=38951684)
  In regards to true HEPA [https://web.archive.org/web/20210225051425/http://www.air-pu...](<https://web.archive.org/web/20210225051425/http://www.air-purifier-power.com/hepatypefilter.html>) ^c38951684

- **IndySun** · [2024-01-11 08:36 UTC](https://news.ycombinator.com/item?id=38949427)
  Ta dah... I've finally been reading Hackernews long enough to notice bigger stories repeat. Where's Dang when he/she/they is/are needed? ^c38949427

  Previously...

  [https://news.ycombinator.com/item?id\=38931559](<https://news.ycombinator.com/item?id=38931559>)

- **stavros** · [2024-01-11 01:04 UTC](https://news.ycombinator.com/item?id=38946018)
  I got the IKEA air quality sensor, and it's always around 5-6 μg/m3, but my bane is cat hair. We have two cats and there's always hair in the air. Is there a filter that will remove those out of the air, and stop me breathing them all the time? ^c38946018

  - **jccooper** · [2024-01-11 01:36 UTC](https://news.ycombinator.com/item?id=38946267)
    Almost any filter will handle cat hair. You probably want to find something with a washable pre-filter (usually a stretch fabric) so you don't waste the expensive actual filter. ^c38946267

    If that's your only concern, a t-shirt over a box fan will probably do the job.

    - **stavros** · [2024-01-11 01:37 UTC](https://news.ycombinator.com/item?id=38946288)
      I tried to make a makeshift filter, but it failed. I guess the box fan wasn't boxy enough. I'll try again, thank you! ^c38946288

- **jononomo** · [2024-01-11 11:02 UTC](https://news.ycombinator.com/item?id=38950605)
  I've often wondered about whether massive outdoor air filters (the size of multi story buildings) could be used to improved the quality of outdoor air.  I don't want to breathe particulates when I'm outside my home, either. ^c38950605

- **iNic** · [2024-01-12 09:03 UTC](https://news.ycombinator.com/item?id=38965742)
  I just want to say that dynomight also has a great article on air purification in general: [https://dynomight.net/air/](<https://dynomight.net/air/>). ^c38965742

- **Paul-Craft** · [2024-01-09 21:45 UTC](https://news.ycombinator.com/item?id=38932574)
  Needs (2022). ^c38932574

- **steveBK123** · [2024-01-11 12:17 UTC](https://news.ycombinator.com/item?id=38951228)
  Anyone in the market for air purifiers should also check out the Coway line, very good products, been using them \~7 years in various form factors. ^c38951228

- **chx** · [2024-01-10 21:25 UTC](https://news.ycombinator.com/item?id=38943396)
  Could someone make a neat blog post like this comparing the CleanSpace Halo to the Dyson Zone Visor? Thanks! ^c38943396

  I would be rather delighted if I could go among people without looking like someone straight out of a catastrophe movie. The Halo looks *weird* even for someone who wears "I am not weird, I am limited edition" t-shirts regularly. The Dyson looks much better but when I did an amateur comparison the performance appeared to be much weaker than the Halo.

  - **throwup238** · [2024-01-10 21:46 UTC](https://news.ycombinator.com/item?id=38943698)
    You can't get decent performance from a respirator type device without a proper seal. The negative pressure created by inhaling is too large a volume and a tiny little fan won't be enough to push that much air fast enough, especially through any kind of filter. If you look at forced air respirators their external units have to be pretty bulky and that's with a full face mask. ^c38943698

    If you want clean air I'm afraid you'll forever have to walk around like an extra on Contagion.

    - **chx** · [2024-01-10 22:33 UTC](https://news.ycombinator.com/item?id=38944385)
      Thanks. ^c38944385

      I will stay with the Halo then.

- **froglets** · [2024-01-11 03:15 UTC](https://news.ycombinator.com/item?id=38947052)
  I’m surprised that air purifiers without UV lamps seem to be the standard. If you’re going to buy something to clean the air, why not have the option to also kill bacteria/viruses/mold spores if any? Especially in houses like mine with kids spewing all kinds of contagion everywhere. ^c38947052

  - **Toutouxc** · [2024-01-11 08:27 UTC](https://news.ycombinator.com/item?id=38949358)
    The article mentions that. First, you’d have to slow down the passage of the particles through the purifier enough so that the UV light could kill everything, which is inconvenient. Second, the filter is supposed to trap the particles and remove them from the environment anyway. ^c38949358

- **unknown** · [2024-01-10 22:56 UTC](https://news.ycombinator.com/item?id=38944669)
  [deleted] ^c38944669

- **boringuser2** · [2024-01-10 23:15 UTC](https://news.ycombinator.com/item?id=38944926)
  It seems that whenever you have expertise in a given area it becomes apparent that Wirecutter gives laughable recommendations. ^c38944926

  Their mattress recommendations, from someone whom has spent large amounts of time trying to piece together what little exists of mattress "science", straddle the border between comical and negligent.

  Consumer Reports is similar.

  - **SamBam** · [2024-01-11 03:21 UTC](https://news.ycombinator.com/item?id=38947106)
    I dunno, I went with their mattress recommendation (at least the one of three years ago, don't know what it is now) and lived it, it's the first mattress I've really liked since becoming an adult. ^c38947106

    - **boringuser2** · [2024-01-11 03:34 UTC](https://news.ycombinator.com/item?id=38947203)
      Mattresses are highly subjective, especially because a decent chunk of the population doesn't have particular requirements for one (i.e. no back or neck problems and general health make it easy to sleep on a rock). ^c38947203

      However, there is a discrete consistency to picking a durable mattress that has advantageous qualities such as support and whatnot, and none of those mattresses are made of quality, durable materials that will provide lasting benefits for sensitive people.

  - **klausa** · [2024-01-11 01:50 UTC](https://news.ycombinator.com/item?id=38946380)
    Do you have results on your research written up somewhere? ^c38946380

- **jononomo** · [2024-01-09 21:27 UTC](https://news.ycombinator.com/item?id=38932340)
  An excellent and informative article. ^c38932340

- **unknown** · [2024-01-10 22:32 UTC](https://news.ycombinator.com/item?id=38944369)
  [deleted] ^c38944369

- **practice9** · [2024-01-11 00:44 UTC](https://news.ycombinator.com/item?id=38945806)
  Aren't most websites like Wirecutter in the business of paid reviews / affiliate marketing? ^c38945806

