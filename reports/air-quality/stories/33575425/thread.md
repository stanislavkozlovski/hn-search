# [Analyzing Carbon Dioxide levels while attending IETF-115 in London, UK](https://news.ycombinator.com/item?id=33575425)

Article: [https://www.isi.edu/\~hardaker/news/20221106-ietf-c02-analysis/](<https://www.isi.edu/~hardaker/news/20221106-ietf-c02-analysis/>)

zdw · 2022-11-12 18:05 UTC · 218 reported comments · archived 2026-11-08 12:25 UTC
Observation: 2026-11-08 12:23 UTC → 2026-11-08 12:25 UTC

## Comments

- **ahaucnx** · [2022-11-12 20:35 UTC](https://news.ycombinator.com/item?id=33576769)
  We do indoor air quality monitoring and see very different results across buildings. ^c33576769

  The biggest differentiator is if the building has mechanical ventilation and to what extent this mechanical ventilation uses fresh air vs internal circulation.

  In unventilated crowded spaces like e.g. classrooms, we regularly see CO2 exceeding 3500 ppm. \[1\]

  However in classrooms with a well designed ventilation system you can keep the CO2 \< 1000ppm during the whole school day.

  What the author did in his hotel room to turn on the fan or play around with the A/C settings is a good idea but many hotels Hvac systems do not draw in sufficient fresh air and you will see high CO2 developments.

  \[1\] [https://www.airgradient.com/open-airgradient/blog/we-measure...](<https://www.airgradient.com/open-airgradient/blog/we-measured-the-co2-level-in-a-classrooms-this-is-what-we-found-out/>)

  - **mistr0** · [2022-11-12 22:05 UTC](https://news.ycombinator.com/item?id=33577604)
    I teach in a UK secondary school; the building with my classroom in was built in the 1960s, as many of them are. Ventilation is poor and after a 60-minute lesson with 25-30 students (age \~15) CO2 will be at 2000-2500 ppm. If there are back-to-back lessons it'll be 3000-3500. I can open some doors, but they lead to connected classrooms so this is only practical if those rooms are not in use. Retro-fitting an AC system is likely possible, but expensive. ^c33577604

    - **Arbortheus** · [2022-11-12 22:08 UTC](https://news.ycombinator.com/item?id=33577626)
      Air quality should be a bigger consideration in schools, I bet students will be more attentative and able to focus better without high CO2 levels. We should create the conditions to allow them to succeed. ^c33577626

    - **ahaucnx** · [2022-11-13 00:15 UTC](https://news.ycombinator.com/item?id=33578608)
      You might be interested to join the SAMHE project in the UK \[1\] (that we are part of). It gives free air quality monitors to secondary schools for a large scientific study. ^c33578608

      \[1\] [https://www.samhe.org.uk/](<https://www.samhe.org.uk/>)

  - **icelancer** · [2022-11-12 21:02 UTC](https://news.ycombinator.com/item?id=33577035)
    3500ppm? That would imply an average CO2 level well above 1000ppm. No wonder why it's impossible to stay focused in lecture halls... ^c33577035

    - **MichaelZuo** · [2022-11-12 21:28 UTC](https://news.ycombinator.com/item?id=33577286)
      Yeah, that really makes me rethink my entire education experience... ^c33577286

      - **JohnBooty** · [2022-11-12 22:16 UTC](https://news.ycombinator.com/item?id=33577699)
        ...you could always distract yourself by thinking about all of the political and military decisions that have been made throughout history, affecting millions and billions of human lives, in stuffy cramped rooms with excessively high CO2 levels. ^c33577699

        ...wait, that's not helping?

        - **p1esk** · [2022-11-13 03:27 UTC](https://news.ycombinator.com/item?id=33579697)
          A cynical view - with better CO2 levels the outcome of those political/military decisions could be worse. ^c33579697

        - **MichaelZuo** · [2022-11-13 02:31 UTC](https://news.ycombinator.com/item?id=33579357)
          The utopia of adequate ventilation. ^c33579357

  - **Reason077** · [2022-11-12 21:51 UTC](https://news.ycombinator.com/item?id=33577473)
    Perhaps CO2 sensors should be part of the standard HVAC sensor suite in big buildings? ^c33577473

    That is, along with measuring temperature, the sensors in each room should also measure CO2 levels. If CO2 is rising, fans can be turned on/turned up to bring more fresh air into the room.

    - **Animats** · [2022-11-13 06:26 UTC](https://news.ycombinator.com/item?id=33580603)
      They are part of the sensor suite in big buildings.\[1\] The usual sensor set is temperature, humidity, and CO2.  It's mostly hotels with conference rooms that are serious about this, because their product is comfortable conferences. ^c33580603

      As buildings approach airtightness, this becomes essential. I was expecting more in this area from the IoT crowd, but they never delivered. It's the old-school HVAC systems which do this.

      Some years back I went to an IoT meeting in San Francisco, in a beautifully converted industrial building in Dogpatch on the waterfront. Big windows and skylights, with openable windows driven by manual chain falls on both. Ceiling fans. Plus a standard HVAC system. Was all of this coordinated in any way? No.

      The place should have had motor drives on the windows. They were all on two long shafts, so it wouldn't be all that hard. As the place filled up with people, the skylights should be opened and the ceiling fans driven to blow upward and exhaust hot air and C02. Open the bay-facing windows slightly for intake air. As the evening went on and outside temperature dropped, close the bay-facing windows, continuing to monitor CO2 and temperature. If heating, open a damper to take air from the outside as necessary to keep the CO2 down. When everybody leaves, flush the air for a few minutes, then close everything up, turn off the fans, and let the temperature drop a few degrees.

      The place should have been a showpiece for intelligent building control. But what were they pushing? Refrigerators with a tablet built into the door, for more than the cost of a refrigerator plus an iPad. The tablet had no useful interaction with the refrigerator; it was just a general use tablet.

      Even home "smart thermostats" don't do much. They need this set of sensors, plus an external air damper so they can switch from recirculate to outside air as necessary. And the ability to run fans, without AC or heat as necessary. But that requires actual installation, which neither Amazon nor Apple can competently handle.

      All this stuff saves enough energy to pay for itself.

      \[1\] [https://buildings.honeywell.com/gb/en/products/by-category/s...](<https://buildings.honeywell.com/gb/en/products/by-category/sensors/temperature-and-humidity-transmitters/co2-temperature-humidity-sensors>)

    - **ArchitectAnon** · [2022-11-12 22:05 UTC](https://news.ycombinator.com/item?id=33577601)
      They are legally required in the primary bedroom of all new build houses in Scotland, possibly also in England and Wales. ^c33577601

      - **Reason077** · [2022-11-12 22:14 UTC](https://news.ycombinator.com/item?id=33577679)
        Huh? Really? Are you thinking of Carbon Monoxide detectors, perhaps? Sometimes these are incorrectly called "CO2 detectors". ^c33577679

        - **sampo** · [2022-11-12 22:56 UTC](https://news.ycombinator.com/item?id=33578019)
          Appears to be true: ^c33578019

          \> CO2 monitoring equipment should be provided in the apartment expected to be the main or principal bedroom in a dwelling where infiltrating air rates are less than 15m3/hr/m2 @ 50 Pa.

          [https://www.gov.scot/publications/building-standards-2017-do...](<https://www.gov.scot/publications/building-standards-2017-domestic/3-environment/314-ventilation/>)

          Well done, Scotland.

          - **pifm\_guy** · [2022-11-13 03:24 UTC](https://news.ycombinator.com/item?id=33579677)
            Monitoring equipment alone isn't really sufficient, unless it is hooked up to a fan or ventilation equipment to maintain a suitable level, and an alarm to alert if that level can't be maintained. ^c33579677

            If the law requires just monitoring equipment, then you know that in a utility cabinet somewhere will be a screen with the data on, that nobody ever looks at, and might as well not be there.

        - **unknown** · [2022-11-12 22:58 UTC](https://news.ycombinator.com/item?id=33578030)
          [deleted] ^c33578030

      - **matsimitsu** · [2022-11-13 02:34 UTC](https://news.ycombinator.com/item?id=33579367)
        New houses in The Netherlands have a monitor in each room (bedrooms, kitchen, living room and bathroom/shower) that control the mechanical ventilation. ^c33579367

        In fancier homes they can control the ventilation per room, though the standard is that they control the ventilation for the entire house.

  - **rsync** · [2022-11-13 03:29 UTC](https://news.ycombinator.com/item?id=33579712)
    "However in classrooms with a well designed ventilation system you can keep the CO2 \< 1000ppm during the whole school day." ^c33579712

    Where does "opening the windows" fit in a scale of "well designed ventilation systems" ?

    I'm not being flip, or snarky - I'm serious.

    I don't think it's terribly sophisticated or *haughty* to consider lack of opening windows to be a poverty.

    Hotel rooms, hospital rooms, classrooms ... whatever ... windows that cannot be opened is a poverty.

    - **kragen** · [2022-11-13 20:46 UTC](https://news.ycombinator.com/item?id=33587161)
      it varies, but usually opening the windows is plenty of ventilation unless it's not an option (e.g., because it's too hot or too cold outside) ^c33587161

      it's much more common to wish for bigger windows because you're hot than because you're falling asleep

      by virtue of stuffing 30 people into a single room you force them to compromise on environmental conditions; whoever's out in the tails of the distribution or has low social status is going to get screwed over because the resulting compromise will favor average people and people of high social status

      that's just how compromises work, people struggle to promote their conflicting interests, so popular people and people with popular interests win

      but typically you can still find a compromise that's pretty okay for 90+\% of people

      (1000 ppmv - 420 ppmv) co₂ \= 580 ppmv co₂

      r 20° / 1 atm \= 24 ℓ/mol

      1 kg co₂ / day / 人 \= 11.6 mg co₂ / s / 人

      30 人 · 11.6 mg co₂ / s / 人 / (44 g co₂/mol co₂) \= 7.9 mmol co₂ / s  (a classroom)

      7\.9 mmol co₂ / s · 24 ℓ/mol \= 0.19 ℓ co₂ / s

      0\.19 ℓ co₂ / s / 580 ppmv co₂ \= 330 ℓ / s (of air)

      in medieval units that's about 700 'cfm'

      if the classroom has 10 m² of open windows you're fine, even an undetectable draft of 0.03 m/s is sufficient, but if it has 1 m² you need a barely detectable breeze of 0.3 m/s, if it has 0.1 m² you need a pretty noticeable breeze of 3 m/s ('light breeze' on the beaufort scale), and if it has a little 100-mm-square register you need 30 m/s which is a 'violent storm' on the beaufort scale (above 'whole gale')

      at 'fresh breeze' (8–11 m/s) you need 300–400 cm² of window

      well designed ventilation systems can provide this kind of airflow while controlling the temperature and humidity but they are at a big disadvantage because 300–400 cm² of window is a lot smaller than 300–400 cm² of duct

      sometimes that's not what matters most tho

  - **sireat** · [2022-11-13 09:25 UTC](https://news.ycombinator.com/item?id=33581444)
    I was surprised how well a large modern building ventilates CO2. ^c33581444

    We had some employees complain about feeling "stuffy" when air conditioning was turned off(due to budget constraints).

    So  maintenance brought their own CO2 meter and I brought my trusty Aranet4.

    Both our readings were around 650 in a medium sized office with 4 people. Apparently the raise of temperature from 22C to 26C was enough to trigger internal "stuffiness".

    PS By comparison my bedroom regularly reaches 3000 in the mornings if no windows are left open.

- **jeroenhd** · [2022-11-12 19:41 UTC](https://news.ycombinator.com/item?id=33576297)
  One thing I wonder about, especially seeing the numbers during take-off: how well can an Aranet 4 sensor deal with changes in pressure and temperature? ^c33576297

  As I understand it, these sensors require (sometimes lengthy) calibration to remain accurate.

  For automatic calibration, the device needs to be in fresh air for 30 minutes, no closer than 1 meter from the nearest person. There is also a manual calibration method. I don't know how often calibration is necessary, but I also think this use case may not be what the sensor was designed to do.

  - **iudqnolq** · [2022-11-12 19:58 UTC](https://news.ycombinator.com/item?id=33576438)
    Many cheaper CO2 sensors require frequent calibration. Often they just assume the weekly min reading is fresh air (420), or something like that, which is extremely imprecise. ^c33576438

    I bought the Aranet4 because it claims not to need recalibration except in exceptional circumstances. They suggest keeping the factory calibration unless you can guarantee a proper controlled environment. I don't have the equipment to test their claims, but the readings have stayed plausible for months with no calibration.

    Edit: Note that if you're using your CO2 sensor as a proxy for the rate at which the air in an occupied room is replaced with fresh air the calibration imprecision doesn't matter. You're probably eyeballing the second derivative over the course of minutes-to-hours.

    I use my CO2 sensor for that, but I also care about the absolute. There's some evidence that normal rates of CO2 in modern buildings make your brain foggy. I'm trying to figure out if a program better when I use various interventions to increase fresh air.

    - **lucb1e** · [2022-11-12 22:35 UTC](https://news.ycombinator.com/item?id=33577857)
      Easy way to test pressure changes: have a small room with a well-fitting door. Ventilate it well, then put the sensor in there. Open and close the door fast (mainly to/from the almost-fully-closed position) to get pressure changes. The pressure will only change briefly, but if it didn't keep up with the airplane, it definitely won't keep up with this. Depending on how frequent the readings are, at some point while opening/closing you'll get readings during a change and an outlier if it's sensitive to this. (You can also fashion something with e.g. cling wrap and stuff, but this seems simpler and you don't use throwaway plastic or anything.) ^c33577857

      I've used a barometer on a plane before. When they turn on the pressurization system, it's very clearly noticeable, but not a huge change. (A train in a tunnel is worse.) I'd expect this would be a similar effect.

      - **TylerE** · [2022-11-13 00:20 UTC](https://news.ycombinator.com/item?id=33578649)
        Pressurization has gotten better over the years. Modern planes generally pressurize (or depressurize, more accurately. Sooner and slower. Like, imagine starting to transistion to the target pressure - usually equivalent to 6-8000ft, over time, starting as soon as the door is closed for pushback, instead of only adjusting during the climb. ^c33578649

    - **ahaucnx** · [2022-11-12 20:18 UTC](https://news.ycombinator.com/item?id=33576618)
      Yes the ABC is often an issue and can lead to an underestimation of the CO2 values. ^c33576618

      This often happens in non ventilated and relatively air tight rooms.

      We collect air quality data from many schools and see this happening in some classrooms that even over the unoccupied time during the night the CO2 will not reach ambient levels the next morning.

      - **p1esk** · [2022-11-12 21:35 UTC](https://news.ycombinator.com/item?id=33577346)
        What do you think about Air Quality Egg product \[1\]? How does it compare to Aranet4?  How do these two compare to AirGradient ONE product? Which chemicals are most important to monitor in a typical 40yo house in Florida: CO2, CO, NO2, SO2, O3? ^c33577346

        \[1\] [https://airqualityegg.com/shop](<https://airqualityegg.com/shop>)

        - **ahaucnx** · [2022-11-13 00:27 UTC](https://news.ycombinator.com/item?id=33578683)
          I do not own an Air Quality Egg or an Aranet so I cannot really comment on both. ^c33578683

          In general most of the low cost monitors use similar sensor modules, e.g. Plantower for PM, Sensirion for TVOCs etc. What is important to ensure that the CO2 sensor is an NDIR or photo accoustic and not using estimated CO2 via a TVOC sensor that is very inaccurate.

          I would start measuring PM, CO2 and TVOCs in the house to first understand more about how well the HVAC system works. Then optimize it for low CO2 and PM. This should then flush out most of the internal pollution sources as well.

          - **p1esk** · [2022-11-13 02:40 UTC](https://news.ycombinator.com/item?id=33579406)
            I understand you might be biased, but still, why would you recommend getting AirGradient ONE over the competing products? ^c33579406

  - **phphphphp** · [2022-11-12 19:48 UTC](https://news.ycombinator.com/item?id=33576370)
    I think you might have it the wrong way round, as the product information mentions fresh air as a requirement for manual calibration, not automatic. ^c33576370

    "If a drift of the CO2 measurements occurs, calibration feature of the device should be used. Auto calibration mode is utilizing ABC algorithm whereas
    Manual calibration mode demands sensor to be exposed to fresh air."

    "CO2 sensor of the device is calibrated at standard atmospheric pressure. CO2 readings are pressure compensated and comply with the
    specifications down to 750 hPa. If the device has to be used at high altitude for a prolonged period of time, manual calibration of the unit should be
    performed for optimal performance. It is not intended to use the device higher than 4000 m (13 000 ft) above the sea level."

    [https://cdn.bfldr.com/FS48XT6B/at/k9b9wjnv8f455crkp7846j/Ara...](<https://cdn.bfldr.com/FS48XT6B/at/k9b9wjnv8f455crkp7846j/Aranet4_datasheet_v25_WEB.pdf>)

  - **ahaucnx** · [2022-11-12 19:52 UTC](https://news.ycombinator.com/item?id=33576395)
    From our experience normal temperature fluctuations do not impact the accuracy. However many NDIR sensors do not like vibrations and get inaccurate after being moved around. Then you need to wait for the automatic baseline calibration to kick in or do a manual calibration. ^c33576395

    The Aranet 4 uses the Senseair Sunrise that is more resistant to vibrations.

    However I could imagine that sudden air pressure changes could have an impact on the measurement accuracy.

  - **mox1** · [2022-11-12 19:50 UTC](https://news.ycombinator.com/item?id=33576387)
    yea I recently started monitoring my homes CO2 levels with some DIY sensors. You need to enter your elevation above sea level or have a pressure sensor hooked up. ^c33576387

    So if the op set a static pressure I assume that would affect the readings a lot.

    Calibration is also just the sensor looking for the co2 floor (ie the lowest level possible). You need to do this weekly or monthly maybe..?

    Auto calibration just sets the lowest level it has recently seen as the floor.

    - **ahaucnx** · [2022-11-12 19:59 UTC](https://news.ycombinator.com/item?id=33576446)
      What was your experience with the DIY monitor that you build? ^c33576446

      I am asking because we maintain an open source / open hardware indoor air quality project \[1\] that we continuously update and I am interested to learn about missing features we might have.

      Did your build have a dedicated pressure sensor?

      \[1\] [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>)

  - **jcdavis** · [2022-11-12 19:56 UTC](https://news.ycombinator.com/item?id=33576419)
    The Aranet has both temperature and pressure sensors, though how those are used as part of the CO2 calculation (if at all) I don't know ^c33576419

    - **fuzzfactor** · [2022-11-13 08:36 UTC](https://news.ycombinator.com/item?id=33581207)
      This touches on instrument theory. ^c33581207

      Besides just the ideal gas law in a nonideal world.

      Let's assume a perfect instrument.

      With a sensor for a target gas for instance that puts out 0 to 10 volts over a range of 0 to 10000 reference ppm, if the response over that range were perfectly linear, and all replacement sensors perfectly identical, then no mathematical device correction would need to be made.  This is the most fundamental analog heart of the device.

      So what is calibration?  It compensates for imperfection.

      Based on a detector (sensor) which is sensitive to the number of molecules it is exposed to at the time, this number of molecules will be mathematically converted to a concentration level in PPM, in the case of gas phase that is PPM by volume.  IOW for every million molecules you breath in, how many are CO2?

      Counting molecules are us.

      If you used an analog dial meter to show you the real-time votage output from the sensor, all you had to do was remember that 1 volt equals 1000 PPM, and you know when the needle points to 0.400 volts that means it's 400 PPM.  At this point you still have a completely analog instrument.  The analog circuitry is doing the math for you, and the math is very simple because the device is so perfect.

      Even the dial-indicating voltmeter is perfect, otherwise there would be a need for it's own mechanical correction like turning the little screw(s) to adjust the needle.

      When you replace the analog voltmeter with a digital voltmeter instead, it's still the same analog instrument at the heart, so no difference yet except you can probably read 0.400 volts more repeatably on the numerical display rather than the analog dial.  Unless you had a very large diameter dial.  And you would still need the voltmeter itself calibrated to make sure the numbers were true voltage otherwise the PPM shown would not be right.  This can be a little more complex, and more subject to error, than turning a little screw on an analog meter but it accomplishes the same thing.  Digital voltmeters usually had more than just one screw to adjust.  And many more (cheap) electronic components inside subject to drift compared to the few mechanical changes capable of occurring over time in the analog meter.

      So digital voltmeters themselves can be very flexible in their features, often analog meters would simply have a custom-printed scale to readout directly in desired units.

      Either way with a perfect voltmeter the perfect sensor still isn't good enough simply because of the task at hand.

      When the air is thinner for any reason whether due to temperature or pressure (altitude), there will naturally be fewer molecules of CO2 detected by the sensor even though it's the exact same reference air sample with the exact same PPM.  But the meter would then show an unrealistically low reading.

      So in order for it to be "reference PPM", you would calibrate under "standard conditions" of temperature & pressure.

      Then as conditions change across the working ranges of temperature & pressure, compensations need to be made so the recorded value remains realistic in PPM.

      The basic equation is PV \= nRT where the pressure times the volume equals the number of molecules times a constant times the temperature.  The pressure is relative to absolute vacuum and the temperature relative to absolute zero.

      With our perfect voltage output we have turned the voltage into a unitless number which we can directly interpret in PPM.  And for gases PPM is n/V, or molecules per (million molecule) volume.

      Rearranging to P/RT \= n/V, we see that for n/V to remain constant, P/RT must remain unity as P & T change, since R is a constant.

      We already knew intuitively that pressure & temperature are inversely related, so the simply perfect analog instrument operator could simply make a few calculations from their voltmeter reading, depending on the temperature in their lab and the barometric reading on their barometer.  Then they could always record the the real CO2 concentration even though the meter reading was only perfect under standard conditions.

      A more advanced analog instrument would instead self-correct its voltmeter readings so when each part of the instrument is fully calibrated, it always showed true PPM regardless of temperature or pressure changes.  By adding a temperature and pressure sensor to the circuit the operator would no longer need to take their own T & P readings in the lab.  The voltages (according to their slopes) from these additional sensors would then affect the main gas sensor voltage to result in the corrected reading.  In a less-than-perfect world each of these sensors also need their own calibration to known reference values under ideal conditions, and to compensate for the variability of electrical component performance of not just the sensors themselves.  So there would be a number of variable resistor calibration adjustments on the circuit board, some being knobs on a control panel, others miniature setscrews inside for factory adjustment not routinely needed.

      Alternatively without a controlled environment for calibration, at least use well documented ambient temperature and pressure.  Calculated compensations then are not based degrees F or C, nor PSIG, instead you use absolute temperature in degrees K, and pressure in PSIA.  These are the mathematical variables that can be completely eliminated from the equation if the actual "standard" controlled environment is available.

      And that's for the analog instrument to do all the math itself.

      These same 3 analog sensors (and voltmeter) with all their component variability and interactive imperfections can have all this support circuitry to allow full (sometimes tedious) analog calibration like this, or forget about having any analog circuitry doing any math and just convert each sensor's raw analog output to digital and have software do the math (and calibration) and display from there.

      This moves the tediousness to the data system electronics instead of the instrument electronics.

      Or anything in between these two extremes.

      Regardless, you only get results as good as your dedication to the electronic tediousness, you just have to put it in the right place either way.

- **sampo** · [2022-11-12 22:45 UTC](https://news.ycombinator.com/item?id=33577929)
  \> (it turns out my office really needs a fan as the single plant on the opposite side of the room is failing to keep up even with my sedentary exhaling) ^c33577929

  A human exhales about 1 kg of CO2 in a day (24 hours). That is about 270 grams of C. You'd need enough plants to sequester 270 grams of carbon, or about 0.5 kg of biomass (dry weight) per day, to "keep up" with your exhaling. This is much more than one houseplant.

  - **kragen** · [2022-11-13 03:46 UTC](https://news.ycombinator.com/item?id=33579810)
    my notes from 02019 [https://dercuano.github.io/notes/gardening-machines.html](<https://dercuano.github.io/notes/gardening-machines.html>) say that my rosemary bush had a doubling time of about 66 days ^c33579810

    rosemary is about 50\% water \[citation needed\] and most of the dry part is carbohydrate, (ch₂o)ₙ, which should weigh \[edited\] 68\% as much than the co₂, so roughly each kg of co₂ becomes 1.4 kg of rosemary

    a doubling time of 66 days is about 1.05\% growth per day, so you need about 130 kg of rosemary bush in your office to grow 1.4 kg per day and thus keep up with your exhaling

    except actually it only needs to grow 1.4 kg per day during the daytime, not at night when it isn't photosynthesizing, so maybe you could get by with 90 kg of rosemary bush or so

    and probably about half a tonne of soil, say about 2 m²

    could be a single plant but it's kind of a tree-sized plant

    if you need it to suck up your co₂ at night you need a crassulacean acid metabolism (cam) plant like aloe, but i think you need a larger amount of it because cam plants tend to grow slower.  maybe moringa but i don't know if it's obligate cam or facultative cam

    \[edited to correct calculation erorr\]

    - **jobigoud** · [2022-11-13 14:39 UTC](https://news.ycombinator.com/item?id=33583447)
      Kurtis Baute tried to seal himself in a greenhouse with plants and that wasn't enough to compensate the exhaling. It was featured in a Tom Scott video: [https://www.youtube.com/watch?v\=1Nh\_vxpycEA](<https://www.youtube.com/watch?v=1Nh_vxpycEA>) ^c33583447

      - **kragen** · [2022-11-13 17:18 UTC](https://news.ycombinator.com/item?id=33585060)
        there are lots of ways to fuck it up ^c33585060

        concrete carbonatation was eating the oxygen in biosphere 2

    - **OJFord** · [2022-11-13 07:23 UTC](https://news.ycombinator.com/item?id=33580840)
      \> maybe you could get by with 90 kg of rosemary bush or so ^c33580840

      Which would be massive, and look absurd indoors.

      Though maybe that's not a problem, since you shouldn't have anyone over who might laugh at and embarrass you over it - it'd then be only half as big as it needs to be!

      - **kragen** · [2022-11-13 07:55 UTC](https://news.ycombinator.com/item?id=33580973)
        i think it would look freaking awesome and smell amazing. i would love it if this were the new standard for offices ^c33580973

        might harbor moths tho

        - **OJFord** · [2022-11-13 08:17 UTC](https://news.ycombinator.com/item?id=33581095)
          I agree it would smell amazing. ^c33581095

          But offices! 90kg+ of living rosemary per person! When I worked in an office we didn't have anything like the space for that, even if you got rid of the desks and chairs and people. That would be quite something.

          - **kragen** · [2022-11-13 08:21 UTC](https://news.ycombinator.com/item?id=33581130)
            you'd need several square meters per person of skylights or other windows to feed the rosemary ^c33581130

            - **OJFord** · [2022-11-13 08:41 UTC](https://news.ycombinator.com/item?id=33581240)
              But higher humidity than you'd otherwise want... Maybe you could get away with something comfortable if they were kept well-watered, a continual automatic drip say. ^c33581240

              - **kragen** · [2022-11-13 08:57 UTC](https://news.ycombinator.com/item?id=33581314)
                rosemary can handle pretty low rainfall, you can probably keep the surface of the soil pretty dry if you water it very intermittently ^c33581314

                things like aloe and spekboom even less rainfall

                then you could work nights

                but this is starting to sound less like an office and more like the stuff i was writing about 9 years ago in [https://dercuano.github.io/notes/underground-arcology.html](<https://dercuano.github.io/notes/underground-arcology.html>)

    - **morog** · [2022-11-13 07:31 UTC](https://news.ycombinator.com/item?id=33580882)
      Spekboom - Portulacaria afra is what u want. Very dense plant with lots of surface area and supposedly among the best CAM photosynthesis plants. Grows indoors, requires minimal care. Image search for 'huge spekboom' they are truly impressive ^c33580882

      - **kragen** · [2022-11-13 08:05 UTC](https://news.ycombinator.com/item?id=33581030)
        looks nice too but it's not obligate cam, apparently you have to starve it of water to force it into cam (which means it won't grow) ^c33581030

        edible tho, like moringa

- **nicoburns** · [2022-11-12 19:29 UTC](https://news.ycombinator.com/item?id=33576215)
  This seems to pretty well justify my recent approach to covid precautions which is to wear an N95 mask on public transport (and nowhere else), and to try and avoid social situations in densely packed rooms where practical. ^c33576215

  - **MuffinFlavored** · [2022-11-12 20:23 UTC](https://news.ycombinator.com/item?id=33576665)
    does wearing a mask stop from spreading if you have it or stop you from getting it from others or both? ^c33576665

    - **Baeocystin** · [2022-11-12 20:51 UTC](https://news.ycombinator.com/item?id=33576924)
      An N95 does both, to a highly effective degree. ^c33576924

      - **timr** · [2022-11-12 21:19 UTC](https://news.ycombinator.com/item?id=33577204)
        We have no good evidence for this claim. The only studies involving n95 masks and respiratory illness were conducted in hospital settings (i.e. don't reflect "normal" life), have high risk of bias (i.e. were small and were not randomized, controlled trials), and have shown mixed results. ^c33577204

        This is the WHO review that summarized the existing evidence for masks at the start of the pandemic. There were 4 studies on n95 masks in hospitals:

        [https://www.thelancet.com/journals/lancet/article/PIIS0140-6](<https://www.thelancet.com/journals/lancet/article/PIIS0140-6>)...

        Additionally, this is the most comprehensive review of mask literature I am aware of. It explicitly states that:

        \> At least ten studies evaluate the clinical efficacy of different types of masks compared to one another, but without a no-mask control group most provide little insight into mask efficacy.

        \> Four RCTs, four meta-analyses, and one prospective cohort study found surgical masks were non-inferior to N95s for protection against respiratory infections, and one found evidence that N95s provide greater protection than medical masks against self-reported clinical respiratory illness but not ILI. However, a recent review found that evidence
        that N95s protect healthcare workers from clinical respiratory infections at all is “low quality". One meta-analysis of particular note, an April 2020 preprint of a Cochrane review of
        clinical evidence for both surgical and N95 masks, “did not find any differences in the clinical effectiveness of either type of mask in the setting of respiratory viral infection transmission to healthcare workers,” although the review’s final November version omitted this language.

        [https://www.cato.org/sites/cato.org/files/2021-11/working-pa...](<https://www.cato.org/sites/cato.org/files/2021-11/working-paper-64.pdf>)

        We simply don't know if n95 masks provide any protection -- personal or otherwise -- in the real world. That is the only honest answer to the parent's question. Everyone who claims otherwise is extrapolating from laboratory experiments, low-quality observational data, or (this is probably the most common)  hearsay.

        - **OJFord** · [2022-11-13 07:46 UTC](https://news.ycombinator.com/item?id=33580941)
          This is like saying we don't know if washing your hands before preparing food helps hygeine in the real world there have been no good studies. ^c33580941

          1\. Of course it does, it doesn't need to be studied;

          2\. Yes fine sure other behaviour may negate any benefit.

          The question was about the performance of the masks, not whether the average person will grab a bus rail then get home whip off the mask and pick their nose before washing their hands.

          To which the answer is simple, N95/FFP3 rates particle filtering effectiveness at a certain size; coronavirus particles are within that window.

          - **rsj\_hn** · [2022-11-13 08:32 UTC](https://news.ycombinator.com/item?id=33581184)
            \> Of course it does, it doesn't need to be studied; ^c33581184

            No, public health mandates are not something you derive from first principles, but from actual observational data about the effectiveness of interventions.

            It's like the difference between a drug being effective in vitro rather than in vivo. There are many confounding factors and side effects that need to be understood, so it is irresponsible to skip directly from the in vitro study to mass distribution of an intervention.

            To help illustrate this point, let's assume that wearing the N95 masks reduces the likelihood of getting infected by some fraction, but not enough to drive the reproduction rate down below 1 (which is certainly the case). Say you only get from 2.0 to 1.8. Therefore unless this difference is the key to overwhelming hospitals, it should make no difference to death rates. However:

            Those who have lung disease (14\% of the population) are less likely to wear these masks because it makes breathing more difficult for them, so they will become differentially more likely to catch the disease as a result of the healthy population wearing the masks than if no one was wearing the masks.  But since herd immunity will be reached anyway (just at a later time), this intervention may result in an increase in deaths as the population of infected people will have a greater share of those with lung disease than if no one wore the masks.

            Now, is the scenario I laid out *true*? Well, we don't really know what herd immunity is here, and we don't know whether differential rates of compliance are big enough, *which is why you have to study it*. You always have to study. You don't go from a thought experiment to an intervention without study, because there are always confounding factors that can reverse your thought experiment once the intervention is applied in the real world.

            This is actually historically interesting, because it was the ineffectiveness of masks during the 1918 flu epidemic that was one of the major findings of public health, distinguishing it as a separate field from immunology. E.g. everyone assumed you needed to wear masks, but ex-post studies showed this made no difference for death rates in the 1918 pandemic.

            Now, I'm not saying that the 1918 data is decisive here, because they didn't have N95 masks then, but still use of the masks they did have was considered a best practice by immunologists, so it was still a shocking result how something that worked in the thought experiment could fail when deployed as an intervention. All of a sudden, people began to realize that "Yes, you need to study these things. First principles and logical deduction is not enough." That realization that public health is not immunology plus Aristotelian logic but is instead its own field -- that is the bedrock axiom of public health.

            - **OJFord** · [2022-11-13 08:38 UTC](https://news.ycombinator.com/item?id=33581223)
              The question wasn't about public health mandates. ^c33581223

        - **azakai** · [2022-11-12 22:22 UTC](https://news.ycombinator.com/item?id=33577756)
          \> We simply don't know if n95 masks provide any protection -- personal or otherwise -- in the real world. ^c33577756

          That is simply not true.

          First, doctors and researchers consistently say that N95s are known to provide protection against Covid.

          Second, this is the first google result on that topic:

          [https://www.cdc.gov/mmwr/volumes/71/wr/mm7106e1.htm](<https://www.cdc.gov/mmwr/volumes/71/wr/mm7106e1.htm>)

          Quoting from that CDC page:

          \> What is already known about this topic?

          \> Face masks or respirators (N95/KN95s) effectively filter virus-sized particles in laboratory settings. The real-world effectiveness of face coverings to prevent acquisition of SARS-CoV-2 infection has not been widely studied.

          \> What is added by this report?

          \> Consistent use of a face mask or respirator in indoor public settings was associated with lower odds of a positive SARS-CoV-2 test result (adjusted odds ratio \= 0.44). Use of respirators with higher filtration capacity was associated with the most protection, compared with no mask use.

          \> What are the implications for public health practice?

          \> In addition to being up to date with recommended COVID-19 vaccinations, consistently wearing a comfortable, well-fitting face mask or respirator in indoor public settings protects against acquisition of SARS-CoV-2 infection; a respirator offers the best protection.

          You can say that that might be just correlation, but as those quotes mention, we do know how N95s work: they filter viral particles. That is easy to prove in lab settings. Real-world settings involve more factors, like how well-fitting the mask is, but it would be very surprising if a good N95 properly used did not offer any protection!

          N95 masks work. It's a good idea to wear one when relevant.

          - **timr** · [2022-11-13 01:12 UTC](https://news.ycombinator.com/item?id=33578926)
            \> That is simply not true. ^c33578926

            \> First, doctors and researchers consistently say that N95s are known to provide protection against Covid.

            I just provided you with the sum total of medical evidence supporting the claim. Citing unspecified "doctors and researchers" is not a rebuttal. You are repeating *hearsay*, which was exactly my point.

            Also, you should know that that MMWR study you've chosen to emphasize here was widely panned by scientists on *both* sides of the mask debate. It's based on a *telephone survey* with a 13\% response rate. The statistics are hopelessly biased due to the test-seeking behavior of the study participants. It is not credible:

            [https://vinayprasadmdmph.substack.com/p/mask-studies-reach-a...](<https://vinayprasadmdmph.substack.com/p/mask-studies-reach-a-new-scientific>)

            It's good that you pointed it out, however, because it's a perfect illustration of the abysmal level of "evidence" that has been used to support similar claims throughout the pandemic. Unfortunately, a many terrible "papers" were published and widely distributed on masks, including many in "good" journals. If you don't understand how to appraise medical evidence, you will be easily misled.

            \> N95 masks work. It's a good idea to wear one when relevant.

            Unfortunately, there is no good evidence supporting this assertion, and "when relevant" is essentially unknown.

            - **azakai** · [2022-11-13 01:48 UTC](https://news.ycombinator.com/item?id=33579129)
              It's not unspecified "doctors and researchers". It's the overwheming consensus among medical professionals. The CDC recommends masks, as I linked. So does the WHO, ^c33579129

              [https://www.who.int/news-room/questions-and-answers/item/cor...](<https://www.who.int/news-room/questions-and-answers/item/coronavirus-disease-covid-19-masks>)

              And so does the European CDC,

              [https://www.ecdc.europa.eu/en/publications-data/using-face-m...](<https://www.ecdc.europa.eu/en/publications-data/using-face-masks-community-reducing-covid-19-transmission>)

              etc. etc. The picture is very clear here.

              And, again, the lab evidence is incredibly supportive. We know that N95s filter viral particles. It's possible *in theory* that that doesn't end up mattering - say if people never wear them right, or if they end up taking more risks because they think they are safer - but that seems unlikely when other evidence says otherwise, and the experts concur.

              - **timr** · [2022-11-13 22:26 UTC](https://news.ycombinator.com/item?id=33588037)
                \> It's the overwheming consensus among medical professionals. The CDC recommends masks, as I linked. ^c33588037

                "Consensus", *without evidence*, is just opinion. Tragically for the credibility of science-based policy, the evidence backing these mask recommendations is incredibly weak. That's just a fact. Repeating to me that "scientists say" something-or-other to be true does not change the fact that the evidence backing the claim is poor.

                Medical science is riddled with examples of interventions that "medical professionals" recommended without evidence, only to find that they were ineffective -- or worse, harmful -- when a controlled study was finally performed. Just a few recent examples: hormone replacement therapy; aspirin for heart disease; widespread opioid use for pain; mammograms under age 50. All were "overwhelming consensus". All have been since found to be useless. Some have led to tragic outcomes.

                The CDC and the WHO could have run randomized controlled trials to find out of n95 masks are effective at preventing illness. They did not.

              - **ehvatum** · [2022-11-13 05:57 UTC](https://news.ycombinator.com/item?id=33580488)
                \> The picture is very clear here. ^c33580488

                I wish it were.

                It should not be difficult to verify that N95 masks filter *COVID* virus particles effectively.

                If such a study had been performed, nobody could reasonably hypothesize that, owing to the properties of the viral envelope, an N95 filter could stop nanometer black carbon particles but not COVID viruses of the same size.

                It is baffling that the very basic experiment has not been done: DOES N95 FILTER COVID?

                The advancement of human knowledge absolutely depends on *VERIFYING* assumptions. Institutionalizing common beliefs without empirical data  is a crime against science.

                - **azakai** · [2022-11-13 06:13 UTC](https://news.ycombinator.com/item?id=33580556)
                  Why are you certain such studies have not been done? Plenty of things have been published in that space. For example, ^c33580556

                  [https://academic.oup.com/jid/article/226/2/199/6582941](<https://academic.oup.com/jid/article/226/2/199/6582941>)

                  [https://www.frontiersin.org/articles/10.3389/fmed.2021.65431...](<https://www.frontiersin.org/articles/10.3389/fmed.2021.654317/full>)

                  You might respond with some specific skepticism about some particular detail in either study. But e.g. the first is in the respected Journal of Infectious Diseases. It passed peer review. And plenty of other studies exist.

                  The bigger picture here is that every major health agency in the world recommends good masks such as N95s, as mentioned earlier. That is the standard for relevant healthcare workers for good reason. The experts in those agencies have looked at the studies and made that conclusion, which is the general consensus in the healthcare field.

                  There is some chance all the experts are wrong on this. That happens sometimes. But it's rare.

                  - **timr** · [2022-11-14 20:21 UTC](https://news.ycombinator.com/item?id=33600414)
                    I gave you a comprehensive review of all literature related to masks, used on people, to prevent actual illness. You don't like the conclusion of that data (there's little clinical evidence supporting their use), but digging up irrelevant laboratory papers doesn't change it. ^c33600414

                    The first link here is a lab study that doesn't demonstrate anything of relevance to the question: *fit-tested* masks, in a laboratory, where the outcome is "virus in the air" doesn't tell you if same masks, *in the real world* will protect against illness *in people*.

                    Second link is more of the same: demonstrating that a mask *can* filter particles, in an ideal setting, does not tell you anything about *what actually happens in the real world*. For that, you need clinical evidence (which I've already shown you is weak).

                    Medical science is filled with stories of things that work in theory, but don't work in practice. Literally every drug that failed a clinical trial (i.e. \>99\% of all drugs tested) worked in the lab. You must do controlled tests on real people to see what *really* works.

                    \> the first is in the respected Journal of Infectious Diseases. It passed peer review.

                    Journal of Infectious Diseases is actually not a great journal, and "peer review" is not a magical talisman that prevents publication of bad research. See also: citing the WHO, the CDC, etc., when you've been shown that the *evidence* for the recommendations they're making is not robust.

        - **andbberger** · [2022-11-12 22:08 UTC](https://news.ycombinator.com/item?id=33577634)
          nonsense, N95s are highly effective and if you want to make a good faith argument that they're not try citing the new england journal of medicine and not the fucking cato institute, good lord ^c33577634

          - **unknown** · [2022-11-13 01:25 UTC](https://news.ycombinator.com/item?id=33578993)
            [deleted] ^c33578993

        - **HyperSane** · [2022-11-12 21:40 UTC](https://news.ycombinator.com/item?id=33577386)
          Why do surgeons wear masks? ^c33577386

          - **MobiusHorizons** · [2022-11-12 21:54 UTC](https://news.ycombinator.com/item?id=33577494)
            Not an expert, but as I understand it, surgeons could be exposed to much more than airborne viruses (bacteria, bodily fluids, etc). So masks would be worn for more possible reasons. It’s a good question though, I hope someone knowledgeable answers it. ^c33577494

            - **azakai** · [2022-11-12 22:25 UTC](https://news.ycombinator.com/item?id=33577783)
              Surgical masks and face shields are indeed designed specifically to protect from fluids. That is very important too. ^c33577783

              Separately from that, when there is a risk of airborne transmission as there is with Covid, doctors and nurses will wear appropriate masks like N95s.

      - **unknown** · [2022-11-12 21:04 UTC](https://news.ycombinator.com/item?id=33577062)
        [deleted] ^c33577062

    - **VancouverMan** · [2022-11-12 21:26 UTC](https://news.ycombinator.com/item?id=33577260)
      Some long-term, large-scale studies of the effects of widespread public masking have been performed recently. ^c33577260

      For example, one lasting over 1.5 years was done in the province of Ontario, Canada, involving approximately 15,000,000 participants, in environments ranging from dense urban settings to sparse rural ones. In Ontario's largest and densest population center, Toronto, the duration this study was about 2 years in length.

      It was conclusively demonstrated that widespread public masking does not prevent infection, and it does not prevent transmission, of airborne viruses.

      It was conclusively proven that such masking did cause accessibility problems, it did cause significant social disruption, and it did cause environmental damage, among numerous other harmful effects.

      - **HyperSane** · [2022-11-12 21:39 UTC](https://news.ycombinator.com/item?id=33577381)
        Can you provide a link to this study? ^c33577381

        If masks don't work then why do surgeons wear them?

        - **samatman** · [2022-11-12 21:58 UTC](https://news.ycombinator.com/item?id=33577531)
          To the latter question, it's to prevent droplets of spittle from landing on exposed tissue. ^c33577531

          There are pathogens which spread by droplets, rather than aerosols, the Sars2 virus doesn't happen to be one of them. Yes, if you spit directly onto an open wound or mucous tissue, but it doesn't live long on surfaces, and the droplet-fomite route is how that vector of infection works.

          - **HyperSane** · [2022-11-13 08:02 UTC](https://news.ycombinator.com/item?id=33581010)
            "prevent droplets of spittle from landing on exposed tissue" ^c33581010

            Isn't tiny droplets of saliva how most respiratory viruses spread?

        - **lucb1e** · [2022-11-12 22:40 UTC](https://news.ycombinator.com/item?id=33577893)
          They're joking that there were infections in the city despite mask requirements (surprise) and that mask requirements caused "significant social disruption".... At least I hope it's supposed to be a joke. ^c33577893

          - **HyperSane** · [2022-11-13 08:02 UTC](https://news.ycombinator.com/item?id=33581012)
            It is just sad anti-mask BS. ^c33581012

            - **VancouverMan** · [2022-11-13 23:02 UTC](https://news.ycombinator.com/item?id=33588298)
              The only thing that's "anti-mask" is reality. ^c33588298

              All of the scientific evidence shows that widespread everyday masking just doesn't work.

              If masking worked at all, then the "pandemic" would have been over by the end of 2020, at the very latest. Obviously, that isn't what happened, because masking isn't effective.

              - **HyperSane** · [2022-11-14 19:06 UTC](https://news.ycombinator.com/item?id=33599180)
                If respiratory viruses spread via tiny droplets of saliva then masks that actually filter them out HAVE TO reduce the spread of these viruses. ^c33599180

                "If masking worked at all, then the "pandemic" would have been over by the end of 2020, at the very latest."

                If 100\% of people masked 100\% when in groups but that is hardly the case.

- **dataflow** · [2022-11-12 20:25 UTC](https://news.ycombinator.com/item?id=33576679)
  I've heard some people can (train themselves to?) tell when the CO2 level rises in the room. Has anyone here managed to? If so, do you have any tips on how (or whether!) to do this, and/or what it feels like (if it's possible to give any vague explanation in text)? ^c33576679

  - **afusalan** · [2022-11-12 20:33 UTC](https://news.ycombinator.com/item?id=33576746)
    \> I've heard some people can (train themselves to?) tell when the CO2 level rises in the room. Has anyone here managed to? If so, do you have any tips on how (or whether!) to do this, and/or what it feels like (if it's possible to give any vague explanation in text)? ^c33576746

    The best indication is feeling sleepy. Once you become sleepy go outside and take deep breaths, then you understand the sensation difference between O2 and CO2.

    - **pistoriusp** · [2022-11-13 07:23 UTC](https://news.ycombinator.com/item?id=33580838)
      I always assumed that this was somewhat natural, but it may just be my upbringing. I grew up in a warm country without air conditioning, so open windows were the only way. Then moved to a cold country and noticed the sensation. I put 1-1 together. ^c33580838

      In my case my face, specifically my forehead, feels warm. Not to the touch, but more to the nerves. I think it may be different for different people.

    - **dataflow** · [2022-11-12 20:35 UTC](https://news.ycombinator.com/item?id=33576776)
      Unfortunately that doesn't seem to work for me. Right now my room has \> 1200ppm CO2 (due to closed doors/windows) but I don't feel sleepy at all, or any differently (that I can discern) from when it's \< 600ppm. Do you know if it needs to be significantly higher for that feeling to kick in? If so, approximately how much? ^c33576776

      - **JohnBooty** · [2022-11-12 22:26 UTC](https://news.ycombinator.com/item?id=33577790) ^c33577790

        ```
            Unfortunately that doesn't seem to work for me.

            Right now my room has > 1200ppm CO2 (due to closed 
            doors/windows) but I don't feel sleepy at all
        ```

        
        It's a very gradual difference. If you're doing something interesting at 1000-2000ppm you probably won't feel sleepy, but it will probably be harder to focus on something you don't find stimulating and you'll be more inclined to feel sleepy.

        - **dataflow** · [2022-11-12 22:29 UTC](https://news.ycombinator.com/item?id=33577813)
          Interesting, I guess I can try to see if I can notice that. Thanks! ^c33577813

      - **colechristensen** · [2022-11-12 20:51 UTC](https://news.ycombinator.com/item?id=33576923)
        Have a meter going and look at it. I’d describe it as a feeling in my lungs as i breathe I can start to feel above 800ppm. The air feels heavy maybe? ^c33576923

        I think some people are more sensitive to it than others.

        - **OJFord** · [2022-11-13 07:27 UTC](https://news.ycombinator.com/item?id=33580857)
          Have you tested yourself by concentrating on your breathing a bit and then guessing the level before you look at it? ^c33580857

          I'm not disbelieving, just curious.

      - **afusalan** · [2022-11-12 21:12 UTC](https://news.ycombinator.com/item?id=33577130)
        Hmm, I've never had the device to measure the levels tbh. I can say I'm fairly sensitive to air as i do breathwork regularly. 1200 ppm sounds a lot, maybe that's coming from not just CO2 in the air but maybe dust particles, smoke, food vapour, or chemicals such as odor, ozone, perfume, house cleaning products etc. ^c33577130

  - **JohnBooty** · [2022-11-12 22:21 UTC](https://news.ycombinator.com/item?id=33577747) ^c33577747

    ```
         Has anyone here managed to? If so, do you have 
         any tips on how (or whether!) to do this
    ```

    
    I have, basically.

    The easiest (only?) way to do this is simply to have a CO2 sensor, and pay attention to it. You'll quickly learn to intuitively correlate what you're seeing on the sensor with what you're experiencing. After a while you'll be able to vaguely approximate the CO2 levels without even looking at the sensor.

    Of course, you won't be able to pinpoint an exact CO2 level, but you'll be able to tell when it's e.g. \> 1000.

    You've already been doing this your whole life, of course. You've already been distinguishing between "fresh" and "stuffy" air. "Stuffy" air is just our colloquial term for air with undesirably high CO2.

    - **lucb1e** · [2022-11-12 22:38 UTC](https://news.ycombinator.com/item?id=33577871)
      Don't you think those 'experience correlations' are based on proxy parameters? Temperature being one of the main ones I would expect. I don't experience water as fresh unless it is cold, for example. ^c33577871

      - **TylerE** · [2022-11-13 00:28 UTC](https://news.ycombinator.com/item?id=33578698)
        Our brains are incredibly good at sensing CO2, because it’s what drives respiration. ^c33578698

        The “my lungs are burning and I must breath” signal is actually caused by high co2. We can’t perceive blood oxygen levels at all.

        This is actually something hospitals have to be aware of. A tiny sliver of the population (1-10000, maybe) have greatly reduced sensation of co2, so can literally stop breathing (while awake!) if placed on high flow 100\% oxygen.

      - **JohnBooty** · [2022-11-12 22:57 UTC](https://news.ycombinator.com/item?id=33578023) ^c33578023

        ```
             Don't you think those 'experience correlations' 
             are based on proxy parameters?
        ```

        
        Oh absolutely, I'm sure that's a huge portion of it. Nonetheless, I'm much more attuned to it now.

        Situations with high CO2 are usually situations with lots of warm, stagnant, exhaled air in rooms filled with people.

        Would I be able to detect high CO2 levels in an environment with cool, well-circulated air? I'm not sure. Certainly not as well, and perhaps not at all.

        In practice, it probably doesn't matter. I don't think there are many of those pathologically counterintuitive CO2 situations. If the air *seems* stuffy or stagnant then you can be fairly certain it's full of CO2 and/or airborne pathogens.

        - **lucb1e** · [2022-11-12 23:26 UTC](https://news.ycombinator.com/item?id=33578272)
          Right. Especially if you own a meter as well, it's probably all good. I also know people that don't own meters who think they're in stale air as soon as it gets a warm in a room and need to see an open window constantly and then turn up the heating some more. But if you have a meter to tell you whether you were right, that argument doesn't work anymore, so I've changed my mind on whether using proxy metrics is necessarily bad! ^c33578272

          - **JohnBooty** · [2022-11-13 04:38 UTC](https://news.ycombinator.com/item?id=33580125) ^c33580125

            ```
                I also know people that don't own meters who think 
                they're in stale air as soon as it gets a warm in 
                a room and need to see an open window constantly 
                and then turn up the heating some more
            ```

            
            Oh man, that seems really obnoxious. I don't even use an *actual* meter that way!

    - **dataflow** · [2022-11-12 22:28 UTC](https://news.ycombinator.com/item?id=33577805)
      I've been trying that; I do have a sensor. I can probably guess the CO2 level with decent accuracy, but that's not because I feel any different—but rather because I know how long I've been in the room with closed doors/windows. ^c33577805

      With respect to "stuffy" vs. "fresh" air, I don't know whether my sense of it is the same as others'. What I would call "stuffy" is probably affected by humidity, dust, odors, plants, etc. and not just CO2.

      - **JohnBooty** · [2022-11-17 05:39 UTC](https://news.ycombinator.com/item?id=33635404) ^c33635404

        ```
            With respect to "stuffy" vs. "fresh" air, I 
            don't know whether my sense of it is the same 
            as others'. What I would call "stuffy" is 
            probably affected by humidity, dust, odors, 
            plants, etc. and not just CO2. 
        ```

        
        That's fair. I'm not sure if I'm really sensing CO2 levels, or if I'm wholly reliant on those proxy factors that you mentioned.

        I know that when my wife turns on the gas oven downstairs I can definitely feel a difference even if I wasn't aware she was turning it on and the CO2 meter confirms the CO2 spike. But even then, maybe I'm just "sensing" it via proxy factors like smell.

        In practice it probably doesn't matter all that much. Those proxy factors are really good proxies. It's hard to think of real-world scenarios where they wouldn't be.

  - **rwmj** · [2022-11-12 20:34 UTC](https://news.ycombinator.com/item?id=33576766)
    At KVM Forum 2019 \[1\] there was a particular theatre where the enclosed space with many people and lack of ventilation was very obvious.  I felt dizzy and sleepy a few times at lectures there (and nowhere else).  No training needed!  Edit: It was the room shown in this picture: \[2\] ^c33576766

    \[1\] [https://events19.linuxfoundation.org/events/kvm-forum-2019/a...](<https://events19.linuxfoundation.org/events/kvm-forum-2019/attend/venue-travel/>)

    \[2\] [https://locations.filmfrance.net/location/lyon-convention-ce...](<https://locations.filmfrance.net/location/lyon-convention-centre-amphitheatre>)

  - **quantum\_magpie** · [2022-11-12 21:31 UTC](https://news.ycombinator.com/item?id=33577314)
    I can't say anything about training it, but beside the usual sleepiness, at \>1000 ppm I get a feeling of swelling eyeballs and tingling teeth/dentures. I've been this way as long as I remember. ^c33577314

  - **zahrc** · [2022-11-12 20:42 UTC](https://news.ycombinator.com/item?id=33576849)
    It feels stuffy. I get headaches and get tired. When you open a window it’s almost like instant relief ^c33576849

    - **JohnBooty** · [2022-11-12 22:30 UTC](https://news.ycombinator.com/item?id=33577814)
      Yeah the thing we've casually called "stuffy air" forever is, essentially, 100\% equivalent with high CO2 levels. ^c33577814

      There are some other situations where non-"stuffy" air might have too much CO2, I guess. I guess you could pump CO2 into a room with cool, dry air.

      But barring a contrived situation like that, stuffy\=CO2.

  - **iofiiiiiiiii** · [2022-11-13 19:02 UTC](https://news.ycombinator.com/item?id=33586213)
    I have the unfortunate pleasure of being very sensitive to CO2 levels. At around 800-900 ppm I get a general feeling that something is abnormal. If it goes to 1000 ppm then I can usually tell that I am not thinking well anymore. It is a similar feeling to being slightly drunk - for example, I start a thought but find it difficult to carry it through to the conclusion. ^c33586213

    Before I got a CO2 meter, I could always tell within hours when my building's flaky central ventilation fan had failed because I simply felt something was off.

    Unless you are similarly cursed/blessed, just get a CO2 meter. I could not imagine learning this, it is like learning to feel temperature.

  - **dzhiurgis** · [2022-11-12 22:08 UTC](https://news.ycombinator.com/item?id=33577630)
    I’m not very sensitive to it but I start getting stuffy nose, especially overnight. ^c33577630

  - **quakeguy** · [2022-11-12 20:33 UTC](https://news.ycombinator.com/item?id=33576743)
    That’s called grandpa-tells-you-to-go-sleep Syndrom, it is harmless usually. ^c33576743

- **bArray** · [2022-11-13 02:48 UTC](https://news.ycombinator.com/item?id=33579455)
  \> I went 2.5 years with no plane fights and minimal in-person contact to suddenly "everyone must get back to normal! get on those planes! let's have lots of face to face meetings!" ^c33579455

  I don't know the author's background, but I really hate that otherwise normal people have been reduced to such measures. The advice to return to normal is good. 2.5 years of lockdown were mostly wasted - sorry, enjoy the resulting recession.

  If you are healthy, COVID is just a nasty flu. Take a few days off work, and go back knowing that your natural immunity will serve you well going forwards.

  One thing that doesn't appear to be addressed is that CO2 is a rough measure for potential exposure, but indoors the air circulation flow is really important. You want the air to take the longest possible path from another person before it meets you. Better yet through a filter, even better it never meets you at all.

  - **hardaker** · [2022-11-14 18:12 UTC](https://news.ycombinator.com/item?id=33598335)
    \> I don't know the author's background, but I really hate that otherwise normal people have been reduced to such measures. ^c33598335

    So, sorry if you read that as a complaint.  But it was a feeling for how I think the world is reacting now.  Not that it's necessarily bad -- as I think that after returning to normal levels of travel and in-person conversations, it's very clear to me that there was no good virtual alternative hallway conversations.  That being said, it also feels like many meetings could be held virtually when there wasn't much need of true in-person interactions.  However, to put one case in point: I had a fantastic trip to IETF-115 and much of that was likely because I was on-site.  I'm glad I went.

  - **legulere** · [2022-11-13 08:44 UTC](https://news.ycombinator.com/item?id=33581253)
    It’s a particularly nasty flu. You’re well advised to train your immune system before encountering the first time with vaccination. It also makes sense to reduce the dangers of infection (not just of Covid), as every infection also does lasting damage to your body including the immune system (there’s a really smart study about measles in the Netherlands about that). ^c33581253

    What you are doing is an optimization problem: you want to reduce your risk of getting infected while restricting yourself as few as possible. How restricting you find measures and how much you want to prevent getting infected is a very personal thing. I will wear masks while shopping and in public transportation, but I still go to restaurants (without masks). Other people will find masks too insufferable.

    Hand hygiene and air hygiene for new buildings should be a no-brainer though.

    - **bArray** · [2022-11-14 00:36 UTC](https://news.ycombinator.com/item?id=33588912)
      \> It’s a particularly nasty flu. ^c33588912

      No doubt, but for the majority it is recoverable.

      \> You’re well advised to train your immune system before encountering the first time with vaccination.

      I believe that it's effectiveness is greatly reduced now. The available vaccine was for the alpha variant. From what I remember reading, it essentially no longer reduces the probability of you getting COVID at all, meaning your immune system is essentially unprepared (and hence can't defend against it).

      \> It also makes sense to reduce the dangers of infection (not just of Covid), \[..\]

      Somewhat, but then you never end up building natural immunity to anything. You have those isolated tribes that would likely get killed off by the common cold if it was ever introduced to them.

      \> How restricting you find measures and how much you want to prevent getting infected is a very personal thing.

      It is a personal thing, but it was also an idea inflicted on people. This was not generally well practised before, nor does it particularly have any benefit done in small (read one) isolated pockets. I believe we have all now seen people who are many-times vaccinated, wear multiples masks, avoid any contact with people, and yet are otherwise perfectly healthy.

      \> Hand hygiene and air hygiene for new buildings should be a no-brainer though.

      Even prior to COVID, I wish more consideration was put in place for air quality. Bin the ionizers and get decent filters in place that reduce carbon dioxide filters.

- **cobertos** · [2022-11-12 20:05 UTC](https://news.ycombinator.com/item?id=33576493)
  The anecdote about being sleepy on a plane makes me wonder if we couldn't just modulate our CO2 intake as a sleep aid. I find it \_incredibly easy\_ to sleep on a plane, and I generally have a very hard time with sleep due to brain not turning off. ^c33576493

  I think it would be interesting to see if there's any correlation between restful sleep and CO2 levels too. Maybe change the CO2 level to higher to induce sleep, and then fall asleep, and then bring it back down to have a nicer sleep.

  - **avian** · [2022-11-12 20:11 UTC](https://news.ycombinator.com/item?id=33576551)
    I would hate to have a machine in my bedroom that is capable of raising the CO2 level. I don't think anyone could convince me that it would not decide to suffocate me at midnight next 29th February or something, regardless of its safety features. ^c33576551

    - **lucb1e** · [2022-11-12 22:50 UTC](https://news.ycombinator.com/item?id=33577969)
      \> a machine in my bedroom that is capable of raising the CO2 level. ^c33577969

      It doesn't have to be so complex. It could be as simple as a little canister that you simply take up, open in the bedroom, and empties itself (for a room of a given m³), then turn ventilation on low and go to sleep. The CO2 level would spike to the target level in a minute or so (presumably not a dangerous level, just one that makes you temporarily less smart and attentive) and then has some half life depending on your ventilation method.

      I'm not a doctor, I have no idea if it's smart to raise the level to 3, 4, idk how many thousand ppm are being proposed for this, even if it's for only 30 minutes or whatever. Just saying, I don't see obstacles to doing this safely if the action itself is safe.

      - **kragen** · [2022-11-13 03:57 UTC](https://news.ycombinator.com/item?id=33579876)
        a 3 × 4 × 3 bedroom contains 36 m³ of air weighing about 44 kg.  2000 ppm co₂ \[this is by mass, right?  not volume?\] would be 88 g or 72 ℓ, which if all pooled on the floor would form a layer 6 mm deep, so probably no danger of direct suffocation ^c33579876

        carbonated drinks are carbonated to about 4 volumes so you could get 6 3-liter bottles of soda water and open them in your bedroom, releasing 72 ℓ of co₂ over the next, probably, half hour

        normal levels of ventilation for inhabited spaces are several air changes per hour, like 3–10, so this wouldn't raise your co₂ levels much unless the ventilation was super low

        i also don't know if this is a safe thing to do but i don't see any obvious dangers.  you can't accidentally put twice as much co₂ in a bottle of soda water and iirc the idlh is like 30000 ppm

        - **kragen** · [2022-11-13 08:37 UTC](https://news.ycombinator.com/item?id=33581210)
          it's by volume: [https://en.wikipedia.org/wiki/Carbon\_dioxide\_in\_Earth\%27s\_at...](<https://en.wikipedia.org/wiki/Carbon_dioxide_in_Earth%27s_atmosphere>) ^c33581210

          'on a molar basis'

          so it's 72 ℓ (3.0 mol) but not 88 g (2.0 mol).  fortunately the rest of my calculations used the correct volume rather than the incorrect mass

      - **cobertos** · [2022-11-13 00:32 UTC](https://news.ycombinator.com/item?id=33578720)
        I imagine you could make it more controlled/targetted using a canister, a mask (like CPAP machines), and a nozzle of specific radius too. Don't have to adjust for the whole room and  don't have to bottle/release as much CO2 ^c33578720

    - **dzhiurgis** · [2022-11-12 22:14 UTC](https://news.ycombinator.com/item?id=33577677)
      Normally your reflexes kick in when you start suffocating from co2. Nitrogen tho… ^c33577677

      I wonder if sleepiness is some sort of evolutionary reflex or actually caused by co2 in body.

    - **MobiusHorizons** · [2022-11-12 21:56 UTC](https://news.ycombinator.com/item?id=33577515)
      I think the general idea would be to have a device that typically reduces co2 level through ventilation, and just turn it off at night. That would let your normal breathing add the co2. ^c33577515

      - **lucb1e** · [2022-11-12 22:47 UTC](https://news.ycombinator.com/item?id=33577942)
        I wouldn't like to take hours for my sleep aid to kick in, if I would need such a thing. ^c33577942

        Instead of the room, maybe a little device called blanket could be used, but I don't know how reliably people get out from under that if they get in the habit of associating under blanket \= sleep \= good, because it certainly wouldn't be good to be under that all night.

        - **cobertos** · [2022-11-13 00:33 UTC](https://news.ycombinator.com/item?id=33578733)
          Might help to have it on a schedule, like a thermostat has, or maybe more advanced like Nest does. Then it kind of tapers you into a sleep schedule. ^c33578733

          Wouldn't work if coming back from a late night out though

- **Reason077** · [2022-11-12 21:42 UTC](https://news.ycombinator.com/item?id=33577399)
  \> *"Conclusions ... don't ride the buses is probably an early and obvious one."* ^c33577399

  Yes, the air quality on London buses is consistently terrible on cold days. There is very little ventilation in those buses other than "open the windows", and when it gets cold people don't do that. Often it seems like you're not only breathing in everyone else's food smells and stinky breath, but road fumes and dust as well.

  - **Litost** · [2022-11-13 00:51 UTC](https://news.ycombinator.com/item?id=33578832)
    It's also possible that air quality on the London Tube is *much* worse than the bus, at least for particulate matter: ^c33578832

    "Researchers found that a person travelling on a bus for two and a half hours was exposed to a third of what they would be travelling on the Tube for just an hour."
    [https://www.independent.co.uk/news/uk/home-news/air-pollutio...](<https://www.independent.co.uk/news/uk/home-news/air-pollution-london-underground-tube-worse-than-above-ground-a8721586.html>)

    EDIT:
    Regarding CO2 levels, there's a 2018 FOI request which seems to imply it wasn't monitored back then, but was within regulatory limits though I'm not sure I'd want to travel on the tube more often than necessary?

    "The regulatory limits for CO2 are 5000 parts per million (ppm) for 8 hours time weighted equivalent or a short term exposure limit (15 minutes) of 15000ppm."
    [https://tfl.gov.uk/corporate/transparency/freedom-of-informa...](<https://tfl.gov.uk/corporate/transparency/freedom-of-information/foi-request-detail?referenceId=FOI-0540-1819>)

    - **Reason077** · [2022-11-13 10:03 UTC](https://news.ycombinator.com/item?id=33581627)
      I’ve lived in London long enough to remember the “black snot” you’d get after riding on the Tube (especially the Northern Line!) back in the early 2000s. They’ve done a lot to improve ventilation, and reduce dust from train brakes, in recent years. ^c33581627

      The air certainly smells and *feels* a lot fresher and healthier on the extensively-ventilated Tube compared to on crowded buses with little or no ventilation at all.

  - **dzhiurgis** · [2022-11-12 22:05 UTC](https://news.ycombinator.com/item?id=33577600)
    Do brits also have “cold air and draft causes common cold” too? ^c33577600

    - **Arbortheus** · [2022-11-12 22:11 UTC](https://news.ycombinator.com/item?id=33577651)
      Yes, but it's something your grandparents might say rather than a widely held belief. I think people nowadays are clever enough to know that colds are a transmissible infection. ^c33577651

      - **Reason077** · [2022-11-12 22:24 UTC](https://news.ycombinator.com/item?id=33577778)
        Yeah. But most bus passengers still dislike being cold more than they dislike stale air. So most of the windows are usually closed. ^c33577778

        - **MichaelCollins** · [2022-11-13 04:13 UTC](https://news.ycombinator.com/item?id=33579962)
          CO2 clouds the mind and impairs judgement.   Dressing inappropriately for the season is probably a symptom of this.  People would dress more appropriately for the weather if they got more fresh air in the winter. ^c33579962

      - **dzhiurgis** · [2022-11-12 22:32 UTC](https://news.ycombinator.com/item?id=33577839)
        Typical response here is “but cold air weakens immunity“! ^c33577839

- **jll29** · [2022-11-12 21:17 UTC](https://news.ycombinator.com/item?id=33577186)
  Thanks, great post. When you visit London, you should also measure your exposure to PM2.5, PM10, NO, NO2, ... - the risk of catching a virus is only one risk from your cocktails of risk types. ^c33577186

  [https://eu.usatoday.com/story/news/world/2017/04/10/london-t...](<https://eu.usatoday.com/story/news/world/2017/04/10/london-toxic-air-pollution-killing-thousands-every-year/100304958/>)

  [https://www.london.gov.uk/press-releases/mayoral/londons-tox...](<https://www.london.gov.uk/press-releases/mayoral/londons-toxic-air-is-triggering-asthma-attacks>)

  [https://www.unep.org/news-and-stories/press-release/revealed...](<https://www.unep.org/news-and-stories/press-release/revealed-every-londoner-exposed-dangerous-toxic-air-particles>)

- **thadk** · [2022-11-12 19:52 UTC](https://news.ycombinator.com/item?id=33576397)
  Several of us have built visualization tools which produce output a bit similar to the one in this article for the aranet4 unit. These can be found linked from: [https://observablehq.com/@thadk/aranet4-explorer](<https://observablehq.com/@thadk/aranet4-explorer>). 
  Works best with the iPad app on an M1/M2 macOS computer. ^c33576397

  There are also several other ways to get the output such as a bleak project on GitHub ([https://github.com/Anrijs/Aranet4-Python](<https://github.com/Anrijs/Aranet4-Python>)).

- **djmips** · [2022-11-12 19:42 UTC](https://news.ycombinator.com/item?id=33576313)
  I have a few thoughts. ^c33576313

  One: that even if the C02 seems fine, if the din of the room means everyone is shouting then viral dispersal

  will be much higher.

  Two: it seems like having fresher air, will be more costly in the winter unless people can put up with lower temperature.

  I wonder how effective an airplane filter really is with regard to viruses.

  Should buildings and enclosed spaces be redesigned to include better filtering and at what running cost will that be?

  - **kortilla** · [2022-11-12 19:54 UTC](https://news.ycombinator.com/item?id=33576404)
    \> wonder how effective an airplane filter really is with regard to viruses. ^c33576404

    Airplanes are far better than any normal indoor building space. It’s a constant blend of outside air that means the entire cabin’s volume of air is gone within something like 5 mins.

    - **sampo** · [2022-11-12 20:19 UTC](https://news.ycombinator.com/item?id=33576632)
      \> Airplanes are far better than any normal indoor building space. ^c33576632

      But only when they fly. When you are waiting that 30 minutes sitting in the plane after boarding, the fraction of re-breathed air can get high. People have measured 2000 and 4000 ppm CO2 readings.

      - **MichaelZuo** · [2022-11-12 21:25 UTC](https://news.ycombinator.com/item?id=33577255)
        Looking from the chart it seems like the CO2 levels were elevated for the entire flight? ^c33577255

        As in it never dips below 1200pm on either the short haul or long haul flight.

        Also with the caveat in the article: "Note that the graphs below aren't calculated for altitude adjustment. Since planes are generally pressurized to an equivalent of 8000 feet, and senor drift is typically 3
         per 1000 feet of elevation, it means that while in the air the CO2
         levels are likely \$24\% higher than shown on the graph."

        It seems the logged numbers are underestimating it.

  - **hedgehog** · [2022-11-13 05:53 UTC](https://news.ycombinator.com/item?id=33580469)
    On the energy item modern HVAC systems use a device called an ERV to greatly reduce energy loss to ventilation. No need to turn down the heat to get fresh air. The thermal plume associated with each occupant makes the problem a bit easier too, in general stale air heads to the top of the room because it's warmer and more humid therefore less dense. Not a new idea and some good models to look at. ^c33580469

    [https://en.wikipedia.org/wiki/Energy\_recovery\_ventilation](<https://en.wikipedia.org/wiki/Energy_recovery_ventilation>)

    [https://techxplore.com/news/2020-12-ventilation-easy-highly-...](<https://techxplore.com/news/2020-12-ventilation-easy-highly-effective-low-cost.html>)

    [https://hackaday.com/2022/07/07/the-benefits-of-displacement...](<https://hackaday.com/2022/07/07/the-benefits-of-displacement-ventilation/>)

- **rufus\_foreman** · [2022-11-12 20:50 UTC](https://news.ycombinator.com/item?id=33576912)
  I guess when I was born, background CO2 was around 330 ppm. Is there anything I can do to breathe air like that again in my house? ^c33576912

  - **yourMadness** · [2022-11-12 21:52 UTC](https://news.ycombinator.com/item?id=33577484)
    You could add 80\% nitrogen and 20\% oxygen to dilute the CO2 to the desired level. ^c33577484

    But that's not exactly easy or cheap. And dangerous when done wrong.

    - **rufus\_foreman** · [2022-11-12 21:56 UTC](https://news.ycombinator.com/item?id=33577516)
      How exactly would I do that? ^c33577516

      I'm OK with not easy, not cheap, dangerous, and done wrong.

      - **samatman** · [2022-11-12 22:05 UTC](https://news.ycombinator.com/item?id=33577607)
        As long as you're okay with not cheap, Alfaintek has you covered. ^c33577607

        - **rufus\_foreman** · [2022-11-12 22:09 UTC](https://news.ycombinator.com/item?id=33577639)
          Do I have to relocate to the EU? ^c33577639

          - **lucb1e** · [2022-11-12 23:01 UTC](https://news.ycombinator.com/item?id=33578063)
            Increased social equality and mobility, happiness index, etc. are a free bonus I hear, so I guess one could generally recommend that. Depends a bit on where you're coming from, Norway/Switzerland/Iceland are also not EU for example. ^c33578063

  - **ThrowawayTestr** · [2022-11-12 21:15 UTC](https://news.ycombinator.com/item?id=33577163)
    Get a co2 scrubber or a bunch of plants. ^c33577163

    - **jefftk** · [2022-11-12 21:43 UTC](https://news.ycombinator.com/item?id=33577411)
      You would need absurd numbers of plants.  You breathe out \~11L/hr CO2, which is \~22g.  Over a day this is \~0.5 kg.  So your plants would need to be getting collectively 0.5kg heavier daily by pulling CO2 from the air just to balance out your own breathing, let alone the CO2 coming in from the outside. ^c33577411

      - **rufus\_foreman** · [2022-11-12 21:45 UTC](https://news.ycombinator.com/item?id=33577421)
        What's the math if I have a cat? ^c33577421

        - **jefftk** · [2022-11-12 21:54 UTC](https://news.ycombinator.com/item?id=33577496)
          Maybe the cat weighs 5\% of what you do, and respirates 5\% as much as well? In which case it's within the margin of error of the above. ^c33577496

          - **rufus\_foreman** · [2022-11-12 22:00 UTC](https://news.ycombinator.com/item?id=33577554)
            I'm from the midwest. The cat weighs like half a percent of what I do. ^c33577554

            - **jefftk** · [2022-11-12 22:08 UTC](https://news.ycombinator.com/item?id=33577635)
              A really small housecat weighs 5lb. For that to be 0.5\% of your weight you'd need to be half a ton, at which point my math above is a bit low. ^c33577635

              - **rufus\_foreman** · [2022-11-12 22:45 UTC](https://news.ycombinator.com/item?id=33577925)
                All right so do the math. ^c33577925

                Have you ever been to the midwest?

                - **jefftk** · [2022-11-12 23:18 UTC](https://news.ycombinator.com/item?id=33578210)
                  Yes, several times, touring with my (niche) band. ^c33578210

                  But I acknowledge that "people who go to contra dances" is not a uniform sampling of the population.

              - **lucb1e** · [2022-11-12 23:03 UTC](https://news.ycombinator.com/item?id=33578081)
                Sounds like nothing (zero) went missing in GP's calculation. ^c33578081

    - **xenonite** · [2022-11-12 21:37 UTC](https://news.ycombinator.com/item?id=33577357)
      Plants increase CO2 levels at night, though. Photosynthesis unavailable then, thus they use dark breathing, setting free CO2. ^c33577357

      - **jefftk** · [2022-11-12 21:44 UTC](https://news.ycombinator.com/item?id=33577416)
        I think maybe some plants do their carbon fixation at night? [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC540897/](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC540897/>) ^c33577416

    - **rufus\_foreman** · [2022-11-12 21:16 UTC](https://news.ycombinator.com/item?id=33577177)
      Is that a thing? Like a CO2 scrubber you can run at home? ^c33577177

      That's what I want.

      - **Reason077** · [2022-11-12 22:30 UTC](https://news.ycombinator.com/item?id=33577815)
        What you really want is a heat exchange / heat recovery ventilation system. Brings in fresh, filtered air from outside, and warms it up by swapping heat with the stale, warm air that it removes. ^c33577815

        - **rufus\_foreman** · [2022-11-12 22:54 UTC](https://news.ycombinator.com/item?id=33577994)
          If the air comes from outside, it's 450 ppm CO2. I want 330 ppm CO2. ^c33577994

          Is that possible?

          - **ThrowawayTestr** · [2022-11-12 23:27 UTC](https://news.ycombinator.com/item?id=33578285)
            Yes it is possible but you won't find a scrubber on Amazon. ^c33578285

            - **rufus\_foreman** · [2022-11-13 00:53 UTC](https://news.ycombinator.com/item?id=33578836)
              Why not? ^c33578836

              That's exactly what I want.

              I have money.

              - **ThrowawayTestr** · [2022-11-13 01:31 UTC](https://news.ycombinator.com/item?id=33579028)
                Because there isn't a market for home CO2 scrubbers. ^c33579028

                Here's a company that sells them.

                [https://www.alfaintek.com/products/air-scrubber/](<https://www.alfaintek.com/products/air-scrubber/>)

                - **rufus\_foreman** · [2022-11-13 02:46 UTC](https://news.ycombinator.com/item?id=33579442)
                  "As low as 400 ppm". ^c33579442

                  I want 330.

                  - **pifm\_guy** · [2022-11-13 03:41 UTC](https://news.ycombinator.com/item?id=33579775)
                    CO2 scrubbers exist.   They're commonly used by deep water divers and as part of anaesthesia equipment in hospitals. ^c33579775

                    If you're happy to do DIY stuff, I'm sure you could buy some and hook it up in your house.

                    Some things to beware of:

                    \* CO2 scrubbers can turn some not-very-dangerous pollutants into highly toxic compounds.   There are various papers suggesting that they seriously impact the mental health of people undergoing surgery for example.

                    \* You need a *lot* of CO2 scrubbing to have any impact.   Unless you need a wheelbarrow when you're changing the filters each week, your filter is probably too small for a typical house.

                  - **ThrowawayTestr** · [2022-11-13 04:16 UTC](https://news.ycombinator.com/item?id=33579971)
                    There's no pleasing you is there? ^c33579971

      - **ThrowawayTestr** · [2022-11-12 21:18 UTC](https://news.ycombinator.com/item?id=33577191)
        They exist but you'd have to contact a commercial HVAC supplier. Easier just to get a bunch of plants. ^c33577191

        - **MertsA** · [2022-11-13 10:27 UTC](https://news.ycombinator.com/item?id=33581750)
          There's not an HVAC vendor on the planet selling a CO2 scrubber for a building. All commercial HVAC manages CO2 levels via ventilation with outside air. They'll often use economizers and such to avoid losing all the energy put into conditioning the air for heat and humidity but none of them can ever bring CO2 levels down below outside atmospheric conditions. ^c33581750

          The only HVAC applications that actually try to reduce CO2 instead of just ventilate are submarines and spacecraft, so good luck trying to make that practical for a house. If I for some reason wanted to try something crazy like this I'd probably look at some of the carbonate solution carbon capture projects out there and try to make that work.

          As others have already pointed out, plants are a bit of a fools errand here. You'd need to live inside a large greenhouse.

          - **ThrowawayTestr** · [2022-11-13 17:48 UTC](https://news.ycombinator.com/item?id=33585370)
            Ok, not HVAC. But air scrubbers exist. ^c33585370

            [https://www.alfaintek.com/products/air-scrubber/](<https://www.alfaintek.com/products/air-scrubber/>)

  - **tpmx** · [2022-11-12 21:02 UTC](https://news.ycombinator.com/item?id=33577046)
    \> background CO2 was around 330 ppm. ^c33577046

    When were you born and where did you get that number from?

    - **rufus\_foreman** · [2022-11-12 21:04 UTC](https://news.ycombinator.com/item?id=33577057)
      Around 50 years ago. I was looking at this chart: [https://www.climate.gov/news-features/understanding-climate/...](<https://www.climate.gov/news-features/understanding-climate/climate-change-atmospheric-carbon-dioxide>) ^c33577057

      - **tpmx** · [2022-11-12 21:09 UTC](https://news.ycombinator.com/item?id=33577107)
        thanks! ^c33577107

  - **kragen** · [2022-11-13 19:14 UTC](https://news.ycombinator.com/item?id=33586338)
    *yes* ^c33586338

    but it's nontrivial

    whitewash curing (lime carbonatation) is the easiest process and the one most used in scuba, anesthesia, and hyperbaric chambers; though it's less energy efficient and involves higher temperatures than amine scrubbers, you can hopefully outsource that part of the process to something outside your house

    the overall reaction is

    cao + co₂ → caco₃

    caco₃ is 44\% co₂ by weight so each kg of co₂ you remove from the air consumes 1.27 kg of quicklime and creates 2.27 kg of chalk

    with only water as a catalyst this typically takes about three months; without even water it takes about three years.  as i understand it, with a few percent of lye as a catalyst it can be complete in under a second, which is how soda-lime cartridges for scuba rebreathers work

    suppose your house is sealed except for 100 ℓ/s ventilation (212 cfm in medieval units).  you're going to be exhaling into it, so maybe you want to reduce the co₂ content from 420 ppm (duude) to 250 ppm, 40\%, so you run 40\% of the air through a lime scrubber, 40 ℓ/s, which outputs effectively co₂-free air

    this intake scrubber has to soak up 17 mℓ co₂ per second (420 ppmv of 40 ℓ/s); at 1 atm and 20°, pv/rt gives us 7.1 millimoles per second, which turns out to be 31 mg of co₂ per second, about 2.7 kg co₂ per day, consuming 3.4 kg per day of quicklime and producing 6.1 kg per day of chalk

    if you're doing this without an alkali catalyst you probably need about 300–400 kg of slaked lime (whitewash or whatever) exposed to air.  if we roughly estimate that as 200 ℓ at a 1-mm-thick paint layer it's 200 m² of freshly whitewashed walls.  this will probably occupy a cubic meter or two in your house.  soda-lime is probably a better option

    either way you're left with about 190 kg per month of chalk waste (maybe with sodium carbonate in it) that you need to dispose of and replace with a bit over 100 kg per month of quicklime.  you could conceivably handle this yourself by burning it in a lime kiln yourself a couple of times a year, but a more pragmatic approach might be to buy four 25-kg bags of quicklime every month (about US\$150) or a one-tonne pallet every 10 months.  a tonne of quicklime exposed to the atmosphere will probably absorb about a kg of co₂ per day even without water

    you can reduce this a little by reducing the flow rate but pretty soon your own co₂ breath starts to build up in the space, especially if you're getting jiggy with your husband in bed

    if instead of scrubbing your intake air you try to hermetically seal your house like a submarine you only need to remove 1 kg co₂ per day (per person) but you have some new problems

    one is that by removing 1 kg of co₂ per day from the air you are effectively removing \[edited\] 0.73 kg of oxygen from the air per day, so your oxygen concentration will fall.  when it falls by 50000 ppm (50 times through the filter) it starts to become a serious problem.  you can do things to replace the oxygen but you can't detect this problem at all without oxygen sensors and it can cause you to fall asleep and never wake up

    the other is that, with such a sealed life-support system, co₂ is far from the only gas you need to actively manage.  water vapor, h₂s from farts, methane from belches, mercaptans from bad breath, and butyric acid from your gym socks all require attention.  the life support systems on the iss are publicly documented and i recommend reading the reports to see how they deal with these issues

    on the other hand you won't be breathing diesel smoke from the semis passing by and you'll be totally set if there's a poison gas attack

    see also [https://news.ycombinator.com/item?id\=33579810](<https://news.ycombinator.com/item?id=33579810>) for the scale required to do this with a greenhouse instead of a lime scrubber, but if you garden you know that's also nontrivial

  - **batch12** · [2022-11-12 20:51 UTC](https://news.ycombinator.com/item?id=33576920)
    Open a window? ^c33576920

    - **ad404b8a372f2b9** · [2022-11-12 20:52 UTC](https://news.ycombinator.com/item?id=33576938)
      Background ppm is no longer at 330, so opening a window would not get you there. You would need to keep the window closed and remove more CO2 than you produce. ^c33576938

      - **rufus\_foreman** · [2022-11-12 21:01 UTC](https://news.ycombinator.com/item?id=33577028)
        Yeah that's my question. How would I remove more CO2 than I produce. ^c33577028

        I've got the window closed, I have a few houseplants, and I am already considering getting rid of Mr. Tiddlesworth, my cat.

        Is there some sort of machine I can buy? Like direct air capture?

        I only need this in like two rooms of the house.

        - **ad404b8a372f2b9** · [2022-11-12 21:27 UTC](https://news.ycombinator.com/item?id=33577283)
          I don't think so. I guess what you want is a CO2 scrubber like they had in Apollo 13, but I don't know of any consumer, room-scale, ones. ^c33577283

          Plants make basically no difference sadly, in my room it gets to 1600ppm in under an hour just from me and my cat Gazpacho, although I've admonished him for breathing so much.

          - **rufus\_foreman** · [2022-11-12 21:37 UTC](https://news.ycombinator.com/item?id=33577361)
            Gets to like 1200 here. ^c33577361

            I think you might have a bad cat.

            Wasn't Apollo 13 pretty much room sized?

            - **OJFord** · [2022-11-13 07:56 UTC](https://news.ycombinator.com/item?id=33580977)
              Certainly wasn't 'consumer'. ^c33580977

        - **HyperSane** · [2022-11-12 21:47 UTC](https://news.ycombinator.com/item?id=33577440)
          I will never understand how people can just get rid of their pets. ^c33577440

          - **rufus\_foreman** · [2022-11-12 22:03 UTC](https://news.ycombinator.com/item?id=33577588)
            You just drive it up to the country and open the door and let it free. You know? ^c33577588

            Like, run free!

          - **lucb1e** · [2022-11-12 23:04 UTC](https://news.ycombinator.com/item?id=33578091)
            I really don't think they were serious. ^c33578091

      - **batch12** · [2022-11-12 20:55 UTC](https://news.ycombinator.com/item?id=33576969)
        Fair point. I wonder if there is a big difference depending on where one lives. For instance, if one were to live in the country, surrounded by trees... ^c33576969

      - **stuaxo** · [2022-11-12 21:06 UTC](https://news.ycombinator.com/item?id=33577075)
        Just checked my Aranet 4, in a room no one has occupied for a few hours, it's at 497 ^c33577075

    - **layer8** · [2022-11-12 22:33 UTC](https://news.ycombinator.com/item?id=33577842)
      Unlikely: [https://imageio.forbes.com/specials-images/imageserve/629c7e...](<https://imageio.forbes.com/specials-images/imageserve/629c7ef77e1b1a5c654fcbbb/NOAA-carbon-dioxide-level/960x0.jpg>) ^c33577842

      That’s in the middle of the Pacific Ocean.

    - **pfdietz** · [2022-11-12 20:53 UTC](https://news.ycombinator.com/item?id=33576942)
      If the window opened onto 1980, sure. ^c33576942

      I guess you could try to live in a place where the plants are photosynthesizing vigorously.

      - **rufus\_foreman** · [2022-11-12 21:13 UTC](https://news.ycombinator.com/item?id=33577136)
        Is that like an actual thing? Like you would have a CO2 meter somewhere and it would be down to 330 because of all the vegetation? ^c33577136

        - **pfdietz** · [2022-11-12 21:17 UTC](https://news.ycombinator.com/item?id=33577184)
          With no wind, a corn field in full sunlight will become CO2 limited in just 10 minutes or so. ^c33577184

          - **unknown** · [2022-11-13 02:07 UTC](https://news.ycombinator.com/item?id=33579241)
            [deleted] ^c33579241

          - **MobiusHorizons** · [2022-11-12 22:01 UTC](https://news.ycombinator.com/item?id=33577562)
            That’s fascinating. How do you know? (Research? Personal experience?) ^c33577562

            - **pfdietz** · [2022-11-12 22:31 UTC](https://news.ycombinator.com/item?id=33577827)
              I was told that, but I can't find a link for that specific claim.  However, I can find a link to some old research that shows CO2 falling during the day in low wind: ^c33577827

              [https://joannenova.com.au/2013/09/plants-suck-half-the-co2-o...](<https://joannenova.com.au/2013/09/plants-suck-half-the-co2-out-of-the-air-around-them-before-lunchtime-each-day/>)

              - **MobiusHorizons** · [2022-11-12 23:52 UTC](https://news.ycombinator.com/item?id=33578456)
                Thanks for digging that up. Looks very interesting. ^c33578456

                - **pfdietz** · [2022-11-13 02:43 UTC](https://news.ycombinator.com/item?id=33579424)
                  This suggests using a greenhouse to absorb CO2 to keep the air you breath fresher. ^c33579424

                  To absorb CO2 at night, plants using the CAM photosynthetic system could be used.  These plants absorb CO2 at night for use during the day, storing the CO2 temporarily as malate.

                  [https://en.wikipedia.org/wiki/Crassulacean\_acid\_metabolism](<https://en.wikipedia.org/wiki/Crassulacean_acid_metabolism>)

    - **rufus\_foreman** · [2022-11-12 20:52 UTC](https://news.ycombinator.com/item?id=33576929)
      It's 420 ppm outside now. ^c33576929

- **simonebrunozzi** · [2022-11-13 06:41 UTC](https://news.ycombinator.com/item?id=33580669)
  This topic brings up one of the biggest issues I have: I couldn't find a single, reliable CO2 monitor that I could plug and play into my home or office. ^c33580669

  I tried PurpleAir, which seemed to be quite good in this regard; but then you read reviews and tests that compare multiple sensors in the same room, and you don't know what to believe.

- **pfdietz** · [2022-11-12 20:51 UTC](https://news.ycombinator.com/item?id=33576922)
  That would be a worrying level of CO2 for the cockpit. ^c33576922

  [https://www.newsweek.com/carbon-dioxide-levels-flight-deck-a...](<https://www.newsweek.com/carbon-dioxide-levels-flight-deck-affect-airline-pilot-performance-1061068>)

- **dzhiurgis** · [2022-11-12 22:02 UTC](https://news.ycombinator.com/item?id=33577571)
  I bought Qingping and it’s best and worst purchase at the same time. On one hand it proved you need to open windows frequently and it’s cool to monitor co2 in public places. On other hand it’s depressing good ventilation won’t happen for decades if not centuries and it’s unfeasible to open windows in super cold, hot or humid climates. ^c33577571

  Also, my measurements were different from author. On a plane co2 was pretty bad until AC was turned on (usually around midway boarding), then it hovered around 1000ppm. On a train it also stayed around 1000ppm.

- **p1mrx** · [2022-11-13 03:34 UTC](https://news.ycombinator.com/item?id=33579740)
  I installed a Raspberry Pi with a CO2 sensor. When levels are high, it runs the bathroom exhaust fan to ventilate the house. ^c33579740

  Instructions and code at [https://github.com/pmarks-net/exhale](<https://github.com/pmarks-net/exhale>)

- **nicoburns** · [2022-11-12 19:35 UTC](https://news.ycombinator.com/item?id=33576256)
  Does anyone have any idea why CO2 levels would spike so high when a plane takes off? ^c33576256

  - **akira2501** · [2022-11-12 19:37 UTC](https://news.ycombinator.com/item?id=33576273)
    I'm not exactly sure,  but during take off the "packs" are typically disabled.  This removes air conditioning and probably lowers the amount of air that would be circulating when they are enabled. ^c33576273

    - **sokoloff** · [2022-11-12 19:49 UTC](https://news.ycombinator.com/item?id=33576381)
      The air cycle machine (“packs”) are turned off if maximum power is needed (as their use requires bleed air, which takes power from the engine). ^c33576381

      - **mleonhard** · [2022-11-12 20:34 UTC](https://news.ycombinator.com/item?id=33576757)
        The author's DEN-LHR flight was on a Boeing 787 aircraft, which use electrically-powered air compressors \[0\].  They do not draw air from the engine. ^c33576757

        787 maintain internal air pressure equivalent to 6,000 feet of elevation.  All other commercial aircraft maintain 8,000 feet air pressure.  I think most of my discomfort from long flights is due to altitude sickness.  The only time I have slept on a long flight and awakened refreshed was on a 787.

        Jet engines use a neuro-toxic lubricant.  Occasionally, some of this enters the cabin through the compressed air feed and poisons the passengers \[1\].  787 passengers don't have this risk because the planes don't draw air from engines.

        \[0\] [https://en.wikipedia.org/wiki/Boeing\_787\_Dreamliner\#Interior](<https://en.wikipedia.org/wiki/Boeing_787_Dreamliner#Interior>)

        \[1\] [https://pubmed.ncbi.nlm.nih.gov/24713335/](<https://pubmed.ncbi.nlm.nih.gov/24713335/>)

        - **Reason077** · [2022-11-12 22:11 UTC](https://news.ycombinator.com/item?id=33577661)
          \> *"I think most of my discomfort from long flights is due to altitude sickness."* ^c33577661

          Seems unlikely. Actual altitude sickness is generally considered to occur only above 8000 ft, and above 10000 ft is where the real risk begins. Symptoms generally don't appear until 12-24 hours after climbing to altitude. Also, risk of altitude sickness increases with physical exertion, and you're probably not doing much of that on a plane!

        - **Baeocystin** · [2022-11-12 20:55 UTC](https://news.ycombinator.com/item?id=33576968)
          I sometimes take commuter flights between San Jose and San Diego, which are almost always Southwest 737's, and I've only seen 6,000 feet on the barometer when I've checked, probably about half a dozen times out of curiosity. FWIW. ^c33576968

        - **MichaelZuo** · [2022-11-12 21:26 UTC](https://news.ycombinator.com/item?id=33577267)
          So then what explains the mysterious lack of air circulation during takeoffs on the 787? ^c33577267

          - **pifm\_guy** · [2022-11-13 03:48 UTC](https://news.ycombinator.com/item?id=33579825)
            Probably just the pilot didn't flick the switch for it while he was having his coffee break while the passengers were boarding. ^c33579825

            I'd bet if you can get a few popular newspapers to write articles about this with scary headlines ('Airline nearly suffocates passengers - and doesn't even apologize!'), then airlines will remind pilots not to do that...

            - **MichaelZuo** · [2022-11-13 04:46 UTC](https://news.ycombinator.com/item?id=33580183)
              But for half an hour? ^c33580183

              That seems like quite a long time to ignore an obvious item on the flight checklist.

        - **pistoriusp** · [2022-11-13 07:26 UTC](https://news.ycombinator.com/item?id=33580854)
          Maybe stress related? ^c33580854

  - **etrautmann** · [2022-11-12 19:49 UTC](https://news.ycombinator.com/item?id=33576380)
    Almost certainly the effect of combustion of jet fuel - which is not a good proxy for Covid risk of course. This article seems to conflate those two a bit, though the data is interesting ^c33576380

    - **jeffbee** · [2022-11-12 21:25 UTC](https://news.ycombinator.com/item?id=33577247)
      Bleed air is taken from the compressors before the combustion section, so it's probably not CO2 from combustion. If it was, it would also be humid and stink of kerosene, which it's not (cabin air is notoriously dry except on the 787) and doesn't (fuel smells in cabins have other causes). ^c33577247

      CO2 rises in the cabin during taxi because the bleed air system is not effective while the aircraft is moving slowly. This is another good feature of the 787: cabin air conditioning works adequately even with the aircraft at rest.

  - **pstrateman** · [2022-11-12 19:41 UTC](https://news.ycombinator.com/item?id=33576305)
    When planes take off there's often a strong smell of exhaust. ^c33576305

    Presumably the external air mix is just full of exhaust before they're at speed.

    - **pornel** · [2022-11-12 20:02 UTC](https://news.ycombinator.com/item?id=33576468)
      Or perhaps external air intake is closed/limited because of the smell. ^c33576468

  - **hardaker** · [2022-11-14 17:43 UTC](https://news.ycombinator.com/item?id=33597870)
    note that probably after hackernews caught the page (before all the data was in) I added a link by Boeing about this and what their belief is about CO2 levels at takeoff and in flight. ^c33597870

- **peteforde** · [2022-11-12 21:52 UTC](https://news.ycombinator.com/item?id=33577486)
  Two years ago, I was living in a house which I suspected had terrible air circulation, leading me to buy an Awair Element. It is not cheap - at \$299, a small army of RasPi hoarders will dislocate their jaws, barking with with rage - but I genuinely love it. [https://www.getawair.com/products/element](<https://www.getawair.com/products/element>) ^c33577486

  The immediate impact was that I became super nerdy about air quality, specifically CO2. It was indeed super high in that house; opening the window helped, but it led to me moving to a place with much better air quality in general. Nature in view, lots of green plants, and an HRV system. I can get \<600ppm with the windows closed.

  TL;DR: if you ponder complex things for a living, you owe it to yourself to get nerdy about CO2 in your sleep and workspaces.

- **stuaxo** · [2022-11-12 20:04 UTC](https://news.ycombinator.com/item?id=33576483)
  I need to start using my Aranet 4, which case did you buy, I already dropped mine on the floor once and it felt lucky it didn't break. ^c33576483

  - **MobiusHorizons** · [2022-11-12 22:02 UTC](https://news.ycombinator.com/item?id=33577577)
    Not the op, but it looked like the case that comes with Chinese iems (fancy earbuds) ^c33577577

    - **hardaker** · [2022-11-14 17:46 UTC](https://news.ycombinator.com/item?id=33597912)
      I am the OP :-) ^c33597912

      It's actually a "CASEMATIX Portable Credit Card Reader Case Compatible with Square Contactless and Chip Reader, Case Only", which was the best possibility I could find.  It would be nice if someone would make a dedicated case for the aranet4 as it is fairly sensitive.  I'm fairly happy with this cheap case, but I'd like something that was better fit and designed for air intake, eg.

- **ThrowawayTestr** · [2022-11-12 21:13 UTC](https://news.ycombinator.com/item?id=33577140)
  This level of obsession over covid is not healthy. ^c33577140

- **Havoc** · [2022-11-12 20:56 UTC](https://news.ycombinator.com/item?id=33576982)
  Anybody know what the actual sensor inside that device is? Spec sheet doesn't seem to say ^c33576982

  - **bloggie** · [2022-11-12 21:59 UTC](https://news.ycombinator.com/item?id=33577550)
    According to some quick duckduckgoogling for “aranet4 tear down” it could be this: [https://senseair.com/products/power-counts/sunrise-hvac/](<https://senseair.com/products/power-counts/sunrise-hvac/>) ^c33577550

    - **jobigoud** · [2022-11-13 14:50 UTC](https://news.ycombinator.com/item?id=33583545)
      Yes, the Aranet 4 is even featured on the front page of SenseAir. ^c33583545

      "We're incredibly proud to have our CO2 sensor Senseair Sunrise inside this popular product."

      The sensor itself costs \$229.00 at co2meter.com.

- **bloggie** · [2022-11-12 21:56 UTC](https://news.ycombinator.com/item?id=33577514)
  I wonder if he got COVID. ^c33577514

  - **pifm\_guy** · [2022-11-13 03:53 UTC](https://news.ycombinator.com/item?id=33579848)
    There are a bunch of other reasons to care about air quality...   Like it being a proxy for your risk of a lot of other aborne pathogens (some of which, unlike COVID, you might actually permanently avoid, rather than COVID which is so infectious that measures like this might delay you getting it by a few days but probably not more as a varient sweeps through everyone in your city). ^c33579848

  - **lucb1e** · [2022-11-12 23:07 UTC](https://news.ycombinator.com/item?id=33578116)
    Not all smokers get lung cancer, but I agree it would be funny if you appear so paranoid and then contract covid (though perhaps they have a legitimate reason to be particularly afraid of sars-cov-2, I don't know their age or comorbidities). ^c33578116

  - **hardaker** · [2022-11-14 17:34 UTC](https://news.ycombinator.com/item?id=33597702)
    Nope.  Not yet as of Monday, Nov 14th. ^c33597702

    \[who just found this discussion of my article... which started long before I finished even getting all the data on the page\]

    - **hardaker** · [2022-11-14 17:47 UTC](https://news.ycombinator.com/item?id=33597947)
      \[further note: I'm pretty consistent about using an N95 mask at nearly all times when I'm not actively eating or drinking\] ^c33597947

- **NotYourLawyer** · [2022-11-12 22:11 UTC](https://news.ycombinator.com/item?id=33577653)
  CO2 levels are interesting in their own right. But imagine being a vaccinated person, wearing N95 masks, and still being this afraid of covid. ^c33577653

  Lose the mask and hire a therapist.

  - **pifm\_guy** · [2022-11-13 03:58 UTC](https://news.ycombinator.com/item?id=33579883)
    I would like to see an analysis of this...    For example, how does wearing a mask every day impact lifetime infection risk? ^c33579883

    On one hand, masks are pretty effective at blocking pathogens.   But on the other, as the rest of the population gets infected around you, your exposure to things you haven't yet seen will get really high, so it might turn out that wearing a mask 24\*7 just delays your inevitable infection by a few days or weeks.

  - **lucb1e** · [2022-11-12 23:18 UTC](https://news.ycombinator.com/item?id=33578206)
    You don't know their age, comorbidities, or what persons they live with that might be susceptible. Plus, I find it interesting from a technical standpoint as well. My current obsession is inflation but I simply enjoy tracking different supermarket product prices and seeing what it reveals more than that I actually need to save up for any particular goal. Tracking data is also a way to pass the time on journeys. ^c33578206

    - **ThrowawayTestr** · [2022-11-12 23:29 UTC](https://news.ycombinator.com/item?id=33578300)
      They're willing to attend a convention. Safe to assume they're not immunocompromised. ^c33578300

      - **lucb1e** · [2022-11-12 23:42 UTC](https://news.ycombinator.com/item?id=33578398)
        Either that or they're trying to live a normal life while dealing with it. You're probably right on that point, though note it was only one of the possibilities mentioned. ^c33578398

- **aaron695** · [2022-11-12 22:13 UTC](https://news.ycombinator.com/item?id=33577674)
  [flagged] ^c33577674

- **thrown\_22** · [2022-11-12 21:14 UTC](https://news.ycombinator.com/item?id=33577158)
  This thread is a perfect example of why normal people don't take obvious repercussions. ^c33577158

  The covid tangent is largely bullshit. You will get it regardless of what precausiosn you take.

  The point is that in a large number of venues we have CO2 levels that are actively detrimental to your ability to think. This is a problem that we need better ventilation to solve. That bedrooms had the poorest air quality is something I wasn't expecting and will likely buy my own sensor to measure.

- **FollowingTheDao** · [2022-11-12 21:01 UTC](https://news.ycombinator.com/item?id=33577030)
  This is not going to change anytime soon. No one really cares about staying alive; climate change, diet, COVID. And COVID is now endemic and a pandemic. ^c33577030

  So either quit your job or learn about staying healthy when exposed to viruses that deplete zinc and other nutrients.

  Zinc deficiency lowers Tertrahydrobiopterin, which lowers coupled NOS, which lowers your immune system (NOS2) and gives you hypertension (NOS3) and makes you  mental (NOS1). The Lower zinc also gives you diabetes. PubMed links for anyone who cares, but you probably don't.

  - **stuaxo** · [2022-11-12 21:04 UTC](https://news.ycombinator.com/item?id=33577063)
    Please post the links, I feel like I live i a weird opposites world, where in the sane world we would have dealt with Covid by now, and have sorted out clean air in our public spaces (and to some extent homes too). ^c33577063

    - **FollowingTheDao** · [2022-11-12 21:29 UTC](https://news.ycombinator.com/item?id=33577299)
      EDITIED TO ADD: ^c33577299

      Before taking Zinc get your Serum Zinc and RBC Zinc levels tested. Easy to do in the US if you have some money.

      Also get your Serum Copper and Ceruloplasmin tested since taking zinc at high dose for a while will lower copper since zinc creates Metallothioneins that capture the copper in the intestine before it can be absorbed.

      \--

      Hey, thanks for being curious! Science!

      Zinc and Tetrahydrobipoterin:

      [https://pubmed.ncbi.nlm.nih.gov/31732151/](<https://pubmed.ncbi.nlm.nih.gov/31732151/>)

      The Gene GCH1 is central to making Tetrahydrobiopterin and uses zinc as a cofactor.

      [https://www.uniprot.org/uniprotkb/P30793/entry](<https://www.uniprot.org/uniprotkb/P30793/entry>)

      The zinc coupling of NOS via GCH1:

      [https://www.ahajournals.org/cms/asset/2cc8b7a0-a31a-4759-bc8...](<https://www.ahajournals.org/cms/asset/2cc8b7a0-a31a-4759-bc8d-da0d1f512dcf/7ff2.jpg>)

      Uncoupled NOS makes a lot of superoxides, BAD!:

      [https://www.liebertpub.com/cms/10.1089/ars.2013.5566/asset/i...](<https://www.liebertpub.com/cms/10.1089/ars.2013.5566/asset/images/medium/figure5.gif>)

      Here is a diagram of all the enzymes that need Tetrahydroibiopterin (BH4):

      [https://www.researchgate.net/figure/Metabolic-pathway-of-BH4...](<https://www.researchgate.net/figure/Metabolic-pathway-of-BH4-dopamine-serotonin-and-tyrosine_fig3_322971717>)

      NOS2 and the immune system:

      [https://pubmed.ncbi.nlm.nih.gov/24477906/](<https://pubmed.ncbi.nlm.nih.gov/24477906/>)

      [https://www.jimmunol.org/content/167/5/3000](<https://www.jimmunol.org/content/167/5/3000>)

      COVID and NOS2:

      [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7754882/](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7754882/>)

      Zinc and hypertension:

      [https://pubmed.ncbi.nlm.nih.gov/32090294/](<https://pubmed.ncbi.nlm.nih.gov/32090294/>)

      NOS3 uncoupling and hypertension:

      [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4816601/](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4816601/>)

      NOS1 and psychosis:

      [https://pubmed.ncbi.nlm.nih.gov/12140778/](<https://pubmed.ncbi.nlm.nih.gov/12140778/>)

      Zinc and Diabetes:

      [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6984028/](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6984028/>)

      [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3407731/](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3407731/>)

      And the BIG one, Zinc and Heart Arrhythmia, you know the thing that all these your people are suddenly dying with?
      [https://publichealth.jhu.edu/2022/covid-and-the-heart-it-spa...](<https://publichealth.jhu.edu/2022/covid-and-the-heart-it-spares-no-one>)

      [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7328074/](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7328074/>)

      You know, they are avoiding looking at zinc, purposefully, and I feel it is a crime against humanity. Seriously.

