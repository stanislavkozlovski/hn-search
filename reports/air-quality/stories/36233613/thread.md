# [The Cuboid: A DIY air purifier that's better than a box-fan (2021)](https://news.ycombinator.com/item?id=36233613)

Article: [https://dynomight.net/better-DIY-air-purifier.html](<https://dynomight.net/better-DIY-air-purifier.html>)

ruph123 · 2023-06-07 21:08 UTC · 138 reported comments · archived 2026-11-08 13:03 UTC
Observation: 2026-11-08 13:02 UTC → 2026-11-08 13:03 UTC

## Comments

- **breput** · [2023-06-07 21:56 UTC](https://news.ycombinator.com/item?id=36234172)
  The Corsi-Rosenthal box\[0\] design using a standard box fan and furnace filters has been tested and verified to be very effective (and cheap): ^c36234172

  \[0\] [https://cleanaircrew.org/box-fan-filters/](<https://cleanaircrew.org/box-fan-filters/>)

  - **binarymax** · [2023-06-07 22:10 UTC](https://news.ycombinator.com/item?id=36234333)
    Indeed, linked in that article is this which I built yesterday and works very very well. ^c36234333

    [https://www.texairfilters.com/a-variation-on-the-box-fan-wit...](<https://www.texairfilters.com/a-variation-on-the-box-fan-with-merv-13-filter-air-cleaner/>)

    \-EDIT- I should also mention that you don't need 5 filters for this (MERV 13 is expensive), you can use 4 and a piece of cardboard for the 6th side that is touching the ground.

    - **lamontcg** · [2023-06-07 23:45 UTC](https://news.ycombinator.com/item?id=36235254)
      Yeah mine has 4 filters with a box fan on top and cardboard that the box fan came in as the base.  All taped together with duct tape.  Brain dead simple and cheap.  Used some more duct tape to fill in the "corners" of the box fan.  Mine blows positive pressure into the box, I just saw some designs that suck negative pressure out of the box, I don't know if that matters, but I've got a PM2.5 meter and mine worked fine last year during the smoke days in Seattle. ^c36235254

      - **Eisenstein** · [2023-06-08 02:54 UTC](https://news.ycombinator.com/item?id=36236599)
        I think it matters because with negative pressure you are causing the box to close and cover the gaps, whereas when you blow you are pushing on the box causing the gaps to expand. ^c36236599

      - **YZF** · [2023-06-08 00:39 UTC](https://news.ycombinator.com/item?id=36235652)
        I would think that you want to keep dust out of your fan motor/bearings etc. so you want the fan to be sucking out of the filter, not the other way around. ^c36235652

        - **culopatin** · [2023-06-08 01:34 UTC](https://news.ycombinator.com/item?id=36236063)
          Those fans normally would operate without any filters on either side, so the dust won’t really matter. ^c36236063

          - **masukomi** · [2023-06-08 11:45 UTC](https://news.ycombinator.com/item?id=36240254)
            ... they'll still function, but if you've ever had one you'll know that dust does matter. They're a pain to clean and the various crap in your air builds up on every edge. Definitely want it sucking filtered if that's that's an option. ^c36240254

  - **DeRock** · [2023-06-07 22:47 UTC](https://news.ycombinator.com/item?id=36234725)
    I see this all the time, why use multiple 1" thick filters to build a box, when you could just use 1x 4" filter. They are pleated, and the surface area should be equivalent. I documented my setup here before: [https://news.ycombinator.com/item?id\=28395232](<https://news.ycombinator.com/item?id=28395232>) ^c36234725

    - **oh\_sigh** · [2023-06-07 23:08 UTC](https://news.ycombinator.com/item?id=36234939)
      Having a greater surface area to filter the air through will decrease the static pressure and be nicer on the fan motor. If OP was putting the filters in series, then yes, it should have no effect. But they are putting the filter in parallel. ^c36234939

      - **DeRock** · [2023-06-08 00:30 UTC](https://news.ycombinator.com/item?id=36235572)
        My point was that 4x 1" filters assembled into a box is the same surface area as 1x 4" filter, but the latter is much easier to assemble. ^c36235572

        - **oh\_sigh** · [2023-06-08 02:09 UTC](https://news.ycombinator.com/item?id=36236291)
          Agreed, but it might cause your fan to burn out much quicker, or be less productive if you're using a box fan, since the static pressure differential will be approximately 16x between the two. ^c36236291

          - **sgc** · [2023-06-08 03:18 UTC](https://news.ycombinator.com/item?id=36236739)
            Why? If they have the same surface area, I would think they would have the same pressure differential? ^c36236739

            - **oh\_sigh** · [2023-06-08 05:29 UTC](https://news.ycombinator.com/item?id=36237608)
              Imagine calculating all possible routes an air molecule could take to escape after it is blown in. In the box case, the air molecule has 4 potential escape routes instead of 1 in the direct stacked filter case. And each escape route has it traversing 1/4 the amount of filter material. ^c36237608

              - **sgc** · [2023-06-08 13:13 UTC](https://news.ycombinator.com/item?id=36241315)
                Respectfully, I think you don't understand how air filters work. Air does not pass through 4x the filter material in a 4 inch filter. Instead, the 4 inch filter is pleated, folded like an accordion, so that each air molecule passes through the exact same thickness of filter as a 1 inch filter of the same MERV rating, but \~3x more surface area allows for \~3x more air to pass through. This is the only reason for making a thicker filter - to allow greater air flow. A box fan is generally operating below the capacity of the 4 inch filter, which is designed to allow for high cfm whole-house airflow. ^c36241315

                - **unknown** · [2023-06-08 17:36 UTC](https://news.ycombinator.com/item?id=36245628)
                  [deleted] ^c36245628

        - **sfink** · [2023-06-08 04:51 UTC](https://news.ycombinator.com/item?id=36237354)
          ??? ^c36237354

          4 x 1" filters, each with a surface area of 10 square megamicrons, provide a total of 40 square megamicrons when assembled into a box.

          A single 1 x 4" filter strapped to a fan gives a total of 10 square megamicrons.

          How are those the same surface area?

          Ah! I get it, because of the pleating. I guess it depends on whether the greater incoming airflow interferes with itself once it gets squeezed between pleats.

    - **postpawl** · [2023-06-07 22:53 UTC](https://news.ycombinator.com/item?id=36234783)
      Can confirm this works great. I wish there were more options for higher quality 20x20 box fans though. I’ve had Lasko fans that got loud after a few months, and I assume that’s a bearing going bad. ^c36234783

      - **bombcar** · [2023-06-07 23:53 UTC](https://news.ycombinator.com/item?id=36235317)
        There are commercial fans but they’re louder and more expensive. ^c36235317

        If there’s a belt from the motor to the fan you’re in for a good time.

    - **yumraj** · [2023-06-07 23:05 UTC](https://news.ycombinator.com/item?id=36234906)
      I have the same, without the 1" pre-filter in your case. The air flow is excellent, though it does get a little loud. ^c36234906

    - **lancefisher** · [2023-06-07 23:11 UTC](https://news.ycombinator.com/item?id=36234963)
      Exactly what I do, but with a 5", 20x25" MERV 16 filter. I run two of these on box fans when it's smokey in the summer, and it works very well. Box fans do get loud though. ^c36234963

    - **\_Nat\_** · [2023-06-07 23:14 UTC](https://news.ycombinator.com/item?id=36234994)
      \> why use multiple 1" thick filters to build a box, when you could just use 1x 4" filter. ^c36234994

      Probably uncertainty over how effective fans are when immediately obstructed, and maybe concerns about particles possibly getting deflected backwards if a filter messes with a smooth, laminar flow.

      This is, if we think of two kinds of airflow:

      1\. \[laminar flow\]([https://en.wikipedia.org/wiki/Laminar\_flow](<https://en.wikipedia.org/wiki/Laminar_flow>) ), which is like a smoothly flowing river;

      2\. \[turbulent flow\]([https://en.wikipedia.org/wiki/Turbulence](<https://en.wikipedia.org/wiki/Turbulence>) ), which is like erratic flow inside a mixer;

      then it seems like a box-fan might effect a laminar-flow further away from the blades (under normal circumstances), but could it be more turbulent near the blades?

      The boxed-in design seems to try to dodge assumptions about how air flows near the blades, reducing uncertainty about how turbulent-flows might screw with it.

  - **duxup** · [2023-06-07 22:21 UTC](https://news.ycombinator.com/item?id=36234453)
    I just built one in preparation for a home remodel.   I want to try to clean out any excess dust while we’re living through a remodel. ^c36234453

    Or even all the excess dust kicked up from a digging out old things we didn’t know he still had…

  - **stinos** · [2023-06-08 12:59 UTC](https://news.ycombinator.com/item?id=36241132)
    Also related: [https://smartairfilters.com/en/about/our-story/](<https://smartairfilters.com/en/about/our-story/>) ^c36241132

  - **skeaker** · [2023-06-07 22:03 UTC](https://news.ycombinator.com/item?id=36234259)
    How does this stack up in terms of noise versus the one in the OP? ^c36234259

    - **fellowniusmonk** · [2023-06-07 22:15 UTC](https://news.ycombinator.com/item?id=36234390)
      I have a few box fans filters and one cuboid fan, it's not actually the cuboid though, I used a circular hepa filter with the inline duct booster fan. ^c36234390

      I leave the fan duct fan running on low (right at the midpoint of the speed dial so technically medium I guess) 24/7 in my kitchen out of eye site because it's so quiet.

      So, in my experience, much quieter, quiet enough that people don't notice it running all the time. I have the dial in reach though so I can crank it all the way if something burns on the stove, clears the air out shockingly fast.

      I got some sound proof panels and crappily bungee corded them around the fan and it didn't have a noticeable effect. I think if I put more effort into the sound baffles it would reduce the sound, but the whole setup without baffles is quiet enough I haven't bothered.

    - **unknown** · [2023-06-07 22:30 UTC](https://news.ycombinator.com/item?id=36234538)
      [deleted] ^c36234538

    - **breput** · [2023-06-07 22:11 UTC](https://news.ycombinator.com/item?id=36234342)
      It's constructed using a regular 3 speed box fan, so it isn't going to be significantly louder than that and possibly quieter depending on how it is shrouded and insulated. ^c36234342

- **yumraj** · [2023-06-07 23:05 UTC](https://news.ycombinator.com/item?id=36234913)
  The intention of the OP/post might be good, but the comparison ([https://dynomight.net/img/cuboid\_purifier/boxfan.jpg](<https://dynomight.net/img/cuboid_purifier/boxfan.jpg>)) makes no sense whatsoever. ^c36234913

  They have just thrown 3 filters on top of the box fan with lots of gaps on the side. Air will *mostly* follow the path of lease resistance and not go through the filters. You need a filter that is the same size, 20x20, as the box fan and then the filter(s) will need to be sealed, via duct tape or so, around the fan for it to be effective.

  - **dynm** · [2023-06-08 00:08 UTC](https://news.ycombinator.com/item?id=36235422)
    Author here. I've tested the results of taping around the edges, you can see the results here: [https://dynomight.net/2020/12/15/some-real-data-on-a-DIY-box...](<https://dynomight.net/2020/12/15/some-real-data-on-a-DIY-box-fan-air-purifier/#taping>) ^c36235422

    - **yumraj** · [2023-06-08 01:27 UTC](https://news.ycombinator.com/item?id=36236015)
      The common way is to use a 20x20 filter, the same size as the box fan. ^c36236015

      Ideally you want to use a 4” thick filter, so a 20x20x4 filter and then just seal the outside. It provides huge surface area for the filter and the air flow is almost the same as the fan without the filter. I have a setup like that and it can really move air. The filter you have are much thinner.

      Now, I have no idea why you’re seeing the same results between taped and non-taped, it makes no sense and is indeed surprising.

      If you time and inclination, you may want to look into a 20x20x4 HEPA filter and try it.

  - **gardnr** · [2023-06-07 23:27 UTC](https://news.ycombinator.com/item?id=36235100)
    You are correct from an engineering perspective. From a cheap/GSD perspective the box fan filters are easy to build and provide a measurable result at a low cost. ^c36235100

    The internet would welcome any new designs you might have. I'm sure OP would be happy to have started a build-off.

    - **tedivm** · [2023-06-07 23:35 UTC](https://news.ycombinator.com/item?id=36235179)
      Yeah but there are *better* box fan filters out there. You can do exactly what OP did with his cube and throw a box fan on top of it instead of the duct fan, and with the higher airflow from the box fan combined with the exact same filter setup you'd likely see better results. ^c36235179

      Most of the box fan filters I've seen these days look like this cuboid fan- as in, they have four filters, a base, and a fan. Many also include some cardboard curved corners to improve airflow and reduce noise. I kind of assumed that's what we were comparing until I saw the image.

      Like these from another thread: [https://cleanaircrew.org/box-fan-filters/](<https://cleanaircrew.org/box-fan-filters/>)

  - **SkyPuncher** · [2023-06-07 23:34 UTC](https://news.ycombinator.com/item?id=36235171)
    the open space will build up pressure, to the point that some air will flow through the filters at equal pressures. ^c36235171

    This is not a perfect device, but it will capture more particulate than nothing.

  - **afterburner** · [2023-06-07 23:44 UTC](https://news.ycombinator.com/item?id=36235247)
    Yeah that box fan setup is hilariously bad. He wasn't nearly so careless about air flow with the design he actually liked. ^c36235247

    - **spion** · [2023-06-08 00:06 UTC](https://news.ycombinator.com/item?id=36235412)
      The box fan is analyzed in a separate article. See [https://dynomight.net/2020/12/15/some-real-data-on-a-DIY-box...](<https://dynomight.net/2020/12/15/some-real-data-on-a-DIY-box-fan-air-purifier/#:~:text=a%20better%20rate%3A-,Taping,block%20airflow%2C%20you%20slow%20down%20the%20fan.%20This%20could%20be%20counterproductive,->). ^c36235412

      - **afterburner** · [2023-06-08 14:23 UTC](https://news.ycombinator.com/item?id=36242357)
        And the construction is just as shoddy. The gaps where air can bypass the filter are *important*. Most of the air will bypass the filters because the air will go through the path of least resistance. ^c36242357

        - **spion** · [2023-06-10 18:13 UTC](https://news.ycombinator.com/item?id=36273172)
          If you read the article, you'll see some interesting measurements on that topic. ^c36273172

- **rainbowzootsuit** · [2023-06-07 22:25 UTC](https://news.ycombinator.com/item?id=36234497)
  What this and the box fans seem to miss is that prop fans have very little ability to generate static pressure. You will move more volume over the static pressure loss of the filters if you use a centrifugal type of fan. A little looking on Amazon shows those at about 3x the price of the prop boosters for the same rated cfm. ^c36234497

  If you add even a little bit of duct to extend approximately 3 duct diameters on the outlet it will make the fan a lot more efficient by allowing the airflow to stabilize and lower buffeting noise at the outlet. There athere are some of the centrifugal fans that include a noise suppressor for more money that's basically a short duct that's double walled and perforated on the inside.

  - **londons\_explore** · [2023-06-07 22:44 UTC](https://news.ycombinator.com/item?id=36234699)
    Having tried both, prop fans seem to beat centrifugal fans for the pressure drop across typical filters, and deliver more air per watt through a filter. ^c36234699

    I suspect the pleated nature of the filter means that the static pressure drop isn't all that much.   Haven't got a manometer to measure it though.

    - **rainbowzootsuit** · [2023-06-08 01:31 UTC](https://news.ycombinator.com/item?id=36236046)
      Thanks for the feedback. Thinking about it some more, a general purpose 1" HVAC filters are rated at about .12 in. water column at 300 feet per minute. If you're running them a lot slower by having 4x-6x area, then I could see that your tests would bear out. ^c36236046

      I often reference this manufacturer when designing a duct system and selecting filter sizes. This is for their MERV10 filter. MERV8 is lower initial pressure. They have a velocity vs pressure chart on page 4. At 50 FPM it's down to about 0.03 in. w.c.

      [https://www.glasfloss.com/product/zl-hv/](<https://www.glasfloss.com/product/zl-hv/>)

      I think a centrifugal could still be an advantage for noise while having a reasonable dimension, but your feedback is sincerely appreciated.

      - **londons\_explore** · [2023-06-08 06:16 UTC](https://news.ycombinator.com/item?id=36237938)
        I kinda wish all filtering was done with a greatly increased surface area. ^c36237938

        A 10x increase in surface area would mean far far less powerful fans are needed, and the filters could last a decade before needing to be replaced.

        - **rainbowzootsuit** · [2023-06-08 16:48 UTC](https://news.ycombinator.com/item?id=36244900)
          In a ducted system the ductwork and air terminals reach an economic happy medium that does not really balance with trying to make the filter pressure loss the driving factor. ^c36244900

- **adanto6840** · [2023-06-07 23:54 UTC](https://news.ycombinator.com/item?id=36235322)
  The quickest way to build one, IMO, is using a hot glue gun.  It takes quite a bit of hot glue to get it nicely sealed (maybe 10 sticks or so), but it's a LOT faster than using tape & it's more forgiving - you just "caulk" the seams liberally.  The non-standard, longer length glue sticks make it especially quick.  I feel like my hot-glued results have generally also been a bit faster/easier to pull partially apart, too, for when it's time to do filter replacements. ^c36235322

  I personally prefer to use two filters on each side, one as a "pre-filter" (cheaper carbon/charcoal, MERV \~10ish), with better (higher MERV, \~13 if possible) rated filters underneath.  You can then replace the prefilters more often, but the filters underneath won't require replacement nearly as much.

  I wrote about building them with hot glue on my blog\[0\] -- shameless plug! :)

  0 - [https://dantonio.info/projects/10-minute-corsirosenthal-box/](<https://dantonio.info/projects/10-minute-corsirosenthal-box/>)

  - **whycombagator** · [2023-06-08 01:35 UTC](https://news.ycombinator.com/item?id=36236076)
    Won’t the hot glue have a bunch of VOCs tho? ^c36236076

    - **Eisenstein** · [2023-06-08 03:03 UTC](https://news.ycombinator.com/item?id=36236666)
      Not at all. Hot glue is a thermoplastic which uses temperature to turn liquid and then solid again, which basically removes the need for VOCs at all. VOCs are solvents and are used to transition the liquid glue to a solid. ^c36236666

      \* [https://en.wikipedia.org/wiki/Hot-melt\_adhesive](<https://en.wikipedia.org/wiki/Hot-melt_adhesive>)

      - **diydsp** · [2023-06-08 11:26 UTC](https://news.ycombinator.com/item?id=36240074)
        Might have pthalates/softeners \[1\] which can be carcinogenic.  Not ideal to circulate.  Suggest cloth tape ^c36240074

        \[1\][https://adhesives.specialchem.com/selection-guide/hot-melt-a...](<https://adhesives.specialchem.com/selection-guide/hot-melt-adhesives>)

  - **culopatin** · [2023-06-08 01:43 UTC](https://news.ycombinator.com/item?id=36236118)
    You mentioned it yourself but I’m thinking caulk could work too. A combo of caulk and tape to contain the mess ^c36236118

    - **Eisenstein** · [2023-06-08 03:05 UTC](https://news.ycombinator.com/item?id=36236680)
      If you want to deal with a lot of smell and a lot of mess and a lot of drying time. Hot glue is super cheap and doesn't need to cure. The advantage to using caulk is zero, unless you count possibly burning yourself with the hot glue. ^c36236680

      - **stinos** · [2023-06-08 12:38 UTC](https://news.ycombinator.com/item?id=36240875)
        There are like tens if not hundreds different caulk compunds, enough of which don't smell. I don't understand why there would be more mess than with glue. I'll give you the drying time though, on the other hand most caulk types remain elastic, glue not as much, might matter with regards vibrations. And caulk is easier to apply properly and aestethically as you can use your fingers. tldr; it's fine you're defending glue, but it's not true thare is no advantage at all. In fact looking at these pictures I'd probably go for the combination, or else caulk only maybe in 2 passes, just seems easier to get a full seal. ^c36240875

        - **unknown** · [2023-06-08 14:43 UTC](https://news.ycombinator.com/item?id=36242672)
          [deleted] ^c36242672

        - **Eisenstein** · [2023-06-08 14:48 UTC](https://news.ycombinator.com/item?id=36242770)
          All I can say is: to those who have never used hot glue or caulk and are thinking of using caulk -- try the hot glue first. You can always pop open the caulking tube if it doesn't work to your satisfaction. ^c36242770

- **bsilvereagle** · [2023-06-07 21:57 UTC](https://news.ycombinator.com/item?id=36234191)
  Note that the OP uses ASHRAE's definition of CADR (nominally airflow rate \* removal efficiency) and not AHAM's more complicated definition which accounts for contamination rate. ^c36234191

  Some details about AHAM's CADR calculation are here: [https://frdmtoplay.com/nagivating-air-purification/](<https://frdmtoplay.com/nagivating-air-purification/>)

- **YZF** · [2023-06-08 00:46 UTC](https://news.ycombinator.com/item?id=36235689)
  I saw a pretty good comparison video the other day of different DIY options:
  [https://youtu.be/KobogQMf\_Xc](<https://youtu.be/KobogQMf_Xc>) ^c36235689

  "What is the best DIY Air Filter?"

  EDIT: I built one for my workshop but in my house with all the windows/doors closed it seems that I can get by with a much smaller filter, there's not that much smoke/particles that keep getting in IMO.

- **altairprime** · [2023-06-07 21:45 UTC](https://news.ycombinator.com/item?id=36234046)
  There’s a simpler construction of this, using tape and the fan or filter cardboard packaging, here: [https://cleanaircrew.org/box-fan-filters/](<https://cleanaircrew.org/box-fan-filters/>) ^c36234046

  - **BizarroLand** · [2023-06-07 23:24 UTC](https://news.ycombinator.com/item?id=36235084)
    I built this for myself. A few strips of Gorilla Tape and some ebay 4 pack for \$45 MERV 15 20x20x2 filters taped together as a support for a 20" box fan from Lowes. ^c36235084

    2600 sq ft home, filter is on the floor on the most open area of the house, which covers about 1/2 of the total space (39' Dome Home, 2 story plus a half story master, the area from the living room / dining room / kitchen to the master is all open area)

    My air quality meter showed me in the low warning area for PM2.5 and PM10 before I started using this, half a day after starting it up I am in the good range across the board, plus the climate is more uniform throughout the house and I'm sleeping better from the gentle breeze and mild white noise.

    I don't know if it would work as well in a boxier home, but a lot of people have said that it does for them as well, so it's probably worth it if you have \$65 to burn and the space for the filter cube setup thing.

- **carabiner** · [2023-06-07 21:37 UTC](https://news.ycombinator.com/item?id=36233946)
  BTW in Seattle we have learned to stock up on these fans, filters in the winter, because they sell out in stores during smoke season. ^c36233946

  - **kennywinker** · [2023-06-07 23:36 UTC](https://news.ycombinator.com/item?id=36235193)
    I hate that smoke season is a real part of life now. We are in a not-so-slow-motion climate collapse. ^c36235193

- **miked85** · [2023-06-07 23:04 UTC](https://news.ycombinator.com/item?id=36234896)
  *\- Two bungee cords (free).* ^c36234896

  *\- Tape (free).*

  *\- Two pieces of packaging foam (free).*

  Not that those are expensive, but I'm not sure why the link says they are free.

  - **qup** · [2023-06-07 23:48 UTC](https://news.ycombinator.com/item?id=36235271)
    In the DIY arena, if you didn't pay for it *today* or *specifically for this project*, then it's free. ^c36235271

    So people will build heirloom-quality furniture pieces for "free" with "scraps."

    But, as a DIYer myself, a lot of things do accumulate for Actually Free, you just have to watch out for good materials.

  - **afterburner** · [2023-06-07 23:47 UTC](https://news.ycombinator.com/item?id=36235262)
    Especially bungee cords. I don't accidentally have bungee cords, nor are they common office supplies... ^c36235262

- **londons\_explore** · [2023-06-07 22:40 UTC](https://news.ycombinator.com/item?id=36234663)
  Related question: ^c36234663

  As filters age, they change colour.  Mine start white and turn dark grey when old.

  However, I noticed that even the outlet side got darker.   That made me wonder if a 'blocked' filter was actually allowing more small particulates through (for example perhaps because all the surface area that a bit of PM2.5 could electrolytically stick to has already been stuck to).

  Does this sound plausible?   Anyone got test results for small particulates of different materials and how the filter performs as it ages?

  - **winrid** · [2023-06-08 04:39 UTC](https://news.ycombinator.com/item?id=36237295)
    You might have some swirl on exit causing some dirty air to be pulled in the front against the filter. ^c36237295

    - **londons\_explore** · [2023-06-08 05:25 UTC](https://news.ycombinator.com/item?id=36237591)
      Nope - no air leaks here.  Every bit of air passes through the filter. ^c36237591

      - **winrid** · [2023-06-08 09:13 UTC](https://news.ycombinator.com/item?id=36239145)
        Not leaks. On filter exit. Air moves around on clean side of filter but it's not a straight line. Dirty air will flow into the clean side from the room due to turbulence of the air on exit. ^c36239145

- **chefandy** · [2023-06-07 23:12 UTC](https://news.ycombinator.com/item?id=36234972)
  I couldn't afford this without having my own shop space. The parts are cheap, but after setting up something the size of a mini fridge that's covered in bungee cords in my little apartment, the marriage counseling would be costly. ^c36234972

  - **kennywinker** · [2023-06-07 23:32 UTC](https://news.ycombinator.com/item?id=36235150)
    If aesthetics are more important than cost, I have a blueair 211+ that does a great job and is quite silent. I would buy it again if a DIY filter was out of the question, tho my next filter will probably be a DIY job with a bit of time spent to make it look nice. ^c36235150

    - **bombcar** · [2023-06-07 23:58 UTC](https://news.ycombinator.com/item?id=36235345)
      I got a smart health cube that looks really nice but the filters are a bit expensive. ^c36235345

      Next time I’ll get one with washable prefilters even if the final one is disposable.

- **jacobsenscott** · [2023-06-07 22:37 UTC](https://news.ycombinator.com/item?id=36234637)
  If you live in a place with forced air heat you can probably set the furnace fan to be on all the time. Install a hepa filter and you are good to go. ^c36234637

  - **hedora** · [2023-06-07 23:19 UTC](https://news.ycombinator.com/item?id=36235041)
    Furnace fans often use a lot more electricity than you’d expect.  You can check by looking at your electric meter with it on and off (or maybe by looking at a sticker on the furnace). ^c36235041

  - **geoffeg** · [2023-06-08 00:00 UTC](https://news.ycombinator.com/item?id=36235361)
    Multiple HVAC techs I've talked to have recommended against installing good/high quality filters in a forced air system. They've explained that high-MERV filters reduce airflow which causes the fan to wear out faster and may affect the performance of the cooling/heating. I'm not sure how accurate that is, researching it seems to suggest a MERV 10 to 12 is a good balance, but I've been told to use a MERV 3 filter. ^c36235361

    - **jefftk** · [2023-06-08 00:23 UTC](https://news.ycombinator.com/item?id=36235506)
      You should be able to look in the manual and see the maximum MERV your forced air system is rated for. ^c36235506

      MERV 3 is really *really* minimal filtering.  Your furnace almost certainly is designed to take better filters than that.

      - **sgc** · [2023-06-08 03:37 UTC](https://news.ycombinator.com/item?id=36236870)
        It is not actually as simple as looking at the manual. You need to take ducting layout into account, since there is a lot of air flow reduction from any ducting system, and some can be much worse than others. It definitely does cause your furnace to overheat if you drop below the required airflow rate, something that can lead to short cycling and even premature failure by cracking your heat exchanger. All of this is calculated out using HVAC software when a system is commissioned (in theory and in many building codes, but not so much in practice). ^c36236870

        As can be seen, this is an issue during the heating season, not the cooling season - which is when many people are fighting smoke. If you actually pay attention to home maintenance, you can go for the better filter in the summer, and drop down to the minimum or close to it during the winter.

    - **whycombagator** · [2023-06-08 01:39 UTC](https://news.ycombinator.com/item?id=36236100)
      Last I looked it appeared you are safe to go MERV 8 for most residential HVAC units. MERV 3 is not filtering much ^c36236100

  - **turtlebits** · [2023-06-07 22:57 UTC](https://news.ycombinator.com/item?id=36234836)
    The only problem is that instead of re-circulating and filtering conditioned air, a furnace fan is going to bring in external unconditioned air (and is only filtered once). ^c36234836

    - **willcipriano** · [2023-06-07 22:59 UTC](https://news.ycombinator.com/item?id=36234859)
      Your furnace pulls from outside? Mine doesn't. I would've thought you'd want to heat the warmer indoor air to save energy. ^c36234859

    - **Waterluvian** · [2023-06-07 23:02 UTC](https://news.ycombinator.com/item?id=36234885)
      I haven’t had a central air system that does this. Mine have always had return vents and it just cycles internal air. ^c36234885

      I’m actually very curious about more intelligent systems. Those that can:

      \- bring in outside air on occasion to freshen things up

      \- negotiate the best way to cool a home depending on outside air. It drives me mad when my AC kicks on and it’s actually colder outside.

      - **dzhiurgis** · [2023-06-08 03:37 UTC](https://news.ycombinator.com/item?id=36236868)
        \> - bring in outside air on occasion to freshen things up ^c36236868

        All HRV's do that. "single room recuperator" from aliexpress is in every flat after renovation in Lithuania.

      - **the\_sleaze9** · [2023-06-08 01:18 UTC](https://news.ycombinator.com/item?id=36235942)
        As a kid I always wanted an external vent on the refrigerator that pulled in outside air when it was cold enough. ^c36235942

    - **nomel** · [2023-06-07 23:12 UTC](https://news.ycombinator.com/item?id=36234969)
      I’ve never seen a furnace fan that pulls in outside air, unless it was some DIY garbage that wasn’t to code, or a huge money waster from 100 years ago. ^c36234969

    - **afterburner** · [2023-06-07 23:49 UTC](https://news.ycombinator.com/item?id=36235282)
      An office or school's central air system might bring in some outside air, but regular house systems don't. They have intake grills inside the house. ^c36235282

    - **kshahkshah** · [2023-06-07 23:34 UTC](https://news.ycombinator.com/item?id=36235174)
      From where? Bringing in outside air is what a 'fresh air' system does like an ERV or HRV ^c36235174

      - **SkyPuncher** · [2023-06-07 23:40 UTC](https://news.ycombinator.com/item?id=36235217)
        Most older homes simple have an outdoor draft/damper for makeup air. ^c36235217

        You’ll draw in a lot of dirty outside air with that setup if you don’t block/reduce outside air intake. It will still go through a filter, but it’s going to cause the filter to dirty very quickly.

- **carabiner** · [2023-06-07 23:19 UTC](https://news.ycombinator.com/item?id=36235042)
  The Cuboid might be better, but because he used two completely different fans, this is not a valid comparison. The Cuboid uses a ducted fan, where the tall duct will increase the flow rate by promoting expansion in the exhaust. The other fan is just a non ducted (or very poorly ducted) box fan. It looks like he also only does one trial for his measurements. *Most of the efficiency CADR/power probably comes from using a better fan*, which is the whole purpose of adding a long duct. ^c36235042

  The extra effectiveness might also come from the Cuboid fan being elevated off the floor. With the box fan standing on the floor and pointing horizontally, it has an additional solid boundary restricting intake air. The vertical pointing fan in the Cuboid does not have this restriction.

  A proper test would use the same fan in both designs. The non-Cuboid fan would be oriented upwards and mounted on stilts. Multiple trials should be done with the results averaged. He omitted a chart showing both particles counts vs. time of both approaches, which would be the most important figure to include.

- **astockwell** · [2023-06-07 21:35 UTC](https://news.ycombinator.com/item?id=36233915)
  This is almost exactly the design used by BlueAir purifiers [https://www.blueair.com/us/blue-family.html](<https://www.blueair.com/us/blue-family.html>) ^c36233915

  Can recommend.

- **groos** · [2023-06-07 22:08 UTC](https://news.ycombinator.com/item?id=36234316)
  The article didn't mention the static pressure of the fan. Typically, for a "suck" type fan, you want higher static pressure and there are fans which are designed expressly for this. ^c36234316

  - **unit\_circle** · [2023-06-07 22:29 UTC](https://news.ycombinator.com/item?id=36234528)
    Noctua makes some nice, slightly ruggedized 12v high static pressure fans. ^c36234528

    - **numpad0** · [2023-06-07 23:44 UTC](https://news.ycombinator.com/item?id=36235251)
      There are also AliExpress storefronts for high static pressure fans(blower and axial), easily 10x as powerful compared to computer case fans. ^c36235251

  - **plagiarist** · [2023-06-07 22:21 UTC](https://news.ycombinator.com/item?id=36234451)
    What would I want to search for to find that? "High static pressure fan?" ^c36234451

    - **ethbr0** · [2023-06-07 22:30 UTC](https://news.ycombinator.com/item?id=36234553)
      [https://www.mcmaster.com/products/high-pressure-blowers/](<https://www.mcmaster.com/products/high-pressure-blowers/>) ^c36234553

      Or don't let the perfect be the enemy of the good -- buy 10x box fans for cheaper, because they're manufactured and shipped in the millions of units.

      If it's not going to catch on fire, why are we worrying about the longevity of something that costs \$30?

      - **ilyt** · [2023-06-07 22:54 UTC](https://news.ycombinator.com/item?id=36234801)
        ...did you look at what you linked ? They are all 65-75dBA+ massive blowers... ^c36234801

    - **rainbowzootsuit** · [2023-06-08 01:58 UTC](https://news.ycombinator.com/item?id=36236209)
      A centrifugal inline fan is what would be the most common to look for. ^c36236209

      They should list a CFM at Inches of Water Column in the 1/4 to 1/2" range to be considered "high static" pressure.

      Those blowers from the other comment are like for your iron smelter.

- **tedunangst** · [2023-06-07 22:42 UTC](https://news.ycombinator.com/item?id=36234675)
  \> If you take the top pick from the Wirecutter and read user reviews carefully, you’ll see that roughly one person a week reporting that their unit exploded. ^c36234675

  I mean, if you read colander reviews on Amazon, you'll find people who somehow lost a hand to it.

  - **themerone** · [2023-06-07 22:55 UTC](https://news.ycombinator.com/item?id=36234808)
    I love the reviews and comments where you really hope the person left it on the wrong product page, such as the person asking how big reppelent helps with babies teething. ^c36234808

    - **crazygringo** · [2023-06-07 23:07 UTC](https://news.ycombinator.com/item?id=36234925)
      It's usually Amazon's fault. A listing can change the product being sold entirely. I suspect it's a well-rated product that sells its listing to a new product so it starts out with high ratings and popularity (even though the reviews are for a different product entirely). ^c36234925

      Historically, Amazon doesn't seem to care.

      - **themerone** · [2023-06-07 23:48 UTC](https://news.ycombinator.com/item?id=36235272)
        I'm aware, but you can tell by the dates if this is the case ^c36235272

- **mrbonner** · [2023-06-07 22:03 UTC](https://news.ycombinator.com/item?id=36234257)
  Ok where did they buy 3 HEPa filters for \$70? ^c36234257

  - **sp332** · [2023-06-07 23:38 UTC](https://news.ycombinator.com/item?id=36235206)
    These are 2 for \$25, and large enough to fit an 8-inch duct fan between. [https://www.target.com/p/costway-2-in-1-air-purifier-replace...](<https://www.target.com/p/costway-2-in-1-air-purifier-replacement-filter-true-hepa-filter-active-carbon-filter/-/A-87878013#lnk=sametab>) ^c36235206

- **ary** · [2023-06-07 22:16 UTC](https://news.ycombinator.com/item?id=36234403) ^c36234403

  ```
    The design should also fix the worst parts of using a box fan:

    1. Make less noise.
    2. Use less electricity.
  ```

  
  Point \#1 is not the worst part of a box fan for many people, myself included. I have a lot of fond memories from growing up where a box fan was running at night due to the outside heat and lack of central AC. It made sleeping a much easier and more pleasant experience.

  - **ethbr0** · [2023-06-07 22:26 UTC](https://news.ycombinator.com/item?id=36234507)
    Spend \$50 and prepare to have your mind blown. ^c36234507

    [https://www.amazon.com/Adaptive-Sound-Technologies-LectroFan...](<https://www.amazon.com/Adaptive-Sound-Technologies-LectroFan-Non-Looping/dp/B00E6D6LQY>)

    - **xen2xen1** · [2023-06-07 22:33 UTC](https://news.ycombinator.com/item?id=36234608)
      I both need the noise and the air (I sleep warm), but I had what had to be a 1950s version of this when I was a teenager , which was just a small enclosed fan that had a top you could regulate to change the sound.  Still miss it sometimes. ^c36234608

      - **salad-tycoon** · [2023-06-07 22:42 UTC](https://news.ycombinator.com/item?id=36234677)
        Yep. Bought one at one of the donation stores for \$2. Made in USA, must be about double my age, and still works great. Amazed that a little fan like that can just keep spinning for that long. ^c36234677

        Hooked it up to a wifi power switch. Old meets new.

        - **qup** · [2023-06-07 23:55 UTC](https://news.ycombinator.com/item?id=36235331)
          I find smart plugs work best with the dumbest devices. I love these pairings and use them a lot myself. ^c36235331

        - **winrid** · [2023-06-08 04:55 UTC](https://news.ycombinator.com/item?id=36237389)
          Nice sealed bearings with generous tolerances will do that. \<3 ^c36237389

  - **Dylan16807** · [2023-06-08 00:05 UTC](https://news.ycombinator.com/item?id=36235406)
    That's fine for the part of the day you're asleep. ^c36235406

    That level of noise is pretty bad for most of the rest.

- **csours** · [2023-06-07 21:45 UTC](https://news.ycombinator.com/item?id=36234047)
  (2021) ^c36234047

  I'm currently dreaming up a ceiling fan replacement that has a much lower profile and also cleans the air with a standard furnace filter.

  - **nilstycho** · [2023-06-07 21:55 UTC](https://news.ycombinator.com/item?id=36234170)
    Have you seen jefftk's ceiling air purifier? ^c36234170

    Post: [https://www.jefftk.com/p/ceiling-air-purifier](<https://www.jefftk.com/p/ceiling-air-purifier>)

    HN Discussion: [https://news.ycombinator.com/item?id\=31590773](<https://news.ycombinator.com/item?id=31590773>)

    - **csours** · [2023-06-07 22:09 UTC](https://news.ycombinator.com/item?id=36234325)
      Haha, yes. I love it. ^c36234325

- **entrepy123** · [2023-06-07 23:12 UTC](https://news.ycombinator.com/item?id=36234981)
  On the topic of air quality, can anyone recommend a "fine dust meter" (or really just "regular dust meter")?  I would prefer totally non-wireless (USB preferred, handheld okay). ^c36234981

  For CO2, the ZGm053U has been a great device.  But now I would like to measure all the dust I see in a dark room with a bright flashlight.

  - **Rebelgecko** · [2023-06-08 01:17 UTC](https://news.ycombinator.com/item?id=36235936)
    I've been using an Airgradient Basic for CO2, PM1, PM2.5, and PM10 (not sure if that includes dust?). Easy to hook it up to a database, Home Assistant, or their cloud. But you can also just use it with a USB battery and read the \#s off the screen. ^c36235936

    - **entrepy123** · [2023-06-08 04:02 UTC](https://news.ycombinator.com/item?id=36237023)
      Thanks. ^c36237023

- **unknown** · [2023-06-07 23:13 UTC](https://news.ycombinator.com/item?id=36234990)
  [deleted] ^c36234990

- **kristopolous** · [2023-06-07 22:31 UTC](https://news.ycombinator.com/item?id=36234566)
  I'm speaking out of ignorance and not criticism, why not just go with a commercial product at that price point? ^c36234566

  I can imagine many theoretical reasons like sourcing and availability but are there things beyond actual conjecture here

  - **fragmede** · [2023-06-07 23:00 UTC](https://news.ycombinator.com/item?id=36234862)
    Cost is a huge concern. A trivial design - filter strapped to a box fan costs \$50. A product specifically design for the purpose could cost upwards of \$500. For something that most people don't pay attention, it's an unnecessary purchase. With most Americans being unable to afford an emergency \$500 purchase, of course a cheap DIY solution would be at the forefront. It's only due to the emergency nature of the need that most people are buying one in the first place, so there's also that. ^c36234862

  - **hedora** · [2023-06-07 23:24 UTC](https://news.ycombinator.com/item?id=36235082)
    This is pretty comparable (but includes a pm 2.5 meter, auto regulates itself, and has half as many filters).  It costs \$700: ^c36235082

    [https://www.usa.philips.com/c-m-ho/air-purifier-and-air-humi...](<https://www.usa.philips.com/c-m-ho/air-purifier-and-air-humidifier/air-purifier-5000>)

  - **winrid** · [2023-06-08 05:00 UTC](https://news.ycombinator.com/item?id=36237420)
    They actually work really well and are 10x cheaper. It's also fun. ^c36237420

    For many people on HN they won't get it. \$500 isn't a lot for an appliance right? For many that's two months groceries...

- **bullen** · [2023-06-08 07:30 UTC](https://news.ycombinator.com/item?id=36238460)
  I only use [https://www.sharpconsumer.com/home-appliances/hg40el/](<https://www.sharpconsumer.com/home-appliances/hg40el/>) ^c36238460

  It runs silently at lowest and humidifies the air too.

  It uses one container of water per day.

  I filter the tap water so it doesn't clog up the filter.

  I disable the ionisation feature which makes particles stick to the walls and furniture.

- **ahaucnx** · [2023-06-07 23:13 UTC](https://news.ycombinator.com/item?id=36234986)
  Working in this field and living in Northern Thailand which has similar high levels of air pollution from wildfires every year, I have spend many years making my house safe from air pollution. ^c36234986

  Box fans with HEPA filters are a good immediate and emergency solution but have their drawbacks, mainly:

  1) The fan and filter fights against particles coming in from outside, through small cracks under the doors, windows etc. So the higher the outdoor air pollution, the more the fan needs to fight against it. At extremely high pollution levels they will get into problems maintaining healthy air indoors.

  2) Sealing the gaps and making your house/room more air tight, increases CO2 levels significantly which leads to drowsyness and decreased mental performance. So you always work with a trade-off.

  3) Often you need to run the fans on highest level to be effective which creates quite a high level of noise.

  4) Ideally you want something demand controlled that switches automatically on/off or regulates its speed based on the pollution levels.

  5) The HEPA filters filter primarily PM2.5 but the wildfires also produce hazardous gases like NOx, VOCs which you would need carbon filters to remove.

  With my company AirGradient (we offer open source air quality monitors \[1\]), we monitor thousands of indoor spaces and the only technology that we found consistently working -no matter of the level of air pollution- are positive pressure systems.

  A positive pressure fresh air system takes air from outside, filters it through HEPA/Carbon filters and pumps it into the room. Thereby pressurizing the room and thus preventing dirty air from entering the room.

  With this system you just need to achieve a slightly higher pressure then outdoors and then you can consistently achieve zero PM levels inside -even when hazardous outdoors. As a result the system, often runs at low fan speeds and does not create much noise.

  Additionally, due to the fact that it uses fresh air, the CO2 levels remain low and you can often add carbon filters to the system.

  I made a comparison test of this type of system \[2\] and a detailed description how it works \[3\].

  \[1\] [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>)

  \[2\] [https://www.airgradient.com/open-airgradient/blog/air-purifi...](<https://www.airgradient.com/open-airgradient/blog/air-purifier-vs-positive-pressure-fresh-air-system-an-unfair-battle/>)

  \[3\] [https://www.airgradient.com/open-airgradient/blog/positive-p...](<https://www.airgradient.com/open-airgradient/blog/positive-pressure-systems-for-clean-air/>)

  - **dogline** · [2023-06-07 23:27 UTC](https://news.ycombinator.com/item?id=36235106)
    While I'm sure that your product is wonderful, setting up a positive pressure system is a bit more work.  The intent here is to get something working on an internal pressure space and have it work well, which it seems to do. ^c36235106

    - **ahaucnx** · [2023-06-07 23:33 UTC](https://news.ycombinator.com/item?id=36235164)
      The DIY box fans are a good emergency solution but with climate change these events will become much more frequent and more permanent solutions to make your house safer should be looked at. ^c36235164

- **odensc** · [2023-06-07 22:10 UTC](https://news.ycombinator.com/item?id=36234338)
  Isn't \$100 (the stated cost to make this) the same as a proper air purifier like a Levoit Core 300? ^c36234338

  - **adanto6840** · [2023-06-08 02:12 UTC](https://news.ycombinator.com/item?id=36236316)
    The Levoit, and basically all 'consumer' purifiers, are extremely under-powered and generally have *very* low air clearance rates & CFM.  Usually relatively/overly expensive filters, too. ^c36236316

    To get a remotely apples-to-apples comparison, look at commercial air purification systems -- think devices intended for areas that allows indoor smoking, such as bars/casinos/smoking rooms/etc.

    My experience was that a relatively modest 20x20 (x12' high) room requires a massive amount of air movement, and products actually designed for spaces of that size generally run \$3-6k or more.

    A Corsi-Rosenthal box can delivery very good PM2.5/PM10 numbers, even with challenging environments & when "stretched" to provide purification for an entire home.

    PurpleAir or a similar quality AQ monitor provides some very objective data to guide you;  I trashed my Levoit purifiers rapidly after realizing just how ineffective (and expensive) they were versus a CR box.

    - **crazygringo** · [2023-06-09 15:33 UTC](https://news.ycombinator.com/item?id=36259363)
      Really not sure what you're talking about. ^c36259363

      The Levoit moves a *lot* of air on its highest setting. The filter is \$23 and lasts for 6-8 months. It works amazingly and effectively in a bedroom or living room or office. I know, I use them and measure my indoor air quality with an Awair.

      The CR box is probably far more powerful, yes, but it's also gigantic. You'd never put it in a bedroom or living room. I'm honestly not sure *where* you'd put it.

  - **crazygringo** · [2023-06-07 23:14 UTC](https://news.ycombinator.com/item?id=36234992)
    Seriously. Plus the Levoit gives you adjustable fan speed to balance noise vs effectiveness, set a timer, it tells you when to replace your filter, it looks nice and professional rather than garage hardware, etc. ^c36234992

    If it were a quarter the price then I appreciate a DIY thing, but this is already in the same ballpark price-wise as the best-selling air purifier on Amazon. I don't get it.

  - **Rebelgecko** · [2023-06-08 01:19 UTC](https://news.ycombinator.com/item?id=36235959)
    These sorts of fan setups also use a lot more electricity than a dedicated air filter with similar stats. Not a big deal if you're just running it for a few days, but something to keep in mind. ^c36235959

  - **Forbo** · [2023-06-07 22:14 UTC](https://news.ycombinator.com/item?id=36234380)
    The Levoit filters are twice as expensive to replace. ^c36234380

    - **odensc** · [2023-06-07 22:30 UTC](https://news.ycombinator.com/item?id=36234549)
      What is that calculation based off of? The article lists the 4 filters as \$70 (which I'd assume you would replace all at once). ^c36234549

      The Levoit uses 1 filter "unit", and filters are \$55 for a 2-pack on Amazon (\$27.5/ea), or half that if you trust the third-party ones.

      Levoit recommends to replace the filters every 6-8 months, so you could get 12-16 months of filtration for \$55. I can't find any calculation in the article for how long the author estimates their filters would last.

    - **crazygringo** · [2023-06-08 00:00 UTC](https://news.ycombinator.com/item?id=36235360)
      They don't seem like it. ^c36235360

      Levoit filters are advertised as lasting 6–8 months and cost \$23 each.

      Meanwhile a set of four filters like the one in the tutorial cost \$70 and looking up comparables online at that price point indicates they're good for 3 months.

      So even if using 4 at a time extends to 12 months, that's still *more* expensive than the up-to-2 Levoit filters you'd use in that time.

      I see zero cost benefit here over Levoit -- it seems to be *more* expensive actually?

      - **neogodless** · [2023-06-09 11:14 UTC](https://news.ycombinator.com/item?id=36256131)
        The Levoit mentioned (I have one) is tiny and only good for a small room. The comparison box fan filter can clean a lot more air over the same time period. ^c36256131

        - **crazygringo** · [2023-06-09 15:34 UTC](https://news.ycombinator.com/item?id=36259389)
          It's good for a large room, not just a small one. I have one too. ^c36259389

          The CR box is tremendous overkill for something like an apartment. It's gigantic and I don't even know where most people would put one even in a house.

          But it's also not what the original post was talking about. The original post is a device akin to a Levoit in terms of size and power.

- **ipsum2** · [2023-06-07 21:54 UTC](https://news.ycombinator.com/item?id=36234150)
  You can also make this with a box fan, construct a box with 4 filters of roughly the same size as the fan, the bottom of the box can be cardboard. Did this back in 2019 and it works great, though I ended up switching to a Coway a few years later because of the noise. ^c36234150

- **Jeff\_Brown** · [2023-06-07 22:56 UTC](https://news.ycombinator.com/item?id=36234829)
  Why does it work better? ^c36234829

  I see that in the test he compares four filters being used completely in the cube setup to three being used incompletely on a box fan. But that doesn't seem like it can be the entire explanation -- particularly given the reduced airflow of the duct fan.

- **unknown** · [2023-06-07 21:57 UTC](https://news.ycombinator.com/item?id=36234197)
  [deleted] ^c36234197

- **binarymax** · [2023-06-07 22:12 UTC](https://news.ycombinator.com/item?id=36234364)
  The haphazard assembly of his box fan doesn't look ideal.  If you're going to do it that way at least get a 20x20 size furnace filter and use some duct tape to seal it. ^c36234364

- **tiahura** · [2023-06-08 00:40 UTC](https://news.ycombinator.com/item?id=36235654)
  Wouldn’t 2 single filter box fans placed in different locations be more effective at moving air around an apartment or house than a single cube? ^c36235654

- **ozmaverick72** · [2023-06-08 00:43 UTC](https://news.ycombinator.com/item?id=36235678)
  I'm guessing the smoke from the fires in Canada is responsible for a lot of the interest in this post ?? ^c36235678

- **mustyoshi** · [2023-06-07 22:05 UTC](https://news.ycombinator.com/item?id=36234282)
  He casually mentioned using the same (dirty) filters for the box fan run, how much did that skew the results? ^c36234282

  - **Tyr42** · [2023-06-07 22:10 UTC](https://news.ycombinator.com/item?id=36234340)
    You don't replace the filters every hour do you?  It's on e a month or once a season for our furnace filters at least. ^c36234340

  - **sp332** · [2023-06-07 23:17 UTC](https://news.ycombinator.com/item?id=36235021)
    With only a few sticks of incense in there, probably none. ^c36235021

- **flaburgan** · [2023-06-07 22:17 UTC](https://news.ycombinator.com/item?id=36234415)
  Can we fix one of these filter at the back of my PC? Would that actually work? ^c36234415

  - **dsr\_** · [2023-06-07 22:49 UTC](https://news.ycombinator.com/item?id=36234740)
    In order to prevent dust buildup inside the PC? Yes. ^c36234740

    In order to meaningfully clean the room's air? Not on one PC, with any reasonable number of fans.

    - **dogline** · [2023-06-07 23:29 UTC](https://news.ycombinator.com/item?id=36235124)
      I dunno.  With some people talking about how many CFM they can move with their fan system, maybe a filter or two would just add to things. ^c36235124

    - **ilyt** · [2023-06-07 22:55 UTC](https://news.ycombinator.com/item?id=36234813)
      Some big radiator + unreasonably sized fans PC+filter build would be *interesting* at the very least ^c36234813

- **chrislan815** · [2023-06-07 22:06 UTC](https://news.ycombinator.com/item?id=36234289)
  bro that's insane ^c36234289

