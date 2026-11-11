# [A small DIY air purifier](https://news.ycombinator.com/item?id=22104874)

Article: [https://github.com/Kels316/DIY-Air-Purifier](<https://github.com/Kels316/DIY-Air-Purifier>)

Rondom · 2020-01-21 07:06 UTC · 168 reported comments · archived 2026-11-08 11:16 UTC
Observation: 2026-11-08 11:15 UTC → 2026-11-08 11:16 UTC

## Comments

- **lmilcin** · [2020-01-21 10:16 UTC](https://news.ycombinator.com/item?id=22105641)
  Air quality test before and after or it doesn't work. ^c22105641

  I am very suspicious with regards to air purifiers. Have you ever seen real HEPA filter? It is thick and it is quite difficult to push air through it. I can't imagine small PC fan that is designed to push air through UNOBSTRUCTED space will make any significant flow of air. I have spent some time with the guys who build PCs and who know great deal about fans and one thing I learned even an object that the air has to pass around or any kink in the path of air can severly impact performance of PC fan. Because they are designed to be quiet and still provide good flow of air they produce almost no pressure differential to speak of and the flow can be halved by a wire mesh that is a bit too dense.

  You need to cycle the air in your room through the filter couple of times to clean it, assuming your filter is any good.

  The cheap fan in the picture would barely be able to cycle the air in a small room maybe once an hour, if it was completely unobstructed. It is very likely that with any kind of HEPA filter the flow will drop by an order of magnitude.

  Go with suggestion of other readers. If you want good, cheap filter, use a box fan and especially one that was designed to give good pressure difference. Take large cardboard or plastic box and mount large HEPA filter in it so that the air has to pass through. The larger the surface of the filter the easier time the fan will have to push the air through it and more efficient it will be.

  - **0-\_-0** · [2020-01-21 11:04 UTC](https://news.ycombinator.com/item?id=22105857)
    \> Because they are designed to be quiet and still provide good flow of air they produce almost no pressure differential to speak of and the flow can be halved by a wire mesh that is a bit too dense ^c22105857

    There are high static pressure fans which address this problem, specifically designed to work with pressure differential, usually used to blow air through radiators for water cooling. The fan linked in the github page (Noctua NF-F12, the "cheap fan" in the picture) is such a fan, it provides a static pressure of 7.63 mmH2O, which is very high.

    Edit: you can get regular-sized 12cm pc fans that need 48 watts and rotate at 7160rpm, move 7.160 m\^3/min air at 35.877 mmH2O static pressure:

    [https://www.frozencpu.com/products/8147/fan-500/Delta\_Mega\_F...](<https://www.frozencpu.com/products/8147/fan-500/Delta_Mega_Fast_120mm_x_38mm_Fan_-_252_CFM_-_Bare_Lead_PFB1212UHE-F00_No_RPM.html?tl=g36c435s1109>)

    - **qpiox** · [2020-01-21 11:58 UTC](https://news.ycombinator.com/item?id=22106130)
      \> it provides a static pressure of 7.63 mmH2O, which is very high. ^c22106130

      Actually, it depends on the specific HEPA filter if that is enough or not. If it's not enough, the air will find the path of less resistance and circulate in and out thru the fan blades, but not thru the filter.

      For some HEPA filters you can find specs. These ([https://www.airclean.co.uk/download/4724](<https://www.airclean.co.uk/download/4724>)) are spec to 250 Pa which would be about 25 mm H2O if I am correct.

      - **maxerickson** · [2020-01-21 12:16 UTC](https://news.ycombinator.com/item?id=22106238)
        Even if they don't recirculate, I sort of doubt that these small fans are going to achieve sufficient air flow through the filter (a radiator is much less of an obstruction than a HEPA filter). ^c22106238

    - **avian** · [2020-01-21 11:40 UTC](https://news.ycombinator.com/item?id=22106030)
      \> it provides a static pressure of 7.63 mmH2O ^c22106030

      If anyone else is wondering, that's about 0.8 mbar (roughly 8 ten-thousands of an atmosphere), or 80 Pa of over-pressure.

      To put this into perspective, my local atmospheric pressure varied about 2000 Pa in the last 48h due to weather changes.

      - **labawi** · [2020-01-21 22:49 UTC](https://news.ycombinator.com/item?id=22112595)
        IMO, absolute pressure doesn't give much of a perspective. ^c22112595

        Car tire pressure is about 1.8-2.5 Bar.

        Your 2000 Pa atmospheric pressure change is about 20 mBar.

        Pressure in an inflated balloon is about 2 mBar (0.002 Bar).

        Noctua's static pressure is 0.8 mBar. Let's call it 0.5 mBar dynamic working pressure.

        Not as low as I expected. Not sure if it will have a semi-reasonable speed, but that will definitely push some air.

        Another comparison, 0.5 mBar is 50 Pa \= 50 N/m². That gives about 50 \* 0.3 \* 0.3 / 10 \~ 0.5 kg force on a 30x30 cm² surface.

        Finally, as the article video and data shows, it does actually work.

        \[1\] [http://scipp.ucsc.edu/outreach/balloon/labs/InflationExp.htm](<http://scipp.ucsc.edu/outreach/balloon/labs/InflationExp.htm>)

        - **avian** · [2020-01-22 06:32 UTC](https://news.ycombinator.com/item?id=22115135)
          That balloon figure doesn’t make sense to me in relation to atmospheric pressure changes. It would mean that a tied-off balloon would randomly inflate and deflate itself depending on weather. ^c22115135

          - **labawi** · [2020-01-22 12:56 UTC](https://news.ycombinator.com/item?id=22117092)
            It does, slightly. Pressure change 20 mBar \= 2\% of absolute atmospheric pressure -\> about 2\% balloon volume change, with corresponding 2\% internal absolute pressure change, while keeping the same low differential inside-outside pressure. ^c22117092

      - **wlesieutre** · [2020-01-21 13:59 UTC](https://news.ycombinator.com/item?id=22106898)
        Lemme go send my air intake through a time machine and as long as the weather keeps changing we can use that to drive air through a filter! ^c22106898

        - **avian** · [2020-01-21 14:24 UTC](https://news.ycombinator.com/item?id=22107087)
          No need for a time machine (or being snarky - I did say it's just for comparison, didn't I? I think it does put the "very high pressure" into perspective) ^c22107087

          That said, your time machine idea could be simply implemented with a large, airtight box. Simply put the filter over it and weather changes will push and pull air through the filter with two orders of magnitude more pressure than this little fan. Volume of filtered air will depend on the volume of the box though, so better get a large one.

        - **thatguy0900** · [2020-01-21 22:25 UTC](https://news.ycombinator.com/item?id=22112355)
          If you had a time machine you might as well just skip the filter and pull in air from before the industrial revolution directly ^c22112355

    - **eeZah7Ux** · [2020-01-21 11:55 UTC](https://news.ycombinator.com/item?id=22106112)
      [https://noctua.at/en/nf-f12-pwm/specification](<https://noctua.at/en/nf-f12-pwm/specification>) ^c22106112

      Static pressure 2,61 mm H₂O  \<-- according to the vendor

      - **0-\_-0** · [2020-01-21 12:19 UTC](https://news.ycombinator.com/item?id=22106253)
        I got it from here: ^c22106253

        [https://noctua.at/en/nf-f12-industrialppc-3000-pwm/specifica...](<https://noctua.at/en/nf-f12-industrialppc-3000-pwm/specification>)

        Or if you just follow the link on the linked page:

        [https://www.pccasegear.com/products/27866](<https://www.pccasegear.com/products/27866>)

  - **ddeck** · [2020-01-21 10:30 UTC](https://news.ycombinator.com/item?id=22105693)
    *\>The larger the surface of the filter the easier time the fan will have to push the air through it and more efficient it will be. * ^c22105693

    This is quite true. Assuming the media in your particle filter is of sufficient quality, the most important metric to look at is the aggregate surface area. The larger the surface area, the more air you will be able to move through it and the more particulate matter it will hold before requiring replacement.

    Particle filters use pleated media for this reason. It's not uncommon to see a filter with 1 square foot face having 50 square feet or more of media. Without specs, the thickness of the filter and the density of the pleating will give you a decent estimate of the filter area. To improve performance and longevity further, it's also typical to have a coarser, pre-filter.

    The machine itself is just a fan to push air through the filter and as noted, any reasonably powerful fan will do a sufficiently good job. High quality machines are only really required where you're filtering air before it enters a given area (e.g. LCD/semiconductor plants), and thus cannot afford to have any unfiltered air leak past the filter.

    - **lmilcin** · [2020-01-21 11:56 UTC](https://news.ycombinator.com/item?id=22106117)
      The quality of the filter is important if you want to remove very fine particles. ^c22106117

      Even good filters do not typically remove all particles, only particles above certain size. If you have cheap filter it may not even capture a portion of the particles you are interested to remove, it may remove none no matter how many times you cycle the air.

  - **cosmolev** · [2020-01-21 14:47 UTC](https://news.ycombinator.com/item?id=22107324)
    \+1. Together with a test in the same environment without a purifier at all. PM count drops down to almost 0 in a room with closed windows with a breathing person inside. Lungs of a person act as a perfect purifier. ^c22107324

    - **OJFord** · [2020-01-21 15:00 UTC](https://news.ycombinator.com/item?id=22107453)
      \> Lungs of a person act as a perfect purifier. ^c22107453

      Is that good?

      I mean, of course it's good that PM doesn't just pass straight into our bloodstream, but isn't our lungs doing the purifying exactly the thing that people try to avoid with mechanical air purifiers?

      - **cosmolev** · [2020-01-21 15:24 UTC](https://news.ycombinator.com/item?id=22107701)
        It is bad of course! PM does pass straight into our bloodstream. ^c22107701

        I was just talking about the test setup. A test of any purifier should be compared to a test with a person in a room without purifier. Otherwise those results are not significant.

      - **lm28469** · [2020-01-21 18:33 UTC](https://news.ycombinator.com/item?id=22109887)
        The whole point of filtering air for PMs is to avoid having them in your lungs so I'm pretty sure that's not "good". ^c22109887

        - **OJFord** · [2020-01-21 21:45 UTC](https://news.ycombinator.com/item?id=22111975)
          Yes, that is what I said. ^c22111975

    - **oiasdjfoiasd** · [2020-01-21 15:07 UTC](https://news.ycombinator.com/item?id=22107523)
      [flagged] ^c22107523

      LOL. Isn't that exactly the reason why you want a Purifier .

  - **DoctorOetker** · [2020-01-22 00:35 UTC](https://news.ycombinator.com/item?id=22113373)
    from a physics perspective there is nearly no lower limit on the pressure differential for a given flux (liters per second) of air (ignoring the mixing entropy). ^c22113373

    just make the analogy pressure \~ voltage, flux \~ current, filter \~ resistance.

    A doubling in flux can be achieved either by doubling the voltage across the resistor ( \~ doubling pressure differential across the filter), OR by halving the resistance of the filter ( \~ placing 2 filters in parallel,  without halving the filter thickness) so technically a PC fan could blow at a typical PC fan pressure differential and flow rate purified air across an arbitrary number of layers of HEPA, as long as enough of those \[N layers of HEPA\] in parallel...

- **kn100** · [2020-01-21 09:39 UTC](https://news.ycombinator.com/item?id=22105502)
  This is a really cool project but frankly you can do it a lot cheaper. Find the cheapest box fan you can find, and find the cheapest HEPA filter you can, and strap the HEPA filter to the front. To improve air purification even futher, slap an activated carbon filter on the front too, and your air purifier now filters VoCs!  For cheap Activated Carbon Filters, look into the kind used for Aquarium filters. They'll work just as well for air as far as I know. ^c22105502

  In China there is a whole company founded on doing just this, although they've since pivoted into selling specific air purification hardware at a significant discount. See: [https://smartairfilters.com/cn/en/product/diy-1-1-air-purifi...](<https://smartairfilters.com/cn/en/product/diy-1-1-air-purifier/>)

  - **post\_break** · [2020-01-21 14:01 UTC](https://news.ycombinator.com/item?id=22106915)
    If you want this to actually work, you take a box fan, and 2 filters. You make a triangle and then some cardboard on the top and bottom to fill the gap. This increases surface area and reduces the stress on the fan due to pressure drop. Slapping a filter directly on to the box fan is going to kill the fan very quickly.  [https://i.imgur.com/SX1RloH.jpg](<https://i.imgur.com/SX1RloH.jpg>) ^c22106915

    - **opencl** · [2020-01-21 14:22 UTC](https://news.ycombinator.com/item?id=22107069)
      I ran a few cheap box fans with filters directly over them for several years and none of them failed, I have heard this claim a lot but it seems overstated. The triangle setup *will* significantly increase the airflow and thus the effectiveness of filtration though. ^c22107069

      - **post\_break** · [2020-01-21 14:37 UTC](https://news.ycombinator.com/item?id=22107226)
        I guess it depends on the quality of filter. If you're rocking a high merv filter for smoke the pressure drop can be significant. ^c22107226

      - **nathancahill** · [2020-01-21 14:57 UTC](https://news.ycombinator.com/item?id=22107427)
        I've done this too for years and no issues. ^c22107427

    - **logfromblammo** · [2020-01-21 16:08 UTC](https://news.ycombinator.com/item?id=22108150)
      Or ditch the cardboard, and use 5 square HVAC filters to make a *true* "box fan". ^c22108150

      - **GR34T3R4L4RM** · [2020-01-21 18:50 UTC](https://news.ycombinator.com/item?id=22110044)
        [https://imgur.com/gallery/jtECP9C](<https://imgur.com/gallery/jtECP9C>) ^c22110044

      - **dredmorbius** · [2020-01-21 23:48 UTC](https://news.ycombinator.com/item?id=22113059)
        The HEPA filters are the expensive component.  Adding more filters doesn't improve net effectiveness. ^c22113059

        Cardboard is the vastly more cost-effective option.  And taping a HEPA filter directly to the back of the fan effective and proven.

        - **sliken** · [2020-01-22 01:00 UTC](https://news.ycombinator.com/item?id=22113513)
          Actually it does.  You'll get higher CFM through the system and it will take 5x longer to saturate the filters with dust.  The cost per month will actually be similar, granted you'll have a higher startup cost with 5 filters instead of 1. ^c22113513

          - **dredmorbius** · [2020-01-22 01:21 UTC](https://news.ycombinator.com/item?id=22113633)
            The time-to-saturate is a wash when you factor in per-filter rates.  You're achieving a 4x longer life per filter, but multiplying that by the 4x filters you are using. ^c22113633

            The net filtration rate *per filter* will fall as that's a function of flow rate \* filtration size.

            Yes, the four- or five-filter version will probably have a *slightly* better overall filtration rate ... but that's really not the principle constraint here.  A single-filter design will drop particle density by \~90\% in about 30 minutes.  That's sufficient.  It's doubtful the final particle density measurement will be much reduced (though if someone's got the data I'd be interested in seeing it), or that this reduction is clinically significant from a health perspective.  Remember that you're likely going *outside* the filtered area, so achieving perfection inside but spending a substantial fraction of your time in unfiltered or far-more-poorly-filtered air, isn't much of a win.

            Meantime, you're tying up 3-4 filters that you don't really need, and which others could make effective use of, for a very low marginal imrovement in your own experience.

            Where the filters themselves are in low supply -- typical for a region where a wildfire has errupted, and particularly true where filters aren't a high-volume item as with Australia presently -- designs which economise on filter use are a net social benefit.

    - **aj7** · [2020-01-21 14:49 UTC](https://news.ycombinator.com/item?id=22107345)
      Right.  And in general, duct tape and popsicle sticks take care if that housing. ^c22107345

    - **yjftsjthsd-h** · [2020-01-21 14:33 UTC](https://news.ycombinator.com/item?id=22107174)
      Clarification: triangle goes on the in or out side of the fan? ^c22107174

      - **post\_break** · [2020-01-21 14:36 UTC](https://news.ycombinator.com/item?id=22107215)
        Doesn't really matter as long as the filters are in the correct orientation. However it would be beneficial if the air is clean before it goes through the fan. ^c22107215

      - **spookthesunset** · [2020-01-21 17:29 UTC](https://news.ycombinator.com/item?id=22109073)
        Put it on the intake.  It will keep the fan clean. ^c22109073

    - **91aintprime** · [2020-01-22 19:27 UTC](https://news.ycombinator.com/item?id=22121071)
      [flagged] ^c22121071

      something something impedance matching

  - **mhd** · [2020-01-21 09:56 UTC](https://news.ycombinator.com/item?id=22105571)
    I don't know why, but I love the fact that someone is selling filters strapped to fans on a reasonably glossy and well-made page. ^c22105571

    - **OJFord** · [2020-01-21 15:03 UTC](https://news.ycombinator.com/item?id=22107482)
      It does kind of look like a joke doesn't it? A demo/how-to masquerading as a shop page. ^c22107482

  - **dublinben** · [2020-01-21 20:41 UTC](https://news.ycombinator.com/item?id=22111304)
    Here's a video from the University of Michigan showing just how effective these cheap DIY air filters can be: [https://www.youtube.com/watch?v\=kH5APw\_SLUU](<https://www.youtube.com/watch?v=kH5APw_SLUU>) ^c22111304

  - **marcinzm** · [2020-01-21 12:32 UTC](https://news.ycombinator.com/item?id=22106325)
    This may or may not work, cheap box fans aren't designed to push/pull air through obstructions (ie: low static pressure) and HEPA filters are giant obstructions. So instead of the air going through the filter it'll go through gaps, around the edges of the blades, etc. ^c22106325

    I used a cheap box fan for some DIY ventilation and the loss in airflow is massive after filter and ducting.

    - **jakeogh** · [2020-01-21 18:41 UTC](https://news.ycombinator.com/item?id=22109962)
      I have a box fan on low 24x7 with a 12 on the input and a 7 on the output. That's not a HEPA rated filter set, but it's fantastic. Allergy season just went away (while in my room) when I started using it a few years ago. I also tried a 3 on the output, and that worked as well, but the flow was noticeably lower. The fan is cheap, \$20. I change the filters every few months, and it always looks like I waited too long. ^c22109962

    - **UnFleshedOne** · [2020-01-21 20:47 UTC](https://news.ycombinator.com/item?id=22111381)
      I used a cheap box fan and a furnace filter held simply by pressure differential. ^c22111381

      Flow drops a lot, but it still works. Filter was dirty after some time. It was hilariously undersized for my purpose (serious belt-sander action leveling sub-floors), but air does move.

    - **Spooks** · [2020-01-21 13:18 UTC](https://news.ycombinator.com/item?id=22106604)
      couldn't you easily test this by sticking your hand (wet it first) in the middle section of the filter and see if you feel any air coming through ^c22106604

      - **dunkelan** · [2020-01-21 13:47 UTC](https://news.ycombinator.com/item?id=22106815)
        You could, but I think the goal would be to make sure the design will work before going through the effort of making it. If you already have all the parts though definitely worth a try. ^c22106815

  - **cosmolev** · [2020-01-21 15:28 UTC](https://news.ycombinator.com/item?id=22107733)
    I have smartairfilter's Cannon purifier. As all those standalone purifiers it works only with windows completely closed. ^c22107733

    I went for ventilation systems that take air from outside, filter it and then bring it inside the room. Namely Xiaomi MJXFJ-300-G1: [https://www.xiaomitoday.com/xiaomi-mijia-air-purifier-mjxfj-...](<https://www.xiaomitoday.com/xiaomi-mijia-air-purifier-mjxfj-300-g1-intelligent-household-filter-at-1040/>)
    I've installed one in every bedroom.

    - **driverdan** · [2020-01-21 15:54 UTC](https://news.ycombinator.com/item?id=22107993)
      That seems quite expensive for what it is. For that price I'd expect it to have an efficient heat exchanger. ^c22107993

  - **asah** · [2020-01-21 20:31 UTC](https://news.ycombinator.com/item?id=22111184)
    Can confirm: did this when the wildfires hit SF a couple years ago, and it really worked!! ^c22111184

    My "measurement" was my lungs when working from home: coughing before, no coughing after. Filters turned black.

  - **fareesh** · [2020-01-21 13:42 UTC](https://news.ycombinator.com/item?id=22106777)
    Would something like this this work sufficiently well to capture airborne fur/dander from a tabby cat? Or will there be a vastly different outcome from an expensive one? ^c22106777

    - **kevinconroy** · [2020-01-21 14:02 UTC](https://news.ycombinator.com/item?id=22106919)
      Yes! We have two box fans with HEPA filters in our bedroom to combat the cat fur/dander. It's made a world of difference. You can see it working as the filter captures everything. Have to change them monthly... but so worth it. \#YMMV \#YouCatsMayVary ^c22106919

      - **apta** · [2020-01-21 14:54 UTC](https://news.ycombinator.com/item?id=22107398)
        Do you strap them to the front or the rear of the fan? Doesn't having them on the front (i.e. where the air blows out) mean that the fan will get dirty since it's sucking the air in? ^c22107398

        - **Nexxxeh** · [2020-01-21 16:25 UTC](https://news.ycombinator.com/item?id=22108325)
          You may wish to use a cheap thin washable pre-filter either way. It will catch a lot of the hair before it hits the fine filtration, which you can then just wash off the pre-filter, making it easier and cheaper to maintain. ^c22108325

          - **fareesh** · [2020-01-21 17:53 UTC](https://news.ycombinator.com/item?id=22109383)
            Do you have a link to one of the cheap thin washable pre-filters that I can look at as a reference for what to buy? ^c22109383

            - **wang\_li** · [2020-01-21 21:30 UTC](https://news.ycombinator.com/item?id=22111831)
              Get some window screen from your local home improvement big box store. ^c22111831

  - **thehesiod** · [2020-01-21 11:05 UTC](https://news.ycombinator.com/item?id=22105863)
    know a way to get them to US reasonably?  cost is like 10x when shipping to US :( ^c22105863

    - **insensible** · [2020-01-21 12:39 UTC](https://news.ycombinator.com/item?id=22106362)
      In the US, grab a basic 20" box fan and toss on a 20x20x1 furnace filter like this one: ^c22106362

      [https://www.homedepot.com/p/Honeywell-20-in-x-20-in-x-1-in-A...](<https://www.homedepot.com/p/Honeywell-20-in-x-20-in-x-1-in-Allergen-Plus-Pleated-FPR-7-Air-Filter-90701-012020/203145810>)

      For extra flow, set up a triangle with the fan on one side and 2 of these filters on the intake end as the other two sides, and duct tape some cardboard to seal the top and bottom.

  - **dandare** · [2020-01-21 10:35 UTC](https://news.ycombinator.com/item?id=22105717)
    I came here to post the very same link :D ^c22105717

- **majos** · [2020-01-21 15:17 UTC](https://news.ycombinator.com/item?id=22107629)
  May as well ask here: do air purifiers have meaningful health benefits for generally healthy people? I get that you change the filter and it's filled with grey muck and that's gross, and that the filters change particulate content in air, but is there good evidence that doing those things improves health if you don't already have some sensitivity to air pollution or live in a highly polluted area? ^c22107629

  I don't know if "Lung India" is a great journal, but the "Efficacy of indoor air filters" section of this paper \[1\] doesn't offer much support. All studies are pretty small and focused on people with asthma or pet allergies. The few studies of populations without such conditions show what look to me like minor improvements, e.g. a \~5 mmHg drop in blood pressure. These aren't super strong studies though.

  The argument that pops up in pro-air-filter pieces draws a line through "air pollution can be a big health hazard" (true), "air filters reduce some particulate content in the air" (true), and "air filters improve health" (unclear). But the "big health hazard" conclusion seems to come from intensely polluted environments, like poorly-ventilated homes that use kerosene, or areas with lots of smoke. For a generic first-world home I can't find much evidence.

  \[1\] [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4587002/](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4587002/>)

  - **storyinmemo** · [2020-01-21 17:35 UTC](https://news.ycombinator.com/item?id=22109147)
    PM 2.5 seems to be like radiation: the more you get, the more you're likely to be affected, even at lowish levels. ^c22109147

    [https://qz.com/1166010/air-pollution-even-at-levels-that-mee...](<https://qz.com/1166010/air-pollution-even-at-levels-that-meet-national-standards-causes-premature-death/>)

  - **sl1ck731** · [2020-01-21 15:34 UTC](https://news.ycombinator.com/item?id=22107784)
    I would assume the majority of people (in the US, anyway) are already filtering their air enough through their central air to make any additional "room-sized" filtering negligible. ^c22107784

    Similarly they make some very dense HVAC filters if standard ones aren't catching the level of particles you need, so I'm not sure what the purpose of these filter-fan things are for *most* people.

    - **dr\_orpheus** · [2020-01-21 16:14 UTC](https://news.ycombinator.com/item?id=22108209)
      Dense HVAC filters make your HVAC systems run much less efficiently. There is less airflow and less heat transfer (either cooling or heating). Anyone that has come to service my air conditioner or furnace has always checked the filter and recommended never getting a denser filter.
      The filters in the HVAC system are more there to prevent your furnace from getting clogged up with larger particles than to help the indoor air quality. ^c22108209

    - **showerst** · [2020-01-21 15:53 UTC](https://news.ycombinator.com/item?id=22107984)
      In a previous house I rented, we swapped the furnace filter for a much finer one (from 8 to 13 on whatever scale they market these things in), and it made the HVAC system run noticeably worse. Lower airflow, noisier, etc. It seemed to me that the intake system couldn't keep up with the reduced flow of the denser filter. ^c22107984

      Could moving to a coarser filter but adding room filters be useful in that context?

    - **lotsofpulp** · [2020-01-21 17:30 UTC](https://news.ycombinator.com/item?id=22109087)
      \>Similarly they make some very dense HVAC filters if standard ones aren't catching the level of particles you need, so I'm not sure what the purpose of these filter-fan things are for most people. ^c22109087

      These are a scam, especially all those 3M filtrete ones.  Air handlers in homes and most other HVAC applications are not made to also serve as tiny particulate filters, so it will make the whole HVAC system slow or even stop since it won't be able to get the air flow it needs to function.

      - **djannzjkzxn** · [2020-01-21 18:56 UTC](https://news.ycombinator.com/item?id=22110116)
        I believe you that the HVAC isn’t designed for such a filter. But a few months back my home was in the path of smoke from some wildfires. The AQI went from 200 to 0 after I installed a filter and ran the house fan for an hour. Also, the furnace doesn’t have to work very hard here because of the mild climate, so I never have much of a heat bill anyway. It would be a bummer if the furnace died because of it running out of spec, but I’m skeptical that the risk-adjusted cost of that is higher than the cost of standalone filtration units. ^c22110116

        - **lotsofpulp** · [2020-01-21 19:15 UTC](https://news.ycombinator.com/item?id=22110347)
          This page has a decent explanation of the problem: ^c22110347

          [https://www.pvhvac.com/blog/whats-the-best-air-filter-for-yo...](<https://www.pvhvac.com/blog/whats-the-best-air-filter-for-your-home>)

          All the commercial HVAC technicians I speak to say to use the cheapest non fancy filters if your goal is to maximize life of the HVAC system, but I'm sure it all depends on everyone's specific system and how the return is and whatnot.

    - **cptskippy** · [2020-01-21 15:55 UTC](https://news.ycombinator.com/item?id=22107999)
      That assumes that your HVAC runs regularly. Apart from deep summer and winter we rarely run our house HVAC. ^c22107999

      We have a filter that runs constantly at low speed because we have pets and without the filter there would be issues for members of my family.

      - **unknown** · [2020-01-21 17:31 UTC](https://news.ycombinator.com/item?id=22109094)
        [deleted] ^c22109094

    - **0xffff2** · [2020-01-22 00:31 UTC](https://news.ycombinator.com/item?id=22113359)
      Do a large majority of people in the US even have central air? It's virtually unheard of to have an HVAC system in older buildings in California. ^c22113359

- **chewz** · [2020-01-21 11:10 UTC](https://news.ycombinator.com/item?id=22105886)
  This seems like useless toy. ^c22105886

  You should be aiming for something larger that would work for an apartment.

  \[1\] [https://youtu.be/kH5APw\_SLUU](<https://youtu.be/kH5APw_SLUU>)

  \[2\] [https://youtu.be/8Hkdpx-59kk](<https://youtu.be/8Hkdpx-59kk>)

  There is thousand vidoes on Youtube on how to DYI one.

  - **dredmorbius** · [2020-01-22 00:03 UTC](https://news.ycombinator.com/item?id=22113171)
    The problem for areas presently affected by high PM2.5 concentrations, most notably Australia, is that materials which are commonplace in the US, box fans, but especially box-fan-sized square HEPA furnace filters, are rare as hen's teeth. ^c22113171

    So alternate designs using available materials are required.

    (Or someone might drop ship a few containers worth of box fans and HEPA furnace filters down under.)

    - **brnt** · [2020-01-22 14:05 UTC](https://news.ycombinator.com/item?id=22117596)
      Same problem here. I've just spent close to an hour trying to locate a box fan for sale in Europe, couldn't find any resembling those I can easily find on amazon.com! ^c22117596

  - **yboris** · [2020-01-21 14:55 UTC](https://news.ycombinator.com/item?id=22107406)
    Thank you for sharing these two videos! I really like the 1st one with the air-quality-measuring-instrument. ^c22107406

    - **chewz** · [2020-01-22 10:35 UTC](https://news.ycombinator.com/item?id=22116265)
      You welcome. ^c22116265

      You can also make DYI air-quality instrument on a cheap using SDS011 sensor and Raspberry Pi. \[2\]

      \[1\] [https://aqicn.org/sensor/sds011/](<https://aqicn.org/sensor/sds011/>)

      \[2\] [https://www.raspberrypi.org/blog/monitor-air-quality-with-a-...](<https://www.raspberrypi.org/blog/monitor-air-quality-with-a-raspberry-pi/>)

- **loldot\_** · [2020-01-21 13:36 UTC](https://news.ycombinator.com/item?id=22106725)
  I don't know how effective they are compared to these devices, but I much prefer to keep plants with air purifying qualities. NASA did a study on a variety of air purifying plants in 1989: [https://ntrs.nasa.gov/search.jsp?R\=19930073077](<https://ntrs.nasa.gov/search.jsp?R=19930073077>) ^c22106725

  - **minikites** · [2020-01-21 14:39 UTC](https://news.ycombinator.com/item?id=22107245)
    You would need to live in an indoor rainforest (approximately 680 plants for a typical house) to see an effect on air quality, a spider plant in the corner isn't doing anything: [https://www.youtube.com/watch?v\=AmeiXikh0v8](<https://www.youtube.com/watch?v=AmeiXikh0v8>) ^c22107245

    - **csytan** · [2020-01-21 15:46 UTC](https://news.ycombinator.com/item?id=22107904)
      \*to see a similar effect on air quality as mentioned in the study ^c22107904

  - **sfgweilr4f** · [2020-01-21 14:45 UTC](https://news.ycombinator.com/item?id=22107300)
    Hasn't that been partially debunked or at least conditions placed on how effective they are? I lost the article that reviewed it. ^c22107300

    - **compressedgas** · [2020-01-21 18:04 UTC](https://news.ycombinator.com/item?id=22109514)
      Potted plants don't improve indoor air quality: [https://news.ycombinator.com/item?id\=21464423](<https://news.ycombinator.com/item?id=21464423>) ^c22109514

  - **trehalose** · [2020-01-21 15:04 UTC](https://news.ycombinator.com/item?id=22107494)
    That's an interesting study, but it appears to only study the plants' ability to filter out a few VOCs. HEPA filters won't help with those (you need an activated charcoal filter for that... or plants, I guess?), but they will help with particulates, and I'm not sure plants will do anything for those. ^c22107494

  - **24gttghh** · [2020-01-21 15:25 UTC](https://news.ycombinator.com/item?id=22107708)
    Last time I checked, most of those aren't safe for house pets either :/ ^c22107708

    - **clairity** · [2020-01-21 23:32 UTC](https://news.ycombinator.com/item?id=22112941)
      there's still a bunch you can buy. apparently many "toxic" plants are only mildly toxic for cats/dogs. ^c22112941

      i don't think they make much difference for air quality, but i bought some "air purifying" plants and cross-checked them against the aspca list for safety:

      [https://www.aspca.org/pet-care/animal-poison-control](<https://www.aspca.org/pet-care/animal-poison-control>)

      (my cat likes to munch on my spider plants, even with cat grass available)

- **storyinmemo** · [2020-01-21 16:27 UTC](https://news.ycombinator.com/item?id=22108341)
  This project would take 2-3 days to filter the volume of air in a 1,000 sq foot apartment... which is to say it would do nothing of significance. To be effective, you want to change the air something closer to once every 30 minutes. ^c22108341

  - **crispyambulance** · [2020-01-21 16:36 UTC](https://news.ycombinator.com/item?id=22108448)
    I agree that it would be silly to expect this thing to purify air for an entire living space. ^c22108448

    With a few adaptations, however, it might be good as a soldering station fume extractor. These already exist and are little more than a tube, a fan, and a filter (usually with activated charcoal).

    The nice thing about this one is that it's circular and could easily adapt to a flexible tube and you could perhaps stack fans for greater sucking power.

- **adrianN** · [2020-01-21 09:31 UTC](https://news.ycombinator.com/item?id=22105459)
  You could probably buy a box fan and tape a HEPA filter in front. ^c22105459

  - **packetslave** · [2020-01-21 09:31 UTC](https://news.ycombinator.com/item?id=22105461)
    This works shockingly well. They were quite popular during last year's California fires when "real" air purifiers were sold out everywhere. ^c22105461

    - **starpilot** · [2020-01-21 10:29 UTC](https://news.ycombinator.com/item?id=22105690)
      Also worked well in Seattle last summer. ^c22105690

  - **pureliquidhw** · [2020-01-21 13:41 UTC](https://news.ycombinator.com/item?id=22106766)
    You'll need to fill in the gaps around the fan blades. I did this with pink foam insulation. After that modification,place the filter on the back of the fan. If the filter suctions onto the fan that's a good sign you're pulling air through the filter and not from the front of the fan. ^c22106766

    - **dredmorbius** · [2020-01-22 00:10 UTC](https://news.ycombinator.com/item?id=22113212)
      There's going to be some reverse flow around the corners of the exhaust-side, but net net, so long as you've got sufficient flow and a sufficiently-rated filter, you'll be moving air through the filter and trapping particles within it. ^c22113212

      A circular exit mask might help slightly, but you're talking a few percent efficiency improvements, not a quantum leap in efficacy.

      Simple, cheap, available, and effective are the goals here.  Diminishing returns set in early.

  - **henryfjordan** · [2020-01-21 21:37 UTC](https://news.ycombinator.com/item?id=22111890)
    I have an "air purifier" from Amazon that's basically just that (but designed for it obviously). I'm not sure that the author is really saving much money by not just buying one. ^c22111890

- **JonathanFly** · [2020-01-21 11:38 UTC](https://news.ycombinator.com/item?id=22106018)
  Is that little fan really effective? I just duck taped a furnace filter to a 20 dollar box fan. No 3d printer needed. ^c22106018

  Just did this recently actually here's a pic [https://mobile.twitter.com/jonathanfly/status/12155378275654...](<https://mobile.twitter.com/jonathanfly/status/1215537827565490176>)

- **qpiox** · [2020-01-21 11:49 UTC](https://news.ycombinator.com/item?id=22106087)
  Pollution sensors for indoor use that can be plug via USB to the mobile phone are really cheap, you can find laser ones like Nova SDS for \$17 and some that are not so precise come even cheaper than that. ^c22106087

  So unless the author buys a real PM2.5 sensor and does a test in a true room and not a box of the size of a Desktop PC, with the sensor on the opposite side of the room, and proves that the pollution drops to below 8micrograms/m3, in a reasonable time frame, than we can say that it is working.

  Until than we can only say that the  purifier is only able to purify a desktop PC.

- **bureaucrat** · [2020-01-21 09:36 UTC](https://news.ycombinator.com/item?id=22105486)
  Not enough airflow to filter air. Really, it's just an expensive way to waste money. ^c22105486

  Seriously? 600mA? Air purifiers are rated like 30W for a reason.

- **toastal** · [2020-01-21 15:46 UTC](https://news.ycombinator.com/item?id=22107905)
  I'm in Bangkok right now which is having a smog issue right now due to pollution and burning in the rice fields across the country. It's a shame that we're buying/making air filters instead of working on policy and cleaner methods of doing work--so now the poor and the wildlife can't afford to have clean air. ^c22107905

  - **overcast** · [2020-01-21 19:11 UTC](https://news.ycombinator.com/item?id=22110309)
    There are cleaner methods, stop taking the easy route and burning everything down. ^c22110309

- **spookthesunset** · [2020-01-21 17:38 UTC](https://news.ycombinator.com/item?id=22109183)
  In addition to the old "strap an HVAC sized air filter on the front of a box fan" tip, I'd add that it is important to maintain a positive air pressure in your living space.  The only path air should enter your dwelling from the outside is via your air filter. ^c22109183

  You can do this by putting the box fan in a window and sealing up any gaps with something like cardboard or thick plastic sheeting.  On the outdoor end of the fan, put your filter.  Close all other windows & doors in the house.

  Keeping a positive indoor air pressure this way makes sure all the air in your house is filtered.  Obviously you'll want to make sure your box fan's filter is rated for smoke / particulate matter.

  - **dredmorbius** · [2020-01-22 00:07 UTC](https://news.ycombinator.com/item?id=22113192)
    Bad advice. ^c22113192

    A decent filter's throughput is going to be multiples of your structure's air-exchange rate.

    What you want to do is to *filter the interior air*, by passing it, multiple times, through the filter.  If you put the fan and filter in a window, you're hugely multiplying the air-exchange rate (to no net benefit), but are *filtering* that air only once.

    The net result is a much *higher* indoor particulates level.

    So no, don't do this.

    - **spookthesunset** · [2020-01-22 00:42 UTC](https://news.ycombinator.com/item?id=22113413)
      Interesting perspective.  Wouldn’t it be best to do some combo of both?  A low volume fan/filter that maintains positive pressure and an internal filter/fan combo? ^c22113413

      I mean in labs and manufacturing facilities that need ultra pure air, I’m pretty sure they maintain a positive pressure inside the sensitive areas.  Otherwise you’ll be sucking in bad crap from every nook and cranny...

      - **dredmorbius** · [2020-01-22 01:14 UTC](https://news.ycombinator.com/item?id=22113595)
        Various lab setups have different requirements. ^c22113595

        For biocontainment you generally want *negative* pressure, such that all *exhaust* is filtered.

        For clean rooms, positive pressure, to ensure filtration and minimum particle reduction levels within the conditioned space.  These also have staged zones, much like a cascade refrigerator, with finer levels of purity as you approach the core.  Humans themselves are excluded from the higher-purity zones (we're leaky bags of flakey skin, hair, dander, sweat, and mucus).  Most especially in chip-fab, but also I suspect various nanofab facilities.

        All of which is pretty much entirely outside my paygrade, so I can't really comment intelligently.

- **jwr** · [2020-01-21 10:10 UTC](https://news.ycombinator.com/item?id=22105621)
  I would suggest worrying much more about PM2.5 and getting a filter that does trap those particles. Many health problems are caused specifically by small particulate matter. ^c22105621

  - **mrspuratic** · [2020-01-21 11:36 UTC](https://news.ycombinator.com/item?id=22106006)
    His statement "I'm not concerned with the ability of the device to remove PM2.5" comes across as dismissive - he's not concerned because he's using a HEPA filter health officials are recommending and therefore he trusts it. HEPA starts at 0.3μm ("PM0.3") particle size, which doesn't cover finer forms of elemental carbon (soot). "H13" is a minimum retention efficiency though, not a specific particle size or application. ^c22106006

  - **qpiox** · [2020-01-21 11:36 UTC](https://news.ycombinator.com/item?id=22106009)
    A true HEPA filter does capture PM2.5 ^c22106009

- **vladocar** · [2020-01-21 14:15 UTC](https://news.ycombinator.com/item?id=22107017)
  Here is similar idea: [https://www.aliexpress.com/item/32989809211.html?spm\=a2g0o.p...](<https://www.aliexpress.com/item/32989809211.html?spm=a2g0o.productlist.0.0.43497b069dZbSy&algo_pvid=2afaf365-792a-4bb2-9d1b-dcc2a10a062f&algo_expid=2afaf365-792a-4bb2-9d1b-dcc2a10a062f-0&btsid=7dc87566-75e8-4331-b4c7-07d5b6c2018c&ws_ab_test=searchweb0_0,searchweb201602_6,searchweb201603_53>) ^c22107017

- **littlejohnny** · [2020-01-21 12:09 UTC](https://news.ycombinator.com/item?id=22106199)
  How about a 'filter' that can 'wash' the air with clean water. To me it appears to me the best possible solution to clean air in a confined space. To put it simply, air can be bubbled through the clean water, to scrub it of both particulate and chemical contaminants. No doubt the apparatus will lend itself to several technical challenges like noise and the need for periodic changes of the water. ^c22106199

  I believe such air purifiers already exist.

  - **pritovido** · [2020-01-21 12:49 UTC](https://news.ycombinator.com/item?id=22106410)
    They do exist. ^c22106410

    The main problem of air washers is that it is not enough to change the water.

    Fungus and spiders love the wet environment. Algae start growing if there is sunlight using just the dust particles on air as food. Also very bad bacteria like salmonella and others could grow if the water gets warm.

  - **dredmorbius** · [2020-01-22 00:15 UTC](https://news.ycombinator.com/item?id=22113244)
    See:  [https://venta-usa.com/product-category/airwashers/](<https://venta-usa.com/product-category/airwashers/>) ^c22113244

    They do an excellent job of humidifying the treated space, which may or may not be ideal.

    - **littlejohnny** · [2020-01-22 00:46 UTC](https://news.ycombinator.com/item?id=22113441)
      dredmorbius, do you own one? At what frequency do you normally change the water? ^c22113441

      - **dredmorbius** · [2020-01-22 01:11 UTC](https://news.ycombinator.com/item?id=22113577)
        No, I don't.  Ran across them discussing filtering options recently. ^c22113577

  - **pmiller2** · [2020-01-21 12:25 UTC](https://news.ycombinator.com/item?id=22106286)
    They do.  They're literally called "air washers," and you can buy them on Amazon. ^c22106286

- **dredmorbius** · [2020-01-21 23:38 UTC](https://news.ycombinator.com/item?id=22112983)
  A group has come up with an alternative design, with a far higher flow rate, and similar in concept to US-based box-fan + furnace-filter designs (materials for which are *not* readily available in Australia), with workshops in Canberra, described here: ^c22112983

  [https://www.eventbrite.com.au/e/making-your-home-smoke-proof...](<https://www.eventbrite.com.au/e/making-your-home-smoke-proof-diy-air-purifier-workshop-tickets-88598234705>)

  Materials for DIY Air Purifiers are:

  \- Floor Fan of any variety (BYO or we will be providing options for large and small fans)

  \- PM2.5-suitable Air filter (we will be bulk ordering the best type of Ryco MicroShield Cabin Filters for this purpose)

  \- Carboard & tape (we will provide these materials)

  Efficiency of the US-based version seems to be quite good:

  [https://invidio.us/watch?v\=kH5APw\_SLUU](<https://invidio.us/watch?v=kH5APw_SLUU>)

- **sampo** · [2020-01-21 12:02 UTC](https://news.ycombinator.com/item?id=22106159)
  What do you think about air washers? In addition to air filters, they blow air over wet surfaces to both clean and humidify the air. ^c22106159

  Here is one from Phillips: [https://www.youtube.com/watch?v\=n3xC3qxVphw](<https://www.youtube.com/watch?v=n3xC3qxVphw>)

  - **bipson** · [2020-01-21 14:32 UTC](https://news.ycombinator.com/item?id=22107166)
    I have one of those. ^c22107166

    It does not "wash" the air. It has a HEPA-filter on the intake side before the humidifying cycle. So it is basically the same thing as all other examples on this comment page.

    You can actually run it without water (which we do), then it does only filtration.

    Don't buy this particular product. It is overprized and has dramatic production quality issues (we sent two back, amazon reviews indicate larger issues).

- **clarry** · [2020-01-21 11:28 UTC](https://news.ycombinator.com/item?id=22105973)
  Speaking of air purifiers, does anyone have recommendations for one that is quiet and still effective? ^c22105973

  I have a pair of Electrolux EAP300s, in small rooms.

  Unfortunately on the lowest manual setting ("Quiet") they hardly do anything for air quality.  And they're still louder than I like.  I think they really optimized for cost; these devices feel very light and plasticy, the fan sounds cheap and has an uneven tone to it, and its speed keeps oscillating back and forth.  The purifier itself is also not stable and it can make an annoying noise if placed on a surface that ends up vibrating along.

  I also thought about DIYing one with noctua fans (which I know are quiet, and I have plenty of them in my PCs), but I suspect they're not going to be very effective.

  - **qpiox** · [2020-01-21 11:36 UTC](https://news.ycombinator.com/item?id=22106001)
    It depends on what noise level is acceptable for you and the room size. ^c22106001

    Out of 30 or so air purifiers available in shops here, of all the ones that are in the \$100-500 category, the Winix P/U450 are able to push the largest amount of air under the constraint of \<40db.

    HEPA filters are rated at which air speed they are most effective and how much pressure is needed. The ammount of pressure will only rise as the filter is saturated with dirt. You need a sufficiently powerful fan, and fans that are both powerful enough and quiet enough are very expensive.

    - **leetbulb** · [2020-01-21 16:02 UTC](https://news.ycombinator.com/item?id=22108086)
      I have two Winix HR1000. They have extremely powerful blowers and are quiet when not in "turbo" mode. The turbo mode is actually pretty good for white noise when sleeping. I've been running them 24/7 for years now and they are still working great. ^c22108086

    - **clarry** · [2020-01-21 12:03 UTC](https://news.ycombinator.com/item?id=22106169)
      I think EAP300 is rated 26dbA on its lowest level. ^c22106169

      I don't mind expensive, I'm tired of buying poor quality products.

  - **frank2** · [2020-01-21 18:50 UTC](https://news.ycombinator.com/item?id=22110048)
    One thing to keep in mind is that an air purifier with a squirrel-cage fan (the kind of fan needed to pull enough air through a HEPA filter) makes a very pleasant sound that is good for masking, e.g., banging noises from neighboring apartments. I regularly run mine just to mask noise. So being loud can be considered a feature. ^c22110048

    - **emrehan** · [2020-01-22 07:38 UTC](https://news.ycombinator.com/item?id=22115442)
      Exposure to noise degrades hearing and have psychological consequences. ^c22115442

  - **unknown** · [2020-01-21 18:47 UTC](https://news.ycombinator.com/item?id=22110024)
    [deleted] ^c22110024

  - **aidenn0** · [2020-01-21 18:39 UTC](https://news.ycombinator.com/item?id=22109946)
    Levoit makes ones that are a lot quieter than the ones you see for around \$100, but you will pay a lot more for them.  I still wouldn't call them "Quiet" though. ^c22109946

- **wiradikusuma** · [2020-01-21 09:42 UTC](https://news.ycombinator.com/item?id=22105513)
  Do air purifiers really work? I always have impression they're just sham, or at least placebo. ^c22105513

  - **Eric\_WVGG** · [2020-01-21 13:55 UTC](https://news.ycombinator.com/item?id=22106865)
    I felt similarly, but I have a family member who is bed-bound, there’s some asbestos removal going on, so I decided to take the plunge. ^c22106865

    I can vouch for their ability to detect impure air. If I start cooking anything, it switches on within seconds. It’ll turn on within about three minutes of sweeping the floor. And if the detectors can turn on when the air is dirty, it stands to reason that they can tell when the air is clean and they turn off as well.

    Shortly after getting this, some intriguing news surfaced regarding the installation of air filters in a California school (due to a gas scare) which resulted in a jump in test scores vs other schools in the same district.

    I am not a scientist, but I’m feeling pretty convinced about the efficacy of these things.

    [https://www.vox.com/2020/1/8/21051869/indoor-air-pollution-s...](<https://www.vox.com/2020/1/8/21051869/indoor-air-pollution-student-achievement>)
    [https://news.ycombinator.com/item?id\=18219391](<https://news.ycombinator.com/item?id=18219391>)

    - **Eric\_WVGG** · [2020-01-21 14:39 UTC](https://news.ycombinator.com/item?id=22107250)
      (A few minutes after posting this, morning rooftop construction started. Sounds of saws and drills buzzing, large objects and beams being dropped directly overhead. Air purifier just kicked into high gear. Yes, I’m definitely into this thing.) ^c22107250

      [https://thewirecutter.com/reviews/best-air-purifier/](<https://thewirecutter.com/reviews/best-air-purifier/>)

      - **bradknowles** · [2020-01-23 07:05 UTC](https://news.ycombinator.com/item?id=22125488)
        I’m a big fan of thewirecutter, and I reference them frequently on most things I’m buying. But for HEPA air filters, I don’t feel like they test the models that I feel are best for someone with asthma, or other similar breathing problems. ^c22125488

        We have several IQAir units, of at least a couple different models. None of them have sensors to automatically ramp up the filtering when they detect pollution, that would be nice. But according to the air quality sensors I have in the house, they do an amazingly good job of filtering the air, at least if you turn them up to high enough levels.

        I have yet to see demonstrated clear benefit of the units with activated charcoal filters for removing VOCs from the air, but my gut feeling is they do help in those areas where VOCs are a concern. Not all parts of our house needs that, however.

        Having four furballs does greatly increase the dander and other allergens we have to deal with, but we wouldn’t give them up for anything, so the IQAir units at least make our lives a bit more livable. Especially during “Cedar Fever” season.

    - **driverdan** · [2020-01-21 15:57 UTC](https://news.ycombinator.com/item?id=22108025)
      Being able to detect particulates in the air isn't what's important. You need to know if it's actually improving the air quality. ^c22108025

      - **Eric\_WVGG** · [2020-01-21 20:02 UTC](https://news.ycombinator.com/item?id=22110891)
        If you're referring to "air quality" in the form of particulates… it does turn off after a while. 15-30 minutes after cooking, one or two after sweeping, etc. Presumably it's triggered by no longer detecting particulates in the air, one would have to be fairly conspiracy-minded to suggest that it's working on some kind of timer (and can tell the difference between dust-timeouts and gas range waste timeouts)… I figured this was too obvious to point out, even given the sort of pedantry we get around here. ^c22110891

        If you're referring to some quality of the air beyond particulates… well that's not what a HEPA is even for, is it? I could be mistaken.

        - **driverdan** · [2020-01-21 21:46 UTC](https://news.ycombinator.com/item?id=22111993)
          How does it compare to a control? If the pollution stops (eg you stop cooking) the particulates will settle on their own. You'd expect the count to go back down to normal over time. How much faster does the air purifier cause the particulate count to decrease? ^c22111993

  - **qpiox** · [2020-01-21 11:41 UTC](https://news.ycombinator.com/item?id=22106039)
    Yes they do. But you need a sufficiently powerful one to be able to circulate the air in the room enough times per hour, more that the circulation that occurs through the doors, windows and even walls. ^c22106039

    Eco-rated houses have a circulation of about 2-3 times per hour. Older houses that are well insulated are about 5-6 times per hour. The purifier needs to be powerfull enough to spin the entire air volume couple of times faster than the natural circulation.

    If your windows and doors leak too much, or if you open them too much, or if you burn oil / light up cigars too much and produce smoke then it might be pointless.

    I live in one of the cities where the pollution is regularly at the top 10 in the world, and the unit I have is able to reduce the pollution inside to a level that is 5-6 times lower than outside if it runs constantly in a mode that is like 30\% of the power. It could do better, but it would be too loud for me.

    - **labawi** · [2020-01-21 23:52 UTC](https://news.ycombinator.com/item?id=22113102)
      Not sure where you live, but if air in my room circulated once in an hour, with doors/windows closed, I'd consider it way too much. We have winters so people tend to plug holes. ^c22113102

      You're not talking about HVAC, are you?

      Nevertheless, I do know people living in leaky homes/building, and they do get \>1 exchange/hour.

  - **jwr** · [2020-01-21 10:12 UTC](https://news.ycombinator.com/item?id=22105628)
    Yes, they definitely do, although to a various degree of effectiveness. If you get a Xiaomi Mi Air 2, for example, it will be very effective. If you get a Dyson fanless thing, not so much. ^c22105628

    In general, there is no escaping physics: you need to move a large quantity of air through something that traps dust particles. The low-tech solution of a fan and a HEPA filter is a very good one, but I would suggest getting a filter that traps PM2.5 particles as well.

    - **Raphmedia** · [2020-01-21 14:55 UTC](https://news.ycombinator.com/item?id=22107410)
      \> If you get a Dyson fanless thing, not so much. ^c22107410

      Any sources on that? I have one and I swear by it. They have a glass HEPA filter and a carbon filter. I'm not quite sure how much air it moves but it's enough to scrub the air of my two floors apartment when someone smokes indoor. It's not really fanless per-se, it's a turbine in the base. You are simply moving the blades down into the base and away from the output area.

      - **oiasdjfoiasd** · [2020-01-21 17:11 UTC](https://news.ycombinator.com/item?id=22108841)
        [flagged] ^c22108841

        Yeah the Dyson purifiers are awesome.

    - **chewz** · [2020-01-21 10:50 UTC](https://news.ycombinator.com/item?id=22105795)
      \> a HEPA filter is a very good one, but I would suggest getting a filter that traps PM2.5 particles as well ^c22105795

      Or read the specs and compare with norm

      [https://en.wikipedia.org/wiki/HEPA\#Specifications](<https://en.wikipedia.org/wiki/HEPA#Specifications>)

  - **chrisparton1991** · [2020-01-21 10:11 UTC](https://news.ycombinator.com/item?id=22105626)
    I decided to buy one when the smoke from the Sydney bushfires blanketed my town. ^c22105626

    In my bedroom I could see and taste the smoke. The air purifier struggled, but it cleared the air around my computer quite well. I have dividing curtains in my room that I was able to close, which made it easier on the purifier.

    All in all I think it was definitely worth the buy. FWIW I picked up a secondhand Kogan SmarterHome air purifier for AUD\$60.

  - **input\_sh** · [2020-01-21 10:23 UTC](https://news.ycombinator.com/item?id=22105669)
    If they have a replaceable HEPA filter, they sure do. ^c22105669

  - **magicalhippo** · [2020-01-21 12:03 UTC](https://news.ycombinator.com/item?id=22106166)
    A few years back I had to temporarily move back to my parents while getting a new place. It had been years since I'd used my room, and it had been neglected a bit. ^c22106166

    First days I started coughing a lot when staying the room for a bit, and I woke up quite stuffy in the morning. Got me an air purifier with HEPA filter and let it run at max setting while at work. After running it a few days like this, I didn't have any more issues.

  - **867-5309** · [2020-01-21 10:02 UTC](https://news.ycombinator.com/item?id=22105588)
    they probably work around a small area where they are placed, but particulates outside of that will be unaffected and ultimately fall to the ground ready to be disturbed and recirculated as dust. I'm under the impression that for something like this to work, you would need to feel the air current at every point in the room, like a light breeze ^c22105588

  - **dredmorbius** · [2020-01-22 00:19 UTC](https://news.ycombinator.com/item?id=22113278)
    Yes.  The DIY box-fan variant as well as many of the specifically-designed products: ^c22113278

    [https://invidio.us/watch?v\=kH5APw\_SLUU](<https://invidio.us/watch?v=kH5APw_SLUU>)

- **jaclaz** · [2020-01-21 09:27 UTC](https://news.ycombinator.com/item?id=22105445)
  Nice. ^c22105445

  For some strange reasons it immediately reminded me of the scene in Apollo 13:

  [https://www.imdb.com/title/tt0112384/quotes/qt0476826](<https://www.imdb.com/title/tt0112384/quotes/qt0476826>)

- **verdverm** · [2020-01-21 15:05 UTC](https://news.ycombinator.com/item?id=22107498)
  I use a box fan with filters taped to each side. You want to do both sides or the air gets pushed/pulled around the edges of the blades, rather than going through the filters. ^c22107498

  - **dredmorbius** · [2020-01-22 00:17 UTC](https://news.ycombinator.com/item?id=22113261)
    That's doable, though you're increasing initial cost by about 1/3, and doubling consumables, by using two filters. ^c22113261

    The net effective increased filtration rate is marginal.

    If you can afford this without concern, it's fine, but it's not necessary.

    - **verdverm** · [2020-01-22 02:47 UTC](https://news.ycombinator.com/item?id=22114103)
      It works with two and not with one, so pretty much required. The effect is far from marginal in my setup. Also far cheaper then the post link, less than half. ^c22114103

      - **dredmorbius** · [2020-01-22 03:41 UTC](https://news.ycombinator.com/item?id=22114382)
        Numerous documented and tested builds with only one. ^c22114382

        [https://invidio.us/watch?v\=kH5APw\_SLUU](<https://invidio.us/watch?v=kH5APw_SLUU>)

        YMMV.

        - **verdverm** · [2020-01-22 14:21 UTC](https://news.ycombinator.com/item?id=22117728)
          Cool, don't really care, happy with my double filtered setup ^c22117728

- **amluto** · [2020-01-21 18:40 UTC](https://news.ycombinator.com/item?id=22109958)
  My general theory is that HEPA makes sense for filtration where a single pass is all you get. So it makes sense for vacuum cleaners, air intakes, and such. But, for room air cleaning, what matters is the *rate* at which particles are removed, not the cleanness of the air coming out. So, for recirculating, something like a MERV 13 filter seems like a better choice: it lets more particles through on each pass, but it also restricts airflow less. ^c22109958

  - **dredmorbius** · [2020-01-22 00:14 UTC](https://news.ycombinator.com/item?id=22113241)
    PM2.5 particles are small enough that they pass through many materials. ^c22113241

    You can use lower-efficiency (higher effective particle-size) filters ... but you'll just be blowing the bad stuff through them rather than removing it.

    The net metric is *how fast the room particulate level drops*, which is the treatment goal.  Flow rate is a red herring.

    - **amluto** · [2020-01-22 17:51 UTC](https://news.ycombinator.com/item?id=22120018)
      That’s why I suggested MERV 13 and not, say, MERV 8.  If your filter removes a mere 50\% of particles at a given size but moves twice as much air as a HEPA filter, you’re doing fine for a recirculating filter. ^c22120018

- **TaylorAlexander** · [2020-01-21 17:22 UTC](https://news.ycombinator.com/item?id=22108989)
  I’m all for DIY, but this looks horribly underpowered to do anything against major pollution. ^c22108989

  I’ve got a Honeywell that’s \$150 and it must have 20-40x the throughput of this little thing.

  [https://www.honeywellstore.com/store/products/honeywell-1700...](<https://www.honeywellstore.com/store/products/honeywell-17000-s-quietcare-permanent-true-hepa-air-purifier-germ-reduction.htm>)

- **unknown** · [2020-01-21 11:35 UTC](https://news.ycombinator.com/item?id=22105995)
  [deleted] ^c22105995

- **edgarvm** · [2020-01-21 12:52 UTC](https://news.ycombinator.com/item?id=22106431)
  Has you tested it effectively can absorbe particles? It's a good project but seems more like a nice form to waste energy ^c22106431

- **mundu\_wa\_hinya** · [2020-01-21 12:21 UTC](https://news.ycombinator.com/item?id=22106261)
  Pretty cool project.... Except for the fact that I cannot buy any of the parts from pccasegear. They deny certain geographical areas access to their website. In fact, this seems to be the new normal. Last week, I was denied access to a recipe from a .au website. Flipping on my VPN restores access.. ^c22106261

- **cwkoss** · [2020-01-21 20:59 UTC](https://news.ycombinator.com/item?id=22111488)
  I've always wondered if you could essentially hook a blower up to a bong to filter particulates out of the air using water.  Would be much cheaper to replace the 'filter', but I suspect it wouldn't filter as well.  Seems like it could be an interesting tradeoff though. ^c22111488

  - **dredmorbius** · [2020-01-22 00:12 UTC](https://news.ycombinator.com/item?id=22113221)
    There is a set of "Luftwascher" ("Air washer") designs which effectively do this. ^c22113221

    These do filter out particulates, but also add enough humidity to the air that this is billed as a feature of the system.  In high-humidity conditions this is less than ideal.

    [https://venta-usa.com/product-category/airwashers/](<https://venta-usa.com/product-category/airwashers/>)

- **grogenaut** · [2020-01-21 13:16 UTC](https://news.ycombinator.com/item?id=22106590)
  Is a filter or an ionizer better for smoke? [https://hackaday.com/2020/01/12/diy-ionizer-clears-the-air-o...](<https://hackaday.com/2020/01/12/diy-ionizer-clears-the-air-on-a-budget/>) ^c22106590

  - **bipson** · [2020-01-21 14:34 UTC](https://news.ycombinator.com/item?id=22107198)
    At least some of them don't really work at all. [https://www.youtube.com/watch?v\=VM9CJZpqfpA](<https://www.youtube.com/watch?v=VM9CJZpqfpA>) ^c22107198

    With something as simple and effective as HEPA-filters, it seems unreasonable to try other technologies.

  - **htfu** · [2020-01-21 16:47 UTC](https://news.ycombinator.com/item?id=22108574)
    Many (most?) proper ones use a combination of a coarse washable pre-filter, charcoal, HEPA, and ionizer.
    Which makes sense, since they all basically do different things. ^c22108574

- **Zardoz84** · [2020-01-21 10:54 UTC](https://news.ycombinator.com/item?id=22105820)
  I would say that there are electronic schemes and plans to build DIY ion air cleaners. They works nice to remove  dust or tabacoo from air. ^c22105820

  Also, ozone air purifier make wonders to keep at bay smells and fats (wonderful to have on the kitchen), and kills bacterias, spores and fungus.

  - **qpiox** · [2020-01-21 11:29 UTC](https://news.ycombinator.com/item?id=22105977)
    Ozone is harmful. ^c22105977

    - **Zardoz84** · [2020-01-21 12:05 UTC](https://news.ycombinator.com/item?id=22106177)
      O3 isn't harmful in small quantity : [https://en.wikipedia.org/wiki/Ozone\#Consumers](<https://en.wikipedia.org/wiki/Ozone#Consumers>) ^c22106177

      Also, ozone purifiers not need to keep working all the time. A usual usage it's have a burst of ozone to sanitize a place, and wait a few minutes to decompose to O2. The result is that any smell is removed, and the ambient is sanitized. I saw this a lot on hotels where they use "ozone cannons" where they are cleaning rooms.

    - **unlinked\_dll** · [2020-01-21 11:43 UTC](https://news.ycombinator.com/item?id=22106054)
      It also smells bad too ^c22106054

      - **regularfry** · [2020-01-21 12:47 UTC](https://news.ycombinator.com/item?id=22106402)
        That's very subjective - I quite like the smell. ^c22106402

- **eeZah7Ux** · [2020-01-21 11:54 UTC](https://news.ycombinator.com/item?id=22106103)
  Static pressure is important as well as airflow! Some info: ^c22106103

  [https://www.engineersedge.com/filtration/hepa\_filter\_pressur...](<https://www.engineersedge.com/filtration/hepa_filter_pressure_drop_considerations.htm>)

- **ivanhoe** · [2020-01-21 10:38 UTC](https://news.ycombinator.com/item?id=22105739)
  if you don't mind a noise you could buy a 2nd hand vacuum cleaner with a built-in hepa or water filter (ideally also with adjustable speed to make it less noisy) and just let it run without a hose, sucking the air and pushing it through the filter... ^c22105739

  - **adrianN** · [2020-01-21 11:32 UTC](https://news.ycombinator.com/item?id=22105988)
    If you don't mind the noise and wasting a kilowatt on something that can be done with two dozen watts. ^c22105988

    - **ivanhoe** · [2020-01-21 12:52 UTC](https://news.ycombinator.com/item?id=22106425)
      That kW will move you more air in 30 minutes than PC ventilator can in a whole day, especially if you're trying to push it through hepa filter which is fairly thick and adds quite a resistance. ^c22106425

    - **clarry** · [2020-01-21 13:46 UTC](https://news.ycombinator.com/item?id=22106808)
      Most vacs are adjustable.  Also, I think they're trying to maintain a roughly constant speed of the fan, not a constant power.  Which would mean that they reach peak power when airflow is obstructed, and idle at lower power when air is passing freely and motor is spinning with little resistance. ^c22106808

    - **robryk** · [2020-01-21 12:46 UTC](https://news.ycombinator.com/item?id=22106395)
      The vacuum cleaner would have much larger airflow though. Would it still have higher energy usage per unit volume of air pumped? ^c22106395

      If not, then cycling the vacuum on and off would actually Dave energy compared to the small fan setup.

  - **unknown** · [2020-01-21 11:53 UTC](https://news.ycombinator.com/item?id=22106100)
    [deleted] ^c22106100

- **SamBam** · [2020-01-21 14:51 UTC](https://news.ycombinator.com/item?id=22107364)
  This basically looks like a mini Shop-Vac. ^c22107364

  If you own a Shop-Vac (a wet-dry vacuum, generically), could you just turn it on without the hose? It would draw much more power, but presumably would work much quicker, and so may end up being more efficient.

  - **OJFord** · [2020-01-21 15:05 UTC](https://news.ycombinator.com/item?id=22107507)
    Of course; ditto any vacuum cleaner, AC with filtration, etc. ^c22107507

    It's just airflow + filter, which is why DIYing them is so popular.

- **htfu** · [2020-01-21 16:53 UTC](https://news.ycombinator.com/item?id=22108644)
  Not sure what the point is when it costs \$100 and is magnitudes smaller and less powerful than a proper one which runs at \$200-300 - an upfront cost which is dwarfed in the long run by filter replacements, as would be the case here. ^c22108644

- **blablaguy** · [2020-01-21 12:48 UTC](https://news.ycombinator.com/item?id=22106408)
  there is also some other air filtering project on github.
  maybe a bit more powerful but more expensive and definitely more ugly.
  [https://github.com/KarstenSiemer/Open-Airfilter](<https://github.com/KarstenSiemer/Open-Airfilter>) ^c22106408

  I don't really think airfilters in that size so much. They need to push a serious amount of air through the filters to be able to accommodate for natural air circulation. Some pc fans don't do the trick I'd suspect

- **unknown** · [2020-01-21 14:36 UTC](https://news.ycombinator.com/item?id=22107217)
  [deleted] ^c22107217

- **CodeSheikh** · [2020-01-21 16:47 UTC](https://news.ycombinator.com/item?id=22108588)
  OP: Do you think [https://www.instructables.com/](<https://www.instructables.com/>) would have been a better place for this than Github.com ? ^c22108588

  Great effort!

- **logfromblammo** · [2020-01-21 16:16 UTC](https://news.ycombinator.com/item?id=22108234)
  Please don't use an iPhone X "for scale". ^c22108234

  The dual-ruled calipers used in the next photo would be an acceptable substitute for just using a plain old ruler.

  - **jbob2000** · [2020-01-21 16:24 UTC](https://news.ycombinator.com/item?id=22108312)
    Most people know what an iPhone X (or similar device) feels like. Not many people have held calipers (or remember what holding them feels like) and not many people can put into context what a marking on a ruler actually means. ^c22108312

    For a quick scale judgment, a smartphone is perfect. It's not supposed to be precise.

    - **logfromblammo** · [2020-01-21 18:52 UTC](https://news.ycombinator.com/item?id=22110067)
      I respectfully disagree.  Smartphones do not come in a single standard size.  Using them as comparisons will end up with the same problem as using coins or banknotes--it is only helpful for those already familiar with the specific comparison item. ^c22110067

      A "for scale" comparison is most useful with a metric-scale ruler.  Metric lengths are standard worldwide.  Including an inch-scale ruler may help US-based persons.  The calipers were useful inasmuch as they had a metric length scale etched into them--a ruler with extra bits.

      By your argument, it is acceptable to report large lengths or areas in multiples of US football fields, volumes as multiples of Olympic-size swimming pools, or database sizes in multiples of the entire literary content of the US Library of Congress.  Journalists do this frequently, and every time, it drives me absolutely bonkers (an aggravation level equivalent to 3 rush-hour traffic jams).

- **jasonsamoa** · [2020-01-22 05:29 UTC](https://news.ycombinator.com/item?id=22114892)
  [flagged] ^c22114892

  This problem has been solved.

  [https://www.youtube.com/watch?v\=kH5APw\_SLUU](<https://www.youtube.com/watch?v=kH5APw_SLUU>)

