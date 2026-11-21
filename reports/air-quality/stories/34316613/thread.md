# [I measured the pollution from my gas stove](https://news.ycombinator.com/item?id=34316613)

Article: [https://www.distilled.earth/p/i-measured-the-pollution-from-my](<https://www.distilled.earth/p/i-measured-the-pollution-from-my>)

jseliger · 2023-01-09 21:45 UTC · 211 reported comments · archived 2026-11-08 12:32 UTC
Observation: 2026-11-08 12:31 UTC → 2026-11-08 12:32 UTC

## Comments

- **lukev** · [2023-01-09 22:06 UTC](https://news.ycombinator.com/item?id=34316898)
  Counterpoint: I also measured the pollution from my gas stove (using the same meter the author is, from the look of the graph) and it was well within acceptable parameters. And I don't even have a vent above it. ^c34316898

  I bought a meter and started monitoring after reading an article similar to this one.

  My next stove will probably be induction, but just be aware that not ALL gas stoves are problematic if set up correctly and burning cleanly.

  Definitely get a meter to make sure, though.

  Edit: since lots of people asked, I got a uHoo sensor from Amazon. It measures basically everything and cost \$300.

  - **\_benedict** · [2023-01-09 22:38 UTC](https://news.ycombinator.com/item?id=34317431)
    NO2 is not easily measured accurately with inexpensive sensors like the uHoo. The US government tests a number of sensors and generally finds them lacking - my limited research suggests NO2 in consumer equipment is generally estimated mathematically based on correlations with other more easily measured pollutants, meaning it’s just not measuring NO2 at all. ^c34317431

    The uHoo was tested some time ago and found to not be that great, but not for NO2 (which wasn’t tested)

    [http://www.aqmd.gov/aq-spec/sensordetail/uhoo](<http://www.aqmd.gov/aq-spec/sensordetail/uhoo>)

    Indeed, as far as I can tell uHoo’s own website does not list an NO2 sensor as part of the equipment, despite listing it as a pollutant it reports:

    [https://getuhoo.com/blog/business/performance-precision-and-...](<https://getuhoo.com/blog/business/performance-precision-and-accuracy-the-technology-of-uhoo-aura-sensors/>)

    - **lukev** · [2023-01-09 22:43 UTC](https://news.ycombinator.com/item?id=34317507)
      This is the same sensor used by others who have reported high NO2 levels correlated with their gas stove burning, though, so it's got to be measuring *something* relevant. ^c34317507

      - **lukev** · [2023-01-10 03:59 UTC](https://news.ycombinator.com/item?id=34320333)
        Update: I read a tweet thread by the author of the original post, and they also used an uHoo. ^c34320333

        So if you find the "uHoo doesn't measure NO2 anyway" argument compelling, then really we're all just talking about nothing.

        - **8note** · [2023-01-10 09:10 UTC](https://news.ycombinator.com/item?id=34322241)
          False positive and false negative rates can be different. Trusting that when it says bad, it means bad can be consistent with doubting when it says good ^c34322241

          - **\_benedict** · [2023-01-10 10:11 UTC](https://news.ycombinator.com/item?id=34322671)
            Also, this is not a measurement that yields symmetric action, since it’s harmful in only one direction. Your actions based on the same level of accuracy are likely to be different. ^c34322671

            If a device can tell you something is maybe poisonous, a positive result is going to lead to very different behaviour than a negative one, even if they’re equally likely to be accurate. This is especially true when your priors (ie research with accurate devices and knowledge of combustion) lead you to expect (prior to measurement) that it will indeed be poisonous.

        - **TedDoesntTalk** · [2023-01-10 04:21 UTC](https://news.ycombinator.com/item?id=34320466)
          So how do I measure NO2 in the home and not something that “correlates”? ^c34320466

          - **\_benedict** · [2023-01-10 08:13 UTC](https://news.ycombinator.com/item?id=34321915)
            The AQMD website has tested devices, and any they found accurate is probably a good place to start. ^c34321915

            My limited research suggests the most affordable and reliable gaseous measurements like NO2 want a metal oxide sensor, which you don’t see on consumer grade equipment but is available affordably from commercial sources. It’s more hassle though so I gave up on measuring NO2 for now. Particulates seem to be readily measured with suitable accuracy by consumer grade equipment.

        - **\_benedict** · [2023-01-10 08:13 UTC](https://news.ycombinator.com/item?id=34321917)
          Yep. ^c34321917

      - **\_benedict** · [2023-01-09 23:19 UTC](https://news.ycombinator.com/item?id=34317973)
        Sure, but it’s not measuring NO2, just things that sometimes correlate with the presence of NO2 in some environment. So, maybe it’s sometimes rightish in a general ball park sense, but often it won’t even be that as these correlations are necessarily based on lots of assumptions that often don’t hold. And this is all ignoring interdevice variability which is often very high on this consumer equipment if the tests are to be believed. ^c34317973

  - **SoftTalker** · [2023-01-09 22:22 UTC](https://news.ycombinator.com/item?id=34317178)
    A good rough indicator is that the flame on a gas burner should be pure blue. If you see yellow tips, or a yellow flame, it's not getting enough oxygen for complete combustion. ^c34317178

    - **halfnormalform** · [2023-01-10 01:17 UTC](https://news.ycombinator.com/item?id=34319006)
      If you use an ultrasonic humidifier with a demineralization cartridge, it will turn your burners bright orange due to the sodium added to the air. It's not dangerous, but very disconcerting until you know what's up. ^c34319006

    - **kragen** · [2023-01-09 22:50 UTC](https://news.ycombinator.com/item?id=34317602)
      proper combustion will probably increase your nitrogen dioxide levels, not decrease them; if you have yellow diffusion tips you are getting unburned hydrocarbons and carbon monoxide which will tend to reduce any nitrogen dioxide present ^c34317602

      the carbon monoxide can kill you pretty fucking dead tho

      - **LarryMullins** · [2023-01-09 23:19 UTC](https://news.ycombinator.com/item?id=34317969)
        That's my understanding as well.   Three stage catalytic converters reduce nitrogen oxide emissions through reduction, so it makes sense that a reducing flame (oxygen starved) would produce less nitrogen oxides than an oxidizing flame. ^c34317969

        - **Gordonjcp** · [2023-01-09 23:35 UTC](https://news.ycombinator.com/item?id=34318102)
          Both my Range Rovers are converted to run on propane, and unlike on petrol the LPG system runs the engine very lean. If you use a special glass sparkplug (those old "Colortune ones!) you can see the flame is a lovely bright blue on propane and quite orange on petrol, with the mixtures set correctly. ^c34318102

          Measured at the downpipe with the sniffer in the lambda sensor hole it shows no (or almost no) CO and a bit more NOx than you'd really want, but after the cat there's no measurable NOx either. The tailpipe emits basically just warm carbon dioxide and water vapour.

          - **noyoudumbdolt** · [2023-01-10 21:39 UTC](https://news.ycombinator.com/item?id=34331898)
            \>*Both my Range Rovers are converted to run on propane* ^c34331898

            What is the downside to this? Obviously availability and ease of filling is part of it, but any other downsides?

            - **Gordonjcp** · [2023-01-11 16:28 UTC](https://news.ycombinator.com/item?id=34340271)
              There's a big metal tank where the spare wheel goes, so you lose a bit of space. Availability can be a problem occasionally, particularly where I moved to, but filling is just as easy as filling a petrol tank. ^c34340271

              In theory the engine makes a bit less power flat out, but I never drive flat out. It's quieter, runs cooler and cleaner, and has a bit more low end torque because propane burns with a bigger slower bang.

            - **kragen** · [2023-01-11 01:21 UTC](https://news.ycombinator.com/item?id=34333825)
              shorter range with the same size gas tank maybe ^c34333825

        - **kragen** · [2023-01-09 23:36 UTC](https://news.ycombinator.com/item?id=34318113)
          yes, though if it's *sufficiently* oxidizing (sufficient excess of air) the flame temperature starts to drop, which will also cut your nitrogen oxide emissions to almost zero ^c34318113

  - **wcoenen** · [2023-01-09 22:13 UTC](https://news.ycombinator.com/item?id=34317026)
    \> *I bought a meter and started monitoring after reading an article similar to this one.* ^c34317026

    Which meter? (I'm asking because I have a bad experience with a device from Aliexpress that turned out to produce fake air quality measurements. Though it did not claim to measure the NO2 pollution which the article talks about.)

    edit: the uHoo seems to be an expensive device that promises to measure a bunch of stuff, but it cannot be calibrated. I would not trust it.

  - **asveikau** · [2023-01-09 22:11 UTC](https://news.ycombinator.com/item?id=34316983)
    I think what I've heard before is that this needs regular monitoring, which most households will not do.  Stuff can break in your stove and oven and you might not know. ^c34316983

    - **RetpolineDrama** · [2023-01-09 22:32 UTC](https://news.ycombinator.com/item?id=34317345)
      \>Stuff can break in your stove and oven and you might not know. ^c34317345

      I'd argue \>99.9\% of people would have no clue if the stove was otherwise functioning normally

  - **nomel** · [2023-01-09 22:35 UTC](https://news.ycombinator.com/item?id=34317391)
    \> And I don't even have a vent above it. ^c34317391

    Where I am, this is illegal!

    I unintentionally bought a "smart" gas range. I hooked it up to turn on my oven fan any time the burners are on, and for some minutes after they're off. I t think all ovens should have this feature, built in.

    - **jjeaff** · [2023-01-10 08:09 UTC](https://news.ycombinator.com/item?id=34321894)
      Do you also have a vent that goes outside? Because an oven fan means little if you don't have external exhaust. ^c34321894

      - **jaclaz** · [2023-01-10 13:58 UTC](https://news.ycombinator.com/item?id=34324885)
        Here (Italy) there is a safety norm originally dating back to 1974 that (though a lot more complicated than this) essentially makes in any kitchen (with a gas stove) compulsory two connections (of a given size, 100 cm2, in practice a 12 cm pipe) with the outside, one at a low level for intake and one (usually it is the kitchen vent, but it could be another opening) for exhaust at a higher level (I seem to remember above 1.80 or 2.00 meters). ^c34324885

        It has to be underlined how - in practice - the actual need for such provisions was at the time perhaps a little exaggerated (as windows were usually leaky) but with the increasing use of air-tight windows (but not usually mechanical ventilation of the house) the intake and exhaust are actually needed.

      - **nomel** · [2023-01-10 20:40 UTC](https://news.ycombinator.com/item?id=34331162)
        Yes, the law requires an actual vent that removes the combustion gases from the breathing space. ^c34331162

  - **miguelazo** · [2023-01-09 22:34 UTC](https://news.ycombinator.com/item?id=34317378)
    \$300?! That's half-way to a decent induction range on sale. ^c34317378

    - **lotsofpulp** · [2023-01-09 22:45 UTC](https://news.ycombinator.com/item?id=34317534)
      The cheapest induction range at Costco is \$1,150.  I would not bother with anything that is so low quality so as to be able to be sold at half of Costco’s cheapest model. ^c34317534

      Also, hiring an electrician to install a power outlet for the induction stovetop could be at least \$500, if not \$1,000+.

      - **shaklee3** · [2023-01-10 06:19 UTC](https://news.ycombinator.com/item?id=34321194)
        I'm in the process of doing this now diy. the wire alone is \$500 before any labor is added. ^c34321194

    - **yamtaddle** · [2023-01-09 22:37 UTC](https://news.ycombinator.com/item?id=34317415)
      Has there been a huge price drop? We bought a range about a year ago and the cheapest induction ranges were still around \$1,800 on sale. Gas could be had for like \$350, entry-level. And has a robust used market, which is lacking for induction (which isn't necessarily the tech's fault—it is fairly new) ^c34317415

      - **interactivecode** · [2023-01-09 22:54 UTC](https://news.ycombinator.com/item?id=34317687)
        Here for example 242 euro, plenty of choice: [https://www.ikea.com/nl/nl/p/matmassig-inductiekookplaat-ike...](<https://www.ikea.com/nl/nl/p/matmassig-inductiekookplaat-ikea-300-zwart-10467093/>) ^c34317687

        - **yamtaddle** · [2023-01-09 23:15 UTC](https://news.ycombinator.com/item?id=34317925)
          Huh. Ikea's got one—and only one—induction option, for \$1,400, in the US. A couple cheap "portable cooktops" (\$70!) but only one range, and it's not cheap, though that is cheaper than what I was seeing last I checked. ^c34317925

          \[EDIT\] Nebraska Furniture Mart, which has a much bigger selection than Ikea:

          Cheapest induction range: \$1,493 (sale price, claims full retail is more than \$800 higher)

          Cheapest gas range: \$529 (also a sale price, claims full retail is \$139 higher)

          - **bash-j** · [2023-01-10 00:01 UTC](https://news.ycombinator.com/item?id=34318347)
            Maybe it's a voltage thing (120V vs 240V)? In Australia you can pick up a Bosch induction cooktop starting from \$899 \~\$620USD including tax. ^c34318347

            - **midoridensha** · [2023-01-10 05:32 UTC](https://news.ycombinator.com/item?id=34320907)
              It's probably just an American thing: many things in America are atrociously expensive for some reason.  Here, it's probably the American expectation of a "range", which is a huge 4-5 burner stovetop combined with a humongous oven large enough for a whole turkey or even a small child. ^c34320907

              Here in Japan, IH stoves aren't that expensive, but they're just stovetops with 2 or 3 burners.  There's no such thing as a "range" here, and while ovens are becoming much more common, they're the size of a microwave oven, and usually combined with one.  You can also get portable single-burner IH stovetops for less than USD\$100.

              - **shaklee3** · [2023-01-10 06:21 UTC](https://news.ycombinator.com/item?id=34321207)
                you're taking shots at American prices compared to Japan, but then say Japan doesn't have those and only tiny versions of them. I use my range all the time at close to full capacity. it's not a useless or wasteful appliance. ^c34321207

                - **midoridensha** · [2023-01-10 07:13 UTC](https://news.ycombinator.com/item?id=34321535)
                  You're cooking turkeys and huge multi-person dinners every day?  When I lived in America, I *never* used my range to full capacity, in fact I never used more than one burner at a time, and never baked anything that wouldn't fit in the little microwave-sized oven I have now (i.e. cupcakes).  Yet I was \*forced\* to own a full-size range, because there's literally no option to have anything else in American homes: every home is built this way. ^c34321535

                  I see this in other things in America: you're forced to spend tons of money on stuff you don't need because that's all that's available, frequently because there's an assumption that you have a big family.  So everyone whines about housing being expensive, but there's no option for a tiny 1-person apartment because building codes don't allow it.

                  - **shaklee3** · [2023-01-10 16:09 UTC](https://news.ycombinator.com/item?id=34327007)
                    obviously not every day, but I do it at least 3 times per year. the vertical space isn't necessarily needed because spatchcocking the turkey is a better method, but oven here are built up standard widths and heights. I have used all the space/racks in the oven before on many occasions. ^c34327007

                    I'm probably not the norm, but I'm actually seeking out a double oven for this very reason. I have to borrow the neighbor's oven during big feasts because we can't fit in.

                    - **yamtaddle** · [2023-01-10 17:16 UTC](https://news.ycombinator.com/item?id=34328121)
                      I use the full width on mine all the time. The height's not really necessary, most of the time, but I don't think the extra material to bring it to counter height is adding much to the cost. ^c34328121

                      \> I'm probably not the norm, but I'm actually seeking out a double oven for this very reason. I have to borrow the neighbor's oven during big feasts because we can't fit in.

                      Double ovens are really, really nice, especially if you favor certain kinds of cooking or cook for large numbers more than a couple times a year.

                      \[EDIT\]

                      It is true that I almost never use more than two burners at once, but OTOH once you've committed to a certain size (and that size *is* nice, for being able to fit e.g. much larger sheet pans in the oven—IDK how you'd roast veggies for five in those tiny apartment-size ovens, without multiple batches) I, again, doubt it's adding much to the cost to go with 4 or 5 burners instead of 2 or 3, if the thing's already big enough to fit that many.

                      - **shaklee3** · [2023-01-10 17:57 UTC](https://news.ycombinator.com/item?id=34328752)
                        Yup! Since we don't have the space for a wall oven, I seeked a double oven. It turns out there's only one manufacturer (GE Cafe) that makes a double oven with an induction range. ^c34328752

                  - **jjeaff** · [2023-01-10 08:23 UTC](https://news.ycombinator.com/item?id=34321982)
                    My experience is that many things in the US are cheaper than Europe or south America. It must depend on what type of products. ^c34321982

                    - **midoridensha** · [2023-01-10 09:10 UTC](https://news.ycombinator.com/item?id=34322239)
                      Yes, it really does.  Some things in the US are absurdly expensive (like eating at a restaurant or getting a medical procedure), other things frequently significantly cheaper than elsewhere (like buying a car, assuming the same model, or a gallon of milk).  Sometimes it's due to expectations: Americans have expectations that others don't, and meeting those expectations costs a lot of money. ^c34322239

            - **maxerickson** · [2023-01-10 02:47 UTC](https://news.ycombinator.com/item?id=34319835)
              As far as multi burner built in cooktop/stove electric/induction setups, pretty much everything available in the US is 240V. ^c34319835

              You can get like countertop stuff that is 120V and lots cheaper.

            - **AngryData** · [2023-01-11 02:07 UTC](https://news.ycombinator.com/item?id=34334201)
              240 is available everywhere in the US, just the regular wall plugs are only using one phase of the two phase input. Often half the house is run on 1 phase and the other half on the opposite phase. ^c34334201

              Many homes already have 240 plugs behind stove and dryer installations. And even if you don't already have one you just need to stick a new breaker in the panel and run a wire using both phases together instead of a neutral or ground.

            - **sokoloff** · [2023-01-10 05:39 UTC](https://news.ycombinator.com/item?id=34320960)
              Any installable\* induction cooktop in the US will be 240V. ^c34320960

              \* meaning “not a countertop plug-in hob”

          - **miguelazo** · [2023-01-10 18:24 UTC](https://news.ycombinator.com/item?id=34329175)
            [https://www.amazon.com/Empava-Induction-Cooktop-Electric-EMP...](<https://www.amazon.com/Empava-Induction-Cooktop-Electric-EMPV-IDC30/dp/B0746DG22R>)?
            Empava 30” Induction Cooktop Electric Stove Black Vitro Ceramic Smooth Surface Glass EMPV-IDC30 \$338 ^c34329175

        - **miguelazo** · [2023-01-10 17:56 UTC](https://news.ycombinator.com/item?id=34328730)
          Thank you, I meant to link to the Ikea drop-ins in my original comment. Excellent value. ^c34328730

    - **nomel** · [2023-01-09 22:37 UTC](https://news.ycombinator.com/item?id=34317422)
      USD? Mid range where I am is over \$1k USD, from a big box store. Amazon shows similar results. Are you thinking a little countertop unit? ^c34317422

      - **miguelazo** · [2023-01-10 17:49 UTC](https://news.ycombinator.com/item?id=34328623)
        Yes. I have seen drop-in counter ranges (not countertop) go on sale for like \$700. In addition, this Samsung range/oven combo was on sale for \$900 in November. ^c34328623

        [https://www.samsung.com/us/home-appliances/ranges/electric/6...](<https://www.samsung.com/us/home-appliances/ranges/electric/6-3-cu-ft-smart-instant-heat-induction-range-in-black-stainless-steel-ne63b8211sg-aa/>)?

    - **lukev** · [2023-01-09 22:37 UTC](https://news.ycombinator.com/item?id=34317416)
      That's true, but it's also valuable for analyzing air quality for lots of other things (including Covid safety using CO2 as a proxy.) I use it at home and also bring it to the office occasionally to make sure things are reasonable there. ^c34317416

  - **ahaucnx** · [2023-01-09 23:10 UTC](https://news.ycombinator.com/item?id=34317891)
    This articles is very misleading and makes conclusions based on a low cost sensor that in most cases will give you very wrong absolute readings. I would not trust the results at all. Unfortuntaley all too often, people do air quality measurements and just blindly believe what they see on the display as true figures. ^c34317891

    It appears that the monitor in this article is a uHoo meter that can also measure NO2. The uHoo uses the SGX Sensortech MICS-2714 as NO2 sensors. It is a low cost metal oxide sensor and has a couple of significant issues. It is extremely suspectible to interfering gases like CO, Ethanol, Hydrogen, Amonia \[1\] and also gives highly different results based on humidity and temperature \[2\]. So just normal temperature and humidity fluctualtions will give greatly different results.

    Like other TVOC sensors, often the measurements correlate somehow with the gases but the absolute measurements are often by magnitudes wrong. If absolute measurements -as highlighted in the article- are important than the sensor needs to be calibrated exactly for this environment. This calibration requirement is even mentioned in the official specs \[2\]:

    IS CALIBRATION NEEDED, AND HOW OFTEN?
    It depends on the application, and on the required precision. Several factors tend to reduce the measurement accuracy e.g. production dispersion on base resistance (Ro) and sensitivity (S), temperature, humidity, the presence of
    interfering gases, ageing of the sensor, and on-time.
    Calibration is needed when the required accuracy cannot be obtained due to one or more of the factors listed above. This is the case for most applications where an absolute gas measurement is needed.

    This problem with absolute measurements on MOX sensors (most TVOC sensors) has been recognised by the large sensors manufacturers like Sensirion and Bosch and the newer generation of these sensors do NOT provide absolute measurements anymore but an INDEX which defines if air quality is improving or getting worse.

    In our open source air quality kits \[3\], we offer the Sensirion SGP41 as an option which is a much more modern sensor and offers an Index for TVOC and NOx. It still suffers from some of above issues like cross-interference of other gases but at least it does not give false absolute values. It can be very useful for detecting spikes but as outlined above the results need to be really understood with the knowledge of the limitations of these sensors in mind.

    \[1\] [https://www.sgxsensortech.com/content/uploads/2014/08/0278\_D...](<https://www.sgxsensortech.com/content/uploads/2014/08/0278_Datasheet-MiCS-4514.pdf>)

    \[2\] [https://www.sgxsensortech.com/content/uploads/2014/08/AN2-\%E...](<https://www.sgxsensortech.com/content/uploads/2014/08/AN2-%E2%80%93-Frequently-Asked-Questions-for-MiCS-Gas-Sensors.pdf>)

    \[3\] [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>)

  - **sliken** · [2023-01-09 23:01 UTC](https://news.ycombinator.com/item?id=34317808)
    My house has a large air volume, the 2nd floor is half as big as the first, so half the first floor has 20 foot ceilings.  I don't monitor NO2, but do monitor PM2.5 and CO2.  I see no difference in PM2.5, but do see my baseline of 550-650 CO2 bump to 1500 with significant gas stove usage.  The CO2 spreads quickly, my basement and bedroom sensors follow the 1st floor pretty quickly. ^c34317808

    If people want a air quality sensor that can upload data to the cloud (by default) or your local graphana, including source for an exporter, I'd check out airthings, their units are basically turnkey and can, but don't require) use a cloud.

    I'm definitely shopping for an induction stove soon.

    - **ed25519FUUU** · [2023-01-12 22:52 UTC](https://news.ycombinator.com/item?id=34361396)
      Do you use an exhaust hood vent when cooking? How long until the CO2 dissipates? ^c34361396

  - **danans** · [2023-01-09 22:35 UTC](https://news.ycombinator.com/item?id=34317393)
    \> but just be aware that not ALL gas stoves are problematic if set up correctly and burning cleanly. ^c34317393

    There is no such thing as a clean burning gas stove.  Even when not in use, they leak methane, and the majority of methane they leak is when they are not in use.

    All gas stoves and ovens, regardless of cost or age, put levels of pollutants into indoor air that are greater than what is safe \[1\].  A \$15k Wolf range is no better than a \$1500 range.

    The solutions are to either introduce a lot of ventilation, or switch to non combustion cooking.

    1\. [https://pubs.acs.org/doi/10.1021/acs.est.1c04707](<https://pubs.acs.org/doi/10.1021/acs.est.1c04707>)

    - **StillBored** · [2023-01-09 23:09 UTC](https://news.ycombinator.com/item?id=34317880)
      That article claims the stove is leaking \~1\% of its burned fuel. Which seems really unlikely, and deeper in they seem to claim its largely from the ignition cycle. Which is still \_really\_ hard to believe even on my old stove which generally takes a few arc's before there is enough gas near the spark igniter to catch. ^c34317880

      Even if you assume that 100\% of the gas loss in the time between when I turn it on, and it goes whoosh and burns all that fuel is wasted (say up to a full second) I would then have to leave the stove on for less than 100 seconds at full blast or double that if I turn the flow down by 1/2 for that gas to equal 1\% of the gas used during the cycle.

      Anyway, compared with the volume of methane in human flatulence, I would be worried more about how good the bathroom ventilation is than how much of unburnt methane manages to avoid being burned and also sucked out the fume hood.

      So, I too am skeptical about these home air sensors, I have one of the egg ones, that claims to measure PPM (CO2/etc). Yet it was spiking every morning, and at first I thought it was my wife putting on perfume, but it happens even when she isn't home in the morning... After watching it and what happens in my house, I suspect its largely measuring the humidity in the air from the shower.

      Doing nothing but turning the shower on causes it to spike a few mins later and then gradually go down for the rest of the day. I guess I didn't think that the majority of the PPM "pollution" in my house is actually just water droplets. Thats a lot different than all the fly-ash or whatever they want you to think is the problem. (edit: just to be clear, I'm not denying indoor pollution, only that the sensor I have, while marketed as such, isn't actually measuring pollution if most of what its measuring is mist from the showerhead).

      - **schiffern** · [2023-01-10 03:43 UTC](https://news.ycombinator.com/item?id=34320240)
        \>they seem to claim its largely from the ignition cycle ^c34320240

        Not so. In the abstract, they say that over three-fourths of their 1\% estimate was from when the appliance is not in use ("steady-state-off"). See Figure 5.

        \>the sensor... isn't actually measuring pollution if most of what its measuring is mist from the showerhead

        It's possible your sensor is actually measuring particulate aerosols created when the water droplets evaporate, leaving behind tiny particles due to dissolved solids.\[1\] The effect is similar to the "salt spray" aerosols formed by ocean wave action.

        The long residence time you report ("gradually go down for the rest of the day") makes this almost guaranteed, since tiny airborne water droplets will evaporate in under one minute at a typical indoor humidity of 50\%.\[2\]

        Hope this helps!

        \[1\] [https://pubmed.ncbi.nlm.nih.gov/17195485/](<https://pubmed.ncbi.nlm.nih.gov/17195485/>)

        \[2\] (see Table 2) [https://link.springer.com/article/10.1007/s10867-020-09562-5...](<https://link.springer.com/article/10.1007/s10867-020-09562-5#Tab2>)

        - **StillBored** · [2023-01-11 20:54 UTC](https://news.ycombinator.com/item?id=34344601)
          "The data for steady-state-off measurements were long-tail skewed, with the top 5 stoves (9\% of sampled units) emitting half (49\%) of all steady-state-off emissions." ^c34344601

          So, they have a couple leaky stoves in the equation and they extrapolate the data.  But they never bother to determine what was leaking, which is actually a fairly simple thing to do since there are commercial leak detectors that are quite sensitive ([https://www.southerncrossinc.com/wp-content/uploads/2019/10/...](<https://www.southerncrossinc.com/wp-content/uploads/2019/10/IRwin-brochure-9.25.19.pdf>)) to at home units that detect NG/propane/etc.

          Plus there were quite a number of other WTF moments in the document that don't match with my understanding of current install practices around NG heaters/etc.

          Not the least of which, is that if 1\% of the usage (which is a lot!) is leaking that will easily show up on peoples meters and be something that can be smelled. Which granted most people don't run outside and check their meter in the morning after having turned off all their gas consumers but people do smell gas. I've known at least one person who ended up ripping up a bunch of the piping in their attic because it was leaking, but i'm guessing its more likely someone forgot about an old appliance with an actual pilot light or the data was categorized improperly.

          Lets just say, that if you were honestly trying to run this study, don't you think you would want to go investigate some of the outliers to at least note that the top couple cases were broken valves, or rusted piping, or just debris in the gas line damaging/keeping the valve from closing (which is why modern gas codes require sediment traps) fully?

        - **Brian\_K\_White** · [2023-01-10 09:46 UTC](https://news.ycombinator.com/item?id=34322486)
          It's interesting to find out what the sensor may be actually measuring, and that it might actually be something, but I'm still left with the questions: ^c34322486

          Is that stuff actually harmful?

          If so, what could you even do about shower mist (at scale, as a reasonable thing to make a policy applying to all 7bn of us)?

          And doesn't it still sound like the gas stove does not stand out as some special problem?

          Or at least that, no article based on this source of data can be said to justify that conclusion.

          Maybe the stove is doing something so much worse than farts and showers that it's worth giving up the utility and efficiency\*, but this source of data does not show it.

          \* Efficiency including other gas appliances, ie, a gas clothes dryer is more efficient and interestingly, less fire risk than electric, but mostly the utility. Nothing else comes close to cooking with gas, it is simply by far the best tool for the job, and that is not an insignificant dismissable item.

          - **danans** · [2023-01-10 16:48 UTC](https://news.ycombinator.com/item?id=34327630)
            \> gas clothes dryer is more efficient and interestingly, less fire risk than electric ^c34327630

            A regular electric dryer is 100\% energy efficient, just like an electric resistance space heater.    A heat-pump electric dryer can be 2-300\% "efficient" (really COP) because it uses a heat pump.

            A gas dryer is strictly less than 100\% efficient - because like with any combustion device, some portion of the fuel is unburned and is sent out the exhaust/flue.   Even the most expensive gas condensing modulating  furnaces are only in the 90-97\% combustion efficiency range.

            Gas dryers are usually more *time* efficient though.  They achieve such high temperatures (thanks to combustion) that they dry clothes 50\% faster.   And because gas is cheaper than electricity, they are cheaper to operate.  The operational energy cost advantage vanishes when compared to heat pump electric dryers, however.

            - **StillBored** · [2023-01-11 21:06 UTC](https://news.ycombinator.com/item?id=34344822)
              Electric dryers aren't 100\% efficient if the source is the usual gas/coal/nuke/etc steam plant because the plant itself is only ballpark 50\% efficient at converting the heat-\>electricity, then you take a percent or ten in transmission losses/etc. So, if the choice is pump the gas to a combined cycle gas plant, burn it, transmit the electricity to a resistivity heating dryer vs pump the gas directly to the dryer and burn it, the gas dryer will generally win. ^c34344822

              Using a heat pump returns much of what is lost, but on balance in most places its sorta a wash. To be specific you have to look at the whole picture including the energy source, which requires actually picking a location/city and a particular product. And even saying maybe 100\% of your power comes from PV+Wind (yah righ, haha) if you really want to lower the footprint the best plan is just to hang your cloths outside.

            - **Brian\_K\_White** · [2023-01-10 18:45 UTC](https://news.ycombinator.com/item?id=34329502)
              Then compare the parts & materials list of a gas dryer and a heat pump dryer. ^c34329502

              - **danans** · [2023-01-11 15:37 UTC](https://news.ycombinator.com/item?id=34339611)
                You keep moving goal posts, but ok. ^c34339611

                Yes heat pumps are more complicated.  Likewise LEDs are more complicated than incandescent bulbs.  Condensing furnaces are more complex than gravity furnaces.  And nothing is simpler than a clothesline.

                Higher efficiency usually involves higher complexity (EVs being an exception, although batteries themselves are pretty complex at tiny scales).

                What's also great about heat pump and other condensing type dryers is that they are ventless.  With a regular vented dryer, each time you run it you exhaust several thousand cubic feet of indoor conditioned air, which gets replaced by outdoor unconditioned (hot, cold, or dirty) air due to the depressurization of your house.

                One way or another, you pay for reconditioning that air.

                Depending on how much you do laundry, your local climate, and the price of energy, a ventless dryer (which can only be electric, naturally) can save you a lot in energy costs by avoiding that air exchange.

    - **lukev** · [2023-01-09 22:48 UTC](https://news.ycombinator.com/item?id=34317578)
      Methane (at the volumes we're taking about) does not have significant health effects; the paper you link speaks mostly about its effect as a greenhouse gas. ^c34317578

      And I'm measuring my NO2 and it's within safe levels. So should I believe you or my own lying eyes?

      Granted, a lot of this may be due to other effects (e.g, ventilation) and I agree my next stovetop won't be gas.

      But clearly some setups are less problematic than others and it's not the case that everyone is poisoning themselves unless they go buy an electric tomorrow.

      - **danans** · [2023-01-10 03:08 UTC](https://news.ycombinator.com/item?id=34320020)
        \> So should I believe you or my own lying eyes? ^c34320020

        That's a question only you can answer.

        \> But clearly some setups are less problematic than others and it's not the case that everyone is poisoning themselves unless they go buy an electric tomorrow

        I didn't say everyone should go electric tomorrow.  But people are exposing themselves to (IMO high) indoor air pollution by using gas stoves without running an extractor fan and opening windows.

        A *lot* of people (everyone I know at least) only run the extractor to get rid of food smells, not for natural gas combustion byproducts, which is a mistake.

    - **hedora** · [2023-01-09 22:39 UTC](https://news.ycombinator.com/item?id=34317454)
      However, there is such a thing as an even dirtier burning gas stove.  For instance, put a natural gas regulator on a propane supplied burner, or vice versa. ^c34317454

      Also, even a properly tuned range will emit all sorts of things that are much worse than methane.

    - **kragen** · [2023-01-09 22:49 UTC](https://news.ycombinator.com/item?id=34317581)
      though any gas other than air will kill you at a high enough dose, methane is pretty extremely safe; wikipedia claims the major risk if you avoid blowing yourself up is that it can displace air and thus oxygen ^c34317581

    - **midoridensha** · [2023-01-10 04:56 UTC](https://news.ycombinator.com/item?id=34320700)
      \>There is no such thing as a clean burning gas stove. Even when not in use, they leak methane, and the majority of methane they leak is when they are not in use. ^c34320700

      How exactly does a gas stove leak methane (or anything else) when it's turned off, so there's no gas flowing?

      - **danans** · [2023-01-10 05:10 UTC](https://news.ycombinator.com/item?id=34320787)
        The valves that open when the stove is operating are not perfectly sealed (they can't be).  They allow a bit of methane to leak constantly. ^c34320787

        - **midoridensha** · [2023-01-10 05:24 UTC](https://news.ycombinator.com/item?id=34320873)
          Is this something about American-style gas stoves, or all gas stoves?  Why would it be impossible to have a valve with a perfect (or reasonably perfect, obviously nothing mechanical is absolutely perfect) seal?  A normal ball valve in a gas line is perfectly sealed; why would the valve in a stove be any different? ^c34320873

          - **Brian\_K\_White** · [2023-01-10 10:05 UTC](https://news.ycombinator.com/item?id=34322621)
            What magic world do you think we live in? Everything leaks at all times. ^c34322621

            And when discussing policy and things at scale, you factor in the total picture where 80\% of the individual examples will be one or more of: damaged, installed wrong, 35 years old, used incorrectly, cheaply designed, cheaply made, etc etc, not the perfect ideal lab example.

            To be clear, I am firmly in the 'keep gas stoves' camp because they simply work the best for that job, the alternatives are not actually alternatives, and I don't think any of these articles actually show that they are harmful, or at least stand out from any other source of of stuff in the air.

            But of course they leak. That isn't even remotely a remarkable claim. 'off' in the real world only ever means 'mostly off'.

    - **maxerickson** · [2023-01-10 02:37 UTC](https://news.ycombinator.com/item?id=34319734)
      How does a study that isolates the air around the stove in order to measure the emissions translate into the levels of pollutants that end up in the average home with a stove? ^c34319734

      I should definitely fix my vent hood though.

  - **ahelwer** · [2023-01-09 22:10 UTC](https://news.ycombinator.com/item?id=34316969)
    How much did you pay for the meter? Last time I looked into this measurements for various metrics were basically useless (unless you're only looking at relative, not absolute numbers) unless you spent at least a few hundred bucks and occasionally calibrated it. ^c34316969

  - **totoglazer** · [2023-01-09 22:32 UTC](https://news.ycombinator.com/item?id=34317350)
    Also have a uHoo. Kind of hate the UI, but it seems like a decent sensor. ^c34317350

    While my CO2 spikes during cooking on gas, fortunately NO2 remains low. 5-15 ppb range. My gas furnace is in the basement, several floors away from my apartment.

  - **jeffbee** · [2023-01-09 22:23 UTC](https://news.ycombinator.com/item?id=34317193)
    I think the big issue here is that renters do not get to pick and choose their appliances, so like other types of indoor health hazards this needs top-down regulation to make landlords replace gas with electric. ^c34317193

    - **0x457** · [2023-01-10 00:14 UTC](https://news.ycombinator.com/item?id=34318466)
      Well: [https://thehill.com/changing-america/sustainability/energy/3...](<https://thehill.com/changing-america/sustainability/energy/3663271-what-does-a-ban-on-natural-gas-appliances-mean-for-homeowners/>) ^c34318466

      However, no politician will ever try to make landlords and homeowners angry by forcing retrofit, whatever they do it will only apply to new properties. I doubt there is anything other than government forcing them will make my landlord install new induction stove or solar panels, and may landlord is actually nice...

      - **thinkcontext** · [2023-01-10 14:53 UTC](https://news.ycombinator.com/item?id=34325721)
        Many of the regulations are written so that if you do a major renovation you have to meet the new code. ^c34325721

    - **s17n** · [2023-01-09 22:27 UTC](https://news.ycombinator.com/item?id=34317265)
      Dear god please no, electric stoves are awful and idgaf about my lungs. ^c34317265

      - **lukev** · [2023-01-09 22:32 UTC](https://news.ycombinator.com/item?id=34317342)
        This is true for resistive electric stoves, which "pulse" on and off to achieve a certain heat level. Truly frustrating to cook with. ^c34317342

        Modern induction stoves are much better (even better than gas, I hear, though I haven't used them extensively yet.)

        - **yellow\_postit** · [2023-01-09 22:37 UTC](https://news.ycombinator.com/item?id=34317413)
          What have you found challenging to cook? I moved from gas to glass top electric and had heard horror stories (had always had gas stoves before) but despite regularly cooking meals for the family I haven’t run into anything problematic beyond worrying my cast iron will scratch the glass top (no issues so far). ^c34317413

          - **reddog** · [2023-01-09 23:00 UTC](https://news.ycombinator.com/item?id=34317788)
            I had a lot of trouble cooking on a halogen electic -- pulse on, pulse off -- stove and all those problems went away when I got an induction.  For years I thought I was a terrible cook but it was always that terrible electric cooktop.   The only thing that cooktop did well was boil water. ^c34317788

            The most frustating thing I tried to cook was good, crispy hashbrowns.  Believe me, I tried everything and the results were always soggy, greasy horror.  When I switched to induction (and replaced all my non-ferrous pans) the results were perfect everytime.

            - **midoridensha** · [2023-01-10 05:48 UTC](https://news.ycombinator.com/item?id=34320995)
              Induction seems to be the holy grail of cooking: electric (so it's clean and doesn't use fossil fuel from Russia), and highly controllable and repeatable.  Everything else should just be banned, gas because it's polluting and problematic, and other types of electric because they just suck. ^c34320995

          - **wonnage** · [2023-01-09 23:02 UTC](https://news.ycombinator.com/item?id=34317824)
            There are a few reasons people prefer gas:
            \- heat output
            \- heat distribution
            \- responsiveness to inputs
            \- durability/ease of cleaning ^c34317824

            I'm in the same boat and have found glass top actually produces more heat than a previous gas range. This isn't surprising at all numerically but people seem to automatically assume gas ranges are hotter even though you can literally just compare the numbers. Distribution is roughly the same or even better - gas tends to heat in a ring (where the flames are) whereas my glass top electric heats the entire circle. This is true even for wok cooking (although I have a flat-bottomed wok).

            Responsiveness to inputs is a real problem, there's a significant lag to temperature changes. Although, this is already something every cook has to deal with - different pans heat at different rates, and the amount of food in the pan is a factor too. You kind of just learn to account for it.

            Surprisingly the last point has been the worst for me - I'm always worried about putting pans down softly, and still have a few scratches. Cleaning is really easy for stuff that will wipe off, and near impossible for everything else. Spills with sugar/starch content need to be cleaned *immediately* or they'll be burned in forever. You can sort of scrape stuff off with a razor blade but you risk scratching the surface. I'm not sure why, given that glass ought to be harder than metal, but it happens nonetheless. With older coil/gas stoves you had drip pans or could line underneath the hob with foil, and just throw the foil away when it got dirty.

            But cooking-wise, no issues.

            - **yellow\_postit** · [2023-01-10 07:32 UTC](https://news.ycombinator.com/item?id=34321651)
              The temp change part makes sense and I can see how figuring out how to account for that across multiple pans could be challenging for folks that haven’t worked with it before. ^c34321651

              Cleaning I’ve had no scratches using bar keepers friends to make a paste and scrape off, ymmv.

              Came across this mother Jones article \[1\] on the success of the gas branding to promote gas stoves which was fascinating.

              \[1\] [https://www.motherjones.com/environment/2021/06/how-the-foss...](<https://www.motherjones.com/environment/2021/06/how-the-fossil-fuel-industry-convinced-americans-to-love-gas-stoves/>)

            - **shaklee3** · [2023-01-10 06:24 UTC](https://news.ycombinator.com/item?id=34321228)
              gas doesn't have higher heat output. this is the reason induction heats water much faster. ^c34321228

          - **mcguire** · [2023-01-09 23:15 UTC](https://news.ycombinator.com/item?id=34317929)
            The major problem with resistive stoves is that they take a relatively long time to warm up and cool down. ^c34317929

        - **jeffbee** · [2023-01-09 22:36 UTC](https://news.ycombinator.com/item?id=34317409)
          Induction ranges are almost all really bad except at the very high end. I have one that will intermittently scorch a 4-inch diameter annulus in the center of the pan while leaving everything else untouched. The only thing it's practical for is boiling water, which is enough of a benefit for me to justify its existence. ^c34317409

          - **llsf** · [2023-01-09 22:49 UTC](https://news.ycombinator.com/item?id=34317595)
            My dad is a professional cook (retired, but used to own a restaurant in France).  He only uses induction.  While he did not get the cheapest one, he did not take the high end either. ^c34317595

            One thing to consider is that quality of the pans and pots.  Nowadays while they are all induction friendly, some provide a better heat distribution than other.

            If asking my dad, the main benefit he sees is the control.

      - **sliken** · [2023-01-09 23:12 UTC](https://news.ycombinator.com/item?id=34317904)
        Electric stoves used to suck, low powered, annoying, and they made temperature control difficult. ^c34317904

        New induction units are more powerful than gas, respond more quickly, and have temperature based controls.  So you can blast and boil a quart of water more quickly, or set it to temperature and it will quickly approach it and maintain it, no more melted pots.

        With induction the heat (or lack of) is literally inside the pot/pan.  So it's already ahead of any combustion outside the pot/pan.  Granted not much, but still it's not behind.

        Also crazy easier to clean, nice flat surface, and there's not much heat outside the pot/pan to cook stuff on.

      - **asveikau** · [2023-01-09 22:30 UTC](https://news.ycombinator.com/item?id=34317304)
        Depending on where you live you may be out of luck in the future.  Some places are requiring them in new construction.  Including California. ^c34317304

        - **yamtaddle** · [2023-01-09 22:34 UTC](https://news.ycombinator.com/item?id=34317373)
          Hope that comes with a price drop. Gas is the only option right now if you want cheap *and* well-performing. Last I checked (maybe a year ago?) the cheapest induction ranges were well into the middle tier of prices. Which makes the fact that I keep seeing stuff about their tending to stop working after only a few years, or suffering from very-fragile surfaces that are easy to crack and ruin, even more of a turn-off. ^c34317373

          - **jerlam** · [2023-01-09 22:45 UTC](https://news.ycombinator.com/item?id=34317524)
            Maybe the ranges are cheap. But the price of natural gas has soared over the past year. Right now, it's cheap again, but it seems that prices are a lot more volatile than electricity, which will benefit from alternative sources of production and storage. ^c34317524

            - **weaksauce** · [2023-01-09 23:23 UTC](https://news.ycombinator.com/item?id=34318013)
              in socal the price of natgas is soaring. they expect this next month to be 3x more expensive than last month which was also more expensive than before. went from \$27 to \$75 and probably now going to be \$200+ for the same amount of use. we'll see. [https://www.ocregister.com/2023/01/06/your-natural-gas-bills...](<https://www.ocregister.com/2023/01/06/your-natural-gas-bills-to-jump-shockingly-high-across-region-socalgas-warns/>) ^c34318013

        - **econonut** · [2023-01-09 22:36 UTC](https://news.ycombinator.com/item?id=34317405)
          Yes, gas stoves are an unfortunate victim of climate policies enacted at the local level as city governments aim to ban all natural gas appliances in new construction in their misguided attempt to save the planet. Don't get me wrong, there is plenty they can do, but banning gas stoves is a ridiculous overstep. ^c34317405

          - **asveikau** · [2023-01-09 23:36 UTC](https://news.ycombinator.com/item?id=34318117)
            I think it's not just about saving the planet.  The gases and combustion are also a contaminant for human health.  Especially children. ^c34318117

            I don't have a beef with California for mandating this.  I do prefer gas stoves.  I can get over it.

          - **jeffbee** · [2023-01-09 22:38 UTC](https://news.ycombinator.com/item?id=34317436)
            Cities are able to take this action because they know they have no intention of building anything ever again, so the impact to actual residents and voters is zero. I should know: my city of Berkeley was the first to ban them. It is pure greenwashing. ^c34317436

            The final insult is single-family home construction and remodel can elect to use gas if they want.

            - **econonut** · [2023-01-09 22:49 UTC](https://news.ycombinator.com/item?id=34317597)
              That's fine for your city, but sucks for those of us living in the midwest. I can't speak for every city, but our growing city likes to model its policies after CA policies, so we get thousands of newly built electric-only homes & apartments. ^c34317597

              - **jeffbee** · [2023-01-09 23:04 UTC](https://news.ycombinator.com/item?id=34317838)
                Well, if your city adopts every dumb idea from Berkeley, that's on you guys. I thought everyone knew we are nuts. ^c34317838

              - **midoridensha** · [2023-01-10 05:58 UTC](https://news.ycombinator.com/item?id=34321060)
                \>but our growing city likes to model its policies after CA policies ^c34321060

                Who elects your city leaders?  This is your own fault.  If your city liked to model its policies after Russian policies, or Saudi Arabian policies, would that be those countries' fault?

            - **asveikau** · [2023-01-09 23:40 UTC](https://news.ycombinator.com/item?id=34318145)
              It's hard for a regulation like this to be retroactive.  There are a lot of gas stoves in use.  It's not feasible to replace them all, for various reasons.  So, restricting to new construction makes sense. ^c34318145

              Most bay area cities need to build more than they are, but I know that new construction in Berkeley is not zero.  One of the last times I was there, I saw some new apartments going up.

            - **dragonwriter** · [2023-01-09 23:40 UTC](https://news.ycombinator.com/item?id=34318143)
              \> Cities are able to take this action because they know they have no intention of building anything ever again, ^c34318143

              California cities don’t, since their choice now is between “approve enough new housing voluntarily” or “lose the ability to reject new housing entirely”.

              Builder's remedy expansion under the Housing Crisis Act of 2019 has changed the landscape fundamentally.

              - **jeffbee** · [2023-01-09 23:48 UTC](https://news.ycombinator.com/item?id=34318221)
                Get back to me as soon as any "builder's remedy" project breaks ground. ^c34318221

                - **asveikau** · [2023-01-10 00:03 UTC](https://news.ycombinator.com/item?id=34318374)
                  If the threat of using the builder's remedy successfully gets cities to change behavior, isn't that working correctly despite no "builder's remedy project breaking ground"? ^c34318374

                  I'd imagine also that these things take years. First for the law to take effect,  since that can't be immediate, and then for any enforcement of it to go through 
                  the courts.

  - **byyll** · [2023-01-11 16:43 UTC](https://news.ycombinator.com/item?id=34340511)
    I've read a few reviews of the uHoo saying they both 2 and put them in the same room and ending up with vastly different readings. I am not sure it's accurate. ^c34340511

  - **diziet** · [2023-01-09 22:11 UTC](https://news.ycombinator.com/item?id=34316988)
    What specific meter did you use? I want to try it myself. ^c34316988

  - **unknown** · [2023-01-09 23:01 UTC](https://news.ycombinator.com/item?id=34317809)
    [deleted] ^c34317809

  - **unknown** · [2023-01-09 22:12 UTC](https://news.ycombinator.com/item?id=34317025)
    [deleted] ^c34317025

- **danans** · [2023-01-09 22:12 UTC](https://news.ycombinator.com/item?id=34317021)
  Indoor air pollution from gas combustion appliances can actually be *worse* in newer homes because they are so much less leaky (and by consequence more efficient) than older homes. ^c34317021

  New building codes call for mechanical ventilation, but not nearly enough to compensate for the byproducts of combustion appliances or other sources of indoor air pollution.

  The best solution (an airtight house with 24/7 whole house mechanical ventilation with heat/humidity recovery) is sadly still the stuff of high end green homes.

  If you cook with a gas stove, you should open windows and run your extractor fan at max when cooking.

  - **bgentry** · [2023-01-09 22:39 UTC](https://news.ycombinator.com/item?id=34317452)
    I have a new house (built in 2020) and it did come with an inefficient, underpowered mechanical ventilation intake that just pulled outside air directly into the home. Given the house is in Austin, Texas where the weather outside rarely matches the conditions inside, this results in a lot of cooling or heating loss, as well as losing the humidity conditioning of the indoor air. It's no wonder that I regularly hear locals advising folks to simply turn off the mechanical ventilator; bringing in hot, humid summer air or cold, dry winter air is not good, even if the fresh air is. ^c34317452

    That's why shortly after moving in, I had the garbage ventilator replaced with an ERV. Based on my research I selected a Renewaire EV-Premium L, a variable speed unit which does up to 280 CFM. That's a ton of fresh air, even for a 4300 sqft house. But importantly it preserves some of the temperature and humidity when exchanging the air, so it's a lot more efficient than a plain mechanical ventilator.

    I have it wired into my Ecobee thermostat. It runs at its configurable low speed 24/7, and the Ecobee puts it in boost mode (full output) for 10-15 minutes per hour.

    This setup did cost some money of course, but the \$2000 cost was pretty minor in the context of a new home. With this setup, we never see a buildup of CO2, VOCs, etc indoors. Definitely worth it when we're both working from home and spending most of our time there. And although we have a gas cooktop, I never see any indoor air quality issues so long as we're running the hood while cooking.

    I hope indoor air quality becomes a bigger priority for homes, offices, and schools. The building codes in this area haven't yet caught up to the need for improved ventilation to account for how much better sealed up modern buildings are.

    - **alliao** · [2023-01-09 23:05 UTC](https://news.ycombinator.com/item?id=34317844)
      is it humid where you are? I'd love to have ERV but I'm in Auckland, NZ where dew point is bit of an issue and house sized dehumidifier isn't common as weather's temperate and heatpump only really caught on in the last decade or so. central air not common. ^c34317844

      - **bgentry** · [2023-01-09 23:22 UTC](https://news.ycombinator.com/item?id=34317992)
        Yes, Austin is quite humid relative to most of the US, though not quite as humid as along the gulf coast (i.e. Houston or New Orleans). ^c34317992

        The ERV was easy to tap into our existing central air system (which is where the crappy ventilator was connected) but if you don't have central air then it's going to be challenging to ensure quality air throughout your home.

      - **danans** · [2023-01-10 04:03 UTC](https://news.ycombinator.com/item?id=34320356)
        Auckland's climate sounds like that of coastal northern California, where HRVs work fine.  What's the concern you have with the dew point? ^c34320356

        The HRV core will drop the humidity of the incoming air stream, at least that is what it does at my house (and it's been extremely wet of late in  northern California).

        - **alliao** · [2023-01-11 20:23 UTC](https://news.ycombinator.com/item?id=34344098)
          do you have a model I can look at? auckland used to be a bit dryer but in the last couple of years starting to get 85\%+ humidity in both summer and winter and get foggy randomly.. the houses around here weren't built for this type of weather. I've seen some hrv systems like lossnay from mitsubishi but i don't think it deals with incoming humidity at all, it is probably relying on indoor heatpumps to deal with it. not even a drain from heat exchanger ^c34344098

      - **danans** · [2023-01-10 03:55 UTC](https://news.ycombinator.com/item?id=34320309)
        ERVs are very common in warm humid climates and cold dry climates (or climates that cycle between those).  If it's a cool humid  climate, an HRV is sufficient - no humidity transfer required. ^c34320309

  - **alliao** · [2023-01-09 23:03 UTC](https://news.ycombinator.com/item?id=34317825)
    i've really come full circle on the whole housing thing. At first I hated leaky old buildings, looked into passivehaus standard etc, wanting to minimising all air leakage. then I read about the NYC's oversized steam powered heater that allowed you to open windows during winter to achieve proper air change per hour during Spanish flu. ^c34317825

    Later on I looked into ERV systems for ventilation, which threw me down path of looking at dew point as when introducing a lot of outside air, humidity becomes an issue. now I'm convinced plenty of older buildings actually considered a lot of these things, I saw many cottages in NZ angled properly to receive the ideal amount of solar gains in different seasons which naturally ventilated and are pleasing to be in. very rare, but they do exist, and as result only a very small heatpump is required to minimally push the comfort envelope one way or another.

    I guess what I am saying is don't fight the nature if you can, and architecture it properly. failing that, airtight + mechanical ventilation is going to be expensive and probably impossible to hit good air quality (6ACH+)...

    - **danans** · [2023-01-10 03:22 UTC](https://news.ycombinator.com/item?id=34320118)
      \> then I read about the NYC's oversized steam powered heater that allowed you to open windows during winter to achieve proper air change per hour during Spanish flu. ^c34320118

      \> I guess what I am saying is don't fight the nature if you can, and architecture it properly.

      Oversized steam heaters are exactly fighting nature, are they not? 
      Really,  every building system is a fight against nature.  The idea is to exploit properties of materials and the forces of nature when you can to get closer to whatever your chosen optimum is without having to fight nature so hard.

      It's not even that hard build to near PassivHaus standards for airtightness these days with regular materials (I did it).  It does take an intention to focus on airtightness, which most production builders don't have.

      \> failing that, airtight + mechanical ventilation is going to be expensive and probably impossible to hit good air quality (6ACH+)...

      3ACH is plenty for good indoor air quality.   I got close to that once with a whole house ventilating fan that cost \$300.  HRV/ERV are more expensive, but they also do  heat recovery and air filtration, and provide consistent air quality everywhere.

  - **aclatuts** · [2023-01-09 22:27 UTC](https://news.ycombinator.com/item?id=34317262)
    Some higher end homes have a make up air system for venting a stove top in air tight houses, but it is so expensive. ^c34317262

    - **ed25519FUUU** · [2023-01-09 22:44 UTC](https://news.ycombinator.com/item?id=34317516)
      Are you describing something different than the overhead fan equipped above the gas range in most new homes? ^c34317516

      - **danans** · [2023-01-10 04:07 UTC](https://news.ycombinator.com/item?id=34320377)
        They are describing a system that automatically creates a path for replacement air when the overhead extractor fan turns on, which is also achievable by opening a window. ^c34320377

        Absent replacement air, stove extractor fans (like any extractor fans) cause an airtight house to experience negative pressure and reduce the effectiveness of the fans.

    - **thinkcontext** · [2023-01-10 14:47 UTC](https://news.ycombinator.com/item?id=34325610)
      I believe you are referring to a Heat or Energy Recovery Ventilator (HRV or ERV).  In the absence of a range hood they would be better than nothing.  But they aren't designed for the large volume of air changes that cooking requires. ^c34325610

- **barney54** · [2023-01-09 22:22 UTC](https://news.ycombinator.com/item?id=34317173)
  I don't understand the correlation between air quality and asthma.  In the United States, asthma rates are way up. This article blames at least part of the increase on air pollution, specifically nitrogen dioxide. But nitrogen dioxide concentrations in the United States are down by 54\% since 1990 alone.  [https://gispub.epa.gov/air/trendsreport/2021/\#air\_trends](<https://gispub.epa.gov/air/trendsreport/2021/#air_trends>)  It isn't outdoor air pollution that's driving the increase in asthma because outdoor air quality is improving (and has been improving for over 50 years in the United States. ^c34317173

  I would imagine that today's natural gas stoves are cleaner than in the past, natural gas appliance don't seem to be driving the increase in asthma either.

  My point is that the data isn't clear what is driving the increase in asthma.

  - **ericbarrett** · [2023-01-09 22:49 UTC](https://news.ycombinator.com/item?id=34317585)
    You raise a great point about air quality improvements. However, nitrogen dioxide, the irritant discussed in the article, is created with any hot-enough combustion process, since it's a reaction of the nitrogen and oxygen already in the air. Quality of fuel should have little to do with it. ^c34317585

  - **gedy** · [2023-01-09 22:26 UTC](https://news.ycombinator.com/item?id=34317245)
    From the increase in allergies, I wonder if life is too clean now basically. ^c34317245

    - **conqueso** · [2023-01-13 15:12 UTC](https://news.ycombinator.com/item?id=34368788)
      There's a well established theory called the "Hygiene Hypothesis" that says exactly this - [https://www.fda.gov/vaccines-blood-biologics/consumers-biolo...](<https://www.fda.gov/vaccines-blood-biologics/consumers-biologics/asthma-hygiene-hypothesis>) ^c34368788

  - **carlivar** · [2023-01-10 06:58 UTC](https://news.ycombinator.com/item?id=34321439)
    C-sections correlate to asthma. Compare c-section rates to asthma rates. ^c34321439

    - **ntimcan** · [2023-01-10 11:50 UTC](https://news.ycombinator.com/item?id=34323405)
      Breastfeeding rates correlate to asthma. Compare rates of breast feeding to asthma rates. ^c34323405

      - **BizarroLand** · [2023-01-11 00:18 UTC](https://news.ycombinator.com/item?id=34333380)
        Being born rates correlate to asthma. Compare rates of being born to asthma rates. ^c34333380

- **bob1029** · [2023-01-09 22:23 UTC](https://news.ycombinator.com/item?id=34317197)
  Induction really is better in a lot of important ways (especially if you value your time and cook every day). The only thing I hate to cook on it is wok-style or anything where the pan has to move quickly *with* fine temperature control. Most of the time, I can blast the rice on max and slide the pan around to similar effect, but it's not ideal and it can "run away" very quickly if food gets stuck. ^c34317197

  Aside from the few caveats, I can't imagine going without. Bringing water or oil to temperature is easily 3-5x faster on my 5kW element. Waiting for a semi-direct flame to heat your pot is so primitive by comparison.

  Then, there is the cleaning aspect. My induction cooktop takes 15 seconds to wipe down. My last gas range had some parts go through dishwasher, with others getting toothbrush-in-sink treatment. Unless you like cooking on a dirty range, this adds up fast.

  - **ajross** · [2023-01-09 22:39 UTC](https://news.ycombinator.com/item?id=34317440)
    Also safety: you can boil over a pot, pick it up, and just wipe the spilled gunk off the stove and the bottom of the pot with your other hand using nothing more than a rag. ^c34317440

    That's not to say you can't get an induction pan searing hot (small pans can actually get much *hotter* than ones over gas), but you have to work at it.  Generally the pan is no hotter than its contents.

    - **bob1029** · [2023-01-09 22:59 UTC](https://news.ycombinator.com/item?id=34317775)
      The safety has some fun and practical side effects. ^c34317775

      I put a paper towel between my cast iron deep fryer and my cooktop to keep it from leaving those weird oily rings behind.

      That said... the ridiculous power does have 1 downside relative to safety. If you are heating oil on an induction cooktop, please set a contingency timer somewhere to remind you to turn it off. In the amount of time it takes a gas range to get oil dangerously-smoking, induction has already ignited it and its been a raging inferno for at least 2 minutes.

      - **LargoLasskhyfv** · [2023-01-10 17:37 UTC](https://news.ycombinator.com/item?id=34328435)
        Mine have more 'UI' than I need. I just use 4 of the buttons. 1 is ON/OFF, where OFF is often superflous, because the timer function does that. Another cycles between choice/display of watts, temperature, or timer, indicated by three LEDs in a row above it. In steps of 10°C, 100Watts, or minutes, chosen by 2 others to the right and left of it, +(UP)/-(DOWN). I'm using temperature only, which is at 180°C by default. Tip, beep, tip, beep, long tap, boop. Indicated by 4 7-segment LEDs. There are other buttons for choosing programs, but I don't use them. Too unintuive. Just using the +/- on demand, according to sight & smell. Except for the timer, that's useful sometimes. ^c34328435

  - **ryantgtg** · [2023-01-12 01:58 UTC](https://news.ycombinator.com/item?id=34348067)
    Do you ever need to heat tortillas? We put those directly on our gas range, and are wondering what the induction solution is. ^c34348067

  - **Quiza12** · [2023-01-09 23:06 UTC](https://news.ycombinator.com/item?id=34317853)
    Agree with it all. Although I'll add that I miss charring vegies over the naked flame, as well. ^c34317853

- **dang** · [2023-01-09 22:40 UTC](https://news.ycombinator.com/item?id=34317468)
  Related ongoing thread: ^c34317468

  *U.S. safety agency to consider ban on gas stoves amid health fears* \- [https://news.ycombinator.com/item?id\=34310218](<https://news.ycombinator.com/item?id=34310218>) \- Jan 2023 (114 comments)

  Also related:

  *Gas stoves are more hazardous than we’ve been led to believe (2020)* \- [https://news.ycombinator.com/item?id\=31630946](<https://news.ycombinator.com/item?id=31630946>) \- June 2022 (122 comments)

  *What a gas stove ban means for restaurants* \- [https://news.ycombinator.com/item?id\=31603850](<https://news.ycombinator.com/item?id=31603850>) \- June 2022 (592 comments)

  *My best estimate is gas stoves decrease life expectancy by 53 days on average* \- [https://news.ycombinator.com/item?id\=30275953](<https://news.ycombinator.com/item?id=30275953>) \- Feb 2022 (117 comments)

  *How bad is my gas stove?* \- [https://news.ycombinator.com/item?id\=29935939](<https://news.ycombinator.com/item?id=29935939>) \- Jan 2022 (520 comments)

  *Cities try to phase out gas stoves but cooks are pushing back* \- [https://news.ycombinator.com/item?id\=27874912](<https://news.ycombinator.com/item?id=27874912>) \- July 2021 (481 comments)

  *Experts are sounding the alarm about the hidden dangers of gas stoves* \- [https://news.ycombinator.com/item?id\=25332332](<https://news.ycombinator.com/item?id=25332332>) \- Dec 2020 (343 comments)

  - **unknown** · [2023-01-10 05:18 UTC](https://news.ycombinator.com/item?id=34320831)
    [deleted] ^c34320831

- **sliken** · [2023-01-09 23:18 UTC](https://news.ycombinator.com/item?id=34317960)
  I didn't realize how big a deal the natural gas related pollution was.  As in the post I found out my rental wasn't doing what it should.  Turns out a hail storm had crushed the hat above the water heater exhaust.  Turns out the resulting air quality in the apartment was so bad my wife's hand writing changed.  We both don't remember much from that year, but have clear memories from the year before and after. ^c34317960

  Luckily we moved out after 8 months and her handwriting returned and our memories got much better.

  I strongly recommend monitoring your air quality, ideally with a CO alarm, since it's deadly quickly, and something like the airthings.com which monitors PM2.5, CO2, radon, and VOC.

- **legitster** · [2023-01-09 22:48 UTC](https://news.ycombinator.com/item?id=34317574)
  \> In other words, it may be possible to build a home with perfectly vented gas appliances, and there may be a safe level of NO2, but in the real world—in the homes that we all actually live in—this is probably the rare exception. ^c34317574

  This is a rather frustratingly blithe conclusion. Should we ban electricity in homes because they can be wired wrong?

  I'm not entirely sold on the health risks as presented, but that the author doesn't seem interested in seriously exploring *any* of the obvious solutions to this (seemingly) fixable problem makes this entire analysis feel rather lazy.

  - **542458** · [2023-01-09 23:16 UTC](https://news.ycombinator.com/item?id=34317938)
    Electricity is a funny comparison to pick. True, we didn’t ban electricity, but we did (effectively) ban certain “types” of particularly dangerous in-home electricity, like knob-and-tube. And like the cited passage, knob-and-tube can theoretically be perfectly safe (and even has some unique advantages!), but often isn’t safe in real-world scenarios. ^c34317938

- **virtual\_void** · [2023-01-09 22:00 UTC](https://news.ycombinator.com/item?id=34316819)
  Interesting. We have a gas stove and a gas furnace. Furnace was changed a few years back and coincides with worse asthma symptoms for both me and my youngest son. ^c34316819

  Anyone have any air quality sensor recommendations? Preferably one that i can easily extract data from for analysis.

  - **koolba** · [2023-01-09 22:19 UTC](https://news.ycombinator.com/item?id=34317118)
    Barring a completely incorrect install, the exhaust of the furnace should be completely vent out of your home. The indoor air is warmed by passing against a heat exchanger. ^c34317118

    If you’re having issues with air quality have your humidity levels checked. If it’s too low, a furnace attached humidifier will solve that by adding humidity to the treated air.

    - **RHSeeger** · [2023-01-09 23:38 UTC](https://news.ycombinator.com/item?id=34318130)
      We have a fairly new forced hot air heating system, and it has a humidifier in-line. It's amazing. You don't really notice it so much until you don't have it. When I'm in a house with forced hot air that doesn't have it, I find it painful. I was at a hotel in DC a while back that had the air on all evening, and my eyes hurt fiercely, dry due to the air. I don't get much of that at home (I'd get none, but... my eyes are broken enough that they're constantly dry to start with). ^c34318130

  - **danans** · [2023-01-09 22:06 UTC](https://news.ycombinator.com/item?id=34316905)
    \> Anyone have any air quality sensor recommendations? ^c34316905

    Search the HN archive. There are lots of debates and discussions about air quality sensors, especially around the time of the West Coast US fires.

    But from right now, every time you turn on your gas stove or oven, open a window and set your stove extractor fan to maximum, even if it briefly makes your house cold.

    - **scottlamb** · [2023-01-09 22:21 UTC](https://news.ycombinator.com/item?id=34317161)
      I don't recall any NO2 sensor recommendations in particular, and that wouldn't have been a focus during the fires. In general though folks here discussed AirGradient kits. [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>) I bought a stack of them, and I recommend them. The Pro kit at least has extra I2C module spots on the board (one for 3V3 modules, one for 5V modules). They sell a SGP41 module for VOC, and (I didn't know this until I looked at the spec sheet \[1\] just now) it also supports NO2. The output's apparently an "index" rather than calibrated physical units that you could compare to the threshold/graph in the post though. ^c34317161

      (btw: iiuc the "special" thing about the SGP41 module sold by AirGradient as opposed to some Alibaba vendor is that the AirGradient one doesn't come with surface-mounted terminating resistors installed. If you buy one from somewhere else and want to plug it into the AirGradient board, you need to desolder those because the AirGradient's I2C bus is already terminated elsewhere.)

      I have an older SGP30. Less luck there; it does VOC and CO2, no NO2.

      \[1\] [https://sensirion.com/media/documents/5FE8673C/61E96F50/Sens...](<https://sensirion.com/media/documents/5FE8673C/61E96F50/Sensirion_Gas_Sensors_Datasheet_SGP41.pdf>)

    - **virtual\_void** · [2023-01-09 22:08 UTC](https://news.ycombinator.com/item?id=34316946)
      Thanks. Will take your advice on both counts! ^c34316946

  - **anamexis** · [2023-01-09 22:07 UTC](https://news.ycombinator.com/item?id=34316919)
    Depending on your inclination for some DIY, AirGradient makes great kits. Open source and easy to use however you want. ^c34316919

    [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>)

  - **DoingIsLearning** · [2023-01-10 14:16 UTC](https://news.ycombinator.com/item?id=34325125)
    \> Furnace was changed a few years back and coincides with worse asthma symptoms for both me and my youngest son. ^c34325125

    As others have said, if correctly installed you should not have any furnace exhaust indoors.

    You should \_always\_ have at least a Carbon Monoxide alarm (CO) installed in the furnace room. If there is no monoxide leak it's unlikely that other particulates are escaping. The CO alarm should be installed in your furnace room irrespective of whatever sensor analytics you would like to add for your investigate.

- **DrFunke** · [2023-01-09 22:17 UTC](https://news.ycombinator.com/item?id=34317088)
  This was a concern of mine, so I purchased an induction stove. Also took it one step further by moving my entire kitchen to a covered outdoor patio. It seemed silly to be breathing oil particles for hours every time I cook chicken. Very grateful for my hypochondriac mother. She taught me to never not stop think about all the ways we can get cancer. ^c34317088

  - **postalrat** · [2023-01-09 22:54 UTC](https://news.ycombinator.com/item?id=34317674)
    Is always thinking about getting cancer a way to get cancer? ^c34317674

    - **DrFunke** · [2023-01-09 23:08 UTC](https://news.ycombinator.com/item?id=34317872)
      Thanks, I'll add that to the list. ^c34317872

- **screye** · [2023-01-09 22:38 UTC](https://news.ycombinator.com/item?id=34317429)
  I would be all for moving off gas-stoves, but can we acknowledge that the alternatives really suck if you like cooking ?             
  I want to be part of the solution, so here are few things that alternatives need to figure out before I move off gas: ^c34317429

  *Easy problems*:

  1\. No more cycling-induction/electric stoves. I do not want my food alternating between burning & sitting around.

  2\. A power setting where low-to-medium aren't only kind of burning your food.

  3\. Off means off. I don't want my food cooking for 5 more minutes after I turn the stove off.

  4\. Kitchen ranges having high quality broilers to make up for the lack of a charring mechanism on alternative ranges.

  *Hard problems*:

  1\. Being able to change the shape of the surface element to trace the shape of the pan. I cook with a wok, and all non-gas-ranges only heat the very center. If I can use a wok to fix the shape of the coil into a bowl, then I can ensure even heating even in a wok. (It's a spring coil, the shape should be mechanically adjustable).

  2\. Can the good ones be competitive on prices with top gas ranges ?

  I really dislike electric stoves, they have the worst of all worlds. Induction stoves: I could live with, but the good ones are too expensive to be a reasonable alternative for most people. There are additional good reasons to switch as seen from this\[1\] video.

  \[1\] [https://www.youtube.com/watch?v\=hX2aZUav-54](<https://www.youtube.com/watch?v=hX2aZUav-54>)

  \_\_\_\_\_\_\_\_\_\_\_\_\_\_

  Final caveat for tropical countries. Here, windows are always open. Houses often lack a gas connection, and instead have a gas-cylinder supplied to the house. So the pollution & removal-of-gas benefits do not apply.
  The cooking culture often relies on instantaneous fire to give certain staple flavors. They rely on curved pot shapes for cooking techniques & and the price differentials hurt a lot more when you're a poor country.

  Gas stoves sound a lot less evil in these tropical circumstances and this is the region where a majority of the world's population lives.

  - **alliao** · [2023-01-09 23:19 UTC](https://news.ycombinator.com/item?id=34317965)
    totally, given good sensor and control it's achievable. ^c34317965

    I've seen commercial grade equipment for wok (shaped) and even claypot 
    (they really need to make a 220v one for where I am [https://www.siroca.co.jp/product/kamadosandenki/](<https://www.siroca.co.jp/product/kamadosandenki/>) )

    hmm a bed of magnets to hug the bottom of pans with flexible induction coils beneath would work, and to clean just pop the magnetic layer into dishwasher

    time for a kickstarter?

- **Reason077** · [2023-01-09 22:54 UTC](https://news.ycombinator.com/item?id=34317694)
  Even an electric/induction stove will generate a lot of indoor air pollution if not well ventilated. ^c34317694

  In my current London flat (which I'm moving out of soon), nobody uses the fan above the stove because it's super loud and doesn't work properly anyway. Frying pretty much anything in the kitchen will cause my PM2.5 meter, which is upstairs in my bedroom on the other side of the house, to go crazy. Often up into the hundreds of µg/m³.

  Good kitchen ventilation is super important, gas stove or otherwise!

- **none\_to\_remain** · [2023-01-09 22:35 UTC](https://news.ycombinator.com/item?id=34317389)
  I will continue cooking with gas and simply accept this risk ^c34317389

- **musicale** · [2023-01-09 22:22 UTC](https://news.ycombinator.com/item?id=34317179)
  Definitely open the windows and turn the hood fan on *before* you turn the stove on (preferably one that actually vents outside since inside ones are useless\[1,2\]) and leave it on until after you turn the stove off. ^c34317179

  \[1\] [https://www.vox.com/energy-and-environment/2020/5/7/21247602...](<https://www.vox.com/energy-and-environment/2020/5/7/21247602/gas-stove-cooking-indoor-air-pollution-health-risks>)

  \[1\] [https://www.cbc.ca/news/science/gas-stoves-air-pollution-1.6...](<https://www.cbc.ca/news/science/gas-stoves-air-pollution-1.6394514>)

- **99\_00** · [2023-01-09 23:13 UTC](https://news.ycombinator.com/item?id=34317914)
  Unless you are willing to stop cooking, comparing indoor pollution while cooking with a gas stove versus when not cooking with anything is dumb. ^c34317914

  Comparing indoor pollution while cooking with a gas stove versus an electric stove makes sense.

  Yes, I suspect electric is cleaner than gas, how much cleaner is what's important.

- **chadlavi** · [2023-01-09 22:19 UTC](https://news.ycombinator.com/item?id=34317124)
  My wife can be in another room and not even know I've turned on the stove/oven, and she starts to cough when I start cooking. (we rent, don't get at me about replacing) ^c34317124

  I try to use our portable induction burner whenever I can now, even though we pay for electricity but we don't pay for gas.

  I was extremely skeptical and snooty about the potential of induction cooktops when it was first floated, but if I owned a home I would definitely prefer an induction stovetop to a gas one now. Induction is a lot faster and more responsive than gas, in my experience. Just wish there were induction stovetops that has real knobs and weren't so easily cracked or scraped.

- **jojobas** · [2023-01-09 22:19 UTC](https://news.ycombinator.com/item?id=34317119)
  It always bugged me that you can just burn something inside, unless there's a proper, exhaust-to-the-outside rangehood.
  I guess the only worse thing is the modern world are Japanese exhaust-to-room oil heaters. ^c34317119

- **ladberg** · [2023-01-09 22:09 UTC](https://news.ycombinator.com/item?id=34316965)
  I've had similarly bad results with CO2, PM2.5, and PM10 concentrations when I use my gas stove. ^c34316965

  If anyone is curious I have a Qingping Air Monitor Lite which I love. It's probably sucking up my data but I don't mind too much because it has a great physical interface, natively connects to HomeKit so I can see the current status and trigger events when levels get too high, and has a decent app that shows charts over time.

  It's nice to be able to remotely see that particulate levels are rising and turn on my air filter for a bit so everything's back to normal by the time I get home.

- **mattpallissard** · [2023-01-10 16:40 UTC](https://news.ycombinator.com/item?id=34327512)
  I worked several years in the food service industry in large, indstrial kitchens.  Ever since I have been puzzled as to why fume hoods over cook stoves are woefully inadequate.  Undersized, under powered, inadequately vented if vented at all. ^c34327512

  Even if your stove is burning cleanly it is a luxury to be able to cook on high heat without filling the entire room with smoke.

  Not to mention I'd suspect the fumes from the burning oil are probably worse than your clean\[ish\] burning LNG/propane stove.

- **beebmam** · [2023-01-09 22:28 UTC](https://news.ycombinator.com/item?id=34317274)
  Natural gas is absurdly cheap in most parts of the US. It's not going to change anytime soon here, simply due to these economic reasons. ^c34317274

  How do I go about testing my gas stove for dangerous emissions?

- **charlie0** · [2023-01-09 22:40 UTC](https://news.ycombinator.com/item?id=34317467)
  I'm not surprised about the gas stove pollution, but am surprised at how ineffective kitchen fans are. I got an air purifier with a sensor on it. It's about 8 feet away from the kitchen and it always goes on a few minutes if I switch any of the burners to a high setting. This happens even when I have the stove fan setting on high. These are suppose to suck the bad air out, but don't seem to do a good job at it. ^c34317467

  - **alar44** · [2023-01-09 22:52 UTC](https://news.ycombinator.com/item?id=34317648)
    Is it actually vented outside? Every place I've had it just recirculates through the hood. ^c34317648

    - **charlie0** · [2023-01-10 18:31 UTC](https://news.ycombinator.com/item?id=34329278)
      Yes, it has a large pipe going up through the ceiling. ^c34329278

- **asdff** · [2023-01-09 23:11 UTC](https://news.ycombinator.com/item?id=34317900)
  It gets so hot in my small kitchen while cooking that I end up opening the window anyhow. Too bad these days you have people who don't even open their windows in the summertime due to central AC. I'm sure their air quality is poor just from plastic products that the modern home is filled with (including carpet and furniture) offgassing ^c34317900

- **boredumb** · [2023-01-10 14:43 UTC](https://news.ycombinator.com/item?id=34325554)
  In case you're wondering why people are suddenly concerned about gas stoves -\> [https://www.bnnbloomberg.ca/us-safety-agency-to-consider-ban...](<https://www.bnnbloomberg.ca/us-safety-agency-to-consider-ban-on-gas-stoves-amid-health-fears-1.1867561>) ^c34325554

- **binkHN** · [2023-01-09 22:54 UTC](https://news.ycombinator.com/item?id=34317695)
  I guess I can corroborate a bit.  Back around the start of the pandemic, I picked up a few Awair devices (back when they were reasonably priced and weren’t used for crypto purposes) and put them around the house.  Whenever we cooked with our gas cooktop, TVOCs skyrocketed and the HVAC system dispersed this throughout the house. ^c34317695

- **StanislavPetrov** · [2023-01-09 22:56 UTC](https://news.ycombinator.com/item?id=34317722)
  I'm fine with the government making people aware of the risks, but not with banning gas stoves.  I'm an adult, and if I want to take that risk for myself, that should be up to me to decide.  The oft-trotted out argument that "well, when you get sick, the government has to take care of you and you are a burden to society" is nonsense.  If sentient adults don't have the right to make their own choices and assess their own risks, because of some amorphous burden to society, then the entire concept of freedom and autonomy is out the window.  This is an increasingly more important issue as people who push for "Socialism" strongly believe it should be up to the government to decide what you are allowed to do and should have the power to decide what "acceptable level of risk" adults are able to take on.  It is also one that pushes people like myself away from "Socialism", which is unfortunate because I believe in a strong social safety net for those who are unable to support and/or take care of themselves (for whatever reason).  But when push comes to shove, I'd rather live in a society without any social safety net whatsoever, where I was free to make my own decisions and take my own risks, than an authoritarian society with a social safety net. ^c34317722

- **CorrectHorseBat** · [2023-01-09 22:15 UTC](https://news.ycombinator.com/item?id=34317054)
  Modern gas boilers here (furnaces aren't very popular, I assume from a pollution point there's no difference) have external intake and exhaust. Would those still give indoor pollution? ^c34317054

  - **nrclark** · [2023-01-09 23:35 UTC](https://news.ycombinator.com/item?id=34318103)
    In the US, furnaces are required to be in a closet and have a carbon monoxide shutoff. A furnace will disable itself if local CO levels get above some threshold. So if your furnace's exhaust is working correctly, it shouldn't have much effect on airborne pollution in your house. And if your exhaust -isn't- working, then your furnace will shut itself off. ^c34318103

    I don't know the rules around gas boilers, but I'd expect that they're probably the same.

    Gas stoves are very different from an air pollution perspective. Kitchens are high-traffic areas in a lot of houses, and stoves are usually out in the open from an airflow perspective. Lots of houses don't have an exhaust hood that vents to the outside. And lots of cooks aren't in the habit of turning on their exhaust fans unless something has burned.

  - **lazide** · [2023-01-09 22:20 UTC](https://news.ycombinator.com/item?id=34317139)
    Any furnace, boiler, etc. which allows any exhaust gas to mix with indoor air is a major risk of Carbon Monoxide poisoning. Which does sometimes happen. ^c34317139

    If it's functioning correctly, exhaust gas and indoor air do not directly contact each other at all, they both go on opposite sides of a heat exchanger.

- **LatteLazy** · [2023-01-10 11:22 UTC](https://news.ycombinator.com/item?id=34323168)
  The study he links to is just a correlation study right? It proves nothing beyond the study author's ability to start with an assumption and then do maths. ^c34323168

- **casey2** · [2023-01-10 10:13 UTC](https://news.ycombinator.com/item?id=34322685)
  Stop with the "stealth" induction ad threads? No, the imperceptible amount of NO2 your gas stove releases is not a reason to waste money. ^c34322685

- **jacooper** · [2023-01-09 23:46 UTC](https://news.ycombinator.com/item?id=34318207)
  \> This story was originally published in January 2022. It has been edited slightly for clarity and to reflect new research. ^c34318207

  January *2023* not 2022.

- **kragen** · [2023-01-09 22:45 UTC](https://news.ycombinator.com/item?id=34317528)
  summary to circumvent the clickbait headline: author measured 291 ppb nitrogen dioxide from his gas stove and gas furnace, and gas stoves increase the risk of childhood asthma by 42\% (relative to an unspecified baseline but I bet it doesn't include cooking with wood or coal) due to the nitrogen dioxide exposure ^c34317528

  article does not mention particulates produced by food being cooked

- **Fauntleroy** · [2023-01-09 22:12 UTC](https://news.ycombinator.com/item?id=34317023)
  Which sensors detect NO2? I have a CO2 and PM2.5 sensor, but I'm finding it hard to come up with anything that mentions NO2. ^c34317023

  - **totoglazer** · [2023-01-09 22:30 UTC](https://news.ycombinator.com/item?id=34317305)
    The uHoo the author and another commenter here mentioned does. ^c34317305

  - **a\_t48** · [2023-01-09 22:20 UTC](https://news.ycombinator.com/item?id=34317142)
    It's a bit pricey, but some Dyson fans can measure NO2. ^c34317142

- **askin4it** · [2023-01-10 17:07 UTC](https://news.ycombinator.com/item?id=34327978)
  If you haven't figured it out: gas stoves are now "bad". By the time the "news" gets here, it's been upscaled to be consumed by 100+ IQs--that's us! ^c34327978

  Looks like the cultural elites don't want you enjoying cooking with gas.

  They'll have to cancel that expression as well. Now you are cooking with subatomic particles!

- **unknown** · [2023-01-09 22:47 UTC](https://news.ycombinator.com/item?id=34317561)
  [deleted] ^c34317561

- **quazar** · [2023-01-13 14:59 UTC](https://news.ycombinator.com/item?id=34368603)
  We were always at war with Gasstovia. ^c34368603

- **globalreset** · [2023-01-09 22:43 UTC](https://news.ycombinator.com/item?id=34317500)
  Absent real life threats, first-world people increasingly busy themselves with inventing surrogate problems. ^c34317500

  Everywhere Nazis are trying to overthrow democracy, climate change is going to destroy us all in the next 5 years, viruses go rampage and we need to lock everyone up, now your gas stove is trying to kill you.

  While in reality western world has never been so safe and prosperous.

  - **alar44** · [2023-01-09 22:56 UTC](https://news.ycombinator.com/item?id=34317714)
    For real. This is an absolute non issue, not even in comparison to anything else. There are tradeoffs for being a human. We need heat to cook. A few ppb in your home of whatever isn't shit compared to, idk, walking next to a fucking road or being in a city. Electric just offloads it to coal plants which is likely worse. ^c34317714

    Good grief.

    - **alliao** · [2023-01-09 23:24 UTC](https://news.ycombinator.com/item?id=34318018)
      don't know if you've been to Japan or followed any Japanese product, the idea of improvement is possible everywhere and anywhere is a compounding and thus powerful concept. Every year a journey between two cities are shortened by 1\% really adds up. I don't see anything wrong with improvements in general, you may be willing to take the risk, but it doesn't hurt that there's some other human beings thinking/working on this issue. ^c34318018

      - **alar44** · [2023-01-09 23:35 UTC](https://news.ycombinator.com/item?id=34318100)
        The externalities to switch the US over to electric are going to be massive compared to any benefits if there even are any. ^c34318100

- **steve76** · [2023-01-09 22:15 UTC](https://news.ycombinator.com/item?id=34317057)
  [flagged] ^c34317057

  \[dead\]

- **ksniwmidjd** · [2023-01-11 14:36 UTC](https://news.ycombinator.com/item?id=34338902)
  [flagged] ^c34338902

  \[dead\]

- **alfor** · [2023-01-09 22:09 UTC](https://news.ycombinator.com/item?id=34316961)
  The site is dedicated to fighting fossil fuels as if there were pure evil. ^c34316961

  Does not seems like a place for balanced views.

  - **virtual\_void** · [2023-01-09 22:21 UTC](https://news.ycombinator.com/item?id=34317147)
    He cites his sources (which seem reasonable), is making measurements and has written up objective results it seems. ^c34317147

    Perhaps there are other articles less objective on that site but it doesn’t seem like this article should be dismissed out of hand.

    - **alfor** · [2023-01-11 00:25 UTC](https://news.ycombinator.com/item?id=34333435)
      We always use heuristics to assess if a source is credible. ^c34333435

      Otherwise we have to do our own research, collect our own data. There is no other way around if there is no trust.

      It’s very easy for some information to be true, but also excluding all the bits that don’t fit the author bias.

      I think a source that is that biasied should be called out.

  - **hristov** · [2023-01-09 22:27 UTC](https://news.ycombinator.com/item?id=34317269)
    Balance does not imply truth. Sometimes truthful views are imbalanced because the truth is imbalanced. ^c34317269

  - **pessimizer** · [2023-01-09 22:33 UTC](https://news.ycombinator.com/item?id=34317366)
    You're never going to be convinced of anything if you'll only accept arguments from people who do not believe them. ^c34317366

  - **dang** · [2023-01-09 23:54 UTC](https://news.ycombinator.com/item?id=34318278)
    (We detached this subthread from [https://news.ycombinator.com/item?id\=34316898](<https://news.ycombinator.com/item?id=34316898>)) ^c34318278

  - **giraffe\_lady** · [2023-01-09 22:14 UTC](https://news.ycombinator.com/item?id=34317036)
    They may not be "pure evil" but they are clearly *extremely bad*. What does a balanced view of that look like for you? ^c34317036

    - **lukev** · [2023-01-09 22:22 UTC](https://news.ycombinator.com/item?id=34317182)
      Gas stoves (like everything else) have pros and cons. CO2 emissions are certainly a major con, which is why my next stove will be an induction. I got a gas ten years ago because induction cooktops were not widely available and the cook quality of gas is far higher than non-induction electric, and I cook a lot and really need quality tools. ^c34317182

      Facts matter, and it doesn't do anyone any good to paint something as "extremely bad" without balancing all relevant facts. Acknowledging that gas stoves are often (but not always) bad for indoor air quality is part of that.

      - **bodangly** · [2023-01-09 22:39 UTC](https://news.ycombinator.com/item?id=34317448)
        I really can’t understand this perspective. Perhaps cheap gas is better than cheap electric cooktops. But my Miele which is radiant, not even induction, heats up VERY fast and provides a very predictable amount of heat via the digital interface. I cook a lot, and thought I’d miss gas when buying my new house, but just about the only change I needed was to get a flat bottomed wok. Electric can definitely be more than adequate on the high end, imo. ^c34317448

        - **huffmsa** · [2023-01-09 22:56 UTC](https://news.ycombinator.com/item?id=34317721)
          \> digital interface ^c34317721

          Like a touchscreen?

          - **bodangly** · [2023-01-10 01:10 UTC](https://news.ycombinator.com/item?id=34318940)
            Sort of but less high tech than most think of w that word, it’s a “touchscreen” - red LEDs tell you the level. ^c34318940

      - **ajross** · [2023-01-09 22:36 UTC](https://news.ycombinator.com/item?id=34317395)
        We did a kitchen reno 11 years ago and hopped on the induction bandwagon then.  There were a pretty good number of options at the high end (i.e. 30" standalone, not an integrated/oven unit).  Induction is hot (heh) right now, but it's been a realistic option for a good while now. ^c34317395

    - **ethanbond** · [2023-01-09 22:20 UTC](https://news.ycombinator.com/item?id=34317133)
      The obvious outcome of the "both sides"-ism of late: We need to give equal airtime to the Inhaling Ignited Hydrocarbons Is Okay Actually group. ^c34317133

      Sources don't matter, depth of analysis doesn't matter, expert consensus doesn't matter, basic risk mitigation principles don't matter, what matters is that wherever a view is shared, all other views must be shared at equal volume and with equal credence.

      - **lr4444lr** · [2023-01-09 22:47 UTC](https://news.ycombinator.com/item?id=34317562)
        Strawman. ^c34317562

        37000 people die each year in vehicular accidents, but somehow people think there's a benefit to using cars, and to use them without making them 3X as expensive just to save perhaps half of those lives.

        So too do we continue to use gas appliances because they're relatively cheap, effective, and resilient, and if you want to convince us the harm is too great, then quantify it for our judgement.

        - **ethanbond** · [2023-01-09 22:59 UTC](https://news.ycombinator.com/item?id=34317774)
          \> if you want to convince us the harm is too great, then quantify it for our judgement. ^c34317774

          That's literally what TFA does. Dispute the data or the argument if you want. "This site looks like it doesn't like fossil fuels" is not disputing the data. It's "I suspect there's another side that's not represented \[duh\] and I therefore will dismiss this information out of hand." It's a terrible heuristic to get *anywhere*.

        - **ryukafalz** · [2023-01-09 23:09 UTC](https://news.ycombinator.com/item?id=34317881)
          \> 37000 people die each year in vehicular accidents, but somehow people think there's a benefit to using cars, and to use them without making them 3X as expensive just to save perhaps half of those lives. ^c34317881

          And each of those crashes is a tragedy. Surely you know that there are also efforts to make streets safer, and that other countries have been vastly more successful at it than the US?

          Traffic crashes were until very recently the leading cause of death among young people, and are still \#2. We shouldn't just overlook that either!

      - **alfor** · [2023-01-14 01:42 UTC](https://news.ycombinator.com/item?id=34376408)
        Just basic common sense would do. ^c34376408

        Everything is dangerous and has some risks, but usually weights the risks against other things, we see what are the ways to mitigate them, etc.

        If you say that gas stove is bad for indoor air quality, how does it compare to making toasts or having carpet and a bit more dust or living close to roads with lots of circulation.

        When it become a religious fervor, when there is only one side of the coin, that’s where there I see a problem.

      - **GauntletWizard** · [2023-01-09 22:23 UTC](https://news.ycombinator.com/item?id=34317190)
        The obvious outcome of "Misinformation and hate speech" policing of late. Proponents of things that are synonymous with civilization cannot have any airtime at all. ^c34317190

        - **1270018080** · [2023-01-10 16:32 UTC](https://news.ycombinator.com/item?id=34327399)
          Right, the only defense of inhaling hydrocarbons is some kind of trad culture war thing. Like because something bad is happening it has to continue happening because it's a part of my "civilization". ^c34327399

        - **mysteryalias** · [2023-01-09 22:42 UTC](https://news.ycombinator.com/item?id=34317488)
          [flagged] ^c34317488

          \[flagged\]

          - **kragen** · [2023-01-09 22:55 UTC](https://news.ycombinator.com/item?id=34317707)
            most of usenet was unmoderated for decades, and was consequently the best source of information on a huge variety of topics, though it certainly was full of trolls ^c34317707

            the nazi revival seems to have come out of newer heavily censored platforms like twitter and youtube

    - **alfor** · [2023-01-12 05:14 UTC](https://news.ycombinator.com/item?id=34349492)
      In this article I understand the concern about NOx, good ventilation, a detector might be a good idea.
      A quick look at the site show how much it is targeting at fighting all fossil fuels. But fossil fuels are the backbone of our civilisation. Yes we need to transition, and it’s happening, but if you were to cut them off completely I think that more that half of the world population would die in the next 12 months.
      So let’s be careful with that transition, we can easily kill more people by raising the cost of fuel than saving future people from hypothetical climate catastrophes or from NOx. ^c34349492

      Whatever what the activists and government does, the pricing alone is driving out all fossil fuels. Solar, wind and batteries are already cheaper than the other alternatives. It’s just a question of a few years.

    - **lazide** · [2023-01-09 22:17 UTC](https://news.ycombinator.com/item?id=34317093)
      With a decent hood, they are not clearly bad. ^c34317093

      - **Zagill** · [2023-01-09 22:38 UTC](https://news.ycombinator.com/item?id=34317435)
        The emissions from such stoves is a large part of what makes them "extremely bad" ^c34317435

        - **lazide** · [2023-01-09 22:45 UTC](https://news.ycombinator.com/item?id=34317529)
          Which emissions, exactly? ^c34317529

          With a proper hood, they aren’t an issue inside.

          When working properly, they are also quite minor.

  - **unknown** · [2023-01-09 22:13 UTC](https://news.ycombinator.com/item?id=34317027)
    [deleted] ^c34317027

  - **alfor** · [2023-01-10 00:37 UTC](https://news.ycombinator.com/item?id=34318677)
    This thread got remove from the main discussion. ^c34318677

    Fell like Twitter before the cleanup here.

  - **unknown** · [2023-01-10 00:37 UTC](https://news.ycombinator.com/item?id=34318671)
    [deleted] ^c34318671

  - **unknown** · [2023-01-09 22:23 UTC](https://news.ycombinator.com/item?id=34317188)
    [deleted] ^c34317188

  - **mperham** · [2023-01-09 22:22 UTC](https://news.ycombinator.com/item?id=34317165)
    [flagged] ^c34317165

    \[flagged\]

    - **rdiddly** · [2023-01-09 23:02 UTC](https://news.ycombinator.com/item?id=34317818)
      I didn't read it as political balance, though it's possible they meant it that way. But before I saw your comment I read it as a balance with the other side being "fossil fuels are pretty damn convenient." Like for cooking & heating. No use trying to ignore that, I mean it's not like people burn them to punish themselves. It's a trade-off. And since you said "Portland" my confidence drops from 92\% (nationwide average) to 86\%, i.e. still pretty confident, that you own a car, so I'm sure you know what I'm talking about. ^c34317818

    - **alfor** · [2023-01-10 00:22 UTC](https://news.ycombinator.com/item?id=34318535)
      Way more people die of cold each year it’s not even funny. ^c34318535

      Huge wildfires are caused by preventing regular small fires until there is way to much material and the condition are perfect: heat, wind, dry. Then you get a massive fire that can’t be stopped.

      Effectively the law of nature don’t care about what we think.

      At the moment we are caught in a new religion of climate change. But more and more people are waking up.

      Just the way you respond piling up argument show how it’s a religious battle for who is holly.

      Stop using coal as soon as possible, transition to solar, EVs, good idea.
      The rest is not as high priority.

    - **zdragnar** · [2023-01-09 22:31 UTC](https://news.ycombinator.com/item?id=34317321)
      Well, one could argue that cold continues to kill more people each year than heat does. ^c34317321

      It's not exactly a winning argument in favor of climate change, but just because a person is holding the correct view on one thing does not mean that they will be correct on others.

      Natural gas cooktops contribute a meaningless amount of CO2 in the grand scheme of things. When everyone is suffering the effects of global warming, they're going to feel silly for all the sacrifices they made along the way while the major sources of greenhouse gasses weren't addressed.

      - **mysteryalias** · [2023-01-09 22:39 UTC](https://news.ycombinator.com/item?id=34317447)
        You do know climate change is making some cold places even colder and increasing the severity of winter storms. Your comment only further strengthens the climate change argument. ^c34317447

    - **unknown** · [2023-01-09 22:33 UTC](https://news.ycombinator.com/item?id=34317365)
      [deleted] ^c34317365

  - **serverholic** · [2023-01-09 22:17 UTC](https://news.ycombinator.com/item?id=34317097)
    Please, please enlighten us with your take on what a balanced view means here. ^c34317097

  - **unknown** · [2023-01-09 22:15 UTC](https://news.ycombinator.com/item?id=34317061)
    [deleted] ^c34317061

- **nemo44x** · [2023-01-09 23:00 UTC](https://news.ycombinator.com/item?id=34317785)
  Get an electric or induction cooking surface and cook food and you’ll notice any and all air quality sensors reporting pollution if you have a poorly vented stove. The very process of heating oil to high temperatures to sear and brown foods emits all sort of pollutant. ^c34317785

  You can live your life by boiling everything on an induction range or you can cook with gas indoors like billions of people have without issue for generations. Stop being weird.

  - **99\_00** · [2023-01-09 23:16 UTC](https://news.ycombinator.com/item?id=34317934)
    Compare pollution while not cooking versus cooking with gas is the opposition of rational thinking. ^c34317934

    Probably even running an electric toaster will have an impact, especially if it hasn't been cleaned out (which is likely).

    - **nemo44x** · [2023-01-09 23:56 UTC](https://news.ycombinator.com/item?id=34318300)
      It’s the same thinking that creates “studies” where they run an old, faulty burner with no ventilation for 3 hours and compare results with running a new induction stovetop and marvel and how much better induction is for you. ^c34318300

      There’s a combined effort to demonize gas ranges by some climate extremists and it has been picked up by some media. They can’t convince people to change (because gas is superior technology) so they cone up with badly designed studies to scare people.

      They won’t be happy until you’re eating dehydrated beetles and grasshoppers.

      I can’t wait until they tell me to stop using my wood burning (gasp!!) fireplace every day.

