# [Air Purifier vs. Positive Pressure Fresh Air System – An Unfair Battle?](https://news.ycombinator.com/item?id=36234510)

Article: [https://www.airgradient.com/open-airgradient/blog/air-purifier-vs-positive-pressure-fresh-air-system-an-unfair-battle/](<https://www.airgradient.com/open-airgradient/blog/air-purifier-vs-positive-pressure-fresh-air-system-an-unfair-battle/>)

ahaucnx · 2023-06-07 22:26 UTC · 115 reported comments · archived 2026-11-08 13:04 UTC
Observation: 2026-11-08 13:03 UTC → 2026-11-08 13:04 UTC

## Comments

- **ahaucnx** · [2023-06-07 23:22 UTC](https://news.ycombinator.com/item?id=36235066)
  Author of the article, happy to answer any questions. ^c36235066

  A bit of background, my house is in Northern Thailand that has similar levels of air pollution every year than what we see currently in North America and Canada and it took me a few years to get my house to zero PM even when having the worst wildfires around. So before installing a positive pressure system and making my house air tight in the process, I experienced with all types of air purifiers but did not find anything that works consistently at very high pollution levels.

  The experience with these wildfires let me actually found AirGradient and we are proud of open sourcing many of our air quality monitors.

  - **\_Nat\_** · [2023-06-08 00:56 UTC](https://news.ycombinator.com/item?id=36235782)
    Seems like the big drawback of the positive-pressure approach would be flushing the heating/cooling out, too (as you've said in the article).  That drawback would seem to be proportional the flowrate of the positive-pressure airflow. ^c36235782

    So what if you redo your experiment with lower positive-pressure flows?  This is:

    1\. Keep the 280-m\^3/hr purifier on the whole time.

    2\. Start with the 220-m\^3/hr positive-pressure system running.

    3\. Wait for the particulate-level to equilibrate, then record the particulate-level and the pressure-difference (between outside and inside).

    4\. Reduce the air-flow of the positive-pressure system by, say, 20-m\^3/hr.

    5\. Loop back to Step-3 while the air-flow of the positive-pressure system isn't negative.

    With the objective to be to determine how low the positive-pressure system's flowrate can get while still maintaining its benefits, reducing heating/cooling losses.

    - **ahaucnx** · [2023-06-08 01:11 UTC](https://news.ycombinator.com/item?id=36235899)
      The system that I am having in place now is connected to our indoor air quality monitor and constantly regulates the fan speed of the PPS. By measuring the CO2 levels in the room, I can also detect when the room is actually occupied.
      This works extremely efficient and by playing around with the parameters can be optimized for cleaner air vs energy efficiency (or both). ^c36235899

      So in a way it does exactly what you say and finds the ideal equilibrium to keep just the right amount of pressure needed.

      - **hedora** · [2023-06-08 03:24 UTC](https://news.ycombinator.com/item?id=36236777)
        Air to air heat exchangers will help a lot with energy loss. ^c36236777

        Now that we have a CO2 meter, I am strongly considering wiring it to an air exchanger and having a PID controller just keep the house co2 below 600-800 ppm, and the pm 2.5 below 10 ug/m3.

    - **MichaelZuo** · [2023-06-08 22:23 UTC](https://news.ycombinator.com/item?id=36250059)
      \> Seems like the big drawback of the positive-pressure approach would be flushing the heating/cooling out, too (as you've said in the article). ^c36250059

      There are lots of enthalpy recovery systems on the market, some that can recover \>75\% of the 'waste' energy, though mostly aimed at larger customers. You need to do a cost-benefit analysis to see if it makes sense to spend the upfront cost.

      - **\_Nat\_** · [2023-06-09 01:03 UTC](https://news.ycombinator.com/item?id=36251763)
        Yeah, looks like you're right: \[waste-heat recovery systems\]([https://en.wikipedia.org/wiki/Waste\_heat\_recovery\_unit](<https://en.wikipedia.org/wiki/Waste_heat_recovery_unit>) ). ^c36251763

        Guessing that there are two main scenarios there:

        1\. A leaky house where positive-pressure causes flows to come out of various leaks all around.

        2\. A well-sealed house where positive-pressure causes flows to leave through a well-defined channel.

        The first-case might be harder to recover heat/coolness from, as the (high/low)-temperature air might leak in a way that'd be harder to make use of it.

        The second-case would seem to offer a stream of warmer/cooler air that could be used with a heat-exchanger or heat-pump or something.

        To note it, well-sealed houses might have issues with relatively poor ventilation, making positive-pressure more desirable -- much like how the OP describes wanting to keep CO2-levels down with their positive-pressure system.

  - **Cocktail** · [2023-06-08 07:13 UTC](https://news.ycombinator.com/item?id=36238351)
    Do you have any issues with mold after air tightening the house? 
    Here in Finland pretty much every house needs constant airflow/intake and the houses built to breathe to fight against mold.
    Im curious if youve had any issues, especially due to living closer to the tropical zone. ^c36238351

    - **Bluestrike2** · [2023-06-08 12:47 UTC](https://news.ycombinator.com/item?id=36240969)
      The problem is solved, barring serious complications with your home's envelope, with mechanical ventilation systems that give you control over how and where air is being exchanged in your house, while filtering it as well. That's assuming your building envelope doesn't have any serious issues; if water is leaking into wall assembly because of a poorly installed roof or gutter system, for example, no amount of ventilation is going to keep things from rotting away in a few years. ^c36240969

      Anyhow, although leaky houses can help deal with moisture, that's pretty much an incidental effect. Leaky homes also comes with significant expense in the form of heat loss, worsened indoor air quality, pathways for bugs to enter the home, etc. There's a reason why we've been moving towards ever-tighter houses, even with the upfront costs and effort required for air sealing, insulation, and mechanical ventilation.

      In the GP's tropical climate, I'd expect that humid air leaking into the house does very little to actually dry out the wall cavities; if anything, there's a good chance that those leaks would do the opposite and support any mold growth.

    - **regularfry** · [2023-06-08 08:16 UTC](https://news.ycombinator.com/item?id=36238766)
      When I got my basement damp-proofed against a nasty mould problem there were three options for how it could be done.  In increasing order if effectiveness, they were:  1) they could re-plaster with a sealant; 2) they could mount plastic stand-off sheets to the wall with plasterboard covering; 3) they could air-tighten and install a positive pressure system. ^c36238766

      So PPSes are sold as a damp prevention mechanism; as long as you install one when you air-tighten it's doing the job that natural airflow would otherwise take care of.

      Also worth noting: each successive option added a zero to the price.

    - **valenterry** · [2023-06-08 09:52 UTC](https://news.ycombinator.com/item?id=36239379)
      He won't because it's Thailand. The air inside the house won't be significantly warmer than outside for a prolonged period of time. Not so in Finland. ^c36239379

      Your best option is a centralized or decentralized automatic ventilation system with heat exchanging and humidity control. On top of that, the better the insulation the less the air is cooling down near walls/windows and the less likely the humidity is condensing into water causing mold. And then last, the less humid the air inside the house is, the more it can cool down before condensation is happening - so keep the humidity low not only with automatic ventilation but also by making sure to not cause humidity by cooking, showering (and breathing, haha) and if you do, air out for just a few minutes.

      - **2rsf** · [2023-06-08 10:31 UTC](https://news.ycombinator.com/item?id=36239654)
        What do you mean by humidity control? a central one? ^c36239654

        I am not saying you don't need one, but here in Sweden modern houses do not use humidity controls and are still air tight and mold free, maybe at the cost of letting more air and energy be swapped. Older houses have local vents at the baths which are humidity sensitive and will blow out excess humidity quickly, again at the cost of wasted energy.

        I suppose that controlling humidity centrally will somewhat save energy, but at what cost and complexity?

        - **valenterry** · [2023-06-08 11:53 UTC](https://news.ycombinator.com/item?id=36240336)
          Well, unless you stop breating, showering, cooking, keeping plants indoors, etc. you will have to somehow moderate/control the humidity as it will grow over time until the dew point close to walls/windows or other cold surfaces is reached. ^c36240336

          The reason why houses in Sweden can be mold free is because people get taught that they need to air out their house on a regular basis. And if you look it up, it tells you to air out not during noon (even though it's warmer so you lose less energy) but in the morning and late evening - specifically for humidity control.

          So...

          \> maybe at the cost of letting more air and energy be swapped

          Yes, exactly that. But since we are in the context of air pollution, opening windows to air out isn't a great idea. That's why I mentioned an automatic ventilation system (which pretty much always contains filters).

          \> Older houses have local vents at the baths which are humidity sensitive and will blow out excess humidity quickly, again at the cost of wasted energy.

          Not only that, fresh air will also be sucked in from somewhere else outside - which then again brings the air pollution inside.

          - **2rsf** · [2023-06-08 14:01 UTC](https://news.ycombinator.com/item?id=36242032)
            All new houses here have mechanical ventilation, usually with heat recovery and heat pumps but without filtering (excluding the heat pump's coarse filter for dust). ^c36242032

            I got curious and read a little, it is generally accepted here that higher pressure in the house can actually lead to mold, maybe because there is no moisture control and it is expected that some of the moisture generated in the house will be driven into the walls, probably assuming the walls are not perfectly sealed. On the other hand air pollution in Sweden is a non-issue, except maybe for a couple of streets in Stockholm.

            - **valenterry** · [2023-06-08 19:19 UTC](https://news.ycombinator.com/item?id=36247201)
              Yeah that makes sense - if you have clean air then why would you need to filter. :) ^c36247201

      - **davemp** · [2023-06-08 11:06 UTC](https://news.ycombinator.com/item?id=36239915)
        Ideally you would have a an air tight house with a mix of interior and exterior insulation based on your min/max temperature deltas and their dew points to keep the sheathing from being too cold ^c36239915

        - **valenterry** · [2023-06-08 11:49 UTC](https://news.ycombinator.com/item?id=36240297)
          That alone is insufficient. Think about the bathroom: the air will be hot and very humid. The walls would have to be way too hot to have a dew point that isn't reached when then hot&humid air cools down at the wall. ^c36240297

          So you are left with reducing the humdity by airing out in some way (with windows, with a very non-airtight building, or using automatic ventilation). Or, of course, you can use a dehumidifier.

  - **tjmc** · [2023-06-08 01:13 UTC](https://news.ycombinator.com/item?id=36235913)
    HVAC engineer here. I'd be interested to know if you've done any measurements with outside air coming through standard F5 filters. This is the typical setup for most ducted AC I come across. Much lower pressure and cheaper than HEPAs. It would be good to know what air quality results as a baseline and also in conjunction with in room purification if you have any data. ^c36235913

    Edit: I'm in Australia. Here's a comparison of filter types for different locations: [https://www.filtermakers.com.au/selection-guide/](<https://www.filtermakers.com.au/selection-guide/>)

    - **ahaucnx** · [2023-06-08 04:37 UTC](https://news.ycombinator.com/item?id=36237277)
      No, we only tested with true HEPA filters. ^c36237277

      One important thing to point out with PPS systems is that you need to get the air from fully polluted to zero polluted in ONE pass as unlike air purifiers, there is no recirculation. So the filter quality is super important.

      - **tjmc** · [2023-06-08 05:11 UTC](https://news.ycombinator.com/item?id=36237506)
        Agreed. Unfortunately we usually only see HEPAs in hospital theatres, CSSDs and the occasional lab. Air quality standards are still very lacking here. They haven't been updated since COVID or the east coast bushfires in any way. ^c36237506

    - **trog** · [2023-06-08 05:47 UTC](https://news.ycombinator.com/item?id=36237724)
      Not sure how to read that guide, but would an F5 filter out smoke well? ^c36237724

      - **tjmc** · [2023-06-08 06:40 UTC](https://news.ycombinator.com/item?id=36238109)
        No they wouldn't. Typically outside air systems shut off in fire mode, but they often keep running if there's smoke due to air pollution. If you need to deal with this you need a HEPA. ^c36238109

        An alternative for critical facilities like datacentres, is they often just go into recirculation mode. This wouldn't work in locations with persistent air polution.

  - **sampo** · [2023-06-08 10:57 UTC](https://news.ycombinator.com/item?id=36239838)
    I have a pet peeve about graphs with bad / non-existent labeling. ^c36239838

    Here is how to read the graph: The black line is the outside air PM2.5. The green-yellow-orange-red bars are the indoors air PM2.5.

  - **frognumber** · [2023-06-08 00:27 UTC](https://news.ycombinator.com/item?id=36235541)
    I have air filters in all my rooms. I guess my questions are: ^c36235541

    1) What should I do to get up to PPS? Should I just run a tube to their inlets through my window?

    2) How is heating / cooling handled? The weather here swings wildly. I'd be reluctant to pump hot or freezing air in. Might work well in spring / fall which are peak allergy season, though.

    3) What's a good way to monitor air quality on the cheap?

    I'm looking for opinionated recommendations.

    - **ahaucnx** · [2023-06-08 00:55 UTC](https://news.ycombinator.com/item?id=36235774)
      1) The first DIY PPS that I built used a small duct fan drawing air from outside and pushing it through a hepa filter to the inside. It is important to use duct fans as you need to create air pressure more than air flow and box fans are not built to create the amount of pressure required. ^c36235774

      2) Ideally you get a PPS system with a heat recovery unit. Also important is to have the PPS demand controlled based on an indoor air quality monitor that measures PM and CO2 and then only pushing in the right amount of air to meet your target values for PM and CO2. This way you can save a lot of energy costs and temperature differentials.

      3) Thanks for asking ;) We maintain popular open source air quality monitor kits that are very easy to assemble and use industry grade sensors \[1\]

      \[1\] [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>)

      - **mlpinit** · [2023-06-08 04:02 UTC](https://news.ycombinator.com/item?id=36237027)
        I was looking for something like this. ^c36237027

        Friendly note: "Join thousands of makers builing their" that's probably meant to be "building".

        - **ahaucnx** · [2023-06-08 07:26 UTC](https://news.ycombinator.com/item?id=36238428)
          Thanks. Fixed. ^c36238428

    - **rapjr9** · [2023-06-08 04:19 UTC](https://news.ycombinator.com/item?id=36237133)
      I've been looking for an inexpensive PPS with heat exchanger that fits in a window (preferably an Andersen window, the kind that opens sideways, but maybe that's too much to ask).  Since there don't seem to be any on the market (for any kind of window) I'm working on a design of my own.  I think that two CPU coolers connected by their CPU plates with one pushing air out and one drawing air in would make a cheap heat exchanger.  Then possibly running a large hose from the outflow of that to the air intake on a small HEPA air purifier would create a simple, cheap PPS.  I know the pressure would not be high inside the house, but it would be a cheap way to introduce fresh air without losing heat/cooling and would help create a small positive pressure, without having to cut big holes in the walls. ^c36237133

      - **rocqua** · [2023-06-08 07:18 UTC](https://news.ycombinator.com/item?id=36238390)
        CPU coolers are tuned for 300 watts cooling at a delta of 60ish degrees centigrade (100ish Fahrenheit). ^c36238390

        You'd be operating at a much lower delta, split over two coolers. At best, the transfered power would scale with the delta, due to tuning it might scale worse.

        I think you might be better off just skipping the heat-pipes of cpu coolers and using aluminum plates positionned in both airflows.
        CPUs need heat-pipes because the heat source is sooo small. Here your heat source will be much bigger, especially in terms of surface area.

        - **rapjr9** · [2023-06-08 09:49 UTC](https://news.ycombinator.com/item?id=36239363)
          Interesting, so in Winter, say the outside temp is 20F and inside temp is 69F, that's a 49F difference.  In Summer, say the outside temp is 85F and the inside temp is 68F, a 17F difference.  Maybe I'd get at best 50\% heat recovery in the Winter and 25\% in the Summer?  That's a lot better than no recovery.  I like the aluminum plate idea, maybe two big heat sinks with long fins attached back to back with the air blowing through the fins would work better and be cheaper.  I like the fact that the CPU coolers are somewhat plug and play though, the fans are already integrated and power supplies are easily available.  Both approaches are fairly easy and cheap to try.  Wikipedia offers some insight on heat pipes: ^c36239363

          [https://en.wikipedia.org/wiki/Heat\_pipe](<https://en.wikipedia.org/wiki/Heat_pipe>)

          So what is the working temperature range for CPU cooler heat pipes?  Though they maybe be optimized for 100F temperature difference, CPU's also don't always run at full speed and maximum power.  So perhaps CPU coolers would still be useful at lower temperature differentials (and lower absolute operating temperatures.)

          - **rocqua** · [2023-06-08 18:36 UTC](https://news.ycombinator.com/item?id=36246541)
            \>  I like the aluminum plate idea, maybe two big heat sinks with long fins attached back to back with the air blowing through the fins would work better and be cheaper. ^c36246541

            That's not quite what I meant. I effectively meant: just make one big, wide heatsink. Then have the intake run through the left side of the heatsink and outtake through the right side. No 'heat transfer between the heatsinks' needed.

            - **rapjr9** · [2023-06-10 20:43 UTC](https://news.ycombinator.com/item?id=36274891)
              Hmmm, there would still need to be heat transfer inside the heat sink from one side to the other via the bottom plate.  Maybe that would still be more efficient than the transfer via a larger contact area between two heat sinks back to back?  Not sure...either would probably work.  What I can build might depend on the geometry and size of the heat sinks that are easily available.  One big heat sink would make construction a little easier. ^c36274891

  - **domoritz** · [2023-06-08 13:31 UTC](https://news.ycombinator.com/item?id=36241583)
    It’s great that PPS can reduce PM2.5 and CO2 to extremely low levels. I live in an area with industrial pollution (coal etc) and am concerned about VOCs, NOXs, SO2s etc as well. Wouldn’t I bring in more of those if I constantly bring in outside air even when the pollution is high outside? Unfortunately I haven’t been able to exactly identify the chemical that’s causing issues for me yet. I’d love to hear your thoughts on this situation. ^c36241583

  - **\_Nat\_** · [2023-06-08 01:14 UTC](https://news.ycombinator.com/item?id=36235920)
    Have you explored the effects of a localized positive-pressure system? ^c36235920

    Like, say the positive-pressure system has a duct that pumps outside-air directly to locations where a resident spends a lot of them time -- like their bed, a work desk, or a couch in a living-room.  Could they get reasonable air-quality that way, even if the system isn't strong enough to clean up other areas of their home that they might spend less time in?

    - **ahaucnx** · [2023-06-08 04:40 UTC](https://news.ycombinator.com/item?id=36237299)
      Yes, this is what I am doing in my house. Pump the cleaned fresh air into the peripheral rooms (mostly bedrooms) and then this actually pressures the whole house (living room, bathrooms etc). ^c36237299

  - **usbinsider** · [2023-06-08 04:41 UTC](https://news.ycombinator.com/item?id=36237302)
    What was the filtration level of the filter system? What was the orientation/positioning? ^c36237302

    I’m wondering if the airflow was in a loop but not mixing the entire room, or the filter wasn’t Hepa (or close), or it wasn’t reaching its claimed throughput/filtration, etc.

    I recently installed a Merv13+Merv16 filter on my newly upgraded HVAC system and am able to drive PM2.5 to 0 with a minimal fan setting of roughly 2ACH. (Granted, we haven’t had wildfire smoke that strongly since installing it, but I induce bad air from time to time and it cleans it up quickly.)

  - **stephen\_g** · [2023-06-08 11:59 UTC](https://news.ycombinator.com/item?id=36240401)
    What kind of NOx and SOx readings do you get? (I assume the AirGradient sensors can measure that?). Do you think an activated charcoal filter is a worthwhile addition? ^c36240401

  - **WhatIsDukkha** · [2023-06-08 00:02 UTC](https://news.ycombinator.com/item?id=36235375)
    What do you need for a 700sqft space built tight? ^c36235375

    So its going to make the minisplit work harder but to what extent at 30 and 40 degree air outside?

    - **ahaucnx** · [2023-06-08 00:57 UTC](https://news.ycombinator.com/item?id=36235792)
      I have seen PPS systems work from small rooms to whole sports halls. If you have a large temperature/humidity differential between inside and outside, I would recommend looking for units with heat recovery system. ^c36235792

  - **aulin** · [2023-06-08 05:53 UTC](https://news.ycombinator.com/item?id=36237764)
    what about Radon? ^c36237764

- **sbirch** · [2023-06-07 23:25 UTC](https://news.ycombinator.com/item?id=36235095)
  You might conclude that the only real option is to buy a positive pressure fresh air system, but this comparison doesn't match my experience. I have no trouble driving the PM2.5 very close to 0 with a few standalone purifiers in my house (verified with a couple air quality monitors) even during bad wildfire smoke events. I'll grant I live in a modern house which is pretty well sealed, but it's also a question of sizing the purifier to the room's size and drafts. ^c36235095

  There are some orthogonal advantages and disadvantages though. On the upside, you'll reduce CO2 and other pollutants from inside your house -- it can get quite stuffy when you can't ventilate due to poor outdoor air quality. A downside is that it may also bring in air at a different temperature or humidity than you'd like (though that can also be controlled to some extent with a HRV/ERV.)

  - **ahaucnx** · [2023-06-07 23:30 UTC](https://news.ycombinator.com/item?id=36235129)
    I agree, if you have a modern house you could bring down the levels with air purifiers but having no fresh air exchange really makes the house feeling very stuffy and you could get into very high CO2 levels which have its own set of health impacts. ^c36235129

    - **stinos** · [2023-06-08 05:49 UTC](https://news.ycombinator.com/item?id=36237735)
      *but having no fresh air exchange* ^c36237735

      That 'but' isn't a given, modern houses which are properly sealed should have ventilation as well specifically to address that issue. Proper ventilation comes with inlet filters but those usually don't keep out PM\<x\> so still the purifier will have to do sme more work because of the constant sucking in of polluted air. However, I honestly do not know how common venitlation is already on other continents than mine where it's been made pretty clear by now that sealing a house equals need for ventilation.

  - **DANmode** · [2023-06-08 00:24 UTC](https://news.ycombinator.com/item?id=36235517)
    What if the goal isn't to reduce measurable air particles, but remove more mold spore "attempts" from adhering to surfaces in your home? Could positive pressure be superior in that case? ^c36235517

    - **rocqua** · [2023-06-08 07:23 UTC](https://news.ycombinator.com/item?id=36238415)
      Positive pressure does 'one shot' filtering. All air in the house goes through the HEPA filter once. Hence any spores (or other patrickes) that get filtered, get filtered immediately. Though spores (or particles) that make it through the filter get to linger indefinitely. ^c36238415

      It sounds like a good filter and PPS would meet your goal.

      - **FredPret** · [2023-06-08 08:06 UTC](https://news.ycombinator.com/item?id=36238695)
        Particles that get through the HEPA filter will get pushed out of the house by the positive pressure. Unless your house is literally airtight and you never leave ^c36238695

  - **thebigman433** · [2023-06-08 00:25 UTC](https://news.ycombinator.com/item?id=36235524)
    What air quality monitors do you use? ^c36235524

  - **coda\_** · [2023-06-07 23:34 UTC](https://news.ycombinator.com/item?id=36235168)
    That's impressive... What are you using for purifiers? ^c36235168

    - **nerdbaggy** · [2023-06-08 00:07 UTC](https://news.ycombinator.com/item?id=36235417)
      I use the Alen Air 75i and have no issues getting my PM2.5 to 0 ^c36235417

      [https://alen.com/products/alen-breathesmart-75i-air-purifier...](<https://alen.com/products/alen-breathesmart-75i-air-purifier?variant=13172054491203>)

      - **bradknowles** · [2023-06-08 07:11 UTC](https://news.ycombinator.com/item?id=36238337)
        The best air filters I have found are the IQAir HyperHEPA filters, which are rated to filter ≥ 99\% at 0.003 microns, which is smaller than a virus particle. That's why these are commonly used in hospitals.
         See: [https://www.iqair.com/us/air-purifiers](<https://www.iqair.com/us/air-purifiers>) ^c36238337

      - **virtuallynathan** · [2023-06-08 00:25 UTC](https://news.ycombinator.com/item?id=36235522)
        That one seems a bit pricey, I think the best I’ve seen for CADR per dollar is the Conway 400(S) or Medify MA-112. ^c36235522

        - **LTL\_FTC** · [2023-06-08 03:23 UTC](https://news.ycombinator.com/item?id=36236774)
          I went down a rabbit hole when California nearly burned down in 2020 and after lots of research came to the conclusion that buying 7x \$100 hepa filters is better than buying 1x \$700 filter. So an inexpensive Winix ended up being the best for me. One for each room. More air cycles and much less noise when they're scattered throughout the house. This is just for particulate matter. If one cares about volatile organic compounds, VOC's, they need to invest is several pounds heavy charcoal filters. The thin ones that come on most filters don't do anything other than act as a pre-filter to catch the large particles. ^c36236774

          - **rocqua** · [2023-06-08 07:26 UTC](https://news.ycombinator.com/item?id=36238434)
            From what I know, this holds for air purifiers. Quantity of air moving through matters more than quality of the filter, because of re-circulation. ^c36238434

            The cool part of a PPS to me is that, because it is a one-shot system (no recirculation) it can actually take advantage of high quality filters.

            - **LTL\_FTC** · [2023-06-09 04:06 UTC](https://news.ycombinator.com/item?id=36252999)
              Yes, sorry. By filters I meant air purifiers with HEPA filters in them. The more cycles, the better. ^c36252999

        - **nerdbaggy** · [2023-06-08 00:29 UTC](https://news.ycombinator.com/item?id=36235567)
          Yeah they are expensive but the best I have found. The 45i is for like 700 square feet for \$400. The nice part about Alen purifiers is the filters last just about a year and lifetime warranty ^c36235567

          - **bmitc** · [2023-06-08 01:15 UTC](https://news.ycombinator.com/item?id=36235924)
            What type of filter is that? HEPA filters are recommended to be changed every few months. ^c36235924

            - **nerdbaggy** · [2023-06-08 01:53 UTC](https://news.ycombinator.com/item?id=36236184)
              Yeah they are HEPA and according to the link below it’s good for 12-15 months ^c36236184

              [https://alen.com/products/alen-breathesmart-75i-hepa-filter?...](<https://alen.com/products/alen-breathesmart-75i-hepa-filter?variant=40426983292993>)

    - **ahaucnx** · [2023-06-07 23:39 UTC](https://news.ycombinator.com/item?id=36235214)
      The positive pressure system is from a local supplier in Thailand and only available in Thailand and China. PM me if you need more information. ^c36235214

      - **atombeef** · [2023-06-08 06:12 UTC](https://news.ycombinator.com/item?id=36237912)
        I'm curious about what supplier and system you're using? I'm currently using a bunch of smartair purifier, that gets indoor pm2.5 to close to zero even when it gets really bad outside every year (also in Thailand). But considering installing a positive pressure (ducted) system with HEPA filter due to high co2 levels (tightly sealed house and no ventilation) ^c36237912

        - **erkkie** · [2023-06-09 17:09 UTC](https://news.ycombinator.com/item?id=36260839)
          Curious too (also in Thailand), currently using smartair and Ikea Starkwind for PM/VOCs. ^c36260839

          Looking to design something more integrated with CO2, house cooling, de-humidifying aspects included (controlled by HA).

          Have you entertained heat exchange systems? Thoughts on the magnitude of impact to aircon?

    - **bmitc** · [2023-06-08 01:15 UTC](https://news.ycombinator.com/item?id=36235921)
      I am using Vornado air purifiers, but I don't have air quality monitoring yet and don't care about WiFi features. The higher end Vornados have monitoring built-in, but it is rudimentary and just a light bar. Without air monitors to check them, it's hard to tell, but they seem to work quite well. Vornado excels at producing room-sized torrents that direct air through its filters. We blew out a candle once and the smoke visibly made a beeline towards the Vornado. ^c36235921

- **c\_o\_n\_v\_e\_x** · [2023-06-08 03:04 UTC](https://news.ycombinator.com/item?id=36236673)
  Former HVAC and controls guy here.  If you are going to the trouble of putting in a PPS, why not measure and control the fan speed based off of static pressure inside the space?  You could measure your static pressure at a point furthest from the fan or you have multiple static sensors and select/control based off the lowest reading. ^c36236673

  The pressure only needs to be just slightly above ambient to keep the dirty ambient air out of the home.  Providing unnecessary extra flow/pressure is doubly bad - one because your are spending extra energy to over-pressurize the space, two because your exchanging more outside air and thus the delta T between inside and outside.

  Another consideration is that if your flow/pressure is too high, you'll have trouble trying to open/close exterior doors.

  - **usbinsider** · [2023-06-08 05:08 UTC](https://news.ycombinator.com/item?id=36237484)
    What’s a good sensor to do that with over the long term? ^c36237484

    - **c\_o\_n\_v\_e\_x** · [2023-06-08 05:27 UTC](https://news.ycombinator.com/item?id=36237604)
      You need a differential air pressure sensor.  I couldn't tell you any brands that would fall in the DIY price range.  Dwyer is a big name in the commercial space. ^c36237604

      - **rocqua** · [2023-06-08 07:29 UTC](https://news.ycombinator.com/item?id=36238457)
        Might it be possible to DIY a differential sensor by taking two callibrated air pressure sensors, and subtracting their difference in software? ^c36238457

        Would solve needing holes in walls, etc.

- **bb88** · [2023-06-08 03:29 UTC](https://news.ycombinator.com/item?id=36236809)
  In my office I have a Costco MERV 13 furnace filter tied to a box fan.  I am down to 0 PM2.5 after a couple of hours. ^c36236809

  In my case it's just a 20" box fan with a 20" square filter bungee corded together.

  The filters last 3-4 months, but are commodities at this point.

  - **29athrowaway** · [2023-06-08 03:33 UTC](https://news.ycombinator.com/item?id=36236841)
    That's a clever trick. Creating the air pressure with a box fan and then filtering using a MERV filter. I guess if you can find a 20x20 box fan and attach a 20x20x1 filter to it you can do this easily. ^c36236841

    But how much the filters last depend on a variety of factors. If you have pets (with fur) your filters will last much less.

    - **bredren** · [2023-06-08 07:23 UTC](https://news.ycombinator.com/item?id=36238411)
      It is called a Cosri-Rosenthal box \[1\].  I've built three variations on these using different kinds and sizes of Filtrete filters they are very cheap and effective. ^c36238411

      The downsides are that they take up a lot of space, are a big eye sore and awkward to carry and move. They also can make a lot of (white) noise on high, which can mask sounds you want to hear.

      They're great for special situations like wildfires or out of the way areas like basements where looks don't matter.

      For common living spaces we use Coway Airmega AP1512's which are relatively compact, auto cycle up and down fan speed and are much more attractive than DIY stuff.

      \[1\] [https://en.wikipedia.org/wiki/Corsi\%E2\%80\%93Rosenthal\_Box](<https://en.wikipedia.org/wiki/Corsi%E2%80%93Rosenthal_Box>)

      - **29athrowaway** · [2023-06-08 13:50 UTC](https://news.ycombinator.com/item?id=36241883)
        And replacing the filter is problematic. ^c36241883

    - **bb88** · [2023-06-08 03:45 UTC](https://news.ycombinator.com/item?id=36236925)
      What's interesting is that if you look on amazon, MERV 13 filters + Bungee Cords + 20" box fans are commonly ordered together.  Further you can do a 20x20x4" MERV 13 to increase the lifespan of the filters. ^c36236925

      It also beats the price of buying specialized HEPA filters for a particular brand of air filter.

    - **lamontcg** · [2023-06-08 06:10 UTC](https://news.ycombinator.com/item?id=36237901)
      Make a cube out of 4 MERV 13 filters and a box fan on top and the cardboard the box fan came in on the bottom and secure it with duct tape.  That'll help reduce the load on the box fan and push more air through more filters. ^c36237901

  - **hollerith** · [2023-06-08 05:51 UTC](https://news.ycombinator.com/item?id=36237755)
    There is a report of a fire started by overheating of the box fan motor in such an ad-hoc purifier. The box fan is not designed for this application. ^c36237755

    Humbly suggest not running this unattended.

    - **bredren** · [2023-06-08 07:17 UTC](https://news.ycombinator.com/item?id=36238380)
      This concern comes up often against DIY filtration systems like this but I've yet to see a study showing this to be the case. ^c36238380

      I have seen this study \[1\] that says no fire hazard is created by motor stress from these kinds of setups.

      \[1\] [https://en.wikipedia.org/wiki/Corsi\%E2\%80\%93Rosenthal\_Box](<https://en.wikipedia.org/wiki/Corsi%E2%80%93Rosenthal_Box>)

    - **btbuildem** · [2023-06-08 13:04 UTC](https://news.ycombinator.com/item?id=36241191)
      A properly built CR box (bottom base, four filter walls, fan on top) relieves this concern. Ample airflow around the fan and four filters let enough air through. ^c36241191

    - **hollerith** · [2023-06-08 14:52 UTC](https://news.ycombinator.com/item?id=36242845)
      (Replying to myself.) ^c36242845

      Here is the report I refer to:

      [https://news.ycombinator.com/item?id\=21382994](<https://news.ycombinator.com/item?id=21382994>)

- **ttul** · [2023-06-08 07:57 UTC](https://news.ycombinator.com/item?id=36238617)
  The magic that everyone needs is a combination of a) heat recovery ventilation (HRV) and b) heat pumps. ^c36238617

  An HRV system passes filtered air through a heat exchanger from the inside to the outside and vice versa. The air passes through a heat exchanger that ensures the interior and exterior remain the same temperature. You end up with fresh, clean air inside your house that has been filtered without changing the interior air temperature.

  Combining an HRV with a heat pump completes the picture, giving you both fresh air and a comfortable temperature, with no need to open the windows and let smoke in.

  - **2rsf** · [2023-06-08 10:57 UTC](https://news.ycombinator.com/item?id=36239843)
    Don't forget ground source for the heat pump. ^c36239843

    - **sagarm** · [2023-06-08 16:46 UTC](https://news.ycombinator.com/item?id=36244848)
      Air source heat pumps apparently work pretty well and are much more practical to retrofit. ^c36244848

      - **2rsf** · [2023-06-08 17:09 UTC](https://news.ycombinator.com/item?id=36245237)
        Much more practical, and yes the improvement is small especially in not so cold countries ^c36245237

- **taeric** · [2023-06-07 23:04 UTC](https://news.ycombinator.com/item?id=36234894)
  I thought the general view was that outside air was what you wanted for a lot of reasons?  I know the general advice was "open windows and hasten air exchange."  Is that out the window if you can keep the place pressurized? ^c36234894

  - **kshahkshah** · [2023-06-07 23:16 UTC](https://news.ycombinator.com/item?id=36235015)
    "It depends" ^c36235015

    If you're in an older building (leaky) with a recirculating range hood (not actually vented) then opening a window is going to improve your air. Many prewar buildings in NYC were constructed with 'overpowered' radiators by the windows with the idea that people would in winter have the windows slightly ajar to bring in clean air.

    In a more modern building with a tight thermal envelope (not leaky) you're not passively through cracks, etc. exchanging w/the outside world. So everything builds up. One solution is a fresh air system like an ERV or HRV which exchanges air, filters, and exchanges heat and humidity too (so an improve version of keeping the window open).

    My 1985 run of the mill center hall colonial is moderately leaky. If I run the bathroom fans a negative pressure environment is created and air is pulled from under the slab (which creates a radon concern, for me). I suspect this approach, slightly pressurizing every room, would work for me. But I think this is very similar to what an HRV/ERV might do anyway...

    - **jaggederest** · [2023-06-07 23:52 UTC](https://news.ycombinator.com/item?id=36235306)
      You can set the air balance in most ERV/HRV to be positive or negative. I think the rule of thumb is that they almost always are set to provide slight positive pressure, to avoid drafting e.g. gas appliance exhaust into the house, but I'm not a HVAC expert, just someone looking into them for residential usage. ^c36235306

    - **pivo** · [2023-06-07 23:34 UTC](https://news.ycombinator.com/item?id=36235167)
      \> Many prewar buildings in NYC were constructed with 'overpowered' radiators by the windows with the idea that people would in winter have the windows slightly ajar to bring in clean air. ^c36235167

      Wow, thank you! I've always wondered why the heat seemed so unnecessarily overwhelming in radiator buildings I grew up in. We'd keep the windows open because there was no way to control the heat and I'd always thought it was such a waste of energy. Not sure how clean the outside air was at the time, but I did really miss the mix of cold and warm air in the winter when I moved to a more modern building.

      - **blamazon** · [2023-06-08 00:30 UTC](https://news.ycombinator.com/item?id=36235579)
        One explanation for this phenomenon is that the initial rapid proliferation of 'modern' radiators in NYC happened around the same time as the 1918 influenza pandemic. It was understood that fresh air was something of an antidote. Tangentially, people wore masks as well during that global pandemic \[1\] and there were even anti-mask groups. \[2\] It makes me wonder what a pandemic a hundred years from now would be like and what physical manifestations of 2020 will remain. ^c36235579

        \[1\]: [https://twitter.com/georgiatech/status/1307410628470956032](<https://twitter.com/georgiatech/status/1307410628470956032>)

        \[2\]: [https://en.wikipedia.org/wiki/Anti-Mask\_League\_of\_San\_Franci...](<https://en.wikipedia.org/wiki/Anti-Mask_League_of_San_Francisco>)

    - **ilyt** · [2023-06-07 23:51 UTC](https://news.ycombinator.com/item?id=36235305)
      Interesting, I always assumed the "overpowered" radiators were just to compensate relatively bad window isolation. ^c36235305

  - **Georgelemental** · [2023-06-07 23:40 UTC](https://news.ycombinator.com/item?id=36235216)
    Not when the outside air is full of wildfire smoke, I would think… ^c36235216

    - **taeric** · [2023-06-08 14:22 UTC](https://news.ycombinator.com/item?id=36242331)
      Perfectly fair.  And I guess the real question is how rapidly the air in a building is recirculated? ^c36242331

  - **ilyt** · [2023-06-07 23:52 UTC](https://news.ycombinator.com/item?id=36235309)
    *well*, to pressurize it you need to take the air from outside, constantly. ^c36235309

- **jdavis703** · [2023-06-08 00:23 UTC](https://news.ycombinator.com/item?id=36235510)
  My experience from west coast wildfires and taking indoor air pollution measurements is if I put 3 air purifiers in one master bedroom and keep the windows and doors closed I can go from code purple air outside to code orange air inside… So it’s not perfect, but it does kind of work if you’re in a situation where you can’t integrate a positive air pressure system. ^c36235510

  - **crazygringo** · [2023-06-08 01:34 UTC](https://news.ycombinator.com/item?id=36236060)
    Something would seem to be wrong in your situation then, just one should be enough to get it to green if windows and doors are closed. ^c36236060

    Not sure if your filters need to be replaced, if you need to wipe dust off their exteriors, or something is just wrong with their airflow that they're not filtering.

    A \$100 Levoit purifier (the longtime Amazon bestseller) has been keeping my bedroom in the green (measured by an Awair) while it's been maroon (400+) AQI outside today here in NYC.

    - **29athrowaway** · [2023-06-08 02:39 UTC](https://news.ycombinator.com/item?id=36236487)
      With those you have to vacuum it every 2 weeks and change the filter every 6 months. ^c36236487

      - **bagacrap** · [2023-06-08 03:38 UTC](https://news.ycombinator.com/item?id=36236877)
        Changing a filter every 6 months sounds more than reasonable to me ^c36236877

        - **29athrowaway** · [2023-06-08 13:51 UTC](https://news.ycombinator.com/item?id=36241891)
          Yes. Just saying that the filter is not simply an appliance that runs forever. ^c36241891

  - **29athrowaway** · [2023-06-08 05:22 UTC](https://news.ycombinator.com/item?id=36237569)
    Air filters are often for particulate matter but not VOCs. ^c36237569

    Or radon. Sometimes trees pump the radon from deeper groundwater and the radon levels rise when trees burn.

    - **ricardobayes** · [2023-06-08 08:40 UTC](https://news.ycombinator.com/item?id=36238915)
      Radon is interesting because not a lot of people think about it, yet it's very dangerous. It's almost everywhere in France, Germany and Scandinavia. If you don't have anti-radon measures in the mentioned countries, high chances are levels are exceeding the limit. ^c36238915

    - **stephen\_g** · [2023-06-08 10:37 UTC](https://news.ycombinator.com/item?id=36239708)
      You can get activated charcoal filters to help. But just having positive pressure (ideally with the intake vent a decent distance from the ground, since radon is quite a lot heavier than air) should help, because radon usually seeps in through the foundation due to pressure in the ground, and the fact that lower levels of houses are often natural at a slight negative pressure. ^c36239708

  - **ninacomputer** · [2023-06-08 00:33 UTC](https://news.ycombinator.com/item?id=36235600)
    This is too real and relatable. We take clean air so for granted huh. ^c36235600

  - **unknown** · [2023-06-08 05:20 UTC](https://news.ycombinator.com/item?id=36237561)
    [deleted] ^c36237561

- **infoseek12** · [2023-06-08 00:29 UTC](https://news.ycombinator.com/item?id=36235562)
  One day I’d love to build a house with positive pressure and a glass topped courtyard. Designed correctly I think you could achieve very low pollution and CO2 levels even if the air outside is awful. The details get complicated though. ^c36235562

  - **zo1** · [2023-06-08 12:56 UTC](https://news.ycombinator.com/item?id=36241097)
    I'd love to do that as well - my idea would also involve a large body of water to stabilize the temperature variations. It can double-up as a swimming pool and as a source of drinking water for the "coming apocalypse". Likewise, the water can be used to grow some plants in that glass-topped courtyard, that can act as a greenhouse. ^c36241097

- **Shank** · [2023-06-08 00:56 UTC](https://news.ycombinator.com/item?id=36235776)
  \> Installation. Unlike an air purifier that you just plug-in, a positive pressure system needs to be installed. This means you need to break a 4 or 6-inch hole into your wall for the air intake and install an air outlet in your wall or ceiling. \[0\] ^c36235776

  Hmm, my apartment has a 4-6 inch hole for air exchange in the living room, but is otherwise a tight air envelope due to being a relatively modern building. Is there...something I can buy for this? This seems reasonably doable, unless I'm missing something obvious.

  \[0\]: [https://www.airgradient.com/open-airgradient/blog/positive-p...](<https://www.airgradient.com/open-airgradient/blog/positive-pressure-systems-for-clean-air/>)

  - **amluto** · [2023-06-08 01:30 UTC](https://news.ycombinator.com/item?id=36236036)
    This is a nice balanced system.  I don’t know whether it can run in a positive pressure mode: ^c36236036

    [https://products.zehnder-systems.com/en/product/zehnder-comf...](<https://products.zehnder-systems.com/en/product/zehnder-comfoair-70>)

    Its big sibling, the Q series, can run balanced or at a configurable amount of imbalance.

    These are really neat, but they’re intended for a pair of holes in different rooms. Maybe you can get one and get it to run in supply only mode:

    [https://www.lunos.de/heat-recovery](<https://www.lunos.de/heat-recovery>)

  - **Too** · [2023-06-10 04:12 UTC](https://news.ycombinator.com/item?id=36267525)
    You surely have air egress in your bathroom and kitchen fan? Modern apartments usually have these on low speed all the time, creating a flow from the rest of the intakes in other rooms. ^c36267525

- **chuckledog** · [2023-06-08 04:36 UTC](https://news.ycombinator.com/item?id=36237270)
  We created a cheap effective DIY positive pressure system and it’s been working well for about a year now.
  Intake: old Winix filter, HEPA ish, broken fan removed, nice filter changability.  Fits in joist bay, faces down drawing air from a protected exterior part of the house.  \$50/yr
  … connected with a steel hvac boot to…
  Duct Fan: AC Infinity 6” leave it on 1/10
  … connected with 10’ of 4” duct to another hvac boot which blows air into a floor register in the bedroom. ^c36237270

  We have 3 of these, always on, ready for the next round of purple air

  Edit: house is in mild climate California

- **andai** · [2023-06-08 08:18 UTC](https://news.ycombinator.com/item?id=36238775)
  Do I understand that with a PPS, it's healthier to be inside than outside? (At least along the "fresh air" dimension.) ^c36238775

  Obviously there's sunlight, exercise, and health benefits to socializing, but I always thought fresh air was one of the main reasons to go outside.

  - **dsab** · [2023-06-08 08:33 UTC](https://news.ycombinator.com/item?id=36238868)
    It might be not so trivious, here in Poland life expectancy is the highest in Kraków, where there is also the highest air pollution due to location. ^c36238868

- **turtlebits** · [2023-06-08 03:28 UTC](https://news.ycombinator.com/item?id=36236802)
  Why not both? I have an ERV setup for positive pressure and constant air purifier running on low. ^c36236802

- **mhb** · [2023-06-08 00:27 UTC](https://news.ycombinator.com/item?id=36235539)
  It would be helpful if you labeled the top curve (outside air) and the lower bars (inside air). ^c36235539

- **prvc** · [2023-06-08 09:04 UTC](https://news.ycombinator.com/item?id=36239074)
  Any strategies for maintaining positive pressure in a dwelling in which installation/ deployment must be reversible (i.e. must not destroy any part of the dwelling)? ^c36239074

  - **btbuildem** · [2023-06-08 13:08 UTC](https://news.ycombinator.com/item?id=36241258)
    You could look at how window AC units are installed -- "temporary" (ie, reversible, but long-term) installations, using various kits that generally boil down to foam strips and extensible accordion partitions to close off space not filled by the unit. ^c36241258

- **micro\_cam** · [2023-06-08 00:09 UTC](https://news.ycombinator.com/item?id=36235427)
  Does anyone make a quality standalone pps with a heat recovery ventilator? I’d buy one I could retrofit in without existing ducting in a second. ^c36235427

  - **amluto** · [2023-06-08 01:32 UTC](https://news.ycombinator.com/item?id=36236051)
    Heat recovery and positive pressure are a bit at odds.  Zehnder and Lunos both make cut-a-hole-in-a-wall ventilation systems. ^c36236051

- **drakenot** · [2023-06-08 02:15 UTC](https://news.ycombinator.com/item?id=36236330)
  What air quality monitors are y’all using? ^c36236330

  - **bb88** · [2023-06-08 04:19 UTC](https://news.ycombinator.com/item?id=36237137)
    There's a bunch but a lot of them are going to have something like this plantower sensor: ^c36237137

    [https://www.aliexpress.us/item/3256801607354554.html](<https://www.aliexpress.us/item/3256801607354554.html>)

    It's a off the shelf part easily manufactured and possibly also easily calibrated.

    As a bonus you can hook it up to a Raspberry Pi or ESP32 board if you want.

  - **LTL\_FTC** · [2023-06-08 03:34 UTC](https://news.ycombinator.com/item?id=36236849)
    Purple air has some nice monitors and I think IQair also has one. ^c36236849

    - **geerlingguy** · [2023-06-08 04:09 UTC](https://news.ycombinator.com/item?id=36237075)
      If you're talking about the author of OP, I'm guessing he uses the AirGradient sensors, since he made them :) ^c36237075

      I like them enough I'm now up to four in my home. They did send two for evaluation initially (I did a video on them last year) but I liked them and bought more. I reflash them to ESPHome so I can easily pop them into Home Assistant.

- **ninacomputer** · [2023-06-08 00:33 UTC](https://news.ycombinator.com/item?id=36235595)
  Picked up a filter purifier here and it's in good use now with the fires. Wish I could get the more fancier and more functional options, but they are so expensive with demand. ^c36235595

