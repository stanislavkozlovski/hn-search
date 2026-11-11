# [Experiments on a \$50 DIY air purifier that takes 30s to assemble](https://news.ycombinator.com/item?id=25442097)

Article: [https://dyno-might.github.io/2020/12/15/some-real-data-on-a-DIY-box-fan-air-purifier/](<https://dyno-might.github.io/2020/12/15/some-real-data-on-a-DIY-box-fan-air-purifier/>)

dyno-might · 2020-12-16 13:15 UTC · 144 reported comments · archived 2026-11-08 11:31 UTC
Observation: 2026-11-08 11:30 UTC → 2026-11-08 11:31 UTC

## Comments

- **ahaucnx** · [2020-12-17 09:18 UTC](https://news.ycombinator.com/item?id=25453948)
  We have open source, open hardware build instructions for a very reliable Air quality sensor that can be used to measure PM2.5 and also CO2. ^c25453948

  [https://www.airgradient.com/diy/](<https://www.airgradient.com/diy/>)

  We have tested it extensively and it is very accurate for the fraction of the costs of commercial sensors. You can build it for less than USD 20 and send the data to our cloud server or any other backend.

  We also measure CO2 because if you have purifiers running you often do not have enough fresh air ventilation and your CO2 often gets very high (often \>1500ppm) causing headaches and reduce cognitive performance.

  We measured this in classrooms some time ago and the results were not very good.

  Details. [https://www.airgradient.com/blog/2020/02/07/we-measured-the-...](<https://www.airgradient.com/blog/2020/02/07/we-measured-the-co2-level-in-a-classrooms-this-is-what-we-found-out/>)

  - **throwaway9d0291** · [2020-12-17 11:30 UTC](https://news.ycombinator.com/item?id=25454616)
    I've seen references to this sensor before and find it a bit concerning that there's no information about how to properly use the CO2 sensor. ^c25454616

    This sensor uses a SenseAir S8, which like most CO2 sensors, has an automatic baseline calibration algorithm enabled \[0\], which expects to see pure, undiluted fresh air at least once every 8 days. The only way to disable it is explicitly, through the MODBUS interface \[1\].

    Leaving it enabled makes perfect sense in a business or businesslike environment because these environments will be completely unoccupied overnight and have air conditioning, which usually does a daily fresh-air purge, ensuring that the sensor will have regular exposure to fresh air.

    However in a residential environment, the auto baseline calibration often doesn't make sense, especially in winter. When the windows are closed and/or people or pets are around, it's very rare for the sensor to see uncontaminated fresh air, so it will see say 500ppm of CO2 and assume it's fresh air when it really isn't. I have measured this and it's a real problem.

    In a residential environment, unless you're sure you have good, frequent exposure to pure fresh air, you're better off doing a fixed calibration once a year or so.

    AirGradient also seems to be a hardware-only design. The ESPHome project \[2\] has great software support for a variety of sensors (including the SenseAir S8, so it should be compatible with the AirGradient hardware) as well as a very well-documented hardware project \[3\]. After trying my own Arduino-based software and then ESP-IDF, I find esphome much more pleasant to work with.

    \[0\]: [https://rmtplusstoragesenseair.blob.core.windows.net/docs/pu...](<https://rmtplusstoragesenseair.blob.core.windows.net/docs/publicerat/PSP107.pdf>)

    \[1\]: [https://rmtplusstoragesenseair.blob.core.windows.net/docs/De...](<https://rmtplusstoragesenseair.blob.core.windows.net/docs/Dev/publicerat/TDE2067.pdf>)

    \[2\]: [https://esphome.io/](<https://esphome.io/>)

    \[3\]: [https://github.com/nkitanov/iaq\_board](<https://github.com/nkitanov/iaq_board>)

    - **cleorama** · [2020-12-17 23:47 UTC](https://news.ycombinator.com/item?id=25462040)
      Is there a CO2 sensor (part) and/or a CO2 monitor (device) one can buy that is well-suited for residential spaces? ^c25462040

      - **throwaway9d0291** · [2020-12-21 10:35 UTC](https://news.ycombinator.com/item?id=25493669)
        Any CO2 sensor (part) that gives you the ability to turn off ASC should work just fine and most of them do, you just need to trigger it. ^c25493669

        Personally, after trying out a bunch of sensors, I use the Sensirion SCD30.

        As for devices, I'm not aware of a consumer device that I'd recommend. If you're willing to do at least a little bit of DIY, Watterott \[0\] sells an SCD30 hooked up to an Arduino-compatible MCU with WiFi, a red/green/blue indication of CO2 levels and ASC disabled by default \[1\].

        It's an open-source hardware design and software \[2\] and has a few reference firmwares \[3\], including one \[4\] for MQTT.

        If you want to go a little bit further, I'd recommend an ESP32 with an SCD30 and ESPHome \[5\]. That's what I use myself, mostly because I already had the sensors prior to Watterott's product existing.

        \[0\]: [https://shop.watterott.com/](<https://shop.watterott.com/>)

        \[1\]: [https://shop.watterott.com/CO2-traffic-light-Plus-version-Wi...](<https://shop.watterott.com/CO2-traffic-light-Plus-version-Wifi>)

        \[2\]: [https://github.com/watterott/CO2-Ampel](<https://github.com/watterott/CO2-Ampel>)

        \[3\]: [https://learn.watterott.com/breakouts/co2-ampel/](<https://learn.watterott.com/breakouts/co2-ampel/>)

        \[4\]: [https://github.com/mariolukas/Watterott-CO2-Ampel-Plus-Firmw...](<https://github.com/mariolukas/Watterott-CO2-Ampel-Plus-Firmware>)

        \[5\]: [https://esphome.io/](<https://esphome.io/>)

  - **shared\_frog** · [2020-12-17 10:46 UTC](https://news.ycombinator.com/item?id=25454382)
    I appreciate your DIY instructions, but I really dislike how your website goes through the effort of hiding what you actually sell and also how much it costs. I don't want to "contact you" to get that information. We've been long enough in the 21st century that it has become an adult, and still I keep running into this archaic nonsense. ^c25454382

    For example, you mention your "sensor package" in the FAQ and that's it. Your DIY instructions mention the "AirGradient PCB", \_but there is no place where I can buy it\_. For the love of god, put a 'buy' button on your website.

    - **Semaphor** · [2020-12-17 11:03 UTC](https://news.ycombinator.com/item?id=25454468)
      The PCB is not sold by them, they have the Gerber files for download, and you can upload them here \[0\] to have it made and shipped to you. ^c25454468

      It seems what they are selling are consulting services with possible parts depending on the results, if you don’t want to do everything yourself.

      \[0\]: [https://jlcpcb.com](<https://jlcpcb.com>)

    - **platz** · [2020-12-17 14:06 UTC](https://news.ycombinator.com/item?id=25455654)
      Usually this means the company does not sell to consumers and is b2b only, similar to how you just can't buy something anonymously online from a wholesale distributor. ^c25455654

      - **input\_sh** · [2020-12-17 15:31 UTC](https://news.ycombinator.com/item?id=25456428)
        Usually, but you have three buttons on the first screen of their homepage: for schools, for offices, *for homes*. I don't think they're only b2b. ^c25456428

        - **nitrogen** · [2020-12-17 17:21 UTC](https://news.ycombinator.com/item?id=25457668)
          That could still be targeting manufacturers of products for those three categories. ^c25457668

        - **brudgers** · [2020-12-17 19:04 UTC](https://news.ycombinator.com/item?id=25459011)
          Volume sales “for homes”means apartments (or condos). “For Homeowners” is a different market. Usually there will be a different website for that market. It will need to mitigate “the customer is always right” attitude prevalent among consumers. ^c25459011

    - **Ottolay** · [2020-12-17 13:51 UTC](https://news.ycombinator.com/item?id=25455525)
      I would be willing to go together to have a set of PCBs if you are interested. Usually there is volume pricing. ^c25455525

      - **gh02t** · [2020-12-17 14:23 UTC](https://news.ycombinator.com/item?id=25455775)
        It might not be worth it to organize a big order nowadays, PCB fabrication is already super cheap. JLCPCB (and others, but I have the most experience with them) will do 5 boards for \$2 + shipping and the first order gets free shipping. I've used this service for prototyping many times and had great experiences. ^c25455775

        I had been planning to build almost the exact same thing as what the parent posted but had been putting it off because I didn't want to draw up a PCB, so this is perfect.

    - **xwdv** · [2020-12-17 11:06 UTC](https://news.ycombinator.com/item?id=25454478)
      They want to change what they charge from time to time so putting a price up front will force them to leave money on the table. Not gonna happen. Contact them instead. ^c25454478

      - **bigiain** · [2020-12-17 11:34 UTC](https://news.ycombinator.com/item?id=25454644)
        Instead of contacting them, I will spend a little time investigating whether there's someone else I can buy from, who doesn't consider being "forced to leave money on the table" makes this a reasonable way t treat potential customers, and will choose to spend money at a less customer hostile business - or possibly do without the product. ^c25454644

        Contacting some random "enterprise sales" team? Not gonna happen.

        - **xwdv** · [2020-12-17 11:39 UTC](https://news.ycombinator.com/item?id=25454669)
          What if they put an upfront price of \$100 dollars but cheaper prices  available if you contact them? ^c25454669

          - **oarsinsync** · [2020-12-17 14:43 UTC](https://news.ycombinator.com/item?id=25455978)
            Increasing friction is increasing friction. The GP wants to reduce friction, and your proposal likely doesn’t do that for the majority of potential customers. ^c25455978

            That said, too many people (myself included) are so used to being courted as a customer (or really, user to try and upsell to or datamine from) that we’ve forgotten that not everyone wants our business and custom.

            Splashing some cold water on your face and reminding yourself that you’re not the centre of the universe from time to time isn’t a bad habit to reduce behaving like entitled children. I still struggle with this, but baby steps... (pun not intended)

      - **newsclues** · [2020-12-17 12:48 UTC](https://news.ycombinator.com/item?id=25455071)
        Change prices?  Update the website. ^c25455071

        - **xwdv** · [2020-12-17 17:24 UTC](https://news.ycombinator.com/item?id=25457721)
          Per customer. ^c25457721

      - **quercusa** · [2020-12-17 21:34 UTC](https://news.ycombinator.com/item?id=25460756)
        When you can get quotes for satellite launches\[0\] without calling anybody, it feels like unnecessary friction at best. ^c25460756

        \[0\] [https://www.spacex.com/rideshare/](<https://www.spacex.com/rideshare/>)

        - **xwdv** · [2020-12-18 12:21 UTC](https://news.ycombinator.com/item?id=25466381)
          That’s mostly for PR. ^c25466381

  - **azmodeus** · [2020-12-17 09:38 UTC](https://news.ycombinator.com/item?id=25454048)
    It would be nice if preassembled kits could be purchased from you. I would be happy to pay USD 40 for a good preassembled kit. ^c25454048

    - **dmitriid** · [2020-12-17 10:25 UTC](https://news.ycombinator.com/item?id=25454285)
      Once you start assembling and selling these, you'll quickly realise why many things are priced the way they are. ^c25454285

      *Especially* low-volume tings like "pre-assembled DIY kits"

    - **cinntaile** · [2020-12-17 10:01 UTC](https://news.ycombinator.com/item?id=25454167)
      The BOM already costs more than USD 40 so USD 80 is probably a more realistic number for a preassembled kit. ^c25454167

      - **azmodeus** · [2020-12-17 17:00 UTC](https://news.ycombinator.com/item?id=25457435)
        Would be happy to pay USD 80 for it as well ^c25457435

    - **headmelted** · [2020-12-17 09:53 UTC](https://news.ycombinator.com/item?id=25454122)
      This.  I no longer have access to a soldering iron and want a bunch of these, not enough that it's worth the cost of buying equipment and the time spent making them. ^c25454122

      Help us give you money! :-)

      - **joshmlewis** · [2020-12-17 17:41 UTC](https://news.ycombinator.com/item?id=25457928)
        You can get good soldering irons for less than \$100. ^c25457928

        - **headmelted** · [2020-12-17 22:45 UTC](https://news.ycombinator.com/item?id=25461528)
          Yeah but I have to buy the soldering iron then spend my time figuring the kit out and doing the job. ^c25461528

          I’d be happy to pay OP for their work and everyone wins.

    - **EricE** · [2020-12-17 21:15 UTC](https://news.ycombinator.com/item?id=25460535)
      Way too low for that - good rule of thumb is 1.5x to 2.5x the cost of materials for labor if someone else is going to do it for you. ^c25460535

  - **JJMalina** · [2020-12-17 18:02 UTC](https://news.ycombinator.com/item?id=25458240)
    The Plantower PMS5003 PM Sensor is unavailable to ship to the US on aliexpress [https://www.aliexpress.com/item/32944660534.html](<https://www.aliexpress.com/item/32944660534.html>)
    Do you know of another supplier that ships to/within the US? ^c25458240

    - **phaedrus441** · [2020-12-17 19:42 UTC](https://news.ycombinator.com/item?id=25459471)
      Did you search for "PMS5003" on aliexpress? I found a few suppliers, and ordered one for \$15.81 with shipping (4.9/5 rating; 156 orders) ^c25459471

      - **JJMalina** · [2020-12-17 20:30 UTC](https://news.ycombinator.com/item?id=25459994)
        Good call, thank you! ^c25459994

    - **jeremywho** · [2020-12-17 18:42 UTC](https://news.ycombinator.com/item?id=25458736)
      I'm looking for this as well. ^c25458736

      The only think I found was [https://www.adafruit.com/product/3686](<https://www.adafruit.com/product/3686>), but thats 4x the price of aliexpress.

      - **denimnerd42** · [2020-12-18 05:30 UTC](https://news.ycombinator.com/item?id=25464190)
        [https://www.aliexpress.com/item/4001039451614.html](<https://www.aliexpress.com/item/4001039451614.html>) ^c25464190

  - **jsingleton** · [2020-12-17 10:47 UTC](https://news.ycombinator.com/item?id=25454392)
    It looks like you're using a Plantower PMS5003. I have one of those hooked up to a Raspberry Pi and it works well but I also built a few of these with ESPs: [https://sensor.community/en/sensors/airrohr/](<https://sensor.community/en/sensors/airrohr/>) ^c25454392

    They support the PMS but I used the default SDS011. They both seem reasonable for relative values but I'm not sure about the accuracy without proper calibration. They don't appear to give similar readings to my Plume Flow 2: [https://plumelabs.com/en/flow/](<https://plumelabs.com/en/flow/>)

  - **IgorPartola** · [2020-12-17 15:29 UTC](https://news.ycombinator.com/item?id=25456407)
    FYI the particle sensor link to AliExpress from that page is broken. ^c25456407

- **chopin** · [2020-12-17 09:10 UTC](https://news.ycombinator.com/item?id=25453911)
  What I am wondering about: I worked with and designed clean room equipment in the nineties. I remember that HEPA requires a considerable pressure difference which cannot be delivered by an axial fan. You'd need a radial one which can deliver a considerable differential pressure, at cost of throughput (where the axial fan shine). If you strap a HEPA to an axial fan and seal it, the fan runs effectively "empty", i.e. it displaces only little air which most likely even doesn't pass the filter. That's why HEPA filters work in vacuum cleaners since they have radial fans. I am astounded by the results of the post. ^c25453911

  I tested simply with a laser. In a normal room you can see the laser beam in dark. If you have a good purifier, you can't.

  - **yborg** · [2020-12-17 18:30 UTC](https://news.ycombinator.com/item?id=25458578)
    \>If you strap a HEPA to an axial fan and seal it, the fan runs effectively "empty", i.e. it displaces only little air which most likely even doesn't pass the filter ^c25458578

    This. I tried a 3M MERV 12 filter taped to the intake of a cheap \$12 box fan and the airflow through the fan went to effectively zero. The fan actually was pulling more air from the front of the fan around the sides of the fanbox than through the filter. Increasing the fan speed just increased this backflow. You are spot on with a radial fan being what you want here, and I notice that basically every commercial air purifier uses such a fan.

    - **EricE** · [2020-12-17 21:18 UTC](https://news.ycombinator.com/item?id=25460575)
      Radial fans are a lot quieter for the volume of air delivered too. ^c25460575

      Wish I could find a room humidifier with a radial fan but all I can find are axial fan designs :p

  - **Traubenfuchs** · [2020-12-17 11:15 UTC](https://news.ycombinator.com/item?id=25454519)
    \>  In a normal room you can see the laser beam in dark. ^c25454519

    Dear god, do you live next to a coal plant? I would argue that in a normal room one should NOT be able to see the laser beam!

    - **myself248** · [2020-12-17 14:50 UTC](https://news.ycombinator.com/item?id=25456041)
      Latch the laser beam on, aim it across the room, and go thump your hand on the couch cushions a few times. ^c25456041

    - **joncrane** · [2020-12-17 12:31 UTC](https://news.ycombinator.com/item?id=25454979)
      You'd be surprised how "dirty" (dusty) the air inside houses is. ^c25454979

      - **metiscus** · [2020-12-17 14:24 UTC](https://news.ycombinator.com/item?id=25455780)
        Especially given the relatively wide range for age and consequently construction type. I've found that newer drywall construction tends to be more dusty in my limited experience than well maintained plaster and lath. ^c25455780

        - **yborg** · [2020-12-17 18:26 UTC](https://news.ycombinator.com/item?id=25458527)
          Wall-wall carpet, especially old carpet, is a dust factory. ^c25458527

          - **metiscus** · [2020-12-17 18:41 UTC](https://news.ycombinator.com/item?id=25458727)
            My house has tile floors which get visibly filthy really quickly. I have a roomba and I personally clean the floors quite often manually. In my parents house which had wall to wall carpet, they would vacuum relatively infrequently but the same amount of dirt was likely being tracked in and around. Their house was more dusty than mine seems to be because of the fact that carpet tends to hide how "dirty" it is. ^c25458727

    - **rootusrootus** · [2020-12-17 17:10 UTC](https://news.ycombinator.com/item?id=25457538)
      Red laser, sure, but in my experience green lasers are significantly brighter and it's much easier to see the beam in clear air (though if you're human you probably need to look down the beam to spot it, my cats can see the beam horizontally and they swat at it). ^c25457538

- **Mister\_Snuggles** · [2020-12-17 13:57 UTC](https://news.ycombinator.com/item?id=25455580)
  The only downside of the DIY route is the noise.  Most box fans that I've seen are very noisy relative to "real" air cleaners/purifiers. ^c25455580

  I've used a box fan plus furnace filter for years to deal with cat litter dust.  Since the particles I want to filter are quite large, I can get away with using a fairly cheap furnace filter.  The nice thing about this is that it's really easy to scale it to your requirements.

  To deal with the noise, I used a motion sensor and switched outlet to only run it for 10 minutes after the litter has been used.  This runs through my existing home automation stuff (Home Assistant+Node-RED), but it could also be done with an Arduino (you don't even something that powerful - two I/O lines is enough), a PIR sensor, and a solid state relay for the fan control.

  I've tried a number of low-dust/no-dust litters, but most of have lead to the cats finding other places to do their business or have disappeared from store shelves when I've needed to replenish it.  Everything about this is a compromise between litter acceptance, litter availability, litter cost, filter cost, filter life, noise, and dust production.

  - **batter** · [2020-12-17 14:46 UTC](https://news.ycombinator.com/item?id=25456001)
    I'm using Vornado fan with 2 16x20x1 merv 11 filters from lowes (2 to make triangle). And in lowest speed it's very quiet. I have commercial air cleaner and my diy is way cheaper to run and as quiet.
    [https://tombuildsstuff.blogspot.com/2013/06/better-box-fan-a...](<https://tombuildsstuff.blogspot.com/2013/06/better-box-fan-air-purifier.html?m=1>) \- like this. ^c25456001

    - **Mister\_Snuggles** · [2020-12-17 16:40 UTC](https://news.ycombinator.com/item?id=25457183)
      I swear I came across that post at one point - it looks very familiar! ^c25457183

      I really want to do this because 20x25x1 filters are a LOT easier to find (where I am anyway) than 20x20x1 filters.  The only obstacle is that the resulting unit ends up taking a lot more space, and that's at a bit of a premium in the place I need it.

      If I move the litter boxes to somewhere with more space I will definitely switch to this design.

  - **unknown** · [2020-12-18 05:32 UTC](https://news.ycombinator.com/item?id=25464198)
    [deleted] ^c25464198

- **westurner** · [2020-12-17 12:24 UTC](https://news.ycombinator.com/item?id=25454934)
  From "Better Box Fan Air Purifier" [https://tombuildsstuff.blogspot.com/2013/06/better-box-fan-a...](<https://tombuildsstuff.blogspot.com/2013/06/better-box-fan-air-purifier.html>) : ^c25454934

  \> *Air purifiers can be expensive and you've probably seen articles recommending to just put a 20" x 20" x 1" furnace filter on a cheap 20" box fan and POOF! instant cleaner air for not a lot of money. It really does clean the air pretty cheap.*

  \> *There's a problem with this though. These fans weren't designed to be run with a filter. The filter will restrict air flow which will put a higher strain on the motor causing it to use more electricity and in worse cases could be a fire hazard. The higher the MERV rating (cleaning efficiency) of the filter the more stress it will put on the fan.*

  \> *Don't worry! You can still have your cheap air purifier as long as the filter area is increased to decrease the effect of air resistance. Instead of using one 20x20x1 filter we'll use two 20x25x1 filters which increases the filter surface area over 250\%. It's a little more expensive because you're using two filters instead of one but the increased filter surface area also helps the filter last longer before it gets clogged up and we're saving on energy use compared to a single filter.*

  - **ruste** · [2020-12-17 18:25 UTC](https://news.ycombinator.com/item?id=25458521)
    \> There's a problem with this though. These fans weren't designed to be run with a filter. The filter will restrict air flow which will put a higher strain on the motor causing it to use more electricity and in worse cases could be a fire hazard. The higher the MERV rating (cleaning efficiency) of the filter the more stress it will put on the fan. ^c25458521

    I'm fairly certain the opposite is true. In fact, most rowing machines work on this principle. The easiest setting is the one where the fan is as closed off as possible because it's pulling a vacuum. Less air, less resistance, easier to row / less power required to spin the fan. If anything, fans should draw less current with air flow on the inlet side restricted.

    - **westurner** · [2020-12-17 21:26 UTC](https://news.ycombinator.com/item?id=25460665)
      A. Putting two \[larger\] filters in a 'V' with cardboard to fill the top and bottom pulls the same amount of air through a larger area of filters ^c25460665

      B. pulling the same volume of air through greater surface area results in greater pressure between the filter and fan than one filter directly affixed to the fan

      C. The lower air pressure / "suction" due to an obstructed intake causes an electric fan motor to fail more quickly.

      D. Increasing the air pressure that the motor is in reduces the failure rate?

  - **rootusrootus** · [2020-12-17 16:34 UTC](https://news.ycombinator.com/item?id=25457121)
    \> we'll use two 20x25x1 filters which increases the filter surface area over 250\%. ^c25457121

    That seems like an overly complicated first attempt, why not just switch to a 20x20x4?

    - **post\_break** · [2020-12-17 16:56 UTC](https://news.ycombinator.com/item?id=25457375)
      Those can be harder to source I've found. Cheaper to use two filters than one as well since you can replaced the prefilter more often. ^c25457375

      - **rootusrootus** · [2020-12-18 02:18 UTC](https://news.ycombinator.com/item?id=25463071)
        But more difficult, yes?  Stacking filters is very different from getting a thicker filter.  The former increases air resistance, the latter decreases it.  So to get the equivalent behavior from two 20x20 filters, you'd have to device some way of routing air through both of them in parallel. ^c25463071

      - **bluGill** · [2020-12-17 21:03 UTC](https://news.ycombinator.com/item?id=25460380)
        I used a 25x20x4 which was easy to find.  Even though I didn't do anything to stop air from flowing around the backside of the filter to the fan it still gets noticeably black fast. ^c25460380

- **Rebelgecko** · [2020-12-17 05:38 UTC](https://news.ycombinator.com/item?id=25452892)
  I wish there were multiple reps of each experiment, especially with how noisy the results were and the difficulties of reproducing smoke ^c25452892

  Regardless, this project actually makes me feel better about buying my fancy air filter

  Instead of buying 2 filters (both HEPA), a fan, and a poorly calibrated air quality sensor for \$150 like the author, I bought an air purifier that contains 2 filters (1 HEPA, 1 activated charcoal) a fan and a poorly calibrated air sensor for \$153.

  However since my air quality sensor is integrated with my purifier, it only pulls \~60 watts at the times when I'm cooking or if something is on fire. That probably saves me \$50/year on electricity

  - **thomas** · [2020-12-17 14:40 UTC](https://news.ycombinator.com/item?id=25455948)
    Yeah, same thought. Something like the Coway air filter ( [https://www.youtube.com/watch?v\=zxiDrEnjYEo](<https://www.youtube.com/watch?v=zxiDrEnjYEo>) ) regularly sells for under \$200, and it is going to be much quieter than this option. It also has been tested fairly extensively from what I've seen, it's EnergyStar approved, etc, and it has a built in sensor. It doesn't look too bad either. ^c25455948

    But I understand the point, especially in times when you can't find a purifier.

    Also, good video on all this: [https://www.youtube.com/watch?v\=kH5APw\_SLUU](<https://www.youtube.com/watch?v=kH5APw_SLUU>)

    - **Rebelgecko** · [2020-12-17 18:20 UTC](https://news.ycombinator.com/item?id=25458454)
      Exactly! I have the uglier but slightly cheaper version of that air purifier (the Coway Airmega 200M). I think the faceplate is the only difference. I forgot to mention in my original comment that it also has a prefilter for larger dust particles, which I imagine probably improves the lifetime of the other filters. ^c25458454

  - **riverdroid** · [2020-12-17 20:31 UTC](https://news.ycombinator.com/item?id=25460000)
    Be aware that the air quality sensor on most units is a cheap VOC sensor. It detects gasses, not particles. It'll trigger if you fart near it or cook something odorous, but not for dust or smoke. ^c25460000

    I have the Winix 5300 and 5500 purifiers (which I highly recommend), and typically run on mode 3 out of 4 because it pulls about 12 watts (and is quiet) but is not massively different airflow than mode 4 which draws about 70 watts (and is noisy).

- **Scene\_Cast2** · [2020-12-17 16:04 UTC](https://news.ycombinator.com/item?id=25456786)
  I did a bit of experimentation with different filters for a DIY build like that. ^c25456786

  Setup: I tried out a bunch of different air filters in a medium-sized apartment. Two objectives: how fast PM2.5 is removed, and down to what level can it bring down PM2.5.

  From worst to best:

  \* Nordic Pure 20x20x4M15+C MERV 15 - the carbon layer absolutely kills airflow, doesn't work

  \* Filtrete 20x20x1, AC Furnace Air Filter, MPR 2800 / MERV 14 - works okay

  \* Nordic Pure 20x20x4 - works well

  \* Lennox Corporation X7935 20X20X5 MERV 16 - works the best. This thing is an absolute beast in terms of filtration performance; significantly lower steady-state PM2.5 readings during the California fires.

  Test equipment: Awair and Plume Flow v2.

  - **esaym** · [2020-12-17 17:11 UTC](https://news.ycombinator.com/item?id=25457547)
    I've been using the Nordic Pure filters for many years now. Way better (and cheaper) than the stuff you get at home depot, etc. ^c25457547

- **nkurz** · [2020-12-16 18:06 UTC](https://news.ycombinator.com/item?id=25445942)
  Thanks for the article! Using incense for testing seems like a good approach.  And yes, the lack of difference between "taped" and "non-taped" is definitely interesting.  I'm wondering if this might be in part because of your choice to use thin and small HEPA filters instead of the more common thicker and full size MERV filters. Intuitively, what matters is the product of the efficiency of the filter and the amount of air passing through the filter.   It's possible that because the resistance of the small HEPA filters is so high, the unfiltered air passing around the filters generates a lower pressure in front of the filter than the non-moving air after the back is taped. ^c25445942

  I recently built up a couple similar box fan filters, but using 20"x20"x5" MERV 15 filters bought "used" off Amazon for about \$20 each.  Note that the total surface area of the folded filter matters for air resistance, not just the height and width of the filter.  That is, depth matters, because all else equal the folds increase the amount of filter area.

  I sealed well, because I thought it would matter.  I removed the back plastic grill to reduce resistance a bit more, and also added a cardboard cowling on the front of the fan, based on the research here: [https://www.texairfilters.com/how-to-improve-the-efficiency-...](<https://www.texairfilters.com/how-to-improve-the-efficiency-of-the-box-fan-and-merv-13-filter-air-cleaner/>).  The idea is that with a high resistance filter on the back, in the absence of cowling you get unhelpful recirculation from the front corners of the fan, although maybe this recirculation might actually be helping reduce pressure in front of the filter in your taped example?

  I haven't done any air quality measurements, but I think the system is working the way I'd expect.   Noise at low speed is tolerable when in another room, but I only use higher speeds when leaving the house.  I'd be interested in more details about your particulate monitor, especially if you are satisfied with it and if it's available in the US.

- **WalterBright** · [2020-12-17 09:00 UTC](https://news.ycombinator.com/item?id=25453872)
  Another way to do it is to bubble the air through water. As a kid, we did an experiment where a cigarette was "smoked" by attaching a tube to the cigarette filter, the tube exited at the bottom of a flask filled with water, and a pump would suck the air from the top of the flask. ^c25453872

  It didn't take long before the water would turn black.

  Quite a turnoff for wannabee smokers, which was the obvious point of the experiment.

  It's the same idea as the Rainbow vacuum cleaner, which uses a tank of water as its filter.

  - **fencepost** · [2020-12-17 15:59 UTC](https://news.ycombinator.com/item?id=25456728)
    *Another way to do it is to bubble the air through water. As a kid, we did an experiment where a cigarette was "smoked" by attaching a tube to the cigarette filter, the tube exited at the bottom of a flask filled with water, and a pump would suck the air from the top of the flask.* ^c25456728

    "We built a bong and discovered that bong water is really nasty."

    - **WalterBright** · [2020-12-17 22:54 UTC](https://news.ycombinator.com/item?id=25461611)
      Thanks for the great laugh. I never thought of that! ^c25461611

      Just think of that nasty bong water being what the smoke does to the fluids in your lungs.

  - **archi42** · [2020-12-17 11:12 UTC](https://news.ycombinator.com/item?id=25454505)
    That's essentially a Shisha you built there, so smoking that way is a thing ;) The tobacco is different, as is the heat source, but I can confirm that the water still turns rather unpleasant. ^c25454505

- **mleonhard** · [2020-12-17 11:59 UTC](https://news.ycombinator.com/item?id=25454778)
  Any MERV8 or higher filter will work. ^c25454778

  You don't need a HEPA filter.  HEPA is only useful when you can only pass the air through the filter once, like in hospitals.  A home air filter can push the air through the filter several times, so an MERV8 is just as good as a HEPA and lasts longer.

  I used a DIY filter to remove wildfire smoke from my apartment.  It's just a 12"x12" MERV8 filter taped to the front of a small fan.  It worked well.  I periodically opened my windows to exchange the stuffy air with fresh+smokey air.  After closing the windows, the filter took about 30 minutes to remove all of the smoke inside.

- **spthorn60** · [2020-12-16 21:44 UTC](https://news.ycombinator.com/item?id=25449180)
  As most home woodworkers could confirm, a filter-on-a-box-fan works wonders in a (saw)dusty garage. Even after sanding or sawing MDF, the air is clean after about 10-15 minutes. From personal observation, I'd suggest that non-taped is a good idea, as any non-filtered air is routed through the fan to help overall circulation; ideally you want to displace all the air in the room quickly. ^c25449180

  - **StavrosK** · [2020-12-17 13:04 UTC](https://news.ycombinator.com/item?id=25455182)
    How long does it take to clear the air without the filter? I'd imagine sawdust is heavy enough to fall down on its own after a while. ^c25455182

    - **spthorn60** · [2020-12-17 13:46 UTC](https://news.ycombinator.com/item?id=25455483)
      Right the heavy stuff falls pretty quickly. The light particles will take quite a long time, and in the meantime, you're potentially breathing all that. I use a large cyclone for the machinery, a filter-on-a-fan, and a mask. My shop is a lot cleaner than it used to be, and I'm sure my lungs are too. ^c25455483

    - **bluGill** · [2020-12-17 13:36 UTC](https://news.ycombinator.com/item?id=25455401)
      Sawdust is a mix of particle sizes. [http://billpentz.com/woodworking/cyclone/beginnnerscorner.ph...](<http://billpentz.com/woodworking/cyclone/beginnnerscorner.php>) has a ton of information on sawdust. ^c25455401

- **lurkertech** · [2020-12-17 21:42 UTC](https://news.ycombinator.com/item?id=25460866)
  The OP design might see a big jump in effectiveness if they add an air guide one one or both sides of the box fan (just make a simple square cardboard tube with some tape) so that by the time the air reaches the filter, it has laminar flow.  This helped enormously in a DIY design I kludged together in Thailand (where box fans are NOT available, so I had to get something to work with regular round desk fans, which everyone already has): ^c25460866

  [https://slice-of-thai.com/air/](<https://slice-of-thai.com/air/>)

  "cannon" design (ugly but effective): [https://slice-of-thai.com/air/\#p3](<https://slice-of-thai.com/air/#p3>)

  This may also explain why the OP heard that the tape "helps" but was surprised when it didn't.  The key issue is likely not sealing with tape but rather forming an air guide.

- **cyounkins** · [2020-12-16 23:37 UTC](https://news.ycombinator.com/item?id=25450277)
  Love the testing. I think the taped/non-taped results may diverge as time goes on and the filter becomes loaded. The static pressure of air filters approximately doubles over the lifetime of the filter, and in an unconstrained system more and more air will be going around the filter instead of through it. ^c25450277

- **jsingleton** · [2020-12-17 10:50 UTC](https://news.ycombinator.com/item?id=25454413)
  There is some interesting info on building a cheap \~\$20 purifier here: [https://airpollutionguide.net/](<https://airpollutionguide.net/>) ^c25454413

  I haven't tried as cheap HEPA filters appear to be harder to get hold of in the UK. Maybe due to different heating systems.

  Clearing the Air: The Beginning and the End of Air Pollution by Tim Smedley is an excellent book if you are interested in this area.

- **konjin** · [2020-12-17 11:59 UTC](https://news.ycombinator.com/item?id=25454781)
  I build one during the forest fires earlier in the year, I bought a box fan and 6 Merv 14 furnace filters. ^c25454781

  My best idea was cutting out the front and back wall of the box the filters came with and squishing the fan between two.

  It worked well enough with the 50cm fan that it could make a 10x8m room pleasant in 10 minutes. The only improvement I would make would be buying a lower rated filter for the intake since it got clogged up with a lot of large particles that were kicked up by the fan.

  I was planning a big build with an impeller fan, but there is something to be said for a solution so stupid that I can rebuild it in 5 minutes with \$50 in parts.

- **totalZero** · [2020-12-17 09:01 UTC](https://news.ycombinator.com/item?id=25453879)
  This is nutty. I love it. ^c25453879

  The limitation for me would simply be the appearance factor; I want my filter to blend in quietly, not to draw attention. I think appearance and noise are part of why people pay so much for fancy purifiers.

  Also, I imagine a centrifugal fan would draw less electricity per CFM under load (air resistance through the filter).

  - **peteretep** · [2020-12-17 14:52 UTC](https://news.ycombinator.com/item?id=25456055)
    [https://smartairfilters.com/en/sqair/](<https://smartairfilters.com/en/sqair/>) ^c25456055

    It’s a fan + a HEPA filter and it’s kinda pretty

    - **ionwake** · [2020-12-17 17:56 UTC](https://news.ycombinator.com/item?id=25458142)
      Do you know how long the filters last? ^c25458142

      - **peteretep** · [2020-12-18 02:35 UTC](https://news.ycombinator.com/item?id=25463152)
        Depends how long you run it and on what speed. I seem to remember we were working on the basis of changing it every three months if we ran it continuously during that time ^c25463152

  - **chopin** · [2020-12-17 09:16 UTC](https://news.ycombinator.com/item?id=25453940)
    With the same throughput radial fans are much bigger than an axial fan. But they can deliver differential pressures in the range of several 100 Pa, which axial fans cannot. ^c25453940

- **infofarmer** · [2020-12-17 10:33 UTC](https://news.ycombinator.com/item?id=25454333)
  Smart Air is a whole company built around a super cheap HEPA-on-a-fan, started by foreigners in China. They still sell their old DIY1.1 model for \$35 shipped (in Mainland). I own and love their filters, although I miss the «smart» features of their competitors. ^c25454333

  [https://smartairfilters.com/en/about/our-story/](<https://smartairfilters.com/en/about/our-story/>)

- **batushka3** · [2020-12-17 17:39 UTC](https://news.ycombinator.com/item?id=25457898)
  TOP indor polution sources from my 2 year experience with concentration detector: ^c25457898

  \- frying pan with just a bit of smoke, pm 2.5/10 goes hundres easy

  \- parafin candles, HCHO formaldehyde goes over 1mg/m3 (can't tell if other are better though)

  \- presurized cans (sunscreen, desodorant, shoe care etc) pm goes hundreds easy

  \- spray surface sanitizer alcohol based, registers high folmaldehyde too

  And it's incredible how well air mixes in flat, spray in one room - few minutes later register in another. No fans needed.

- **neilv** · [2020-12-17 17:28 UTC](https://news.ycombinator.com/item?id=25457776)
  When I made one of these with a cheap box fan and a good 3M filter that covered one face completely, I ran into the airflow problem. ^c25457776

  For reasons (cheap fan with the cable and switch going in the center of the rear), I had to have the filter on the outflow side of the fan, and I was getting much more airflow back out the corners of inflow side of the fan than through the filter.

  I'm frugally-inclined, but I was desperate to clean up some nasty dust from construction work, so I ended up buying 2 Levoit air purifier appliances.  They have better airflow, and are much quieter.  They also exhaust upwards, which I guessed might be less likely to disrupt a whole lot of dust-at-rest at once.

  A problem now is not so much that the consumable filter cartridges are expensive, which I could live with if they are motivated to be high-quality, but that counterfeits are inevitable.  A related problem is that I don't have a great way to measure filter effectiveness, whether I'm buying high-quality genuine, third-party, counterfeit, or genuine facing pressure from counterfeits and seeing less value in remaining high-quality.

  - **EricE** · [2020-12-17 21:22 UTC](https://news.ycombinator.com/item?id=25460631)
    Just cut down a furnace filter to fit inside.  I’ve been doing that for years with a few Sharp units I can’t get filters for any more (discontinued) and some newer Levoits.   If you leave them running all the time on low they are more effective than running them part of the day with the “official” filters. ^c25460631

    - **neilv** · [2020-12-17 22:50 UTC](https://news.ycombinator.com/item?id=25461572)
      Good idea -- that would work for my larger Levoit unit, which takes a pair of flat rectangular filters, though not for the smaller cylindrical unit. ^c25461572

      For now, I'm going to try to keep buying the Levoit filters, since I think they have more "layers" than the furnace filters, and I don't have a good sense of what all I should to be filtering in this location.  But it's good to have a backup plan.

- **ocdtrekkie** · [2020-12-17 16:10 UTC](https://news.ycombinator.com/item?id=25456861)
  I used a 20x20x1 taped to a box fan for over a year as an air purifier because I had ferrets, and ferrets leave a particular odor floating about most of the time. ^c25456861

  I didn't want to use an odor-removing filter with charcoal on my furnace because they're super thick and put strain on the motor, and I don't care about the box fan.

  It worked really well, probably the biggest challenge was securing the filter to the fan: I put my filter on the "out" side of the fan, and it was really hard to keep it attached. Duct tape and the like actually often would fail, and air would just start moving around the filter. For good airflow through the filter I really had to give the air little other choice.

  I'm curious if it would've worked just as well had I filtered the air on the "in" side of the box fan... keeping it attached would've been much easier, but I'm not sure if there's any forces that would make "pushing" air through the filter work better than "pulling" air through the filter.

  - **rootusrootus** · [2020-12-17 16:26 UTC](https://news.ycombinator.com/item?id=25457017)
    Personally I'd do the filter on the input side of the fan.  They're designed to be pretty free flowing to begin with, since they're intended to be on the input side of the furnace blower.  It would also keep the fan itself a bit cleaner.  Suction is almost sufficient by itself to keep the filter in place. ^c25457017

    FWIW, Alton Brown made a jerky dryer using a similar technique, and he used bungee cords to hold the filters to the box fan.  That's probably less hassle than duct tape.

  - **turtlebits** · [2020-12-17 17:03 UTC](https://news.ycombinator.com/item?id=25457471)
    They sell silicon bands designed to keep the filter attached to 20" box fans.  They're \<\$10 and work well. ^c25457471

- **giantg2** · [2020-12-17 18:05 UTC](https://news.ycombinator.com/item?id=25458292)
  It could be more efficient if you use a old cardboard boxes and duct tape to build a custom fit shroud connecting/ mounting the filter to the fan. ^c25458292

  I use a similar setup on a homemade glove box / flow hood type device for culturing mushrooms. I have an 8" duct booster fan pushing air into a cardboard box. Between that box and the flow hood I have a HEPA filter sandwiched between them using bolts and wing nuts. The only thing I'd change is the fan. The booster fan was cheap, but has trouble with the back pressure (lower air flow). I would probably look at using squirrel cage or maybe a radon fan. They should be able to handle the pressure.

- **artvark11** · [2020-12-16 18:32 UTC](https://news.ycombinator.com/item?id=25446335)
  Are diy filters effective at removing smells or only removing the measurable particles? ^c25446335

  - **Traubenfuchs** · [2020-12-17 11:25 UTC](https://news.ycombinator.com/item?id=25454581)
    Smells are usually VOCs (volatile organic compound). Those need to be trapped in an active carbon filter. An alternative is to destroy them with ozone (also called "activated air", "ionized air"), but to do so one needs ozone concentrations that are unhealthy for living beings. Ozone is very unhealthy! Ozone is generated electrically or via UVC lamps. An especially common and harmful VOC, formaldehyde, can be destroyed by the extremely overpriced dyson air filters via their cryptomic technology. ^c25454581

  - **xnyan** · [2020-12-17 05:03 UTC](https://news.ycombinator.com/item?id=25452689)
    To echo everyone else, you want activated carbon. Put it in your filter stack behind the other filter and you’re golden. ^c25452689

  - **ethanwillis** · [2020-12-16 18:53 UTC](https://news.ycombinator.com/item?id=25446718)
    Not sure, but I know my commercial air filter has an optional activated charcoal filter screen in order to do smell removal. ^c25446718

    I also know that one trick to remove the smoke smell from a used car is to use an ozone generator in the car.

    - **culopatin** · [2020-12-17 15:09 UTC](https://news.ycombinator.com/item?id=25456206)
      The problem with ozone generators in cars is that they often react with some plastics and do more harm than good. Unfortunately they are the only way of getting in the nooks and crannies and inside the ac vents to clean mold and that kind of stuff. ^c25456206

      I’ve had steering wheels turn to gel using ozone and they smell funkier than what was in there.

  - **cyounkins** · [2020-12-16 23:34 UTC](https://news.ycombinator.com/item?id=25450248)
    Most things that smell are very very small particles not captured by even HEPA filters and require a different kind of filtration. Most commonly activated carbon is used, either as granule or deposited on fibers. ^c25450248

    - **rckoepke** · [2020-12-17 00:43 UTC](https://news.ycombinator.com/item?id=25450849)
      HEPA filters are actually more efficient at capturing very very small particles (\<0.1 micron) than they are at capturing simply small particles (≈0.3 micron). The tiniest particles are light enough to be captured using electrostatic forces rather than the more typical mechanical filtration that is effective at capturing large particles. ^c25450849

      More precisely, many odors are not particles at all but rather gases/vapors. Activated charcoal can capture larger organic molecules because it has an incredibly jagged/porous surface - just 100 grams of activated charcoal provides over 1,000,000 square feet of "effective" filtration surface area.

      - **cyounkins** · [2020-12-17 02:43 UTC](https://news.ycombinator.com/item?id=25451763)
        Yes, that's true that HEPA is very efficient at particles in the 0.01 to 0.1 micron range. It may also be below that, but I personally haven't seen that data. But because HEPA fails to filter gases/vapors, its performance must fall off before 1 angstrom \= 0.0001 micron. ^c25451763

        \> odors are not particles at all but rather gases/vapors

        I think the confusion comes from people referring to "particulate" as particles of \>\= 0.01 micron, whereas in physics we say that gases/vapors are also composed of particles. They may be single atoms floating (can't actually come up with an example though) or small molecules like O\^2, CO, etc, but I'd still call those particles.

        - **ClumsyPilot** · [2020-12-17 11:55 UTC](https://news.ycombinator.com/item?id=25454752)
          \> 'but I'd still call those particles' ^c25454752

          But then in your world there are no such things as gasses? If so, the world uses all usefullness

    - **xiphias2** · [2020-12-17 09:03 UTC](https://news.ycombinator.com/item?id=25453883)
      I don't know any way to filter NO2 effectively from air, and I have tried practically all commercial air filters with the largest carbon filters on the market. The worst parts of air pollution cannot be filtered out without industrial devices (that are part of the air filteration system) as far as I know. ^c25453883

      - **ddeck** · [2020-12-17 09:47 UTC](https://news.ycombinator.com/item?id=25454094)
        NO2 and other acidic gases are typically filtered using activated alumina balls impregnated with an oxidizing agent such as potassium permanganate or sodium permanganate. ^c25454094

        There are residential air purifiers available that use this in combination with activated carbon for their gas stage.

        - **xiphias2** · [2020-12-17 11:56 UTC](https://news.ycombinator.com/item?id=25454757)
          I bought IQAir and tried multiple filters (I think they use potassium permanganate), and I wasn't able to significantly reduce NO2 in my room. 3M masks similarly may work if the toxic gas concentration is far above the high levels, but I couldn't get it from normal/high to low levels. ^c25454757

          Maybe you are talking about an integrated air filtration system, as I haven't tried that yet (though I'm planning to try it).

  - **heavyset\_go** · [2020-12-17 11:04 UTC](https://news.ycombinator.com/item?id=25454475)
    I lit a candle in a room where I had one running, and the filter darkened pretty quickly. It seemed to have caught some of the smoke particles, which can be pretty small at under a micron. ^c25454475

  - **Havoc** · [2020-12-17 01:36 UTC](https://news.ycombinator.com/item?id=25451255)
    Not really. ^c25451255

    To remove smells ozone generators are used. That stuff is really dangerous though

    - **xnyan** · [2020-12-17 05:02 UTC](https://news.ycombinator.com/item?id=25452679)
      This is not correct. Activated carbon is very effective and in wide use for odor removal. ^c25452679

      - **Havoc** · [2020-12-19 19:36 UTC](https://news.ycombinator.com/item?id=25480426)
        \>This is not correct. ^c25480426

        No it's not.

        That 200 USD fine for smoking in hotel rooms? What do you think happens afterwards? Buy a bunch of activated carbon filters? Or get a professional ozone odor removal provider to roll in their with their gear?

      - **hajimemash** · [2020-12-17 10:28 UTC](https://news.ycombinator.com/item?id=25454300)
        This is correct, but this is incorrect. ^c25454300

- **acvny** · [2020-12-17 17:23 UTC](https://news.ycombinator.com/item?id=25457692)
  Wait. I did the same thing and after running the filter for several months, when I disassembled it, the filter was clean as new, but the bulk of the dust was laying somewhere between the blades and the motor and on the edges of the fan. It is very hard to actually get the right type of fan and assemble it correctly because simple fan will not work (the air will flow over the blades, thus not providing the required suction so that the air passes through the filters). The filters have pretty high resistance so you need a very efficient sucking / blowing fan to make the air pass through. ^c25457692

- **JohnJamesRambo** · [2020-12-17 11:28 UTC](https://news.ycombinator.com/item?id=25454598)
  It would be neat to see results of a good furnace filter on the fan.  Saves the cost of the bungee because the air flow holds it on pretty much, and the filters are cheaper.  It is what I use in my grow house to filter the air. ^c25454598

- **yoyman** · [2020-12-17 13:59 UTC](https://news.ycombinator.com/item?id=25455593)
  Did this with a small fan (around 6" in diameter) and it died out within a week of use. To be fair, the HEPA filter I used was really restrictive but anyone who plans to do this should probably keep that in mind. ^c25455593

- **roflchoppa3** · [2020-12-17 16:22 UTC](https://news.ycombinator.com/item?id=25456972)
  These boxfan + hepa filters seem pretty affordable, but seem to have a really strange physical footprint. Do SUV cabin fans not push enough CFM to be effective? [https://www.rockauto.com/en/moreinfo.php?pk\=10863244&cc\=1502...](<https://www.rockauto.com/en/moreinfo.php?pk=10863244&cc=1502557&jsn=822>) ^c25456972

  This paired with a filter seems like it would do the job, and based on the enclosure you might be able to have a smaller footprint. No CFM data though.

  - **UncleOxidant** · [2020-12-17 16:27 UTC](https://news.ycombinator.com/item?id=25457033)
    I think box fans are used because that's what people already have around. When wildfires rendered our air here in the PNW unbreathable last September a lot of folks were scrambling for something that would work quickly. Waiting around for an SUV cabin fan to arrive and then trying to figure out an enclosure made that a non-starter. ^c25457033

  - **bluGill** · [2020-12-17 21:08 UTC](https://news.ycombinator.com/item?id=25460443)
    They should, and probably stay closer to the rated cfm with a filter there.  However now you need a 12 volt power supply instead of plugging into a normal outlet.  Plus you need to design a housing for it. ^c25460443

    Neither of these are hard problems for DIY, but they are not nearly as easy or quick as a cheap fan and some tape.

- **igor47** · [2020-12-17 17:59 UTC](https://news.ycombinator.com/item?id=25458194)
  i am also a "fan" of the home-made air purifier. we had a bunch of them around our house over the fire season this summer. it's helpful to compare the numbers: ^c25458194

  [https://igor.moomers.org/minimal-viable-air-quality](<https://igor.moomers.org/minimal-viable-air-quality>)

  if you want to build your own monitor, i still have a bunch of PMS7003 sensors around. ping me if you want to grab one in berkeley

- **pengaru** · [2020-12-17 17:32 UTC](https://news.ycombinator.com/item?id=25457820)
  I thought an "air purifier" included VOC removal, as in had activated charcoal in the filter medium. ^c25457820

  Isn't this just an air filter if it only removes particulates?

- **textech** · [2020-12-17 15:04 UTC](https://news.ycombinator.com/item?id=25456161)
  Without an activated carbon filter on the outside to collect dust and other bigger particles your HEPA filters will be utterly useless in only a few weeks. If you keep your windows closed then I guess it could last longer but then you may have CO2 issues. ^c25456161

- **ionwake** · [2020-12-17 17:53 UTC](https://news.ycombinator.com/item?id=25458098)
  I don't mean to go against the spirit of the thread but does anyone know how these DIY compare to actual commercial products - and can anyone recommend a good air purifier?  Thank you ^c25458098

  ( I will remove this comment if it is offtopic )

  - **nkurz** · [2020-12-17 20:04 UTC](https://news.ycombinator.com/item?id=25459681)
    I think a reasonable summary is that the homemade versions are cheaper and actually more effective than most commercial versions, with the downside that they are usually larger and often noisier.  The largest factor for effective air purification is airflow, and the homemade versions offer higher airflow but at the cost of greater noise and looking janky.  There are somewhat reasonable fears that the homemade versions might be fire hazards, but in practice they are probably no more dangerous than the bare fans on which they are based.  Really, both solutions work just fine.  If looking commercial, be sure to consider the cost and availability of replacement filters.  If considering DIY, realize that you don't need to get it perfect, almost anything is better than nothing. ^c25459681

  - **hundchenkatze** · [2020-12-17 17:55 UTC](https://news.ycombinator.com/item?id=25458131)
    \> how these DIY compare to actual commercial products ^c25458131

    That's actually what this article discusses:

    "If you’re in a hurry, this post says that if you strap two HEPA filters to a box fan, it will clear the air of basically all the particles we can measure, and it will do it *faster than a commercial filter* that costs twice as much."

    - **ionwake** · [2020-12-17 17:57 UTC](https://news.ycombinator.com/item?id=25458146)
      Thank you ^c25458146

  - **EricE** · [2020-12-17 21:27 UTC](https://news.ycombinator.com/item?id=25460675)
    Radial fans (also known as squirrel cage blower, or visualize a water wheel from an old fashioned water driven flour mill) will move air more quietly than an axial fan in a box fan.  Levoit on Amazon are some great, relatively inexpensive units and when the HEPA filter it comes with needs replacing I use use furnace filters cut down to size.  If you want it to last a bit longer, you can use quilt batting as a pre-filter before the furnace filter to catch the big stuff and extend the life of the furnace filter. ^c25460675

- **dbsmith83** · [2020-12-17 17:00 UTC](https://news.ycombinator.com/item?id=25457427)
  Love the data on this experiment.  I made one of these during the wildfires, and it was apparent that it was working after just a few days.  The once colorless filter had become noticeably grey/yellowed. ^c25457427

- **leafmeal** · [2020-12-17 20:12 UTC](https://news.ycombinator.com/item?id=25459786)
  I'd like to see a control run where you don't attach a filter to the fan. ^c25459786

  My hypothesis is that it won't look very different compared to when the filter is attached (I hope I'm wrong though).

- **causality0** · [2020-12-17 15:13 UTC](https://news.ycombinator.com/item?id=25456251)
  Reading the graph, it looks like it took both purifiers a full twenty minutes to make the air as clean as it was before the fans kicked all the particles off surfaces and into the air. ^c25456251

  - **nkurz** · [2020-12-17 17:23 UTC](https://news.ycombinator.com/item?id=25457703)
    Are you making a joke, or did you perhaps miss the description of the expiriment that involves burning a piece of incense when he starts the test?  I agree though that in a more formal test, a "null" version without the incense would be a good comparison. ^c25457703

- **NietTim** · [2020-12-17 10:18 UTC](https://news.ycombinator.com/item?id=25454242)
  Interesting. I only have central ventilation but my mom has central heated air in her house, in theory she could chuck a HEPA filter in front of it to get cleaner air in all of her house. ^c25454242

  - **nkurz** · [2020-12-17 12:21 UTC](https://news.ycombinator.com/item?id=25454918)
    Note that this can be a really bad idea.   While it might temporarily improve the air quality, extreme filtration will reduce the air flow through the system.  This will in turn reduce the efficiency of the heater, possibly in a way that causes its internals to overheat and destroy themselves.   Rather than "upgrading" to higher filtration, you are safer replacing whatever filter is there with a new clean one that matches the correct specs and then adding higher quality filtration separately. ^c25454918

    - **exhilaration** · [2020-12-17 14:39 UTC](https://news.ycombinator.com/item?id=25455939)
      I've read the same thing, that if you put a heavy duty filter on your furnace you put a heavier strain on the motor and risk burning it out. I'm not an HVAC professional so research this yourself. ^c25455939

    - **NietTim** · [2020-12-17 18:15 UTC](https://news.ycombinator.com/item?id=25458397)
      This is a very good point, thanks ^c25458397

  - **dsr\_** · [2020-12-17 12:05 UTC](https://news.ycombinator.com/item?id=25454824)
    Odds are good that she has a MERV filter... and that it hasn't been changed in years. ^c25454824

    - **NietTim** · [2020-12-17 18:16 UTC](https://news.ycombinator.com/item?id=25458412)
      She probably has, but the heating module gives her a periodic reminder to clean it (which I then have to do because she can't reach it). It gets replaced every few years, I think she has a service contract :) ^c25458412

- **totetsu** · [2020-12-17 12:14 UTC](https://news.ycombinator.com/item?id=25454882)
  water filters also have the incompatible proprietary filters problem. I wanted to try filtering some water so I could make coffee that wasn't bitter but every water filter seemed to want me to buy a bunch of plastic to go around a replaceable filter. In the end I settled on pyrolysized cherry wood branches, (activated carbon, or biochar). It seems them carbonated bamboo is also used in tea making. It worked but it certainly took a long time leaving the sticks in the water. ^c25454882

  - **dole** · [2020-12-17 13:38 UTC](https://news.ycombinator.com/item?id=25455419)
    In the spirit of DIY/OSS here, I think ideally you’d want to emulate something like a Berkey water filter, these are basically just steel tanks with large threaded cylindrical charcoal filters (2” diameter, \~10” long) that use gravity to pull the water from the top to the bottom. ^c25455419

    A simple 3D printed housing filled with some charcoal/carbon media to  trickle filter like a Brita would be interesting to see its effectiveness.

    - **tk75x** · [2020-12-17 14:37 UTC](https://news.ycombinator.com/item?id=25455915)
      At my parents house, we set up a whole-house water filtration system by repurposing water softeners. empty the guts of one, refill with aquarium supply activated carbon, then adjust the electronics to your liking and you're good to go. Those systems are designed to run 24/7 and soften/filter all the water going into your house. ^c25455915

  - **bluGill** · [2020-12-17 21:13 UTC](https://news.ycombinator.com/item?id=25460504)
    There are standard sizes and housings for water filters.  No fridge uses anything standard, but you can find them.  you need some sort of plastic (or at least something food safe) around the filter though. ^c25460504

- **abyssin** · [2020-12-17 15:33 UTC](https://news.ycombinator.com/item?id=25456443)
  I tried building a similar air purifier in Belgium last year and I've never been able to source the parts at a similar cost. ^c25456443

  - **boredpudding** · [2020-12-17 15:56 UTC](https://news.ycombinator.com/item?id=25456685)
    Same problem for The Netherlands here. I just want to put a hepa filter on a fan, but unfortunately I can only find hepa filters for vacuum cleaners or existing air purifiers. ^c25456685

    If anybody has a link for where to buy a regular square/rectangle hepa filter, that would be great.

    - **bluGill** · [2020-12-17 21:12 UTC](https://news.ycombinator.com/item?id=25460486)
      This is a hepa replacement for one of the air purifiers you can buy.  Just go to the store, find an air purifier, read the back of the box to see what filter it takes, then look up/down/over a shelf - they replacement filters are generally carried in the same aisle. You will probably be surprised at just how small the filters for most of those commercial air purifiers are. ^c25460486

- **unknown** · [2020-12-17 12:26 UTC](https://news.ycombinator.com/item?id=25454949)
  [deleted] ^c25454949

- **unknown** · [2020-12-17 09:51 UTC](https://news.ycombinator.com/item?id=25454114)
  [deleted] ^c25454114

- **sal9000** · [2020-12-16 23:59 UTC](https://news.ycombinator.com/item?id=25450475)
  Nice article! Which EPA filters you ended up using? Thinking of building one myself. ^c25450475

- **jansan** · [2020-12-17 09:32 UTC](https://news.ycombinator.com/item?id=25454019)
  This is certainly done with COVID-19 in mind. Is there any source that shows how effective HEPA filters are for filtering SARS-CoV-2, given that its average size is just 130nm, which is twenty times smaller than PM2.5. ^c25454019

  - **ddeck** · [2020-12-17 10:04 UTC](https://news.ycombinator.com/item?id=25454185)
    HEPA is a bit of a loose term. It generally means 99.97\% efficiency for 0.3 micron sized particles at some particular airflow. ^c25454185

    0\.3 micron was chosen because as noted by another commenter below, high efficiency filters typically filter better at smaller sizes than this.

    A more stringent certification is EN1822, which first tests which particle size penetrates the filter the most, and then rates the efficiency based on that particle size.

    With respect to viruses, a minimum of EN1822 H14 is required for use in European biological safety cabinets. An H14 filter is 99.995\% efficient as it's most penetrating particle size (MPPS).

    That said, it's important to realize the difference between using a filter to pass air into/out of a clean environment (e.g positive/negative pressure clean room) versus just using an air purifier in a room. In the latter case, the machine is only going to filter the air going through it, and will take a significant amount of time to turn over the air in the room, during which time it's just blowing things around.

  - **mkskm** · [2020-12-17 11:07 UTC](https://news.ycombinator.com/item?id=25454485)
    The respiratory aerosols containing viruses such as COVID are typically \~3 um. See section 10.4 on this page: ^c25454485

    [https://tinyurl.com/FAQ-aerosols](<https://tinyurl.com/FAQ-aerosols>)

- **kingnothing** · [2020-12-17 18:15 UTC](https://news.ycombinator.com/item?id=25458407)
  Wirecutter also has some info on this setup compared to commercially available options. tldr: a good HEPA filter will remove 99\% of impurities, their box fan setup removed 87\%. ^c25458407

  [https://www.nytimes.com/wirecutter/reviews/best-air-purifier...](<https://www.nytimes.com/wirecutter/reviews/best-air-purifier/#what-if-you-just-put-a-furnace-filter-on-a-box-fan>)

- **nether** · [2020-12-17 14:13 UTC](https://news.ycombinator.com/item?id=25455702)
  The downside is that these filters sell out in places where there are fires. So the time to buy them is now. ^c25455702

  - **rootusrootus** · [2020-12-17 17:23 UTC](https://news.ycombinator.com/item?id=25457701)
    I agree.  When we had wildfire smoke descend on our area, the stores sold out within hours.  If you live in an area which routinely experiences wildfire smoke, it's worth stocking a few filters, both 20x20x4 for box fans and whatever size your furnace uses.  It made a huge difference to have fresh filters to swap out every few days. ^c25457701

- **kylebenzle** · [2020-12-17 08:58 UTC](https://news.ycombinator.com/item?id=25453862)
  [flagged] ^c25453862

  With Covid-19 Rates Rising Adding an Air Purifier To Your Home is the Single Most Important Thing You Can Do to Improve Your Health \[0\]

  \[0\] [https://kylebenzle.medium.com/adding-an-air-purifier-to-your...](<https://kylebenzle.medium.com/adding-an-air-purifier-to-your-home-is-the-single-most-important-thing-you-can-do-to-improve-your-4b9568c8056e>)

