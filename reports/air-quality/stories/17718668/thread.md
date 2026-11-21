# [The Weight of Numbers: Air Pollution and PM2.5](https://news.ycombinator.com/item?id=17718668)

Article: [https://undark.org/breathtaking/](<https://undark.org/breathtaking/>)

anarbadalov · 2018-08-08 19:24 UTC · 67 reported comments · archived 2026-11-08 10:51 UTC
Observation: 2026-11-08 10:50 UTC → 2026-11-08 10:51 UTC

## Comments

- **anarbadalov** · [2018-08-08 20:12 UTC](https://news.ycombinator.com/item?id=17719025)
  Undark & the Pulitzer Center visited seven countries on five continents to examine the impacts of particulate pollution on the lives of everyday people, and to uncover what’s being done — or not — to address it. The project is comprised of data visualizations, short narratives, on-the-ground 360-degree videos, an explainer film, and photos from Pulitzer prizewinning photographer Larry Price. ^c17719025

  What's interesting is that PM2.5 is a measurement used by policymakers and organizations all over the world, yet the average person doesn't really know what it is, or why it matters. (I know I didn't until we began work on the project.) And it turns out that while developing nations bear the brunt of it, this kind of pollution doesn't discriminate, and it's a problem everywhere from India to Nigeria to California. In fact, a full 90\% of people live in areas that exceed World Health Organization guidelines for exposure, so the odds are high that wherever you live, you’re breathing it in, too.

  \[full disclosure: I work for Undark. We're a non-profit science and society magazine published under the auspices of the Knight Science Journalism program\]

  - **sberder** · [2018-08-09 00:08 UTC](https://news.ycombinator.com/item?id=17720724)
    A very interesting subject indeed, living in China and running a startup in that field, I find educating people is the biggest challenge of all! ^c17720724

  - **ggm** · [2018-08-09 00:14 UTC](https://news.ycombinator.com/item?id=17720756)
    Do you work with the people at QUT (Brisbane) or Floreanopolis (Brazil) doing fine particulate work near airports and in hospitals? my partner did some proofreading and english-as-a-second-language with these people, fascinating stuff (as a complete outsider) and very important. ^c17720756

    - **anarbadalov** · [2018-08-09 13:23 UTC](https://news.ycombinator.com/item?id=17723937)
      We don't. While we do often publish stories on public health issues, we don't conduct any of the research, we just report on the science. Australia and Brazil aren't regions we visited for this project, although I wouldn't be surprised to hear that there are areas experiencing extreme events in both. ^c17723937

      - **ggm** · [2018-08-09 21:28 UTC](https://news.ycombinator.com/item?id=17728665)
        Australia has a huge depndency on air and road freight with massive diesel subsidy to truckers and more air miles per Citizen than many other economies. We also have long hot dry weather. So the fine particulate matter issue here. Brazil has inadequate health funding and high humidity so gets mould.. ^c17728665

- **gh02t** · [2018-08-08 20:46 UTC](https://news.ycombinator.com/item?id=17719326)
  I recently built a sensor for particulate matter (using the Plantower PMS7003, a laser-based sensor) and it's interesting to look at the effects of every day tasks. Cooking for instance causes a huge spike in PM1.0/2.5/10.0 levels, but so do more mundane tasks like vacuuming or spraying aerosols. ^c17719326

  I'd like to add a sensor for CO2, but it's a bit more complicated. A lot of the easy to use sensors marketed for the purpose are MOX sensors and the "equivalent CO2" reading they give is pretty much a complete lie except in a very narrow range of circumstances.

  - **legulere** · [2018-08-08 20:54 UTC](https://news.ycombinator.com/item?id=17719381)
    I have a sensor built into an air purifier and have observed the same. Anything textile-related is bad like shaking out your blanket, which makes carpets seem horrible to me. But frying stuff really is the worst. You can go in the hundreds of micrograms, even with induction. ^c17719381

    A positive thing I have also learned is that opening the windows works best to get PM levels to a background level. Luckily it is only in the area of 5-20ug pm2.5 here

    For CO2 i have been recommended this one: [https://clientmedia.trade-server.net/1768\_tfadost/media/8/00...](<https://clientmedia.trade-server.net/1768_tfadost/media/8/00/1800.pdf>) which seems to measure CO2 directly.

    - **saidajigumi** · [2018-08-08 22:12 UTC](https://news.ycombinator.com/item?id=17719982)
      PM2.5 particulates are also a big problem with woodworking and other manufacturing processes.  There, having proper particulate capture (via properly designed hoods, ducting, etc.) and adequate airflow and duct design (to not restrict airflow) is critical. ^c17719982

      For kitchen use, the lessons are largely similar: you need a fume hood that's properly designed and installed, with adequate airflow (often rated in CFM in the USA) to hold and exhaust the particulates.  The particular heat source used of gas, electric, or induction, doesn't matter so much because it's the heated food, cooking oil, etc. that's throwing off the particulate matter.

      - **gascan** · [2018-08-10 19:09 UTC](https://news.ycombinator.com/item?id=17735989)
        The food is part of it, but the heat source must have some involvement. Combustion of gas produces byproducts, no way around it, and studies of camping stoves have shown the cleanliness of burn is wildly variable depending heavily on basic parameters like the shape of your cookware and the distance from the flame. ^c17735989

        (For camp stoves, the chief question is carbon monoxide production- if a stove produces low enough levels of carbon monoxide, it's safe-ish to use inside a small tent high on a mountain in a blizzard where you can't cook outside. Climbers have died of CO poisoning cooking in tents, so it is a real possibility)

    - **qiqing** · [2018-08-08 21:25 UTC](https://news.ycombinator.com/item?id=17719640)
      Do you recommend the air purifier that you have? And would you mind sharing which one has a built-in sensor? I'd like to try measuring my laundry room. ^c17719640

      - **sberder** · [2018-08-09 00:13 UTC](https://news.ycombinator.com/item?id=17720748)
        Most purifiers on the market with built-in sensors are unreliable to measure. They usually go for cheap IR sensors without flow control. Your results will vary wildly depending on conditions (temperature and humidity affect measurements a lot).
        I personally like Xiaomi purifiers for their affordability and noise level. ^c17720748

        If you're concerned about measuring pm2.5 in your space, you should consider buying a good entry level monitor like the laser egg or air visual (acquired by iqair not so long ago).

        Don't hesitate to ask more questions, air quality had been my main business for the past 4 years.

        - **roel\_v** · [2018-08-09 08:25 UTC](https://news.ycombinator.com/item?id=17722480)
          Are there air quality meters available at affordable prices (say, \<\= \$100) that can easily be integrated with home automation systems? (like, have an api, or that connect to cloud services so that I can capture the traffic?) Also, any recommendations on outdoor sensors? There have been a few crowd sourced efforts over thale last few years, but I've not been very impressed by them. ^c17722480

          - **sberder** · [2018-08-15 00:00 UTC](https://news.ycombinator.com/item?id=17762914)
            I don't know of any cheap outdoor sensors, they are more tricky than indoor as wind (air flow in the sensor), temperature, humidity and dust become more of a prominent problem.
            For a cheap sensor, laser egg publishes API endpoints to get latest data. You can also fairly easily add a plantower to an arduino/raspi kind of setup. Pantower is a sensor that will give you reliable output OOTB, can be improved but good enough. ^c17762914

        - **sundvor** · [2018-08-09 02:45 UTC](https://news.ycombinator.com/item?id=17721350)
          We have a Coway AP-1008DH, and it's interesting to see how quickly it comes on when cooking. Probably cheap sensors, but it appears to be a good device overall. ^c17721350

          I see that Air Visual ship to Australia; could this be a good way to assess the pollution levels at the school we're considering moving our son to (see my other response in this thread), or could there be cheaper options? Thanks!

          - **sberder** · [2018-08-09 04:58 UTC](https://news.ycombinator.com/item?id=17721721)
            We do work with a lot of schools here in SEA. not in Australia yet but AFAIK the market is probably not ready yet. ^c17721721

      - **oh\_sigh** · [2018-08-08 22:25 UTC](https://news.ycombinator.com/item?id=17720092)
        They are expensive, and it doesn't have a built in sensor, but I have an IQAir healthpro compact and have confirmed with my own particle detector that it filters out \> 99\% of PM0.1 particles, and 100\% of PM2.5 particles. ^c17720092

        If you don't care what it looks like, you can easily build your own air purifier for much cheaper. All it is is a blower fan which forces air through 2 or 3 filters, with the last being a HEPA filter. You can get all the requisite pieces for about \$100.

        - **rahimnathwani** · [2018-08-08 23:00 UTC](https://news.ycombinator.com/item?id=17720373)
          We use IQAir machines, too, but buy third party filters from HEPAAirDirect.com as they're cheaper than the originals, and seem very well made. And their pre-filter comes with a removable coarse dust filter. ^c17720373

          For the DIY route, these guys in Beijing sell a kit: [https://smartairfilters.com/cn/en/](<https://smartairfilters.com/cn/en/>)

        - **memonkey** · [2018-08-09 05:08 UTC](https://news.ycombinator.com/item?id=17721754)
          IQAir is just a fan, but it isn't just a HEPA filter. IIRC, the bottom filter is a large particle filter (for dust and hair), the middle filter is a carbon filter (for smoke and paint) and the third is a micro particle filter (\<2.5pm). HEPA is a loose industry standard and not everybody meets those requirements anyway. ^c17721754

          But yeah, you can easily just put a few dryer sheets on the back of your fan if all you're worried about is large dust and hair particles. The only reason to buy IQAir is if you're paranoid or severely allergic/have health problems.

  - **ridgeguy** · [2018-08-09 03:51 UTC](https://news.ycombinator.com/item?id=17721534)
    \> ...it's interesting to look at the effects of every day tasks. ^c17721534

    I suspect pretty much every task elevates PM levels.

    I made a somewhat surprising and definitely unwelcome discovery by turning off the lights in my bathroom, flushing, and shining a green laser pointer around (Rayleigh/Tyndall scattering, etc.). Followed up with the same test while scuffing my feet on carpet and doing a few other everyday activities.

    It was interesting, so I'd recommend trying it at home, but not right before dinner. Or breakfast. Or ever, if you have an overly vivid imagination.

    - **gh02t** · [2018-08-09 05:05 UTC](https://news.ycombinator.com/item?id=17721742)
      I dunno. I'm not really convinced that *all* particulates are automatically harmful at modest levels, at least not to a degree that is worth worrying about. The stuff that worries me are aerosolized modern pollutants- things like smog, glass dust from cutting fiberglass (particularly nasty stuff), and in the future potentially even new wonder materials like carbon nanotubes. ^c17721742

      An air purifier with a HEPA filter and an ionizer will take care of the majority of visible airborne household dust, if it really bothers you.

  - **clumsysmurf** · [2018-08-08 22:27 UTC](https://news.ycombinator.com/item?id=17720102)
    Are there any schematics / plans for your project? I honestly don't trust Phoenix's sensor data (many times it says things are OK - AQI is green - but just looking around you can tell its not). ^c17720102

    - **gh02t** · [2018-08-09 01:48 UTC](https://news.ycombinator.com/item?id=17721137)
      I don't have any personally, but the Plantower sensors are pretty straightforward. They just use standard UART serial, you can use an Arduino or even a simple USB-to-serial adapter, the only catch is that it must use 3.3V power and logic. Their datasheet describes how to wire them up and talk to them and you can also find plenty of code examples online. ^c17721137

      The PMS7003 is a very accurate laser based sensor with forced airflow, I trust it. Sharp also makes a much cheaper analog sensor based on IR, but I didn't get very reliable measurements from it.

      Edit: here you go [https://learn.adafruit.com/pm25-air-quality-sensor/overview](<https://learn.adafruit.com/pm25-air-quality-sensor/overview>) . Is for the PMS5003 but that's basically the same sensor.

  - **gascan** · [2018-08-08 21:53 UTC](https://news.ycombinator.com/item?id=17719831)
    Cooking with gas or electricity? ^c17719831

    I've heard before that cooking with gas causes significantly more indoor air quality problems, but I'm curious what your observations are.

    - **gh02t** · [2018-08-09 01:41 UTC](https://news.ycombinator.com/item?id=17721103)
      Cooking with gas doesn't release much particulate matter, but it does release volatile organic compounds. Most of it seems to be from the food itself; if you can smell it then there's stuff in the air. Any cooking involving oil seems to be the worst offender. ^c17721103

    - **graeme** · [2018-08-08 23:10 UTC](https://news.ycombinator.com/item?id=17720427)
      My electric stove shoots my AQI through the roof when frying. Made me consider alternate ways to cook. ^c17720427

      Though, would like to know if gas is worse, as one alternative I was considering was Donabe, which requires gas.

      - **gascan** · [2018-08-10 19:13 UTC](https://news.ycombinator.com/item?id=17736008)
        I think this is what I had originally read that made me curious. ^c17736008

        [https://www.greenbuildingadvisor.com/article/the-hazards-of-...](<https://www.greenbuildingadvisor.com/article/the-hazards-of-cooking-with-gas>)

        This talks less about particulate, it seems. Electric clearly doesn't produce carbon monoxide or nitrogen dioxide.

      - **SECProto** · [2018-08-09 02:15 UTC](https://news.ycombinator.com/item?id=17721247)
        A fume hood that keeps splatters in and vents a lot would work. I think it's just unavoidable that frying vaporizes/aerosolizes particles, so your options are either vent the contaminated air, or don't fry. ^c17721247

        - **graeme** · [2018-08-09 14:49 UTC](https://news.ycombinator.com/item?id=17724647)
          So gas that doesn't fry would be ok? Like, making a stew for example. Am wondering if the gas burning itself produces a lot of particulates. ^c17724647

          I don't think a fume hood is an option in my apartment unfortunately.

          (You can get a single gas burner to cook things in a donabe)

          - **gh02t** · [2018-08-09 15:29 UTC](https://news.ycombinator.com/item?id=17725010)
            Gas combusts pretty cleanly and doesn't release much. ^c17725010

            I personally wouldn't worry about particulates from cooking that much. Get an air purifier if you want, any decent one should be able to pull that stuff out of the air fairly quickly.

            - **graeme** · [2018-08-09 16:45 UTC](https://news.ycombinator.com/item?id=17725830)
              Well, from frying the AQI was sometimes getting as high as 400. That seems...worrisome. ^c17725830

              (More typical is 70-150, but that's usually with windows open. Harder in winter)

          - **SECProto** · [2018-08-10 09:08 UTC](https://news.ycombinator.com/item?id=17731754)
            sorry, i was commenting on the cooking technique (frying) not the heating method. Electric will create less particulate than gas, no matter how efficient the gas. frying will create more particulate than boiling, probably. if you're in Japan (guessing from the donabe reference) you'd probably be better off avoiding restaurants (with their smoking and cooking residue et al) if you're too concerned :) ^c17731754

            - **graeme** · [2018-08-14 05:08 UTC](https://news.ycombinator.com/item?id=17755705)
              Actually not in japan. Just looked like a tasty, easy way to make meals and was interested in trying it. Nut unsure of the effects of the gas burner on indoor air pollution. ^c17755705

              A quick search suggests this may be a poor idea on air quality grounds: [https://ehp.niehs.nih.gov/122-a27/](<https://ehp.niehs.nih.gov/122-a27/>)

  - **bigmit37** · [2018-08-09 00:17 UTC](https://news.ycombinator.com/item?id=17720770)
    Do you have any recommendations for sensors I can buy? I don’t know If I would be able to build one. ^c17720770

    - **gh02t** · [2018-08-09 01:52 UTC](https://news.ycombinator.com/item?id=17721154)
      Not off the top of my head, but here's a tutorial on how to build one. The Plantower sensors are pretty easy to use. ^c17721154

      [https://learn.adafruit.com/pm25-air-quality-sensor/overview](<https://learn.adafruit.com/pm25-air-quality-sensor/overview>)

- **clumsysmurf** · [2018-08-08 22:25 UTC](https://news.ycombinator.com/item?id=17720089)
  Its probably worse that it looks ^c17720089

  "Researchers from Queen Mary University of London have found that people exposed to air pollution levels well within UK guidelines have changes in the structure of the heart, similar to those seen in the early stages of heart failure."

  [https://www.sciencedaily.com/releases/2018/08/180803103315.h...](<https://www.sciencedaily.com/releases/2018/08/180803103315.htm>)

  - **sundvor** · [2018-08-09 00:36 UTC](https://news.ycombinator.com/item?id=17720863)
    That's interesting. ^c17720863

    We're looking at moving our son to a new school that's right at the corner of two major artery roads in Melbourne, with some 17 000 vehicles passing daily (just on one of them) according to VicRoads. The building doesn't appear to have a HVAC/filtration system. Playground is behind the building, but still has significant back traffic and is inside of 100-300 metres from the main roads.

    I'm saying that the fumes from the cars and trucks could likely have long term health impact, but struggling to convince wife of this - she says if it was that dangerous, then why wouldn't someone have done something about it? I must clearly be paranoid.. ?

    Personally, even though the small school appears otherwise excellent, I'm loath to expose him to these fumes.

    I seem to have acquired an ability to taste them whilst on my bicycle commute, and will don a Respro mask when riding the streets with the most backed up traffic.

    - **sberder** · [2018-08-09 04:55 UTC](https://news.ycombinator.com/item?id=17721711)
      You should be concerned as many research shows: ^c17721711

      \* leaving close to a busy road raises the risk of early dementia \[1\]

      \* higher risk of asthma

      \* cardiac arythmia

      I could go longer but don't want to get too dark

      For your situation, I think a laser egg from kaiterra is a good machine, you can bring it around and is reliable on the long run. They use a plantower sensor (mentioned in another comment) but have their own firmware on to interpret the readings. I know the founder of kaiterra personnaly so I might be biased but I'm not the only one in the industry recommending it for home use. The laser egg 2 is also measuring TVOC but is a bit more expensive, you might want to look into that. Overall a good and reliable machine for this price.

      You would also like to consider PM10 in Australia, from memory, the dryness of the country and heavy farming in certain areas was producing a lot of bigger particles.

      You can also track public data on sites like aqicn.org \[2\] or openAQ \[3\] (though the data looks sparse for Australia there).

      \[1\] [https://www.thelancet.com/journals/lancet/article/PIIS0140-6...](<https://www.thelancet.com/journals/lancet/article/PIIS0140-6736%2816%2932399-6/fulltext>)

      \[2\] [http://aqicn.org/map/\#@g/-37.8328/144.8348/11z](<http://aqicn.org/map/#@g/-37.8328/144.8348/11z>)

      \[3\] [https://openaq.org/\#/map?\_k\=ej77x9](<https://openaq.org/#/map?_k=ej77x9>)

      - **sundvor** · [2018-08-09 06:48 UTC](https://news.ycombinator.com/item?id=17722093)
        Great response, thanks very much. That's interesting how it's also been linked to cardiac arrhythmia! I'm unable to order a Laser Egg from (no Australian distributors), so would need to source an alternative - unless I go for a freight forwarder. ^c17722093

        - **sberder** · [2018-08-14 23:57 UTC](https://news.ycombinator.com/item?id=17762897)
          You could simply contact them, they're a bunch of good people, I'm sure they could make it work for you! ^c17762897

      - **ljcn** · [2018-08-09 09:19 UTC](https://news.ycombinator.com/item?id=17722698)
        Funny to see this 16-bit-plus-one range in the Laser Egg specs: ^c17722698

        \> PARTICLE COUNT

        \> 0-65536 particles / 0.1L

    - **clumsysmurf** · [2018-08-09 00:50 UTC](https://news.ycombinator.com/item?id=17720924)
      You have a legitimate concern, I've seen a few studies over the years measure VOCs as a function of distance from busy roads. Here is a very recent one: ^c17720924

      [https://www.sciencedaily.com/releases/2015/04/150421105344.h...](<https://www.sciencedaily.com/releases/2015/04/150421105344.htm>)

      [https://futurism.com/an-app-can-identify-highly-polluted-are...](<https://futurism.com/an-app-can-identify-highly-polluted-areas-in-cities/>)

      - **sundvor** · [2018-08-09 00:58 UTC](https://news.ycombinator.com/item?id=17720958)
        Thanks, greatly appreciate that. This helps fuel (no pun intended) my belief that Australia is just ignorant of such things, and that this - in addition to the fact that it's very uncomfortable data - may be why we don't "hear about it" so as to speak. ^c17720958

  - **graeme** · [2018-08-08 23:09 UTC](https://news.ycombinator.com/item?id=17720416)
    \>In the study, average annual exposures to PM2.5 were well within UK guidelines (25µg per cubic metre), although they were approaching or past World Health Organisation (WHO) guidelines (10µg per cubic metre). ^c17720416

    What AQI do these numbers translate to?

- **b\_b** · [2018-08-08 23:32 UTC](https://news.ycombinator.com/item?id=17720537)
  I'd recommend anyone who would like to clean the air of the home to use products from SmartAir \[1\] which is as inexpensive as just a fan attached to a filter, both of which they sell (although you can just buy the filter by itself and attach it to a fan you already own). I visited their office in China and received a complementary filter, which when installed in my hotel room in Beijing, definitely cleared the air and there was a noticeable difference from such a simple mechanism. Recommended for both price and effectiveness. ^c17720537

  \[1\] \= [https://smartairfilters.com/cn/en/?r\=global](<https://smartairfilters.com/cn/en/?r=global>)

  - **sberder** · [2018-08-09 00:22 UTC](https://news.ycombinator.com/item?id=17720802)
    I wouldn't, I've used their filters and followed them from the very beginning. It is an inexpensive solution but comes with its own serious flaws. They're very noisy which doesn't really work well in rooms where you actually live. They also suffer from poor CADR (Clean Air Delivery Rate) as those fans were never designed to handle high pressure differentials (before/after filter) unless you run them at full speed which is noisy. ^c17720802

    The project is interesting nonetheless, it helped demystifying purifiers and rectify the market prices in China (with other brands like Phillips and Xiaomi). Their new product for professional spaces is quite good.

  - **staikken** · [2018-08-09 01:54 UTC](https://news.ycombinator.com/item?id=17721166)
    I've worked for a company that measures PM2.5 in the past. Using a HEPA filter to remove PM2.5 seems unlikely to me. Perhaps there's something more going on here than I've picked up from a quick skim of the site (perhaps there's some sort of cyclonic separation happening) but I'm skeptical this is actually removing particulate at that scale. ^c17721166

    - **sberder** · [2018-08-09 05:05 UTC](https://news.ycombinator.com/item?id=17721743)
      I'm not sure I get what you're saying here, HEPA is a standard that was developed for medical environments & clean rooms \[1\]. To qualify as HEPA, a filter should be able to remove 99.97\% of particles 0.3µm and above so it is definitely impacting PM2.5 (particles 2.5µm and below). ^c17721743

      See my other comment \[2\] for my opinion on smartair solutions.

      \[1\] [https://en.wikipedia.org/wiki/HEPA](<https://en.wikipedia.org/wiki/HEPA>)
      \[2\] [https://news.ycombinator.com/item?id\=17720802](<https://news.ycombinator.com/item?id=17720802>)

      - **staikken** · [2018-08-09 06:25 UTC](https://news.ycombinator.com/item?id=17722000)
        I was under the impression that the filtration efficiency by particle size for such a filter was not a linear relationship.\[0\] So manufacturing to a lower bound of 3 may not say much for particles even slightly smaller. My estimation of the magnitude of this effect may be off however as this company seems to suggest. ^c17722000

        \[0\][https://www.globalspec.com/learnmore/manufacturing\_process\_e...](<https://www.globalspec.com/learnmore/manufacturing_process_equipment/filtration_separation_products/hepa_filters_ulpa_filters>)

  - **clumsysmurf** · [2018-08-09 00:01 UTC](https://news.ycombinator.com/item?id=17720682)
    Correct me if I'm wrong, but the fans in these units appear to be axial — but ideally you would want centrifugal fans for this application. ^c17720682

- **coconut\_crab** · [2018-08-09 02:25 UTC](https://news.ycombinator.com/item?id=17721278)
  I have always wondered what is the relationship between PM2.5 measurement and humidity/dew point. From what I have read all three types of PM2.5 sensors (beta ray, particle counting...) can't tell the difference between dust particles and water droplet. Googling around gives me a lot of conflicted answer\[1\]\[2\]\[3\]. ^c17721278

  If one looks at the air quality graph of my city\[0\], it can be seen that summer has much better AQI while winter/spring are worse. But I feel summer is much more dustier and spring is cleaner because the street is always wet from drizzle (dust is prevented from floating in the air). Maybe it has something to do with the lower dew point during winter/spring as my city has very high humidity, from 60\% to 100\% (right now it is 90\%).

  \[0\] [http://hanoiair.de/en\_US/](<http://hanoiair.de/en_US/>)

  \[1\] [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4555266/](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4555266/>)

  \[2\] [https://www.ncbi.nlm.nih.gov/pubmed/29063278](<https://www.ncbi.nlm.nih.gov/pubmed/29063278>)

  \[3\] [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4072227/](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4072227/>)

- **elektor** · [2018-08-08 21:00 UTC](https://news.ycombinator.com/item?id=17719431)
  Does anyone have experience with buying an air quality sensor for personal use? I know of Plume and AirBeam but have not seen them in use. ^c17719431

  - **jonathankoren** · [2018-08-08 21:44 UTC](https://news.ycombinator.com/item?id=17719775)
    I have a [https://www.purpleair.com/](<https://www.purpleair.com/>) . It measures PM 1.0, PM 2.5, and PM 10.0 . It uses the same laser scanning sensor that everyone else seems to be using, a [https://learn.adafruit.com/pm25-air-quality-sensor/overview](<https://learn.adafruit.com/pm25-air-quality-sensor/overview>) , only it has two of them. You have to plug it into the wall and it communicates over wifi. Honestly, it feels a bit mom-and-pop-ish (it's literally housed in a PVC pipe.), but it seems to work. ^c17719775

    Purple Air, talks about how it uploads everything to PurpleAir.com, but their website is really really janky. Luckily, the device has a web server, and spits out data in JSON, so even if Purple Air goes belly up, your sensor should still work.

    I have mine integrated into [http://www.weewx.com/](<http://www.weewx.com/>) via [https://github.com/bakerkj/weewx-purpleair](<https://github.com/bakerkj/weewx-purpleair>) , and I calculate an Air Quality Index from this data using [https://github.com/jonathankoren/weewx-aqi](<https://github.com/jonathankoren/weewx-aqi>) .

    Ideally, I'd like a sensor that calculated all the other pollutants you're supposed to track, but this is what I have.

    The sensor is responsive. When the smoke filtered down from the Mendocino Complex fire last week, I saw a huge spike across the particulates, and even today with the Spare The Air alert, the AQI is quite a bit elevated.

    The one thing I'll note about its performance, is that after installation, the sensor read abnormally high until the first rain. After that, its performance is on par with other surrounding sensors.

    Would I recommend it? I don't know. I feel like I should have shopped around more for one, so I can't really compare it to anything. I do like how it reports data in an open manner.

  - **oh\_sigh** · [2018-08-08 22:27 UTC](https://news.ycombinator.com/item?id=17720104)
    I have this one and it works quite well: [https://www.amazon.com/gp/product/B071RF6B2Y](<https://www.amazon.com/gp/product/B071RF6B2Y>) ^c17720104

    I compared it with a friends much more expensive device, and the results were within 5\% of each other.

    - **sonofblah** · [2018-08-08 22:50 UTC](https://news.ycombinator.com/item?id=17720288)
      None on Amazon appear to have overall high ratings. ^c17720288

      There's probably opportunity in the space for someone who can create an effective, reasonably-priced model.

      - **oh\_sigh** · [2018-08-09 01:50 UTC](https://news.ycombinator.com/item?id=17721147)
        Agreed. I was concerned about ordering mine based on the reviews, but after looking at a lot of reviews, it is because people didn't read the manual(or, couldn't understand it's Chinglish). The actual product itself works well though, and the readings were within a few percent of my friends Fluke 985(\~\$5k particle counter - because he is a HVAC professional). ^c17721147

  - **exogen** · [2018-08-09 00:31 UTC](https://news.ycombinator.com/item?id=17720843)
    I have a Foobot which is a consumer-friendly version, less like a professional instrument and more like a smart speaker. ^c17720843

    The neat thing is that it has an API, so I was able to build my own pretty dashboard showing PM, VOCs, and CO2 in my apartment.

  - **rahimnathwani** · [2018-08-08 21:07 UTC](https://news.ycombinator.com/item?id=17719485)
    A popular one among expats where I live (Beijing) is the Laser Egg. ^c17719485

- **mikeyouse** · [2018-08-08 22:35 UTC](https://news.ycombinator.com/item?id=17720169)
  Does anyone have a sense of where the damage is done regarding PM?  I live in SF and our apartment is a block away from a busy road and a gas station, both of which concern me. 
   Not to mention the wild fires of late depositing ash all over our yard.. Also, being a SF apartment, there isn't A/C so we leave the windows open on hot days. ^c17720169

  Is there data around whether an active air filter running in a closed room before we go to sleep will help? Should it just run constantly? Is there any good method to actually lower the amount of PM I'm inhaling?

  - **whatever1** · [2018-08-09 00:41 UTC](https://news.ycombinator.com/item?id=17720886)
    PM2.5 are mostly secondary organic aerosols, meaning particles that form after the reaction of other emissions. Unfortunately these can occur even with chemicals that have traveled for days and then they react with local emissions. So if you live in a forest which emitts a load of pinene and other organics and due to microclimate you receive NOX etc from a city not that nearby, boom you get very high PM2.5. ^c17720886

  - **jonathankoren** · [2018-08-08 22:59 UTC](https://news.ycombinator.com/item?id=17720367)
    Purpleair.com has a map of of sensors that update in near real time you can look at. ^c17720367

    - **mturmon** · [2018-08-09 00:35 UTC](https://news.ycombinator.com/item?id=17720860)
      That is a cool site.  I had not known there was such an extensive sensor network out there. ^c17720860

      One thing to remember about the kind of location the parent comment wrote about: particulates are very local.  Trace gases like O3 or CH4 can have very sharp spatial gradients - e.g., near highways, major streets, or dairy farms.  You can observe sharp decreases from emission levels to background levels within 10s of meters.  And PM2.5 mixes even more poorly than these trace gases, meaning PM2.5 shows sharper gradients.

      So, if you live in a built-up area and you really want to find out about PM2.5 due to your open window, or on your patio or backyard, you may need a very close-by measurement.

      You will still observe correlations between health outcomes and mean PM2.5 within, say, one 1km\^2 monitoring footprint versus an adjacent footprint.  So the background level is definitely telling you something.

  - **cyrildorsaz** · [2018-08-08 22:49 UTC](https://news.ycombinator.com/item?id=17720280)
    I bought a AirMega last year. It always runs on "quiet mode" and the PM2.5 is below 5 all the time in my 900sqf apartment. [http://airmega.com](<http://airmega.com>) ^c17720280

    - **infinite8s** · [2018-08-09 01:12 UTC](https://news.ycombinator.com/item?id=17721003)
      Does it work well for a multiroom apartment? ^c17721003

  - **deepGem** · [2018-08-08 22:50 UTC](https://news.ycombinator.com/item?id=17720294)
    You can use www.breezometer.com to check real time PM2.5 readings in your location. Based on that you can figure out whether you need an air filter or not. ^c17720294

- **alfozan** · [2018-08-09 05:33 UTC](https://news.ycombinator.com/item?id=17721816)
  Air Quality Monitors Comparison:
  [https://explorables.cmucreatelab.org/explorables/air-quality...](<https://explorables.cmucreatelab.org/explorables/air-quality-monitor-tests>) ^c17721816

- **darkhorn** · [2018-08-09 01:27 UTC](https://news.ycombinator.com/item?id=17721061)
  Enable your location in Android and then google "air pollution". It will show air poluttion in your area. ^c17721061

  - **rcMgD2BwE72F** · [2018-08-09 10:07 UTC](https://news.ycombinator.com/item?id=17722907)
    Or don't tell Google your position continuously and just type "air pollution \<city\>" ^c17722907

