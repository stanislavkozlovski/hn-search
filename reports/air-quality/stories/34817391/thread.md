# [IKEA made a smart air quality sensor to track indoor pollution](https://news.ycombinator.com/item?id=34817391)

Article: [https://www.engadget.com/ikea-vindstyrka-indoor-air-quality-sensor-195810594.html](<https://www.engadget.com/ikea-vindstyrka-indoor-air-quality-sensor-195810594.html>)

thunderbong · 2023-02-16 11:28 UTC · 179 reported comments · archived 2026-11-08 12:42 UTC
Observation: 2026-11-08 12:41 UTC → 2026-11-08 12:42 UTC

## Comments

- **ahaucnx** · [2023-02-16 17:01 UTC](https://news.ycombinator.com/item?id=34821396)
  I have extensively tested the previous model and it was a bit of a mixed result with the strongest selling point the price being really affordable. You can see my review and test result on our blog \[1\]. ^c34821396

  One of the biggest negative points that I found was that the traffic light cut off points are way off. So it shows a green light from 0-35 μg/m³ whereas the WHO defines the annual limit now at less than 5 μg/m³.

  Unfortunately in this new model this seems still to be the case and has not been improved (according to the manual \[2\]). So the VINDSTYRKA still gives misleading indications through the traffic light but at least you can now see the μg/m³ on the display and make a more informed judgement (compared to the old model without display).

  It is difficult to make a judgement on the accuracy without really running it through a test cycle but it is definitely missing a CO2 sensor. Measuring CO2 indoors is most likely the most important parameter, especially if you live outside strongly polluted areas e.g. in Asia.

  CO2 sensors that give good accuracy are relatively expensive and I believe it was probably shelved because of costs which is a pity. So this looks like a big missed opportunity but I will try and source one of these and write a review.

  If you are interested for a DIY kit with high quality sensors, check out our AirGradient kits \[3\].

  \[1\] [https://www.airgradient.com/open-airgradient/blog/ikea-vindr...](<https://www.airgradient.com/open-airgradient/blog/ikea-vindriktning-accuracy>)

  \[2\] [https://www.ikea.com/cz/cs/manuals/vindstyrka-senzor-kvality...](<https://www.ikea.com/cz/cs/manuals/vindstyrka-senzor-kvality-vzduchu-chytre__AA-2351596-1-2.pdf>)

  \[3\] [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>)

  - **kixiQu** · [2023-02-16 17:26 UTC](https://news.ycombinator.com/item?id=34821880)
    While it won't catch "you need to open your office window", I'd recommend it to anyone for their kitchen. VOCs and PM2.5 can get real bad without the cook realizing so anything that's even slightly reliable can be useful ^c34821880

  - **Animats** · [2023-02-16 17:41 UTC](https://news.ycombinator.com/item?id=34822165)
    \> Definitely missing a CO2 sensor. ^c34822165

    CO2 sensing devices have become cheaper. No need to buy a kit. Here are two from China. \[1\]\[2\]

    \[1\] [http://www.langder.com/](<http://www.langder.com/>)

    \[2\] [https://www.alibaba.com/product-detail/Factory-direct-sales-...](<https://www.alibaba.com/product-detail/Factory-direct-sales-wall-mounted-carbon_1600180533280.html>)

    - **jahnu** · [2023-02-16 18:28 UTC](https://news.ycombinator.com/item?id=34823209)
      How’s the accuracy? ^c34823209

  - **mcjiggerlog** · [2023-02-16 17:14 UTC](https://news.ycombinator.com/item?id=34821653)
    Agreed - the lack of CO2 monitoring is a shame. ^c34821653

    I bought a relatively inexpensive CO2 monitor (\~90 EUR) and it was really an eye opener. If you work in a small home office, the speed that you reach levels of CO2 that *will* have a noticeable impact on your mental faculties (eg 2000ppm) is incredible. Definitely makes you step up your ventilation game!

    - **hebrox** · [2023-02-16 19:25 UTC](https://news.ycombinator.com/item?id=34824368)
      Can you share which one you bought? ^c34824368

      - **mcjiggerlog** · [2023-02-16 20:07 UTC](https://news.ycombinator.com/item?id=34825113)
        [https://www.amazon.es/gp/product/B07R4XM9Z6](<https://www.amazon.es/gp/product/B07R4XM9Z6>) ^c34825113

  - **noja** · [2023-02-16 17:19 UTC](https://news.ycombinator.com/item?id=34821748)
    Ikea: Does the new model still have a fan that annoyingly switches on and off every 10 seconds? ^c34821748

    AirGradient: support for Homekit please!

  - **cptskippy** · [2023-02-17 03:31 UTC](https://news.ycombinator.com/item?id=34830377)
    While the Ikea Vindriktning might not be accurate, I have found it incredibly consistent and reliable.  I bought a handful of them and hacked them with ESPs (thanks Hypfer) to push data into Home Assistant. ^c34830377

    They're sensitive enough that I can track if/when our cat boxes get cleaned.

    We have a 3 story house and have observed air quality changes in our bedroom and office that are immediately above our stove in the kitchen.

    [https://i.imgur.com/Mjk65pL.png](<https://i.imgur.com/Mjk65pL.png>)

    There isn't a lot people can do to affect the baseline air quality in their homes, but having a sensor that can identify negative change is significantly better than nothing.  A precise and accurate sensor is nice but doesn't offer much benefits above or beyond that.

  - **criddell** · [2023-02-16 17:42 UTC](https://news.ycombinator.com/item?id=34822189)
    Your AirGradient ONE page says "contact us for pricing". How much is it? Why don't you list the price? ^c34822189

    - **ahaucnx** · [2023-02-16 17:56 UTC](https://news.ycombinator.com/item?id=34822498)
      Unlike our kits, the AirGradient ONE targets commercial customers with large and sometimes complex requirements so the price varies depending on this. ^c34822498

      But to give you an estimate it is somewhere between USD 200-300.

  - **privacyking** · [2023-02-17 04:45 UTC](https://news.ycombinator.com/item?id=34830887)
    I've been looking to get a few sensors and ended up going with awair for my first one after reading some comments in your forum. When is your updated PCB (with better ground plane, etc) going to be released? ^c34830887

  - **nebben64** · [2023-02-16 23:26 UTC](https://news.ycombinator.com/item?id=34828231)
    How does AirGradient compare with the Aranet4 CO2 monitor ? ^c34828231

    - **ahaucnx** · [2023-02-17 00:43 UTC](https://news.ycombinator.com/item?id=34829056)
      CO2 should be very similar because we also use a Senseair CO2 sensor module like Aranet but with the AirGradient you can also measure PM and optionally TVOCs. ^c34829056

  - **berberous** · [2023-02-16 17:11 UTC](https://news.ycombinator.com/item?id=34821591)
    Have you tested Awair? How does Airgradiant compare? ^c34821591

    - **ahaucnx** · [2023-02-16 17:15 UTC](https://news.ycombinator.com/item?id=34821665)
      Awair uses much better sensors than the Ikea and the accuracy should be quite similar to the AirGradient. ^c34821665

  - **dgellow** · [2023-02-16 20:14 UTC](https://news.ycombinator.com/item?id=34825222)
    Do you sell them in europe too? ^c34825222

    - **ahaucnx** · [2023-02-17 00:41 UTC](https://news.ycombinator.com/item?id=34829031)
      Yes. We ship worldwide. ^c34829031

- **unwind** · [2023-02-16 11:58 UTC](https://news.ycombinator.com/item?id=34817596)
  Captain Obvious checking in: the name (which Engadget classified as "tongue-twisting") literally means "wind strength", or "wind speed" as its called in actual English. It's two words: "vind" is (surprise) "wind" and "styrka" is "strength". The latter can be pronounced decently by pretending the "y" is perhaps a double "e", or something. ^c34817596

  It is, admittedly, is a bit weird of a name for a sensor that measures air quality but on the other hand it's Ikea and they name things after their own mind.

  Source: am Swedish.

  - **input\_sh** · [2023-02-16 12:12 UTC](https://news.ycombinator.com/item?id=34817702)
    Now I'm curious and since you're already here, what's the difference between VINDTRYRKA and VINDRIKTNING? For context, both are IKEA's air quality sensors, but the new one has a screen. ^c34817702

    - **Jensson** · [2023-02-16 12:16 UTC](https://news.ycombinator.com/item?id=34817733)
      Vindriktning is wind direction. So you have strength, and direction, so next is Vindvektor? ^c34817733

      - **cdaven** · [2023-02-16 15:34 UTC](https://news.ycombinator.com/item?id=34819986)
        There's also the lamp VINDKAST, which in English is "wind throw" or "flurry". ^c34819986

        - **bborud** · [2023-02-16 17:00 UTC](https://news.ycombinator.com/item?id=34821382)
          gust of wind ^c34821382

  - **LargoLasskhyfv** · [2023-02-16 16:40 UTC](https://news.ycombinator.com/item?id=34821046)
    German: Windstärke (Strength of Wind) ^c34821046

    - **jacooper** · [2023-02-16 17:26 UTC](https://news.ycombinator.com/item?id=34821881)
      Windgeschwindigkeit for wind speed. ^c34821881

      - **LargoLasskhyfv** · [2023-02-16 22:19 UTC](https://news.ycombinator.com/item?id=34827327)
        Also valid, but more specific, like meters per second. ^c34827327

        I've been referring to the (more commonly used?) [https://en.wikipedia.org/wiki/Beaufort\_scale](<https://en.wikipedia.org/wiki/Beaufort_scale>) where the scale is more coarse.

  - **jacooper** · [2023-02-16 14:39 UTC](https://news.ycombinator.com/item?id=34819198)
    Actual English? ^c34819198

    - **smallnix** · [2023-02-16 16:21 UTC](https://news.ycombinator.com/item?id=34820715)
      I guess op meant "proper English " as in "not literally but semantically translated" ^c34820715

      - **unwind** · [2023-02-16 16:52 UTC](https://news.ycombinator.com/item?id=34821242)
        Yes, exactly that. Thanks. ^c34821242

    - **benj111** · [2023-02-16 16:38 UTC](https://news.ycombinator.com/item?id=34821010)
      As opposed to the thing wot they speak in the colonies. ^c34821010

- **netrus** · [2023-02-16 11:59 UTC](https://news.ycombinator.com/item?id=34817599)
  What does it take to produce cheap CO2 sensors? Ikea would be my best bet to provide a large enough market for good-enough sensors to bring prices down. A CO2 sensor should be in every classroom and every office, but it's not affordable enough yet. ^c34817599

  - **ThePhysicist** · [2023-02-16 12:51 UTC](https://news.ycombinator.com/item?id=34818018)
    Normally a high CO2 level will go hand in hand with the air feeling stuffy from other pollutants that build up at the same time, so there's hardly a need to continuously use a CO2 meter as you can easily notice when the air "goes bad". CO2 buildup is quite predictable in most closed rooms based on the number of people inside, the room volume and the ventilation as well, so you can just work out a ventilation schedule and stick to that instead. Common sense often beats smart gadets. ^c34818018

    Personally I have a CO2 meter in my tiny office room but I don't need to look at it as I pretty much know that it will be in the red after being in the room for a while with the door closed.

    - **crazygringo** · [2023-02-16 13:43 UTC](https://news.ycombinator.com/item?id=34818447)
      \> *Normally a high CO2 level will go hand in hand with... other pollutants that build up at the same time* ^c34818447

      No, I think you've got that backwards. It's other pollutants that may (but also may not) go hand in hand with CO2.

      CO2 is the only pollutant constantly produced by people and that works as the main indicator of air quality.

      Things like PM2.5 or VOC levels, *if* they are being produced at all, will *also* be trapped in stale air. But my apartment, for example, generates virtually none of those, except for when I'm cooking, when it generates massive quantities of PM2.5.

      I use a CO2 monitor in my living room and I adjust the crack in the window several times a day to keep it around 550 without wasting too much on heating. It's not even remotely common sense, you *absolutely* need a sensor.

      - **shafyy** · [2023-02-16 14:29 UTC](https://news.ycombinator.com/item?id=34819062)
        \> *I use a CO2 monitor in my living room and I adjust the crack in the window several times a day to keep it around 550 without wasting too much on heating. It's not even remotely common sense, you absolutely need a sensor.* ^c34819062

        It's more efficient to air out by opening the windows fully and creating a draft for a few minutes several times a day than to leave the window cracked when it's colder outside.

        - **not\_kurt\_godel** · [2023-02-16 14:35 UTC](https://news.ycombinator.com/item?id=34819150)
          That's not adequate, at least for me as a relatively average sized man in a relatively average sized living unit. My respiration is sufficient to raise CO2 levels indoors to over 800ppm from background levels within an hour without constant ventilation. ^c34819150

        - **crazygringo** · [2023-02-16 14:32 UTC](https://news.ycombinator.com/item?id=34819114)
          No it's not. ^c34819114

          CO2 levels build up higher than I want within half an hour so I'd have to be doing that all day long. And it would result in a periodically freezing apartment.

          It's much more efficient for me to keep it open a crack.

          - **titaniumdafodil** · [2023-02-16 15:19 UTC](https://news.ycombinator.com/item?id=34819790)
            Do you have central air, and keep the fan running? I've experimented with this at our place and doing a full cycle for 5 minutes, then turning the fan to "on" rather than "auto" and closing all doors and windows will keep it below 700 everywhere for about 6 hours. Otherwise the second floor climbs into the 1000's while the first floor stays around 500 ^c34819790

          - **thadk** · [2023-02-17 04:28 UTC](https://news.ycombinator.com/item?id=34830784)
            I got the window unit version of [https://www.openerv.org](<https://www.openerv.org>) and it is better than leaving the window open. ^c34830784

          - **shafyy** · [2023-02-16 19:13 UTC](https://news.ycombinator.com/item?id=34824123)
            I mean efficient in terms of heating/energy, not CO2 levels. ^c34824123

    - **loudmax** · [2023-02-16 13:20 UTC](https://news.ycombinator.com/item?id=34818253)
      Thinking about CO2 levels isn't common sense until after you've been keeping an eye on one of these gadgets.  After sitting in a meeting room for an hour, people may find it feels warm or stuffy or notice a slight headache, but they won't necessarily draw the connection that they really ought to open a window or door or adjourn the meeting for a few minutes.  The importance of breathing fresh air becomes much more common sense after you've learned to tell the difference. ^c34818253

      - **throwaway14356** · [2023-02-16 13:26 UTC](https://news.ycombinator.com/item?id=34818312)
        walking outdoors seems the perfect formula ^c34818312

        - **doitLP** · [2023-02-16 14:32 UTC](https://news.ycombinator.com/item?id=34819109)
          As someone who worked too long at an office with non-existent ventilation and a fetish for long, closed door meetings, my motto became: ^c34819109

          “Take a break. Go outside. Walk around the block. Never come back.”

          - **throwaway14356** · [2023-02-16 16:56 UTC](https://news.ycombinator.com/item?id=34821318)
            I bet walking while talking is great once people get used to it. ^c34821318

        - **o\_m** · [2023-02-16 13:48 UTC](https://news.ycombinator.com/item?id=34818523)
          For now. As we keep burning fossil fuels the air outside will be like a stuffed meeting room. ^c34818523

          - **unknown** · [2023-02-16 14:04 UTC](https://news.ycombinator.com/item?id=34818743)
            [deleted] ^c34818743

          - **throwaway14356** · [2023-02-16 16:54 UTC](https://news.ycombinator.com/item?id=34821290)
            nah, gladly indoor air is still much worse :) ^c34821290

    - **not\_kurt\_godel** · [2023-02-16 14:26 UTC](https://news.ycombinator.com/item?id=34819025)
      \> Normally a high CO2 level will go hand in hand with the air feeling stuffy from other pollutants that build up at the same time, so there's hardly a need to continuously use a CO2 meter as you can easily notice when the air "goes bad" ^c34819025

      Strong disagree based on direct experience. I have a HEPA unit that keeps air in the entire living unit clean (from VOCs, particulate matter, NO2, etc.) but doesn't alter CO2 levels. There is little to no human-detectable effect from CO2 levels rising up to 2500ppm (according to my separate CO2 monitor).

      - **dfadsadsf** · [2023-02-16 14:29 UTC](https://news.ycombinator.com/item?id=34819063)
        HEPA filter does not do much for VOC. VOCs, because they are gases, are about 1000 times smaller than what HEPA filters can capture. You need carbon-based filter to neutralize them. ^c34819063

        - **not\_kurt\_godel** · [2023-02-16 14:31 UTC](https://news.ycombinator.com/item?id=34819100)
          My unit has both HEPA and carbon-based filters. The point is, my CO2 levels rise independently of any other pollutant and it's not reliably detectable by a human as far as I can tell. ^c34819100

          - **Filligree** · [2023-02-16 15:03 UTC](https://news.ycombinator.com/item?id=34819568)
            How often do you swap the carbon filter? ^c34819568

            My understanding, admittedly driven by 3D printing, is that they only last about a week before the substrate degrades. Fortunately activated carbon is cheap.

            - **not\_kurt\_godel** · [2023-02-16 15:23 UTC](https://news.ycombinator.com/item?id=34819834)
              Variable, between 6 months and a year, per the manufacturer's recommendation and unit's ability to sense when the filter needs replacing. It seems like you're saying yours only last a week because you're constantly generating fumes from 3D printing? I don't do anything like that. I would be curious to get some kind of independent measurement of effectiveness of a new filter over time (and I suppose I will from my air monitor next time I replace). But again, the point is my separate air quality monitor shows increases in CO2 that are not associated with rise in any of the other 4 detectable pollutants it measures. ^c34819834

              - **Filligree** · [2023-02-16 17:09 UTC](https://news.ycombinator.com/item?id=34821535)
                What I’ve been told is that the carbon filter will stop absorbing VOCs after a week, regardless of how much I use the printer. Considering that some of them are carcinogens, I’m not taking any chances. ^c34821535

                Presumably this should also hold for other carbon filters, then, but I don’t know how I would verify that.

    - **icee** · [2023-02-16 16:25 UTC](https://news.ycombinator.com/item?id=34820788)
      I went to a lot of trouble to install an ERV — a Panasonic model. Brought my CO2 levels down from consistently over 1200ppm to \~500ppm with people in the house. Hot/humid areas make it difficult to bring in fresh air since the moisture in the air can lead to all sorts of issues and obviously it's very inefficient to have 100 degree air coming into the house when you're seeking mid-70s temps indoors. ERVs are designed to address these issues. ^c34820788

      Check out a video here to see how these things work (this demo is an HRV, so it doesn't help with humidity, but you can see how well it works when there is a big temperature difference between indoors and outdoors).

      [https://youtu.be/QOSelUK6dpQ?t\=436](<https://youtu.be/QOSelUK6dpQ?t=436>)

      - **sib** · [2023-02-16 17:29 UTC](https://news.ycombinator.com/item?id=34821929)
        For those, like me, who didn't know: ^c34821929

        ERV \=\= Energy Recovery Ventilator

        See [https://en.wikipedia.org/wiki/Energy\_recovery\_ventilation](<https://en.wikipedia.org/wiki/Energy_recovery_ventilation>)

      - **latchkey** · [2023-02-16 16:57 UTC](https://news.ycombinator.com/item?id=34821344)
        That's really neat. Haven't seen something like that before, thanks for sharing. ^c34821344

    - **flemhans** · [2023-02-16 13:05 UTC](https://news.ycombinator.com/item?id=34818142)
      I can't feel the difference between 1500ppm and 500ppm CO2 levels, yet 1500 is above recommended limits. ^c34818142

      It's actually quite difficult to keep it below 1000 for us, and getting these sensors in every room has been quite the 'curse' :D

      - **drewda** · [2023-02-16 14:20 UTC](https://news.ycombinator.com/item?id=34818937)
        FWIW, the frustrations of not being able to change high CO2 levels was just a topic of discussion over on [https://news.ycombinator.com/item?id\=34648021](<https://news.ycombinator.com/item?id=34648021>) ^c34818937

      - **boppo1** · [2023-02-16 13:20 UTC](https://news.ycombinator.com/item?id=34818259)
        I've wondered about this. If I install an air monitor in my room, what do I do if it shows low quality? Open my window in below-freezing winter temps? Hire someone to overhaul my furnace and vents? ^c34818259

        - **arrrg** · [2023-02-16 13:46 UTC](https://news.ycombinator.com/item?id=34818500)
          So, this works with temperatures down to freezing and below (don’t know what the cut off is, maybe there is none given this planet’s temperature range) and if you heat and dress appropriately (i.e. not up to super high temperatures – around 20°C or so – and if you have a sweater or jacket on or can put one on). ^c34818500

          Obviously you also need the appropriate building for it. (So no fancy passive house. No fancy air conditioning – which is quite uncommon where I’m from anyway.)

          Generally, if you only open the windows for five minutes or so the air will cool down substantially (the right moment to pull on that sweater) but everything else (walls, furniture) will not really cool down that much, meaning the room will be quick to be back at an appropriate temperature.

          We learned and did this in school, often do it in offices and meeting rooms and also at home. Though, admittedly the temporary unpleasantness does frequently lead to people postponing opening the windows forever and ever. (Once every 90 minutes in a classroom setting might not be enough.)

          In those settings a CO2 traffic light as an obvious visual indicator would be super helpful.

        - **happymellon** · [2023-02-16 13:35 UTC](https://news.ycombinator.com/item?id=34818377)
          If you aren't willing to do anything about it then why bother with the air monitor? ^c34818377

          If you only have a single room then your options are limited, however moving rooms or opening a door to a different room and turning on a fan to increase circulation?

          If it is CO2 then you could invest in a houseplant or two.

          - **Ajedi32** · [2023-02-16 13:47 UTC](https://news.ycombinator.com/item?id=34818513)
            \> If it is CO2 then you could invest in a houseplant or two. ^c34818513

            This seemed wrong to me, so I checked and it seems like you'd need hundreds of houseplants to make any significant difference: [https://www.realhomes.com/news/do-house-plants-remove-carbon...](<https://www.realhomes.com/news/do-house-plants-remove-carbon-dioxide-from-homes>)

            - **boppo1** · [2023-02-16 17:50 UTC](https://news.ycombinator.com/item?id=34822371)
              Seems like there'd be a market for a CO2 \> O2 exchanger of some sort. I don't know enough chemistry to recognize why this is probably too difficult for commercial viability. ^c34822371

          - **dgacmu** · [2023-02-16 13:44 UTC](https://news.ycombinator.com/item?id=34818459)
            Houseplants do not exchange anything near significant amounts of CO2 for this purpose. ^c34818459

            The long term answer is to improve the HVAC: reconfigure for more external air mixing (commercial), or find a way to install an HRV or ERV, or open a window, but that can be expensive or impossible depending on the situation.

            - **hellweaver666** · [2023-02-17 12:26 UTC](https://news.ycombinator.com/item?id=34833835)
              I'm currently renovating a house in The Netherlands, we're installing a heat pump and to make the place more efficient we also replaced the glass with triple glazed (but without vents in the frames as they let heat escape). Given that we were effectively making our house a "sealed envelope" we had to add mechanical ventilation (ERV) to ensure proper airflow around the property. As you can imagine, retrofitting ducting around an old house required a LOT of creative work! ^c34833835

            - **happymellon** · [2023-02-16 18:05 UTC](https://news.ycombinator.com/item?id=34822693)
              The houseplant was just the cheer them up while they slowly suffocate since they weren't going to do anything about it. ^c34822693

              Like a button that does nothing.

        - **crazygringo** · [2023-02-16 13:46 UTC](https://news.ycombinator.com/item?id=34818493)
          Open the window. In my apartment I keep a single open somewhere between a millimeter and a centimeter when it's below freezing, depending on the temperature and wind. That's enough to keep my CO2 sensor happy (try to keep it around 550), and it (shockingly) doesn't seem to affect my heating bill all that much. There's a cold corner of the room next to that window, but the rest of the apartment stays just as warm. (I have a thermostat that controls heating.) ^c34818493

          I also keep a humidifier running full blast (silently) because otherwise it will get crazy dry on some days.

          - **Semaphor** · [2023-02-16 14:31 UTC](https://news.ycombinator.com/item?id=34819098)
            \> I also keep a humidifier running full blast (silently) because otherwise it will get crazy dry on some days. ^c34819098

            Heh, I usually keep the dehumidifier running, I don’t think I’ll ever need a humidifier. Currently, 80\% RH (7g/m³) outside, with indoor levels all slightly above 60\%.

          - **thombat** · [2023-02-16 15:07 UTC](https://news.ycombinator.com/item?id=34819613)
            That cold corner risks becoming a condensation point and so developing mold. ^c34819613

            - **crazygringo** · [2023-02-16 16:16 UTC](https://news.ycombinator.com/item?id=34820624)
              It doesn't though. The relative humidity at 70°F is only 30-35\% with the humidifier running full blast. Because it's often 7-15\% without the humidifier. Because the air coming through the window is bone dry. ^c34820624

              The problem in the winter here is keeping *enough* humidity in the air. It would be nice if I ever had to worry about condensation. ;)

        - **throwaway14356** · [2023-02-16 13:30 UTC](https://news.ycombinator.com/item?id=34818342)
          if you keep the window open all year, dress appropriately and avoid heated buildings you don't notice how cold it is. I switch it on a few years ago because my cat is getting really old. I now feel cold if its 17 C or below. ^c34818342

          - **kgermino** · [2023-02-16 15:20 UTC](https://news.ycombinator.com/item?id=34819808)
            That is an extraordinarily climate-specific recommendation. It’s currently a fairly mild 30F/-1 C outside my house and even that is obviously way too cold to go without heat completely. ^c34819808

            - **throwaway14356** · [2023-02-16 16:53 UTC](https://news.ycombinator.com/item?id=34821274)
              You are conditioned to think you are and feel cold. Look how cold some countries and regions get? The people working outside there are not a different species. The trick is to get used to it gradually. I didn't say it was fun or easy. ^c34821274

              I spend a good bit of winter working outside but with physical activity it is much easier.

              Do you have other ideas? I mean, it would be nice? I cant think of anything else besides migration.

              - **Germanika** · [2023-02-16 20:45 UTC](https://news.ycombinator.com/item?id=34825788)
                \>Look how cold some countries and regions get? ^c34825788

                As someone from said countries and regions, people living outside freeze to death here. Long before you get to that point your water pipes will freeze, leaving you without running water. The pipes will then burst and flood your house if you don't address it quickly enough. You can certainly heat it to a lower temperature and occasionally crack open a window for some fresh air, but there's a difference between conditioning yourself to be comfortable at 17C and -30C.

      - **maxerickson** · [2023-02-16 13:31 UTC](https://news.ycombinator.com/item?id=34818350)
        I imagine people are mostly perceiving humidity and heat when they notice a room getting stuffy. ^c34818350

    - **pasc1878** · [2023-02-16 14:56 UTC](https://news.ycombinator.com/item?id=34819430)
      No it does not. ^c34819430

      This is from experience.

      The CO2 level in my bedroom gets high whilst I sleep.

      I open the window and the CO2 drops quickly but the VOC pollutant levels rise.

    - **dghughes** · [2023-02-16 13:49 UTC](https://news.ycombinator.com/item?id=34818536)
      \>Normally a high CO2 level will go hand in hand with the air feeling stuffy ^c34818536

      I bought my Dad a NetAtmo weather station one part is outside and one is inside.

      During Christmas with guests over I looked and saw the CO2 was 1000ppm it felt very stuffy (no air handler in an old house). I opened a window and let some fresh cool air in and CO2 out. It felt so much better.

      It was nice to know why it felt stuffy. It wasn't just all the turkey and potatoes that I had eaten.

    - **pasc1878** · [2023-02-16 14:55 UTC](https://news.ycombinator.com/item?id=34819425)
      No it does not. ^c34819425

      This is from experience.

      The CO2 level in my bedroom gets high whilst I sleep.

      I open the window and the CO2 drops quickly but the pollutant levels rise.

    - **Gravityloss** · [2023-02-16 14:37 UTC](https://news.ycombinator.com/item?id=34819174)
      I find stuffiness feeling correlates mostly with humidity. ^c34819174

  - **wkat4242** · [2023-02-16 15:03 UTC](https://news.ycombinator.com/item?id=34819564)
    Sensirion makes a decent photoacoustic-based sensor called the SCD41. It's about 30 bucks in volume. ^c34819564

    Other models are laser based (NDIR) and more expensive.

    There's also eCO2 which is estimated based on VOC levels and basically useless.

    So in other words, adding real CO2 would increase the price a lot. At least double it (since the sensor cost isn't the only factor obviously)

    This would totally change the value proposition and target market. I guess they did their research and decided against it. There's other devices that do CO2 for around \$100.

    - **peterbraden** · [2023-02-16 15:27 UTC](https://news.ycombinator.com/item?id=34819896)
      The SCD40 series is a pain to calibrate - it will drift out of calibration unless it's left outside at some points. It's not ideal for consumer electronics. ^c34819896

      - **woefblaf123** · [2023-02-16 15:33 UTC](https://news.ycombinator.com/item?id=34819977)
        This is not unique to the SCD40 series. This applies also to NDIR based sensors. They also need to 'see' outside air on a weekly basis. ^c34819977

        It's just the way CO2 sensing tech works.

        - **fotta** · [2023-02-16 15:40 UTC](https://news.ycombinator.com/item?id=34820082)
          Not necessarily. The SCD series can have auto calibration turned off. You take it outside once and baseline that to 400ppm. The drift on the sensor is rated very low (+-50 ppm over the sensor’s lifetime). This is what I do with my SCD30. ^c34820082

          - **wkat4242** · [2023-02-16 22:52 UTC](https://news.ycombinator.com/item?id=34827750)
            Interesting, I didn't know that, I've only used them in auto mode. I also have SCD30s, the 40s are a pain in the \*\* to solder and they were hard to get because they are new. ^c34827750

            I wonder why they don't just calibrate them off the factory line then? I mean, 50ppm is not much. In auto mode you won't get much better accuracy than that because you don't always air the house well enough to get down to 400 (let alone in a city's CO2 bubble).

  - **ikekkdcjkfke** · [2023-02-16 12:42 UTC](https://news.ycombinator.com/item?id=34817934)
    Why isn't my 1000\$ smartphone loaded with sensors, infrared camera, decibel meter etc. ^c34817934

    - **jve** · [2023-02-16 13:32 UTC](https://news.ycombinator.com/item?id=34818353)
      ... yeah, apart from gyroscope, pressure, proximity, light, position, magnetic, accelerometer, g, fingerprint, blood oxygen, internal temp and IR sensors. ^c34818353

      - **whstl** · [2023-02-16 14:41 UTC](https://news.ycombinator.com/item?id=34819222)
        And some smart speakers are now loaded with thermometer and hygrometer. ^c34819222

        - **m3kw9** · [2023-02-16 15:40 UTC](https://news.ycombinator.com/item?id=34820078)
          All Home pod mini and the new big hompod has those ^c34820078

    - **soderfoo** · [2023-02-16 12:47 UTC](https://news.ycombinator.com/item?id=34817983)
      Manufacturers believe consumer sentiment favors cramming more telephoto selfie cams and the like in to phones. ^c34817983

      - **literalAardvark** · [2023-02-16 13:40 UTC](https://news.ycombinator.com/item?id=34818412)
        Unfortunately, word on the street agrees. I'd really love CO2, HRV and a physical keyboard, but it's just not gonna happen ever, because we'd end up with the Homermobile. ^c34818412

        - **red-iron-pine** · [2023-02-16 17:20 UTC](https://news.ycombinator.com/item?id=34821768)
          homemobile was ugly and expensive.  if they could be slipped in easily and reasonably cheaply then it might fly. ^c34821768

    - **varjag** · [2023-02-16 12:50 UTC](https://news.ycombinator.com/item?id=34818012)
      \> decibel meter ^c34818012

      You have the microphone in your smartphone.

    - **davidy123** · [2023-02-16 12:59 UTC](https://news.ycombinator.com/item?id=34818089)
      You can add these things via USB (not sure about iPhone). If enough people find it helpful, it'll become part of the package eventually. ^c34818089

      - **happymellon** · [2023-02-16 13:38 UTC](https://news.ycombinator.com/item?id=34818399)
        There are a few lightning adaptors, I have an IR camera for example, however they are talking about the USB C port is going to be proprietary so it will only work for power unless you have Apple approved wiring and chips. ^c34818399

    - **loudmax** · [2023-02-16 13:24 UTC](https://news.ycombinator.com/item?id=34818299)
      Because the demand hasn't been there.  If more people learn the benefits of these sensors and decide they want more of them they'll pay more for models that include them and manufacturers will respond to demand.  If people don't know about them, or don't perceive any particular benefit, those sensors will remain niche and expensive. ^c34818299

    - **aflag** · [2023-02-16 12:44 UTC](https://news.ycombinator.com/item?id=34817965)
      Probably because it would make it cost more than \$1000 while not being useful to most people. ^c34817965

    - **arsome** · [2023-02-16 13:28 UTC](https://news.ycombinator.com/item?id=34818326)
      Same reason I can't have a hardware keyboard on any modern, reasonably priced phone: lack of demand. ^c34818326

    - **goodpoint** · [2023-02-16 13:02 UTC](https://news.ycombinator.com/item?id=34818122)
      Because manufacturers invested a lot in advertising to create demand for extremely high resolution screen and cameras. ^c34818122

      Even if air quality sensors would have saved lives (see covid and air pollution) that's not what companies optimize for.

    - **aintgonnatakeit** · [2023-02-16 13:18 UTC](https://news.ycombinator.com/item?id=34818238)
      iPhone has a decibel meter ^c34818238

      - **LeonM** · [2023-02-16 15:50 UTC](https://news.ycombinator.com/item?id=34820232)
        Any phone has a decibel meter, it's the microphone. ^c34820232

        However, I can imagine that with Android devices calibration is going to be an issue (with iPhones, you know which sensor is being used)

  - **the\_generalist** · [2023-02-16 12:46 UTC](https://news.ycombinator.com/item?id=34817977)
    I toyed with something like this a few years ago. Never really built the thing, but you can actually do this with a Rasberry Pi and a couple of attachments. ^c34817977

  - **lostmsu** · [2023-02-16 15:34 UTC](https://news.ycombinator.com/item?id=34819984)
    Note, the IKEA sensor does NOT monitor CO2. ^c34819984

  - **agoose77** · [2023-02-16 12:36 UTC](https://news.ycombinator.com/item?id=34817882)
    Depends what "cheap" is. You can get MHZ19 \< £20-30 last I checked. ^c34817882

    - **progbits** · [2023-02-16 12:40 UTC](https://news.ycombinator.com/item?id=34817918)
      Sensirion SCD40, a good quality compact sensor from very reputable manufacturer, sells for \$25 in bulk. ^c34817918

      - **MichaelZuo** · [2023-02-16 13:00 UTC](https://news.ycombinator.com/item?id=34818095)
        After including all the costs and markups to get it to retail, that would imply an MSRP of at least \$200. ^c34818095

        - **billiallards** · [2023-02-16 16:25 UTC](https://news.ycombinator.com/item?id=34820778)
          Looks like \<\$30 to buy a single unit on DigiKey with a prevailing price \~\$40, but you'd probably need a reflow oven to solder the unit. \$60 for an assembled board at retail. ^c34820778

          Bulk retail is closer to \$20, so OP may not have been referring to negotiated wholesale volume pricing.

          [https://octopart.com/search?q\=scd40&currency\=USD&specs\=0](<https://octopart.com/search?q=scd40%C2%A4cy=USD&specs=0>)

          - **MichaelZuo** · [2023-02-16 20:49 UTC](https://news.ycombinator.com/item?id=34825847)
            \$60 for an assembled unit at a retail store when the sensor alone is \$20-\$25 in bulk? ^c34825847

    - **unknown** · [2023-02-16 15:06 UTC](https://news.ycombinator.com/item?id=34819609)
      [deleted] ^c34819609

  - **unknown** · [2023-02-16 13:25 UTC](https://news.ycombinator.com/item?id=34818302)
    [deleted] ^c34818302

- **smhg** · [2023-02-16 13:35 UTC](https://news.ycombinator.com/item?id=34818376)
  On the Czech IKEA website it's listed with a price of 999 CZK \[0\]. This is about 42 EUR. ^c34818376

  \[0\] [https://www.ikea.com/cz/cs/p/vindstyrka-senzor-kvality-vzduc...](<https://www.ikea.com/cz/cs/p/vindstyrka-senzor-kvality-vzduchu-chytre-40498234/>)

  - **marbu** · [2023-02-16 15:12 UTC](https://news.ycombinator.com/item?id=34819696)
    On the other hand, it's already reported as "soul out". ^c34819696

  - **tpmx** · [2023-02-16 15:16 UTC](https://news.ycombinator.com/item?id=34819752)
    That includes 21\% VAT. So \$37 + sales tax. ^c34819752

  - **pjc50** · [2023-02-16 14:43 UTC](https://news.ycombinator.com/item?id=34819232)
    Not yet available in the UK at all, sadly. ^c34819232

- **fbn79** · [2023-02-16 12:21 UTC](https://news.ycombinator.com/item?id=34817773)
  It's important to know that accuracy of this sensor are very low [https://www.airgradient.com/open-airgradient/blog/ikea-vindr...](<https://www.airgradient.com/open-airgradient/blog/ikea-vindriktning-accuracy/>) ^c34817773

  - **tecleandor** · [2023-02-16 12:33 UTC](https://news.ycombinator.com/item?id=34817855)
    Be aware that review is not for this product, but for the previous one. I don't know if they're using the same sensors inside. ^c34817855

    Edit: to be clear, the new product is called VINDSTYRKA, the review you link is for Vindriktning, the previous "non smart" sensor.

  - **zihotki** · [2023-02-16 12:28 UTC](https://news.ycombinator.com/item?id=34817819)
    While absolute accuracy is low, you still can use it to see the trend. Often the trend and approximate measurements are good enough.
    Edit: spelling ^c34817819

  - **MaxPengwing** · [2023-02-16 12:28 UTC](https://news.ycombinator.com/item?id=34817816)
    not the same device. Would be nice if they did a tear down of Vindstyrka as well. ^c34817816

  - **danuker** · [2023-02-16 12:30 UTC](https://news.ycombinator.com/item?id=34817836)
    Looks like the new device has a screen and is called Vindstyrka, and the one reviewed is an old one with LED indicators, Vindriktning. ^c34817836

  - **unknown** · [2023-02-16 12:31 UTC](https://news.ycombinator.com/item?id=34817842)
    [deleted] ^c34817842

  - **unknown** · [2023-02-16 12:53 UTC](https://news.ycombinator.com/item?id=34818032)
    [deleted] ^c34818032

- **progbits** · [2023-02-16 11:56 UTC](https://news.ycombinator.com/item?id=34817575)
  They are already selling the Vindriktning for a long time. It doesn't have a screen, just a traffic lights style indicator, and the thresholds are quite high. However it costs like \$10 and if you buy a \$3 esp module and spend few minutes soldering you can get it integrated into home assistant. ^c34817575

  This new device looks nice but due to the display I expect the price to be much higher.

  - **martin\_a** · [2023-02-16 12:11 UTC](https://news.ycombinator.com/item?id=34817693)
    This was the first thing that came to my mind. ^c34817693

    I've got various IKEA lights integrated in Home Assistant which is no problem due to sticking to the ZigBee standard, so I can use my existing gateway + RPi 3.

    If those air quality monitors would support the ZigBee standard too, that would be very nice.

    - **progbits** · [2023-02-16 12:37 UTC](https://news.ycombinator.com/item?id=34817895)
      Definitely. These could be nice for locations where they can be seen as they actually look nice and provide useful display. ^c34817895

      But usually I prefer to hide something cheaper and uglier behind furniture and then get the data on my phone.

      I wish they put these into other objects like lamps, picture frames etc

  - **Jensson** · [2023-02-16 13:36 UTC](https://news.ycombinator.com/item?id=34818383)
    You can get a calculator for a few dollars, basic screens aren't that expensive. The screen shown looks like the same level as a calculator and a few printed symbols on top of it, so price shouldn't need to change much at all. ^c34818383

- **seltzered\_** · [2023-02-16 14:05 UTC](https://news.ycombinator.com/item?id=34818759)
  Worth reminding of this blog post concerning cheap air quality monitoring systems: [https://halestrom.net/darksleep/blog/048\_indoorairsensing/](<https://halestrom.net/darksleep/blog/048_indoorairsensing/>) ^c34818759

- **glitcher** · [2023-02-16 15:31 UTC](https://news.ycombinator.com/item?id=34819939)
  Off topic: upon first opening this web page I was surprised to think that maybe I had already visited all the links in the article. Then I realized purple is one of the site's primary colors, and both visited and unvisited links look the same there. ^c34819939

- **londons\_explore** · [2023-02-16 13:14 UTC](https://news.ycombinator.com/item?id=34818207)
  Could an air quality sensor be made by using a spark gap and then a spectrometry on the light produced by the spark? ^c34818207

  You should be able to measure CO2, NOX, and various other pollutants this way, either via emission or absorption spectroscopy.   For solid PM2.5 pollution, you could potentially identify the chemical make up of the particles, which should be good for identifying the iron metal dust from machines, the stone dust from building work, the organic skin dust, the rubber dust from tyres, the carbon dust from engines, etc.

  Seems like a single cheap sensor  that might be able to provide a lot more info than other more complex sensor types.

  - **Doxin** · [2023-02-20 11:54 UTC](https://news.ycombinator.com/item?id=34867278)
    I think the signal from regular air would swamp out any signal from higher CO2 counts or particulates or the like. Of course since you already know beforehand which spectral peaks you want to look at you can presumably use some really narrow color filters which might help. ^c34867278

- **thimkerbell** · [2023-02-16 14:55 UTC](https://news.ycombinator.com/item?id=34819416)
  Two points: ^c34819416

  First, as noted by many below (above), IKEA really needs to put a CO2 monitor in this thing, to tell room occupants the most useful information.

  Second, one person being confidently wrong can use up a lot of other people's time. Maybe there's some way that forum design could reduce this problem. Maybe there isn't.

  - **skrebbel** · [2023-02-16 15:10 UTC](https://news.ycombinator.com/item?id=34819673)
    \> Second, one person being confidently wrong can use up a lot of other people's time. Maybe there's some way that forum design could reduce this problem. Maybe there isn't. ^c34819673

    Is this like an HN subtweet or am I just daft? I have absolutely no idea which comment you're referring to here.

  - **idiotsecant** · [2023-02-16 15:03 UTC](https://news.ycombinator.com/item?id=34819552)
    Is CO2 level useful, though? Our bodies are really exceptionally good at detecting harmful CO2 levels. There's very little effect to CO2 buildup in air up to levels that people are good at detecting. VOCs, PM2.5, and other contaminant classes are not so easily detected by human hardware, though. ^c34819552

    - **valenterry** · [2023-02-16 15:06 UTC](https://news.ycombinator.com/item?id=34819601)
      There's something between "perfectly fine" and "harmful" though. bad co2 levels can impact concentration without being harmful. ^c34819601

  - **thimkerbell** · [2023-02-16 15:10 UTC](https://news.ycombinator.com/item?id=34819660)
    (One thing that might aid reader skimming could be a 2nd step of offering the commenter something like 60 characters' worth of mild highlighting, to apply to their comment where they wish, to stress most important point(s), if they want to.) ^c34819660

  - **turtlebits** · [2023-02-16 15:53 UTC](https://news.ycombinator.com/item?id=34820268)
    While I agree that CO2 sensors are useful, they'll significantly add to the price.  High CO2 levels in a home aren't a health risk unlike PM2.5 or VOCs though. ^c34820268

- **bborud** · [2023-02-16 17:20 UTC](https://news.ycombinator.com/item?id=34821760)
  Looks like it uses this particle sensor: [https://www.environmental-expert.com/products/cubic-model-pm...](<https://www.environmental-expert.com/products/cubic-model-pm1006k-led-particle-sensor-752064>) ^c34821760

- **rjsw** · [2023-02-16 12:52 UTC](https://news.ycombinator.com/item?id=34818029)
  The owner of the ISP that I use has been experimenting with making his own \[1\]. ^c34818029

  \[1\] [https://www.revk.uk/2019/09/environmental-sensor.html](<https://www.revk.uk/2019/09/environmental-sensor.html>)

  - **hellweaver666** · [2023-02-17 12:52 UTC](https://news.ycombinator.com/item?id=34834046)
    If you're in the UK, Pimoroni have a bunch of awesome sensor boards with a PicoW attached to them which makes it super easy to put sensors on your network (they have sensors designed for indoor and outdoor use and even a full weather station!) ^c34834046

- **d1sxeyes** · [2023-02-17 15:38 UTC](https://news.ycombinator.com/item?id=34835841)
  \> It can tell a Starkvind purifier to ramp up the fan speed based on particulate levels, for instance ^c34835841

  Starkvinds already have an 'auto mode' which does exactly that. I love being able to see air quality and humidity, but in reality, pretty much every device you can control remotely which is capable of influencing air quality and humidity already has the capability built in, and I have fallen short of finding any *actually useful* automations that involve either humidity or air quality sensors.

- **slavoingilizov** · [2023-02-16 14:04 UTC](https://news.ycombinator.com/item?id=34818744)
  Honest question - monitoring air quality accurately is great, but monitoring doesn't solve problems. Once you know it's bad, what do you do? I've been wondering what's the point of monitoring something if you can't do anything about it? Do people move house when it's consistently bad? Are the majority of issues caused by in-house pollutants so you open windows for ventilation more? Maybe I'm biased but in my neck of the woods, the bad air quality comes from \_outside\_. So unless I up sticks, not much else to do. ^c34818744

  - **alias\_neo** · [2023-02-16 15:32 UTC](https://news.ycombinator.com/item?id=34819961)
    I built a PM2.5 and PM10 monitoring "box" for Home Assistant when we got our log-stove installed. ^c34819961

    The goal was to know how bad the air quality would be in our living room / home.

    Having used it for several weeks, now I've learned a couple of things;

    The air quality \_in\_ the house is usually \_much\_ better than it is outside, for example, I measure an average of 1-2ug/m3 inside, but if I take it outside or open the window it can rise to 20-30ug/m3, we live on a fairly busy road. I looked into the UK air quality guidelines and the advice is literally to "close your windows".

    Second, the log stove has no effect on the (PM) air quality in the living room when burning properly, however, opening the door to refuel, or not lighting it to a proper burn can cause the levels to shoot up to 70ug/m3 or as high as 200ug/m3 if you let a lot of smoke out while dicking around with the fire, this has a pretty slow fall-off and usually takes hours to drop back to "normal".

    I want a CO2 monitor next to check CO2 levels too.

  - **karmelapple** · [2023-02-16 14:22 UTC](https://news.ycombinator.com/item?id=34818977)
    Do you have a CO2 or other air monitor at your home? 
    Do you have a gas oven?
    Every time I turned on my gas oven, the CO2 would spike from 600ppm to over 1200ppm almost immediately. I wouldn’t have known that without a meter, and wouldn’t have realized my air quality was bad inside. ^c34818977

  - **BelleOfTheBall** · [2023-02-16 14:06 UTC](https://news.ycombinator.com/item?id=34818767)
    You can use methods of cleaning the air in your house, I assume things like humidifiers and specialized air conditioning/cleaning units exist. The point of these sensors is to show the problem actually exists. If thousands of people suddenly find out their home air is compromised, that will then create a demand for air purification tools. ^c34818767

  - **blago** · [2023-02-16 14:06 UTC](https://news.ycombinator.com/item?id=34818766)
    Air purifiers work pretty well for most kinds of pollution, and they are widely available. ^c34818766

  - **jabroni\_salad** · [2023-02-16 15:08 UTC](https://news.ycombinator.com/item?id=34819644)
    I'm bad with pollen and air filters have been good for me. It's just on a timer though, I don't use any fancy sensors. ^c34819644

- **yalogin** · [2023-02-16 16:42 UTC](https://news.ycombinator.com/item?id=34821085)
  These sensors can only estimate based on what passes through them. So is it a good enough approximation for the whole room let alone the whole house? I get it that the very presence of some particles at some density will tell a story. Since we know where we are placing that device we have to extrapolate the numbers and get an overall sense of pollution in the house. Can folks that use something like this chime in with experience and how effective or useful this is? ^c34821085

- **cptskippy** · [2023-02-16 19:05 UTC](https://news.ycombinator.com/item?id=34823960)
  Hey I made an IKEA smart air quality sensor too! ^c34823960

  [https://imgur.com/a/UhL4OuD](<https://imgur.com/a/UhL4OuD>)

- **input\_sh** · [2023-02-16 12:07 UTC](https://news.ycombinator.com/item?id=34817669)
  Worth pointing out that they already had a sensor, but it didn't have a screen, just LEDs that turned from green to red. ^c34817669

  For price reference, it's \$16. [https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor...](<https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor-60515911/>)

  - **BossingAround** · [2023-02-16 14:51 UTC](https://news.ycombinator.com/item?id=34819355)
    Which is notoriously imprecise \[1\]. ^c34819355

    \[1\] [https://www.airgradient.com/open-airgradient/blog/ikea-vindr...](<https://www.airgradient.com/open-airgradient/blog/ikea-vindriktning-accuracy/>)

    - **wartijn\_** · [2023-02-16 17:52 UTC](https://news.ycombinator.com/item?id=34822404)
      That article is linked a few times in these comments, but I think it should be noted that that article is written by a competitor. Airgradient is a commercial company that sells air quality sensors. And it seems to be the only source that states the Ikea sensor is imprecise, so I wouldn't call it "notoriously imprecise" ^c34822404

- **chewmieser** · [2023-02-16 12:06 UTC](https://news.ycombinator.com/item?id=34817660)
  There’s plenty of air quality monitors out there already. Doesn’t seem like this does anything unique, but I’ll be interested in seeing the price when it’s available. ^c34817660

  I personally use an Atomotube Pro ([https://store.atmotube.com/](<https://store.atmotube.com/>)) which also has the added benefit of being portable.

  - **joshvm** · [2023-02-16 12:48 UTC](https://news.ycombinator.com/item?id=34817994)
    A big benefit would be ZigBee integration. Not particularly unique, but IKEA tend to do a reasonable job in terms of quality and price and their smart home bits are easy to connect to HomeAssistant. They claim it can talk to STARKVIND, so it should have that capability. They seem to be a bit more reliable than Aqara/Xiaomi (battery life seems to be variable for me). ^c34817994

    - **djhworld** · [2023-02-16 16:57 UTC](https://news.ycombinator.com/item?id=34821329)
      \> Not particularly unique, but IKEA tend to do a reasonable job ^c34821329

      I'd say they do a great job.

      While they offer hub and app (not sure if the app is cloud connected) for less technical users, most of the 'smart' product line is just zigbee so will work with any zigbee gateway. I think that should be applauded, especially as other "smart" product providers either go bust or pull product lines rendering them useless.

    - **a\_paddy** · [2023-02-16 15:45 UTC](https://news.ycombinator.com/item?id=34820153)
      IKEA's marketing material say it's not compatible with the Tradfri Hub, so might be using Matter over Thread. Although the DIRIGERA does still also support ZigBee, they are moving away from it. ^c34820153

      - **tecleandor** · [2023-02-16 16:42 UTC](https://news.ycombinator.com/item?id=34821081)
        I've seen in websites that it's Matter compatible (although I haven't seen that information in their press release) ^c34821081

        Edit: I guess people are extrapolating that info on being compatible with their DIRIGERA Hub, that seems to be Matter compatible.

        9to5mac reports this info:


        ```
          Update 2/15: IKEA has shared with us that the DIRIGERA smart hub doesn’t have Matter support yet (after its launch last fall), but it is “ready” to enable it with a future update. As noted below, the new air quality monitor does not have HomeKit or Matter capability on its own but can gain it when paired with the DIRIGERA but only after IKEA pushes the Matter update to the hub. We’ve reached out to IKEA asking about a Matter launch date.
        ```

        
        [https://9to5mac.com/2023/02/14/ikea-smart-indoor-air-quality...](<https://9to5mac.com/2023/02/14/ikea-smart-indoor-air-quality-monitor-matter-homekit/>)

  - **gizmodo59** · [2023-02-16 12:34 UTC](https://news.ycombinator.com/item?id=34817867)
    It looks good. But the reviews on Amazon says it’s not having a good battery life. How’s it for you? I don’t need to travel that much so I can keep it plugged in all the time? ^c34817867

    - **chewmieser** · [2023-02-16 12:54 UTC](https://news.ycombinator.com/item?id=34818037)
      Battery life is fine, not amazing but fine. I can usually get around a week or so of battery life depending on what I'm using it for. I usually leave it near an outlet anyway so I can plug it in periodically. The portable nature of the device is a nice-to-have for me but I usually just use it in my home. ^c34818037

      One thing that it lacks is WiFi connectivity - all syncing needs to be done via bluetooth. Which makes sense since it's portable but WiFi would be nice when it's at home. But the device is open and their site gives you ways to make it WiFi compatible if you so desired.

      I originally found it through a report that showed it as effective as expensive air quality testing gear. It happened to be the only portable one as well that rated that well.

- **robg** · [2023-02-16 15:10 UTC](https://news.ycombinator.com/item?id=34819669)
  LG has a purifier and sensor combo that I used to learn we were likely aerosolizing heavy metals in our humidifiers. ^c34819669

  - **somehnguy** · [2023-02-16 16:15 UTC](https://news.ycombinator.com/item?id=34820610)
    My air purifier's meter goes into the red whenever I use the shower down the hall from it - it did the same thing as my previous home as well. I've always just assumed it's a side-effect of the raised humidity. ^c34820610

  - **dalyons** · [2023-02-16 15:47 UTC](https://news.ycombinator.com/item?id=34820177)
    What did you do about this? I just noticed the same thing with my purpleair indoor (goes crazy on pm2.5 when I run the humidifier) ^c34820177

- **Toutouxc** · [2023-02-16 19:23 UTC](https://news.ycombinator.com/item?id=34824323)
  \> IKEA already has a side table that doubles as an air purifier, but now it has a way to gauge just how clean that air really is ^c34824323

  Please note that the purifier/table combo and the standalone purifier, both called Starkvind, already have a PM2.5 sensor and are smart (Zigbee) devices.

- **m3kw9** · [2023-02-16 15:33 UTC](https://news.ycombinator.com/item?id=34819976)
  Makes sense, it would help sell their air purifier.  Still could be useful by it self but if you are already concerned about air quality, this will push you to confirm your fears. ^c34819976

  The product development team there is rolling

  - **adolph** · [2023-02-16 15:45 UTC](https://news.ycombinator.com/item?id=34820161)
    So like: air sensor (\$) -\> air purifier (\$) -\> filters for previous (\$\$\$ over time) ^c34820161

    [https://en.wikipedia.org/wiki/Razor\_and\_blades\_model](<https://en.wikipedia.org/wiki/Razor_and_blades_model>)

- **taeric** · [2023-02-16 15:06 UTC](https://news.ycombinator.com/item?id=34819607)
  I welcome more information on air quality.  I do not look forward to the emerging state of it.  I fully expect it to be closer to back surgeries than otherwise. ^c34819607

- **rishikeshs** · [2023-02-16 13:35 UTC](https://news.ycombinator.com/item?id=34818380)
  Is it possible to build a similar one using Arduino? ^c34818380

  - **KerrickStaley** · [2023-02-16 13:56 UTC](https://news.ycombinator.com/item?id=34818599)
    Look up AirGradient. ^c34818599

- **KerrickStaley** · [2023-02-16 14:00 UTC](https://news.ycombinator.com/item?id=34818667)
  I've been very happy with my AirGradient \[1\]. It measures PM2.5, CO2, temperature, and humidity. I got the \$67 kit and assembled it; it was a fun soldering project. I like that I can reflash it and get it to send data to VictoriaMetrics on my Raspberry Pi over WiFi. The biggest thing that I dislike is that the CO2 sensor loses calibration over time and (from what I understand) needs to be re-exposed to fresh outdoor air every \~2 weeks. ^c34818667

  I might buy this IKEA sensor too to see how they compare; wouldn't hurt to be able to monitor a second room.

  \[1\] [https://www.airgradient.com/](<https://www.airgradient.com/>)

  - **thebruce87m** · [2023-02-16 19:21 UTC](https://news.ycombinator.com/item?id=34824273)
    A well ventilated room should return to outside ppm levels during the day if unoccupied. ^c34824273

  - **vestrigi** · [2023-02-16 16:40 UTC](https://news.ycombinator.com/item?id=34821049)
    Isn't the recalibration even a problem of all CO2 sensors, including the IKEA model? ^c34821049

    - **Toutouxc** · [2023-02-16 21:36 UTC](https://news.ycombinator.com/item?id=34826695)
      IKEA doesn’t sell a CO2 sensor. ^c34826695

- **jeffreygoesto** · [2023-02-16 12:38 UTC](https://news.ycombinator.com/item?id=34817904)
  With a Bosch Bme680 you can detect farts. Take that, CO2 enthusiasts... \=;-} ^c34817904

  - **BossingAround** · [2023-02-16 14:54 UTC](https://news.ycombinator.com/item?id=34819390)
    Looks interesting; is there a blog somewhere detailing how to hook the sensor up to Raspberry Pi or something similar? ^c34819390

    - **hobo\_mark** · [2023-02-16 15:22 UTC](https://news.ycombinator.com/item?id=34819823)
      You literally connect four wires and \`pip install bme680\`. ^c34819823

- **KaiserPro** · [2023-02-16 13:20 UTC](https://news.ycombinator.com/item?id=34818251)
  has anyone found the price of these? ^c34818251

  I have some second hand awair sensors, which I got for about £50. They are brilliant, but cost £200 new.

  - **BossingAround** · [2023-02-16 14:53 UTC](https://news.ycombinator.com/item?id=34819378)
    \~40EUR on the Czech Ikea website that someone posted here. ^c34819378

- **donutshop** · [2023-02-16 13:48 UTC](https://news.ycombinator.com/item?id=34818517)
  Unpopular opinion - Airthings make very good air quality sensors, and detects radon levels as well. ^c34818517

  - **Toutouxc** · [2023-02-16 19:56 UTC](https://news.ycombinator.com/item?id=34824904)
    That’s not even an opinion, much less an unpopular one. ^c34824904

- **folly237** · [2023-02-16 13:41 UTC](https://news.ycombinator.com/item?id=34818431)
  Maybe I'm out of the loop since moving away from any IKEA store 6 years ago...but this feels a bit out of the ordinary for them, doesn't it? To me, IKEA \= "build your own furniture". Not "smart home tech". ^c34818431

  - **Toutouxc** · [2023-02-16 19:55 UTC](https://news.ycombinator.com/item?id=34824876)
    Way out of the loop. IKEA now sells loads of smart home tech: smart lightbulbs, LED drivers, motion sensors, light switches, power outlets, air purifiers, motorized window shades and even amazing smart speakers (designed by IKEA, but fully compatible Sonos internals with respectable sound quality). ^c34824876

  - **BossingAround** · [2023-02-16 14:54 UTC](https://news.ycombinator.com/item?id=34819399)
    I'm sure people said that too when Amazon was launching AWS. ^c34819399

  - **jeromegv** · [2023-02-16 14:50 UTC](https://news.ycombinator.com/item?id=34819333)
    They have been selling TVs for many years. ^c34819333

- **blago** · [2023-02-16 14:10 UTC](https://news.ycombinator.com/item?id=34818824)
  So much irony considering that Ikea's furniture is probably the main source of formaldehyde pollution in most people's homes. I don't judge them too hard but ironic nevertheless. ^c34818824

  - **bklyn11201** · [2023-02-16 14:15 UTC](https://news.ycombinator.com/item?id=34818879)
    How much pre-1993 Ikea furniture still exists in USA homes?! ^c34818879

    - **blago** · [2023-02-16 14:46 UTC](https://news.ycombinator.com/item?id=34819281)
      What happened in 1993? ^c34819281

      - **CharlesW** · [2023-02-16 15:33 UTC](https://news.ycombinator.com/item?id=34819973)
        That's when IKEA stopped adding formaldehyde to its products. ^c34819973

        [https://www.ikea.com/us/en/customer-service/knowledge/articl...](<https://www.ikea.com/us/en/customer-service/knowledge/articles/3d6091g2-bc89-4337-8489-2e7771f4g1fg.html>): *"Trace amounts of formaldehyde can be found in our products as it is a naturally occurring substance, however, we do not add formaldehyde to our range. As a precautionary measure, IKEA has phased out several chemicals that could potentially be harmful, often ahead of legislation."*

        - **blago** · [2023-02-16 23:56 UTC](https://news.ycombinator.com/item?id=34828560)
          This is not from 1993. ^c34828560

          "Trace amounts of formaldehyde can be found in our products"

          Trace amounts sounds great, but that's open to interpretation. There are MANY guidelines by different authorities and their levels differ by more than an order of magnitude. If you take OSHA PEL as baseline you can claim trace amounts and still be pretty harmful.

          "however, we do not add formaldehyde to our range."

          Range? This sounds so vague it feels deliberate.

          "As a precautionary measure, IKEA has phased out several chemicals that could potentially be harmful, often ahead of legislation."

          They didn't say formaldehyde was one of them :-)

          Also, did you ready the linked PDF? It says they don't use formaldehyde in their paint and lacquer. They didn't say anything about their glue and particle board. That's where formaldehyde is indispensable and used in large amounts.

