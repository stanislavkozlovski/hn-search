# [Air Quality Monitors from USD \$169 to \$6k use the same low-cost PM Modules](https://news.ycombinator.com/item?id=37652832)

Article: [https://www.airgradient.com/blog/most-aq-monitors-use-same-pm-modules/](<https://www.airgradient.com/blog/most-aq-monitors-use-same-pm-modules/>)

ahaucnx · 2023-09-26 00:41 UTC · 71 reported comments · archived 2026-11-08 13:14 UTC
Observation: 2026-11-08 13:13 UTC → 2026-11-08 13:14 UTC

## Comments

- **emmanuel\_1234** · [2023-09-26 14:16 UTC](https://news.ycombinator.com/item?id=37659703)
  This reads like a disguised ad for AirGradient, which pops up here every now and then. I fell for it because it claimed to be "open". Well, although it is definitely more "open" than most, it feels like an afterthought. ^c37659703

  See for example this: [https://forum.airgradient.com/t/airgradient-diy-pro-pcb-3-7-...](<https://forum.airgradient.com/t/airgradient-diy-pro-pcb-3-7-2-4-1-2023-04-13-source-code-sketch/927/13>), linked to a Github issue opened in June.

  Somehow, the source code for the new version has been overwritten by an older (CC-BY-NC) version, yet the issue has been left to rot, both on the support forum and on Github, letting me to think that the "openness" is mostly a posture to lure the HN crowd. Additionally, the -NC clause is definitely a deal breaker, and I should have investigated further before giving them my money.

  (it sucks to air it out in public here, but apparently the AirGradient folks don't care much about issues raised on their own forum).

  - **ahaucnx** · [2023-09-26 14:33 UTC](https://news.ycombinator.com/item?id=37659983)
    Achim from AirGradient here. First of all, I appreciate your openness and I hope the following helps to clarify a few things: ^c37659983

    1) All our monitor kits are licensed under CC-BY-SA (and not as mentioned above CC-BY-NC). There was a short period where we had them under NC license but since NC is not truely open-source we switched to the more permissive SA license. We wrote in more detail about this on our blog \[1\]

    2) We are aware that our open-source firmware is currently lacking the quality level we would like to see because we have been very busy with the hardware side of the project. I do hope that in the coming months we will have more time to look after the firmware side and I already had a couple of calls with contributors in the last few days who are happy to help. It's definitely an area we need to improve.

    We are currently setting up a focus group and I would love to have people included that might have a more critical view on the project. Please contact me if you would be interested to participate.

    \[1\] [https://www.airgradient.com/blog/thoughts-on-licensing/](<https://www.airgradient.com/blog/thoughts-on-licensing/>)

    - **loufe** · [2023-09-26 15:40 UTC](https://news.ycombinator.com/item?id=37660989)
      An easy first step would be to do a minimum of engagement with those people kindly putting effort into submitting PRs to the repo. You could even assign a community maintainer to help with testing and managing PRs and issues if you don't have the time. ^c37660989

      - **ahaucnx** · [2023-09-26 15:44 UTC](https://news.ycombinator.com/item?id=37661053)
        Thank you. This is a good suggestion. ^c37661053

  - **CodesInChaos** · [2023-09-26 15:33 UTC](https://news.ycombinator.com/item?id=37660882)
    [https://github.com/airgradienthq/arduino/blob/master/example...](<https://github.com/airgradienthq/arduino/blob/master/examples/DIY_PRO_V4_2/DIY_PRO_V4_2.ino>) ^c37660882

    The current version of the file mentioned in that thread says CC-BY-SA [https://github.com/airgradienthq/arduino/blob/master/example...](<https://github.com/airgradienthq/arduino/blob/master/examples/DIY_PRO_V4_2/DIY_PRO_V4_2.ino>)

    (Though I don't understand why anybody would use CC-BY-SA for code, instead of a copyleft license designed for code)

  - **ahaucnx** · [2023-09-27 04:06 UTC](https://news.ycombinator.com/item?id=37669958)
    Your comment about "disguised ad" also gave us some food for thought and I just wrote an article how we want to be transparent about our own product promotions and some changes we have implemented \[1\]. ^c37669958

    \[1\] [https://www.airgradient.com/blog/are-our-articles-disguised-...](<https://www.airgradient.com/blog/are-our-articles-disguised-ads/>)

  - **scottlamb** · [2023-09-26 15:29 UTC](https://news.ycombinator.com/item?id=37660804)
    \> Somehow, the source code for the new version has been overwritten by an older (CC-BY-NC) version, yet the issue has been left to rot, both on the support forum and on Github, letting me to think that the "openness" is mostly a posture to lure the HN crowd. Additionally, the -NC clause is definitely a deal breaker, and I should have investigated further before giving them my money. ^c37660804

    As an AirGradient customer, I just don't care about that. The software side isn't complicated, and I prefer running these things with ESPhome rather than their Airduino sketch anyway. The value of AirGradient for me is that they've curated a nice collection of sensors, designed a good enclosure and matching PCB mask for them, and are offering them at a very affordable price for DIYers.

    - **margalabargala** · [2023-09-26 15:52 UTC](https://news.ycombinator.com/item?id=37661171)
      Same. I buy my hardware from airgradient, I flash ESPHome onto it, I ignore the airgradient software (sorry airgradient!). ^c37661171

      I appreciate that they are open with their hardware, and make it seamlessly easy to do the above, and also that they provide information into the industry like with this article. So I give them my money for their hardware rather than purchasing the components separately.

    - **toomuchtodo** · [2023-09-26 15:30 UTC](https://news.ycombinator.com/item?id=37660823)
      \+1, it just works, that is superior imho vs being as open as some are demanding (as an AirGradient customer). ^c37660823

      \> Well, although it is definitely more "open" than most, it feels like an afterthought.

      Open enough!

  - **M3t0r** · [2023-09-26 16:01 UTC](https://news.ycombinator.com/item?id=37661303)
    I got an AirGradient like 2 years ago and was very disappointed with the quality of the firmware. I wrote my own with Arduino which was good enough for \~2 years. But last week I found out about ESPHome, and they have a blueprint [https://devices.esphome.io/devices/AirGradient-DIY](<https://devices.esphome.io/devices/AirGradient-DIY>) that just works. My (slightly) customized version: [https://gist.github.com/M3t0r/b81ce82796a2ec30f5470f1345f9ca...](<https://gist.github.com/M3t0r/b81ce82796a2ec30f5470f1345f9ca97>) ^c37661303

    Whatever you think of the openness or quality of the firmware, the hardware is open enough to just flash your own.

  - **snapplebobapple** · [2023-09-26 23:50 UTC](https://news.ycombinator.com/item?id=37667553)
    Am i the weird one? I don't think i even booted their firmware before flashing the unit with esphome (which is awesome one can juat do that) ^c37667553

- **ahaucnx** · [2023-09-26 14:02 UTC](https://news.ycombinator.com/item?id=37659452)
  Author here. I'm planning to do some more comparison testing of PM modules and planning to benchmark modules from Sensirion, Plantower, Cubic and AlphaSense. Let me know if you know some other sensor modules that could be interesting. I think this could be a pretty interesting follow up post. ^c37659452

  - **stephen\_g** · [2023-09-26 15:21 UTC](https://news.ycombinator.com/item?id=37660675)
    Do you know what sensor is in the Davis Instruments Airlink? I was thinking of buying one but it's just PM, no CO2 or VOC sensors I believe. ^c37660675

    - **ahaucnx** · [2023-09-26 15:25 UTC](https://news.ycombinator.com/item?id=37660748)
      It looks to also have a Plantower PM sensor but the smaller version (PMSA003) \[1\]. ^c37660748

      \[1\] [http://www.aqmd.gov/docs/default-source/aq-spec/field-evalua...](<http://www.aqmd.gov/docs/default-source/aq-spec/field-evaluations/davis-instrument-airlink---field-evaluation.pdf?sfvrsn=14>)

      - **stephen\_g** · [2023-09-26 15:45 UTC](https://news.ycombinator.com/item?id=37661062)
        Ah cool, thanks! I assumed that would be in that report but I can't get that domain to load for some reason! ^c37661062

        - **ahaucnx** · [2023-09-26 15:53 UTC](https://news.ycombinator.com/item?id=37661183)
          By the way, we have worked with the Plantower A003 and saw much more failure rates than with the 5003 model. So I'd not really recommend it. ^c37661183

  - **agloe\_dreams** · [2023-09-26 14:46 UTC](https://news.ycombinator.com/item?id=37660201)
    I do wonder where the VINDSTYRKA sits...though I kinda imagine that if anyone beats your price point per quality you probably wouldn't actually say. ^c37660201

    - **ahaucnx** · [2023-09-26 14:49 UTC](https://news.ycombinator.com/item?id=37660245)
      The VINDSTYRKA does not contain a CO2 module which is the most expensive part of the BOM, so it's not directly comparable. ^c37660245

      For this blog post I only looked at the monitor tested by AQ-Spec \[1\] and the Ikea one is not in their list.

      \[1\] [https://www.aqmd.gov/aq-spec/evaluations/criteria-pollutants...](<https://www.aqmd.gov/aq-spec/evaluations/criteria-pollutants/summary-pm>)

      - **clairity** · [2023-09-26 16:05 UTC](https://news.ycombinator.com/item?id=37661366)
        no one should worry about CO₂ *at all* in their homes or offices. only workers in certain industries/factories, where CO₂ can get several orders of magnitude higher, need to be concerned at all about it. you (here and in your marketing materials) are stoking needless anxiety over a gas that life on earth literally *requires*. ^c37661366

        pollutants, on the other hand, and particularly particulate matter (especially chemicals that we've manufactured recently in human history), do have proven negative health consequences and should be monitored and mitigated in the home and office. it's estimated that over a million people a year die prematurely of respiratory and cardiovascular complications due to pollution.

        in short, a lack of CO₂ monitoring in favor of PM and VOCs by ikea should be seen as a plus, not a minus here.

        note that VOCs are typically estimated from cheap CO₂ sensors, and are likely to be highly unreliable as a result, but more accurate (and more expensive) VOC sensing is possible, e.g., [https://www.degruyter.com/document/doi/10.1515/revac-2021-01...](<https://www.degruyter.com/document/doi/10.1515/revac-2021-0127/pdf>)

        - **amluto** · [2023-09-26 17:08 UTC](https://news.ycombinator.com/item?id=37662440)
          I thought cheap instruments usually estimated CO2 from a MOS TVOC sensor. ^c37662440

          In any case, for automation purposes, CO2 sensing is extremely useful.  Regardless of whether you think indoor CO2 directly causes cognitive performance issues or is a proxy for other things that cause those issues (the issues themselves are well documented), indoor CO2 is an excellent measure for the fraction of indoor air consisting of exhaled air, which is a good thing to use for automated demand controlled ventilation.

        - **vGPU** · [2023-09-28 01:36 UTC](https://news.ycombinator.com/item?id=37684085)
          Not at all. The majority of studies have found a notable decline in cognitive ability starting somewhere around the 800-1,200 ppm range. Due to increasing insulation/energy standards/etc, modern homes have poor air exchange and levels will often get that high or higher unless a window is opened. I have seen quite a few reports of people seeing levels exceeding 2,000 at night, and multiple studies showing that many multifamily/efficiency homes would easily get over that 1,000 ppm mark. ^c37684085

    - **louwrentius** · [2023-09-26 15:51 UTC](https://news.ycombinator.com/item?id=37661151)
      Not sure if it really helps but I wrote something about it: ^c37661151

      [https://louwrentius.com/ikea-50-vindstyrka-vs-290-dylos-air-...](<https://louwrentius.com/ikea-50-vindstyrka-vs-290-dylos-air-quality-monitor.html>)

- **an\_account** · [2023-09-26 14:28 UTC](https://news.ycombinator.com/item?id=37659886)
  I’ve gone down the air quality monitor rabbit hole and, after building my own, have settle on just buying/recommending the Awair Element.\[1\] ^c37659886

  Interestingly, it’s not in the table in this article.

  \[1\] [https://www.getawair.com/products/element](<https://www.getawair.com/products/element>)

  - **ahaucnx** · [2023-09-26 14:36 UTC](https://news.ycombinator.com/item?id=37660021)
    I only took sensors that have been tested by AQ-Spec into consideration because they mention the PM module used and the Awair Element was not tested by them. ^c37660021

  - **ahaucnx** · [2023-09-27 06:35 UTC](https://news.ycombinator.com/item?id=37670974)
    Be aware that Awair has intentionally bricked their first generation of Monitors \[1\]. ^c37670974

    \[1\] [https://www.reddit.com/r/Awair/comments/y7i5ku/awair\_discont...](<https://www.reddit.com/r/Awair/comments/y7i5ku/awair_discontinues_support_for_v1_devices/>)

  - **newfonewhodis** · [2023-09-26 15:22 UTC](https://news.ycombinator.com/item?id=37660696)
    I'm curious, what did you learn in your research? What made you land on Awair? ^c37660696

  - **FloatArtifact** · [2023-09-26 15:47 UTC](https://news.ycombinator.com/item?id=37661085)
    Cost is quite a bit higher over \$200 and the components can't be replaced. This is important as there's a limited lifespan of certain sensors which should be taken into account. ^c37661085

    - **merrywhether** · [2023-09-26 16:36 UTC](https://news.ycombinator.com/item?id=37661844)
      At least for the previous model, the sensor module was an all-in-one that I was able to easily replace myself with the exact part from AliExpress. It wasn’t officially replaceable but it was fewer than 10 screws and like a 2/10 difficulty. Afterwards it booted right up. ^c37661844

    - **mr\_november** · [2023-09-26 17:19 UTC](https://news.ycombinator.com/item?id=37662637)
      Currently 25\% off bringing it to \~\$155 so I pulled the trigger. ^c37662637

      Was going to buy the air gradient but shipping is not free and is for the awair so difference was negligible.

      Would also love to hear why grandparent poster has settled on recommending the awair over others.

- **iancmceachern** · [2023-09-26 14:50 UTC](https://news.ycombinator.com/item?id=37660254)
  This is common. ^c37660254

  Bluetooth headsets?  There are only a handful of chipsets in all.

  A to D converters?  Same.

  On and on.  There are often not more than a handful of options for many ics.

- **rapjr9** · [2023-09-27 02:04 UTC](https://news.ycombinator.com/item?id=37668904)
  I like the Dylos laser particle counter: ^c37668904

  [http://dylosproducts.com/dc1100paqmc.html](<http://dylosproducts.com/dc1100paqmc.html>)

  The version I have has an RS-232 output and a graphing program that runs on Windows.  Connect it to an old laptop with an FTDI USB to RS-232 cable and you can log particle count histories.  You have to clear the air intake port of dust once in a long while with a burst of compressed air.

  The Sharp LED dust sensors aren't as accurate as a laser counter, but can give you a useful enough readout for dust and smoke:

  [https://global.sharp/products/device/lineup/selection/opto/d...](<https://global.sharp/products/device/lineup/selection/opto/dust/index.html>)

  These are probably what is in the cheapest air quality monitors.

- **RecycledEle** · [2023-09-26 20:57 UTC](https://news.ycombinator.com/item?id=37665706)
  During the pandemic I took 2 clear tubes, and put PM meters in them. I used tape to tape various COVID masks between them and to seal them kind of air tight. Then I placed computer fans at each end to push air through. I learned that the best filters I could get only worked down to 2.5 microns. ^c37665706

- **bearjaws** · [2023-09-26 15:09 UTC](https://news.ycombinator.com/item?id=37660519)
  At the point where you spend \>\$400 you might as well buy hardware to purify the air... Unless you have a very specific molecule in mind, a standard HEPA + carbon filter will fix 99\% of your problem. ^c37660519

  - **stephen\_g** · [2023-09-26 15:14 UTC](https://news.ycombinator.com/item?id=37660571)
    Usually yes. But it does depend on the air quality outside and how leaky the building is - in certain places with very poor air quality you'd need a very serious flow rate through your purifier to keep up unless you have a positive pressure system (where you filter the air coming in to the building instead of just recirculating through a filter), and keep it at a positive pressure to stop dirty air constantly leaking in (especially when running bathroom exhaust fans or kitchen rangehoods that vent outside). ^c37660571

    In fact there's an article on the very same blog as the original post about it - [https://www.airgradient.com/blog/positive-pressure-systems-f...](<https://www.airgradient.com/blog/positive-pressure-systems-for-clean-air/>)

    Of course the downside is larger load on air conditioning, at which point you can look at heat recovery or energy recovery ventilation systems. I'm quite keen to get one of those to get more fresh air in since I can't leave my front or most of the side windows of the house open at night (road gets too noisy in the morning).

    - **FabHK** · [2023-09-26 15:39 UTC](https://news.ycombinator.com/item?id=37660969)
      Exactly. It's fairly straightforward to get PM2.5 down while CO2 goes up, and vice versa. The trick is to control both. ^c37660969

  - **Retric** · [2023-09-26 15:17 UTC](https://news.ycombinator.com/item?id=37660618)
    Smoke (aka fire), Humidity, and Carbon monoxide are worth monitoring and aren’t going to be fixed by a HEPA and carbon filter.  Further if you’re concerned about regular air pollution it’s worth verifying how well your filtration is working. ^c37660618

    - **aidenn0** · [2023-09-26 15:43 UTC](https://news.ycombinator.com/item?id=37661033)
      Smoke is a combination of particulates and VOCs which will respectively be filtered by HEPA and carbon filters. ^c37661033

      - **ahaucnx** · [2023-09-26 15:46 UTC](https://news.ycombinator.com/item?id=37661083)
        Carbon filters typically do not last very long so it's good to monitor TVOCs. ^c37661083

        - **aidenn0** · [2023-09-26 15:53 UTC](https://news.ycombinator.com/item?id=37661176)
          Oh, absolutely; I was just responding to the claim that smoke isn't filterable. ^c37661176

          If you have an intentional fire, you can maintain your filters and run them; spot checking particulates and VOCs.

          If you are worried about unintentional fires, you address that with a \$40 smoke alarm, not a \$6k AQM.

          - **Retric** · [2023-09-26 16:09 UTC](https://news.ycombinator.com/item?id=37661438)
            You missed the point.  Smoke from a burning couch isn’t the issue, the burning couch is. ^c37661438

            - **aidenn0** · [2023-09-26 16:17 UTC](https://news.ycombinator.com/item?id=37661552)
              \> If you are worried about unintentional fires, you address that with a \$40 smoke alarm, not a \$6k AQM. ^c37661552

              - **Retric** · [2023-09-26 16:36 UTC](https://news.ycombinator.com/item?id=37661853)
                Redundancy.  Also, 40\$ smoke detectors can take a while to alert you to a fire in your basement etc.  So it’s often a good idea to have a whole house smoke alarm system. ^c37661853

        - **reaperman** · [2023-09-26 15:56 UTC](https://news.ycombinator.com/item?id=37661226)
          These last a long time, FWIW. \>1 year at surprisingly high flow rates. ^c37661226

          [https://terra-bloom.com/collections/carbon-filters](<https://terra-bloom.com/collections/carbon-filters>)

      - **Retric** · [2023-09-26 16:06 UTC](https://news.ycombinator.com/item?id=37661382)
        Not when the house fire consumes you and the HEPA filers… ^c37661382

        For wildfire smoke you still want monitoring as existing filters may not be enough.  Temporary measures like sticking extra filters in front of fans may be necessary.

        - **michaelt** · [2023-09-26 16:16 UTC](https://news.ycombinator.com/item?id=37661542)
          I'm pretty sure smoke detectors for fire don't cost \$169, let alone \$6k. ^c37661542

          - **Retric** · [2023-09-26 16:44 UTC](https://news.ycombinator.com/item?id=37661978)
            When you only want to detect smoke that’s cheap, but as you add features you do eventually get into that price range. ^c37661978

            Ie: Smoke only costs less than Smoke + carbon monoxide.  People want to monitor levels not just have an alarm which requires a screen or network connectivity.  People want to know if there’s a fire in the building even if there far enough away not to hear a local alarm etc etc.

            Though eventually you circle back and have a cheap smoke alarm for redundancy.

- **jiveturkey** · [2023-09-26 15:30 UTC](https://news.ycombinator.com/item?id=37660818)
  why do we have to keep suffering these AurGradient ads? the sensor itself is not close to being the whole story. as evidenced by the price range of the complete products built around said sensors. ^c37660818

  - **jiveturkey** · [2023-09-27 20:59 UTC](https://news.ycombinator.com/item?id=37681226)
    should have said it at the same time. i'm sure i've posted this in the past. if AirGradient wishes to be taken seriously they need to get on this list: ^c37681226

    [http://www.aqmd.gov/aq-spec/evaluations/criteria-pollutants/...](<http://www.aqmd.gov/aq-spec/evaluations/criteria-pollutants/summary-pm>)

    AFAICT [https://www.aqmd.gov/aq-spec/sensors](<https://www.aqmd.gov/aq-spec/sensors>) is the same set of what they call "sensors" (but which are actually complete products), just the web page organized a little differently.

    Until I see an independent evaluation, AirGradient's claims are just as useless as other vendor's claims.

    I don't understand this bit from the AirGradient page [https://www.airgradient.com/research/](<https://www.airgradient.com/research/>) :

    \> Open Air will focus on PM2.5 measurements

    AQI is based on PM1.0, PM2.5 and PM10 measurement. Their products all (including the Open Air referenced in that page) appear to use Plantower sensors, which measure all 3 sizes.

- **quickthrowman** · [2023-09-26 16:44 UTC](https://news.ycombinator.com/item?id=37661979)
  Does anyone with an AQI sensor in their house actually use it to control HVAC equipment, or is it just for monitoring? In a commercial HVAC control system, if the AQI sensor (or CO2/NO2) reaches \[setpoint\], a make-up air unit and exhaust fan (or similar setup, could be an exhaust fan and outside air damper) will turn on until the AQI value is below the setpoint. Is anyone using an AQI sensor to energize a relay coil to turn on their furnace fan to try and correct PM2.5 and CO2 levels? ^c37661979

  - **highclass** · [2023-09-27 15:54 UTC](https://news.ycombinator.com/item?id=37676558)
    In Korea, they sell complete systems that do this. Basically sensor and HVAC and/or kitchen stove fan. These systems are built in high-end new apartments. ^c37676558

- **nikisweeting** · [2023-09-26 13:32 UTC](https://news.ycombinator.com/item?id=37659049)
  This is the best one I've seen: [https://boseansafety.com/products/air-quality-monitor-home-t...](<https://boseansafety.com/products/air-quality-monitor-home-t-z01>) ^c37659049

  It's by an industrial mining supply company instead of a consumer goods company, and seems to be more accurate than the cheap Amazon options I tried.

  - **lysp** · [2023-09-26 13:45 UTC](https://news.ycombinator.com/item?id=37659229)
    This seems to look very similar to generic ali express sensors: ^c37659229

    ie. Quick search:

    [https://www.aliexpress.com/item/1005005944910617.html](<https://www.aliexpress.com/item/1005005944910617.html>)

    Generally things without user manuals, or proper specifications are either directly from there, or rebadged from there.

    - **dahart** · [2023-09-26 14:04 UTC](https://news.ycombinator.com/item?id=37659495)
      Ali express has the Bosean, and the specs appear to be different from the link you found. [https://www.aliexpress.us/item/3256803168407076.html](<https://www.aliexpress.us/item/3256803168407076.html>) ^c37659495

      I see multiple knock-offs of the version you linked, the packaging looks different than the Bosean. Is the lack of a brand or company name printed on the device a potential clue about which one’s a knock-off?

  - **pxx** · [2023-09-26 14:21 UTC](https://news.ycombinator.com/item?id=37659773)
    It seems unlikely it has a true CO2 sensor for that price point (it could, but the bom price of just the module is over \$20). The co2 "equivalent" from VOC sensors is pretty crappy in my experience. ^c37659773

    - **bananapub** · [2023-09-26 14:46 UTC](https://news.ycombinator.com/item?id=37660208)
      while true that actual CO2 sensors are expensive, this device doesn't even claim to have one ^c37660208

      - **mikestew** · [2023-09-26 14:55 UTC](https://news.ycombinator.com/item?id=37660318)
        Scroll down, and it shows a CO2 measurement on the screen. ^c37660318

  - **jondwillis** · [2023-09-26 13:35 UTC](https://news.ycombinator.com/item?id=37659090)
    Invalid SSL cert, ironic for that domain name! ^c37659090

    edit) nevermind, on public wifi

    - **sinuhe69** · [2023-09-26 13:40 UTC](https://news.ycombinator.com/item?id=37659151)
      It uses a certificate issued by Let's Encrypt, so you might need to update your root certificates list. ^c37659151

    - **TonyTrapp** · [2023-09-26 13:39 UTC](https://news.ycombinator.com/item?id=37659138)
      No issues here with the certificate (Firefox / Windows). ^c37659138

    - **dewey** · [2023-09-26 13:38 UTC](https://news.ycombinator.com/item?id=37659124)
      Works for me on iOS Safari, maybe something on your end? ^c37659124

- **jpambrun** · [2023-09-26 16:42 UTC](https://news.ycombinator.com/item?id=37661953)
  It would be nice to add radon to the table. Some consumer air quality monitor have it and the usability of the mail test means many people don't know their exposure. ^c37661953

- **remlov** · [2023-09-26 13:49 UTC](https://news.ycombinator.com/item?id=37659273)
  ̶\>̶ ̶*̶1̶6̶9̶.̶0̶0̶ ̶t̶o̶ ̶6̶.̶0̶0̶0 ̶U̶S̶D̶.̶*̶ ^c37659273

  Title was corrected.

  Kit costs 138.00, fully assembled costs even more.

  - **LeifCarrotson** · [2023-09-26 14:05 UTC](https://news.ycombinator.com/item?id=37659510)
    The current edition of the "kit" is just a pre-soldered PCB, a plastic case, and some screws, it's basically a complete product. ^c37659510

    The original DIY basic or pro kit are also close to complete - basically dropping some dev boards on 0.1" headers onto the PCB (and a USB-C connector, and 1.25mm pitch PM sensor cable, slightly harder).

    You can also get just the bare sensor from a reputable distributor for \$40:

    [https://www.adafruit.com/product/3686](<https://www.adafruit.com/product/3686>)

    Or get the same sensor from overseas for about \$12.

    I just built the AirGradient DIY Pro kit (no longer listed for sale on the website?), it's remarkable how PM and CO2 spike through the whole house when we cook on our natural gas stove - been waffling on that induction cooktop, but it's probably time! Still need to get the TVOC/NOx module to add to it...

    - **ahaucnx** · [2023-09-26 14:11 UTC](https://news.ycombinator.com/item?id=37659619)
      We actually plan to bring the version back that needs soldering. We took it temporarily out of the shop because a number of people overestimated their soldering skills and couldn't get it running. The usb and jst plug are difficult to solder for people without much experience. ^c37659619

      - **LeifCarrotson** · [2023-09-26 18:34 UTC](https://news.ycombinator.com/item?id=37663810)
        FWIW, I had no problem building it, but I'm an EE with decades of experience and the right tools like a proper temperature-controlled soldering station, hot air, magnification, paste/flux/wick, etc.  I agree it would not be reasonable for someone without both a modicum of skill and the right tools. ^c37663810

        Having taught a number of coworkers to solder, it's hard to convey exactly what difficulty that entails without either scaring off worried potential buyers who could do it or giving overconfident buyers who can't do it an excess of confidence. There's probably a good deal of overlap between those two groups. Thanks for pulling it temporarily while you figure out a compromise.

        I did wish that the guidance on the JST connector orientation was better - a little silkscreen with "1 BLK" and "8 PUR", or a representation of the connector tabs/slot orientation, would have meant I didn't have to squint at photos. There'd be room for that info on a pre-built picoblade to 0.1" header adapter board...

        Also, my kit did not include the large electrolytic capacitor, but I had a suitable one on hand.

    - **\_2d30** · [2023-09-26 14:53 UTC](https://news.ycombinator.com/item?id=37660294)
      Your PM2.5 will spike from cooking regardless. Doesn’t matter the method of heat, it’s from the food. ^c37660294

      - **LeifCarrotson** · [2023-09-26 18:34 UTC](https://news.ycombinator.com/item?id=37663816)
        Time to test and maybe improve the exhaust fan, it's so loud right now we usually don't use it... ^c37663816

    - **remlov** · [2023-09-26 14:08 UTC](https://news.ycombinator.com/item?id=37659561)
      Looking closer, this is probably a cheaper much more feature rich alternative to the aranet4 I've got. ^c37659561

      - **ahaucnx** · [2023-09-26 14:15 UTC](https://news.ycombinator.com/item?id=37659685)
        The AirGradient also uses a SenseAir CO2 Sensor like the Aranet but also measures additionally PM and TVOCs. ^c37659685

  - **ahaucnx** · [2023-09-26 13:54 UTC](https://news.ycombinator.com/item?id=37659344)
    The range is up to six thousand dollars, not six dollars. ^c37659344

    - **remlov** · [2023-09-26 14:04 UTC](https://news.ycombinator.com/item?id=37659490)
      I stand corrected. The period in 6.000 in place of a comma threw me off. ^c37659490

