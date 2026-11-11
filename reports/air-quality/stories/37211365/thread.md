# [Clever coating turns lampshades into indoor air purifiers](https://news.ycombinator.com/item?id=37211365)

Article: [https://techxplore.com/news/2023-08-clever-coating-lampshades-indoor-air.html](<https://techxplore.com/news/2023-08-clever-coating-lampshades-indoor-air.html>)

PaulHoule · 2023-08-21 15:58 UTC · 37 reported comments · archived 2026-11-08 13:12 UTC
Observation: 2026-11-08 13:12 UTC → 2026-11-08 13:12 UTC

## Comments

- **pfdietz** · [2023-08-22 12:52 UTC](https://news.ycombinator.com/item?id=37221997)
  I knew a guy at work a couple of decades ago who was extremely sensitive to organic vapors.  Simply opening a dry erase marker in a nearby cube would send him to get medical attention.  He wasn't faking it. ^c37221997

  At one point he was trying out an air purifier from NASA that used UV light and titanium dioxide to destroy organic contaminants.  The light creates electrons and holes in the TiO2, causing the contaminants to be oxidized.  As I recall it didn't work well enough for his purposes (or perhaps created degradation products he also reacted to.)  The notion of using TiO2 to make self-cleaning surfaces is also a fairly old one.  One proposal had cars with TiO2 on their radiators, with the idea they'd destroy more smog than they'd create.  If I recall correctly there are also TiO2 coated toilets in Japan.

  - **salad-tycoon** · [2023-08-22 13:10 UTC](https://news.ycombinator.com/item?id=37222200)
    I believe what you are referencing are hydroxyl generators. I looked into these vs ozone generators when I bought an old very stinky and smoke filled house. They cost a lot more than ozone but are thought to not be irritating like ozone. Plus ozone breaks rubber and silicone down. ^c37222200

- **prometheus76** · [2023-08-22 12:30 UTC](https://news.ycombinator.com/item?id=37221730)
  The most efficient and inexpensive air purifier I have found consists of a cheap box fan with a furnace filter taped to the back of it. You can even get a fancy furnace filter and still come out way ahead financially. The other nice aspect of this approach is that you get much more air throughput for a fraction of the cost of a dedicated air purifier. ^c37221730

  - **nucleardog** · [2023-08-22 14:20 UTC](https://news.ycombinator.com/item?id=37223106)
    The “more throughput for your buck” seems to hold even as you move up beyond “filter taped on a fan”. ^c37223106

    The air filter I built out ran me about \$200 without the filters. (Lumber, inline duct fan, foam tape for sealing, window screen, some other accoutrements. The bulk of the cost was the fan.)

    The filters are two 3M MPR1500/MERV12 5” deep furnace filters that ran \$75. They’re prefiltered with some activated carbon sheet and some window screen (to avoid the filters clogging with pet hair). This is a similar filter to what runs in my furnace and they generally last over a year in there—the 5” filters have a lot of surface area.

    So all in let’s round up and call it \$300. Looking at Amazon and ignoring the questionably rated all-caps-manufacturer style products, looks like they would get me an air purifier rated for 600 square feet at two air changes per hour. Similar deal at Home Depot.

    At two changes per hour mine’s good for about 3000 square feet. Which means in the space it’s in it can do more like 10 air changes per hour, or one every 6 minutes.

    In reality that’s a lot of moving air and makes quite a lot of noise. Day-to-day I’m running it at around 20\% and sitting at two changes per hour. But when we’re cooking something smoky or during wildfire season, it’s one knob to turn up a bit and the air cleans up in here almost immediately.

    I run an AirQ which measures PM1/2.5/10, among other things. Without the filter on they all hover around 20ug/m3. When we’re frying food it can easily hit 300-400ug/m3 in here and unless we open up a bunch of windows it takes a long time to come down.

    With the filter on it’s 0. Not 0.something, just a flat 0. If I turn it off and get it up to 300-400 in here and then turn it back on to about 60\%, we’re back below 100 within 15 minutes, and down to something that rounds off to zero about a half hour after that.

    Which is all a long ramble to not really say anything except that it was a fun project.

    - **andrei\_says\_** · [2023-08-22 14:24 UTC](https://news.ycombinator.com/item?id=37223165)
      This sounds amazing. Do you have a reference to the materials and possibly plans? Sounds like a great design to open source. ^c37223165

      - **haneefmubarak** · [2023-08-22 15:38 UTC](https://news.ycombinator.com/item?id=37224295)
        I believe he's referring to a Corsi Rosenthal filter: ^c37224295

        [https://en.wikipedia.org/wiki/Corsi\%E2\%80\%93Rosenthal\_Box](<https://en.wikipedia.org/wiki/Corsi%E2%80%93Rosenthal_Box>)

      - **nucleardog** · [2023-08-22 15:59 UTC](https://news.ycombinator.com/item?id=37224612)
        It's somewhere on my infinitely expanding todo list to actually document it properly somewhere (though likely on my personal site where literally nobody will see it). Overall though it's pretty conceptually simple and straightforward to build if you've got some basic tools and are moderately handy. ^c37224612

        I pulled a few photos of the build off my phone and threw them online. I should preface them with "I'm a software engineer, not a carpenter.". You can probably get a good idea of the whole thing from these: [https://files.bogon.cloud/d/9d8d2f9b9e8f454ba305](<https://files.bogon.cloud/d/9d8d2f9b9e8f454ba305>)

        Conceptually it's just a wooden tube the size of a 16x25 furnace filter. The middle section houses an inline duct fan which pulls air from inside the box and exhausts out a hole in the top. That draws air in through the giant holes at the end of the tube and blows it out the top. The filters slot in on either end, so any air drawn in is pulled through the filters. The whole box is built out of half a sheet of OSB and a couple lengths of 2x2 and couple small pieces of 2x4.

        I used some neoprene rubber tape (the particular one I bought was sold for wrapping pipes to insulate them) where I attached the outer shell to the frame as well as under the attachment points for the fan to help seal the "inner box" and keep vibration down. Used way more screws than I needed just to try and make sure everything was as air tight as possible.

        The box is sized such that the 2x2 frame matches the \_outer\_ size of the filter which leaves the hole a bit (3" on either dimension) smaller than the typical filter in order to accommodate most of the typical variations in filter sizes. (A 25x16 filter is... apparently never 25x16. That's actually how I ended up with these 3M filters--bought them for my furnace then found out it takes some weird even more non-standard size.) The frame the filter sits against also has some neoprene tape stapled to it to help create a seal when the filter's sitting against it.

        The filter isn't actually held in place by anything but friction and the fact that I don't really move this thing around much. I built another 2x2 frame to sit outside the filter to help hold it in place as well as to have somewhere to staple some window screen so the filters didn't immediately plug with pet hair. (Last couple images show the amount of hair and dust that it catches after running it for a bit.) Since that's not fixed in place by anything you could actually put any filter \_up to\_ 5" deep in there--anything smaller and the frame can just slide further in. (Though I'm not sure something like a 1" filter would support the air volume the fan can pull. In a pinch you could at least put \_something\_ in and just run it at a lower speed though.)

        The hole the fan sits in just has another strip of neoprene tape run around the inside to seal it to the top board so I don't have any major leaks there. I did end up stapling another piece of window screen over the hole just to make sure my kid or cats didn't throw any toys in there and wreck the fan.

        The activated charcoal filter is just a 16x48" sheet I bought off of Amazon and cut in half and set against the filters. The frame + screen holds it against the filter well enough.

        You probably can't see in any photos, but my carpentry skills are not \_that\_ good, so I did wind up with a few small gaps between the outer shell boards where the filters sit that weren't sealed off by anything since there's no 2x2/etc inside that part. Ended up just filling them with a glue gun. Once I was done I used a kleenex to check for any major leaks--held it around all the joins, edges of the filter frame, etc, and watched whether it got sucked towards it. I'm sure \_some\_ air is getting in somewhere, but definitely the vast majority of the air is going through the filters. Even with the duct fan barely above a whisper, it's pulling enough air that a balled up kleenex will stick anywhere on either filter.

        I... I guess if anyone has any questions or feedback feel free! I kinda just cobbled this together one weekend when I got annoyed at the wildfire smoke, so I'm sure there's probably some room for improvement.

        - **andrei\_says\_** · [2023-08-24 06:47 UTC](https://news.ycombinator.com/item?id=37245795)
          Thank you for sharing this. Your carpentry skills being “not that good” is a feature - most of ours aren’t either. ^c37245795

    - **Wistar** · [2023-08-22 15:06 UTC](https://news.ycombinator.com/item?id=37223821)
      Do you have any photos of your filter system? I am curious about the form factor that uses two 5” filters, rather than the four filter rigs I have seen. ^c37223821

      - **nucleardog** · [2023-08-22 16:02 UTC](https://news.ycombinator.com/item?id=37224655)
        Posted a few in reply to a sibling comment, they're here: [https://files.bogon.cloud/d/9d8d2f9b9e8f454ba305](<https://files.bogon.cloud/d/9d8d2f9b9e8f454ba305>) ^c37224655

        IMG007 is the mostly-complete build and probably answers your question most directly.

        Basically it's just a wooden tube with a fan inside in the middle that draws air from inside the tube and exhausts it out the top. I stick a furnace filter in each end of the tube so the air that's getting sucked in is pulled through the filters.

        - **Wistar** · [2023-08-22 18:27 UTC](https://news.ycombinator.com/item?id=37226728)
          Perfect. Thank you. ^c37226728

    - **justinlloyd** · [2023-08-22 16:59 UTC](https://news.ycombinator.com/item?id=37225534)
      I did a similar thing. Built a plywood box, used cheap box fans, MERV12 4", with a replaceable activated filter. Didn't think to use the screen door covering for pet hair. That's a good fix. The plywood box contains... the cat litter box, one for each litter box. And then I have a few other air filters throughout the home of similar, box\=\>box fan\=\>MERV12 filter. ^c37225534

      - **nucleardog** · [2023-08-22 18:13 UTC](https://news.ycombinator.com/item?id=37226559)
        Oh man... we've got a couple cats as well and I hadn't even thought of that. We've currently got a couple litter boxes inside the TV stand so even just cutting another couple holes in the back and adding a 120mm fan with some cut-to-size MERV13 + activated charcoal or something would probably go a long way to keeping the dust and smell down. ^c37226559

        Thanks for the ideas!

        - **justinlloyd** · [2023-08-22 19:07 UTC](https://news.ycombinator.com/item?id=37227206)
          If you have a spare bathroom, and have a duct fan, with some 4" ducting, and a couple of MERV filters to prevent dust going up the duct, guess where you can duct the litter box odour too? Look up. ^c37227206

          But yes, a fan that can pull some semi-decent airflow, I run the box fans on lowest setting possible, I could probably run 12v 120mm or 200mm computer fans and get the same effect, and pull that air through a charcoal filter and box filter, it cuts out all dust, allergens and honestly, just about all the odour. The cats have to drop an absolute stinker to overcome the filters. If you hit Amazon, you will find a lot of euphemistic phrases on pages for ducted fans, activated filters, and so forth, for "filtering for your tomato plants that you grow indoors." That's the kind of equipment you can research. The odour from smelly, indoor "tomato plants" are not even in the same league for what my cats produce on a daily basis.

          Edit: Wait, I'm replying to original author who built the ducted fan version. You already know about the euphemistic language on Amazon as you have no doubt DYOR (done-your-own-research). Apologies.

          Edit part-deux: The activated filters I picked up come in a big sheet, and then I cut them down to size to fit the back of the MERV. I simply tape them on with gaffer tape and they hold until I am ready to change them out, a single sheet of filter lasts well over a year before it loses odour control. I experimented with layers of activated filter, but, anecdotally, it didn't seem to make much difference. I think the thick MERV filter slows down the air flow enough that the odour causing particles linger around the activated filter for a longer period of time, so they have more chance to bond.

  - **pxx** · [2023-08-22 14:23 UTC](https://news.ycombinator.com/item?id=37223142)
    This is a fairly good concept but it is not efficient, especially if you're using 1" filters. The operating cost is high because the fan uses a lot of electricity compared to better designed units. See this analysis: ^c37223142

    [https://onlinelibrary.wiley.com/doi/10.1111/ina.13163](<https://onlinelibrary.wiley.com/doi/10.1111/ina.13163>)

    Even with fairly reasonable electricity numbers you should look into building a more complicated box. And if your time is of import the dedicated purifiers start winning again after you amortize the startup cost (also they typically are better engineered for noise concerns).

    - **Ajedi32** · [2023-08-22 15:18 UTC](https://news.ycombinator.com/item?id=37223970)
      Thanks, that's exactly the sort of information I've been looking for! Though I disagree with the methodology used to calculate ongoing (operating) costs, as it seems that doesn't include the cost of replacement filters, only the cost of electricity. Many dedicated air filters have replacements that cost hundreds of dollars, so that seems like a huge oversight when comparing to standard MERV 13 furnace filters that I can pick up for \$10 a pop. ^c37223970

      (The electricity price they used in their calculations is also nearly double what I pay, but that's an understandable deviation given that electricity prices can vary wildly by region.)

  - **Ajedi32** · [2023-08-22 14:53 UTC](https://news.ycombinator.com/item?id=37223618)
    I wish there were more commercial air filters that accepted standard furnace filters. They're super inexpensive compared to the proprietary filters designed for specific air purifiers, have *tons* of surface area (allowing for good airflow), and there are plenty available with MERV 13 ratings. ^c37223618

    There's an argument to be made that MERV 13 isn't a good substitute for the higher rated carbon/HEPA filters that most dedicated air filters are designed to use, but I've read some things that make me question that assumption. Specifically, it sounds like, at least to a point, lower efficiency filters can be compensated for by increasing airflow, resulting in air passing through the filter multiple times?\[1\] I never got a satisfying answer to that question.

    \[1\]: [https://dynomight.net/ikea-purifier/](<https://dynomight.net/ikea-purifier/>)

  - **dillydogg** · [2023-08-22 12:38 UTC](https://news.ycombinator.com/item?id=37221813)
    I remember reading about the Corsi-Rosenthal boxes when the pandemic was at it's peak. ^c37221813

    [https://en.wikipedia.org/wiki/Corsi\%E2\%80\%93Rosenthal\_Box](<https://en.wikipedia.org/wiki/Corsi%E2%80%93Rosenthal_Box>)

  - **rajnathani** · [2023-08-22 14:37 UTC](https://news.ycombinator.com/item?id=37223379)
    Well, the interesting thing about the post is that it is specifically about VOCs. Airflow based air purification through Carbon filters and HEPA/MERV filters barely do anything to reduce VOCs (keep in mind that VOCs themselves are of many subtypes). ^c37223379

  - **walleeee** · [2023-08-22 17:32 UTC](https://news.ycombinator.com/item?id=37226002)
    I am partial to the "Cuboid" as described here [https://dynomight.net/better-DIY-air-purifier.html](<https://dynomight.net/better-DIY-air-purifier.html>). Quiet, easy, effective, and get all the foam you need from the duct fan packaging. ^c37226002

  - **francisofascii** · [2023-08-22 13:31 UTC](https://news.ycombinator.com/item?id=37222449)
    I wonder if a box fan will cause too much airflow, which would cause all the allergens to be spewed all over the room. You might need to run this system when not using the room. ^c37222449

    - **iambateman** · [2023-08-22 13:52 UTC](https://news.ycombinator.com/item?id=37222735)
      I don’t think so. The box fan can only pull air through the filter, so it should pull everything out of the air which it can in a few minutes. ^c37222735

      This kind of fan can do multiple air changes per hour, depending on how many sqft it’s supporting.

- **jbm** · [2023-08-22 07:02 UTC](https://news.ycombinator.com/item?id=37219563)
  This could be interesting (as I have also been looking for something to reduce CO2 and VOC in the home), but the important part is probably this: ^c37219563

  \> only require a visible light source that also produces heat—such as a halogen or incandescent bulb—and a lampshade coated with a thermocatalyst.

  My read is that you wouldn't be able to do this with an LED, and I only use LED lights around the house.  Isn't any heat production from a light is an inefficiency to begin with?

  - **woadwarrior01** · [2023-08-22 10:01 UTC](https://news.ycombinator.com/item?id=37220615)
    I've got Philips Hue LED lights around the house, and although the bulb remains relatively cool, the base gets surprisingly hot (75-80C) after they've been on for a couple of hours. ^c37220615

  - **frereubu** · [2023-08-22 07:47 UTC](https://news.ycombinator.com/item?id=37219802)
    The article says that they're "extending the technology so it will also be compatible with LEDs" but as you say it seems to be triggered by heat so I'm not sure how that will work, but it would need to given the phasing out of incandescent (and presumably halogen?) bulbs. ^c37219802

    - **rantallion** · [2023-08-22 07:50 UTC](https://news.ycombinator.com/item?id=37219815)
      The last paragraph explains: ^c37219815

      \> Unlike halogen and incandescent bulbs, however, LEDs release too little heat to activate thermocatalysts. So Kim's team is developing photocatalysts that are stimulated by the near-UV light emitted by LEDs, as well as other catalysts that transform part of the LEDs' visible light output into heat.

      - **baq** · [2023-08-22 09:33 UTC](https://news.ycombinator.com/item?id=37220427)
        my LEDs have UV-absorbing coating that emits visible light... ^c37220427

  - **mnemotronic** · [2023-08-23 16:27 UTC](https://news.ycombinator.com/item?id=37238476)
    My refrigerator generates heat.  Well, not generate, but moves the heat from inside the fridge to outside the fridge.  Can I use that? ^c37238476

  - **unknown** · [2023-08-22 10:38 UTC](https://news.ycombinator.com/item?id=37220835)
    [deleted] ^c37220835

- **criley2** · [2023-08-22 10:30 UTC](https://news.ycombinator.com/item?id=37220774)
  This seems... cool but pretty pointless for indoor air purification. Maybe this is more like "passive purification". ^c37220774

  But an air purifier needs to turn over all the air in a room to purify it. My air purifier running at full speed takes half an hour to turn the air over in my room.

  Presumably this would never be capable of purifying a room to any sufficient level, it would just be a tiny 0.5\% upgrade to a good active air purifier. Like having a desk plant.

  IMO I would drop the light concept, and put this thermocatalyst reactive material inside of a standard air purifier to replace the carbon filter. Unless this material isn't capable of handling a large workload, in which case... Ok

- **rob74** · [2023-08-22 08:04 UTC](https://news.ycombinator.com/item?id=37219888)
  So, this lampshade filters the air that happens to pass by it by accident? Ok, the heat from the light bulb probably also produces some convection, but I wonder how long it takes to completely purify all the air in a reasonable-sized room? It's a bit dubious that the article doesn't contain any info on this... ^c37219888

  - **getwiththeprog** · [2023-08-22 09:52 UTC](https://news.ycombinator.com/item?id=37220565)
    I image it would clean the air in a similar fashion to a salt-lamp. ^c37220565

    - **willcipriano** · [2023-08-22 11:38 UTC](https://news.ycombinator.com/item?id=37221270)
      So not at all? ^c37221270

      - **rob74** · [2023-08-22 13:19 UTC](https://news.ycombinator.com/item?id=37222305)
        don't underestimate the placebo effect! ^c37222305

  - **VoodooJuJu** · [2023-08-22 14:04 UTC](https://news.ycombinator.com/item?id=37222893)
    What the lamp does is it transfers wealth from fools to charlatans by attaching to it benign, magical, but not logically untrue attributes, in this case, "air purifier". One comment is pretty apt: it purifies as well as a salt lamp. ^c37222893

- **ambientenv** · [2023-08-22 21:40 UTC](https://news.ycombinator.com/item?id=37228887)
  I don't know. We seem to get down right giddy, wallowing in our cleverness to create solutions to problems we, ourselves, have created, without addressing the root cause or making any changes which will negate the need for our so-called solution.  Imagine a world where we don't have to be this cleaver to thrive and live healthy and fruitful lives. ^c37228887

- **sooheon** · [2023-08-22 08:14 UTC](https://news.ycombinator.com/item?id=37219944)
  Cool, would be nice in conjunction with HEPA & charcoal, especially in high risk areas like the kitchen. ^c37219944

- **plagiarist** · [2023-08-22 14:19 UTC](https://news.ycombinator.com/item?id=37223084)
  This seems silly. Maybe the coating could be useful on a larger surface in a mildly-trafficked room. But I don't think I'd spring for a lampshade over placing a small active purifier under the lamp. ^c37223084

