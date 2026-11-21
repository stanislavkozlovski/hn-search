# [Open Source Outdoor Air Quality Monitor](https://news.ycombinator.com/item?id=36922790)

Article: [https://www.airgradient.com/open-air/](<https://www.airgradient.com/open-air/>)

ahaucnx · 2023-07-29 17:59 UTC · 96 reported comments · archived 2026-11-08 13:11 UTC
Observation: 2026-11-08 13:10 UTC → 2026-11-08 13:11 UTC

## Comments

- **ahaucnx** · [2023-07-29 19:21 UTC](https://news.ycombinator.com/item?id=36923556)
  I'm the founder of AirGradient and last year we have decided to focus our company on open hardware air quality monitors that we produce professionally. ^c36923556

  Our outdoor monitor Open Air has been designed from the start as an open hardware project with a beautiful plastic injected enclosure to demonstrate that open source hardware can look and perform on the same level like traditional products.

  We do also work intensively with research institutions around the world to test the monitor and ensure that the monitors are as accurate as possible \[1\].

  Happy to answer any question that might come up.

  \[1\] [https://www.airgradient.com/research/](<https://www.airgradient.com/research/>)

  - **cyberax** · [2023-07-29 20:49 UTC](https://news.ycombinator.com/item?id=36924409)
    How good is the calibration for your temperature and humidity sensors? ^c36924409

    I'm absolutely miffed by the poor-quality sensors that are off by 10\% humidity and 2-3C of temperature. I bought several sensors to try and find the best ones, and now like a man with two watches I'm never sure what the actual time is.

    - **ahaucnx** · [2023-07-29 21:05 UTC](https://news.ycombinator.com/item?id=36924582)
      Most of the times the sensor modules are actually pretty accurate but the heating up of the enclosure e.g. from heat radiated by the MCU creates the issues.
      In our indoor monitor it took us several months to get the airflow through the enclosure right so that the temperature and humidity sensors are very close to ambient. ^c36924582

      - **Havoc** · [2023-07-30 08:11 UTC](https://news.ycombinator.com/item?id=36928990)
        Yep. Recently superglued a temp ensor straight onto the back of an ESP32. Seemed like it would be ok given two pcbs with low thermal conductivity in between. ^c36928990

        ...5 degrees diff. Damnit.

      - **RobotToaster** · [2023-07-29 22:12 UTC](https://news.ycombinator.com/item?id=36925247)
        My Xiaomi one has exactly that problem. ^c36925247

  - **PeterStuer** · [2023-07-30 09:10 UTC](https://news.ycombinator.com/item?id=36929326)
    The Sensorcommunity (formerly luftdaten project) is very popular in Europe with over 10k sites active. It seems very similar to your approach (oss for both hardware and software). ^c36929326

    How does your approach differ from theirs? Will both interoperate?

    [https://sensor.community/en/](<https://sensor.community/en/>)

  - **dano** · [2023-07-29 23:12 UTC](https://news.ycombinator.com/item?id=36925804)
    A battery backed solar powered unit would be ideal for installation where power is not readily available. Scheduled WiFi or the addition of LoRa would also be a benefit. Nice project. ^c36925804

    - **T3OU-736** · [2023-07-30 01:17 UTC](https://news.ycombinator.com/item?id=36926688)
      I am planning to put the AirGradient (not sure which model yet) into the yet-to-be-built van with a camping setup. Powering it independent of the van's electrical system is a consideration. ^c36926688

    - **weinzierl** · [2023-07-30 05:14 UTC](https://news.ycombinator.com/item?id=36928046)
      Came here to ask that: Any chance for battery powered LoRaWAN version? ^c36928046

  - **kingsloi** · [2023-07-29 19:38 UTC](https://news.ycombinator.com/item?id=36923746)
    Awesome work! Do you have any plans to add/track gas pollutants? ^c36923746

    I run a similar open source app specifically for my little community in Gary, IN [https://millerbeach.community](<https://millerbeach.community>) and run a RAMP monitor provided by a local company Sensit Technologies, and a PurpleAir II and have about \~4 years worth of data in 15 min intervals. I've been meaning to swap out the PurpleAir with another, but I'll swap it out with this instead!

    - **ahaucnx** · [2023-07-29 19:41 UTC](https://news.ycombinator.com/item?id=36923789)
      We started testing electrochemical NO and NO2 sensors from Alpha Sense in our lab and are in the early stages to design a unit that would also measure these gases but we are many months away to have something in the market. ^c36923789

      - **KirillPanov** · [2023-07-30 00:55 UTC](https://news.ycombinator.com/item?id=36926547)
        The EPA limit for NO2 is 100ppb; have you found a sensor that can reliably report levels near that threshhold for less than \$500?  I haven't.  Also the ones that don't require frequent recalibration seemed to be even more expensive. ^c36926547

      - **declan\_roberts** · [2023-07-29 21:53 UTC](https://news.ycombinator.com/item?id=36925084)
        I can’t wait for this, especially with how often gas stoves are in the news lately. ^c36925084

  - **wodenokoto** · [2023-07-29 19:38 UTC](https://news.ycombinator.com/item?id=36923744)
    I think the website is very unclear about what you get, other than part names. What can the pro do that the normal can't do? Can I connect the TVOC to the non-pro? ^c36923744

    - **ahaucnx** · [2023-07-29 19:44 UTC](https://news.ycombinator.com/item?id=36923820)
      The TVOC module is only for the PRO indoor kits. The BASIC kit does not have space for the TVOC module. ^c36923820

      The PRO comes with a nice plastic enclosure, has a larger display and due to its larger size measures temperature and humidity more accurately (since there is more space, the temperature sensor has more distance to active components that heat up).

  - **cvwright** · [2023-07-29 20:59 UTC](https://news.ycombinator.com/item?id=36924508)
    This is random but I’d love to hear more about what’s involved in designing an enclosure and getting it manufactured at scale. ^c36924508

    - **ahaucnx** · [2023-07-29 21:07 UTC](https://news.ycombinator.com/item?id=36924613)
      The tooling for the plastic enclosure was quite complex and time consuming. If there is interest I can write a blog post about it. ^c36924613

      - **smokelegend** · [2023-07-29 22:39 UTC](https://news.ycombinator.com/item?id=36925524)
        That would be a interesting topic! ^c36925524

        If you write it, people will read it!

        I am one of those many people who will read it.

        "Sharing is caring"

    - **starky** · [2023-07-30 17:13 UTC](https://news.ycombinator.com/item?id=36933438)
      In general with injection molded parts the process has a few steps: ^c36933438

      1\. Design

      Starting from a set of requirements and what has to go into the enclosure you start working on the design. Here you are often working with other teams that influence the design. These could be other mechanical designers working on interior components, electrical designers working on PCBAs, industrial designers that want to make the exterior aesthetically pleasing and nice to interact with.

      The parts is designed with many factors in mind. What material will you be using? How does the part take into account good injection molding design practices (consistent wall thickness, avoiding undercuts, drafts to enable release from the mold, etc.)? How do the parts mechanically fit together? Normally you will be making prototypes at this point (e.g. 3D prints).

      Once you are happy with the design you create drawings and send a 3D database and the drawing to vendors for quote.

      2\. Design For Manufacture (DFM)

      Once you get the quotes back and choose a vendor you start the DFM process with your supplier. Their tooling engineers take a look at your design and provide a document with their feedback telling you where your design needs changes in order to be manufacturable. Part of this is running the part through simulations where they simulate how the plastic fills the mold to identify potential issues. You go back and forth until both parties are satisfied with the design before giving approval to start tooling.

      3\. Samples/Testing

      About 6-8 weeks later the vendor has finished the tool and done some tooling trials to dial in their process before sending you the first off tool (T0/FOT) samples. At this point the parts are generally not textured and may have some defects. You inspect the parts and provide feedback about what needs to be improved. At the same time the parts will be tested to see if there are any design issues, if something needs to be changed there you issue the vendor a tool mod report and they quote the costs to make the changes in the tool before sending updated samples for inspection/testing (usually called T1, T2, etc.). Once you are satisfied you have the vendor send the tool for texturing and get samples that are hopefully the final design and appearance.

      4\. Production

      Once the design is done approval is given to start buying the parts in high volumes for production.

  - **CommanderData** · [2023-07-29 20:10 UTC](https://news.ycombinator.com/item?id=36924049)
    I'm struggling to see the benefit of your product. Apart from the outdoor element. You can buy a 4 in 1 air monitor from Amazon for half the price (Co2, PM, Temp and Humidity) i.e. [https://www.amazon.co.uk/Indoor-Air-Quality-Monitor-Multifun...](<https://www.amazon.co.uk/Indoor-Air-Quality-Monitor-Multifunctional/dp/B0C7D2PPCY>) ^c36924049

    There are others with 6 in 1 with app control for less.

    Aren't there other sensors that would be more useful providing better insights on pollutants and health you could provide at a premium that these cheaper monitors can't.

    - **ahaucnx** · [2023-07-29 20:23 UTC](https://news.ycombinator.com/item?id=36924178)
      We use high quality sensor modules like e.g. the SenseAir S8 NDIR CO2 sensor that is made in Sweden and also Sensirion modules from Switzerland. These are much more expensive than less accurate sensor modules that you find in many other monitors. ^c36924178

    - **aequitas** · [2023-07-30 06:50 UTC](https://news.ycombinator.com/item?id=36928552)
      This is the cheapest option I found that would do MQTT or allow me to include my own HTTP endpoint for scraping Prometheus metrics over WiFi. ^c36928552

    - **ted\_dunning** · [2023-07-30 01:17 UTC](https://news.ycombinator.com/item?id=36926692)
      The sensor quality and the open source nature make a lot of difference there. ^c36926692

  - **iampivot** · [2023-07-30 15:20 UTC](https://news.ycombinator.com/item?id=36932092)
    Built one of the Airgradient Pro a few weeks ago, it works a threat! The bundled usb-c cable didn't work though. ^c36932092

    - **ahaucnx** · [2023-07-30 16:08 UTC](https://news.ycombinator.com/item?id=36932695)
      This is interesting. Can you please contact our support I would like to learn more about the failed cable. Thanks! ^c36932695

  - **mplewis** · [2023-07-30 08:08 UTC](https://news.ycombinator.com/item?id=36928973)
    Will it be possible to get a DIY kit for the outdoor monitor? I would be interested in 3D printing my own case at home. ^c36928973

    - **ahaucnx** · [2023-07-30 08:45 UTC](https://news.ycombinator.com/item?id=36929196)
      Yes should be possible. Please contact us via our contact form on the website. ^c36929196

  - **chsreekar** · [2023-07-29 19:24 UTC](https://news.ycombinator.com/item?id=36923602)
    Do you have an indoor version? ^c36923602

    - **ahaucnx** · [2023-07-29 19:29 UTC](https://news.ycombinator.com/item?id=36923652)
      Yes, we also have a popular open-hardware, open-source indoor air quality monitor that measures CO2, PM, Temperature and Humidity. You can also get an optional TVOC module that can measure chemicals and NOx. ^c36923652

      This version we currently only sell as a pre-soldered kit \[1\] but it is very easy to assemble (no need to solder anything) and you just need to plug a few modules together and close the enclosure with a few screws.

      \[1\] [https://www.airgradient.com/kits/](<https://www.airgradient.com/kits/>)

    - **ted\_dunning** · [2023-07-30 01:17 UTC](https://news.ycombinator.com/item?id=36926685)
      Their indoor version came first. I use several of them in my house and love them. ^c36926685

      I particularly love the open source nature of them that allows me to redirect their data reporting to my own homebrew data systems.

      About to buy some more of them, in fact.

- **zerof1l** · [2023-07-29 20:37 UTC](https://news.ycombinator.com/item?id=36924292)
  I don't see any benefit in this product having two identical sensors side by side. Based on the datasheet, the reading between sensors is quite consistent, meaning that there's no improvement in accuracy. What would be better is to have two different sensors, one of which actually counts PM 10.0. ^c36924292

  A little-known fact about these air quality sensors is that they don't actually measure three different particle sizes, they typically measure the smallest one and then return some statistically determined value for the larger ones.

  \[1\] [https://www.digikey.jp/htmldatasheets/production/2903006/0/0...](<https://www.digikey.jp/htmldatasheets/production/2903006/0/0/1/pms5003-series-manual.html>)

  - **ahaucnx** · [2023-07-29 20:44 UTC](https://news.ycombinator.com/item?id=36924363)
    There are two main advantages of having two sensors: ^c36924363

    a) Data quality: You can detect if one sensor fails as the two readings will start to deviate and then replace the faulty one

    b) Extend the life of the monitor: The PM sensors with the laser and optics have a limited life. By having two inside, you can alternate the measurement and put them in sleep mode inbetween. Thus extending the life of the monitor.

    - **cyberax** · [2023-07-29 20:54 UTC](https://news.ycombinator.com/item?id=36924455)
      Just a note: can you stagger the sensor time a bit unevenly? ^c36924455

      Instead of 50\%/50\% time split, can you do something like 40\%/60\%? This reduces the risk of both sensors failing at once because they have approximately the same duty time.

      - **jeffnappi** · [2023-07-29 22:05 UTC](https://news.ycombinator.com/item?id=36925180)
        Considering it is open source, you could do this :) ^c36925180

        - **cyberax** · [2023-07-30 07:52 UTC](https://news.ycombinator.com/item?id=36928867)
          I've just ordered a device, we'll see. ^c36928867

    - **codetrotter** · [2023-07-29 23:40 UTC](https://news.ycombinator.com/item?id=36926019)
      \> You can detect if one sensor fails as the two readings will start to deviate and then replace the faulty one ^c36926019

      But how do you know which one is the faulty one?

      - **ted\_dunning** · [2023-07-30 01:20 UTC](https://news.ycombinator.com/item?id=36926710)
        The failure modes are commonly fairly apparent. One sensor will go to a static low value and the other will show normal variability. ^c36926710

        In the theoretical limit of all mathematically possible failure modes and all possible environmental conditions, this would be impossible of course. But we live in a fairly predictable environment and the nature of the failures is not unlimited. As such, it is pragmatically pretty easy to see the difference.

    - **unknown** · [2023-07-29 22:41 UTC](https://news.ycombinator.com/item?id=36925549)
      [deleted] ^c36925549

  - **trailbits** · [2023-07-29 23:08 UTC](https://news.ycombinator.com/item?id=36925759)
    My outside sensors sometimes get contaminated from pieces of spider webs. It can be really hard to distinguish this from otherwise dirty air in a single sensor system, but when you have two you know something is wrong with one of them. A quick clean with the vacuum and both agree again. ^c36925759

- **traceroute66** · [2023-07-29 19:31 UTC](https://news.ycombinator.com/item?id=36923675)
  Time for the usual reminder that there is a search function on the bottom of every single YC page. ^c36923675

  Air gradient has been extensively discussed here multiple times already.

  - **frognumber** · [2023-07-29 21:38 UTC](https://news.ycombinator.com/item?id=36924930)
    I don't mind the repost. It's doing good work. It's good to be reminded of it, and it's a slightly different thing each time. I'll buy it when it's ready for prime time. ^c36924930

    The founder reads this.

    Founder: What's held me back from buying this is a lack of github links and instructions. EVERY place you say "open source" should link to the repo. The repo should have CLEAR instructions for how to hack this.

    There's a lot of copy like "We provide detailed instructions and videos" but NO hyperlink to said detailed instructions or videos. Any place you mention specs should link to ACTUAL specs. What's your BOM? What microcontroller are you using? Do I rewrite the firmware in Python? Rust? MakeCode? Etc.

    Those are the tires I want to kick. If my child can program this in MakeCode and it's designed for tinkering, it's a no-brainer. If it's on github, and easy to set up to work from my desktop, it's reasonable. If it involves setting up docker containers and proprietary environments for hacking C code, it's not as obvious a buy. If I can't figure out how to get started in 30 seconds, I assume it's the last one. I have a lot of projects around the house I wish I'd done, and I'm not buying more until a few of those finish.

    Also, I will never pay for your service. The whole point of open everything is I control my data.

    The other piece I'd like is a dirt-cheap set of temperature / humidity tools. I bought an 8-channel weather station, so I can monitor temperature indoors and in each room. I'd love to switch to something more open.

    Again, a lot of this comes down to how easy it is to get started. If I can make dashboards in 5 minutes with numpy / plotly / pylab / etc., I'm delighted. If I can't, but it's not bad, I'm grumpier. etc.

    So in conclusion, I'd do user studies and think-aloud protocols with customers.

    - **ahaucnx** · [2023-07-30 00:16 UTC](https://news.ycombinator.com/item?id=36926291)
      Thanks, this is great feedback and we definitely lack these links in that new copy. I will add them soon. In the meantime: ^c36926291

      Build instructions: [https://www.airgradient.com/open-airgradient/instructions/di...](<https://www.airgradient.com/open-airgradient/instructions/diy-open-air-presoldered-v11/>)

      BoM, schematics etc: [https://www.airgradient.com/open-airgradient/instructions/di...](<https://www.airgradient.com/open-airgradient/instructions/diy-open-air-documentation-v11/>)

    - **ted\_dunning** · [2023-07-30 01:26 UTC](https://news.ycombinator.com/item?id=36926755)
      You sound like me. ^c36926755

      The supplier answers all your questions on their website (and as you can see, the founder is taking your suggestions)

      Also, their software is just as hackable as you seem to want. I was able to create my own dashboard in a very short time using numpy and plotly. I query my archive using duckdb.

  - **kayson** · [2023-07-29 20:04 UTC](https://news.ycombinator.com/item?id=36923992)
    The guy who runs air gradient posts his articles here pretty frequently. Not sure at what point, if any, it breaks the rules. It definitely feels a little spammy to me though. ^c36923992

    - **hutzlibu** · [2023-07-29 20:29 UTC](https://news.ycombinator.com/item?id=36924221)
      I think there is no rule limiting new links. If it gets voted up, it makes it. And reposting existing links is ok every 6 months or so (I think). ^c36924221

      - **dfc** · [2023-07-30 00:19 UTC](https://news.ycombinator.com/item?id=36926315)
        They reposted the "When paying more  does not get you more accuracy" link 4 times in 2 months. I don't mind occasional reposts but that seems a little much: ^c36926315

        [https://news.ycombinator.com/from?site\=airgradient.com](<https://news.ycombinator.com/from?site=airgradient.com>)

        - **ahaucnx** · [2023-07-30 01:07 UTC](https://news.ycombinator.com/item?id=36926612)
          Yes I agree on this one. ^c36926612

          I reposted it because I thought this could be quite interesting for the hn crowd. On the 4th time it got more than 200 comments. Since then I did not repost it again.

          - **dfc** · [2023-07-30 23:54 UTC](https://news.ycombinator.com/item?id=36937306)
            Would you have posted it again if  the fourth post did not receive 200 comments? ^c36937306

  - **triyambakam** · [2023-07-29 19:48 UTC](https://news.ycombinator.com/item?id=36923857)
    I appreciate when things come up again. Obviously enough people either haven't heard of it or want to talk about it again for it to be upgoated to the front page. ^c36923857

    - **traceroute66** · [2023-07-29 20:56 UTC](https://news.ycombinator.com/item?id=36924476)
      \> I appreciate when things come up again ^c36924476

      My own position on this is that there is difference.

      If, like today's post, we're talking about what in forum-slang would be a "bump" post, then as far as I'm concerned it has near-zero value. Its basically just attention seeking if we're being honest.

      Meanwhile if it's re-posting a link but in the context of a significant change, for example a new version with major new features, then obviously it's a different kettle of fish altogether.  That's obviously perfectly fine.

      - **ahaucnx** · [2023-07-29 21:01 UTC](https://news.ycombinator.com/item?id=36924533)
        This page about the monitor is brand new and contains quite a lot of information that has never been published/posted before, e.g. the exact specs of the monitor and explanations about the enclosure design. ^c36924533

  - **philshem** · [2023-07-29 20:38 UTC](https://news.ycombinator.com/item?id=36924305)
    \> …there is a search function on the bottom of every single YC page ^c36924305

    Weird, in all seriousness, I never noticed.

  - **declan\_roberts** · [2023-07-29 21:52 UTC](https://news.ycombinator.com/item?id=36925071)
    I don’t understand, is this a problem? ^c36925071

    There’s nothing new under the sun.

- **epaulson** · [2023-07-29 21:42 UTC](https://news.ycombinator.com/item?id=36924972)
  The EPA had some money from the recovery funding and then the inflation reduction act to do more air quality monitoring stations - the EPA gave out 132 awards around the country, my city got one and we're putting up 68 sensors around town (one in each census tract) - the program and the awardees are here, if you're interested in seeing if your city got one: ^c36924972

  [https://www.epa.gov/arp/arp-enhanced-air-quality-monitoring-...](<https://www.epa.gov/arp/arp-enhanced-air-quality-monitoring-communities-competitive-grant>)

  (My city is using QuantAQ sensors, which weren't cheap)

  - **mcny** · [2023-07-29 23:54 UTC](https://news.ycombinator.com/item?id=36926132)
    \> (My city is using QuantAQ sensors, which weren't cheap) ^c36926132

    will your data be publicly available in near real-time? 
    as far as I can tell, airnow.gov only has data from airports. 
    will you share this data with the epa somehow?

- **nathan\_f77** · [2023-07-30 02:32 UTC](https://news.ycombinator.com/item?id=36927226)
  This company is pretty awesome! I lived in Chiang Mai for a few years and the burning seasons were absolutely horrible. I will never live there again. I bought an air quality sensor from a makerspace in Chiang Mai, and I was a bit frustrated that they kept it closed source so I couldn't get the data into Home Assistant. ^c36927226

  I currently have TuYa TS0601 Zigbee air quality sensors in every room of my house. I don't think the data is very accurate, but I just use it to automatically turn on the rangehood fan when the PM25 spikes in the kitchen, and an extractor fan in the workshop. Also to monitor CO2 in the bedroom and our offices and turn on the nearby bathroom fans. So I use them more as a boolean sensor and don't really need precise measurements.

  I live in New Zealand and fortunately our outdoor air quality is very good all year. If I lived somewhere with frequent wildfires (e.g. Sydney or Melbourne), then I'd probably upgrade to the airgradient indoor sensors.

  New Zealand is small and we have a lot of problems (cost of living, housing crisis, low salaries, etc.) so we've been thinking about moving somewhere else, but I don't know if I can give up the clean air. It's actually a pretty nice place to live.

- **stickac** · [2023-07-29 20:04 UTC](https://news.ycombinator.com/item?id=36923985)
  Open-source is mentioned 10x on the website, but there is no link to the actual source. ^c36923985

  - **ahaucnx** · [2023-07-29 20:26 UTC](https://news.ycombinator.com/item?id=36924201)
    It is linked on the technical documentation \[1\]. ^c36924201

    \[1\] [https://www.airgradient.com/open-airgradient/instructions/di...](<https://www.airgradient.com/open-airgradient/instructions/diy-open-air-documentation-v11/>)

  - **unknown** · [2023-07-29 20:27 UTC](https://news.ycombinator.com/item?id=36924209)
    [deleted] ^c36924209

  - **ianlevesque** · [2023-07-29 20:46 UTC](https://news.ycombinator.com/item?id=36924375)
    I bought one recently (it’s great) and found the source here [https://github.com/airgradienthq/arduino](<https://github.com/airgradienthq/arduino>) ^c36924375

- **hlandau** · [2023-07-30 06:48 UTC](https://news.ycombinator.com/item?id=36928544)
  I always get surprised by how many sensor products offer temperature and humidity but not pressure, considering that combined MEMS temperature/humidity/pressure chips are available. Having a sensor which can do temperature/humidity/pressure as well as air quality/CO2 would definitely be of interest to me. ^c36928544

  - **ahaucnx** · [2023-07-30 07:08 UTC](https://news.ycombinator.com/item?id=36928631)
    When we started with the monitor development we looked at several temp/humidity sensors and some had pressure included. However after testing several of them we found out that the SHT series from Sensirion offers the best accuracy/calibration out of the factory. So we used them and I think they are also used in many other monitors. ^c36928631

  - **defrost** · [2023-07-30 06:53 UTC](https://news.ycombinator.com/item?id=36928569)
    Not just you. ^c36928569

    Doing geophysical air surveys back in the day we'd record distance to ground, temp, humidity, and air pressure in order to have a running estimated mass between craft and ground to correctly scale readings such as radiometric spectrums from ground decay which weaken with mass between source (ground) and detector (craft).

- **xvfLJfx9** · [2023-07-29 19:31 UTC](https://news.ycombinator.com/item?id=36923680)
  If the device worked with ZigBee, I would get it immediately. However, it seems to support only WiFi, which means if someone gains physical access to the AirQuality monitor (which isn't exactly difficult since it is placed outside), they can potentially extract the WiFi password and gain full access to my network. ^c36923680

  - **ahaucnx** · [2023-07-29 19:40 UTC](https://news.ycombinator.com/item?id=36923765)
    Yes that's a good point. ^c36923765

    It probably makes sense to put it on a separate WiFi network (or a guest network) if access to the monitor is possible for unauthorized persons.

    - **seanp2k2** · [2023-07-29 20:15 UTC](https://news.ycombinator.com/item?id=36924104)
      Definitely recommend a separate 2.4ghz N-mode only wifi with separate passphrase and client isolation on a different vlan with routing only out to the internet for all IoT stuff. ^c36924104

      - **hpb42** · [2023-07-29 21:40 UTC](https://news.ycombinator.com/item?id=36924955)
        I'm curious, why N-mode only? What is the issue with a/b/g? ^c36924955

  - **cyberax** · [2023-07-30 06:36 UTC](https://news.ycombinator.com/item?id=36928489)
    \> If the device worked with ZigBee, I would get it immediately. ^c36928489

    A huge problem with ZigBee is that it's not OpenSource-friendly. The tools are proprietary and devkits are pretty pricey.

  - **ted\_dunning** · [2023-07-30 01:27 UTC](https://news.ycombinator.com/item?id=36926773)
    I keep my sensors on a separate network. There's very little they can do. ^c36926773

- **mkskm** · [2023-07-29 22:40 UTC](https://news.ycombinator.com/item?id=36925537)
  Here's another one on Adafruit (more time intensive but includes a VOC sensor) [https://learn.adafruit.com/air-quality-sensor-silo-house](<https://learn.adafruit.com/air-quality-sensor-silo-house>) ^c36925537

- **KirillPanov** · [2023-07-30 00:50 UTC](https://news.ycombinator.com/item?id=36926518)
  WIRED DATA CONNECTION. ^c36926518

  It needs a wired data connection.  For crying out loud.  Don't screw this up like PurpleAir did.

  You already have a micro-usb (or maybe usb-c) plug for the power.  You're not adding an extra wire.

  The amount of nightmarish grief the wifi in purpleairs causes makes me want to scream.

  Even if you manage to magically fix all the reliability problems, it's a safety issue.  A town near me whose economy is supported by a paper mill hunted down the person who was running a purpleair and pressured their landlord into cancelling their lease.  The town then set up indoor stations at the school and library -- where they report on filtered, air-conditioned air.

  You can wardrive for these things using their MAC address.  They have to be outdoors.

  Stop it.

  - **playa1** · [2023-07-30 01:05 UTC](https://news.ycombinator.com/item?id=36926605)
    Power over Ethernet would be a nice option. ^c36926605

    Wouldn’t data over usb-c require a computer to drive it?

- **yosito** · [2023-07-30 07:29 UTC](https://news.ycombinator.com/item?id=36928744)
  I'm trying to order one of these for my home in Thailand in an area with poor air quality monitoring. On the website it looks like you ship to Thailand for just \$20. Is that really the case? ^c36928744

  - **ahaucnx** · [2023-07-30 08:57 UTC](https://news.ycombinator.com/item?id=36929271)
    We are based in Thailand :) and yes we try to keep international shipping costs low. ^c36929271

    - **yosito** · [2023-07-30 10:10 UTC](https://news.ycombinator.com/item?id=36929634)
      Great! I'll place an order soon! ^c36929634

  - **petemir** · [2023-07-30 08:04 UTC](https://news.ycombinator.com/item?id=36928945)
    And what about customs fees? I’m also interested buying from Europe/Switzerland. ^c36928945

    - **ahaucnx** · [2023-07-30 08:58 UTC](https://news.ycombinator.com/item?id=36929276)
      Most of the time people get not charged customs but I think Switzerland is one of the few countries that are relatively strict. ^c36929276

- **stevep001** · [2023-07-29 19:33 UTC](https://news.ycombinator.com/item?id=36923702)
  I'd be a buyer if you had an indoor unit with a radon sensor. ^c36923702

  - **cyberax** · [2023-07-29 20:47 UTC](https://news.ycombinator.com/item?id=36924393)
    Why would you want a radon sensor in a product that does constant monitoring? ^c36924393

    Radon concentration is not a transient state, and you need to measure it for a fairly long time to get a good idea of the true concentration.

    - **simondotau** · [2023-07-29 23:44 UTC](https://news.ycombinator.com/item?id=36926057)
      Doesn’t your second sentence adequately explain your first sentence? Something that does constant monitoring would surely be good at measuring for a “fairly long time”. ^c36926057

      - **cyberax** · [2023-07-30 00:22 UTC](https://news.ycombinator.com/item?id=36926338)
        I mean that you need to accumulate the readings for a long time because the specific activity is so low. ^c36926338

  - **ahaucnx** · [2023-07-29 19:37 UTC](https://news.ycombinator.com/item?id=36923740)
    We have looked into adding a radon sensor but it is very difficult to get an off-the-shelf radon module in the market that is reasonably priced. ^c36923740

    If any of you can recommend a module I would be very interested to hear.

    - **JumpCrisscross** · [2023-07-29 20:13 UTC](https://news.ycombinator.com/item?id=36924078)
      Repackaging these sensors might be a better play than an OTS procurement model. Lots of people are making pretty packages for commodity sensors. Few are developing new sensor packages. ^c36924078

- **declan\_roberts** · [2023-07-29 21:52 UTC](https://news.ycombinator.com/item?id=36925067)
  I’ve been running the open source “stop light” design for awhile. It works great but the internet is very flaky on the esp board. Not entirely sure why, but easy to disable internet and just use the colors. ^c36925067

  It helped me identify patterns, such as CO2 settling in my large living room.

  Knowing that the CO2 levels are healthy throughout the day really helps me feel better about living in a new sealed home.

- **Brosper** · [2023-07-29 20:19 UTC](https://news.ycombinator.com/item?id=36924144)
  I strongly recommend to not always trust everything because it's open source. Air Quality as all different weather ingredients are measure and there is a big difference how you measure. I am not advocate of any "pro" solution. I just want you to know to check many sources. ^c36924144

  - **ahaucnx** · [2023-07-29 20:28 UTC](https://news.ycombinator.com/item?id=36924214)
    Yes, I totally agree. This is why we do extensive research to ensure the accurateness and reliability of the monitor against reference instruments. You can read more about it on our research page \[1\]. ^c36924214

    \[1\] [https://www.airgradient.com/research/](<https://www.airgradient.com/research/>)

- **xnzakg** · [2023-07-29 20:10 UTC](https://news.ycombinator.com/item?id=36924050)
  How well does the USB-C cable (and the rest of the PCB!) hold up outdoors? Especially in areas with salt, like near a coast or a place where salt is used on the roads in winter? From what I understood the sensor isn't sealed? ^c36924050

  - **ahaucnx** · [2023-07-29 20:21 UTC](https://news.ycombinator.com/item?id=36924158)
    At the moment it is not sealed. We are currently looking into conformal coating options and will probably have this available in one of the next batches (we are currenly checking what coating our PCB assembler can do). ^c36924158

- **unrealp** · [2023-07-31 05:16 UTC](https://news.ycombinator.com/item?id=36939051)
  @dang - kindly note this frequently posted topic by same user every few weeks. Not sure if this is just for advertising. Since this is being pushed by founder there should be at least be showhn? ^c36939051

- **SJetKaran** · [2023-07-29 21:08 UTC](https://news.ycombinator.com/item?id=36924626)
  The indoor monitor looks really interesting! I bought a Aranet4 recently, so don't think I'll invest in another Air Quality monitor soon, but I'm interested in checking this device for next buy. ^c36924626

- **Surplus7421** · [2023-07-31 16:21 UTC](https://news.ycombinator.com/item?id=36944954)
  If there is no rule about posting the same product every few days/weeks from the same person who is also the owner of the product, there should be one. @dang ^c36944954

- **legulere** · [2023-07-30 09:03 UTC](https://news.ycombinator.com/item?id=36929298)
  Can it push data to [https://sensor.community/en/](<https://sensor.community/en/>) ? ^c36929298

  - **toomuchtodo** · [2023-07-30 20:53 UTC](https://news.ycombinator.com/item?id=36935839)
    How does that site compare to [https://openaq.org/](<https://openaq.org/>) ? ^c36935839

- **jhot** · [2023-07-29 20:00 UTC](https://news.ycombinator.com/item?id=36923963)
  One of the Plantowers in my purple air has died and the power supply is flaking out as well. Think I'll grab one of these as a replacement. ^c36923963

- **bozhark** · [2023-07-29 22:03 UTC](https://news.ycombinator.com/item?id=36925156)
  I’m excited, this is on the build list. ^c36925156

  All I need to add is moister meter and CO2 controller to be complete

- **majkinetor** · [2023-07-29 20:30 UTC](https://news.ycombinator.com/item?id=36924226)
  Can I get the data as CSV or similar for custom presentation, backup and analysis? ^c36924226

  - **ted\_dunning** · [2023-07-30 01:33 UTC](https://news.ycombinator.com/item?id=36926803)
    It is the work of a moment to adjust the source code to send your data to any server you like. The server can be as simple as a few lines of Python to catch the JSON data and archive it. ^c36926803

    The simplest format is to send JSON data like the system does anyway, just change the URL it sends to.  From there, you can accumulate the data and present it any way you like. I keep my historical data in parquet format on a Pi4. YMMV.

  - **ahaucnx** · [2023-07-29 20:31 UTC](https://news.ycombinator.com/item?id=36924247)
    If you use our data platform, you can easily export an csv file with all the data in our database.
    But since it is open source you can also easily adjust the firmware and send the data to another server. ^c36924247

