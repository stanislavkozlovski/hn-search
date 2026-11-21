# [Measuring dust with a Dylos air quality monitor (2012)](https://news.ycombinator.com/item?id=32365343)

Article: [https://woodgears.ca/dust/dylos.html](<https://woodgears.ca/dust/dylos.html>)

walterbell · 2022-08-06 06:04 UTC · 9 reported comments · archived 2026-11-08 12:16 UTC
Observation: 2026-11-08 12:16 UTC → 2026-11-08 12:16 UTC

## Comments

- **ahaucnx** · [2022-08-07 13:31 UTC](https://news.ycombinator.com/item?id=32376329)
  This article is from 2012. The Dylos was one of the first relativelely affordable PM2.5 monitors. Now we have a much higher range of pretty accurate fine dust sensors using the laser scattering method. ^c32376329

  We work a lot with the Plantower PMS5003 model (we use for our open-source DIY monitor kits) and its a very reliable module which is also used in the purple air and typically cost you around USD 15-20.

  It is important to know that these sensors are factory calibrated for specific kinds of dust, for example the "arizona road dust" and thus if you measure different kinds of dust (like the wood dust in the article), the accuracy might be off.

  Also the measurements are influenced by high humidty so it is important to use comprensation algorithms for this or preheat the air before measurements to reduce the humidity.

  - **ghostpepper** · [2022-08-07 15:56 UTC](https://news.ycombinator.com/item?id=32377424)
    Are these sensors factory calibrated? I’ve recently installed some 433 mhz accurite temperature/humidity sensors and connected them to Home Assistant. Part of why I went with consumer units as opposed to a DIY pcb was because I assumed that, while bare chips off Ali Express or DigiKey may be precise, I would have no way of knowing if they’re actually accurate. ^c32377424

    - **ahaucnx** · [2022-08-07 17:19 UTC](https://news.ycombinator.com/item?id=32378020)
      All modules we use in our DIY kits \[1\] are factory calibrated and we use the same sensor modules in our commercial sensor that went through the RESET Air certification. So these sensors are very good. We compare them side by side and see no differences in accuracy. ^c32378020

      Another important thing is the PCB and enclosure design to ensure accurate air flow to the sensors and also prevent internal heat influencing the temperature reading.

      In the DIY Pro kit we use a similar design like our commercial monitor but as a fully open sourced version. So it's very accurate.

      \[1\] [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>)

  - **porknubbins** · [2022-08-08 02:14 UTC](https://news.ycombinator.com/item?id=32381824)
    I’m confused about your comment in the third paragraph- I thought microns are microns. Could you explain how it needs to be calibrated for different types of dust? ^c32381824

  - **unknown** · [2022-08-07 16:57 UTC](https://news.ycombinator.com/item?id=32377866)
    [deleted] ^c32377866

  - **walterbell** · [2022-08-07 13:44 UTC](https://news.ycombinator.com/item?id=32376425)
    Is there a recommended sensor for particles in the range of 0.5 to 2.5 microns, like the Dylos DC1100 Pro? ^c32376425

    - **ahaucnx** · [2022-08-07 13:52 UTC](https://news.ycombinator.com/item?id=32376470)
      Some low cost sensors are offering data channels down to 0.3 microns like the Sensirion SPS30 but in my opinion most of them are tuned towards delivering the highest accuray at around 2.5PM because many standards (e.g. WHO) are based on PM2.5. ^c32376470

      - **walterbell** · [2022-08-07 14:25 UTC](https://news.ycombinator.com/item?id=32376719)
        Indeed, looks like most of the PM sensors are focused on PM2.5, a few detect PM1.0, and only the Dylos Pro attempts PM0.5-2.5, [http://www.aqmd.gov/aq-spec/evaluations/summary-pm](<http://www.aqmd.gov/aq-spec/evaluations/summary-pm>) ^c32376719

        Workshops and garages are concerned with fine dust from cutting or milling metal and wood.

        2020 paper reviewed 50 PM sensors and discussed calibration, [https://www.mdpi.com/1424-8220/20/23/6819/htm](<https://www.mdpi.com/1424-8220/20/23/6819/htm>)

        *\> We present an extensive review of the LCPMS currently available on the market, their electronic characteristics, and their applications in published literature and from specific tests. Most of the reviewed LCPMS can accurately monitor PM changes in the environment and exhibit good performances with accuracy that, in some conditions, can reach R2 values up to 0.99. However, such results strongly depend on whether the device is calibrated or not (using a reference method) in the operative environment; if not, R2 values lower than 0.5 are observed.*

        2021 Lawrence Berkeley paper, [https://escholarship.org/content/qt2fm3s5zv/qt2fm3s5zv.pdf](<https://escholarship.org/content/qt2fm3s5zv/qt2fm3s5zv.pdf>)

        *\> End-users should be made aware that the PM data from the current low-cost sensors needs to be understood as an indication of a state change or a rough estimation rather than actual concentration in indoor environments.*

- **walterbell** · [2022-08-06 06:53 UTC](https://news.ycombinator.com/item?id=32365631)
  Model with serial port, [http://www.dylosproducts.com/dcproairqumo.html](<http://www.dylosproducts.com/dcproairqumo.html>) ^c32365631

  [http://www.dylosproducts.com/toquabairpue.html](<http://www.dylosproducts.com/toquabairpue.html>)

  *\> The DC1100 is a true Laser Particle Counter that works on the same principles as the \$8,000 particle counters used in pharmaceutical and semiconductor clean rooms. Those guys really do need to know how clean their air is and they don’t use sensors like the one on your air cleaner. Those cheap sensors usually have an LED and photodiode arranged at an angle so the photodiode will pick up any light scattered back off the particles in the air. This design is inexpensive, but suffers from very poor signal to noise ratio and can only detect light scattered off many particles in a volume of air.

  \> In contrast, the DC1100 uses a focused laser which results in a drastically higher signal to noise ratio. This means that air can be flowed through a focused laser beam and the DC1100 is actually sensitive enough to detect individual particles. With this ability the DC1100 cannot only count the particles, but it can also size them based on the amount of light they scatter. For convenience sake, the DC1100 displays two particle counts – small and large. The large particle count includes pollens, dust mite debris, insect feces, coarse dust, etc. The small particle count includes most bacteria, mold, fine dust, etc. The small particle count can range from many thousands down to zero so the home owner can measure air quality with vastly greater resolution than is possible with 5 green LEDs.*

- **falcolas** · [2022-08-07 14:49 UTC](https://news.ycombinator.com/item?id=32376901)
  Meta: Jesus, this was 10 years ago? I remember it coming out, and it doesn’t feel that long ago. ^c32376901

