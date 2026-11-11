# [Low Cost CO2 Sensors Comparison: Photo-Acoustic vs. NDIR](https://news.ycombinator.com/item?id=35261115)

Article: [https://www.airgradient.com/open-airgradient/blog/co2-sensors-photo-acoustic-vs-ndir/](<https://www.airgradient.com/open-airgradient/blog/co2-sensors-photo-acoustic-vs-ndir/>)

zdw · 2023-03-22 14:02 UTC · 50 reported comments · archived 2026-11-08 12:49 UTC
Observation: 2026-11-08 12:49 UTC → 2026-11-08 12:49 UTC

## Comments

- **wkat4242** · [2023-03-24 02:54 UTC](https://news.ycombinator.com/item?id=35284469)
  Interesting comparison. But they don't mention that the NDIR sensors have much less drift. I've read that they can go without calibration (outside air) for much longer especially if you turn off auto calibration, without much loss of accuracy. ^c35284469

  It's probably also because no photoacoustic-based sensors have a control gas side like most NDIR sensors do have as the article does mentioned. So it's much easier to eliminate environmental factors. Temperature, pressure etc.

  Also photoacoustic sensors are pretty new so the tech may improve over time.

  If your scenario lets the sensor see outside air every few days both are fine, but I'd still prefer NDIR if space permits, at least for now.

  Even photoacoustic sensors aren't yet at the size you can put them in a phone by the way. The VOC/"eCO2" sensors are tiny and would fit in a phone but horribly inaccurate as the article says so their results aren't very useful (unless it's the VOC - Volatile Organic Component part you're interested in). But VOC doesn't really correlate to CO2 in a closed environment. For example, spray just a bit of alcohol in a room and it'll fly up like crazy but the real CO2 level will be unchanged.

  - **alwayslikethis** · [2023-03-24 03:35 UTC](https://news.ycombinator.com/item?id=35284777)
    Are you sure? I have a MH-Z19 and it drifted by more than 50\% (baseline went to about 180-200 ppm) after a month or two without calibration. It is from a reliable vendor and the readings are quite stable, so it's unlikely to be a fake sensor. ^c35284777

    - **ysleepy** · [2023-03-24 11:02 UTC](https://news.ycombinator.com/item?id=35287450)
      I have a MH-Z19C and have been running it with auto-calibration disabled for over a year and it didn't drift much. ^c35287450

      Is is possible that you have auto-cal on and the sensor is never exposed to true outside air? It uses some sort of minimum tracking to calibrate the \~400ppm point.

      This is anecdata though.

      - **wkat4242** · [2023-03-24 17:27 UTC](https://news.ycombinator.com/item?id=35292505)
        Exactly I'm pretty sure this is what it is. It won't drift much but you do have to turn the auto calibration off, otherwise it will grab any low CO2 moment and try to calibrate to it, drifting further off track with every calibration. ^c35292505

    - **wkat4242** · [2023-03-24 08:08 UTC](https://news.ycombinator.com/item?id=35286343)
      Well I heard this from someone using Sensirion SCD30/31s in implementations for industrial purposes. In my own application I use them at home only and I often have a chance to air them. ^c35286343

      What you need to do though is specifically turn off the auto calibration. Because if you don't, it will view any near-400 readings as '400' (e.g. thinking it's outside air) and the calibration is dragging itself off over time.

      The MH-Z19 is a bit cheaper and I don't really have direct experience with them, though I do have one in my Awair Lite.

- **teekert** · [2023-03-24 11:46 UTC](https://news.ycombinator.com/item?id=35287778)
  I have the Aranet4. Pretty expensive (220 eur) but I'm very happy with it. During the reconstruction of our house, we are sharing a bedroom with the kids. It's cold, we close things... First night I saw CO2 go up to 2500 ppm and I got up to open windows. I had headaches every morning, that's gone now (I do have cold nostrils now though). ^c35287778

  And now I'm using it to check all spaces, I'm going to need some active ventilation in almost all rooms it seems like.

  I feel that CO2 ppm is a good proxy for measuring the need for ventilation (which is also needed when cooking, moisture etc). I'm using the hell out of the device. It's nice that it will probably last \>1 year on a standard battery.

  One device in every room would be cool, coupled to Home Assistant to steer Blauberg ventilation units or something... The Aranet is too expensive for that, so great to see developments like this.

  - **umeshunni** · [2023-03-24 17:32 UTC](https://news.ycombinator.com/item?id=35292581)
    It's funny how even leaving the windows open for 15 minutes can lower the Co2 PPM by 400-500 points. ^c35292581

- **e12e** · [2023-03-24 09:53 UTC](https://news.ycombinator.com/item?id=35287006)
  \> When the CO2 molecules absorb the IR light, they start to “humm” and this sound can be picked up by a microphone. ^c35287006

  TIL - But where can I learn more? Is this a mostly classic effect (heat/shockwave) or mostly quantum level?

  - **mnw21cam** · [2023-03-24 12:28 UTC](https://news.ycombinator.com/item?id=35288132)
    A combination. The reason the CO2 absorbs that particular wavelength of IR light is deeply bound in quantum processes. But the reason they hum is simply a classic heat effect. ^c35288132

    - **e12e** · [2023-03-24 13:05 UTC](https://news.ycombinator.com/item?id=35288495)
      But the hum is a certain frequency - how is that? ^c35288495

      - **mnw21cam** · [2023-03-24 13:12 UTC](https://news.ycombinator.com/item?id=35288576)
        Because the IR light is turned on and off at that frequency. ^c35288576

        - **e12e** · [2023-03-24 13:39 UTC](https://news.ycombinator.com/item?id=35288919)
          Ah how boring (and clever). ^c35288919

          :)

- **unwind** · [2023-03-24 07:48 UTC](https://news.ycombinator.com/item?id=35286212)
  Absolutely fantastic, the graph with the two sensors (based on different technologies!) reporting every peak and valley in perfect synchronization almost made me cry. Beautiful. ^c35286212

  Then again the values reported are not the *same*, one of them seems to be more sensitive and goes higher/lower all the time, so I would still not know which sensor to get and how much to trust the data. I guess if the price is as equal as they state (\~\$20) then the more sensitive one would be "safer" if trying to avoid too high CO2 levels.

- **bsmth** · [2023-03-24 06:29 UTC](https://news.ycombinator.com/item?id=35285707)
  I've been interested in trying out different air sensors for a while. I tested out some of the super cheap ones ("MQ-7" etc.) for DIY cellular iot devices. I wasn't impressed at all with the accuracy, it was more like a random number generator. I recall that pre-heating was something you needed to do with it but I've since realized it's required once for 48 hours before general use, not a two-minute warmup each time a device is powered up. Anyway the general consensus seemed to be that anything under 50EUR was a waste of money. Did anyone else have success with the cheaper sensors? ^c35285707

  This post got me interested again in trying out something a bit more robust.  I've put through an order for the kit linked in the article. Looking forward to trying it out.

  - **mnw21cam** · [2023-03-24 12:31 UTC](https://news.ycombinator.com/item?id=35288164)
    The cheaper sensors detect volatile organic compounds, and assume that CO2 level correlates with that. This isn't necessarily true. BigClive tested one, and called it a party detector\[0\], because it was great at picking up alcohol, but not so good at detecting when a literal stream of CO2 was blasted at it. ^c35288164

    \[0\] [https://www.youtube.com/watch?v\=D2Wq4Yg52No](<https://www.youtube.com/watch?v=D2Wq4Yg52No>)

  - **illegalsmile** · [2023-03-24 13:49 UTC](https://news.ycombinator.com/item?id=35289048)
    I come from a remote environmental instrumentation background and it's pretty amazing where the technology has gone. I've built two of the airgradient kits, tested various relatively inexpensive sensors and compared them to professional grade sensors. While this stuff is not even close to research grade it's a fraction of the cost, \$35 for NDIR CO2? Crazy to me. You could setup a few of these sensors inexpensively, do an in-situ calibration (your house, backyard, whatever), model the response and apply a correction factor to give you some pretty good results. ^c35289048

    For homes good enough is fine so it's really cool to see these devices become more available. You'll have fun with the kit, it's super easy to use and really easy to integrate.

  - **ahaucnx** · [2023-03-24 07:11 UTC](https://news.ycombinator.com/item?id=35285977)
    Thanks for ordering our air quality monitoring kit! ^c35285977

    We use the same industry grade sensor modules that are normally in much more expensive commercial monitors. So the kit will give you very good accuracy.

- **alwayslikethis** · [2023-03-24 02:41 UTC](https://news.ycombinator.com/item?id=35284400)
  I wonder how long these last. I have a couple of MH-Z19 sensors (from a reliable source) and they drift (showing lower readings) by more than 50\% after a couple of weeks/months without calibration. If calibration is to compensate for the debris stuck in the sensor or declining source brightness, one must wonder how long the sensors would remain accurate for. Anyone knows enough to enlighten me on this? ^c35284400

  - **ahaucnx** · [2023-03-24 05:04 UTC](https://news.ycombinator.com/item?id=35285280)
    We usually use the SenseAir S8 NDIR sensors that have a very good quality but also have a couple of MH-Z19 sensors in monitors that run since a couple of years without issues. ^c35285280

    We ran a comparison between the two and the S8 and MH-Z19 pretty much delivers the same values (with ABS turned on).

    We use the automatic baseline calibration in pretty much all our installations so we do not have experience on long term drifts.

- **londons\_explore** · [2023-03-24 08:59 UTC](https://news.ycombinator.com/item?id=35286670)
  I wonder what would happen if phone manufacturers started integrating photo acoustic CO2 sensors in their phones? ^c35286670

  They could alert when CO2 goes over 1500 ppm and say 'Warning:. Harmful air quality detected.  Increase ventilation or move outdoors'.

  The same sensor could also detect Ozone, CO or NOx using different LED's, thereby making a pretty good detector for common poisonous gasses.

  - **Malic** · [2023-03-24 12:42 UTC](https://news.ycombinator.com/item?id=35288277)
    A crowd-sourced map of such levels across a large geographic area (with outdoor/indoor data) would be interesting to look at. ^c35288277

    Has anyone done something like this already?

    - **londons\_explore** · [2023-03-24 16:08 UTC](https://news.ycombinator.com/item?id=35291109)
      CO2 data is hard to crowdsource because the sensors aren't yet built into phones, and tend to all be proprietary with no standard interface. ^c35291109

- **nimish** · [2023-03-24 02:33 UTC](https://news.ycombinator.com/item?id=35284342)
  Infineon has a similar sensor, [https://www.infineon.com/cms/en/product/sensor/co2-sensors/p...](<https://www.infineon.com/cms/en/product/sensor/co2-sensors/pasco2v01/>) ^c35284342

  Neat little thing but you have to be sure to calibrate it.

- **dws** · [2023-03-24 04:46 UTC](https://news.ycombinator.com/item?id=35285188)
  Interesting that they don't recommend TVOC sensors. I spent a few months trying to get a set of CSS811 sensors to behave. They'd consistently, but erratically, drift upwards into "you should be dead now" territory, returning to believable levels only when fully reset. ^c35285188

  - **ahaucnx** · [2023-03-24 05:02 UTC](https://news.ycombinator.com/item?id=35285265)
    Author here. ^c35285265

    We do only recommend TVOC sensors to detect spikes but not for any specific concentration measurements. For spikes, TVOC has some use cases, e.g. detecting aggressive cleaning chemicals or leaking chemicals, e.g. in an art classroom if somebody forgot to close the pot with color.

    - **dws** · [2023-03-24 05:30 UTC](https://news.ycombinator.com/item?id=35285401)
      Agreed, thought it seems unlikely to me that the sensors I was testing were reacting to any sort of leak or out-gassing. They consistently showing a steady increase in TVOCs over 12 hours in an empty room with a window cracked. ^c35285401

      - **ahaucnx** · [2023-03-24 06:04 UTC](https://news.ycombinator.com/item?id=35285577)
        No experience with the CSS811 sensor but the Sensirion TVOC sensors definitely react very quickly to chemicals in the room. ^c35285577

        - **GeoAtreides** · [2023-03-24 09:03 UTC](https://news.ycombinator.com/item?id=35286699)
          Any experience with the Bosch BME680 (or 688)? Or, baring that, any use cases for TVOC sensors in a home? ^c35286699

          I mean, it's interesting to see the breath\_voc\_equivalent spiking up at night during my digestion, or spiking up after I eat beans, but otherwise I'm not getting anything unexpected out of it -- maybe my biggest discovery was finding out how much humidity influences air quality (most of the time it's almost like the air quality is a humidity inverted graph). And I suppose TVOC sensors might pick up things that your nose can't, but what that might be? Cleaning chemicals do tend to have powerful smells.

          Also, for people interesting in playing with sensors, nowadays you don't have to solder, as many sensors have Qwiic/QT connectors, you just plugged them in.

  - **numpad0** · [2023-03-24 09:48 UTC](https://news.ycombinator.com/item?id=35286974)
    Was it the Sparkfun BME280/CCS811 combo by chance? It seemed to drift up when temperature has positive errors and downward if negative, and the heater in CCS811 was affecting temperature reading on BME280. Adding a second temperature sensor delayed drift somewhat in my case, though the effect was marginal. ^c35286974

- **throwaway81523** · [2023-03-24 04:15 UTC](https://news.ycombinator.com/item?id=35285018)
  I think photoacoustic sensors used less power than NDIR, but maybe I'm wrong.  I'm glad to hear the accuracy is comparable.  I wasn't sure, so I bought an NDIR sensor from adafruit a while back. ^c35285018

- **haram\_masala** · [2023-03-24 02:38 UTC](https://news.ycombinator.com/item?id=35284385)
  The time plot of CO2 in the bedroom is sobering - it seems that they’re reaching levels where CO2 causes cognitive impairment. ^c35284385

  - **MBCook** · [2023-03-24 03:07 UTC](https://news.ycombinator.com/item?id=35284577)
    It doesn’t look like it hits 1000 ppm. I thought anything under 1000 was fine and concern didn’t start until closer to 1500. ^c35284577

    - **gambiting** · [2023-03-24 06:52 UTC](https://news.ycombinator.com/item?id=35285851)
      My office at home will quickly go over 2000 and then 3000ppm if I keep the door and window closed. It sucks in winter because I basically have to keep the window open(and be cold) if I want to have the privacy of a closed door. ^c35285851

      It did make me realize why I was feeling sleepy and not quite so focused after long period of time in that room, so getting a CO2 sensor was great in that sense. I also stopped closing the door to our bedroom - CO2 levels would easily go over 2500ppm overnight if you left the door closed.

      - **mschuster91** · [2023-03-24 07:16 UTC](https://news.ycombinator.com/item?id=35286012)
        If you own your home, you could install a ventilation system with an air-to-air heat exchanger with the outside... that way you at least reduce the heating loss. Or you install a forced ventilation towards whatever adjacent room there is, with a foam mesh to pad down on sounds. ^c35286012

        - **gambiting** · [2023-03-24 07:47 UTC](https://news.ycombinator.com/item?id=35286207)
          We wallet has involuntarily clenched at the thought of how much that would cost. I'll stick with opening the window for now I think. ^c35286207

          - **mschuster91** · [2023-03-24 08:08 UTC](https://news.ycombinator.com/item?id=35286344)
            Why? You can have a simple indoor exchange for under a hundred dollars - a simple bathroom fan for 20€ would be a starter if you don't mind its noise, but stuff like axial fans for pot growers is pretty cheap as well (e.g. \[1\]). That, a 100mm core drill and a fairly simple mechanical 230V switch on the door should be enough. ^c35286344

            A heat exchange fan can be had for 525€ \[2\].

            \[1\] [https://www.grow-shop24.de/Silent-Axialluefter-100m-h-100mm-...](<https://www.grow-shop24.de/Silent-Axialluefter-100m-h-100mm-Anschluss>)

            \[2\] [https://raumluft-shop.de/getair-smartfan-dezentraler-wohnrau...](<https://raumluft-shop.de/getair-smartfan-dezentraler-wohnraumlueftung-mit-waermerueckgewinnung-komplett-set-ohne-steuerung.html>)

            - **gambiting** · [2023-03-24 09:31 UTC](https://news.ycombinator.com/item?id=35286880)
              Because labour is crazy and I don't feel comfortable doing this myself. I've recently had a basic AC unit installed at home, it was £500 for the hardware and then another £1000 on top of that for the installation. I imagine that exchange fan would be at least £1000 installed and I just don't have a grand laying around spare to do this. ^c35286880

              - **mschuster91** · [2023-03-24 12:16 UTC](https://news.ycombinator.com/item?id=35288018)
                Yeah, AC units do require a lot of specialized labor to install (in some jurisdictions, it actually may even be mandated by law)... but a simple fan? That's half an hour for the drill, half an hour for the electrician and that's it. ^c35288018

  - **elcritch** · [2023-03-24 02:50 UTC](https://news.ycombinator.com/item?id=35284446)
    I could imagine that happens in many boardrooms too. ;) ^c35284446

- **Havoc** · [2023-03-24 15:15 UTC](https://news.ycombinator.com/item?id=35290132)
  Found some SCD41 on aliexpress for aroundd 17 bucks so will give that a shot. ^c35290132

  The existing TVOC got is functionally useless due to drift

- **bsder** · [2023-03-24 05:25 UTC](https://news.ycombinator.com/item?id=35285372)
  Why do these things bottom out at 400ppm when that's supposed to be the "normal" CO2 level? ^c35285372

  - **gambiting** · [2023-03-24 06:55 UTC](https://news.ycombinator.com/item?id=35285867)
    Because......you can't really go below it? So they are calibrated to start at 400ppm, because your ambient air won't have any less than that unless you have active CO2 scrubbers running, and that's very very rare. ^c35285867

    Also I have multiple SCD41 sensors and can confirm that they do give you values both below 400ppm and above 5000ppm - they just get less accurate out of that range.

    - **snvzz** · [2023-03-24 07:06 UTC](https://news.ycombinator.com/item?id=35285946)
      I can't get below 400ppm even outdoors. ^c35285946

      - **gambiting** · [2023-03-24 07:15 UTC](https://news.ycombinator.com/item?id=35286010)
        That's the point - globally all air now contains above 400ppm, it's the great tragedy of climate change. You can only see less than 400ppm if you put the sensor in an airtight container and add something that absorbs CO2 to it - then the value will go below 400ppm. But because that's not how most people use these sensors, they are calibrated for 400ppm upwards. ^c35286010

      - **Robotbeat** · [2023-03-24 07:16 UTC](https://news.ycombinator.com/item?id=35286015)
        I would hope not: [https://www.co2.earth/](<https://www.co2.earth/>) ^c35286015

    - **Robotbeat** · [2023-03-24 07:15 UTC](https://news.ycombinator.com/item?id=35286005)
      A freshly poured concrete structure with poor ventilation can go well below 400ppm. ^c35286005

      - **gambiting** · [2023-03-24 07:16 UTC](https://news.ycombinator.com/item?id=35286018)
        Sure, so like I said, you have a situation where a CO2 scrubber(in that case concrete) is present. If you need accurate measurement of CO2 below 400ppm and not just "it's less than 400ppm" then you need to buy a different sensor. ^c35286018

        - **Robotbeat** · [2023-03-24 18:29 UTC](https://news.ycombinator.com/item?id=35293494)
          This is a problem if you have a fairly well-sealed greenhouse as well. The CO2 level can go below 400ppm and reduce plant productivity. ^c35293494

          If you have a suggestion for a good but affordable CO2 sensor that can measure at or below 400ppm reliably, I’m all ears!

          - **gambiting** · [2023-03-24 18:34 UTC](https://news.ycombinator.com/item?id=35293556)
            So all Sensiron sensors are tuned for minimum 400ppm, other than this one: ^c35293556

            [https://sensirion.com/products/catalog/STC31](<https://sensirion.com/products/catalog/STC31>)

            The problem is that it gives you percentage of CO2 in air instead of ppm, it can go all the way down to 0\% though. I guess there must be a way to figure out the ppm based on that? I guess?

            Here's an example of a product with this sensor already integrated:

            [https://www.sparkfun.com/products/18385](<https://www.sparkfun.com/products/18385>)

            Also I want to point out that their other sensors(SCD40 and SCD41) will actually give you a value even below 400ppm - just that their accuracy drops below that value. So it might say it's 300ppm when in reality it's 250ppm. Not sure how important it is for you.

- **snvzz** · [2023-03-24 07:06 UTC](https://news.ycombinator.com/item?id=35285940)
  SDC30 has higher accuracy and cost me almost the same as SDR41 price I'm seeing. I am confused. ^c35285940

