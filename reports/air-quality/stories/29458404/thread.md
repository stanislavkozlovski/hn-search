# [Ikea Vindriktning Air Quality Sensor Review and Accuracy](https://news.ycombinator.com/item?id=29458404)

Article: [https://www.airgradient.com/resources/ikea-vindriktning-accuracy/](<https://www.airgradient.com/resources/ikea-vindriktning-accuracy/>)

ahaucnx · 2021-12-06 11:26 UTC · 163 reported comments · archived 2026-11-08 11:55 UTC
Observation: 2026-11-08 11:54 UTC → 2026-11-08 11:55 UTC

## Comments

- **ahaucnx** · [2021-12-06 14:14 UTC](https://news.ycombinator.com/item?id=29459929)
  Author here. I forgot to mention: ^c29459929

  With a Wemos D1 mini (ESP8266) MCU that costs around USD 2.00, you can pretty easily make the Vindriktning WiFi connected and get the data to a backend \[1\].

  You just need to solder three wires, and there is enough space within the enclosure to fit the D1 mini inside.

  This would then allow you to get the exact measurements and to better understand if the "green" is more on the lower end or the higher side.

  \[1\] [https://github.com/Hypfer/esp8266-vindriktning-particle-sens...](<https://github.com/Hypfer/esp8266-vindriktning-particle-sensor>)

  - **namdnay** · [2021-12-06 15:18 UTC](https://news.ycombinator.com/item?id=29460727)
    Nice article! One small typo: ^c29460727

    \> It can be seen that all three sensors correlate very well but that the Vindriktning only shows about 65\% of the PM2.5 values of the other two sensors and thus seems to considerably *understate the air quality*.

    I think here you mean "overstate the air quality" right? Or "understate the air pollution"

  - **accountofme** · [2021-12-07 06:09 UTC](https://news.ycombinator.com/item?id=29469522)
    Hi author! Nice write up and good analysis. However I think you missed something in the analysis. ^c29469522

    The sensor is only accurate to +-20uG/m\^3 this also means it can never reach a reading of healthy air according to the WHO specs... I think that is a bigger issue that the traffic light UI.

    Apologies for picking on this issue. I am very thankful you took the time to create this article and look at the all the specifications.

  - **404mm** · [2021-12-06 14:23 UTC](https://news.ycombinator.com/item?id=29460035)
    Hi, thanks for the article! ^c29460035

    Are there any non expensive sensors you could recommend? I care about the indoor air quality but it gets very pricey. I have Awair at home but it covers only one room and the unit runs \$300 a piece :(

    - **gonehome** · [2021-12-06 14:56 UTC](https://news.ycombinator.com/item?id=29460427)
      Not the OP, but I tried a bunch of these and wrote up details here: [https://www.reddit.com/r/AirQuality/comments/ikf1ed/are\_ther...](<https://www.reddit.com/r/AirQuality/comments/ikf1ed/are_there_any_good_air_sensors/>) ^c29460427

      Most of them (including the awair) are complete crap.

      I found one that seems okay and is also one of the cheaper ones.

      I use and like this one best: [https://www.amazon.com/dp/B07DHXQXGK/](<https://www.amazon.com/dp/B07DHXQXGK/>)

      Simple screen with relevant details, no crappy 2.4ghz wifi, no crappy app, etc. it just works.

      - **404mm** · [2021-12-06 15:55 UTC](https://news.ycombinator.com/item?id=29461245)
        Aqmd tested Awair and it came with really good results actually. I’m struggling to find the report online at the moment. ^c29461245

        - **gonehome** · [2021-12-06 17:03 UTC](https://news.ycombinator.com/item?id=29462343)
          It doesn’t tell you AQI or PM2.5 so it’s results may be consistent but are fairly useless. ^c29462343

          I’d be curious what report you saw, last I looked the consistency of the results wasn’t even that great either.

          - **nitrogen** · [2021-12-06 22:03 UTC](https://news.ycombinator.com/item?id=29466288)
            Awair's phone app lists both AQI and PM2.5, and PM2.5 is available on the device itself by pressing buttons to change the display.  Somewhat confusingly, the indoor AQI is on the Outdoor tab. ^c29466288

            - **gonehome** · [2021-12-06 23:48 UTC](https://news.ycombinator.com/item?id=29467353)
              Cool - this must be new? ^c29467353

              When I owned one they only had some proprietary quality score and how it related to PM2.5 or AQI was not listed.

        - **Matrixik** · [2021-12-06 18:58 UTC](https://news.ycombinator.com/item?id=29464056)
          This one?: [https://www.aqmd.gov/aq-spec/evaluations/summary-pm](<https://www.aqmd.gov/aq-spec/evaluations/summary-pm>) ^c29464056

          - **404mm** · [2021-12-06 20:38 UTC](https://news.ycombinator.com/item?id=29465342)
            Unfortunately no, not this one. I also came across these but I recall a several page long reports for each device individually. Tested in controlled environment and compared with some professional \$20k+ sensor. 
            I wish I could deliver better than promises lol. ^c29465342

      - **noja** · [2021-12-06 21:13 UTC](https://news.ycombinator.com/item?id=29465808)
        That looks like the Eve Room [https://www.evehome.com/en/eve-room](<https://www.evehome.com/en/eve-room>) ^c29465808

    - **mellavora** · [2021-12-06 16:17 UTC](https://news.ycombinator.com/item?id=29461588)
      I'm a fan of the airgradient, they offer a very nice DIY. You can build a quality sensor for under \$50. ^c29461588

      [https://www.airgradient.com/diy/](<https://www.airgradient.com/diy/>)

      Components:


      ```
          Wemos D1 Mini USD 2.24
          Wemos OLED display USD 2.47
          Plantower PMS5003 PM Sensor USD 13.89
          Senseair S8 CO2 Sensor USD 28.00
          SHT30 or SHT31 Temperature and Humidity Sensor Module USD 2.55
      ```

      
      I think the lead article was posted by the founder of airgradient. I've had some email exchanges with him, he is supportive and helpful.

      - **geerlingguy** · [2021-12-06 18:00 UTC](https://news.ycombinator.com/item?id=29463237)
        I can also attest to the inexpensive simplicity (and decent reliability) of the AirGradient sensors. ^c29463237

      - **GekkePrutser** · [2021-12-07 03:38 UTC](https://news.ycombinator.com/item?id=29468851)
        That looks like a great kit! It's that Senseair S8 a real CO2 sensor though? It's a bit cheap, most in that price range are just estimated (eCO2) ^c29468851

        - **ahaucnx** · [2021-12-07 13:19 UTC](https://news.ycombinator.com/item?id=29472139)
          The S8 is a high quality NDIR CO2 sensor often used in professional air quality monitors. ^c29472139

    - **ahaucnx** · [2021-12-06 14:39 UTC](https://news.ycombinator.com/item?id=29460224)
      I am not aware of a good and low-cost wifi connected sensor but as I mentioned it is relatively easy to build one yourself. ^c29460224

      If you don't want to buld yourself, there are a few relatively good non-connected PM 2.5 sensors for example the "SmartMi PM2.5 Air Quality Monitor" that I can recommend. It costs around USD 30 here in Asia.

    - **tnorthcutt** · [2021-12-06 16:24 UTC](https://news.ycombinator.com/item?id=29461679)
      You might be interested in the author's DIY kits: [https://www.airgradient.com/diy](<https://www.airgradient.com/diy>) ^c29461679

    - **ruffrey** · [2021-12-06 14:39 UTC](https://news.ycombinator.com/item?id=29460221)
      I’ve used this one \[1\] then ordered similar ones from Ali express after getting the Adafruit one working. ^c29460221

      1\. [https://www.adafruit.com/product/3686?gclid\=CjwKCAiAhreNBhAY...](<https://www.adafruit.com/product/3686?gclid=CjwKCAiAhreNBhAYEiwAFGGKPCbnSc7S_o-NHHVYP1RGUcrdKj-7pB6y6rVpt1VYwujHfXoB-e2aGhoCuTIQAvD_BwE>)

      - **stavros** · [2021-12-06 15:07 UTC](https://news.ycombinator.com/item?id=29460562)
        I can second this one, I soldered four wires to connect it to an ESP8266 and flashed ESPhome and that was it, it's worked fine for months. ^c29460562

    - **bobiny** · [2021-12-06 14:48 UTC](https://news.ycombinator.com/item?id=29460320)
      I like my Netatmo. I see that it costs \$200 on Amazon for main module + you can connect 3 additional ones for other rooms — they cost \$86 each. It shows CO2 (notifies when it's high on smartphone), temperature, relative humidity and noise level. ^c29460320

      - **unknown** · [2021-12-06 16:04 UTC](https://news.ycombinator.com/item?id=29461391)
        [deleted] ^c29461391

    - **ortusdux** · [2021-12-06 14:50 UTC](https://news.ycombinator.com/item?id=29460356)
      I've been looking at ordering a variety of environmental sensors from Seeed Studio's Grove line.  They look approachable and affordable, but I cannot vouch for their quality. ^c29460356

      [https://www.seeedstudio.com/Grove-Laser-PM2-5-Sensor-HM3301....](<https://www.seeedstudio.com/Grove-Laser-PM2-5-Sensor-HM3301.html>)

  - **zibzab** · [2021-12-06 20:47 UTC](https://news.ycombinator.com/item?id=29465461)
    Are you recording sensors output? ^c29465461

    If the sensors have been calibrated in software, wouldn't you get the uncalibrated values?

  - **ZoomZoomZoom** · [2021-12-07 08:00 UTC](https://news.ycombinator.com/item?id=29470061)
    I assume you're in some way connected to the site maintainers (or it's just you). Please, tell them the site is broken, as it does not display anything without JS. ^c29470061

    There's *nothing* dynamic on the page (in fact, on most pages on the site). It's mostly text and images, a user doesn't need to run your blobs of code to see them.

  - **unknown** · [2021-12-06 20:39 UTC](https://news.ycombinator.com/item?id=29465359)
    [deleted] ^c29465359

  - **jb1991** · [2021-12-06 15:07 UTC](https://news.ycombinator.com/item?id=29460561)
    It would be great to hear some alternative suggestions for a consumer air quality meter that is accurate, reliable. I.e. are the AirThings products good? Or do you have any other recommendations? ^c29460561

    - **samsolomon** · [2021-12-07 02:14 UTC](https://news.ycombinator.com/item?id=29468429)
      I purchased two Airthings View Plus monitors about a month ago. We had a subslab depressurization system installed to mitigate Radon in the basement. The company offered continuous monitoring for \$300/yr. Instead I decided to purchase monitors and keep an eye on it myself. ^c29468429

      It's hard to know how good the products will be long-term, but the app and charting is pretty good. You can download reports via their web dashboard. I've turned off all notifications except for the CO2 monitor. The ePaper screen is legible, but the text is a little rough around the edges.

      Here's what it tracks:

      \- Radon

      \- PM 2.5

      \- VOC

      \- CO2

      \- Humidity

      \- Temperature

      \- Pressure

      I will say that the View Plus is Airthings most expensive product. If you don't care about PM 2.5 or Radon monitoring, they have significantly cheaper options.

  - **balaji1** · [2021-12-06 20:56 UTC](https://news.ycombinator.com/item?id=29465588)
    Should we just consider buying an air purifier? ^c29465588

    Currently in Bay Area where air outside seems good but these apartments seem poorly ventilated, old fixtures, old floors, lots of electronics, etc.

  - **wnevets** · [2021-12-07 01:15 UTC](https://news.ycombinator.com/item?id=29468043)
    Have you tested other air quality sensors, if so have you tested the uHoo? ^c29468043

    [https://getuhoo.com/](<https://getuhoo.com/>)

  - **newman314** · [2021-12-06 21:09 UTC](https://news.ycombinator.com/item?id=29465751)
    Given that the correlation is pretty good, I wonder if it's sufficient to just add a compensating factor to get a better sense of air quality. ^c29465751

  - **smusamashah** · [2021-12-07 00:49 UTC](https://news.ycombinator.com/item?id=29467837)
    Append this info in your article please. It's a very useful suggestion for future readers. ^c29467837

  - **pingec** · [2021-12-06 19:02 UTC](https://news.ycombinator.com/item?id=29464102)
    Are there any air quality devices that work well outdoors in all kind of weather? ^c29464102

- **Someone1234** · [2021-12-06 13:56 UTC](https://news.ycombinator.com/item?id=29459751)
  Informative article with fair, fact based, conclusions. ^c29459751

  I'd like to add that:

  \- The VINDRIKTNING is extremely consumer accessible (\$11.99, good build, simple traffic light system).

  \- It may be put into spaces that previously had no particulate air quality monitoring.

  \- The spouse-acceptance-factor is extremely high (unlike e.g. a couple of circuit boards wired together off of Aliexpress).

  There are other consumer friendly offerings, but they aren't affordable (e.g. Amazon Smart Air Quality Monitor 4x cost, Airthings 10x cost). That being said, IKEA could fix their traffic-light system's cut off points for free and should consider it.

  - **ahaucnx** · [2021-12-06 14:19 UTC](https://news.ycombinator.com/item?id=29459992)
    It is actually pretty easy to build a much more accurate air quality sensor with the Plantower PM2.5 module as a base and a Wemos D1 mini as WiFi connected MCU. We have build instructions on our website on how to do it \[1\] + a nice 3D printable enclosure to pass the spouse-acceptance ;). ^c29459992

    \[1\] [https://www.airgradient.com/diy/](<https://www.airgradient.com/diy/>)

    - **Someone1234** · [2021-12-06 14:26 UTC](https://news.ycombinator.com/item?id=29460073)
      I don't think our usages of "accessible" are the same. ^c29460073

      For example expecting to consumers to have a 3D printer and know how to use one would preclude it from my definition by a lot. Let alone needing a breadboard and to manually solder on components onto it.

      Accessible is walking into a store, putting a reasonable amount of money down, and plugging the thing in. Then providing output anyone can understand without training or expertise (e.g. traffic lights, smiley faces, etc).

      - **hedora** · [2021-12-06 16:37 UTC](https://news.ycombinator.com/item?id=29461909)
        I once bought an air filter that had the pm 2.5 rating surrounded by a blue/yellow/red halo.  The only things it was missing were logging, and the ability to run the sensor without the fan.  It could change fan speeds based on PM 2.5, but it was calibrated for a small room, and always ran way too slow. ^c29461909

        I wish there were standards around thermostats these days.  If there were, then people could sell gizmos that measure PM 2.5, then (if the windows are closed), use it to set the speed of the variable speed blower in central air furnaces accordingly.  This would cut our electricity usage by at least 20-30\% during fire season.

        (I’d love to see a legal mandate for interoperability in this space.)

        - **genewitch** · [2021-12-06 18:44 UTC](https://news.ycombinator.com/item?id=29463833)
          My furnace blower isn't in use any longer, but it has connections for varying speeds, 6, I think. It only uses 1, though. I'm unsure of how it would even be used in practice, as it appears it's just various voltages. Ideally furnace blowers would be inverter ran so you could just tell the inverter how fast to run the fan, rather than changing the supply voltage. ^c29463833

          Mine was a 3.5 ton HVAC, I replaced it with a five head, five and a half ton "mini split"; while the split air has had it's share of issues (like, I got a full refund of the purchase price a few months ago due to manufacturing defects of the copper lines), I prefer having air handling done bear the ceiling and using 20x20x1 inch filters on box fans (or fancy filters if those are your style) on the floor. The mini split has the inverter driven motors everywhere, and is completely silent during normal use.

          I have two AQM, and occasionally one or the other will register high CO2 or whatever and I will open a couple of windows and run exhaust fans (built in to the home) to cycle the air, it takes about 20 minutes. The main furnace style system did no filtering or air quality management.

        - **Tijdreiziger** · [2021-12-06 19:22 UTC](https://news.ycombinator.com/item?id=29464340)
          \> I wish there were standards around thermostats these days. ^c29464340

          [https://en.wikipedia.org/wiki/OpenTherm](<https://en.wikipedia.org/wiki/OpenTherm>)

      - **mellavora** · [2021-12-06 16:39 UTC](https://news.ycombinator.com/item?id=29461939)
        to be fair, ahaucnx  didn't use the word 'accessible', he just said 'easy to build' -- and this is hacker news, not consumer reports. ^c29461939

        but if you do want 'accessible' in your sense of the word (pay some money, get a working assembled unit), AirGradient does sell assembled units. And can provide a back-end system for remote monitoring if you would like.

        - **Someone1234** · [2021-12-06 18:38 UTC](https://news.ycombinator.com/item?id=29463747)
          The comment was edited to remove the word. “Easy to build” wasn’t originally there. ^c29463747

      - **zahma** · [2021-12-06 21:04 UTC](https://news.ycombinator.com/item?id=29465694)
        Fortunately this is even easier: [https://sensor.community/en/sensors/](<https://sensor.community/en/sensors/>) ^c29465694

    - **formerly\_proven** · [2021-12-06 17:57 UTC](https://news.ycombinator.com/item?id=29463185)
      I see that there's a tiny 20x20 fan in these modules. Do these make audible noise or are the fans in these running rather slowly just to have air movement "better than convection" through the sensor? ^c29463185

      - **GekkePrutser** · [2021-12-06 22:53 UTC](https://news.ycombinator.com/item?id=29466793)
        The person who did the original hack on these says they are audible and the controller is constantly switching the fan on and off so they reconnected it to 3.3v all the time. So it runs at a lower speed and constantly. ^c29466793

        See this link under the low noise mod heading

        [https://github.com/Hypfer/esp8266-vindriktning-particle-sens...](<https://github.com/Hypfer/esp8266-vindriktning-particle-sensor>)

  - **beckingz** · [2021-12-06 17:13 UTC](https://news.ycombinator.com/item?id=29462491)
    Spouse acceptance factor is an underrated engineering constraint. ^c29462491

    - **monopoledance** · [2021-12-06 18:04 UTC](https://news.ycombinator.com/item?id=29463321)
      [flagged] ^c29463321

      And likely an unnecessary sexist remark.

      - **ev1** · [2021-12-06 18:10 UTC](https://news.ycombinator.com/item?id=29463418)
        No sex or gender was implied by the word spouse? ^c29463418

        - **monopoledance** · [2021-12-06 19:18 UTC](https://news.ycombinator.com/item?id=29464299)
          [flagged] ^c29464299

          "technically, ..."

          Yeah, I know. That's why I said likely. C'mon, don't play stupid.

          - **illumanaughty** · [2021-12-06 19:47 UTC](https://news.ycombinator.com/item?id=29464634)
            What makes it likely when nothing about sex/gender is mentioned? Seems like you're the one that has a gender bias and you're projecting lol ^c29464634

            - **monopoledance** · [2021-12-06 21:02 UTC](https://news.ycombinator.com/item?id=29465662)
              [flagged] ^c29465662

              Sure. Must be me projecting, because sexism in tech does not exist.

              \> Spouse acceptance factor is an underrated engineering constraint

              So, tell me, how could this be interpreted without implicit gender assumptions? Get creative, you got this!

          - **simondotau** · [2021-12-06 20:26 UTC](https://news.ycombinator.com/item?id=29465147)
            Can you explain why it would be sexist, even if we applied mid-20th century framing to it? Why is it degrading to describe someone as having a different threshold of tolerance for aesthetics? ^c29465147

            - **monopoledance** · [2021-12-06 20:52 UTC](https://news.ycombinator.com/item?id=29465526)
              [flagged] ^c29465526

              \> having a different threshold of tolerance for aesthetics

              Lol. How you all trying hard to reframe it, to make it sound innocent.

              I am not going to explain shit. Look how y'all got triggered, totally normal reaction... The original post flagged... If you don't see the generalized "women/wives don't like nerdy/tech stuff", there is no point to this.

          - **UnFleshedOne** · [2021-12-06 19:56 UTC](https://news.ycombinator.com/item?id=29464742)
            Well, but is it wrong? Even you knew which gender is less likely to like bare baseboard with chips sticking out. Do you expect people to actively disregard their lived experience? ^c29464742

            - **monopoledance** · [2021-12-06 20:53 UTC](https://news.ycombinator.com/item?id=29465554)
              [flagged] ^c29465554

              \> Well, but is it wrong? Even you knew which gender is less likely to like bare baseboard with chips sticking out. Do you expect people to actively disregard their lived experience

              Thanks, for confirming it. Ridiculous, how everyone is trying to bend interpretation.

              - **GekkePrutser** · [2021-12-07 03:32 UTC](https://news.ycombinator.com/item?id=29468830)
                But you're the one who called it sexist. Even though it is merely a statistical likelihood. ^c29468830

                As others have pointed out it is really a serious consideration for a lot of people so I don't think it's an unnecessary remark, and the OP went out of their way to make it not sexist.

                - **monopoledance** · [2021-12-07 09:18 UTC](https://news.ycombinator.com/item?id=29470502)
                  [flagged] ^c29470502

                  Thanks, for not over-reacting and seeking actual debate.

                  So, why do you think the others have tried hard to reframe the statement as meaning something unspecific? Why didn't they just point out the "statistical likelihood"?

                  Because, they know (deep down) the spouse/wife talk *is* very much following a certain tradition. An argument about the "nature of women", or as you said "statistical likelihood" (who's statistic?) is exactly what has been used to justify why women shouldn't be considered for access to certain parts of society and is normative. Do I really have to explain why publicly maintaining such stereotypes is influencing behavior in other parts of life? Wouldn't mansplaining tech to women just be "effective", as they are "statistically unlikely" to know their way around it?

                  Don't you think, this "the wife, eh" in this context creates an implicit "me and the boys" atmosphere? Do you think this actually invites participation for wives, or women in general? C'mon. How about me only suggesting this as sexism (not even the original comment, but the follow-up appraisal) immediately getting downvoted and killed (happened before I got defensive myself) supports anything but a "boys club" interpretation?

                  \> Philosopher Kate Manne defines sexism as one branch of a patriarchal order. In her definition, sexism rationalizes and justifies patriarchal norms, in contrast with misogyny, the branch which polices and enforces patriarchal norms. *Manne says that sexism often attempts to make patriarchal social arrangements *seem natural, good, or inevitable\* so that there appears to be no reason to resist them\*.

                  \>...

                  \> Gender stereotypes are widely held beliefs about the characteristics and behavior of women and men.\[78\] Empirical studies have found widely shared cultural beliefs that men are more socially valued and more competent than women in a number of activities.\[79\]\[80\] Dustin B. Thoman and others (2008) hypothesize that "\[t\]he socio-cultural salience of ability versus other components of the gender-math stereotype may impact women pursuing math". Through the experiment comparing the math outcomes of women under two various gender-math stereotype components, which are the ability of math and the effort on math respectively, Thoman and others found that women's math performance is more likely to be affected by the negative ability stereotype, which is influenced by sociocultural beliefs in the United States, rather than the effort component. As a result of this experiment and the sociocultural beliefs in the United States, Thoman and others concluded that individuals' academic outcomes can be affected by the gender-math stereotype component that is influenced by the sociocultural beliefs.\[81\]

                  [https://en.wikipedia.org/wiki/Sexism](<https://en.wikipedia.org/wiki/Sexism>)

  - **LeanderK** · [2021-12-06 14:15 UTC](https://news.ycombinator.com/item?id=29459952)
    I think being low-cost is very important, otherwise I wouldn't consider it. I don't live near a major road, but in a small city. I don't think the air-quality is bad, but I also don't know for sure. I would not invest a significant amount of money (more than 10-15€). ^c29459952

    - **Someone1234** · [2021-12-06 14:29 UTC](https://news.ycombinator.com/item?id=29460098)
      I've found a lot of indoor sources of contaminants for example cheese that fell off a Pizza onto the oven floor will put you into "yellow" the next time you run the oven. ^c29460098

    - **TheBlerch** · [2021-12-06 14:25 UTC](https://news.ycombinator.com/item?id=29460056)
      You may find the Breezometer app helpful - I’ve found it quite accurate for local outdoor air quality in several different areas. ^c29460056

  - **azth** · [2021-12-06 14:17 UTC](https://news.ycombinator.com/item?id=29459972)
    \> - The spouse-acceptance-factor is extremely high (unlike e.g. a couple of circuit boards wired together off of Aliexpress). ^c29459972

    Which circuit boards do you recommend that have high accuracy that can be ordered?

    - **ahaucnx** · [2021-12-06 14:23 UTC](https://news.ycombinator.com/item?id=29460024)
      I can recommed the Plantower 5003 PM sensor. Plantower also has smaller ones, e.g. 7003 or A003 but we get the best (most accurate and stable) readings from the 5003 model. ^c29460024

      We also experienced with more expensive ones e.g. from Sensirion but did not really measure a significant advantage compared to the Plantower.

- **DannyBee** · [2021-12-06 15:19 UTC](https://news.ycombinator.com/item?id=29460741)
  I would be very careful with this kind of evaluation. There are lots of sensors that perform well vs reference instruments but not in the field. ^c29460741

  If you want real evaluations, SCAQMD (the folks in charge of air quality for southern california) do evaluations of commercially available, low cost sensors, both against reference instruments and the lab.

  See [http://www.aqmd.gov/aq-spec/evaluations](<http://www.aqmd.gov/aq-spec/evaluations>)

  You can see what i said is true from the table - *lots* of sensors that are very well correlated with reference instruments in the lab, but suck horribly in the field.

  I would think you would be better off submitting the sensor in question to them, and letting them put it through its paces.

  (They publish within a month of finishing testing, and testing takes \~8 weeks)

  - **dognotdog** · [2021-12-06 16:05 UTC](https://news.ycombinator.com/item?id=29461398)
    IMO, the single biggest problem is that even five-figure reference instruments disagree considerably in the 0-20 ug/m3 range, and if you look at the figures of the SCAQMD tests, you won't see much more than noise in the scatter plots in that range, with increasing consistency at larger concentrations. Some of this is due to mismatches in response times and synchronization, but a lot of it is due to different disturbances, noise processes, and varying sensitivities to different particle size distributions in different sensor types. ^c29461398

    With inexpensive optical scattering sensors, the situation is even worse. While it is easy enough enough to "count" individual 2.5um particles, the scattering equations work out to an order of 10\^6 reduction in scattering amplitude, per particle, going down to 0.3um (when measured with red or infra-red light), and different particle compositions will scatter differently. On top of that, the number of particles increases significantly per unit mass concentration, making the signal processing a lot harder once one can't just threshold individual "blips" in the signal.

    Whether the sensors are particle counting or nephelometric in principle, the basic trade-off is that to see smaller particles, they need higher amplification factors, which in turn increases thermal noise, also amplifies stray light, and makes the device more sensitive to EM interference. Many signal processing pipelines do simplistic noise filtering, throwing out much of the baby with the bathwater.

    On top of these principal difficulties, the optical scattering type sensors are quite sensitive to temperature variation, and aging of the photoelectronic components, which is why field tests under varied conditions often depress their accuracy even further.

    Long story short, it is very easy to build a sensor with qualitatively good correlations to actual PM concentration, as long as the PM concentration is sufficiently high, but the health effects have no threshold, and every added bit of pollution counts, starting at zero. Unfortunately, commodity PM sensors are quite bad at quantifying these low, yet meaningful, ambient pollutant levels, which is probably why IKEA chose their traffic light thresholds the way the did: not because of how it relates to health, but because this is what they could do with a \$12 device.

  - **jiveturkey** · [2021-12-06 19:33 UTC](https://news.ycombinator.com/item?id=29464469)
    \+1 ^c29464469

    I don't have a problem with the OP's analysis of the Ikea sensor. It seems generally reasonable. But rather with their implication that the DIY sensor being promoted is of higher quality.

    Because accuracy is very much a "finished product" implementation issue, not just the sensor itself, such implication is off-base, particularly in direct comparison to any finished commercial product. The accuracy of the DIY version is going to vary -- a lot -- depending on the builder of such.

    I wonder if AQMD would evaluate a "reference build" of the DIY sensor, seeing as there is an enclosure as part of the "reference" implementation. At bare minimum, the airgradient site should have comparison to highly ranked (by AQMD) sensors, such as purple air. I'm actually quite surprised there are no such comparisons on the site.

  - **hedora** · [2021-12-06 17:01 UTC](https://news.ycombinator.com/item?id=29462323)
    Thanks for the link; that’s a great resource! ^c29462323

    To summarize their current results:  Purple Air (especially version 2) is the only one that doesn’t suck at measuring PM 2.5.  None of the consumer-targeted gaseous sensors they tested work.

    Did I miss something?  Is some other third party running more comprehensive tests?

    - **DannyBee** · [2021-12-06 17:23 UTC](https://news.ycombinator.com/item?id=29462650)
      Assuming you care PM1.0/PM2.5 (which are what are truly harmful), and want R\^2 \>0.9: ^c29462650

      Atmotube pro
      Elitech (for PM2.5)
      Purpleair

      The field evaluations have good expositions of the underlying data in slide form.
      For sure the purpleair is the best bet that i can see.
      Note that they are pragmatic as well - if you read field evaluations, AQMD folks generally think \>0.8 R\^2 is very good.  Which probably makes sense comparing a \$50-\$250 device to a several thousand dollar reference instrument.

      Note that one serious issue is that a bunch of the sensors aren't just uncorrelated, they are often dramatically undercounting. It would be one thing if they were dramatically overcounting, and told you air was horrible when it wasn't.
      But they are actually telling you air is fine when it isn't even close to fine.

      I actually went down the same path as OP about 6 months ago. I have used a dylos meter in my old woodshop, and was building a new one, and wanted to see what the the best thing to do was.
      After a bunch of looking, i found these folks.
      I am not aware of others doing this breadth of testing.

      (It turn out the dylos meter is either accurate, or overcounts, depending on temperature/humidity.  This is actually acceptable since it won't tell me things are good when they are bad, but it also turned out the purpleair was consistently good for the same price :P)

    - **formerly\_proven** · [2021-12-06 18:02 UTC](https://news.ycombinator.com/item?id=29463279)
      So the two purpleair devices are using PM1003 and PM5003 sensors, respectively. These are available off the shelf as well. I suppose the salient question is: does purpleair calibrate / select these themselves or add anything to them (e.g. filter), or can you just use a PMS5003 for 30 bucks and get similar results? ^c29463279

      - **genewitch** · [2021-12-06 19:11 UTC](https://news.ycombinator.com/item?id=29464211)
        Afaik you can use the \$30 module and be within acceptable tolerances, but you really should have at least a temperature and humidity sensor as well, because as that changes the other sensors will report differently. ^c29464211

        I've noticed that even being exposed to pure carbon dioxide the sensors I have will increase the counts of CO, VOC, and HCHO, which is unlikely and a false read.

        I only care about CO2 for my devices, so my two \$30 sensor based devices are fine.

    - **Gatsky** · [2021-12-06 20:37 UTC](https://news.ycombinator.com/item?id=29465330)
      The Sensirion does pretty OK for the price and form factor. ^c29465330

- **zahma** · [2021-12-06 21:08 UTC](https://news.ycombinator.com/item?id=29465739)
  I think I’ve plugged this here before. Sensor is an open community trying to track pollution. You can build your own sensor by ordering a dozen or so parts for 50-100 USD off AliExpress or Amazon (or wherever else you’d prefer because there’s really nothing extraordinary here). Some sensors even go down to 1 micrometer. The firmware is built to distinguish between 1, 2.5, and 10 micrometers. I believe AQI is the standard metric that is used for  the map’s visualization. ^c29465739

  It requires minimal technical expertise, no 3D printing, no soldering, and minimal configuration.

  It’s a noble mission, and I find the granularity of data for both pollution and temperature far more telling than the estimates of more centralized systems.

  Check out the map and guide here:

  [https://sensor.community/](<https://sensor.community/>)

  [https://sensor.community/en/sensors/](<https://sensor.community/en/sensors/>)

  - **dheera** · [2021-12-06 21:35 UTC](https://news.ycombinator.com/item?id=29466028)
    I've been using a Adafruit Plantower PMSA003I and it always reads 0 even if the AQI is 90 at my place. ^c29466028

    It basically always reads 0 if the AQI is anywhere under 200, and pretty useless.

    I wonder if there is a better I2C sensor that I could use?

    - **zahma** · [2021-12-07 08:20 UTC](https://news.ycombinator.com/item?id=29470182)
      Sounds like it’s not working. There is always particulate matter to be detected, so even if you are fortunate enough to live in a low-pollution area, there should be some PM readings. The AQI is just an estimation of how healthy it is to breathe particulate matter per 8hours or ozone per 24 hours. So if the AQI is reported to be 90, it means you should definitely see *some* PM readings. My sensor was not very expensive but worked very well for a couple years until it broke a couple weeks ago, likely from moisture. Go to the guides section of the sensor community site and see which sensors they recommend. I think they’re largely interoperable. ^c29470182

      - **dheera** · [2021-12-07 17:27 UTC](https://news.ycombinator.com/item?id=29475449)
        What sensor are you using? ^c29475449

  - **rplnt** · [2021-12-06 22:01 UTC](https://news.ycombinator.com/item?id=29466267)
    Looking at the map of EU, any idea why the hole in Czech Republic? ^c29466267

    - **zahma** · [2021-12-07 08:12 UTC](https://news.ycombinator.com/item?id=29470137)
      Because it’s a voluntary community. They aren’t pulling data from other sources to aggregate onto the map. What you see on the map is a collection of individuals who have built their own sensor and keep it online. ^c29470137

      - **rplnt** · [2021-12-07 15:01 UTC](https://news.ycombinator.com/item?id=29473132)
        Yes, my question is if there's any indication why Czech Republic is special case as you can clearly see its borders. ^c29473132

- **ortusdux** · [2021-12-06 14:28 UTC](https://news.ycombinator.com/item?id=29460092)
  Does anyone know how amazon's new unit fares?  It monitors PM 2.5, CO, VOCs, temp, & humidity for 70\$.  I wouldn't buy one considering the source, but I am interested in how effective it is. ^c29460092

  [https://www.amazon.com/dp/B08W8KS8D3?&linkCode\=ll1&tag\=andro...](<https://www.amazon.com/dp/B08W8KS8D3?&linkCode=ll1&tag=androidpolice-20&linkId=94100b6ff8788125941f574f1290c259&language=en_US&ref_=as_li_ss_tl>)

- **flybrand** · [2021-12-06 16:51 UTC](https://news.ycombinator.com/item?id=29462151)
  I work at H&V - we’re one of the biggest makers of air filter media (the rolled goods / fabrics - not the actual filters). ^c29462151

  We love seeing the innovation going on in this space - any suggestions on how we could better support this growing awareness of the value of IAQ?

  - **dribblecup** · [2021-12-06 18:43 UTC](https://news.ycombinator.com/item?id=29463820)
    Sponsor open source code and open source hardware solutions that DIY folks can put together at \$300 or below price point. ^c29463820

    Gold star if you sponsor an independent test of this solution to verify its effectiveness.

    Bonus points for explaining what matters in terms of testing.

    Self-serving (which is OK in this context) points for explaining how your product mitigates the problem by demonstrating the DIY metered results.

    - **jve** · [2021-12-06 20:07 UTC](https://news.ycombinator.com/item?id=29464894)
      I mean... first of all I would like to hear what are the consequences of good/bad IAQ (Indoor Air Quality?) ^c29464894

      I'm actually more driven/interested in data/compare it to other folks, but I don't have a clue what does it mean for my health. What's the difference between PM2.5, PM10, PM1, PM0.1. What is TVOC (as in sensor description: benzene,etc Volatile organic compounds), HCHO (is for formaldehyde). How do I measure them (parent expands on these questions), what are the "norms" and, most importantly: WHY should I care about those values?

      Then ofcourse tips on HOW to decrease those particles. That's where filter comes in, yeah. First time someone said he just slaps filter on an air ventilator, I was like: "Wow, it's SO simple? Yeah, sounds logical"

      - **flybrand** · [2021-12-06 23:16 UTC](https://news.ycombinator.com/item?id=29467018)
        That’s one of the reasons I’m asking - the supply chain is really split up. ^c29467018

        1/ lots of medical studies cover benefits of better iaq

        2/ filter design is well described in academia and by filter makers (grade of media chosen, pleat type, system specs)

        For both, we could do some education modules if we did this.

    - **flybrand** · [2021-12-06 23:14 UTC](https://news.ycombinator.com/item?id=29467002)
      We can pay for the testing all day long - we are a major customer at most testing labs. ^c29467002

      How big of an award gets attention?

      \$1k for the best?  \$500 for runner ups?  Testing for all?

- **micheljansen** · [2021-12-06 14:20 UTC](https://news.ycombinator.com/item?id=29459997)
  The article already mentions connecting a Wemos D1 mini, which lead me to searching for a howto. Stumbled onto this excellent article by my old friend Guy, complete with assembly pictures: [https://style.oversubstance.net/2021/08/diy-use-an-ikea-vind...](<https://style.oversubstance.net/2021/08/diy-use-an-ikea-vindriktning-air-quality-sensor-in-home-assistant-with-esphome/>) ^c29459997

  - **jve** · [2021-12-06 23:09 UTC](https://news.ycombinator.com/item?id=29466952)
    Was super easy to follow instructions and get the same steps done. ^c29466952

    Can you/your friend point out what kind of lovelace widget is that? Named: Our VINDRIKTNING chart after normal cooking, that helpfully has  3 gradients (green/orange/red)?

    Thanks.

    - **micheljansen** · [2021-12-07 11:44 UTC](https://news.ycombinator.com/item?id=29471412)
      I'd reach out to him on Twitter (he's @guysie there). ^c29471412

- **jve** · [2021-12-06 16:15 UTC](https://news.ycombinator.com/item?id=29461551)
  Really glad this was published. I was looking at airgradient solution for PM2.5 monitoring, but while thinking - saw this @ IKEA and bought it. And it is in my short term plan to wire it with Wemos D1 so I plot values and make sense on whether IKEA air purifier helps anything or not. Because if I follow the LEDs, it's chaos - it can be RED for hours with purifier nearby. And the same without purifier - colors just like to change in my house. ^c29461551

  I have a question about precision: If the precision ±20μg/m³ - isn't it actually normal that they "extend" the green led up to 35μg/m³ then? Because that 12μg/m³ is maybe 32? Uh, looks like not even PMS5003 can reliably show you that green line with a high confidence, doesn't it?

  Btw here is a nice thread that shows you how to wire it up with Wemos D1 and connect to Home Assistant. People compare their readings with other meters, too. But someone says he bought multiple of those and even those show different numbers. Someone sees IEKA values 10x higher (for lower values, but within specified accuracy) than other sensor [https://community.home-assistant.io/t/ikea-vindriktning-air-...](<https://community.home-assistant.io/t/ikea-vindriktning-air-quality-sensor/324599/168>)

  But at least they FOLLOW the plot of more accurate sensors. I see value in that. I want to know if air purifier helps something or how much it helps.

  - **genewitch** · [2021-12-06 19:20 UTC](https://news.ycombinator.com/item?id=29464319)
    As a quick aside, both the air quality things I bought say not to rely on instantaneous readings but instead to use the aggregator average reading. One has the ability to show averages and the other is more like "if the value is consistently higher than normal it's probably correctly 'high'" - so unless there's some weirdness in the Ikea one it shouldn't be switching colors unless you are very close to the threshold. ^c29464319

    It is possible that your air filter shakes or vibrates enough that it's kicking dust up, or you have poor indoor air quality. How often do you have to replace filters and how dirty are they? For reference I live in a forest, with pollen and dirt dust and people and pet dust, poor seals on windows, and open doors/screens, as well as high humidity year round; I buy the 3M 1000-1500 filters which are pretty beefy, and they last about two months before becoming uniformly dark grey on front and back. Ideally I'd replace them monthly but they're about \$15 each and that adds up across three filters.

    I ask because I don't think my system does anything for VOC, I don't use carbon filters for the three, so I'm mostly filtering dust, pollen, clay, etc.

    - **jve** · [2021-12-06 19:57 UTC](https://news.ycombinator.com/item?id=29464766)
      I bought this unit just \~2 weeks ago? [https://www.ikea.com/us/en/p/foernuftig-air-purifier-black-6...](<https://www.ikea.com/us/en/p/foernuftig-air-purifier-black-60488069/>) ^c29464766

      So I haven't had chance to change filters yet.

      Yeah, but it has high outgoing airflow, so I suppose it shakes up dust for me. It changes to red pretty fast when starting to cook, then hours, hours to bring it down.

- **AdrianoKF** · [2021-12-06 20:11 UTC](https://news.ycombinator.com/item?id=29464949)
  I have a Vindriktning with the ESP8266 makeover sitting on the desk behind me, feeding its data into my Home Assistant instance. So far it's working great, except for one annoying detail: I'd much prefer the forced airflow fan to be on at all times, since the constant on-off cycling (around every \~10s) is quite audible and distracting in a quiet environment. ^c29464949

  - **solomonb** · [2021-12-06 20:13 UTC](https://news.ycombinator.com/item?id=29464967)
    How do you know it is working great? Have you compared it against other known sensors? ^c29464967

    - **AdrianoKF** · [2021-12-11 18:53 UTC](https://news.ycombinator.com/item?id=29523264)
      "Working great" in the sense that the modification and integration was pretty painless. In terms of output quality, I've only done a few smoke tests (pun intended) - cooking, blowing smoke over the sensor - with decent results. ^c29523264

  - **gedy** · [2021-12-07 02:01 UTC](https://news.ycombinator.com/item?id=29468350)
    You can move the fan power to the 3.3v pin on the ESP8266, runs much quieter ^c29468350

- **dahart** · [2021-12-06 16:22 UTC](https://news.ycombinator.com/item?id=29461653)
  I don’t think using the brand new WHO guidelines is very fair. Not sure when it was released, but regardless this product was likely completely designed and manufactured before the WHO guidelines were published, just a few months ago. ^c29461653

  Also, Airnow.gov still has a published scale that is *worse* than the IKEA product. [https://www.airnow.gov/aqi/aqi-basics/](<https://www.airnow.gov/aqi/aqi-basics/>). Green is 0-50, Yellow is 51-100, Orange 101-150, and Red 151-200.

  - **ahaucnx** · [2021-12-06 17:17 UTC](https://news.ycombinator.com/item?id=29462554)
    Airnow is using US AQI and not μg/m. US AQI 50 corresponds to approx. 12 μg/m. ^c29462554

    - **dahart** · [2021-12-06 17:34 UTC](https://news.ycombinator.com/item?id=29462825)
      Oh thank you, pre-coffee units fail on my part. ^c29462825

      So I’d guess most air sensors on the market aren’t necessarily classifying their readings into green-good / red-bad, or at least come with a now-outdated chart. Are there sensors that have been released and/or updated to match the new guidelines already?

- **stdbrouw** · [2021-12-06 14:39 UTC](https://news.ycombinator.com/item?id=29460222)
  The choice to display anything under 35 μg/m³ as "good" does not seem unreasonable at first glance. Indoor PM2.5 can often be higher than outdoor so that the yearly average will be pushed down by time spent outside and there is no need to have \<5 μg/m³ inside too. Also, by the author's admission the unit also measures particles larger than PM2.5 which are less harmful. There's no point in having a unit that will flash orange or red for almost everyone almost all of the time. ^c29460222

  - **srg0** · [2021-12-06 15:27 UTC](https://news.ycombinator.com/item?id=29460862)
    I think it was a conscious design decision to reduce false alarm rate. Assuming that this low cost device can be/become very inaccurate, then the designers had two choices: ^c29460862

    1) Report all alarms as detected. Eventually, the device becomes a red LED which users learn to ignore.

    2) Report a problem when the device is reasonably sure there is a problem. Green light does not necessarily mean that the air quality is good, but when the LED becomes red, it should be taken seriously.

  - **ahaucnx** · [2021-12-06 14:49 UTC](https://news.ycombinator.com/item?id=29460334)
    As I mentioned in the article it really depends on the length of the exposure and how you use the sensor. ^c29460334

    Yes in many places in Europe or North America, the outdoor air quality is most of the time good.

    However -unfortunately- there are also many places where the outdoor air quality is very unhealthy most year round and then an annual exposure to 35 μg/m³ vs 5 μg/m³ makes a big difference.

    - **aaron695** · [2021-12-06 19:27 UTC](https://news.ycombinator.com/item?id=29464392)
      [flagged] ^c29464392

      \> the outdoor air quality is most of the time good.

      This is the point, knowing when it's bad so you can change behaviour?

      When does it spike in a forest? You'd guess when it's windy? But is it seasonal? Does dust matter more the pollen, I think pollen is more PM 10. Salt from the sea breeze is bad (PM2.5), how does that mix with leaf matter in Fall?

      \>  Indoor PM2.5 can often be higher than outdoor so that the yearly average will be pushed down by time spent outside and there is no need to have \<5 μg/m³ inside too.

      This line form OP is totally incorrect.

      Indoors should be less than outdoors, unless you have a fire or smoke indoors.

      And why does "yearly average" matter? Smoking cigarettes (which is exactly the same as what we are talking about) is not about a "yearly average".

- **simonebrunozzi** · [2021-12-06 15:38 UTC](https://news.ycombinator.com/item?id=29461021)
  It's almost incredible that for something as "simple" as an air quality sensor, particularly in relation to PM2.5 (the most important metric for most buyers, IMHO), there's no simple answer as: product X costs \$50 and provides 99.X\% accuracy; product Y costs \$200 and provides 99.9X\% accuracy. ^c29461021

  Two years ago, during one of the most intense fire seasons in California, I spent a few hours studying different solutions, and ended up buying a refurbished PurpleAir sensor. It seemed to work great, but I felt it was a bit too expensive for what it was doing, too bulky, and in general not as easy to use for the ordinary person as it should be.

  Same problem with home air filters - if you want to purify the air in your house, there's too many snake-oil solutions out there, and few that are worth the spending.

  - **hedora** · [2021-12-06 17:08 UTC](https://news.ycombinator.com/item?id=29462404)
    Air filtration and monitoring are a classic market for lemons. ^c29462404

    Wirecutter has decent-ish tests of air filters, though they assume tiny New York apartments, so you have to dig around a lot to find results for larger units.

    (From reading their review, you’d think \>1000 sq ft homes are unheard of in the US, but the average is closer to 2000 sq ft)

  - **ortusdux** · [2021-12-06 16:34 UTC](https://news.ycombinator.com/item?id=29461861)
    Finding myself in a similar situation with last years fires, I have had great luck with the WINIX air filters sold at costco.  I bought 2 on sale for \$100/ea.  They are 5 staged with HEPA and charcoal filters, have a built-in air quality monitor of unknown quality (I should open one up one of these days), and they have an ok app that allows you to check air quality and adjust their settings.  Each unit includes 2 years of filters, and they look to be about \$30/year/unit to replace after that. ^c29461861

  - **s0rce** · [2021-12-06 18:54 UTC](https://news.ycombinator.com/item?id=29464004)
    If you have some electronics experience you can buy the Plantower sensors that PurpleAir uses and connect it to a microcontroller, there are guides mentioned in the comments here. ^c29464004

- **Foivos** · [2021-12-06 13:59 UTC](https://news.ycombinator.com/item?id=29459783)
  For the price it is offered, it performs very well. I am not aware of any other PM2.5 sensor at \$10. It cheapest I have seen is \$40. ^c29459783

  You can still use it to get a rough idea of your air quality and it is definitely "better than nothing (or not having it)".

  - **Semaphor** · [2021-12-06 14:31 UTC](https://news.ycombinator.com/item?id=29460125)
    The one they use for their DIY Kit \[0\] actually costs \$16-19 \[0\] at aliexpress ^c29460125

    \[0\]: [https://www.airgradient.com/diy/](<https://www.airgradient.com/diy/>)

    \[1\]: [https://www.aliexpress.com/item/32944660534.html](<https://www.aliexpress.com/item/32944660534.html>)

- **dsizzle** · [2021-12-06 14:27 UTC](https://news.ycombinator.com/item?id=29460084)
  Does anybody have any stories of how devices like this revealed a problem -- what the problem was, does an air filter fix it, etc? ^c29460084

  - **fma** · [2021-12-06 18:35 UTC](https://news.ycombinator.com/item?id=29463714)
    Yes...formaldehyde exposure is a big issue in the US. Not many know of it. I bought a new construction house, so it has new carpet, paint, cabinets, wood flooring etc has an off gas effect. I honestly it's criminal to allow builders to build like this, or material to be manufactured like this. That "new car" smell, that smell when you open up new furniture made of plywood (the glue contains formaldehyde) . ^c29463714

    There are threshold laws in the US and Europe. There are laws from OSHA that regulate where you work - but no laws that regular where you sleep! It's all driven by money, of course...material with lower formaldehyde cost more to manufacture. Just walk into a Sherwin Williams and compare their paint. The highest ones are eco friendly "Low VOC" (volatile organic compound) - so industry definitely knows about it.

    The numbers in my house were effectively off the charts and OSHA would be closing down your employer if you had this exposure at work.

    Remediation for this is essentially allow to off gas, keep windows open. Off gassing also is impacted by humidity, so may be low during winter but high in the summer or when it rains.

    Air filter DOES NOT fix this. The amount of air moved by a HVAC is peanuts compared to just opening windows for a few minutes.

    California has regulations: [https://ww2.arb.ca.gov/our-work/programs/composite-wood-prod...](<https://ww2.arb.ca.gov/our-work/programs/composite-wood-products-program/about>)

    - **GekkePrutser** · [2021-12-07 03:48 UTC](https://news.ycombinator.com/item?id=29468891)
      Some filter vendors like Xiaomi offer active carbon filters to capture formaldehyde. Not sure how well it performs but I notice it captures odours well too. ^c29468891

    - **dsizzle** · [2021-12-06 23:20 UTC](https://news.ycombinator.com/item?id=29467062)
      \> The numbers in my house were effectively off the charts ^c29467062

      Did you get a measurement done, and if so where do you go to get that?

      - **fma** · [2021-12-06 23:41 UTC](https://news.ycombinator.com/item?id=29467268)
        I got a formaldehyde detector. A "Dumb" one ([https://www.amazon.com/gp/product/B00SIYDUUM/ref\=ppx\_yo\_dt\_b...](<https://www.amazon.com/gp/product/B00SIYDUUM/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1>)) and also a Foobot - which is an IoT detector. ^c29467268

        They generically measure "VOC".

        The only reason why I knew of this is because my wife is from China and it's more regulated (kinda funny, isn't it?) and people know to let their house breathe before moving in. Otherwise I'd be celebrating our "new house smell"...which would prob linger for months and months in an average American home since families don't like to open windows.

  - **colechristensen** · [2021-12-06 15:38 UTC](https://news.ycombinator.com/item?id=29461028)
    You would be surprised how much particulate certain cooking methods produce, your home can go from 0 AQI to forest fire levels for a few hours without a filter. ^c29461028

    With the right filter and sensor, you can keep your AQI in the single digits consistently and react appropriately to particle buildup.  If you have a CO2 sensor as well you can react to CO2 buildup which is something I have experienced plenty of times in a modern apartment (not necessarily dangerous levels but levels high enough that cognitive effects should be expected). It is hard to keep indoor CO2 levels anywhere near outdoor levels without forced ventilation with the outside or living in a large house.

    - **kfarr** · [2021-12-06 19:42 UTC](https://news.ycombinator.com/item?id=29464575)
      We have an indoor purple air sensor with a color gradient indicator (from green all the way to purple and many gradients in between). Exactly as you've said we are surprised at the number of times cooking has turned the air quality horrible indoors. Further we are able to see how when air outside is smoky from wildfires that the internal air filters are doing their job. Definitely worth the cost for us in the Bay Area: [https://www2.purpleair.com/products/purpleair-pa-i-indoor](<https://www2.purpleair.com/products/purpleair-pa-i-indoor>) ^c29464575

    - **dsizzle** · [2021-12-06 17:10 UTC](https://news.ycombinator.com/item?id=29462436)
      Do you have any recs for the right filter and sensor? ^c29462436

      - **dylanz** · [2021-12-06 18:17 UTC](https://news.ycombinator.com/item?id=29463485)
        Someone referred me to [https://oransi.com/](<https://oransi.com/>) and I purchased one of the large EJ120 models.  I've had it running for a few days and my place no longer has a smell and the air just feels clean.  It's bizarre. ^c29463485

        - **amatecha** · [2021-12-06 19:17 UTC](https://news.ycombinator.com/item?id=29464287)
          Nice, thanks for the recommendation.  Is the EJ120 very audible?  Where do you place it?  Like someone mentioned elsewhere, the spouse approval factor is relevant for what air filtration solution I go with... haha ^c29464287

        - **dsizzle** · [2021-12-06 19:00 UTC](https://news.ycombinator.com/item?id=29464067)
          Doesn't look like any of those have sensors, unless I missed that? I guess one sensor is your nose in this case, ha. ^c29464067

      - **colechristensen** · [2021-12-06 23:16 UTC](https://news.ycombinator.com/item?id=29467015)
        HEPA filters which include a claim for 99.97\% filtration (HEPA is put on a lot of things that are much less useful) Honeywell makes good ones. ^c29467015

        MPR 2800 furnace filters for the box fan contraption. 3M makes good ones. Your furnace might not appreciate how much they slow down flow.

        IQAir monitors are unreasonably expensive and IOT nonsense, but still good.

  - **dirtyid** · [2021-12-06 15:24 UTC](https://news.ycombinator.com/item?id=29460821)
    I have a xiaomi air purifier with AQ detector. Scrubber seems to to help with allergies. Detector itself is pretty much a glorified smoke detector Tamagotchi toy for me. I haven't found much use for it other than to keep numbers as low / nominal as I can. For which living in a pretty clean part of the city with good air quality means being more mindful when I cook to reduce smoke. That said the high AQ alarm has saved me a couple times from leaving stove top on / burning pots. Kind of paid for itself in that sense. ^c29460821

  - **kccqzy** · [2021-12-06 19:45 UTC](https://news.ycombinator.com/item?id=29464600)
    There was a time when my air quality sensor (a Temtop device) showed suspiciously high PM2.5 in the kitchen. It turned out the kitchen oven had too much oil build up inside and required cleaning. And no, I tried both cheap and expensive air purifiers; none of them could beat opening the kitchen window or turning on the range hood (a dedicated one, not the kind attached to a microwave). In this particular case, it was also a good reminder to clean the oven. ^c29464600

- **prashnts** · [2021-12-06 14:55 UTC](https://news.ycombinator.com/item?id=29460416)
  I have a question since the author is around: ^c29460416

  My sensor was working fine for a few months. It’s located near the area I smoke, so whenever I’m smoking it changes to red quickly. And after a few minutes (10 or so) it’d go back to green.

  But for past few weeks it’s stuck at red. I disassembled it and cleaned the intake hole (which is covered with a fabric) and it worked after. However it went back to displaying red again all the time.

  So my question is whether this sensor needs frequent cleaning? If so what are the alternatives?

  - **renewiltord** · [2021-12-06 19:13 UTC](https://news.ycombinator.com/item?id=29464226)
    Out of curiosity, and with no judgment intended, what is the purpose of the air quality sensor if you are actively smoking? Is it a mechanism for you to determine whether the smoking is exposing other members of the household to second-hand smoke, etc.? ^c29464226

    I only ask because it seems to me (with no concrete research) that the smoking risk is much greater than generalized air quality risk.

  - **ahaucnx** · [2021-12-06 14:59 UTC](https://news.ycombinator.com/item?id=29460472)
    I don't really have much experience with the PM1006K in the Ikea sensor but it is not untypical that PM sensors can get "stuck" and showing high concentrations. ^c29460472

    Sometimes it helps to blow compressed air inside to push out any dust that might cover the optics but that also often does not help too much or only temporary.

    - **prashnts** · [2021-12-06 15:56 UTC](https://news.ycombinator.com/item?id=29461264)
      Thank you! I’ll try that. Building an airgradient sensor is next in my list of projects! ^c29461264

    - **skybrian** · [2021-12-06 17:45 UTC](https://news.ycombinator.com/item?id=29462999)
      I've seen this and rebooting my Temtop sensor seems to help, sometimes. ^c29462999

- **giantg2** · [2021-12-06 23:42 UTC](https://news.ycombinator.com/item?id=29467290)
  I wish I could find a home executable mold spore test procedure that will give me spore counts by types. Most of the consumer tests are next to worthless. I think all I need is a fan with known volume of flow through some .3 micron filter paper, then I can check it under a microscope (guess the filter paper could use a grid, unless my hemocytomer will cast shadow through the paper. ^c29467290

- **djanogo** · [2021-12-06 17:38 UTC](https://news.ycombinator.com/item?id=29462876)
  Playing devil's advocate, this device is obviously made for mass market(\$11.99), what if the WHO/AQI "Good" numbers are too hard to achieve for general consumers?, the buyers of this device might be venturing into clean air for the first time and the last thing they want to see is "orange/red" ALL the time. ^c29462876

  - **blacksmith\_tb** · [2021-12-06 17:44 UTC](https://news.ycombinator.com/item?id=29462975)
    I bought three Vindriktnings when they came out, and on a day when we had some wildfire smoke making outdoor air quality around 150 put all three outside. Two went yellow then red, while the third stayed green... I guess I'd prefer a false positive to a false negative personally. It's true, they only cost me \$13 each, so not a huge loss but it does suggest there are quality control problems with either the sensor or the whole device. ^c29462975

  - **NamTaf** · [2021-12-07 00:30 UTC](https://news.ycombinator.com/item?id=29467685)
    I think it's folly to try to cater for the type of person who buys a product, has it identify an issue, then blames the product for identifying the issue. ^c29467685

- **GatorD42** · [2021-12-06 15:40 UTC](https://news.ycombinator.com/item?id=29461050)
  The color guides seem similar to the IQAir AirVisual Pro and Apple’s weather app. Like the article mentions this is likely to be inside and most useful for alerting when cooking has caused significant particle emissions, that’s what I use my AirVisual for. ^c29461050

- **thecal** · [2021-12-06 13:56 UTC](https://news.ycombinator.com/item?id=29459760)
  Direct link to the item: [https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor...](<https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor-60515911/>) ^c29459760

- **pnathan** · [2021-12-06 18:17 UTC](https://news.ycombinator.com/item?id=29463494)
  When I was looking into air quality a year or two ago, I realized that the color-coded "AQI" so popular are not precisely a scientific analysis, as they are a blend of different measurements, with cutoffs specified by committee. Different countries have different formulas for AQI. That doesn't make them wrong, but it makes them not a "gospel truth". ^c29463494

  I have a Dylos rigged up inside my apartment, feeding particle measurement data to a serial port, which stores the data on my own cloud. I don't bother with AQI.

- **intrasight** · [2021-12-06 15:27 UTC](https://news.ycombinator.com/item?id=29460868)
  [http://energysmartohio.com/indoor-air-quality/which-indoor-a...](<http://energysmartohio.com/indoor-air-quality/which-indoor-air-quality-monitors-are-best-and-why/>) ^c29460868

  I've always returned to the Dylos sensor as the gold standard

  Another good review of sensors: [http://www.aqmd.gov/aq-spec/evaluations/summary-pm](<http://www.aqmd.gov/aq-spec/evaluations/summary-pm>)

- **punnerud** · [2021-12-06 14:53 UTC](https://news.ycombinator.com/item?id=29460389)
  Archived version (from today):
  [https://web.archive.org/web/20211206144732/https://www.airgr...](<https://web.archive.org/web/20211206144732/https://www.airgradient.com/resources/ikea-vindriktning-accuracy/>) ^c29460389

- **rceDia** · [2021-12-06 14:20 UTC](https://news.ycombinator.com/item?id=29460006)
  Cheap, easy to use is o.k. not sure of reliability. Another IOT at home air quality solution is Purple Air. Offers units for outdoor or indoor. Not as cheap as IKEA but affordable.
  [https://www2.purpleair.com/](<https://www2.purpleair.com/>) ^c29460006

  - **micheljansen** · [2021-12-06 14:25 UTC](https://news.ycombinator.com/item?id=29460053)
    \$200 for the cheapest model though. That's a factor 20! ^c29460053

- **maltalex** · [2021-12-06 15:40 UTC](https://news.ycombinator.com/item?id=29461055)
  Say I'm convinced enough to order an AirGradient kit. Is this accurate? Does it take up to 5 weeks for *most* destinations? ^c29461055

  \> We currently ship approximately 1-2 weeks after receipt of payments. Delivery takes 2-3 weeks to most destinations (North America, Europe, Australia).

  - **ahaucnx** · [2021-12-06 15:51 UTC](https://news.ycombinator.com/item?id=29461196)
    The shipping times mentioned on the website are a bit conservative and often it is faster. ^c29461196

    We currently have kits in stock and ship within a few days of orders received.

    Shipping times really vary depending on destination and are hard to predict but 2-3 weeks is a good estimation.

- **FPGAhacker** · [2021-12-06 23:36 UTC](https://news.ycombinator.com/item?id=29467219)
  \> Green: 0-35 /Good + Low ^c29467219

  \> Amber: 36-85/OK + Medium

  \> Red: 86- /Not good + High

  I absolutely despise this pattern. You could not pick a worse set of colors for the most common form of color blindness.

  - **Spivak** · [2021-12-07 01:01 UTC](https://news.ycombinator.com/item?id=29467933)
    It's not so bad because it operates on the same philosophy as street lights. Even if you were completely color blind you would still be able to tell. This is how it appears in real life. ^c29467933


    ```
        +---+      +---+      +---+
        |   | Good |   | Fair | * | Poor
        | * | <--  | * | <--  | * | <--
        | * |      |   |      |   |
        +---+      +---+      +---+
    ```

- **dheera** · [2021-12-06 21:35 UTC](https://news.ycombinator.com/item?id=29466021)
  I've been using a Adafruit Plantower PMSA003I and it always reads 0 even if the AQI is 90 at my place. ^c29466021

  It basically always reads 0 if the AQI is anywhere under 200, and pretty useless.

- **jansan** · [2021-12-06 13:54 UTC](https://news.ycombinator.com/item?id=29459732)
  My takeaway from the article: Buy the sensor, make sure air quality is in the "good" range (green light) and you will be fine. I think I will order a few. ^c29459732

  - **blackbear\_** · [2021-12-06 14:09 UTC](https://news.ycombinator.com/item?id=29459883)
    \> Conclusion: \[...\] However, the defined cut off values for the air quality and its description as “Good”, “OK”, and “Not Good” are not based on science or international recommendations and create the false understanding that the air is good, when in fact it is not good at all. ^c29459883

    - **jansan** · [2021-12-06 15:29 UTC](https://news.ycombinator.com/item?id=29460890)
      Considering that the article was basically written by somone who is selling competing products I would take this statement with a truckload of salt. ^c29460890

      - **colechristensen** · [2021-12-06 15:42 UTC](https://news.ycombinator.com/item?id=29461080)
        I’m not selling anything and unless the writer is outright lying about the number ranges, I agree with them.  The “green” range is way too lenient and the sensor will only help you keep away from really terrible air quality, most people would have it green always while doing nothing at all. ^c29461080

        - **jansan** · [2021-12-06 16:23 UTC](https://news.ycombinator.com/item?id=29461661)
          As I understand it "yellow" will indicate better air quality than "Unhealthy for Sensitive Groups" according to the US standard. I see a difference between "Unhealthy for Sensitive Groups" and "really terrible air quality" as you describe it. ^c29461661

          - **colechristensen** · [2021-12-06 23:19 UTC](https://news.ycombinator.com/item?id=29467055)
            There's acutely unhealthy for sensitive groups and there's long term unhealthy for anyone. ^c29467055

            Convincing reasons exist to think that significantly lower levels than are acutely unhealthy have long term health impacts.  On top of that, you don't really need a sensor to know whether or not your air has particulate levels that are acutely unhealthy, you just know it.

            If you don't care or only want to know if your air is quite bad, sure, buy one of these. I don't think it's a reasonable level, but you do you.

  - **tdrdt** · [2021-12-06 13:57 UTC](https://news.ycombinator.com/item?id=29459765)
    Exactly. Recently I bought a very cheap CO2 meter. It is inaccurate, but still accurate enough for 99\% of the people. ^c29459765

    - **numpad0** · [2021-12-06 14:32 UTC](https://news.ycombinator.com/item?id=29460143)
      Referring to acetone detectors with lousy linear lookup feature as “eCO2 sensor” is infuriating but do I must admit it’s an okay reminder for room occupants to open windows… ^c29460143

    - **TheBlerch** · [2021-12-06 14:19 UTC](https://news.ycombinator.com/item?id=29459987)
      Which CO2 meter did you get, how accurate is it and how much did it cost? Agreed people just need a meter good enough to tell them when air quality isn’t good. ^c29459987

      - **tdrdt** · [2021-12-06 14:36 UTC](https://news.ycombinator.com/item?id=29460186)
        The brand is Simr, but I think there are only 3 or 4 meters that are sold as whitelabel and rebranded a thousand times.
        I think it was around \$30. ^c29460186

        Outside it measures around 400ppm so the base point is good. Inside it measures 480ppm with good ventilation. When someone farts it goes to 2000ppm for a while. So I think it measures 'alright'.

        - **mh-** · [2021-12-06 15:27 UTC](https://news.ycombinator.com/item?id=29460857)
          I'd pay \$30 for a fart detector. CO2 accuracy would just be a bonus ^c29460857

  - **etimberg** · [2021-12-06 14:07 UTC](https://news.ycombinator.com/item?id=29459863)
    Agreed. I think I will buy at least one given that the cost is so low. ^c29459863

- **jerjerjer** · [2021-12-06 14:13 UTC](https://news.ycombinator.com/item?id=29459921)
  Anything proven and with a better sensor quality? ^c29459921

- **Animats** · [2021-12-06 19:50 UTC](https://news.ycombinator.com/item?id=29464672)
  That's just particles. No CO2 sensor. ^c29464672

  - **mpalczewski** · [2021-12-06 22:45 UTC](https://news.ycombinator.com/item?id=29466708)
    Just to add to this: ^c29466708

    CO2 is important because it is a proxy for how much air you are rebreathing.  This is especially important because of Covid.  If you have a few people in a poorly ventilated room co2 will climb.  Whereas in a well ventilated room, it might be nearly as good as being outside.

    Even for just being at home this is important because if the air is poorly ventilated it will feel "stuffy".  It can affect how well you are able to think and work.

    Most air quality meter's only measure pollution, and you have to get an expensive one to measure co2 which is why it is frequently omitted despite importance.

    - **eb0la** · [2021-12-07 00:11 UTC](https://news.ycombinator.com/item?id=29467567)
      Not just Covid. In an office environment or a school, you need to be under 1000ppm: ^c29467567

      Effects of low-level inhalation exposure to carbon dioxide in indoor environments: A short review on human health and psychomotor performance
      [https://www.sciencedirect.com/science/article/pii/S016041201...](<https://www.sciencedirect.com/science/article/pii/S0160412018312807>)

    - **knownjorbist** · [2021-12-07 00:47 UTC](https://news.ycombinator.com/item?id=29467822)
      What are good CO2 monitoring options near this price point? ^c29467822

      - **mpalczewski** · [2021-12-07 22:23 UTC](https://news.ycombinator.com/item?id=29478985)
        I don't believe there are any. ^c29478985

- **liversage** · [2021-12-06 17:29 UTC](https://news.ycombinator.com/item?id=29462735)
  Some trivia: ‘Vindriktning‘ is ‘wind direction' in Swedish. ^c29462735

- **unknown** · [2021-12-06 15:23 UTC](https://news.ycombinator.com/item?id=29460799)
  [deleted] ^c29460799

- **baxuz** · [2021-12-06 13:55 UTC](https://news.ycombinator.com/item?id=29459747)
  Oh, I was just about to buy a few. ^c29459747

  - **unknown** · [2021-12-06 18:10 UTC](https://news.ycombinator.com/item?id=29463412)
    [deleted] ^c29463412

- **errcorrectcode** · [2021-12-06 14:17 UTC](https://news.ycombinator.com/item?id=29459963)
  [flagged] ^c29459963

  Nope, just nope. Ikea: purveyors of chemical-laden flat packs and cheap, unrepairable items that don't last. PMS5003 modules are much better (PM1, 2.5, and 10) and only cost \$20. PM1 and 2.5 are far more damaging to health than PM10.

  - **Swenrekcah** · [2021-12-06 14:31 UTC](https://news.ycombinator.com/item?id=29460134)
    Almost all furniture I’ve ever owned has been IKEA. With very few exceptions they have all been very durable. Repairability is excellent because everything is designed to be taken apart by amateurs and spare parts are easily found. They are also easy when moving because they can so easily be taken apart. ^c29460134

    - **errcorrectcode** · [2021-12-06 14:38 UTC](https://news.ycombinator.com/item?id=29460211)
      [flagged] ^c29460211

      It wouldn't need spare parts if it didn't break. "Very durable" compared to what since you have no experience with anything else? Not solid wood furniture.

      A table that weighs 8 lbs and costs 10 dollars should only be used on a Hollywood set as breakaway furniture for safety.

      You sound like you're rationalizing a religious tribe rather than making a rational argument.

      - **slantyyz** · [2021-12-06 14:59 UTC](https://news.ycombinator.com/item?id=29460465)
        \> You sound like you're rationalizing a religious tribe rather than making a rational argument. ^c29460465

        So do you, actually.

        IKEA has products of varying price points. Yeah some of the cheap stuff might be pretty bad. Having said that, I have family members with IKEA furniture that is now around 30 years old without issues.

        I have expensive solid wood furniture as well as IKEA furniture. Some of my own IKEA pieces that I bought after finishing uni have lasted 30 years and are still in use. I don't think I've thrown any IKEA furniture out, only passed them on to other people.

        - **errcorrectcode** · [2021-12-06 15:34 UTC](https://news.ycombinator.com/item?id=29460965)
          [flagged] ^c29460965

          You're appear to be seeking conflict with a lame, baseless, personal attack because you are also a part of that cult and can't handle criticism.

          30 years is nothing. I have 200 year old solid wood furniture. I seriously doubt anything made from sawdust will ever last that long.

          I hope you and your family enjoy your IKEA decor.

          - **slantyyz** · [2021-12-06 15:44 UTC](https://news.ycombinator.com/item?id=29461102)
            \> You're appear to be seeking conflict with a lame, baseless, personal attack because you are also a part of that cult and can't handle criticism. ^c29461102

            Um, ok. I guess you got me there.

            \> 30 years is nothing. I have 200 year old solid wood furniture. I seriously doubt anything made from sawdust will ever last that long.

            Ok, good for you then? I don't need anything to last 200 years, but I wouldn't be surprised if my sawdust furniture lasts longer than me, since I take pretty good care of my furniture.

            \> I hope you and your family enjoy your IKEA decor.

            Yep.

      - **maltalex** · [2021-12-06 14:58 UTC](https://news.ycombinator.com/item?id=29460450)
        \> You sound like you're rationalizing a religious tribe rather than making a rational argument. ^c29460450

        I can't believe that I find myself defending Ikea on HN, but... what?

        The parent's argument is very rational - in their experience products have been durable, and the repairability high for obvious reasons. What's religious about that?

        I owned several pieces of Ikea furniture myself, and some were well made out of solid materials. Others were not. Unsurprisingly, the material quality was strongly correlated with the price of the item.

        - **errcorrectcode** · [2021-12-06 15:28 UTC](https://news.ycombinator.com/item?id=29460885)
          [flagged] ^c29460885

          Myopia from limited experience is absurdly arrogant.

          I have experience with O'Sullivan, IKEA, and fine furniture like Stickley. You can't sand or paint sawdust when it crumbles. If it gets wet, it's ruined. Fine furniture often appreciates in value, while pressed dust doesn't, falls apart when disassembled, and cannot be economically repaired.

          - **slantyyz** · [2021-12-06 15:38 UTC](https://news.ycombinator.com/item?id=29461018)
            \> falls apart when disassembled ^c29461018

            Funny, in the 30+ years that I've had IKEA furniture, I've moved several times. That you can disassemble IKEA furniture is a benefit when moving, and I've had no issues disassembling and reassembling multiple times.

      - **avh02** · [2021-12-06 14:56 UTC](https://news.ycombinator.com/item?id=29460432)
        \> It wouldn't need spare parts if it didn't break ^c29460432

        I guess you've never lost a single screw in your life.

        - **unknown** · [2021-12-06 15:29 UTC](https://news.ycombinator.com/item?id=29460902)
          [deleted] ^c29460902

        - **errcorrectcode** · [2021-12-06 15:29 UTC](https://news.ycombinator.com/item?id=29460897)
          [flagged] ^c29460897

          Cheap shot. Maybe you shouldn't be commenting today.

  - **hedora** · [2021-12-06 15:49 UTC](https://news.ycombinator.com/item?id=29461168)
    Ikea has multiple price tiers (e.g. “good”, better, best).  The bottom tier is basically disposable dorm furniture, which is likely to be ruined/tossed anyway.  Move up a tier if you want something that’s cheaper than other alternatives and lasts. ^c29461168

    The only thing I’ve found that competes with their mid tier is used furniture.  (Which is obviously better for the environment than buying new.)

    - **handrous** · [2021-12-06 17:23 UTC](https://news.ycombinator.com/item?id=29462654)
      I can only assume people who complain about Ikea—price, assembly instructions, quality, et c.—have never experienced other flat-pack furniture, like what Wal-Mart or Target stock, which is worse on *all* of those measures. Or most bulky, ugly, fake-fancy big box furniture, even not flat-packed. ^c29462654

      I can only beat them on quality-per-dollar by going used, as you note—mid-century-modern used furniture is expensive (and is what a lot of Ikea stuff is designed after) but anything earlier or later is usually very cheap.

      Brands that consistently provide better quality for non-flat-pack furniture tend to be *way* more expensive than Ikea, outside the range of what most normal folks are even considering.

      And yeah, it's true that their cheapest tier is practically disposable, but it's hard to complain when an end table costs \$20 or whatever. Of course it's not gonna last decades, at that price.

    - **robin\_reala** · [2021-12-06 15:58 UTC](https://news.ycombinator.com/item?id=29461303)
      \[Disclaimer: IKEA employee\] ^c29461303

      We’ve got buy back / resale programmes globally, and the US trialled it a couple of months ago. I’d expect to see this expand over time.

      [https://www.ikea.com/us/en/newsroom/corporate-news/ikea-us-h...](<https://www.ikea.com/us/en/newsroom/corporate-news/ikea-us-helps-customers-prolong-the-life-of-their-furniture-with-launch-of-buy-back-and-resell-service-puba9b1f107>)

      - **hedora** · [2021-12-06 16:25 UTC](https://news.ycombinator.com/item?id=29461696)
        Oh wow, that’s great!  The less resources Ikea consumes, the better. ^c29461696

        However, I was referring to Craigslist “free” listings and antique shops.  I suspect those will continue to win out on price or craftsmanship over most stuff Ikea sells.  It’s hard to beat items that are free and/or hand-crafted from old growth hardwood.

        Our house is split roughly evenly between free stuff, antiques, and ikea stuff.

    - **mnw21cam** · [2021-12-06 17:17 UTC](https://news.ycombinator.com/item?id=29462558)
      I have a folding dining table from ikea. It's \%&(\*! heavy, surprisingly so for a small table, and is solid wood. It has already lasted 15 years and I can see it lasting another 100. ^c29462558

      Agreed, ikea sells some flimsy stuff, but they also sell some really solid stuff.

      - **xvf22** · [2021-12-07 02:11 UTC](https://news.ycombinator.com/item?id=29468416)
        I'll say this, the Ikea stuff my parents had incorporated a hell of a lot more solid wood than I see today. ^c29468416

