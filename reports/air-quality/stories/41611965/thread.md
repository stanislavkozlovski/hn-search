# [Infineon's CO2 Sensor Monitors Indoor Air Quality](https://news.ycombinator.com/item?id=41611965)

Article: [https://www.allaboutcircuits.com/news/infineons-co2-sensor-precisely-monitors-indoor-air-quality/](<https://www.allaboutcircuits.com/news/infineons-co2-sensor-precisely-monitors-indoor-air-quality/>)

WaitWaitWha · 2024-09-21 19:08 UTC · 83 reported comments · archived 2026-11-08 13:40 UTC
Observation: 2026-11-08 13:39 UTC → 2026-11-08 13:40 UTC

## Comments

- **ahaucnx** · [2024-09-22 01:06 UTC](https://news.ycombinator.com/item?id=41613827)
  We did some extensive testing of photo-acoustic and optical NDIR CO2 sensors indoors as well as outdoors and also in comparison to scientific reference instruments. ^c41613827

  I just updated the blog post that I wrote last year \[1\] with the specs of this new Infineon sensor and also our experiences with doing CO2 measurement outdoors.

  In summary we can say that under normal indoor conditions (e.g. small range of temperature, relative high range of CO2 etc.), the photo-acoustic NDIR sensors perform well.

  However, outdoors they significantly underperform optical NDIR sensors to the extent that they are barely usable. See for example this chart \[2\].

  It's hard to say why exactly they perform so poorly outdoors but I believe that they rely on quite complex internal algorithms that probably have been only developed with typical indoor conditions in mind and as soon as some parameters like temperature are out of the typical range, they significantly drop in their performance.

  Furthermore, we also detected that they are sensitive to interference from low frequency noise which could for example come from ventilation systems, refrigerators etc. This is not surprising as they rely on their internal microphone to do the photo-acoustic measurements.

  All of this and the rock-solid performance we see with optical NDIR sensors made us quite wary about the photo-acoustic sensors and not use them in our open-source hardware monitors. As I said, I believe they work quite well in general but because we saw also some really strange and unexpected behavior of these photo-acoustic sensors, I'd now always prefer optical NDIR sensors if possible.

  \[1\] [https://www.airgradient.com/blog/co2-sensors-photo-acoustic-...](<https://www.airgradient.com/blog/co2-sensors-photo-acoustic-vs-ndir-updated/>)

  \[2\] [https://www.airgradient.com/blog/co2-sensors-photo-acoustic-...](<https://www.airgradient.com/blog/co2-sensors-photo-acoustic-vs-ndir-updated/#outdoors>)

  - **wkat4242** · [2024-09-22 01:52 UTC](https://news.ycombinator.com/item?id=41614057)
    Interesting. But why would you monitor CO2 outdoors? Even the NDIR ones just return "400" when they detect outdoor air and use it as calibration. ^c41614057

    Though i believe you can turn off the auto calibration which is probably a good idea in busy city areas where I imagine outdoor CO2 is slightly higher than 400. And manually calibrate them with an actual known source.

    - **ahaucnx** · [2024-09-22 02:12 UTC](https://news.ycombinator.com/item?id=41614156)
      Outdoor CO2 levels can go up to 700-800ppm in rural areas due to plants creating CO2 \[1\]. I was initially surprised it's that high but it was verified with reference instruments. ^c41614156

      Why measure CO2 outdoors?

      We are able to detect emission sources pretty well now with our outdoor monitors \[2\] that have the SenseAir S8 NDIR sensor built in. You can see some real data in the blog post I wrote about launching our global CO2 map \[3\].

      So setting up a dense network of these sensors in a city would allow to measure if for example the introduction of low-emission zones or switching to electric buses etc. would work.

      Another use case is to check for leakage in underground CO2 storage facilities.

      All-in-all it's still experimental (to some extent) but we know the accuracy is there and we can see more and more use cases as outlined in my blog post. So we now work hard to get more and more of these sensors out there to get more data to identify additional use cases.

      \[1\] [https://www.airgradient.com/blog/performance-of-low-cost-co2...](<https://www.airgradient.com/blog/performance-of-low-cost-co2-sensors-outdoors/>)

      \[2\] [https://www.airgradient.com/outdoor/](<https://www.airgradient.com/outdoor/>)

      \[3\] [https://www.airgradient.com/blog/airgradient-global-co2-map/](<https://www.airgradient.com/blog/airgradient-global-co2-map/>)

      - **neilv** · [2024-09-22 13:29 UTC](https://news.ycombinator.com/item?id=41616935)
        \> *Outdoor CO2 levels can go up to 700-800ppm in rural areas due to plants creating CO2 \[1\].* ^c41616935

        We need to get those rural voters more oxygen, STAT!

        - **nroets** · [2024-09-22 17:34 UTC](https://news.ycombinator.com/item?id=41618542)
          Em, do you know that plants are actually a net source of oxygen ? And a sink of CO2 ? ^c41618542

          - **tedivm** · [2024-09-22 19:18 UTC](https://news.ycombinator.com/item?id=41619244)
            Net, sure, but it's actually really really complex when you look at point in time numbers. ^c41619244

            \> Carbon dioxide is not released during photosynthesis, but small amounts of that gas are emitted both day and night as a by-product of cellular respiration. It is worth noting that the majority of plants absorb carbon dioxide during the day for photosynthesis and do so in greater amounts than they release for cellular respiration.

            So depending on the time plants could easily be pushing out more CO2 than they are pulling it *at that time*, which could result in CO2 concentrations increasing during that time.

          - **Projectiboga** · [2024-09-22 21:32 UTC](https://news.ycombinator.com/item?id=41620263)
            Time dependent, plants give off O2 in the evening. The co2 is released by the micro organisms which are bacterial and fungal and breathe O2 just like us. ^c41620263

            - **stavros** · [2024-09-22 22:33 UTC](https://news.ycombinator.com/item?id=41620657)
              Plants are overall a sink of CO2, as it goes into building their mass. ^c41620657

        - **aaron695** · [2024-09-22 22:37 UTC](https://news.ycombinator.com/item?id=41620675)
          [flagged] ^c41620675

          \[dead\]

      - **darby\_nine** · [2024-09-22 06:52 UTC](https://news.ycombinator.com/item?id=41615109)
        Surely this refers to decomposition and not living plants. Your link doesn't appear to finger plants as the culprit at all. ^c41615109

        - **avianlyric** · [2024-09-22 07:44 UTC](https://news.ycombinator.com/item?id=41615343)
          Plants produce CO2 as well, photosynthesis is only used to produce sugars, normal respiration (I.e. sugars + O2 \= energy + CO2), is used by plants to consume those sugars. ^c41615343

          Only a plant cells containing chlorophyll and exposed to sunlight will photosynthesise. Notably at night there isn’t much sunlight, so normal respiration dominates a plants gas conversion processes, and results in them producing net CO2.

          Based on the graphs in the blog post, I assume GP is placing the CO2 production on plants because it the CO2 levels peak at night, then return to normal every morning.

          - **mschuster91** · [2024-09-22 08:47 UTC](https://news.ycombinator.com/item?id=41615636)
            Yep, I've noticed this as well with my cannabis grow tent. At an 18/6 lighting schedule, it's noticeable that CO2 grows up to 800ppm in the tent at the end of the fake-night cycle. ^c41615636

      - **specto** · [2024-09-22 16:56 UTC](https://news.ycombinator.com/item?id=41618261)
        It seems like ozone is the missing piece. The only ones that measure outdoor ozone are governments, and the numbers keep increasing. ^c41618261

        - **TeMPOraL** · [2024-09-22 21:20 UTC](https://news.ycombinator.com/item?id=41620180)
          Isn't the increasing numbers good here at this point? Or not at this altitude? ^c41620180

          - **RF\_Savage** · [2024-09-22 22:04 UTC](https://news.ycombinator.com/item?id=41620467)
            No it is not. Ozone is not good for breathing. ^c41620467

      - **Rebelgecko** · [2024-09-22 04:18 UTC](https://news.ycombinator.com/item?id=41614589)
        Who do you calibrate these CO2 sensors in areas where the background level is so high? ^c41614589

        - **ahaucnx** · [2024-09-22 05:12 UTC](https://news.ycombinator.com/item?id=41614770)
          Not sure what you mean with calibration here. Above is not so much about calibration but correlation. Basically comparing the monitors to the reference data. ^c41614770

          - **Rebelgecko** · [2024-09-23 07:09 UTC](https://news.ycombinator.com/item?id=41623184)
            Sorry, should've been "how". My understanding is that the optical sensors work by recalibrating every week or so, assuming that the lowest CO2 level they've seen is equivalent to the baseline "outdoor" ppm that was set in the factory (which can be adjusted over time to account for climate change). ^c41623184

            If the sensors are in an environment where the CO2 is always elevated, how do you keep it properly calibrated (eg if the CO2 never goes under 700ppm, how do you stop it from recalibrating so that it returns "400" when it should actually return "700") I know you can just turn calibration off but won't the sensors' accuracy decrease over time?

          - **hyperknot** · [2024-09-22 05:56 UTC](https://news.ycombinator.com/item?id=41614904)
            I think he meant How?, meaning normally a calibration is placing indoor monitors outdoors for 20 mins. ^c41614904

            - **avianlyric** · [2024-09-22 07:56 UTC](https://news.ycombinator.com/item?id=41615413)
              If you’re using reference grade instruments, I would assume they’re calibrated in labs using well controlled environments. ^c41615413

              I.e. put sensor in vacuum chamber, remove all gases, then introduce know amount of gases to produce a known target environment.

              Given their reference instruments, I assume they’re also capable of maintaining their calibration for a long period of known time, before they need to be re-calibrated. They would never rely on something as inaccurate as “20 mins outdoors” to calibrate themselves.

      - **aaron695** · [2024-09-22 22:08 UTC](https://news.ycombinator.com/item?id=41620502)
        [flagged] ^c41620502

        \[dead\]

    - **cyberax** · [2024-09-22 05:43 UTC](https://news.ycombinator.com/item?id=41614854)
      \> Interesting. But why would you monitor CO2 outdoors? ^c41614854

      For example, to know that it's futile to try to turn on ventilation to lower the indoor CO2 concentration.

      - **crazygringo** · [2024-09-22 19:14 UTC](https://news.ycombinator.com/item?id=41619223)
        Yup. In my city, on windy winter days the CO2 is as low as it gets, in the low 400's. ^c41619223

        But on a hot windless summer day in a temperature inversion, my meter will read 700 or even 800 outdoors, as the CO2 from vehicles and maybe even power plants just sits around without going anywhere.

        In the winter, if my indoor reading is 800 I open the window a crack to improve my concentration. On certain days in the summer, I just accept it's going to be 1,000 indoors and there's nothing I can do about it.

        - **iforgotpassword** · [2024-09-22 21:52 UTC](https://news.ycombinator.com/item?id=41620398)
          Interesting. I never gave this whole thing much of a thought, but always assumed co2 levels would be higher during winter as there's no green outside to absorb it, plus everyone turning on the central heating systems. ^c41620398

    - **unknown** · [2024-09-22 13:29 UTC](https://news.ycombinator.com/item?id=41616933)
      [deleted] ^c41616933

  - **OldGuyInTheClub** · [2024-09-22 18:28 UTC](https://news.ycombinator.com/item?id=41618927)
    Optical linewidths are influenced by temperature and pressure.  Outdoors, humidity can be a factor as well.  When I did photoacoustic spectroscopy, we used two or more wavelengths in the measurement; one on resonance, one off resonance to help with background discrimination.  I am not sure whether these ultracompact instruments have that capability. ^c41618927

    Additionally, contaminants on any surface the light strikes will generate spurious signals.  Lock-in (synchronous) detection at the optical source modulation frequency can help get rid of a lot of noise but if the noise appears at that frequency, it will corrupt the measurement.

    This classic paper from 1986 covers a lot of what can be done with the technique and how to do it correctly.  Reviews of Modern Physics is behind a paywall but there's a copy on the web at the URL below.


    ```
      Applications of photoacoustic sensing techniques
      Andrew C. Tam
      Rev. Mod. Phys. 58, 381 – Published 1 April 1986
    ```

    
    [http://users.df.uba.ar/dkunik/photothermal/review/tam86.pdf](<http://users.df.uba.ar/dkunik/photothermal/review/tam86.pdf>)

  - **simonebrunozzi** · [2024-09-23 21:10 UTC](https://news.ycombinator.com/item?id=41630593)
    If money is not a problem (let's say, up to \$1,000), what's the best CO2 indoor sensors you would suggest today? ^c41630593

  - **dr\_kiszonka** · [2024-09-22 15:27 UTC](https://news.ycombinator.com/item?id=41617707)
    If you have time, could you write a bit more about the humming phenomenon? ^c41617707

    - **OldGuyInTheClub** · [2024-09-22 18:35 UTC](https://news.ycombinator.com/item?id=41618988)
      Photoacoustic is usually done with a chopped or pulsed light source at a few hundred Hz (ie. audio frequencies).  If the molecules don't absorb at that wavelength or if the molecules are not present, the light just goes through.  If light is absorbed, there will be slight heating when the beam is on resulting in a sound wave at the chopping/pulsing frequency.  This is detected by the microphone.  For weak absorptions, the intensity of the sound wave will be linear in the concentration. ^c41618988

      I think this is what is meant by "humming": There is a sound that is generated when the target molecule is present.

  - **moogly** · [2024-09-22 13:11 UTC](https://news.ycombinator.com/item?id=41616815)
    The Infineon press release talks about indoor monitoring only, and it is even present in the title, but I have noticed that you guys consider HN to be a very important marketing channel, so I get it. ^c41616815

    - **ahaucnx** · [2024-09-22 13:21 UTC](https://news.ycombinator.com/item?id=41616880)
      If you take the time and actually read the blog post I linked to, you will see that mostly it is about indoor CO2. ^c41616880

      However, to understand the performance of these different sensor technologies it is important to point out that they fail under certain environmental conditions, e.g. outdoors.

      - **unknown** · [2024-09-22 13:57 UTC](https://news.ycombinator.com/item?id=41617112)
        [deleted] ^c41617112

- **OldGuyInTheClub** · [2024-09-21 21:52 UTC](https://news.ycombinator.com/item?id=41612909)
  Nice to see this miniaturization of photoacoustic spectroscopy - something I've done a bit of in the past.  It is an underappreciated technique.  Ordinarily one measures the difference in optical throughput with and without a sample.  If it is a weak absorber, it is a difference between two large numbers.  PAS is zero background.  No absorption, no pressure wave, no signal.  Any absorption stands out clearly against that zero background. ^c41612909

- **babl-yc** · [2024-09-21 21:55 UTC](https://news.ycombinator.com/item?id=41612927)
  Seems similar to the SCD40 photoacoustic approach. ^c41612927

  I used that for an open-source CO2 monitor I designed:

  [https://bitclock.io/](<https://bitclock.io/>)

  [https://github.com/goat-hill/bitclock](<https://github.com/goat-hill/bitclock>)

  - **ahaucnx** · [2024-09-22 02:02 UTC](https://news.ycombinator.com/item?id=41614111)
    Great project, lovely design and super cool that it's also open source hardware. ^c41614111

    We at AirGradient open sourced our monitors around 2 years ago and this has been the best decision for our company.

  - **nonninz** · [2024-09-23 10:37 UTC](https://news.ycombinator.com/item?id=41624524)
    Great project, thank you! ^c41624524

    BTW Your "Advanced ESP32 development with ESP-IDF" guide \[1\] is the best "getting started" guide I've seen so far. Up to now no guide has been so clear and complete, and I've spent one week being very frustrated by how confusing the official ones are.

    So thank you again. You made me rekindle the spark of creativeness that got buried by age and daily grind.

    \[1\] [https://bitclock.io/blog/esp-idf-vscode](<https://bitclock.io/blog/esp-idf-vscode>)

    - **babl-yc** · [2024-09-29 18:54 UTC](https://news.ycombinator.com/item?id=41689510)
      Glad to hear! I spent a bunch of time on that post so I was hoping someone would read it :) Good luck with your projects ^c41689510

- **londons\_explore** · [2024-09-22 12:13 UTC](https://news.ycombinator.com/item?id=41616510)
  I have used the MH-Z19 \[1\] \$10 real CO2 sensors for a bunch of things.   They appear to work well, although I have no ability to measure the accuracy of the results. ^c41616510

  I do have a 'one day when I get free time' plan to make new firmware for them to also measure  moisture and a bunch of other VOC's which have unique absorption spectra in the 800-2000nm range, since the hardware itself can be abused as a poor-man's spectrometer.

  \[1\]: [https://www.aliexpress.com/w/wholesale-z19-co2.html](<https://www.aliexpress.com/w/wholesale-z19-co2.html>)?

  - **IgorPartola** · [2024-09-22 12:19 UTC](https://news.ycombinator.com/item?id=41616539)
    There is a way to program these? ^c41616539

    - **londons\_explore** · [2024-09-22 12:45 UTC](https://news.ycombinator.com/item?id=41616651)
      they're just ST microcontrollers.    you can put your own firmware on and do what you like with the hardware. ^c41616651

      The hardware consists of an incandescent bulb and photodiode with amplifier and high res ADC.

      The bulb and photodiode sit in a box with a silvered interior, which allows light from the bulb to reflect around inside the box a lot (and having some light absorbed by CO2) before hitting the photodiode.

- **vardump** · [2024-09-21 20:57 UTC](https://news.ycombinator.com/item?id=41612623)
  Finally an actually working (cheap?) CO2 sensor? ^c41612623

  So many of those actually measure humidity, temp and VOCs and try to derive some sort of CO2 reading out of those.

  - **tzs** · [2024-09-21 21:32 UTC](https://news.ycombinator.com/item?id=41612798)
    It's not really "finally". They introduced a similar sensor, the PASCO2V01, a couple years ago. That one has been available on a breakout board with the necessary support hardware from SparkFun for over a year \[1\]. ^c41612798

    Comparing the datasheets for the PASCO2V01 and the new PASCO2V15 the old one actually seems a little better as far as CO2 measuring performance goes. They are the same on most things, but the old one has slightly better accuracy.

    The new one is ±(50 ppm + 5\%) between 400 ppm and 3000 ppm.

    The old one is ±(30 ppm + 3\%) between 400 ppm and 5000 ppm.

    The big difference is this:

    \> Infineon has recently introduced the PASCO2V15, a new 5 V sensor to improve air quality monitoring in building environments.

    Both of them require a dual voltage power supply. They both want 3.3 V for their digital components and a higher voltage for their IR emitter.

    For the older one that higher voltage is 12 V. For the newer it is 5 V.

    \[1\] [https://www.sparkfun.com/products/22956](<https://www.sparkfun.com/products/22956>)

    - **fnordpiglet** · [2024-09-21 21:35 UTC](https://news.ycombinator.com/item?id=41612820)
      Iirc they were merged into esphome last year too. ^c41612820

  - **Animats** · [2024-09-21 22:15 UTC](https://news.ycombinator.com/item?id=41613032)
    True. The cheap ones are trying to guess CO2. Those are called "indoor air quality sensors". ^c41613032

    Small CO2 sensors have been available for years, for about \$50. Compare \[1\].

    Life of this new device is only 10 years, which is short for HVAC systems. A hotel might have a thousand of these.
    Older devices say "15+" years.

    All these devices have a calibration problem. They drift. They try to correct by treating the lowest value they ever see as "normal" (that's about 400 ppm CO2 today, vs 300 PPM in 1950) and recalibrating. So they're not useful for observing a general increase in CO2. They're also not useful for greenhouses, where CO2 levels may drop below ambient CO2 due to photosynthesis.
    Manual recalibration is possible but requires feeding in pure nitrogen and a known nitrogen/CO2 mixture.\[2\]

    Devices which don't need that re-calibration exist.\[3\] They're more complicated. Also don't seem to be stocked by the usual distributors.

    \[1\] [https://rmtplusstoragesenseair.blob.core.windows.net/docs/pu...](<https://rmtplusstoragesenseair.blob.core.windows.net/docs/publicerat/PSP107.pdf>)

    \[2\] [https://www.co2meter.com/blogs/news/7512282-co2-sensor-calib...](<https://www.co2meter.com/blogs/news/7512282-co2-sensor-calibration-what-you-need-to-know>)

    \[3\] [https://www.murata.com/en-us/products/sensor/co2/overview/te...](<https://www.murata.com/en-us/products/sensor/co2/overview/technicalinfo>)

    - **brianglick** · [2024-09-22 01:43 UTC](https://news.ycombinator.com/item?id=41614024)
      Do you know of anywhere at all to get one of the devices that don’t require re-calibration? ^c41614024

      - **Animats** · [2024-09-22 03:43 UTC](https://news.ycombinator.com/item?id=41614473)
        That is a really good question. ^c41614473

        Murata announced this in 2019, and there's a part number (IMG-CA0011-00/
        IMG-CA0012-00/IMG-CA0023-00) and a full data sheet.\[1\] But no distributor has it. Not DigiKey, Mouser, Arrow, or Newark. Even Octopart doesn't list it. It's on Murata's list of recommended products, not the discontinued list. Try contacting Murata.

        \[1\] [https://go.murata.com/rs/382-MEZ-125/images/HC\%20CO2-sensor\%...](<https://go.murata.com/rs/382-MEZ-125/images/HC%20CO2-sensor%20and%20microblower.pdf>)

  - **fuzzy2** · [2024-09-21 21:05 UTC](https://news.ycombinator.com/item?id=41612671)
    Sensirion has the SCD40, which appears to be based on the same principle. It's much cheaper than the SCD30. ^c41612671

    - **\_blk** · [2024-09-21 21:45 UTC](https://news.ycombinator.com/item?id=41612876)
      Yes, SCD30 series are optical while SCD40 series are photoacoustic. STC series are thermal conductivity based. STC and SCD40 are smaller than SCD30 but less accurate if memory serves (check datasheet). ^c41612876

  - **rainburg** · [2024-09-21 21:13 UTC](https://news.ycombinator.com/item?id=41612709)
    The Senseair S88, which was released earlier this year, costs \~\$22/piece, or \~\$13/piece if you order more than 100. ^c41612709

  - **IgorPartola** · [2024-09-21 21:00 UTC](https://news.ycombinator.com/item?id=41612639)
    This was my thought exactly. I used sensors that were about \$25/each in the past and those worked well but this would be seemingly way easier to integrate and get ahold of. ^c41612639

    - **vardump** · [2024-09-21 21:05 UTC](https://news.ycombinator.com/item?id=41612673)
      \$25 for a CO2 sensor component that actually works is not bad at all. ^c41612673

      - **tobi1449** · [2024-09-21 21:09 UTC](https://news.ycombinator.com/item?id=41612695)
        Sensirion SCD41 should be pretty good, right?
        You can get them for \~25 USD on aliexpress ... ^c41612695

        - **ale42** · [2024-09-21 21:14 UTC](https://news.ycombinator.com/item?id=41612716)
          I'm not sure I would source non-Chinese electronic components from Aliexpress... (unless it's just to play with them, definitely not for a product): you might need to check their reliability and quality. Pretty sure that Sensirion themselves are not selling there, so they are probably either clones, fakes, recycled ones, or if you are lucky authentic ones that for some reason ended up there (but I can't imagine a way). ^c41612716

          - **throwup238** · [2024-09-22 02:16 UTC](https://news.ycombinator.com/item?id=41614174)
            *\> or if you are lucky authentic ones that for some reason ended up there (but I can't imagine a way).* ^c41614174

            Chinese fabs are notorious for running secret shifts that make their customers’ chips to sell themselves. They’re the exact same chip but made without authorization, using the customer’s exact design.

            That said, Sensirion has their own CMOS fabs in Switzerland so that’s very unlikely to be the case here. If they work at all, the counterfeit chips are probably some Chinese CO2 sensor IC that's small enough to fit into the same package, lightly customized to fit the pinout of the original. Or it's just a microcontroller inside faking it a la FTDI.

            - **tobi1449** · [2024-09-23 09:45 UTC](https://news.ycombinator.com/item?id=41624207)
              Huh, good points. 
              It doesn't seem to be just a micro sensor faking it, as it reacts as expected for example when opening the windows.
              I guess the only way to tell if they are any good is to buy a verified good CO2 sensor and compare the outputs then. ^c41624207

        - **radicality** · [2024-09-21 23:26 UTC](https://news.ycombinator.com/item?id=41613408)
          I got mine from M5Stack and works quite well, I’m submitting data every 5 seconds using EspHome/HomeAssistant ^c41613408

- **clumsysmurf** · [2024-09-21 21:23 UTC](https://news.ycombinator.com/item?id=41612752)
  I worked in a building 500 ft from a busy highway and when I cleaned my desk it always had black dust on it. ^c41612752

  Along these lines of air quality, can anyone recommend a similarly advanced PM2.5 / PM10 sensor under \$100 / ea?

  - **trog** · [2024-09-21 21:33 UTC](https://news.ycombinator.com/item?id=41612808)
    I haven't gotten their PM sensor unit but have a CO2 sensor from CO2.click. About to pull the trigger on a PM sensor but just deciding which one. The founder there is active on a few places including Mastodon and I really like my CO2 sensor from them. ^c41612808

    Edit: sorry missed your price guidance. They are quite a bit more so probably not what you're after!

  - **seper8** · [2024-09-22 10:01 UTC](https://news.ycombinator.com/item?id=41615989)
    Please get an air purifier with a HEPA filter... ^c41615989

    Ikea sells a reasonable air purifier AND seperate sensors nowadays!

  - **e44858** · [2024-09-22 17:11 UTC](https://news.ycombinator.com/item?id=41618376)
    Sensirion SEN54. ^c41618376

    It also measures temp/humidity/voc, and has a built-in fan to speed up the response time.

  - **christina97** · [2024-09-21 22:51 UTC](https://news.ycombinator.com/item?id=41613251)
    Have been using a Plantower PMS5003 for a while with ESPhome and it’s pretty good. ^c41613251

- **nimish** · [2024-09-21 21:05 UTC](https://news.ycombinator.com/item?id=41612670)
  They've had a 12v version for a while, and it's quite nice despite the high voltage requirement. I made a little breakout with a boost converter. Sensirion has a slightly smaller sensor as well, SCD41 that I think works on similar principles. ^c41612670

  Neither are cheap, around \$25-40 each in small quantities. The infineon one has a full blown microcontroller handling the operation of the sensors.

  To keep accuracy you would need to have a CO2 gas setup which isn't cheap either, but for indoor use I don't think it matters.

- **FL33TW00D** · [2024-09-21 21:46 UTC](https://news.ycombinator.com/item?id=41612878)
  I’ve been considering designing a wearable that monitors CO2 and PM2.5 continuously, but I’m unsure if people would wear it in conjunction with an Apple Watch or similar. ^c41612878

  - **triwats** · [2024-09-21 22:33 UTC](https://news.ycombinator.com/item?id=41613143)
    This is super interesting for me - but I'd love to put it on a bicycle (they are often locked up and stationary - for example) but move at faster speeds. Maybe this means they are only useful at tracking information when locked/stationary? ^c41613143

    I really like the idea of using cheap (?) devices in a sort of mesh to feed back telemetry data on pollution. Pollution is everyone's concern, so visualising that would be cool.

    Interested to hear if you had any more thoughts on this!

    - **carstenhag** · [2024-09-21 23:04 UTC](https://news.ycombinator.com/item?id=41613310)
      Related: cheap device to track pollution + mesh + visualization: [https://luftdaten.info/](<https://luftdaten.info/>) ^c41613310

      Once had this thing on a balcony of a shared flat in Heilbronn, Germany. Wondered what that was, previous tenant told me about it and it was never removed from there.

      - **triwats** · [2024-09-23 16:21 UTC](https://news.ycombinator.com/item?id=41627751)
        Blimey, that's great! Thanks ^c41627751

    - **rapjr9** · [2024-09-22 13:15 UTC](https://news.ycombinator.com/item?id=41616839)
      The Bikenet project mapped CO2 in a small town: ^c41616839

      [https://www.cs.dartmouth.edu/\~sensorlab/pubs/BikeNet-SenSys0...](<https://www.cs.dartmouth.edu/~sensorlab/pubs/BikeNet-SenSys07.pdf>)

      - **triwats** · [2024-09-23 16:21 UTC](https://news.ycombinator.com/item?id=41627746)
        This is neat, thanks so much! ^c41627746

  - **sbierwagen** · [2024-09-22 07:28 UTC](https://news.ycombinator.com/item?id=41615269)
    Note that NDIR sensors use a surprising amount of power, since they're based around an incandescent bulb shining light through the sample volume. A CO2 wearable will need to be recharged once a day, like a smart watch. ^c41615269

  - **crazygringo** · [2024-09-21 21:53 UTC](https://news.ycombinator.com/item?id=41612919)
    I'm not sure how accurate that would be on your wrist, because the proportion of recently exhaled air would be so much higher, since it's only a foot or two from your mouth. ^c41612919

    CO2 monitors often have little silent fans to draw in fresh air as well, for accuracy.

    - **christina97** · [2024-09-21 22:45 UTC](https://news.ycombinator.com/item?id=41613213)
      I don’t think it’d make a difference. I’ve got one on my desk in front of me and can’t detect a difference with me at the desk vs not. ^c41613213

      - **stevenhuang** · [2024-09-22 02:37 UTC](https://news.ycombinator.com/item?id=41614240)
        Unless your room has really good airflow you should be able to tell quite clearly. ^c41614240

        I have an SCD41 and I see a large spike in readings less than a minute after sitting down at my desk.

  - **seper8** · [2024-09-22 09:47 UTC](https://news.ycombinator.com/item?id=41615930)
    I'd wear this! This would also be very cool to share with others, form like a network to get a clearer picture of air quality ^c41615930

    - **FL33TW00D** · [2024-09-22 11:02 UTC](https://news.ycombinator.com/item?id=41616218)
      It only became possible to do it in a wearable form factor very recently using a combination of the following 2 sensors:
      [https://sensirion.com/products/catalog/STCC4](<https://sensirion.com/products/catalog/STCC4>)
      [https://www.bosch-sensortec.com/media/boschsensortec/downloa...](<https://www.bosch-sensortec.com/media/boschsensortec/downloads/product_flyer/bst-bmv080-fl000.pdf>) ^c41616218

      Not sure the market is big enough to invest my time.

    - **akira2501** · [2024-09-22 17:53 UTC](https://news.ycombinator.com/item?id=41618665)
      \> to get a clearer picture of air quality ^c41618665

      A wearable CO2 monitor would do the opposite of this.

      If you want to measure quality you need fixed location devices.

- **ckocagil** · [2024-09-22 01:32 UTC](https://news.ycombinator.com/item?id=41613969)
  The problem with the common CO2 sensor modules is they don't have DC accuracy. Meaning they rely on the device being present in place where it regularly (e.g at least once a week) gets exposed to fresh air, which the module sets as its baseline. This works because fresh air has roughly the same CO2 concentration everywhere. ^c41613969

  Hopefully this method doesn't have the same restriction.

- **koolba** · [2024-09-22 02:28 UTC](https://news.ycombinator.com/item?id=41614207)
  \> With this architecture, the sensor achieves a high level of precision, offering an accuracy of ±50 ppm ±5\% between 400 ppm and 3,000 ppm. The overall range of the sensor is from 0 to 32,000 ppm. ^c41614207

  What does the back to back ± mean? Is that the variance of accuracy from device to device? Or does the 5\% reference the specific range of 400-3000?

  - **zootboy** · [2024-09-22 03:07 UTC](https://news.ycombinator.com/item?id=41614343)
    It's saying that it could be either +/-50 ppm from the actual reading, or +/-5\%  from the actual reading, whichever is worse. ^c41614343

    - **metaphor** · [2024-09-22 04:47 UTC](https://news.ycombinator.com/item?id=41614697)
      \> *It's saying that it could be either +/-50 ppm from the actual reading, or +/-5\% from the actual reading, whichever is worse.* ^c41614697

      No, it's stacked, and strictly applicable between 400-3000 ppm as characterized (despite 0-32000 ppm operating range by design).

      At the lower 400 ppm end, accuracy is +/- 50 ppm +/- 20 ppm \= +/- 70 ppm.

      At the upper 3000 ppm end, accuracy is +/- 50 ppm +/- 150 ppm \= +/- 170 ppm.

      Also worth noting that the calibrated reference used to determine this published accuracy has an uncertainty of +/- 2\%; ref datahseet\[1\] Table 7.

      Caveat emptor: this published accuracy can't be trusted at face value when sampling more than 1 meas/min; ref ibid.\[1\] Table 4.

      \[1\] [https://www.infineon.com/dgdl/Infineon-PASCO2V15-DataSheet-v...](<https://www.infineon.com/dgdl/Infineon-PASCO2V15-DataSheet-v01_30-EN.pdf?fileId=8ac78c8c914a3ac8019179fecd0c351d>)

- **sbierwagen** · [2024-09-22 07:41 UTC](https://news.ycombinator.com/item?id=41615330)
  I built a CO2 meter around a SCD30 five years ago: [https://bbot.org/blog/archives/2024/05/19/pocket\_co2\_meter\_b...](<https://bbot.org/blog/archives/2024/05/19/pocket_co2_meter_before_it_was_cool/>) ^c41615330

  My takeaway is that it draws a lot more power than you'd expect, thanks to the incandescent light source, and unless there's quite a lot of airflow over the sensor, it'll exhibit self-heating at any poll rate under every ten minutes.

- **shadowpho** · [2024-09-21 21:16 UTC](https://news.ycombinator.com/item?id=41612725)
  Have been using scd30/31/40. Great sensors. This one requires a bit more power but would be interesting to see price as it seems it actually measured CO2. (A lot of other sensors simulate it with measuring alcohols and assume people breathing which gives poor results) ^c41612725

- **Genbox** · [2024-09-21 21:35 UTC](https://news.ycombinator.com/item?id=41612822)
  Datasheet can be found here: [https://www.infineon.com/dgdl/Infineon-PASCO2V15-DataSheet-v...](<https://www.infineon.com/dgdl/Infineon-PASCO2V15-DataSheet-v01_30-EN.pdf?fileId=8ac78c8c914a3ac8019179fecd0c351d>) ^c41612822

- **JSDevOps** · [2024-09-21 22:11 UTC](https://news.ycombinator.com/item?id=41613015)
  [https://aranet.com/en/home/products/aranet4-home?srsltid\=Afm...](<https://aranet.com/en/home/products/aranet4-home?srsltid=AfmBOorZLBfVwdXjQ4rIhhoJPo0sstleUggzHxWeiO8cuqrgLjgB4h-H>) ^c41613015

  - **thadk** · [2024-09-22 00:12 UTC](https://news.ycombinator.com/item?id=41613602)
    I believe Aranet4 contains this NDIR optical sensor [https://www.co2meter.com/collections/sensors/products/006-0-...](<https://www.co2meter.com/collections/sensors/products/006-0-0007-senseair-sunrise-co2-sensor?variant=43961135923398>) ^c41613602

  - **elliottkember** · [2024-09-21 22:37 UTC](https://news.ycombinator.com/item?id=41613166)
    Like that, but cheaper and more accurate. ^c41613166

- **skykooler** · [2024-09-22 02:53 UTC](https://news.ycombinator.com/item?id=41614297)
  It's \$26 on Mouser, which seems like a reasonable price. ^c41614297

- **dzhiurgis** · [2024-09-21 21:30 UTC](https://news.ycombinator.com/item?id=41612790)
  Would be nice if they packaged these up in laptops - fan is already there and always running. ^c41612790

