# [Low-cost open source device can measure air pollution anywhere](https://news.ycombinator.com/item?id=35186431)

Article: [https://news.mit.edu/2023/low-cost-device-can-measure-air-pollution-anywhere-0316](<https://news.mit.edu/2023/low-cost-device-can-measure-air-pollution-anywhere-0316>)

GavCo · 2023-03-16 18:44 UTC · 74 reported comments · archived 2026-11-08 12:49 UTC
Observation: 2026-11-08 12:48 UTC → 2026-11-08 12:49 UTC

## Comments

- **Karawebnetwork** · [2023-03-16 20:01 UTC](https://news.ycombinator.com/item?id=35187586)
  Link to project website: [https://senseable.mit.edu/flatburn/](<https://senseable.mit.edu/flatburn/>) ^c35187586

  Link to assembly guide: [https://github.com/MIT-Senseable-City-Lab/OSCS/blob/main/Bui...](<https://github.com/MIT-Senseable-City-Lab/OSCS/blob/main/Build/Handbook/Flatburn_%20Assembly%20Guide.pdf>)

  Link to bill of materials: [https://docs.google.com/spreadsheets/d/1-fR-0hTxHKbjaRf8DbH6...](<https://docs.google.com/spreadsheets/d/1-fR-0hTxHKbjaRf8DbH62WgUFVeNE4eUEsaAd-YdDYg/edit#gid=2089068555>)

  Naively searching for every lines of the bill of materials gives me around \$300, with a handful of items being around \$50 and everything else under \$5. I'm sure a hobbyist could find the parts for cheaper, especially things like individuals connectors that I found for around \$5. I've seen them go as low as \$0.25 when bulk purchased.

  Disclaimer: it's possible that some SKUs led me to the wrong products. I am not into electronics. I encourage you do to the same exercise before drawing conclusions.

  - **clnq** · [2023-03-16 22:14 UTC](https://news.ycombinator.com/item?id=35189558)
    Not to undermine the DIY aspect which could be fun, but it looks like you could buy an Atmotube for about half as much (if you take the research survey) — [https://ukstore.atmotube.com/](<https://ukstore.atmotube.com/>). Though it doesn't register noise levels. ^c35189558

    They can also build you an Atmocube which can measure noise and a few other things for \$200-\$500 based on what I found online.

    - **greggsy** · [2023-03-17 00:06 UTC](https://news.ycombinator.com/item?id=35190776)
      Not sure why it needs an acceleromete, gyro or gps, and the solar circuitry might not be required for all use cases.
      Seems a bit over engineered, unless they were gearing towards a roving platform your could put on the back of your bike, or a balloon. ^c35190776

      - **Johnny555** · [2023-03-17 01:47 UTC](https://news.ycombinator.com/item?id=35191797)
        *unless they were gearing towards a roving platform your could put on the back of your bike, or a balloon* ^c35191797

        Or a car, like the Flatburn device in the linked article?

        - **clnq** · [2023-03-17 02:18 UTC](https://news.ycombinator.com/item?id=35192062)
          But the air above some streets is quite polluted in terms of NOx and particulate matter, and the air above the open road is very clean. In the cities, the street pollution levels vary a lot based on time (peak, off-peak) and day (weekday, weekend, holiday, public event day). I wonder if there would be any useful signal left in the noise. ^c35192062

    - **Karawebnetwork** · [2023-03-17 13:30 UTC](https://news.ycombinator.com/item?id=35196822)
      Anecdotal, but my Atmotube v1 did not last very long after I was only a little rough with it (tied to a backpack). I wonder if the solution brought here might be more sturdy / easier to repair in the context of developing nations. ^c35196822

  - **unknown** · [2023-03-17 09:12 UTC](https://news.ycombinator.com/item?id=35194820)
    [deleted] ^c35194820

  - **JKCalhoun** · [2023-03-17 00:04 UTC](https://news.ycombinator.com/item?id=35190760)
    Perhaps some industrious person (looks around room) could put together a BOM on a site like Mouser to make it a little easier to order many of the parts. ^c35190760

  - **sacnoradhq** · [2023-03-17 02:06 UTC](https://news.ycombinator.com/item?id=35191966)
    Overly complicated and expensive. ^c35191966

- **grozzle** · [2023-03-16 19:43 UTC](https://news.ycombinator.com/item?id=35187283)
  It would be useful if headlines said "\~\$10", "sub \$100", "sub \$1000" et cetera, instead of vague terms like "low-cost". ^c35187283

  - **cinntaile** · [2023-03-16 19:57 UTC](https://news.ycombinator.com/item?id=35187518)
    According to the linked paper in the article it's \<2500usd. ^c35187518

    [https://doi.org/10.1016/j.atmosenv.2023.119692](<https://doi.org/10.1016/j.atmosenv.2023.119692>)

    - **cwkoss** · [2023-03-16 21:51 UTC](https://news.ycombinator.com/item?id=35189254)
      I wouldn't call that 'low cost' ^c35189254

      - **segmondy** · [2023-03-16 23:47 UTC](https://news.ycombinator.com/item?id=35190617)
        how much can you buy one for or build one for? ^c35190617

        - **SECProto** · [2023-03-17 00:21 UTC](https://news.ycombinator.com/item?id=35190925)
          \> how much can you buy one for or build one for? ^c35190925

          \$10: [https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor...](<https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor-60515911/>)

          presumably not quite feature-comparable, but the article and website are rather absent in report what exactly the "flatburn" is detecting - sounds like "fine particulate" (PM2.5? PM10?) and NO2

          - **henearkr** · [2023-03-17 09:16 UTC](https://news.ycombinator.com/item?id=35194853)
            There is no NO2 sensor in the BOM. ^c35194853

          - **ClumsyPilot** · [2023-03-17 01:10 UTC](https://news.ycombinator.com/item?id=35191389)
            This is like comparing apples and Orangutans ^c35191389

            they are that different

        - **malfist** · [2023-03-17 18:53 UTC](https://news.ycombinator.com/item?id=35201295)
          \$640: [https://shop.air-q.com/air-Q-pro-air-analyser-14-sensors](<https://shop.air-q.com/air-Q-pro-air-analyser-14-sensors>) ^c35201295

          Or if you're building yourself, \$35: [https://sensirion.com/products/catalog/SEN55](<https://sensirion.com/products/catalog/SEN55>)

          Both include NO sensors.

          - **henearkr** · [2023-03-18 03:40 UTC](https://news.ycombinator.com/item?id=35205817)
            The second link seems pretty cool, and cheap!! ^c35205817

            Have you experience playing with it?

            In particular, I wonder how usable it is with e.g. a Linux laptop.

            It looks like the device uses a I2C interface.

- **ahaucnx** · [2023-03-17 04:37 UTC](https://news.ycombinator.com/item?id=35193174)
  We at AirGradient maintain popular indoor and outdoor open source air quality monitoring projects \[1\] and gained quite a lot of experience on air quality measurement. ^c35193174

  The hard part of these projects is not connecting electronic modules and get some air quality data out of it but to ensure that the data is accurate and this is where I have some questions. The success of these kind of projects stands and falls with the trust that people have in the data it generates.

  1) The built uses the Sensirion SPS30 PM sensor. As per Sensirion assembly guideline the maximum allowed air flow around the sensor is one meter per second. This corresponds to 3.6 km/h or 2.2 m/h. A car normally travels a multitude of this speed. I did not see anywhere in the built instructions how they manage the airflow inside the enclosure to be within this limit. In my opinion detailed airflow simulations inside the enclosure are essential.

  2) Temperature and humidity has strong impacts on the accuracy of PM measurements and it is important that these are accounted for. This is already a challenge for stationary low cost sensors but having this sensor mounted on the roof of a car will probably give a wide vaiety of different heat exposures. I did not see how this is accounted for.

  3) I am not sure if there are large advantages with mobile sensors compared to a high density stationary network of low cost sensors. Air pollution, especially on roads fluctuates a lot with peak times. So a measurmenet taken at 8am at a busy junction might be quite different a few hours later. How long do you keep past measurements valid for a certain location?

  I applaud all open source projects in this space and it looks like a lot of effort went into this project so it would be great if above concerns could be addressed/clarified from somebody in the team.

  \[1\] [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>)

  \[2\] [https://sensirion.com/media/documents/7990F04A/616544B0/Sens...](<https://sensirion.com/media/documents/7990F04A/616544B0/Sensirion_Particulate_Matter_AppNotes_SPS30_Mechanical_Design_and_As.pdf>)

  - **stephen\_g** · [2023-03-17 09:16 UTC](https://news.ycombinator.com/item?id=35194849)
    Yeah, the idea of mounting them on top of vehicle seemed a bit strange to me too, given how the particulate sensors work. Perhaps they could use the GPS and just sample for a bit when the vehicle has been stopped for a few seconds? ^c35194849

    I didn't think of the temperature issue - that does seem like a tricky problem too...

  - **jrockway** · [2023-03-17 05:04 UTC](https://news.ycombinator.com/item?id=35193352)
    \> Temperature and humidity has strong impacts on the accuracy of PM measurements ^c35193352

    How do you guys accurately measure humidity electronically?

    - **ahaucnx** · [2023-03-17 05:38 UTC](https://news.ycombinator.com/item?id=35193568)
      We mostly use the Sensirion SHT temperature and humidity sensors that are quite accurate. ^c35193568

      - **jrockway** · [2023-03-17 18:55 UTC](https://news.ycombinator.com/item?id=35201318)
        Ah interesting.  I have a weather station that uses that chip (not sure if 40 or 45), and the instructions say to never expect great information from it until you calibrate it against a sling psychrometer.  (It is certainly not the worst humidity sensor I have.  The one in my humidifier is consistently 10\% off from the other sensors.  The BME280 seems to yield similar results to the SHT45.  But without a calibrated reference, I'm just guessing, and assumed that was the state of the art of electronic humidity sensing.  A man with two inaccurate watches that agree with each other is never on time, or something like that.) ^c35201318

- **AceJohnny2** · [2023-03-16 19:34 UTC](https://news.ycombinator.com/item?id=35187155)
  Usual disclaimer that MIT's PR dept is really effective (I've stopped paying attention them because of so much hype), and there's quite a chasm between a proof of concept and a mass-market device. ^c35187155

  - **alsodumb** · [2023-03-16 19:49 UTC](https://news.ycombinator.com/item?id=35187383)
    Yup, they are really good. ^c35187383

    The Open Agriculture fraud is a living example: [https://gizmodo.com/mit-built-a-theranos-for-plants-18379682...](<https://gizmodo.com/mit-built-a-theranos-for-plants-1837968240>)

    - **gumby** · [2023-03-16 20:41 UTC](https://news.ycombinator.com/item?id=35188215)
      That one was supercharged by the Media Lab's PR organ.  But even without that assistance, the regular MIT "news" office is head and shoulders above its peers in making the trivial appear transformational and the outstanding appear...boring. ^c35188215

      My favorite was a publicity piece about a new proof for the behavior of higher-order manifolds with some absurd justification as to why you should care, something like how it would revolutionize battery electrodes or something like that.

      PS: "living example" was a nice touch.

      - **alsodumb** · [2023-03-16 22:08 UTC](https://news.ycombinator.com/item?id=35189477)
        Hahaha I was worried no one’s gonna get my pun. ^c35189477

- **l1am0** · [2023-03-16 21:00 UTC](https://news.ycombinator.com/item?id=35188539)
  This feels like old news. Built such a thing for a german hacker initiative like 7years ago. Back then sub 50€ and still runs. ^c35188539

  Data available at luftdaten.info

  [https://sensor.community/de/sensors/airrohr/](<https://sensor.community/de/sensors/airrohr/>)

  - **MandieD** · [2023-03-16 22:23 UTC](https://news.ycombinator.com/item?id=35189668)
    We built those and got them running one evening at a Meetup in Erlangen - looks like they had to switch to a temperature/humidity sensor that requires soldering the pins on, because the ones we used back then came ready to plug in, not a soldering iron in sight. ^c35189668

  - **throwaway8451** · [2023-03-17 07:20 UTC](https://news.ycombinator.com/item?id=35194242)
    I can vouch for that. A friend built one of these and since it worked really well, so I and some others built five more last year. Make sure to put a piece of window screen over the openings of the tube to keep insects and spiders out. If you have enough dexterity, you can even hide the screen inside the opening of the tube to make it less unsightly. ^c35194242

  - **gsich** · [2023-03-17 04:52 UTC](https://news.ycombinator.com/item?id=35193286)
    I have the same sensor but I don't trust those values at all. Especially after a few years when the sensor has dirt suckes in. ^c35193286

    Not sure how to calibrate those. I didn't buy 3 of them to measure the accuracy.

    - **throwaway8451** · [2023-03-17 07:16 UTC](https://news.ycombinator.com/item?id=35194211)
      These measurement devices have a limited lifetime and I think it is really the intake of dust and dirt that limits how long they can be used. That's why they're not running continously but for some seconds every few minutes (because flowing air will carry dust much more easily). If it's clogged up with dust or dirt, it really might be at end of life. I keep the electronics and sensor of mine in a closed box if I am not operating it. ^c35194211

      - **gsich** · [2023-03-18 21:43 UTC](https://news.ycombinator.com/item?id=35213387)
        Yes. But I can't see that, the sensor will still output values regardless of being clogged up. Not sure if I can open the device without destroying it, haven't tried. The power runs all the time as long as the USB cable is connected, but it's only a Serial-USB converter. ^c35213387

- **photochemsyn** · [2023-03-16 20:55 UTC](https://news.ycombinator.com/item?id=35188455)
  This sounds highly implausible for anything other than very crude and not-very-useful measurements.  Quantifying air pollution is a fairly hard problem, chemically speaking.  The composition of particulate matter is highly diverse as it may arise from a wide variety of sources, i.e. agricultural, industrial, wildfires, diesel engines, etc.  Just looking at the particulate PM2.5/PM10, broadly speaking there's the organic carbon fraction and the inorganic metal fraction. The former is highly complex, e.g.: ^c35188455

  \> "The considerably increased chromatographic resolution in GC×GC \[gas chromatography\] allows separation of many UCM \[organic carbon\] compounds while the TOFMS \[mass spectrometer\] supplies mass spectral data of all separated compounds. However, the data sets are getting enormously complex. In a typical PM2.5 sample from Augsburg *more than 15,000 peaks can be detected*... "

  [https://www.sciencedirect.com/science/article/abs/pii/S00219...](<https://www.sciencedirect.com/science/article/abs/pii/S0021967303015498>)

  Some particulate matter may have a heavy metal fraction, some may not and that's also not easy to determine (but was a major factor in leaded gasoline pollution).  Here's a sample of the kind of work that has to be done to get reliable measurements:

  \> "...using quadrupole inductively coupled plasma – mass spectrometry (q-ICP-MS). We report improved measurements of key aerosol elements including Al, V, Cr, Fe, Ni, Cu, and Zn in airborne coarse particulate matter (PM10)... This technique was used to determine the elemental composition of over 150 PM10 samples collected from an industrialized region in Houston, TX."

  [https://www.sciencedirect.com/science/article/abs/pii/S00032...](<https://www.sciencedirect.com/science/article/abs/pii/S0003267010014522>)

  On top of that there's nitrogen oxides and PAN, ozone, etc.  The only relatively inexpensive recent innovations seem to be the use of drones to collect samples for lab analysis (would have been useful in East Palestine).

  Getting accurate measurements of all the species involved in air pollution requires a modern analytical lab packed with equipment that costs hundreds of thousands of dollars and highly trained technicians to operate.  The press release and snippets from the paper don't address such important details at all.

  - **ddulaney** · [2023-03-16 21:01 UTC](https://news.ycombinator.com/item?id=35188556)
    Most definitely it's hard to dig into the actual composition of air pollution. But "how much PM2.5 is in the air", while definitely crude, is still extremely useful. That said, decent sensors for PM concentration are already pretty cheap (\<\$100 for a module; \~\$100 for a full package), so unless the price is going way down it's unclear how useful this particular innovation is. ^c35188556

  - **B1FF\_PSUVM** · [2023-03-16 23:46 UTC](https://news.ycombinator.com/item?id=35190610)
    I spent some hours on Amazon and AliExpress looking at cheap (under 100 bucks) air quality devices, and all I found was junk that made up figures for most "measures", if you read carefully the buyer reviews. ^c35190610

    I suppose the cheap & good device does not exist, but the junk seems to be selling fairly well. The demand is there, but not the product, and this press release seems another way of cashing in ...

    - **stephen\_g** · [2023-03-17 09:03 UTC](https://news.ycombinator.com/item?id=35194764)
      Big Clive on YouTube has done some videos on devices like these - like a "CO₂ meter" that seemed to actually just contain a VOC sensor - while it was quite good at detecting things like alcohol vapour, it's just useless as an actual CO₂ sensor. ^c35194764

      I wouldn't trust anything from AliExpress or anything that's not a known quality brand on Amazon. I'm looking at maybe getting a Davis Instruments AirLink to (at different times) do both indoor and outdoor monitoring for PM1, 2.5 and 10, as well as temperature and humidity, but it's pretty pricy (a bit over AU\$300). There's also the new Ikea indoor monitoring device \[1\] coming out next month too, which should be a lot more affordable I think.

      1\. [https://about.ikea.com/en/newsroom/2023/02/14/ikea-launches-...](<https://about.ikea.com/en/newsroom/2023/02/14/ikea-launches-vindstyrka-a-smart-sensor-to-measure-indoor-air-quality>)

  - **ckocagil** · [2023-03-16 21:31 UTC](https://news.ycombinator.com/item?id=35188976)
    A lot of these cheap, portable sensors "cheat" in one way or another. E.g CO2 sensors that assume they'll be subject to open air once every few days, using that minimal CO2 value as a baseline. So while they give numbers which can be useful if the user is aware of its limitations, they're far from being analytical tools. ^c35188976

    In contrast PM is pretty easy to get right. Shine laser, count particles.

  - **Severian** · [2023-03-16 22:12 UTC](https://news.ycombinator.com/item?id=35189536)
    Not only that, but they are deployed on top of automobiles, where the air quality in the surrounding air is going to be worse to begin with. I understand the benefits of using GPS, but I don't see where they mention this being an issue. ^c35189536

    - **jve** · [2023-03-17 07:33 UTC](https://news.ycombinator.com/item?id=35194326)
      Well, it is approximately same height our nose is placed. ^c35194326

      - **whiplash451** · [2023-03-17 08:35 UTC](https://news.ycombinator.com/item?id=35194633)
        There might be a difference between the pollution in the middle of the driveway and the pollution just a few meters away on the sidewalk. ^c35194633

- **thewanderer1983** · [2023-03-16 23:06 UTC](https://news.ycombinator.com/item?id=35190208)
  For those wanting a cheaper version that is small and works great. I've been using this for a while at home. It integrates nicely with home assistant. ^c35190208

  [https://community.home-assistant.io/t/sniffer-air-quality-se...](<https://community.home-assistant.io/t/sniffer-air-quality-sensor-using-esp32-with-lcd-pmsa003-bme680/226870>)

  [https://github.com/kylemanna/sniffer](<https://github.com/kylemanna/sniffer>)

  - **alexeldeib** · [2023-03-16 23:35 UTC](https://news.ycombinator.com/item?id=35190498)
    Hadn't heard of that but built something similar by adapting tutorials from adafruit for their microcontrollers, lcds, air quality sensors, starting with [https://learn.adafruit.com/adafruit-trinkey-qt2040](<https://learn.adafruit.com/adafruit-trinkey-qt2040>) ^c35190498

- **jl6** · [2023-03-16 19:51 UTC](https://news.ycombinator.com/item?id=35187412)
  I don’t know if this is the device to do it, but the premise is solid: create awareness that air pollution is a real thing affecting specific areas in which  *you* are breathing right now, not just an abstract bad thing that may or may not be happening somewhere to someone. ^c35187412

  - **cactusplant7374** · [2023-03-16 20:38 UTC](https://news.ycombinator.com/item?id=35188186)
    I'm debating buying one for myself so I can judge whether air pollution is effecting my asthma. You can find AQI for a lot of cities but it appears the calculation often isn't done with local devices. Satellite imaging? ^c35188186

    - **x3iv130f** · [2023-03-16 23:14 UTC](https://news.ycombinator.com/item?id=35190285)
      For home use, you should aim for multiple sensors that can track temperature, humidity, CO2, VOC, and PM2.5. ^c35190285

      CO2 is important to track as high concentrations can impact sleep quality and critical thinking ability.

      VOCs is important to track as they are associated with asthma and allergic reactions.

      CO2 can only be removed by opening a window.

      Most VOCs come from household chemicals and are only removed by using lots and lots of charcoal filters as the HEPA filters in household air purifiers aren't able to capture it in significant amounts.

      - **stephen\_g** · [2023-03-17 09:11 UTC](https://news.ycombinator.com/item?id=35194815)
        CO₂ can also be removed with mechanical ventilation, of course. Preferably heat- or energy-recovery ventilation to pre-condition the outside air being brought in, so you're not just dumping the air you expended energy heating or cooling straight out! ^c35194815

      - **rnk** · [2023-03-17 02:01 UTC](https://news.ycombinator.com/item?id=35191924)
        I like that but I also want to measure carbon monoxide making into my house and propane or natural gas leaks. What sensor does that also? ^c35191924

        - **Eisenstein** · [2023-03-17 07:18 UTC](https://news.ycombinator.com/item?id=35194234)
          The problem is that carbon monoxide sensors degrade, so any sensor that incorporates one will have a limited life. ^c35194234

    - **callalex** · [2023-03-17 00:58 UTC](https://news.ycombinator.com/item?id=35191293)
      Your local community might already be contributing to the PurpleAir network. ^c35191293

- **gniv** · [2023-03-16 20:05 UTC](https://news.ycombinator.com/item?id=35187641)
  The key word -- which is missing from the PR title, but is in the paper title -- is "calibration". The novelty is there. Apparently this is a big problem due to varying humidity levels. ^c35187641

  - **Havoc** · [2023-03-16 20:08 UTC](https://news.ycombinator.com/item?id=35187700)
    Not just humidity - CO2 equivalent sensors are also quite fond of drifting ^c35187700

- **gnramires** · [2023-03-16 19:48 UTC](https://news.ycombinator.com/item?id=35187369)
  Can't find the air quality sensor on their bill of materials ^c35187369

  - **shrx** · [2023-03-16 20:03 UTC](https://news.ycombinator.com/item?id=35187617)
    The Readme file \[1\] on their GitHub repo contains this bill of materials: [https://docs.google.com/spreadsheets/d/1-fR-0hTxHKbjaRf8DbH6...](<https://docs.google.com/spreadsheets/d/1-fR-0hTxHKbjaRf8DbH62WgUFVeNE4eUEsaAd-YdDYg/edit#gid=2089068555>) ^c35187617

    This lists a "particle module", a temperature sensor and some other seemingly irrelevant sensors (GPS, accelerometer).

    \[1\] [https://github.com/MIT-Senseable-City-Lab/OSCS/tree/main/Bui...](<https://github.com/MIT-Senseable-City-Lab/OSCS/tree/main/Build/Hardware/Hardware%20schematics>)

    edit: looks like the "particle module" is just a LTE/BT communication module, so really there don't seem to be any environmental sensors other than for temperature.

    - **detaro** · [2023-03-16 20:21 UTC](https://news.ycombinator.com/item?id=35187891)
      You are only looking at the list for the main board, the air quality sensor carrier is the second sheet of the doc. ^c35187891

      - **adolph** · [2023-03-16 22:11 UTC](https://news.ycombinator.com/item?id=35189517)
        It only includes a particulate matter sensor and "Analogue Front End (AFE) Alphasense A4 Air Quality Gas Sensors" but not the sensors to use. ^c35189517

      - **gnramires** · [2023-03-16 20:26 UTC](https://news.ycombinator.com/item?id=35187986)
        Thanks! ^c35187986

  - **e44858** · [2023-03-16 21:47 UTC](https://news.ycombinator.com/item?id=35189199)
    The particulate sensor is Sensirion SPS30, mentioned on the AQ Ext Board tab in the spreadsheet. ^c35189199

  - **ivarvong** · [2023-03-16 20:05 UTC](https://news.ycombinator.com/item?id=35187638)
    There's a mention of the SEN5X here: [https://github.com/MIT-Senseable-City-Lab/OSCS/blob/main/Bui...](<https://github.com/MIT-Senseable-City-Lab/OSCS/blob/main/Build/Hardware/Hardware%20schematics/Flatburn-sensor-board.pdf>) ^c35187638

    - **antoniuschan99** · [2023-03-16 20:37 UTC](https://news.ycombinator.com/item?id=35188164)
      I also see an alphasense afe, and bme280 ^c35188164

- **ck2** · [2023-03-17 02:42 UTC](https://news.ycombinator.com/item?id=35192264)
  IKEA hack ^c35192264

  [https://style.oversubstance.net/2021/08/diy-use-an-ikea-vind...](<https://style.oversubstance.net/2021/08/diy-use-an-ikea-vindriktning-air-quality-sensor-in-home-assistant-with-esphome/>)

  and of course previously on HN, airgradient DIY

  [https://news.ycombinator.com/item?id\=27124671](<https://news.ycombinator.com/item?id=27124671>)

  The more the better. Maybe one day built into every smoke detector.

  Maybe in a decade built into your phone. Another decade in your watch.

- **louison11** · [2023-03-17 00:21 UTC](https://news.ycombinator.com/item?id=35190931)
  This is a DIY open source air quality monitor starting from \$67, a lot cheaper than what the article mentions: [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>) ^c35190931

  Been geeking out on AQ (air quality) lately and it’s fascinating. Market is very messy though. Few options with huge price discrepancies. Ultimately it looks like the sensors inside the fancy \$300+ monitors cost a few dollars to acquire.

- **ggm** · [2023-03-16 23:04 UTC](https://news.ycombinator.com/item?id=35190180)
  Large scale data collection like this is good stuff. Sure, it can look like data for data's sake, but the downstream modelling from streetscape PM2/2.5 distribution into how it gets into people is there. ^c35190180

  NO levels need to be collected alongside PM2 and CO/CO2. That stuff is really bad for you.

  Insane amounts of inner-city schools without Air conditioning depend on open windows, kids sitting inside all-day next to busy streetscapes with diesel trucks roaring by. We know what this does to people.

  - **WWLink** · [2023-03-16 23:12 UTC](https://news.ycombinator.com/item?id=35190271)
    \> Insane amounts of inner-city schools without Air conditioning depend on open windows, kids sitting inside all-day next to busy streetscapes with diesel trucks roaring by. We know what this does to people. ^c35190271

    The surburbian schools I went to as a kid didn't have air conditioning, just a line of windows in the back of the room that were always open during the spring & summer, and a line of windows in the front near the ceiling, that were also open on hot days.

    AFAIK most of those schools were remodeled in the 2000s. They added air conditioning and nobody opens the windows anymore. That's great on a hot day, but man I really liked the fresh air on days with nice weather.

    - **ggm** · [2023-03-16 23:15 UTC](https://news.ycombinator.com/item?id=35190301)
      My son's school was built in the inner city Brisbane streetscape in the 1920s in a time of low car density. Once we vehicled up, it was sitting between two day long constant flows of cars, buses and trucks. I believe it was also the first public school in Brisbane south of the tropics to get air-conditioning (Qld used to manage the economics of the problem by defining a climate boundary to limit the cost) ^c35190301

      I get that "fresh air is best" and we kind-of also got that in covid times, its important to replace the air in a closed space. I like fresh air too. The problem is, what "fresh" is.

      If you sit at a window above the garbage bins, for the first 10-20 minutes you know what people had for dinner. After your nose shuts down you tune it out,  but those particles didn't stop winging it from the prawn heads into your breathing tract. We can't easily tell we're breathing in diesel particulate matter and like, unless you happen to walk by an airport at the right time to get a whiff from a passing jet,  but the fine matter is there, smelt or not.

      I sometimes think that wheezy asthmatic non-sports kid down the back of the class is the canary in the coal-mine: if they're having a bad day, actually everyone in that room might be.

      For the first year of my new Apt, every time we came back in from shopping we got a whiff of a lovely "new house smell" -the complex VOCs include the formaldehyde in the construction materials out-gassing. That stuff isn't good for you: [https://en.wikipedia.org/wiki/New\_car\_smell](<https://en.wikipedia.org/wiki/New_car_smell>)

- **dariosalvi78** · [2023-03-16 20:17 UTC](https://news.ycombinator.com/item?id=35187843)
  I had a similar DIY project, also using some Alphasense sensors, + some cheaper metaloxide ones. It was somewhat promising, but it needs long-lasting colocation studies and, after I moved to Sweden, I lost any support from the local authorities and gave up.
  [https://bochovj.wordpress.com/tag/air-quality/](<https://bochovj.wordpress.com/tag/air-quality/>) ^c35187843

- **unknown** · [2023-03-16 23:40 UTC](https://news.ycombinator.com/item?id=35190543)
  [deleted] ^c35190543

- **uoaei** · [2023-03-16 19:57 UTC](https://news.ycombinator.com/item?id=35187527)
  Official repo: ^c35187527

  [https://github.com/MIT-Senseable-City-Lab/OSCS](<https://github.com/MIT-Senseable-City-Lab/OSCS>)

- **theaussiestew** · [2023-03-16 20:01 UTC](https://news.ycombinator.com/item?id=35187587)
  Impressive, I’ve been wanting to build a portable version of this for a while now. It would look like a smart band but integrate environmental sensors and the users would then be aware of how their environment is affecting them. They would also have the option of contributing their data to a collective dataset. ^c35187587

  - **simulator5g** · [2023-03-17 01:30 UTC](https://news.ycombinator.com/item?id=35191603)
    That would be a great feature for a smart watch. ^c35191603

- **henearkr** · [2023-03-17 04:15 UTC](https://news.ycombinator.com/item?id=35193032)
  They mentioned a NO2 sensor in the article, but then I don't see it in the BOM. ^c35193032

  Was it only used for the calibration?

  If so, that would be a shame, as I am precisely looking for an inexpensive but reliable NO2 sensor device.

- **Rebelgecko** · [2023-03-16 21:44 UTC](https://news.ycombinator.com/item?id=35189153)
  How does this compare to something like an Airgradient, which you can put together for like \$50? More detail about what constitutes the PM2.5 or PMn particles you're measuring? ^c35189153

- **throwaway09432** · [2023-03-17 02:22 UTC](https://news.ycombinator.com/item?id=35192101)
  The production of this gadget will create more pollution. ^c35192101

- **sacnoradhq** · [2023-03-17 02:03 UTC](https://news.ycombinator.com/item?id=35191942)
  Uh.. you can just get an Arduino, LCD module, and a Plantower PMS5003 for \$35. ^c35191942

  That's what I did when the air was unbreathable with an AQI \~ 900.

- **Animats** · [2023-03-17 04:51 UTC](https://news.ycombinator.com/item?id=35193284)
  How does this differ from every other cheap air quality meter? ^c35193284

- **mistrial9** · [2023-03-16 20:46 UTC](https://news.ycombinator.com/item?id=35188301)
  there is an old man in Berkeley who has made very good money for more than thirty years, designing and selling these. No, he does not want to "open source" it (I tried). ^c35188301

