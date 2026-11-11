# [AirGradient Open Source Air Quality Monitor for CO2 and PM2.5 Measurements](https://news.ycombinator.com/item?id=34571885)

Article: [https://www.airgradient.com/open-airgradient/instructions/diy-pro-v37/](<https://www.airgradient.com/open-airgradient/instructions/diy-pro-v37/>)

ahaucnx · 2023-01-29 19:42 UTC · 159 reported comments · archived 2026-11-08 12:37 UTC
Observation: 2026-11-08 12:36 UTC → 2026-11-08 12:37 UTC

## Comments

- **pppone** · [2023-01-29 21:39 UTC](https://news.ycombinator.com/item?id=34573044)
  I would recommend checking out the AQ-SPEC program \[1\]. They do quite comprehensive tests on low-cost air quality sensors.  My side project with a few friends \[2\] chose to use the Sensirion SPS30 \[3\] for our portable PM2.5 monitor.  As mentioned by others, it's a bit more expensive than the PMS5003 used by AirGradient, but we preferred its documentation, company reputation, and form factor at the time of choosing (2019).  The PMS5003 is perfectly capable, and has demonstrated good success with many projects/companies using the sensor (e.g. PurpleAir). However, a quick search suggests there are some issues with a recent batch of these sensors \[4\]. ^c34573044

  \[1\]: [https://www.aqmd.gov/aq-spec/sensors](<https://www.aqmd.gov/aq-spec/sensors>)

  \[2\]: [https://www.open-seneca.org/](<https://www.open-seneca.org/>)

  \[3\]: [https://sensirion.com/products/catalog/SPS30/](<https://sensirion.com/products/catalog/SPS30/>)

  \[4\]: [https://community.purpleair.com/t/new-version-of-plantower-p...](<https://community.purpleair.com/t/new-version-of-plantower-pms5003/288>)

  - **rkagerer** · [2023-01-30 06:22 UTC](https://news.ycombinator.com/item?id=34576445)
    This resource is amazing. ^c34576445

    I bought a Dylos DC1700-PM a while back for around \$400; interesting to see how the lab test shows it producing varying data at 65\%+ humidity (I live in a fairly humid climate and that perhaps contributes to why I see large shifts in readings throughout the day).

    Is there a good, sub-\$3000 meter that is accurate, 'just works', and requires little to no maintenance?

  - **kayson** · [2023-01-30 06:04 UTC](https://news.ycombinator.com/item?id=34576327)
    Ooof based on the aq-spec summaries... None of the gas sensors are particularly good. And the best ones are thousands of dollars.. ^c34576327

  - **unknown** · [2023-01-30 05:12 UTC](https://news.ycombinator.com/item?id=34575999)
    [deleted] ^c34575999

  - **NathanielK** · [2023-01-30 01:37 UTC](https://news.ycombinator.com/item?id=34574837)
    That program is excellent! I purchased an AtmotubePro for PM2.5 measuring, and their testing and confirming it uses and SP30 makes me much more confident in it's readings. ^c34574837

    - **belter** · [2023-01-30 18:56 UTC](https://news.ycombinator.com/item?id=34584659)
      It's a shame its does not seem to do CO2 only a compound measure of VOC gases. It seems only the Atmo Cube has CO2 measures. ^c34584659

  - **newman314** · [2023-01-29 23:53 UTC](https://news.ycombinator.com/item?id=34574089)
    Your site does not appear to have pricing for your kit based on brief browsing. ^c34574089

    - **pppone** · [2023-01-30 12:22 UTC](https://news.ycombinator.com/item?id=34578751)
      Sadly not yet. Since this is more of a voluntary commitment amongst my friends and I (we're in the process of finishing our PhDs), we lack the human-power to take the product to market at the moment. ^c34578751

    - **chubbnix** · [2023-01-30 00:39 UTC](https://news.ycombinator.com/item?id=34574414)
      They are about \$50 from my search which is about 5x more than the plantower pm2.5 sensors. There is a big difference in documentation and that issue with the new MCU on the plantower units is concerning since they all have the same markings and housing when purchased. ^c34574414

      - **pppone** · [2023-01-30 12:33 UTC](https://news.ycombinator.com/item?id=34578844)
        At volume, the SPS30 gets down to \~\$30 a piece. Their newest sensors (SEN5X) offer similar specs, and are about \$25 per single unit, or \$15 a piece at volume for the cheapest variant.  The more expensive variant include integrated T/RH monitoring, which is very handy for humidity corrections for this type of PM2.5 sensing. ^c34578844

- **NikolaNovak** · [2023-01-29 22:33 UTC](https://news.ycombinator.com/item?id=34573477)
  Open source diy is wonderful. But is there a reliable trustworthy monitor that can just... Be bought? A box that will reliably tell me what's the carbon dioxide carbon monoxide dust allergens volatile compounds? Am I possibly being greedy and I need several konitors (I wouldn't have an issue with that)? ^c34573477

  Every review I check for any consumer accessible device seems to indicate they're inaccurate, miscalibrated, or downright deceptive :-(

  - **daniel\_iversen** · [2023-01-29 23:50 UTC](https://news.ycombinator.com/item?id=34574073)
    I got the uHoo Air Quality Monitor\[1\] and I love it. One of the few nice smart-home/app ones to monitor carbon monoxide too. But it's pricey. I can probably get some discount codes from them if the HN community is interested (I've spoken with their team once before in Singapore and they were very nice and accommodating!) ^c34574073

    \[1\] [https://getuhoo.com/](<https://getuhoo.com/>)

    - **XorNot** · [2023-01-30 03:11 UTC](https://news.ycombinator.com/item?id=34575398)
      I have this one too, but yeah, it was expensive when I got it and has only gone up. I also don't love the dependency on a remote cloud. ^c34575398

      What I'd like is a box which would just host an HTTP endpoint on my wifi network, and respond with a Prometheus metric endpoint (maybe throw JSON in there so it can give a "device specific" super accurate response too).

      Let the community worry about the rest of the integration.

    - **thatcat** · [2023-01-30 00:45 UTC](https://news.ycombinator.com/item?id=34574462)
      Hey, have you tested it much? This evaluation site shows weirdly low r\^2 values of 0.0, but maybe they just haven't evaluated it. [http://www.aqmd.gov/aq-spec/evaluations](<http://www.aqmd.gov/aq-spec/evaluations>) ^c34574462

    - **revicon** · [2023-01-30 01:57 UTC](https://news.ycombinator.com/item?id=34574977)
      I own this one as well.  I’ve been pleasantly surprised at how well it works and how quickly I can see changes when it alerts me to a CO2 buildup and I go open some doors.  It’s satisfying to be able to see the effect fresh air has on my environment watching their charts. ^c34574977

      I picked this one because it also monitors Nitrogen Monoxide which gas stoves give off which many other air monitors do not test for.

      I haven’t tried their IFTTT integration though, that will be next.

  - **tomaskafka** · [2023-01-29 23:05 UTC](https://news.ycombinator.com/item?id=34573737)
    Anything under \$60 doesn't have a 'real' CO2 sensor. One of the good budget ones is Cleargrass Air Monitor. ^c34573737

    - **s0rce** · [2023-01-29 23:53 UTC](https://news.ycombinator.com/item?id=34574090)
      You can diy for under 60 with a photoacoustic SCD41. ^c34574090

  - **karmelapple** · [2023-01-29 23:07 UTC](https://news.ycombinator.com/item?id=34573757)
    The Aranet has worked well for me, and I think is calibrated well and works smoothly. It’s not the cheapest though, but I haven’t recharged it in over a year… almost two years now! ^c34573757

    [https://a.co/d/9o1Qvzb](<https://a.co/d/9o1Qvzb>)

    - **throwaranay4933** · [2023-01-30 19:25 UTC](https://news.ycombinator.com/item?id=34585071)
      Great product. You can get data into Prometheus with [https://github.com/ryansouza/aranet4-exporter-go](<https://github.com/ryansouza/aranet4-exporter-go>) too. ^c34585071

    - **symlinkk** · [2023-01-29 23:13 UTC](https://news.ycombinator.com/item?id=34573800)
      This is the right pick, because it has an NDIR sensor. ^c34573800

      - **karmelapple** · [2023-01-30 02:54 UTC](https://news.ycombinator.com/item?id=34575323)
        Yeah, I did a bunch of research before I got one. I was primarily interested in CO2. It was very interesting in the earlier days of covid-19, but it’s still interesting now, even around home. I have noticed how the CO2 level spikes to 1200 or more when I turn on my gas stove. That, along with recently learning about how gas stoves can cause issues for children, have me planning to get an induction stove very soon. ^c34575323

    - **NikolaNovak** · [2023-01-30 03:27 UTC](https://news.ycombinator.com/item?id=34575465)
      That one only does co2 though, am I correct? It would not help me with allergens or dust etc ^c34575465

      - **jve** · [2023-01-30 13:42 UTC](https://news.ycombinator.com/item?id=34579432)
        Yes, CO2/temp/humidity only. ^c34579432

        We have one in office, I think more than 2 years already and haven't changed batteries. Bought new one, compared readings and CO2 readings were matching.

        Was trying to look whether old one should be recalibrated (per instructions, have to leave outdoors for a while every \<don't remember\> months). However our office CO2 is already \~600-700ish when people are here, so maybe it is fresh enough for recalibration.

        Ah, and home-assistant integration is finally available for Aranet [https://www.home-assistant.io/integrations/aranet/](<https://www.home-assistant.io/integrations/aranet/>)

  - **LeegleechN** · [2023-01-30 03:36 UTC](https://news.ycombinator.com/item?id=34575499)
    The Airthings View Plus is a good one. It has high quality (for consumer) particulate, CO2, VOC and Radon sensors and a good interface. Also tracks temperature, pressure, and humidity for completeness. ^c34575499

  - **blueblimp** · [2023-01-30 01:12 UTC](https://news.ycombinator.com/item?id=34574698)
    For PM2.5, the Qingping Air Monitor (or the Lite version if you prefer that) is good. The review I've read found it has decent accuracy, and, though I haven't tested it rigorously myself, the readings seem reasonable in my experience. The main reason I recommend it, though, is that the UI is great: it keeps graphs of past values that are easy to access, both on the screen and in the app. ^c34574698

    On the topic of allergens, I wasn't able to find any device that can measure that.

  - **ahaucnx** · [2023-01-29 22:53 UTC](https://news.ycombinator.com/item?id=34573632)
    PM, CO2, temperature and humidity can be fairly accurately measured with consumer monitors provided they use good sensors. ^c34573632

    You can check if the monitor is RESET AIR certified which is an independent and 3rd party test against reference devices.

    [https://www.reset.build/directory/monitors/air](<https://www.reset.build/directory/monitors/air>)

  - **dewey** · [2023-01-30 08:00 UTC](https://news.ycombinator.com/item?id=34577038)
    There will be one from Ikea coming out \[1\], I'm currently waiting for that one after selling my Awair. ^c34577038

    \[1\] [https://www.notebookcheck.net/IKEA-VINDSTYRKA-smart-air-qual...](<https://www.notebookcheck.net/IKEA-VINDSTYRKA-smart-air-quality-monitor-appears-with-integrated-display.680559.0.html>)

    - **leokennis** · [2023-01-30 10:43 UTC](https://news.ycombinator.com/item?id=34578086)
      Be aware that its "predecessor" happily: ^c34578086

      \> shows you a green light until 35 μg/m³ which is SEVEN TIMES the WHO air quality guideline. It is also around 3 times what the US AQI regards as Good.

      [https://www.airgradient.com/open-airgradient/blog/ikea-vindr...](<https://www.airgradient.com/open-airgradient/blog/ikea-vindriktning-accuracy/>)

  - **harrydehal** · [2023-01-30 05:13 UTC](https://news.ycombinator.com/item?id=34576006)
    Check out the Purple Air community map and their sensors: ^c34576006

    [https://map.purpleair.com/?mylocation](<https://map.purpleair.com/?mylocation>)

    [https://www2.purpleair.com/products/list](<https://www2.purpleair.com/products/list>)

  - **dotancohen** · [2023-01-31 10:06 UTC](https://news.ycombinator.com/item?id=34593354)
    What is wrong with an cheap device like this? ^c34593354

    [https://www.aliexpress.com/item/1005005011458177.html](<https://www.aliexpress.com/item/1005005011458177.html>)

    \$15 from AliExpress including shipping. If you are concerned about accuracy, could you not take it outdoors to see how it measures the unaffected atmosphere, then bring it back indoors to see how it compares? For instance, if you are concerned that the 900 PPM reading in your bedroom is inaccurate, you could take it outside and see how it reads compared to the expected \~420 PPM. You might be off by a few PPM, but would it not be accurate enough to see if you are approaching dangerous levels?

  - **rogers18445** · [2023-01-30 05:26 UTC](https://news.ycombinator.com/item?id=34576108)
    Sensirion CO2 Gadget is good with one of the best \[small, reasonably priced\] sensors (SCD41). Has BLE interface (with android/ios app). Only shows co2. [https://sensirion.com/products/catalog/SCD4x-CO2-Gadget/](<https://sensirion.com/products/catalog/SCD4x-CO2-Gadget/>) ^c34576108

    It does use auto calibration, which means you need to bring it outside for a few minutes every once in a while (7 days IIRC). Not doing it will not break it, but the readings will drift downward (sensor assumes that the lowest reading it gets in a period of time must be 400 ppm) - and will be fixed in a few minutes outside (few minutes of \<400 ppm sets lowest reading to 400).

    - **quinncom** · [2023-01-30 19:53 UTC](https://news.ycombinator.com/item?id=34585462)
      I’m fond of the CO2 Gadget too, but the autocalibration function takes 7 days to kick in, during which it must be plugged in continuously. This makes it impractical for use as a travel CO2 sensor when moving between two locations at different elevations. E.G., I had my Gadget calibrated for CDMX (2050m), then travelled to SF (50m) where the Gadget read 800ppm outdoors. I left the Gadget plugged in outside for four days, but it never calibrated before I left. I corresponded with an engineer at Sensirion who said it may be possible to add manual calibration via software update, and created a ticket for their product team. I hope they implement that. ^c34585462

      - **rogers18445** · [2023-01-30 22:45 UTC](https://news.ycombinator.com/item?id=34587675)
        That's interesting. For regular use however this may not be a big deal, auto calibration has a secondary mechanism by which it will recalibrate in just a few minutes if ppm \< 400. ^c34587675

        So after 8 days plugged in, the sensor is sure to be calibrated incorrectly to inside air, then you take it outside and it recalibrates again to correct values within a few minutes?

    - **summm** · [2023-01-30 09:29 UTC](https://news.ycombinator.com/item?id=34577597)
      I highly recommend Dual-NDIR sensors that bring their own volume of calibration gas. Auto calibration is not practical in any serious indoor monitoring use case. ^c34577597

      - **rogers18445** · [2023-01-30 17:32 UTC](https://news.ycombinator.com/item?id=34583275)
        How would that work? Having one sensor sealed with reference gas does nothing to help the second sensor. Is there actually a dual sensor which shuttles the gas between them? Seems complicated. ^c34583275

        - **summm** · [2023-01-30 23:12 UTC](https://news.ycombinator.com/item?id=34588018)
          it's a 2nd sealed chamber and shares some sensor parts. Some parts are different, so it's not perfect of course, but much better as the requirement of regular manual calibration. Sensirion SCD30 for example, where you can even see the Y shape of the gas chambers. ^c34588018

          - **rogers18445** · [2023-01-30 23:15 UTC](https://news.ycombinator.com/item?id=34588071)
            SCD30 also has autocalibration with outside air though? ^c34588071

  - **vijaykodam** · [2023-01-30 12:21 UTC](https://news.ycombinator.com/item?id=34578742)
    Recently bought Netatmo Smart Home weather station, which comes with both indoor and outdoor modules. It measures air quality (CO2, PM2.5) along with temperature, humidity, air pressure, sound. It has its own app and can work with Apple HomeKit and Alexa. Happy with it as of now. ^c34578742

    [https://www.netatmo.com/en-us/weather/weatherstation](<https://www.netatmo.com/en-us/weather/weatherstation>)

    - **daydream** · [2023-01-30 13:26 UTC](https://news.ycombinator.com/item?id=34579280)
      Pretty sure that Netatmo measures only CO2, not PM2.5. There’s no mention of PM2.5 on the link you posted. ^c34579280

      Also, to properly calibrate the Netatmo needs to be exposed to essentially outside air once a week as it takes the weekly lower bound as its reference point. More sophisticated sensors don’t have this limitation.

  - **shafyy** · [2023-01-30 13:04 UTC](https://news.ycombinator.com/item?id=34579071)
    I have been using the Awair for like 3 years, and it seems to work fine. I never did a test to compare it to other products, though. ^c34579071

  - **mikkelam** · [2023-01-30 08:54 UTC](https://news.ycombinator.com/item?id=34577376)
    Seems like airgradient has one [https://www.airgradient.com/airgradient-one/](<https://www.airgradient.com/airgradient-one/>) ^c34577376

    There's no pricing though and it looks like it's tied to subscription software.

  - **Forge36** · [2023-01-29 23:03 UTC](https://news.ycombinator.com/item?id=34573720)
    I spent \$30 on one and \$20 on another. They're "close enough" and I could connect them to home assistant. The reviews suggests the CO2 is off by 100 ppm. I've only seen VOC measurable when it's in my garage. ^c34573720

    It depends on your purpose.

  - **DavideNL** · [2023-01-30 08:20 UTC](https://news.ycombinator.com/item?id=34577170)
    There's also privacy, many monitors also record sound levels (like the Netatmo for example which is used a lot.) Many monitors send all collected data to their cloud. ^c34577170

  - **poxrud** · [2023-01-30 01:51 UTC](https://news.ycombinator.com/item?id=34574935)
    Amazon has their own air sensor for Alexa that can do PM2.5 ^c34574935

- **aedocw** · [2023-01-29 21:14 UTC](https://news.ycombinator.com/item?id=34572827)
  For folks who want to do something similar (no CO2 measure, and possibly less accurate) for far less per sensor, you can easily connect an ESP8266 (\$5) to an IKEA VINDRIKTNING (\$16) air quality sensor\[1\]. Stick a AM2302 (\$7) on the outside and you get PM2.5, temperature and humidity for about \$30. ^c34572827

  \[1\]: [https://style.oversubstance.net/2021/08/diy-use-an-ikea-vind...](<https://style.oversubstance.net/2021/08/diy-use-an-ikea-vindriktning-air-quality-sensor-in-home-assistant-with-esphome/>)

  - **M3L0NM4N** · [2023-01-29 21:24 UTC](https://news.ycombinator.com/item?id=34572906)
    I will note though, CO2 measure indoors can be very valuable. Higher levels of CO2 result in less brain function, as shown by this Tom Scott video: [https://youtu.be/1Nh\_vxpycEA](<https://youtu.be/1Nh_vxpycEA>) ^c34572906

    - **reeckoh** · [2023-01-29 22:04 UTC](https://news.ycombinator.com/item?id=34573263)
      They can also be a canary for other issues, like mold accumulation. ^c34573263

  - **PaulBGD\_** · [2023-01-29 21:30 UTC](https://news.ycombinator.com/item?id=34572972)
    I have both a modded VINDRIKTNING and the airgradient, imo the airgradient is worth it if you want everything in one package. More accurate than the ikea, a nice screen/case, and you don’t have to strap a humidity sensor to the outside. Plus CO2 is great, more people need CO2 detectors. ^c34572972

  - **jve** · [2023-01-30 07:45 UTC](https://news.ycombinator.com/item?id=34576955)
    Did just that by following that particular tutorial. Didn't expect accuracy, just following how air quality changes when baking, turning on humidifier, etc. ^c34576955

    However now my VINDRIKTNING shows red with MAX reading all the time - I suppose not to be placed in the kitchen - some sticky oil grease landed on the sensor.

  - **unknown** · [2023-01-30 06:47 UTC](https://news.ycombinator.com/item?id=34576586)
    [deleted] ^c34576586

- **kayson** · [2023-01-29 20:18 UTC](https://news.ycombinator.com/item?id=34572261)
  Wish I had seen this before I bought all the constituent parts on sparkfun! Though I do have some concerns about the accuracy of the PM2.5 sensor (mainly because the data sheet isn't exceptionally clear).I ended up getting the Sensirion equivalent over this one even though its quite pricey. ^c34572261

  Every all-in-one air quality monitor I've seen except one omit some fairly important metrics - NO2 and hydrogen sulfides. I'm guessing it's because the sensors are extremely expensive (I got quotes for \$90+/ea from one vendor). I ended up finding a startup, SPEC Sensors, that has much cheaper screen-printed sensors, and if their data sheets are to be believed, they're more than sufficient.

  - **ahaucnx** · [2023-01-29 20:24 UTC](https://news.ycombinator.com/item?id=34572326)
    We have made very good experience with the Plantower PMS5003 PM sensor and thousands of them went through our test chamber. The plantower has also shown one of the best accuracies for low-cost sensors compared to reference stations in various studies. ^c34572326

    I agree that the data sheets from Plantower are not great. Unfortuntately this is often the case from Chinese manufacturers.

    - **comboy** · [2023-01-29 20:56 UTC](https://news.ycombinator.com/item?id=34572658)
      I second Plantower (I've only used a few PMS7003), it allows you to build a really high quality sensor while being really a beginner project using some arduino and LCD.  Note that this is only for particulates in the air. ^c34572658

      Btw, why thousands? And any reasons for not using CCS811 for TVOC and HDC1080 for temp while you're at it? Sounds like you have tons of experience and it's not easy to find reviews which properly test these.

      - **ahaucnx** · [2023-01-29 21:32 UTC](https://news.ycombinator.com/item?id=34572990)
        No specific reasons other than that we are pretty happy with the quality from Sensirion and thus like to use their sensors. ^c34572990

    - **kayson** · [2023-01-29 21:47 UTC](https://news.ycombinator.com/item?id=34573099)
      That's good to know! Have you published your testing results anywhere? ^c34573099

    - **Fnoord** · [2023-01-30 06:02 UTC](https://news.ycombinator.com/item?id=34576315)
      Pimoroni's Enviro and Enviro+ use it. I build two. Fun stuff. ^c34576315

  - **dheera** · [2023-01-29 21:07 UTC](https://news.ycombinator.com/item?id=34572764)
    I made something similar ^c34572764

    [https://dheera.net/projects/airmonitor/](<https://dheera.net/projects/airmonitor/>)

    I used a PMSA003I and had major problems with it -- it was always reporting 0 for AQI if the actual value was anywhere below \~100. It wasn't sensitive to low levels of pollution. Is the PMS5003 any better?

    - **5e92cb50239222b** · [2023-01-30 06:43 UTC](https://news.ycombinator.com/item?id=34576560)
      I've been using three PMS5003 for years. It is sensitive to minute deviations in PM concentrations. Since I live in a very polluted area, I try to stay within one room as much as possible with a purifier running on full blast. Opening an inside door for a second lets a small amount of pollution in, which the sensor notices right away (it may be only half a microgram per m³, but it always goes up reliably). ^c34576560

      I manage to keep indoor PM2.5 levels within 1\% of what's happening outside, which the sensor also tracks as expected (so if outside it's 100 µg/m³, the indoor sensor shows 0-1 µg/m³, when the outside level rises to 250, my sensor starts showing 2-2.5 µg, and so on).

    - **ahaucnx** · [2023-01-29 21:20 UTC](https://news.ycombinator.com/item?id=34572881)
      We also used the A003 in the past and were not happy with accuracy and quality. We had quite a number of them failing early. The 5003 is a lot better in my opinion. ^c34572881

      - **dheera** · [2023-01-29 21:27 UTC](https://news.ycombinator.com/item?id=34572938)
        thanks! ^c34572938

  - **fierro** · [2023-01-29 21:40 UTC](https://news.ycombinator.com/item?id=34573058)
    would love a blog post / tutorial for this set up including the expensive sensors.  I think a lot of us who care about air quality don't mind spending a few hundred dollar for cool new data ^c34573058

    - **kayson** · [2023-01-30 22:54 UTC](https://news.ycombinator.com/item?id=34587796)
      I can do that. Might take a while though ^c34587796

- **mastax** · [2023-01-29 23:04 UTC](https://news.ycombinator.com/item?id=34573726)
  I bought one of the DIY Pro kits and put it together. I liked it overall. I think the kit is a good value, it's convenient to get everything all together, and the injection molded case is nice. The included software and cloud dashboard are convenient and functional. There are some less good parts, though: ^c34573726

  \- The instructions aren't great, but I can't remember what I had trouble with specifically.

  \- The included screws for the case are tiny, soft, and aren't self tapping. I never got them in all the way and gave up on them after the first disassembly. The USB power cable sort-of holds the clamshell together without them.

  \- I had issues with the reliability of the connection to the I2C sensors, especially after adding the SGP30. Reducing the speed to 100kHz helped somewhat but made the display update slowly. I never got the SHT3x temperature sensor to work reliably in the bottom corner position, so I moved it to the open top spot. I did try out various levels of I2C pull-up and removed redundant pull-ups from the modules that came with them installed. I think part of the problem is the loose fit of the included pin headers, soldering the sensors directly may help.

  \- The temperature sensor always reads high by about 5-10 degrees F, even when installed in the recommended far corner position. I tried mounting the airgradient vertically to try to induce a draft to clear out the generated heat but that didn't help. I could try to calibrate it but I doubt it's a simple offset.

  \- The dashboard is basic, had some annoying bugs, and they want you to pay for it. I can't remember specifically what I disliked because I replaced the firmware with EspHome long ago and set up a grafana dashboard to monitor it.

  - **ahaucnx** · [2023-01-29 23:17 UTC](https://news.ycombinator.com/item?id=34573834)
    Thank you for your feedback. ^c34573834

    With the new version (3.7) that is also now sold as the updated kit we have addressed most of these issues.

    \- we now supply stainless steel torx screws including screw driver

    \- we have now the SGP41 AirGradient module in our shop that has no pull up resistors and works very stable

    \- we redesigned the i2c circuit which now runs completely on 3.3v

    \- so far we never charged a DIYer for our dashboard but might do so at a reasonable price in future if our server costs rise.

    We continue fixing issues (software and hardware) that come up in our forum and are dedicated to ensure we deliver a high quality kit.

    - **runjake** · [2023-01-30 00:41 UTC](https://news.ycombinator.com/item?id=34574435)
      I just got my DIY Pro Kit a couple days ago and put it together and got it online today. ^c34574435

      Some issues:

      \- It’s easy overall but the instructions are pretty not good.

      \- The OLED displays text upside down. As far as I can tell, it is mounted the only correct way it can be mounted in the case.

      \- The unit is connected to Wi-Fi and is pingable, but it’s only communicated to the dashboard once. It’s displaying data on the OLED. I don’t have any firewall rules for it. Definitely more troubleshooting required on my end.

      I’m using a 1A power supply for it. Does it need more?

      - **runjake** · [2023-01-30 02:30 UTC](https://news.ycombinator.com/item?id=34575179)
        A few updates for someone who happens upon this thread: ^c34575179

        \- Be sure to flash via the ESP board's USB-C. Do not use the board USB-C as this is for power only. The docs are actually pretty clear here, but it's worth mentioning.

        \- It doesn't matter if you have a Pro DIY or Pro DIY Pre-Soldered, flash the image corresponding to the actual position of the OLED.

        Lower right OLED: [https://www.airgradient.com/open-airgradient/instructions/di...](<https://www.airgradient.com/open-airgradient/instructions/diy-pro/#software>)

        Upper left OLED: [https://www.airgradient.com/open-airgradient/instructions/di...](<https://www.airgradient.com/open-airgradient/instructions/diy-pro-presoldered/#software>)

        \- Your serial number is just the hexadecimal after the "AG-" or "AirGradient-" designation of your unit (eg. "206d86"). Mine was "AG-" which doesn't match what the docs say. Use this 6 or however many hexadecimal serial number to add the unit to the Dashboard. It seems to fail after the first update if you include the "AG-".

      - **ahaucnx** · [2023-01-30 01:14 UTC](https://news.ycombinator.com/item?id=34574716)
        Please give feedback on the instructions so that we can improve them. You can also message us through the support form. ^c34574716

        If the text is upside down, you flashed from the wrong build instructions. For the PRO Kit (OLED bottom right) use \[1\] for PRO Presoldered (OLED top left) use \[2\]

        The reason we had the display on two different location can be found here \[3\]. From now onwards we will only have display windows on the bottom right.

        Please use at least 2.4A power supply. The WiFi issues could be due to that.

        \[1\] [https://www.airgradient.com/open-airgradient/instructions/di...](<https://www.airgradient.com/open-airgradient/instructions/diy-pro/#software>)

        \[2\] [https://www.airgradient.com/open-airgradient/instructions/di...](<https://www.airgradient.com/open-airgradient/instructions/diy-pro-presoldered/#software>)

        \[3\] [https://www.airgradient.com/open-airgradient/blog/diy-pro-ki...](<https://www.airgradient.com/open-airgradient/blog/diy-pro-kit-journey/>)

        - **runjake** · [2023-01-30 01:55 UTC](https://news.ycombinator.com/item?id=34574956)
          Am I confused? I have the pre-soldered kit, but the OLED display is on the bottom-right, not the upper-left. ^c34574956

          [https://imgur.com/a/CkPv7FD](<https://imgur.com/a/CkPv7FD>)

          I will try to track down a 2.4A power supply, thanks.

          - **ahaucnx** · [2023-01-30 02:25 UTC](https://news.ycombinator.com/item?id=34575143)
            You might have already gotten the new kit. Can you please contact us at [https://www.airgradient.com/support/](<https://www.airgradient.com/support/>) and let us know your order number.
            It should be easy to fix. ^c34575143

            - **runjake** · [2023-01-30 21:38 UTC](https://news.ycombinator.com/item?id=34586792)
              I was able to flash the non-presoldered image on my new Pre-soldered unit and it works great now and displays properly. ^c34586792

              I did not have a 2.4A USB power supply handy, so I'm still using an old 1A iPhone USB charger and it works fine with the AG across the house from my WAP.

        - **fragmede** · [2023-01-30 18:10 UTC](https://news.ycombinator.com/item?id=34583915)
          \> Please use at least 2.4A power supply. ^c34583915

          Oof. IMO unless the board only needs 500mA at 5V, you'll save yourself a ton of money in customer service calls by providing your own power supply and "requiring" customers to use yours.

    - **dustinsterk** · [2023-01-30 23:22 UTC](https://news.ycombinator.com/item?id=34588155)
      Great to see, do you offer any discount codes/promo coupons for folks wanted to build multiple devices for their home/office? ^c34588155

- **ahaucnx** · [2023-01-29 19:54 UTC](https://news.ycombinator.com/item?id=34572000)
  This is an updated version of our DIY air quality monitor that now includes a configuration button and some other PCB improvements around the I2C bus. ^c34572000

  It has also pin breakouts so you can easily add additional sensors if required. Hardware and software are both open source and can easily be adjusted.

  - **Youden** · [2023-01-29 20:39 UTC](https://news.ycombinator.com/item?id=34572485)
    Was the decision to use pin headers instead of SMD components a conscious choice? ^c34572485

    For the particulate sensors it's unavoidable but you can use Sensirion's SCD4X series for CO2, just about any VOC chip you want, and an ESP32 module instead of dev board.

    It should be substantially cheaper overall since the components can be ordered in bulk and the only assembly needed would be the particulate sensor.

    I've been meaning to get around to it myself but I still haven't settled on how to power it. I'm really tempted to try stuffing it full of giant batteries so that it can run for at least around a year without a cable.

    - **ahaucnx** · [2023-01-29 20:42 UTC](https://news.ycombinator.com/item?id=34572516)
      Most people find it easier to solder through holes than SMD. We use SMD in our commercial product. ^c34572516

      We are testing the SCD4x and like it so far. It might be a future option.

      - **Youden** · [2023-01-29 22:28 UTC](https://news.ycombinator.com/item?id=34573439)
        I guess what I'm asking is does it need to be hand-solderable? With places like JLCPCB offering cheap SMD assembly, SMD boards are still accessible to hobbyists. ^c34573439

        - **mardifoufs** · [2023-01-29 22:55 UTC](https://news.ycombinator.com/item?id=34573657)
          I though JLPCB only assembled components that are available in their catalogue. If they don't have the part you need, you'll have to hand assemble it. These are pretty niche components, with odd footprints and size so I'd be surprised if assembly was available. ^c34573657

          - **Youden** · [2023-01-30 08:02 UTC](https://news.ycombinator.com/item?id=34577058)
            You can have them order parts that are available at Mouser, Digikey and the other parts vendors. They have the SCD41 \[0\], SGP41 \[1\] and a variety of ESP32 modules (e.g. \[2\]) in their catalogue. The preorder prices can be a bit out of whack but they'll correct them when they actually buy the part. ^c34577058

            \[0\]: [https://jlcpcb.com/partdetail/Sensirion-SCD41\_DR2/C3659294](<https://jlcpcb.com/partdetail/Sensirion-SCD41_DR2/C3659294>)

            \[1\]: [https://jlcpcb.com/partdetail/Sensirion-SGP41\_DR4/C3659325](<https://jlcpcb.com/partdetail/Sensirion-SGP41_DR4/C3659325>)

            \[2\]: [https://jlcpcb.com/partdetail/EspressifSystems-ESP32\_S2\_MINI...](<https://jlcpcb.com/partdetail/EspressifSystems-ESP32_S2_MINI_1N4/C2847294>)

    - **comboy** · [2023-01-29 21:07 UTC](https://news.ycombinator.com/item?id=34572761)
      If you want continuous measurement, battery is pretty much not an option, PM2.5 will use a small fan, so even at 30mA it's 30 \* 24 \* 365 so for a year you need 262,800mAh battery, it's a different voltage but to put it in context your laptop is likely under 10,000mAh. If you only need to take measurements say every 30mins then sure, but then either you worry about sending it somewhere and receiving it or you need to use additional battery power for displaying it. ^c34572761

  - **aikinai** · [2023-01-29 22:49 UTC](https://news.ycombinator.com/item?id=34573597)
    Is there any way to checkout without PayPal? I was mysteriously banned a few years ago with no details and no recourse. And I don’t see an option to just pass through a credit card without logging in. ^c34573597

    Edit: Never mind! I found out tapping the credit card logo worked to do a pass through payment without logging into PayPal. Purchased!

    And thanks for supporting international shipping too!

    - **ahaucnx** · [2023-01-29 23:27 UTC](https://news.ycombinator.com/item?id=34573910)
      I think you should be able to just pay with credit card. If you have problems please contact us through the support form. ^c34573910

  - **smcleod** · [2023-01-29 20:00 UTC](https://news.ycombinator.com/item?id=34572051)
    Nice! Great work making it open source! ^c34572051

- **RobotToaster** · [2023-01-29 20:48 UTC](https://news.ycombinator.com/item?id=34572581)
  It isn't open source as it's under a NC licence, which restricts the field of endeavour. ^c34572581

  [https://www.oshwa.org/faq/\#non-commercial](<https://www.oshwa.org/faq/#non-commercial>)

  [https://opensource.org/osd](<https://opensource.org/osd>)

  - **simondotau** · [2023-01-30 08:40 UTC](https://news.ycombinator.com/item?id=34577297)
    No matter how much they wish it were otherwise, OSI doesn't get to dictate what "open source" means. It's not their trademark. The term existed before they did. And equally as importantly, the words *open* and *source* existed before they did. ^c34577297

    The source for AirGradient is not closed. It is open.

    - **RobotToaster** · [2023-01-30 21:26 UTC](https://news.ycombinator.com/item?id=34586620)
      Looking again there aren't even any source files available for the PCB at all, only gerber files, which are purely manufacturing files. ^c34586620

- **crazygringo** · [2023-01-29 21:07 UTC](https://news.ycombinator.com/item?id=34572767)
  This is tangential, but is anyone aware of a live outdoor CO2 levels map? I've never been able to find one anywhere. ^c34572767

  Because outdoor levels seem to vary significantly in a kind of 400-600 range, and it's impossible to calibrate a sensor outside without a reference point. On a windy winter day you can probably assume it's close to the global \~414, but on a muggy still summer day my sensors usually read significantly higher when holding them outdoors.

  - **keenanj** · [2023-01-29 21:56 UTC](https://news.ycombinator.com/item?id=34573186)
    This is a plug for my non-profit building an open-source version of exactly that: ribbitnetwork.org. ^c34573186

    Our society deserves to have a publicly available map of outdoor emissions. There are lots of hard science and data analysis questions to solve in order to get there with reliable and cheap sensors, but I think it’s a journey worth going on.

    We’re on discord and GitHub if anyone wants to come build with us.

    - **crazygringo** · [2023-01-29 22:59 UTC](https://news.ycombinator.com/item?id=34573686)
      Thank you! That's exactly the kind of thing I was looking for. ^c34573686

      I've been utterly baffled by how atmospheric CO2 is one of the very top issues of our time, and yet... I can get live temperature, humidity, and things like PM2.5, PM10, NO2, O3, etc... but *not CO2*.

      Since you're in this area, do you have any insight as to why?

      There are thousands of official air quality monitors used all over the world for calculating AQI and similar. Why did they skip CO2? Is there something inherently difficult or inaccurate about measuring it, is its short-term variation simply seen as irrelevant to health and not worth studying, or is there a political fear that live monitoring might somehow become ammunition for climate change deniers, along the lines of every winter blizzard leading to some people taunting "where's your global warming now?"

      The US government measures CO2 at the Mauna Loa Observatory in Hawaii... and seemingly nowhere else?

      - **alwayslikethis** · [2023-01-30 08:03 UTC](https://news.ycombinator.com/item?id=34577063)
        I don't think local outdoor CO2 levels vary by much. Sure, if you are near a significant source (a highway or a factory burning things), then you'll have some locally elevated levels. Even then, however, the locally elevated levels are unlikely to have a significant effect on health, since it is very easily diffused. ^c34577063

        Another side of this issue is that CO2 is relatively difficult to measure reliably, because it is a very unreactive molecule. It is not susceptible to oxidation or most other reactions that can be used to determine its presence. Most reliable sensors use an IR light source and measure its attenuation by CO2.

      - **keenanj** · [2023-01-30 00:40 UTC](https://news.ycombinator.com/item?id=34574417)
        Thanks! Yeah you can build a CO2 outdoor sensor with our instructions on GitHub and hopefully soon you will be able to just purchase a kit if you’d like. ^c34574417

        As for your question about why does this not exist, there isn’t exactly one reason, but all of the reasons you stated above are certainly a part of the story.

        The US government has not deployed a network like this primarily due to cost. Monitoring stations that the EPA install typically have a cost of at minimum \$100k to install and finding people to maintain it is even harder.

        Citizen science networks are generally started and deployed by for-profit companies. Because it’s hard to draw a direct line between a high CO2 measurement and some sort of immediate effect, most for-profit companies can’t justify the cost to build and sell something like this. For instance, purple—air is a for profit based on pollution particles. Consumers latch onto this because it has direct health effects and benefits you as the purchaser to know if you should open the windows or not today. Same with weather monitoring stations. There is a direct benefit for you in planning your day to know what the hyper local temperature outside is.

        It’s a real shame and a place where capitalism fails society in my opinion. Having more data on the issue is important to inform gov. policy, hold emission sources accountable etc.

        - **keenanj** · [2023-01-30 00:46 UTC](https://news.ycombinator.com/item?id=34574467)
          I also don’t want to trivialize the difficulty in the data analysis for the very low cost co2 sensors. The accuracy and precision of non-calibrated cheap ( \<\$100 ) is very poor. It’s still a bit of an unsolved problem to figure out how to best use this data. The theory is that a dense network of low cost and a few high grade sensors can be used to produce meaningful datasets. However it’s still risky and lots of research and testing is needed to validate this. The amount of money required is a bit outside the scope of what most academic  labs can support on their own. And it’s way too risky to raise investments as a for-profit. ^c34574467

          However I do think it’s worth doing, hence why the org. is a non-profit.

          - **crazygringo** · [2023-01-30 02:19 UTC](https://news.ycombinator.com/item?id=34575109)
            Thank you for all the insight! And thank you for starting the non-profit as well. ^c34575109

  - **namibj** · [2023-01-29 21:59 UTC](https://news.ycombinator.com/item?id=34573219)
    You can use a chemical CO2 scrubber (e.g., bubbling air through a saturated solution of calcium hydroxide) to get a rather stable/repeatable sub-ambient reference to calibrate the sensor with. ^c34573219

    An aquarium bubbler , or rather two, should be easy to plumb to a CO2 sensor. Just skip the water bath for one of them.

    The calcium hydroxide is sold as "hydrated lime" and needs to just be stored isolated from CO2, and is mildly basic, so will slowly corrode your fingers (wash after touching, don't get any in your eyes).

    Shouldn't even need gloves for this usecase, where one occasionally swaps the water and sediment for fresh stuff.

    Btw, the waste, after soaking CO2, is just harmless limestone. Sprinkle around somewhat to make it a thin layer to ensure it all converts soon.

  - **breput** · [2023-01-29 22:38 UTC](https://news.ycombinator.com/item?id=34573519)
    Many CO₂ sensors have a 0 ppm calibration setting option, so you can place them in a small container and fill it with a CO₂-free gas such as nitrogen or even butane. Obviously nitrogen is safer although somewhat more expensive and more difficult to buy in small canisters. ^c34573519

    But realistically for home air quality measurements, it doesn't really matter. If you happened to calibrate it at 600 ppm you'd know when you later saw values below 400 ppm. Or you'd read a little high which probably isn't something you'd even notice.

  - **ck2** · [2023-01-30 04:15 UTC](https://news.ycombinator.com/item?id=34575715)
    limited cities but try [https://aqicn.org/map/northamerica/](<https://aqicn.org/map/northamerica/>) ^c34575715

    - **crazygringo** · [2023-01-30 17:03 UTC](https://news.ycombinator.com/item?id=34582734)
      That's a perfect example of what I'm talking about. Like every other AQI map, it *doesn't* include CO2. ^c34582734

- **hrez** · [2023-01-30 03:25 UTC](https://news.ycombinator.com/item?id=34575454)
  If you're like me and only looking for CO2 monitor, here is a short story. ^c34575454

  I was researching all the sensors and kits and was narrowing down on AirGradient actually. Per my research the best last gen CO2 sensors are from swiss Sensirion   SCD4x series. So I started looking how to build something on it etc.

  While poking around, by pure chance I saw that Sensirion makes SCD4x-CO2-Gadget which is SCD41 sensor with LED indicator and BLE and powered by USB the size of flash drive.

  [https://sensirion.com/products/catalog/SCD4x-CO2-Gadget/](<https://sensirion.com/products/catalog/SCD4x-CO2-Gadget/>)

  So, you can just stick it in USB charger anywhere and either use visuals or a mobile app that will show the number or import data for a chart.
  All for \$60 from official Sensirion dealer like digikey.

  I don't mean to sound like an Ad, but it's the best sensor as far as I know, for least cost and nothing to solder (perhaps a negative for some :)
  No affiliation.

  - **rogers18445** · [2023-01-30 05:40 UTC](https://news.ycombinator.com/item?id=34576190)
    This is indeed the absolute best value co2 consumer 24/7 monitor you can buy right now. ^c34576190

    You don't have control over calibration however, it's set to auto. So you need to expose it to outside air every 7 days or it will drift. The good news that a drift should be automatically fixed in just a few minutes after you take it outside.

    If you live in a high co2 area, the ppm values will not be accurate. But relative measurements will be. And you can just add the difference if you know it to any number you see.

- **sc00ty** · [2023-01-29 22:55 UTC](https://news.ycombinator.com/item?id=34573652)
  I ordered two DIY pro kits (with the TVOC sensors) earlier this month and went to start working on them yesterday. After flashing the firmware, neither one would create a hotspot for me to connect to. Looking at them and doing some googling, i found they include knock-off Wemos D1 minis (labeled "mimi"). It looks like they're aware there are Wi-Fi issues, but the chips are still being used \[0\]\[1\]. I sent in an email yesterday but I'm not expecting a response until at least tomorrow. ^c34573652

  \[0\]: [https://www.airgradient.com/open-airgradient/blog/d1-mimi/](<https://www.airgradient.com/open-airgradient/blog/d1-mimi/>)

  \[1\]: [https://forum.airgradient.com/t/issues-with-new-dyi-pro-pres...](<https://forum.airgradient.com/t/issues-with-new-dyi-pro-presoldered-kit/414/22>)

  - **ahaucnx** · [2023-01-29 23:03 UTC](https://news.ycombinator.com/item?id=34573716)
    Customer support will be in office tomorrow and we are sending a free replacement to all customers that have been impacted by a non working D1. ^c34573716

    The "Mimi" version should not have the problem and we found it to be very stable and it is currently our default version.

    More information here: [https://www.airgradient.com/open-airgradient/blog/d1-mimi/](<https://www.airgradient.com/open-airgradient/blog/d1-mimi/>)

- **miniwark** · [2023-01-30 07:57 UTC](https://news.ycombinator.com/item?id=34577026)
  There is another Open Source alternative by FabLab Barcelona. The SmartCitizen Kit: ^c34577026

  [https://smartcitizen.me/](<https://smartcitizen.me/>)

  [https://www.seeedstudio.com/Smart-Citizen-Starter-Kit-p-2865...](<https://www.seeedstudio.com/Smart-Citizen-Starter-Kit-p-2865.html>)

  It is mainly for outdoor pollution (including light & noise), but it also include indoor gaz sensors for Co2 and VOC.

- **dragontamer** · [2023-01-29 21:55 UTC](https://news.ycombinator.com/item?id=34573176)
  Each time I see these, I feel a bit weird because they all rely upon a specific sensor, and the software / electronics is barely above beginner level. ^c34573176

  A PM2.5 sensor is based off of infrared LEDs and photodiodes.

  CO2 however is harder for me to understand. Does anyone know how that works?

  Temperature is easy: just a calibrated thermistor.

  Humidity: I dunno and am also curious.

  \--------

  It's be a lot more comfortable for me to call this open source if the sensors actually gave design control to the engineer, more so than just assembly.

  - **breput** · [2023-01-29 22:21 UTC](https://news.ycombinator.com/item?id=34573388)
    The Senseair S8 CO₂ sensor\[0\] used in this project also uses an infrared LED and works on the principal that CO₂ absorbs certain frequencies of light. ^c34573388

    So if you know the brightness of the LED and the volume of air between it and the sensor, you can calculate the amount of CO₂ by comparing the expected vs. received light intensity.

    \[0\] [https://rmtplusstoragesenseair.blob.core.windows.net/docs/pu...](<https://rmtplusstoragesenseair.blob.core.windows.net/docs/publicerat/PSP126.pdf>)

    - **dragontamer** · [2023-01-29 22:28 UTC](https://news.ycombinator.com/item?id=34573440)
      Good to know. ^c34573440

      So methinks that a CO2 sensor would have to be based off of multiple LEDs + Photodiodes, to measure the absorbed light at \_different\_ frequencies. (LEDs and Photodiodes typically are only active at one frequency: such as 900nm or 700nm).

      If "all" frequencies are deflected, its PM2.5 (some particle got in the way of the measurement).

      If "some" frequencies are deflected, then its CO2.

      \----------

      The question after that comes down to calibration and test data. Is there an easy way to create CO2 density and/or PM2.5 particles of a certain density?

      \---------

      There's a big difference.

      1\. Photodiodes and LEDs are extremely common parts manufactured by a wide variety of companies around the world. By tying yourself to Photodiodes/LEDs, you are less tied to any particular company.

      2\. Photodiodes and LEDs are well under 10-cents each. Though some more carefully calibrated ones / specialty ones may reach as high as \$1 to \$2.

      - **breput** · [2023-01-29 22:55 UTC](https://news.ycombinator.com/item?id=34573648)
        \> (LEDs and Photodiodes typically are only active at one frequency: such as 900nm or 700nm). ^c34573648

        That's not entirely correct. The spec sheet for the LED will give an intensity vs. wavelength chart, which depending on the LED can be 10s to 100s of nanometers wide. As long as the source LED has a sufficiently bright output in one of the CO₂ absorption bands, it doesn't have to be exactly tuned like a laser.

        NDIR is the technology used in most consumer-grade CO₂ sensors: [https://en.wikipedia.org/wiki/Nondispersive\_infrared\_sensor](<https://en.wikipedia.org/wiki/Nondispersive_infrared_sensor>)

      - **breput** · [2023-01-30 00:09 UTC](https://news.ycombinator.com/item?id=34574208)
        \> The question after that comes down to calibration and test data. Is there an easy way to create CO2 density and/or PM2.5 particles of a certain density? ^c34574208

        Most CO₂ sensors have the ability to calibrate to either 400 ppm or 0 ppm. So if you really care enough, you can fill a small box with nitrogen and calibrate to 0 ppm.

  - **aidenn0** · [2023-01-30 02:28 UTC](https://news.ycombinator.com/item?id=34575159)
    FYI, getting temperature right is actually quite hard.  It's sitting on a piece of copper next to a bunch of stuff that makes heat. ^c34575159

    If you don't know what you're doing, then you'll get it wrong (except maybe if you use a fan).

- **edge17** · [2023-01-29 20:05 UTC](https://news.ycombinator.com/item?id=34572118)
  Just out of curiousity, what are the equivalent commercial products in this space? ^c34572118

  - **ahaucnx** · [2023-01-29 20:12 UTC](https://news.ycombinator.com/item?id=34572190)
    We also offer a fully certified commercial product (AirGradient ONE) focusing on B2B (Offices, Schools). Then you have monitors from other companies e.g. Awair, AirThings, Kaiterra, Air Visual etc measuring similar air quality parameters. ^c34572190

    We try to set us apart by promoting open data standards, clear data ownership, long lasting products that are easy to repair and maintain. More details on our main website \[1\].

    \[1\] [https://www.airgradient.com/](<https://www.airgradient.com/>)

  - **marcel\_hecko** · [2023-01-29 20:27 UTC](https://news.ycombinator.com/item?id=34572351)
    Well we do a version with multiple uplink technology option and a full SDK\[1\]. The market is actually quite segmented depending on the final use case. This is IMO mostly because of the price of these devices. The CO2 probe itself is costly especially if metrologically calibrated so if you want one for every room in the school / office / home its not insignificant investment. ^c34572351

    I'll include a link to our datasheet \[1\] as to actually answer the question hoping Im not breaking HN rules.

    \[1\] [https://docs.moirelabs.com/scoria-datasheet/](<https://docs.moirelabs.com/scoria-datasheet/>)

  - **wallflower** · [2023-01-29 20:21 UTC](https://news.ycombinator.com/item?id=34572298)
    The IQAir is very nice. There is also the Purple Air monitor. ^c34572298

    [https://www.iqair.com/us/air-quality-monitors](<https://www.iqair.com/us/air-quality-monitors>)

    [https://www.purpleair.com](<https://www.purpleair.com>)

    - **erinnh** · [2023-01-29 20:39 UTC](https://news.ycombinator.com/item?id=34572487)
      Totally not a judgement about the quality of it, but it amazes me how the IQAir is only supported via Cloud. Even for this really local information I need to contact some Cloud to be able to get the information into my smart home. ^c34572487

      This stuff annoys me a lot.

      - **ahaucnx** · [2023-01-29 20:46 UTC](https://news.ycombinator.com/item?id=34572547)
        Yes unfortuntately we see a clear trend among other companies towards walled gardens, closed data and forcing people into subscriptions. We at AirGradient do not support this development and made very clear statements on our website. ^c34572547

      - **dgacmu** · [2023-01-29 20:55 UTC](https://news.ycombinator.com/item?id=34572651)
        You can connect to it via SMB and grab the raw logfiles. It stores them as csv. ^c34572651

        [https://www.iqair.com/us/newsroom/download-the-airvisual-nod...](<https://www.iqair.com/us/newsroom/download-the-airvisual-node-pro-s-data-using-samba>)

        Not a friendly API for integrating but you can build from there
        (I have an air visual pro and I do this)

        - **erinnh** · [2023-01-29 21:01 UTC](https://news.ycombinator.com/item?id=34572710)
          Thank you. The only info I found was their cloud connection. ^c34572710

          I was interested because I wouldn't have to deal with customs in their case, but considering the price and interesting integration, dealing with customs might be better :P

          - **dgacmu** · [2023-01-30 01:15 UTC](https://news.ycombinator.com/item?id=34574721)
            Welcome. Actually, on checking, they've also added a .json file with the latest measurements. ^c34574721

            smbclient -U airvisual\%PASSWORD \\\\\\\\192.168.X.Y\\\\airvisual -c "get latest\_config\_measurements.json"

            if you want an interactive display. Otherwise there are a bunch of csv files with the archived values, under a time-varying filename like:

            202301\_AirVisual\_values.txt

            With format:

            Date;Time;Timestamp;PM2\_5(ug/m3);AQI(US);AQI(CN);PM10(ug/m3);PM1(ug/m3);Outdoor AQI(US);Outdoor AQI(CN);Temperature(C);Temperature(F);Humidity(\%RH);CO2(ppm)
            2023/01/01;00:00:03;1672531203;0.0;0;0;0.0;0.0;8;3;22.7;72.8;41;406;

            - **wallflower** · [2023-02-01 14:37 UTC](https://news.ycombinator.com/item?id=34611018)
              Thanks for digging into the mucks of the quote end quote API. SMB makes me think they were aiming for the commercial market and just repurposed it for home. ^c34611018

      - **newZWhoDis** · [2023-01-29 21:25 UTC](https://news.ycombinator.com/item?id=34572921)
        I was gifted an air things and had this exact problem. Local WiFi device is useless, stores everything in their cloud and takes forever to load randomly. ^c34572921

      - **wodenokoto** · [2023-01-29 20:44 UTC](https://news.ycombinator.com/item?id=34572530)
        I believe this is to support their pollution maps and pollution forecasts. Which makes the high price of the product odd to me. ^c34572530

  - **zokier** · [2023-01-29 21:28 UTC](https://news.ycombinator.com/item?id=34572952)
    Vaisala has some air quality monitors, although they seem more oriented towards outdoors use? [https://www.vaisala.com/en/products/weather-environmental-se...](<https://www.vaisala.com/en/products/weather-environmental-sensors/air-quality-transmitter-aqt530-urban-industrial-systems>) ^c34572952

- **pigtailgirl** · [2023-01-29 20:29 UTC](https://news.ycombinator.com/item?id=34572363)
  \-- live in seoul - air quality is sometimes "unbreathable" - using AirIQ api for smart home alert - [https://www.iqair.com/us/air-pollution-data-api](<https://www.iqair.com/us/air-pollution-data-api>) \-- ^c34572363

- **unclekev** · [2023-01-30 02:58 UTC](https://news.ycombinator.com/item?id=34575339)
  Anyone here using/found a decent Air Quality sensors that is plug and play with Home Assistant? ^c34575339

  - **davidrhunt** · [2023-01-30 03:08 UTC](https://news.ycombinator.com/item?id=34575380)
    I struggled with the same search and ended up getting the AirGradient DIY Pro Kit Pre-Soldered. Not quite plug and play but the steps to get it up and running are fairly straightforward. Just plug parts in, drop some firmware on, and go. Curious what other suggestions are out there because I would still like something simpler! ^c34575380

    [https://www.airgradient.com/open-airgradient/shop/\#!/DIY-Pro...](<https://www.airgradient.com/open-airgradient/shop/#!/DIY-Pro-Kit-Pre-Soldered/p/476627519/category=0>)

  - **sunsetMurk** · [2023-01-30 03:06 UTC](https://news.ycombinator.com/item?id=34575372)
    I use a 'LEVOIT air purifier'\[1\], and it has a  PM2.5 sensor that works w/ Home Assistant out of the box through the VeSync integration \[2\]. ^c34575372

    1- [https://smile.amazon.com/gp/product/B08L73QL1V](<https://smile.amazon.com/gp/product/B08L73QL1V>)
    2- [https://www.home-assistant.io/integrations/vesync/](<https://www.home-assistant.io/integrations/vesync/>)

- **Tempest1981** · [2023-01-29 20:11 UTC](https://news.ycombinator.com/item?id=34572176)
  I have a handheld \$65 TVOC meter, but it's tricky to get repeatable measurements. It needs 5-10 minutes to warm up, but then the reading jump around almost 2x. It has 4 digits of resolution, but 1 digit of accuracy? ^c34572176

  Regardless, indoor TVOC levels increase significantly over 2-3 days. Then opening the windows brings them back down. Not sure if that's normal. (TVOC \= Total volatile organic compounds)

  Any recommendations for quality sensors?

  - **ahaucnx** · [2023-01-29 20:20 UTC](https://news.ycombinator.com/item?id=34572289)
    Compared to CO2 and PM measurements, TVOCs are the most difficult to measure because they encompass a wide range of chemicals that trigger the sensor. Some are very harmful, e.g. aggressive paint and others (hopefully) harmless like sunscreen. Both trigger the sensor. ^c34572289

    Additionally the sensors are only showing you correct absolute levels in lab conditions, e.g. using ethanol at a specific temperature and humidity. So in real environments, the absolute values are pretty useless.

    We now use a newer generation of TVOC senor e.g. the SGP41 that is more index based and eliminates the issue of the absolute values.

    We also observe that temperature and humidity can influence the TVOC measurements.

    All in all, TVOC is good to detect spikes and check what is causing these, e.g. use of aggressive cleaning chemicals. However the absolute levels in e.g. ppb should better be ignored.

    Yes, it is normal that fresh air flushes out chemicals and you can see this improvement. We do like the SGP4x series from Sensirion for TVOC sensors.

    - **drakenot** · [2023-01-29 20:46 UTC](https://news.ycombinator.com/item?id=34572545)
      Are they accurate enough for me to ensure I’m keeping VOC levels down while 3D printing different materials? ^c34572545

      - **ahaucnx** · [2023-01-29 21:16 UTC](https://news.ycombinator.com/item?id=34572841)
        Yes I think they should be suitable for that. ^c34572841

      - **ted\_dunning** · [2023-01-29 21:00 UTC](https://news.ycombinator.com/item?id=34572699)
        That could be an excellent use for sensors that only give reasonable relative measurements. ^c34572699

  - **parker\_mountain** · [2023-01-29 20:18 UTC](https://news.ycombinator.com/item?id=34572265)
    FWIW, TVOCs can collect together and move around in "waves", your indoor air is not just one big evenly distributed "soup". The sensors also have lots of factors that affect them, such as humidity - you can usually find more info in the docs for the sensor part. ^c34572265

    A better approach would be to sample consistently and use that to build a graph showing TVOC ppm over time.

- **pbronez** · [2023-01-29 21:56 UTC](https://news.ycombinator.com/item?id=34573188)
  Anyone know how hard it would be to convert this from USB-C power & wifi connectivity to PoE for power + data? ^c34573188

  TI has PoE chips for around \$4, but I don’t know enough about electrical engineering to figure out how to swap that into this design.

  [https://www.ti.com/product/TPS23861](<https://www.ti.com/product/TPS23861>)

  - **pbronez** · [2023-01-29 22:05 UTC](https://news.ycombinator.com/item?id=34573275)
    Looks like you can get a PoE to USB-C adapter for \$35: ^c34573275

    Revotech PoE to Type-C Adapter Converter, Convert POE to Output 5V/2.4A USB C with Ethernet, IEEE802.3af with 10/100Mbps , Wired Broadband and PD Charging for Smart Phone/Tablet, Plug and Play (P2C5V) [https://a.co/d/7320MNa](<https://a.co/d/7320MNa>)

    Wonder how complex it is to access the network this way.  If you have to modify the USB implementation you may as well skip the adapter and add an RJ45 + internal PoE chip…

- **pfyy** · [2023-01-29 21:33 UTC](https://news.ycombinator.com/item?id=34573003)
  We made a small co2 sensor based on the sensirion scd30 and m5 stack. If you want a portable sensor with battery and display, you might be interested. Source code is on [https://github.com/smoca-ag/m5stack\_co2\_sensor](<https://github.com/smoca-ag/m5stack_co2_sensor>) ^c34573003

- **patja** · [2023-01-29 20:53 UTC](https://news.ycombinator.com/item?id=34572629)
  A project I did to make CO2 monitors with a Sensiron SCD41 sensor and Adafruit MagTag e-ink module: ^c34572629

  [https://www.printables.com/model/121265-salud-co2-monitor](<https://www.printables.com/model/121265-salud-co2-monitor>)

- **jph** · [2023-01-29 20:18 UTC](https://news.ycombinator.com/item?id=34572266)
  This is super-useful. The TVOC / NOx module is especially compelling. Can I purchase it pre-soldered? ^c34572266

  I do see your commercial offering (AirGradient ONE) and I'd like to buy that for my office. How does a typical consumer purchase one online?

  - **upon\_drumhead** · [2023-01-29 20:29 UTC](https://news.ycombinator.com/item?id=34572371)
    They have pre-soldered kits in their store, which took me a hot minute to actually find. ^c34572371

    [https://www.airgradient.com/open-airgradient/shop/](<https://www.airgradient.com/open-airgradient/shop/>)

    - **ahaucnx** · [2023-01-29 20:48 UTC](https://news.ycombinator.com/item?id=34572572)
      The presoldered kit also comes already pre-flashed and you can literally build it in 5-10 minutes. Just need to plug in the sensors, one cable and screw it together. ^c34572572

- **maweki** · [2023-01-29 20:30 UTC](https://news.ycombinator.com/item?id=34572376)
  Is it common for the HN audience to be able to fabricate their own PCBs? I believe none of my local hacker spaces have fabrication facilities. ^c34572376

  Whenever I see that, it means having to pay somebody quite a bit instead of do it yourself.

  - **idiotsecant** · [2023-01-29 20:33 UTC](https://news.ycombinator.com/item?id=34572417)
    You *can* make your own PCBs quite easily with cheap chemicals, a laser printer, and some tubs to agitate the mixture. It's a bad idea though, when you can design them and get them made online *incredibly* cheaply. ^c34572417

  - **dgacmu** · [2023-01-29 20:39 UTC](https://news.ycombinator.com/item?id=34572484)
    There are some home-brewable ways for single layer boards, particularly one sided -- you can do the old school copper board + mask + etch with something like ferric chloride. It's pretty easy but you do want to be careful as the chemicals are a bit nasty. Newer school is to print the mask and transfer using a laminator. ^c34572484

    You can also physically etch with a milling machine. It's a bit more expensive but low startup cost if you already have a small cnc mill. You probably have access to one at a maker space. That's most likely the easiest way to go.

  - **ted\_dunning** · [2023-01-29 20:59 UTC](https://news.ycombinator.com/item?id=34572690)
    It is incredibly easy to use an on-line service to specify and fabricate PCBs. ^c34572690

    I just did it for an adapted multi-sensor temperature system and the boards were about \$5 and tooling costs were minimal. The quality far exceeded anything that I have ever been able to do by myself.

    Self-etching is a royal pain for a medieval quality result. It probably winds up costing more than ordering the boards from PCBWay or similar manufacturer.

    - **midoridensha** · [2023-01-30 04:48 UTC](https://news.ycombinator.com/item?id=34575862)
      It's basically impossible to made a modern PCB at home; you can certainly make something that's not even at the quality level of an early 1970s PCB: single-layer, single-sided, no solder mask, but that's about it.  For modern circuitry, you want at a minimum double-sided, plated thru-holes, immersion tinned, and a solder mask.  For more complex circuits or those needing better power/ground shielding to keep noise down, you need 4 layers, which is totally impossible at home. ^c34575862

  - **jazzyjackson** · [2023-01-29 20:41 UTC](https://news.ycombinator.com/item?id=34572503)
    I guess I wouldn't say common - but hackerspaces and especially fablabs will often have a Roland CNC machine capable of carving PCBs out of copper-coated-fiberglass - but once you go through all that (paying for a couple broken 1/64" routing bits as you learn to use the machine...) it starts to make sense to pay \$5 per square inch at oshpark ^c34572503

  - **Kuinox** · [2023-01-29 20:31 UTC](https://news.ycombinator.com/item?id=34572394)
    I built one.  
    But without PCB.  
    I just used wires and soldered it. ^c34572394

  - **aidenn0** · [2023-01-29 20:38 UTC](https://news.ycombinator.com/item?id=34572467)
    I haven't had any made in a while but last time I got 2 index-card sized PCBs with silk-screen and solder mask for under \$40 after shipping. ^c34572467

- **edge17** · [2023-01-29 23:05 UTC](https://news.ycombinator.com/item?id=34573738)
  If I live next to a construction site, would something like this provide some guidance in terms if whether I should be doing more to clean up the air in my home? ^c34573738

  - **harrydehal** · [2023-01-30 05:31 UTC](https://news.ycombinator.com/item?id=34576140)
    I run an indoor sensor from a different company and it definitely allows me to measure whenever the neighbors are doing yardwork, or there's a fire down the street, etc. ^c34576140

    My sensor is indoor, but I am curious about picking up an outdoor sensor to see if I can find any long-term correlation between a train passing and increase in emissions.

  - **ahaucnx** · [2023-01-29 23:22 UTC](https://news.ycombinator.com/item?id=34573875)
    The PM sensor will easily pick up the dust from the construction site and you will probably notice changes in wind direction as well. ^c34573875

- **sytelus** · [2023-01-30 02:57 UTC](https://news.ycombinator.com/item?id=34575335)
  On a side note, Amazon's one of the least known great product is smart air quality monitor for under \$100: [https://www.amazon.com/Introducing-Amazon-Smart-Quality-Moni...](<https://www.amazon.com/Introducing-Amazon-Smart-Quality-Monitor/dp/B08W8KS8D3/>) ^c34575335

  - **ycombinatornews** · [2023-01-30 04:30 UTC](https://news.ycombinator.com/item?id=34575779)
    Doesn’t measure CO2. Just CO ^c34575779

- **pax** · [2023-01-29 23:04 UTC](https://news.ycombinator.com/item?id=34573725)
  Can AirGradient be made to contribute to [https://sensor.community/](<https://sensor.community/>) or [https://openaq.org](<https://openaq.org>) data streams? Or anything similar? ^c34573725

  - **ahaucnx** · [2023-01-29 23:21 UTC](https://news.ycombinator.com/item?id=34573870)
    Yes very much. We are in touch with OpenAQ on this matter. ^c34573870

- **FullKirby** · [2023-01-30 04:41 UTC](https://news.ycombinator.com/item?id=34575832)
  I signed up to their newsletter and instantly got a mail saying "Dear John, we have shipped your DIY kit... " with a very shady link to "track my package". What just happened here ?? ^c34575832

  - **ahaucnx** · [2023-01-30 05:09 UTC](https://news.ycombinator.com/item?id=34575985)
    Thanks for pointing this out. It seems we linked it to the wrong form (we have one internal one when we actually ship the kits)! Will fix this immediately. ^c34575985

- **1270018080** · [2023-01-29 21:57 UTC](https://news.ycombinator.com/item?id=34573205)
  Does anyone know of air quality monitors that check for NO2 as well as CO2? ^c34573205

  - **slawwwc** · [2023-01-30 09:30 UTC](https://news.ycombinator.com/item?id=34577606)
    Air-Q does both. Looks interested, but I don't know much about the quality of their products.
    [https://en.air-q.com/produktvarianten](<https://en.air-q.com/produktvarianten>) ^c34577606

- **arriu** · [2023-01-29 21:09 UTC](https://news.ycombinator.com/item?id=34572785)
  How does this compare to something like the Aranet4 module? ^c34572785

  - **ahaucnx** · [2023-01-29 21:14 UTC](https://news.ycombinator.com/item?id=34572824)
    It should give very similar results. As far as I know the Aranet also uses a CO2 Sensor from Senseair. ^c34572824

    - **thadk** · [2023-01-30 07:39 UTC](https://news.ycombinator.com/item?id=34576918)
      It appears to be this \$60 Senseair Sunrise however: [https://sensormaestros.com/products/sensor/gas/co2/senseair-...](<https://sensormaestros.com/products/sensor/gas/co2/senseair-sunrise/>) ^c34576918

      [https://senseair.com/news/customer-cases/aranet4-senseair-su...](<https://senseair.com/news/customer-cases/aranet4-senseair-sunrise-inside/>)

- **Khaine** · [2023-01-30 08:37 UTC](https://news.ycombinator.com/item?id=34577277)
  This looks great, does it also measure VOCs?  Aren't VOCs one of the main things households should be worried about? ^c34577277

- **unknown** · [2023-01-29 19:55 UTC](https://news.ycombinator.com/item?id=34572011)
  [deleted] ^c34572011

- **xtiansimon** · [2023-01-30 12:54 UTC](https://news.ycombinator.com/item?id=34578985)
  What’s the application of this project? Education? Or verifying your high-rise apartment has good air quality? ^c34578985

- **unknown** · [2023-01-29 21:55 UTC](https://news.ycombinator.com/item?id=34573183)
  [deleted] ^c34573183

