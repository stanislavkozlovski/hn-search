# [How to Determine the Error of an Air Quality Sensor?](https://news.ycombinator.com/item?id=40020402)

Article: [https://www.airgradient.com/blog/how-to-determine-error-of-sensor/](<https://www.airgradient.com/blog/how-to-determine-error-of-sensor/>)

ahaucnx · 2024-04-13 04:06 UTC · 47 reported comments · archived 2026-11-08 13:31 UTC
Observation: 2026-11-08 13:30 UTC → 2026-11-08 13:31 UTC

## Comments

- **Borealid** · [2024-04-14 09:07 UTC](https://news.ycombinator.com/item?id=40029816)
  When I read the HN article title, I knew which domain it'd be from before I saw it. ^c40029816

  I have several AirGradient devices and they've been great, no hassle at all with my own software instead of cloud-connected anything. I just wish there were a really good CO monitor that was also no-pain.

  Thanks for making a product that sells on its own merits instead of forcing ecosystem lock-in or trying to obscure what the thing is or does.

  - **ahaucnx** · [2024-04-14 12:18 UTC](https://news.ycombinator.com/item?id=40030607)
    Achim from AirGradient here. Thank you for your support. Very appreciated. ^c40030607

    We are currently working on bringing a lot more features into our open-source firmware \[1\], for example mDNS, local API etc. to make it even easier for non-cloud connectivity. We are also working on an offical home assistant integration.

    \[1\] [https://github.com/airgradienthq/arduino](<https://github.com/airgradienthq/arduino>)
    \[2\] [https://www.airgradient.com/documentation/local-server/](<https://www.airgradient.com/documentation/local-server/>)

    - **guiambros** · [2024-04-14 14:24 UTC](https://news.ycombinator.com/item?id=40031268)
      Thank you for everything you've done. I have a few AirGradients, and they are rock solid. ^c40031268

      Native Home Assistant integration would be fantastic. I already have mine connected using ESP32, and it works well, but setup is a bit finicky. Would be great to have something easily flashable.

  - **nicolaslem** · [2024-04-14 09:36 UTC](https://news.ycombinator.com/item?id=40029915)
    I have a Fibaro CO sensor on my z-wave network which is relatively low-pain and lock-in free. In my opinion CO monitors are a bit different from say CO2 or VOC in that they should really show 0 ppm at all times. If they don't you want them to alert you first and optionally record the data/send it somewhere. That's why I am fine with this device being treated more like a smoke detector than an IoT device. ^c40029915

  - **nsbk** · [2024-04-14 17:01 UTC](https://news.ycombinator.com/item?id=40032527)
    Same here! Props to Achim from AirGradient, we need more entrepreneurs like them. I built some of their DIY Air Quality Sensors open design boards for myself and was so happy with them that now I build and give them as gifts to people I care about. ^c40032527

    I integrate them in HomeAssistant via MQTT, see \[1\].

    More in line with the discussed article, I correct the humidity and temperature by adding/subtracting a fixed deviation that I calculated from observation, but I would like to implement something based on \[2\].

    \[1\]: [https://github.com/nsbk/airgradient\_mqtt](<https://github.com/nsbk/airgradient_mqtt>)

    \[2\]: [https://www.airgradient.com/blog/slr-temperature-example/](<https://www.airgradient.com/blog/slr-temperature-example/>)

  - **thebruce87m** · [2024-04-14 20:39 UTC](https://news.ycombinator.com/item?id=40034277)
    \> When I read the HN article title, I knew which domain it'd be from before I saw it. ^c40034277

    Well of course - they are they only company in this space that consistently post these articles to HN, and as the article says:

    \> This is an Ad for our Own Product

    - **ahaucnx** · [2024-04-14 20:54 UTC](https://news.ycombinator.com/item?id=40034389)
      Just to clarify.  We label the banner BELOW the article with this disclaimer. The article itself is purely written from a science perspective and not at all an advertisement. ^c40034389

  - **xandrius** · [2024-04-14 15:46 UTC](https://news.ycombinator.com/item?id=40031958)
    Same! I have one and been playing with it for a while but if they added CO reading + alarms, I would buy one device for me and one for each of my family members. ^c40031958

- **ck2** · [2024-04-14 15:50 UTC](https://news.ycombinator.com/item?id=40031992)
  I really love the spirit of AirGradient and their products. ^c40031992

  However they are shooting themselves in the marketing foot by not doing free datastorage for life for their users and therefore competing with PurpleAir which is the closed premium they are competing against.

  Google has chosen PurpleAir for their map overlay for air quality, it shouldn't be that exclusive but the reason why is the sheer number of installs.

  compare for your area:

  [https://map.purpleair.com/](<https://map.purpleair.com/>)

  vs the emptiness of

  [https://map.airgradient.com/](<https://map.airgradient.com/>)

  I keep telling them they need to just GIVE FOR FREE their units to all public universities in the United States with free data for life reporting, it will change their entire company's presence in the USA and maybe even make Google add them.

  Right now many universities, firehouses, stadiums, etc. etc. use WeatherStem for local weather recording/reporting. You know what WeatherStem does NOT have? Air Quality recording/reporting. Imagine if AirGradient gave their units to all the major WeatherStem sites that already have power and internet setup.

  look at the pulldown for the WeatherStem open-source data export and imagine AirGradient added for air quality to ALL those hundreds of universities

  export pulldown [https://forsyth.weatherstem.com/data](<https://forsyth.weatherstem.com/data>)

  breakout ([https://forsyth.weatherstem.com/](<https://forsyth.weatherstem.com/>))

- **riedel** · [2024-04-14 18:11 UTC](https://news.ycombinator.com/item?id=40033086)
  Our lab build and characterized one of the first low cost mobile PM sensing devices and worked with a major manufacturer of reference devices. I think the article is partially over simplifying. This is because also the reference devices do some tricks to derive mass concentration. Real mass concentration can only be measured at a low frequency by using actual filters that absorb the PM in the correct size category. Optical and beta attenuation devices are actually calibrated. The question is if the translation of absorption and count is actually so stable against mass. If you use other types of sensors like nephelometers you can for sure get different readings, however: are they really more wrong? Particularly if due to the measurement pricinciple a higher resolution is in the data. If you would want to measure mass concentration you would need to compare against real mass concentration and aggregate values. I am not sure if high resolution RSME is really helpful as a metric here. Constantly in place calibrated low cost sensors are often quite good. But this does not tell so much about their quality. In the end it is what you want to do with the sensor. For regulatorybpurposes (measuring e.g urban background) the placement of the sensor is often more important than the accuracy. If you want to discover relative and transient effects a well calibrated network of dense low-cost sensors might be a fit. In the end you cannot even easily translate exposure to harm, because it the material of your PM very likely will also matter (we are just assuming the typical mix in most cities when deriving limits) ^c40033086

  - **ahaucnx** · [2024-04-14 21:15 UTC](https://news.ycombinator.com/item?id=40034549)
    These are all excellent points that demonstrate the complexity of air quality measurement -especially for PM. ^c40034549

    We are planning many more articles like this one and hopefully step by step we can cover some of these aspects as well.

- **doodlebugging** · [2024-04-14 20:19 UTC](https://news.ycombinator.com/item?id=40034107)
  I appreciate the focus of the article and the explanations laid out for us. I would like to point out though that the two photos used as the "Less Polluted" and "More Polluted" examples may not fit the descriptions. ^c40034107

  Less Polluted shows a point in a city after a rain shower. The passage of a storm front tends to leave the air behind it more clean that it was before it arrived. That example makes the most sense.

  More Polluted does not make sense when you look at the photo since it obviously shows a storm front making it's way across a city, maybe the same one in the "Less Polluted" example. That storm is cleaning the air as it passes and the buildings in the foreground look like the storm has already passed. To me that means that the air from the photographer's vantage point should be clean already. It isn't possible to know whether you are looking east at dawn or west at sunset but either way that storm has passed, bringing clearer air to the city.

  A better example would be a photo of that same city on a cloudless summer day when the air is choked with smog and those who care are wishing for a nice storm like the one pictured to sweep through and clean it all up.

  - **ahaucnx** · [2024-04-14 21:08 UTC](https://news.ycombinator.com/item?id=40034493)
    Yes that's a good point. We will look for more suitable photos to illustrate this better - ideally from the same city. 
    We could probably use Chiang Mai, Thailand where our company of located and has wide annual swings of air quality. ^c40034493

  - **stavros** · [2024-04-14 21:04 UTC](https://news.ycombinator.com/item?id=40034468)
    I think they just thought the rain was smog. ^c40034468

- **seanmceligot** · [2024-04-14 15:13 UTC](https://news.ycombinator.com/item?id=40031686)
  I'm glad to see there's an alternative to Airthings. The problem with them is they should be calibrated at least every  year but they can't be, so they just deny that they ever go wrong and pretend the problem doesn't exist. ^c40031686

  - **dawnerd** · [2024-04-14 17:53 UTC](https://news.ycombinator.com/item?id=40032929)
    I’ve had mine for over a year and it displays basically the same values my other sensors show. Not sure it’s that big of a problem. ^c40032929

- **nox101** · [2024-04-14 18:02 UTC](https://news.ycombinator.com/item?id=40032993)
  I hope it's okay to ask this question. For you that have these sensors, what actions do you take based on what they tell you? Open more windows when you're cooking? Put on a mask when you vacuum? ^c40032993

  Just curious.

  I've dreamed of some future perfect portable sensor like a star trek tricorder or something that would tell me if the air in my office, or shopping center has bad stuff in the air (chemicals, viruses, mildew, etc...) to some point that I can print out a reading and tell my office the building is legally unsafe. I haven't seen anything like that.

  I have sensor at home but all it tells me is PPM and I rarely pay attention.

  - **jbm** · [2024-04-14 22:10 UTC](https://news.ycombinator.com/item?id=40034917)
    I live in Canada, where radon is an issue.  The item I got from Airwave gave me a half year of data that was close enough to the safety limit that I decided to add radon mitigation to my home.  I then lent it to a friend who decided to do the same. ^c40034917

    I have multiple CO2 meters in the house that helped me determine that there were no major issues with airflow, and led me to consider other ways to improve our sleep quality.  This was also kinda helpful for me during parties; I'm usually not thinking about opening the window during winter, but when the CO2 level passes 1200 or so, I'll usually open it a crack.

    - **gausswho** · [2024-04-15 14:15 UTC](https://news.ycombinator.com/item?id=40040816)
      What measurements from the Airgradient devices specifically indicate radon? I have both the outdoor and indoor one but struggle to get actionable evidence. ^c40040816

      - **jbm** · [2024-04-15 16:49 UTC](https://news.ycombinator.com/item?id=40042927)
        Ah, I have an Airthings Wave Plus (I thought it the parent was asking about air quality meters in general.). The information is in the app; I've never used an airgradient device. ^c40042927

  - **quickthrowman** · [2024-04-14 18:23 UTC](https://news.ycombinator.com/item?id=40033181)
    \> I hope it's okay to ask this question. For you that have these sensors, what actions do you take based on what they tell you? Open more windows when you're cooking? Put on a mask when you vacuum? ^c40033181

    I don’t get it either, there’s not much you can do with a residential AQI sensor without adding a bunch of other automation controls.

    Commercially, these are used in building automation to do things like turn on the exhaust fans and make up air units in a parking structure when the CO levels go up, or to open an outside air damper in an AHU to let more fresh air in if elevated CO2 levels are detected.

    I just don’t see the application for residential use. It’s just a PPM number, does anyone actually take action if the number gets too high? Anyone automate their actions?

    - **SECProto** · [2024-04-14 18:42 UTC](https://news.ycombinator.com/item?id=40033313)
      \> there’s not much you can do with a residential AQI sensor without adding a bunch of other automation controls. ^c40033313

      You don't need automation. I have a portable CO2 monitor (aranet4) and it gives me an indication of how effectively the air is being exchanged. I've learned that my desk location at home is ok during summer and winter, but when temperatures are moderate the furnace isn't running as much, and the CO2 will get quite high. I keep a window cracked when I work there and it's enough to bring it down to reasonable levels. I didnt know this information before getting it. Similar when I was visiting relatives over easter - the CO2 in the bedroom got up to 2500ppm wile I slept (old house, sealed tight but no forced air circulation). I opened the window for the rest of my stay.

      - **Klathmon** · [2024-04-14 20:59 UTC](https://news.ycombinator.com/item?id=40034419)
        I had a similar experience. I got a cheap CO2 sensor from AliExpress, I basically would open a window or the door to my office if it got over 1000 during the day. I don't consciously notice a difference, but it also measures pm2.5 levels and I was surprised at how high they get while cooking. ^c40034419

        Then for shits and giggles I brought it with me to the inlaws and after turning it on there was shocked the CO2 levels were 4300ppm!

        Suddenly the headaches they would get at home made sense, and they've started opening windows in the mornings to help circulate some air.

    - **Royce-CMR** · [2024-04-14 18:33 UTC](https://news.ycombinator.com/item?id=40033241)
      Super fast reply from someone else - Yes, I have a standing air filter unit. If PPM went up I’d kick it into max gear. ^c40033241

      (Now I have it running on very low continuously and it keeps PPM down)

      The unit is rated for spaces 2x my square footage so on max it makes a quick improvement.

      For CO2, minimize cooking / burning and kick on the air to attempt circulation. Worst case leave for a bit. (Used to be very sensitive to CO2 levels, it’s getting better).

  - **rinron** · [2024-04-14 18:49 UTC](https://news.ycombinator.com/item?id=40033371)
    It taught me that most bedrooms dont have enough air flow, it helped me figure out just how much i need the window open or not closing the door which improved my sleep.  Also helped me see the importance and notice the effect of having a air filter, and fine tune location and fan speed.  I find that air quality is something you get used to and dont realize the effect it has on you unless you pay attention and experiment.  its not something i pay attention to every day i could probably use it 1 week 2 times a year and have 90\% of the benefit.  That being said a lot of people probably live in better more well designed places with less issues than i have. ^c40033371

  - **billfor** · [2024-04-14 18:32 UTC](https://news.ycombinator.com/item?id=40033234)
    I have outdoor and indoor. For outdoor it was helpful for wildfires and knowing when to go outside. For indoors I sometimes pay attention to it. It gave me some surprising insights into cooking and the pollution it causes - so now I try to remember to turn on the hood vent all the time - even things like making waffles generate a surprising amount of pollution. ^c40033234

- **jddj** · [2024-04-14 09:15 UTC](https://news.ycombinator.com/item?id=40029842)
  \> Yet, you would probably go for the *right* sensor, true? That’s because this one has a lower relative error. ^c40029842

  If the author is about, I have a feeling this should read *left*?

  - **ahaucnx** · [2024-04-14 12:30 UTC](https://news.ycombinator.com/item?id=40030660)
    I believe you talk about the section about normalized RMSE (nRMSE). The nRMSE on the right side is 6\% and thus lower than the nRMSE on the left side with 66\%. The lower the nRMSE the better. So I believe the article is correct. ^c40030660

    However it's always important to not only look at one performance metric but a bundle, e.g. including R2 for the correlation to make a good judgement of a sensor quality.

    We covered some of the basics in an earlier article \[1\].

    \[1\] [https://www.airgradient.com/blog/sensor-performance-precisio...](<https://www.airgradient.com/blog/sensor-performance-precision-reproducibility-accuracy/>)

- **poulpy123** · [2024-04-15 06:55 UTC](https://news.ycombinator.com/item?id=40037697)
  I recently bought one of their monitor, and I'm pretty happy with it. It was the only one that provided CO2, PM2.5 and VOC at my price point.  They were also tested by the agency in charge of monitoring the air quality in Paris, so I can reasonably trust their monitors at the difference of most of the non pro ones. I only wish there was a possibility to store the data on a micro SD card. ^c40037697

- **m4x** · [2024-04-14 09:33 UTC](https://news.ycombinator.com/item?id=40029903)
  Based on the title, I was expecting this article to have instructions for calibrating an air quality sensor, rather than just explaining different error types. ^c40029903

  - **ahaucnx** · [2024-04-14 12:23 UTC](https://news.ycombinator.com/item?id=40030636)
    This post is part of a series of posts. We already wrote a few posts about sensor calibrations, e.g. how to develop a correction algorithm for temperature \[1\] or how to use R for making a linear regression \[2\]. ^c40030636

    In one of the next topics we will dive more into PM correction and the sensitivity to relative humidity.

    If you want to know more about the science of air quality monitoring, we are also running webinars that you can watch on our reserach page \[3\].

    \[1\] [https://www.airgradient.com/blog/slr-temperature-example/](<https://www.airgradient.com/blog/slr-temperature-example/>)

    \[2\] [https://www.airgradient.com/blog/using-r-for-sensor-correcti...](<https://www.airgradient.com/blog/using-r-for-sensor-correction/>)

    \[3\] [https://www.airgradient.com/research/](<https://www.airgradient.com/research/>)

  - **wezdog1** · [2024-04-14 12:36 UTC](https://news.ycombinator.com/item?id=40030681)
    It doesn't mention anything about calibrating ^c40030681

    - **seanmceligot** · [2024-04-14 15:15 UTC](https://news.ycombinator.com/item?id=40031704)
      I was looking for this too, "site:airgradient.com calibrate" brings a lot of results, so it seems like they support it,  but I haven't dug in yet. ^c40031704

      - **runjake** · [2024-04-14 16:19 UTC](https://news.ycombinator.com/item?id=40032211)
        See: [https://news.ycombinator.com/item?id\=40030636](<https://news.ycombinator.com/item?id=40030636>) ^c40032211

    - **m4x** · [2024-04-15 10:06 UTC](https://news.ycombinator.com/item?id=40038547)
      What you think the purpose of determining the error of an instrument is, if not to calibrate it? ^c40038547

- **Luc** · [2024-04-14 09:12 UTC](https://news.ycombinator.com/item?id=40029829)
  Ok, so you compare your sensor to a reference sensor. But... ^c40029829

  \> If you compare two reference instruments, they should ideally measure exactly the same, namely the true pollutant concentration. But they don’t: A study from the US-EPA co-located two commonly used reference instruments (Met One BAM-1020 and Teledyne API T640) and found that, at certain concentration ranges, they diverged by over 25\% from each other.

  - **honk** · [2024-04-14 16:55 UTC](https://news.ycombinator.com/item?id=40032499)
    This reference instrument variability is especially true of the BAM, which due to its measurement technology has a high "noise floor" at low concentrations, while remaining a fairly good measurement at high concentrations. I believe two identical BAMs next to each other can easily have more than 25\% disagreement at the lower end of the concentration range. ^c40032499

    The T640 also recently had its approved calibration algorithm(s) updated, to a new set which often reads about 7\% lower. What does that mean for T640 reference data collected in the past? I don't know, and AFAIK neither does the EPA really.

    All that to say that reference instruments are still instruments with limitations, even if from a regulatory perspective we treat them as "truth".

- **Havoc** · [2024-04-14 12:25 UTC](https://news.ycombinator.com/item?id=40030648)
  Have experimented with this too - the accuracy is less of a concern to me than the fact that PM sensors require airflow and most achieve that via shitty whiny tiny fans. bzzzzzz ^c40030648

  Closest "solution" I've found is the airsensors built into some airfilters. They seem to steal some of the main airflow rather than having a second fan. Obviously not quiet but at least fan size is decent so bit lower pitch

  As for other measurements - for temp/humidity/pressure...any sensor will do. CO2  - the SCD41 are best I've found, BME680 and BME688 are hot garbage.

  - **ahaucnx** · [2024-04-14 12:34 UTC](https://news.ycombinator.com/item?id=40030679)
    It really depenends on the PM sensors you use. For the Plantower 5003 we use in our monitors, you only hear a faint noise from the fan when you put it directly at your ear. However some other monitors need an extra fan in the enclosure and some of them can get noisy. ^c40030679

    For CO2, the Sensirion SCD41 is a good sensor which uses photo accoustic principle. We found NDIR sensors using light spectometrie to be a bit more accurate like the SenseAir S8. Price wise the two are quite similar.

    - **geerlingguy** · [2024-04-14 14:52 UTC](https://news.ycombinator.com/item?id=40031497)
      Can confirm, I have about 8 gradients deployed now, including one in my studio with 31 dBa noise floor, and I can only ever hear the Plantower's fan with my ear nearly touching the device. I've never heard it day to day. ^c40031497

  - **ploxiln** · [2024-04-14 17:18 UTC](https://news.ycombinator.com/item?id=40032645)
    The noisy fan really varies by device. My Air Graident Basic DIY makes very little noise. I have another device I got earlier, a "Lonicera" (some chinese brand) and it looks like it has an extremely similar Plantower PM sensor inside, which is what has the little fan ... but it is often way noiser and rattle-y, the fan is clearly somewhat malfunctioning. I've taken it mostly apart, but it didn't seem worth the effort to go the last mile to fix or replace it. ^c40032645

  - **beryilma** · [2024-04-14 17:30 UTC](https://news.ycombinator.com/item?id=40032728)
    \> BME680 and BME688 are hot garbage. ^c40032728

    I agree 100\%. What they measure (which is already very non-precise), only vaguely correlates with air quality and there are many factors that would throw off the readings.

    Reading from their reference manual, one can already see from all the complicated expressions (regression) and numerical factors that they tried too hard to come up with something that looks like an air quality metric.

  - **HankB99** · [2024-04-14 13:13 UTC](https://news.ycombinator.com/item?id=40030847)
    \> BME680 and BME688 are hot garbage. ^c40030847

    I've got a BME680 on a Raspberry Pi reporting the values it senses. I'm confused about how to interpret the air quality readings as far as what is good vs. what should be concerning. Is that what you mean by "hot garbage" or are you not satisfied with the accuracy readings themselves?

    - **Havoc** · [2024-04-14 20:41 UTC](https://news.ycombinator.com/item?id=40034295)
      The readings coming out of it are basically meaningless & only vaguely correlate with what's happening it the room ^c40034295

    - **beryilma** · [2024-04-14 18:18 UTC](https://news.ycombinator.com/item?id=40033144)
      They are just not accurate. 25\% variability is just not an acceptable level of accuracy. And their results are very dependant on temperature and humidity. ^c40033144

- **somat** · [2024-04-15 00:12 UTC](https://news.ycombinator.com/item?id=40035717)
  I have to admit I was a bit disappointed that the conclusion was effectively diff your sensor with a reference sensor, I was hoping it was more like "here is how to make your own reference measurement". ^c40035717

  Don't get me wrong it was a good article, I appreciate the math on how to make a meaningful diff.

  - **anikra** · [2024-04-15 10:51 UTC](https://news.ycombinator.com/item?id=40038827)
    Hi Anika from AirGradient here (the one who wrote the article). ^c40038827

    Unfortunatly, we still depend on reference instruments to figure out the performance of a sensor. But you can find reference stations that publish their air quality data online. 
    If you want to do you own reference experiment, check if you can find a closeby air quality station and compare your data with this one. But keep in mind that, if reference and monitor are a few (kilo)meters apart, the air pollution emissions in the surroundings will probably differ. So you might not be able to compare every peak and squiggle, but I would expect that you can see a general correlation if you compare a sufficient time period (at least a week).

