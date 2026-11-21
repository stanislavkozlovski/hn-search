# [We Launched the Largest Real-Time Global CO2 Map](https://news.ycombinator.com/item?id=40834059)

Article: [https://www.airgradient.com/blog/airgradient-global-co2-map/](<https://www.airgradient.com/blog/airgradient-global-co2-map/>)

ahaucnx · 2024-06-29 23:34 UTC · 18 reported comments · archived 2026-11-08 13:35 UTC
Observation: 2026-11-08 13:35 UTC → 2026-11-08 13:35 UTC

## Comments

- **mfrankpb** · [2024-06-30 08:12 UTC](https://news.ycombinator.com/item?id=40835800)
  sensor.community is probably the larger CO2 map, as it currently has 12,236 active sensors compared to Airgradient's 500 sensors \[1\]. They also offer instructions for the construction of sensor kits or the purchase of pre-assembled units. The CCC has an interesting presentation about its mission and approach \[2\].
  How do you differentiate yourself from sensor.community? ^c40835800

  /edit: My mistake: sensor.community focuses on PM2.5 µg/m³ while you provide CO2 information. Please excuse my mistake.

  \[1\] [https://sensor.community/en/](<https://sensor.community/en/>)

  \[2\] [https://media.ccc.de/v/mch2022-213-sensor-community-global-o...](<https://media.ccc.de/v/mch2022-213-sensor-community-global-open-environmental-data-platform>)

  - **t-writescode** · [2024-06-30 09:52 UTC](https://news.ycombinator.com/item?id=40836158)
    I do notice that that website has \_\_fantastic\_\_ coverage of Germany and parts of Europe, but almost nothing in the US. I suppose things like this are very region-specific. ^c40836158

  - **ahaucnx** · [2024-06-30 08:20 UTC](https://news.ycombinator.com/item?id=40835829)
    Yes. There are many PM maps with a lot more monitors like PurpleAir map but I don't know any for CO2 comparable to what we launched. ^c40835829

- **ahaucnx** · [2024-06-30 06:40 UTC](https://news.ycombinator.com/item?id=40835510)
  Achim from AirGradient here. ^c40835510

  We are super thrilled about launching this and the examples that I describe in the blog post are quite encouraging that we can get some really useful data out of it.

  Happy to answer any questions.

  - **aydyn** · [2024-06-30 06:58 UTC](https://news.ycombinator.com/item?id=40835574)
    How do you account for inaccuracy in the measurements? I have two different sensors (from different companies) side by side. Sometimes they are spot on, but right now they are 100 ppm different. ^c40835574

    - **ahaucnx** · [2024-06-30 07:09 UTC](https://news.ycombinator.com/item?id=40835610)
      At the moment we have the automatic baseline calibration set to a default of seven days. This means the sensor modules auto calibrate to around 400ppm every week. This typically gets them very close to each other when co-located. ^c40835610

      However, as the article points out, the measurements are not reference grade and should not be taken as an absolute correct value but our tests show that the sensor modules are actually performing very well \[1\].

      Rather it is important to look at the patterns of the measurements, e.g. do they correlate with traffic patterns or wind directions (e.g. downstream from a power plant etc).

      I think the example I give in the original post about the pollution from the speed boats captures this quite well.

      We do hope that with this open-source hardware project, we can motivate much more people to build a monitor and contribute their data. Then with the growing data set there can be extremely interesting applications with machine learning and adding additional data sources like wind direction, emission inventories etc.

      The data is freely available through our public API \[2\] and if somebody wants to start modelling it, please get in touch with us. It would be great to co-operate.

      \[1\] [https://www.airgradient.com/blog/performance-of-low-cost-co2...](<https://www.airgradient.com/blog/performance-of-low-cost-co2-sensors-outdoors/>)

      \[2\] [https://api.airgradient.com/public/docs/api/v1/](<https://api.airgradient.com/public/docs/api/v1/>)

      - **t-writescode** · [2024-06-30 07:23 UTC](https://news.ycombinator.com/item?id=40835648)
        As the planet gradually climbs above 400ppm as an average - or even low - everywhere, won't that mean these sensors become less and less accurate? Is there a plan to handle that? ^c40835648

        edit: still precise, probably highly precise, but .... the mark just goes up and up?

        - **ahaucnx** · [2024-06-30 07:25 UTC](https://news.ycombinator.com/item?id=40835654)
          Yes, at some point we probably need to lift the adjustment above 400 for the automatic baseline calibration which is easily doable. ^c40835654

- **sturza** · [2024-06-30 10:36 UTC](https://news.ycombinator.com/item?id=40836360)
  Link to the actual map: [https://www.airgradient.com/map/](<https://www.airgradient.com/map/>) ^c40836360

  - **ahaucnx** · [2024-06-30 10:37 UTC](https://news.ycombinator.com/item?id=40836366)
    Use the orange button on the top left to switch to CO2. Default is PM2.5. ^c40836366

- **stemlord** · [2024-06-30 06:22 UTC](https://news.ycombinator.com/item?id=40835457)
  Maybe I'm missing this info somewhere, but would like to better understand the accuracy of the placement of the markers on the map. For example there's a 702 ppm marker in Moorestown Township NJ. Is this the exact location of one sensor, and would this then mean that some entity in Moorestown NJ is producing tons of co2? ^c40835457

  - **ahaucnx** · [2024-06-30 06:53 UTC](https://news.ycombinator.com/item?id=40835553)
    All data is crowd sourced from people that purchased our open-source outdoor monitor Open Air \[1\] either as a kit or the fully assembled version. ^c40835553

    Once the monitor is operating, the user can opt-in to make the data public and enter longitude and latitude of the location. Then it will appear as that spot on the map. If people have privacy concerns we recommend them to just move the location a bit off from their exact one.

    A level of 702ppm is not necessarily an indicator for an emission source. There are quite substantial natural diurnal cycles, especially in the country side as plants emit CO2 in the night. We have observerd peaks with up to 800ppm just based on that.

    I think a common misconception is around climate change that we believe that the 430ppm that we currently have is very constant across the atmosphere when in reality it can have substantial variations.

    \[1\] [https://www.airgradient.com/outdoor/](<https://www.airgradient.com/outdoor/>)

    - **stemlord** · [2024-07-02 01:16 UTC](https://news.ycombinator.com/item?id=40852640)
      Interesting, makes sense. Thanks ^c40852640

- **traspler** · [2024-06-30 09:37 UTC](https://news.ycombinator.com/item?id=40836101)
  I have an „older“ model of the outdoor module without the CO2 measurement (from June '23, the one with two PM2 modules) is it possible to upgrade it easily? I think mine also has a slot for a TVOC/NOx sensor but as far as I remember the sensor available on the store was not compatible due to size. Has that changed? ^c40836101

  - **ahaucnx** · [2024-06-30 09:43 UTC](https://news.ycombinator.com/item?id=40836124)
    Yes it's easy to upgrade. You can purchase the CO2 module in our online shop under the spare parts section. ^c40836124

    The CO2 module will go into one of the PM slots. So you will have a spare PM sensor.

    Feel free to also contact me through our web site support form if you have special questions on the upgrade.

- **Angostura** · [2024-06-30 10:24 UTC](https://news.ycombinator.com/item?id=40836302)
  I'm very interested in getting a sensor and taking part - but is there any information on optimum mounting position? For example, if I live in a terraced house in London with a reasonably large back garden, shoudl I be mounting on an exterior house wall? Bottom of the garden, or doesn't really matter? ^c40836302

  - **ahaucnx** · [2024-06-30 10:29 UTC](https://news.ycombinator.com/item?id=40836328)
    If possible mount it:
    \- at least 1.5m above ground to avoid dust from the ground getting into the sensor
    \- avoid proximity to HVAC system or barbecue grills etc that could influence the sensor
    \- if possible mount it in permanent shadow so that you get a relative accurate temperature reading (if needed) ^c40836328

- **grigio** · [2024-06-30 20:09 UTC](https://news.ycombinator.com/item?id=40839948)
  wow China is so clean, and also Ukraine uses green missiles ^c40839948

- **unknown** · [2024-06-30 11:12 UTC](https://news.ycombinator.com/item?id=40836534)
  [deleted] ^c40836534

