# [Reverse engineering Xiaomi air purifier NFC stickers](https://news.ycombinator.com/item?id=31540394)

Article: [https://www.flamingo-tech.nl/2022/05/27/this-is-how-they-do-it/](<https://www.flamingo-tech.nl/2022/05/27/this-is-how-they-do-it/>)

thunderbong · 2022-05-28 14:00 UTC · 113 reported comments · archived 2026-11-08 12:04 UTC
Observation: 2026-11-08 12:03 UTC → 2026-11-08 12:04 UTC

## Comments

- **BasilPH** · [2022-05-28 18:01 UTC](https://news.ycombinator.com/item?id=31542366)
  I've built dynomight's DIY filter\[\^1\], and I love it. No DRM issues either. ^c31542366

  \[\^1\]: [https://dynomight.net/better-DIY-air-purifier.html](<https://dynomight.net/better-DIY-air-purifier.html>)

  - **Someone1234** · [2022-05-28 20:33 UTC](https://news.ycombinator.com/item?id=31543553)
    Very cool. Anyone seen a mod that adds activated carbon? A lot of DIY filters are very cost-effective, but the lack of activated carbon is a big downside compared to commercial solutions. ^c31543553

    There's really only two air cleaning technologies that are worthwhile right now:

    \- HEPA filters (remove PM 2.5 particulate and above).

    \- Activated carbon (neutralizes harmful gases).

    The only other thing that may be worthwhile is a pre-filter, but that is mostly a cost saving measure rather than actually improving air filtration.

    Unfortunately commercial filters are full of gimmicks that don't work or may even be harmful due to Ozone generation (e.g. Ionizers, UV lights, et al.).

    - **papercrane** · [2022-05-28 21:06 UTC](https://news.ycombinator.com/item?id=31543862)
      You could buy an activated charcoal filter built to attach to the same inline fan booster from most garden stores that carry indoor growing equipment. They're popular with people growing cannabis indoors to remove the smell from their grow area. ^c31543862

      Something like this:

      [https://www.amazon.com/dp/B07GSKFBL8/](<https://www.amazon.com/dp/B07GSKFBL8/>)

    - **Reason077** · [2022-05-29 00:21 UTC](https://news.ycombinator.com/item?id=31545062)
      My Philips air purifier has separate HEPA and carbon filters that can be replaced independently from each other. And also a pre-filter mesh that collects large dust particles and can be vacuumed out. ^c31545062

  - **joshvm** · [2022-05-28 20:05 UTC](https://news.ycombinator.com/item?id=31543306)
    Perhaps a stupid question. Why go to the trouble of bolting together four filters, instead of attaching the duct fan to a cylindrical HEPA filter? Then you just need two plates: one to adapt the duct inlet and one to seal the base of the filter. ^c31543306

    I think, as with many DIY projects, one must look to the pot growing community. They solved the problem of "how do I not stink out my apartment" a long time ago - duct fans and HEPA/carbon filters are the mainstay of grow rooms.

    - **bsder** · [2022-05-28 20:26 UTC](https://news.ycombinator.com/item?id=31543491)
      Link?  I'm interested. ^c31543491

      However, I suspect availability plays into it.  Almost anyone can pick up a couple of rectangular HEPA filters and a box fan from the local hardware or big box store.

      I've never seen a cylidrical HEPA filter.  So, I probably need to order that from an industrial supplier.

      And, aren't duct fans kind of noisy?  Do they make quiet ones?

      In addition, this fan/filter seems even easier:
      [https://smartairfilters.com/en/blog/cannon/](<https://smartairfilters.com/en/blog/cannon/>)

      - **joshvm** · [2022-05-28 20:43 UTC](https://news.ycombinator.com/item?id=31543640)
        The duct fan + filter combo is how lots of cylindrical consumer units work (e.g. Levoit, Philips, etc). They just use crappy fans which don't really pull any air through, or they're very expensive for what they are. In terms of availability, I think the current popularity helped, otherwise you could also look at the auto market, lots of cylindrical filters there and they'd be fine for pulling out stuff like pollen, though you might want a carbon filter as well. ^c31543640

        I have no idea what's required for HEPA certification, but lots claim to be:

        [https://www.amazon.com/LEVOIT-Core-Replacement-High-Efficien...](<https://www.amazon.com/LEVOIT-Core-Replacement-High-Efficiency-300-RF/dp/B07RSZSYNC>)

        It has an outer dust mesh, the HEPA filter and a carbon insert. They're all the same though, I think you could use any manufacturer's filter. Longevity isn't really an issue if a supplier goes bust, just re-make the adapter ring. Pretty much all you need and you don't need to worry about sealing the corners.

        According to OP's link, they use a duct fan booster which is a lot quieter than a box fan (at least the claim is it can go down to 16 dB).

        Though a question is does a can-shape system work better? Or would you get the same effect if you used a single flat filter with the same "unrolled" area? I have no idea, and there's so much uncertainty involved with DIY testing.

      - **jrochkind1** · [2022-05-28 20:50 UTC](https://news.ycombinator.com/item?id=31543718)
        Hm,  I feel like cylindrical HEPA filters are common for shop vacs and widely available? Searching "HEPA filter shop vac" on home depot gets what looks like plenty; or are these not what would work for that kind of design, maybe we're talking about different things? They are "cylindrical" by being pleated. ^c31543718

    - **kortex** · [2022-05-28 21:31 UTC](https://news.ycombinator.com/item?id=31544060)
      Cost and availability. Cylinder filters tend to be way more expensive (\$30-50 per, I've seen true HEPA cylinder ones "for allergy sufferers" aka medical space, \>\$130) than rectangular (a few bucks). Rectangular also comes in a wider variety of form factors than cylinders, with more different filter styles (eg different thickness, with carbon, high flow, true HEPA/MERV \>13). ^c31544060

  - **someotherperson** · [2022-05-28 18:38 UTC](https://news.ycombinator.com/item?id=31542620)
    I go back to that page often. I might finally buy the parts tonight and actually make it instead of just thinking about it :) ^c31542620

- **jrockway** · [2022-05-28 22:33 UTC](https://news.ycombinator.com/item?id=31544450)
  The big problem I see with DRM on air filters is that air filters don't do anything complicated.  Remove the electronics module and connect the fan directly to power.  Done.  They should have done that in the factory and pocketed the profit from not buying electronics and NRE. ^c31544450

  (This is less possible on things like printers, which have to synthesize somewhat complicated motion, carefully release ink at the right time, etc.)

  - **hnarn** · [2022-05-29 06:42 UTC](https://news.ycombinator.com/item?id=31546979)
    I saw an article about someone literally just tying an air filter to the front of a construction fan, and apparently it worked well to improve the air quality in the room it was in (it was bad to begin with, of course). ^c31546979

    It’s a very simple concept hidden behind a lot of unnecessary technology.

- **throwaway4good** · [2022-05-28 15:17 UTC](https://news.ycombinator.com/item?id=31540953)
  Nice hack. But my xiaomi air purifier works just fine with a non-xiaomi filter - only thing it will do extra is show a warning at power on. ^c31540953

  - **GekkePrutser** · [2022-05-28 15:37 UTC](https://news.ycombinator.com/item?id=31541143)
    True for the older models but the new ones switch off after a certain time ^c31541143

    - **JohnJamesRambo** · [2022-05-28 18:11 UTC](https://news.ycombinator.com/item?id=31542436)
      The air purifier people must have met some printer ink people at a conference. ^c31542436

    - **throwaway4good** · [2022-05-28 17:52 UTC](https://news.ycombinator.com/item?id=31542309)
      Mine is a 3H. ^c31542309

      - **GekkePrutser** · [2022-05-28 18:26 UTC](https://news.ycombinator.com/item?id=31542540)
        Oh ok, I heard some of them switch off for sure (after a few hours). I read this on an online forum discussing integration with Home Assistant, some users got around it by just setting an automation in Home Assistant to switch it back on again :) Which is what I would have done if my 3S had had the same problem. But it doesn't. ^c31542540

        Strange that some models are affected but others not.

        - **throwaway4good** · [2022-05-28 19:09 UTC](https://news.ycombinator.com/item?id=31542846)
          Maybe it is because I am in the EU? This stuff is obviously in software and all my xiaomi gadgets get ota updates regularly. ^c31542846

          - **GekkePrutser** · [2022-05-29 00:26 UTC](https://news.ycombinator.com/item?id=31545079)
            Could be. I'm also in the EU but most stuff on my domotica vlan has no access to internet. It's possible the purifier never updated after I connected it. I know the API I use to control it with home assistant is purely local. ^c31545079

            The forum where I read this was also EU based though. Weird.

          - **Mandatum** · [2022-05-28 23:13 UTC](https://news.ycombinator.com/item?id=31544684)
            In AU, mine doesn't turn off either. ^c31544684

- **VoidWhisperer** · [2022-05-28 14:41 UTC](https://news.ycombinator.com/item?id=31540700)
  I think my question with this would be: ^c31540700

  How accurate is the filter durability that the normal filter \<-\> air purifier tracks? If it tracks reasonably well (which, without more info, I have my doubts for the same reason printer ink cartridge capacity tracking is bad), wouldn't using these stickers kind of defeat the purpose of using the filter in the air purifier, since these kinds of filters do have finite durability and after that it isn't purifying the air as well as it could be.

  - **chmars** · [2022-05-28 14:50 UTC](https://news.ycombinator.com/item?id=31540776)
    The filter durability is time-based in my experience: ^c31540776

    I set up several air purifiers at the same time in December 2021 but used them in different areas, i.e., with different filter loads. The air purifiers ran 24/7 and mostly in automatic mode, except for some hours after known possible coronavirus exposures.

    Official end of filter life was reached after about five months and for all filters on the same day. The air purifiers are still running tough, that's a plus!

    Xiaomi recommends to replace filters every 6 to 12 months. The recommendation, however, is based on the use in polluted Asian cities, I guess. We have rather clean air here. I therefore assume that it is safe to use the filter for an additional few months.

    - **Danieru** · [2022-05-28 15:00 UTC](https://news.ycombinator.com/item?id=31540844)
      HEPA filters get more effective overtime in exchange for more restricted airflow. Thus the failure mode is "air is not flowing" and not "air is not getting cleaned". ^c31540844

      At home I use 3 air filters in various rooms. These are standard/mid-range Japanese Sharp filters. Japanese because we live in Japan, not because Japanese HEPA filters are special. The filters themselves can be bought for about 30\$ online. When the filters get near end of life I've had success by switching to a higher fan speed. This is not magic, at some point even on the highest setting airflow starts to match the old medium speed. The high speed mode consumes about 4x the electricity of medium speed.

      The net result is there exists an intersection point where continuing to use a filter costs more money than replacing. For us in Japan with expensive electricity this point exists sometime after the airflow has diminished but the filter is viable on high speed. In cheap electricity countries the filter might become unusable before electricity becomes a significant cost.

      - **5e92cb50239222b** · [2022-05-28 18:09 UTC](https://news.ycombinator.com/item?id=31542426)
        \> because we live in Japan ^c31542426

        May I ask why you're using them at all? Every time I look at Japanese cities they seem to have PM2.5 levels in a second-digit microgram range. A bad day seems to be something like 15 µg.

        - **bjoli** · [2022-05-28 21:24 UTC](https://news.ycombinator.com/item?id=31544000)
          Poor ventilation and a stir fry on medium-high heat will bring you above harmful levels for several hours in my experience. ^c31544000

          Candles, cleaning, frying. All very good ways to increase air pollution in your home that nobody speaks about.

        - **Danieru** · [2022-05-28 23:22 UTC](https://news.ycombinator.com/item?id=31544736)
          First off I don't want to under sell Japan, it is a pretty nice country and Tokyo is pretty clean. Sadly it's still a city with car pollution all cities have. ^c31544736

          Unique to Japan is the pollen. After WW2 Japan was reforested in mass with a single variety of tree. Thus making the exact pollen release an annual torture test for anyone without air filters. My theory is everyone eventually gets pollen alergies, it's just a matter of time. My wife is affected during pollen season, and I've starting to notice myself become affected as well.

          We do not stir fry, that's not a thing in Japanese cuisine. And our cooking is all IH so no gas particle. Yet even we will notice if the air purifiers are not running. We'll first notice our noises are a bit stuffy, and omly then check to find a kid has turned off the air purifier.

          An upshot to low pollution is filters last ages.

    - **dirtyid** · [2022-05-31 20:10 UTC](https://news.ycombinator.com/item?id=31574318)
      \>additional few months ^c31574318

      Xiaomi filter processing Canadian air in a semi high traffic area after 2 years looks better than my Asian country filter after 6 months.

  - **GekkePrutser** · [2022-05-28 14:49 UTC](https://news.ycombinator.com/item?id=31540765)
    I have one and it tracks very poorly. It tracks only the usage time regardless of how fast the fan is running. ^c31540765

    When on auto, it is mostly spinning at idle, hardly sucking air through the filter, and as such it's hardly contaminating the air filter (in fact the airflow is so low I stopped using auto mode at all, there is just no point).

    It also doesn't take into account how contaiminated the ambient air is (even though it has an air quality sensor on the one I have).

    I run mine at about 40\% so I use the filters about 2-3 lifetimes :) Even that is a pessimistic approach IMO because the air here is very clean. I mainly have it because of hayfever (pollen allergy).

    - **chmars** · [2022-05-28 14:52 UTC](https://news.ycombinator.com/item?id=31540791)
      In automatic mode, different ppm level should result in higher fan speeds. That is at least the case with my filters. Cooking for example can be a trigger. ^c31540791

      You are of course right that automatic mode does not do much. At the same time, higher fan speeds are noticeable (and annoying).

      - **GekkePrutser** · [2022-05-28 15:40 UTC](https://news.ycombinator.com/item?id=31541171)
        For my environment it never ramps up in that mode at all. Ambient levels are never higher than 10ppm or so. ^c31541171

        I know the sensor works because once there was a small bin fire outside. There was no visible smoke indoors, I only noticed a slight smell. But the purifier immediately ramped up and showed over 200ppm.. So it does work.

        I'm surprised it's so low as I live at the 2nd floor on a fairly busy street with many diesel buses passing.

  - **userbinator** · [2022-05-28 21:46 UTC](https://news.ycombinator.com/item?id=31544168)
    If they wanted to really track the filter life, they would use a static pressure sensor like a lot of HVAC installations have. It's clear what the companies doing this DRM shit are prioritising, and it's not accuracy. ^c31544168

  - **deno** · [2022-05-28 14:54 UTC](https://news.ycombinator.com/item?id=31540802)
    In my unit it's just 365 days countdown. ^c31540802

    OTOH a lot of the Xiaomi purifiers have built-in air quality monitor so really you can just ignore the useless filter health value and figure out if the filter is working for yourself, based on how it performs.

- **occz** · [2022-05-28 16:21 UTC](https://news.ycombinator.com/item?id=31541535)
  Good stuff. The author of the post has also previously made a defeat device that can fairly simply be installed in your purifier, which simply reports the filter to always be at 100\%. Useful if you're in a place where the filter will last significantly longer than what Xiaomi thinks. I bought one and it works great, I can definitely recommend it. ^c31541535

  - **KennyBlanken** · [2022-05-28 16:40 UTC](https://news.ycombinator.com/item?id=31541697)
    Or just buy a unit from one of the companies that doesn't engage in DRM nonsense. ^c31541697

    Coway and Winex both do not do this and make top-rated units.

- **romseb** · [2022-05-28 14:39 UTC](https://news.ycombinator.com/item?id=31540685)
  \> This will significantly decrease the waste footprint from a whole filter.. to just a sticker ^c31540685

  I don't think I understand which problem this solves. I can turn on my Xiaomi Air Purifier with or without a filter. It's just a fan. Is this about a new version that does not work with an old filter?

  - **pawelos** · [2022-05-28 14:54 UTC](https://news.ycombinator.com/item?id=31540807)
    I have Air Purifier 3H, and with an old filter it displays big red “0\%” most of the time, instead of showing PM2.5 level. Which is annoying. ^c31540807

    And the filter works effectively a few times longer than what is displayed (at least according to the PM2.5 sensors on the same device).

  - **GekkePrutser** · [2022-05-28 14:47 UTC](https://news.ycombinator.com/item?id=31540745)
    Mine too, I have the 2S. ^c31540745

    However I have read that the new air purifiers (from the 3 onwards) switch off after a couple of hours when they don't see a filter sticker, or a used-up one.

- **alliao** · [2022-05-29 00:53 UTC](https://news.ycombinator.com/item?id=31545195)
  hold down back button and front button till it beeps
  release front button
  keep holding down back till it beeps again
  then you'll see entering engineering menu
  disconnect power
  restart
  this completely resets all memory ^c31545195

  - **na85** · [2022-05-29 02:09 UTC](https://news.ycombinator.com/item?id=31545614)
    \>this completely resets all memory ^c31545614

    Enabling the user to do what?

    - **alliao** · [2022-05-29 02:49 UTC](https://news.ycombinator.com/item?id=31545848)
      oh my bad, since it wipes all memory, includes number of hours the filter(with RFID) is used, thus resetting the filter to 100\% health again without giving it a brand new RFID to accumulate the hours on. ^c31545848

- **random3** · [2022-05-28 16:28 UTC](https://news.ycombinator.com/item?id=31541604)
  Can someone explain what's the result of filter utilization / capacity.
  Is it efficiency? Does it start spilling out particles? ^c31541604

  I feel like a 100\% used filter will still do a pretty good job, so unclear how much of the utilization \% has commercial reasoning?

  - **5e92cb50239222b** · [2022-05-28 17:45 UTC](https://news.ycombinator.com/item?id=31542247)
    I live in an very polluted area (average PM2.5 level in winter around 300 µg/m³) and have been running the same filter non-stop in a cheapest Xiaomi purifier for 1.5 years. It's almost black, but works fine, as confirmed by DIY PM sensors. I think it puts more strain on the motor, but I don't see any difference in efficiency. ^c31542247

  - **Waterluvian** · [2022-05-28 16:37 UTC](https://news.ycombinator.com/item?id=31541665)
    My intuition is that the more “full” it is, the less air will flow through it, meaning it just doesn’t do as much. ^c31541665

    Not to suggest that what the manufacture decides “100\%” is is actually that.

    - **oh\_sigh** · [2022-05-28 17:25 UTC](https://news.ycombinator.com/item?id=31542071)
      That's exactly right for HEPA filters, not sure about other types of filters though. ^c31542071

      - **thaeli** · [2022-05-28 18:10 UTC](https://news.ycombinator.com/item?id=31542430)
        This applies for any media filter. VFD drive on the motor can keep airflow constant and increase energy usage instead, but for most fans the increase in static pressure means less air volume. Heavily loaded filters can also have more air bypassing the filter, which may or may not be significant depending on the application. For this kind of air filter bypass just subtracts from the airflow through the filter media. ^c31542430

  - **KennyBlanken** · [2022-05-28 16:37 UTC](https://news.ycombinator.com/item?id=31541669)
    Efficiency in terms of airflow goes down, and static pressure difference goes up - but the filters trap more of the particles going through them. Changing filters on furnaces and AC units is really important, since lack of airflow hurts efficiency. ^c31541669

    Wirecutter (which is usually trash) confirmed this in testing; versions of units that had been running for months or longer (ie one they bought a year ago and used in someone's home, vs a new unit bought new with little run time) tended to perform better in terms of how many particles they completely removed.

    The unit starts using more electricity to do the same work, has to run at higher fan speeds, etc. So it's a tradeoff between that and the cost and waste generated by buying more filters.

    - **ehPReth** · [2022-05-28 17:00 UTC](https://news.ycombinator.com/item?id=31541882)
      curious - why is Wirecutter trash? I’ve been sorta feeling iffy about them for no real reasons but they seem highly recommended ^c31541882

      - **inferiorhuman** · [2022-05-28 19:09 UTC](https://news.ycombinator.com/item?id=31542843)
        With air purifiers at least Wirecutter completely ignores known problems in order to collect sweet, sweet referral fees.  Comments about the high levels of VOCs in some brands' filters, fans exploding, etc. all get/got ignored. ^c31542843

        In my case I bought a couple Coway air purifiers only to find that Coway doesn't honor their warranty.  I hit all the common complaints from the comments section – comments Wirecutter staff refuse to acknowledge.

      - **lostlogin** · [2022-05-28 18:02 UTC](https://news.ycombinator.com/item?id=31542370)
        I was reading their list of coffee grinder recommendations. Some they recommend I got rid of years ago as they aren’t very good. It may be the case that they had a price ceiling, as the article mentions how costly grinders are, but it’s certainly dropped my opinion of Wirecutter. ^c31542370

      - **rhexs** · [2022-05-28 17:10 UTC](https://news.ycombinator.com/item?id=31541958)
        They almost always conveniently only recommend products that allow for referral fees. ^c31541958

        - **eli** · [2022-05-28 17:21 UTC](https://news.ycombinator.com/item?id=31542041)
          so pretty much anything sold by a major retailer? ^c31542041

        - **aardvarkr** · [2022-05-28 17:20 UTC](https://news.ycombinator.com/item?id=31542034)
          The product manufacturers don’t pay referral fees, it’s the retailer. So your entire argument against them is you’re mad they make money by linking to Amazon or target? ^c31542034

          - **inferiorhuman** · [2022-05-28 19:11 UTC](https://news.ycombinator.com/item?id=31542865)
            \> So your entire argument against them is you’re mad they make money by linking to Amazon or target? ^c31542865

            That's not my entire problem with them, but it's a problem.  Because they're reliant on referral fees their motivation is purely to get you to buy random crap whether or not it's any good.  So long as their reputation holds up that's good, but once they start promoting crap there's going to be a long tail of folks who think "oh it's on wirecutter, it must be good".

            Take a look at their reviews.  It's not that they promote stuff that they might get a kickback on, Wirecutter *only* promotes stuff they can generate a referral link to.

          - **wincy** · [2022-05-28 17:26 UTC](https://news.ycombinator.com/item?id=31542084)
            I’d definitely prefer something like Consumer Reports who has the budget to expose scams like Molekule who claim to invent some magical new type of air purification. ^c31542084

          - **unknown** · [2022-05-28 17:40 UTC](https://news.ycombinator.com/item?id=31542190)
            [deleted] ^c31542190

      - **SemAntics0** · [2022-05-28 17:47 UTC](https://news.ycombinator.com/item?id=31542262)
        Years ago, they really drilled into the performance of the various products they compared and frequently the winner was a specialist product from a brand you had never heard of, but it really was the best on the market. Wirecutter articles did good testing with defined rationale that might not be up to laboratory standards, but it was enough to clearly identify which products were offering the best performance. When they labeled a product "The Best X", you could be fairly confident that it was going to outperform almost everything else on the market. They tested everything from the highest range products to the garbage chinesium specials and if you read the entire article, you could see where some products might outperform in certain areas, but under perform in others, letting you make an informed decision that wasn't simply picking the "Winner". Effort had clearly been put into discovering a full range of products instead of simply comparing the amazon options. Any product that was disqualified from comparison had a clear and reasonable rationale. ^c31542262

        Starting around 2018 the quality of testing plummeted into clickbait territory. Many articles appeared to justify their choices entirely based on reading amazon reviews without actually putting hands on the product, a theory reinforced by waves of comments appearing that despite a wirecutter recommendation, the product was absolute junk. My personal "Wirecutter is a lost cause" moment was when I was looking for a new comforter and the writer had simply disqualified every single option that was polyester based because "I don't like how polyester feels." That's not good testing. That's opinion. If I wanted subjective opinions on products I wouldn't be at Wirecutter.

        For an contemporary example, pull up their "The Best Drill" article. The reviews highlight things you could discover from holding the drill and looking at it. The testing is a single test performed by a single person with no edge cases or alternative uses considered. If ergonomics are such a critical consideration that it gets entries shot down, shouldn't you have multiple people testing to see how different models perform in different people's hands? Furthermore, the only products tested are mid-range household drills available from big box stores. Nothing from the professional brands like Festool or Hilti or some brand I've never heard of. No explanation why I shouldn't just buy a Harbor Freight special for half the price. No explanation why any other consumer-grade brands weren't included. The articles don't provide "The best drill", they're providing "The best consumer-grade drill for light duty work", and this attitude has spread to every corner of the site. You can't go to wirecutter and find a specialist tool that outperforms the commonly available options any more, because they're not even including it in testing.

        - **diziet** · [2022-05-28 20:40 UTC](https://news.ycombinator.com/item?id=31543603)
          The Best Drill article doesn't even mention impact drivers, which are going to be tremendously easier on the wrist/hand for screwing in screws. An explanation for the lay audience would help. Nor are questions such as: "How much torque is there? What is the torque curve? How much torque do you need? Do you need a hammer drill? What is the noise like?" addressed. ^c31543603

          I do think more specialty gear is hard to cover, as for example the the impact driver here: [https://www.youtube.com/watch?v\=l\_pCeGmQU8w](<https://www.youtube.com/watch?v=l_pCeGmQU8w>) or AvE's youtube coverage of tools goes beyond that. Project Farm tends to have better coverage of general equipment with pretty good objective tests: [https://www.youtube.com/channel/UC2rzsm1Qi6N1X-wuOg\_p0Ng](<https://www.youtube.com/channel/UC2rzsm1Qi6N1X-wuOg_p0Ng>) but even he can't cover all the brands/models: He covered Festool but not Hilti's SF 2H-A Hammer, for example.

          Techgearlab has pretty unbiased coverage, and they also have an small incentive to cover products that have affiliate programs -- however, for example their parent rock climbing site Crash Pad Coverage: [https://www.outdoorgearlab.com/topics/climbing/best-boulderi...](<https://www.outdoorgearlab.com/topics/climbing/best-bouldering-crash-pad>) includes Organic pads which have no affiliate program.

        - **inferiorhuman** · [2022-05-28 23:36 UTC](https://news.ycombinator.com/item?id=31544839)
          I should probably start off with: yeah, I don't like the Wirecutter drill article or find it useful.  They eventually call out their intended target audience: ^c31544839


          ```
            For most household tasks, a 12-volt drill is more than adequate. It’s the smallest
            class of drill, and due to advances in battery and motor technology, such models
            have become formidable with regards to power. … If you’re a rabid DIYer with plans
            to build a deck, a doghouse, and a tree house, we recommend a stronger, 18- or 20-
            volt drill. 
          ```

          
          They're not reviewing higher end pro tools because that's not their audience.  Were pros ever looking at WC for reviews?  I know that for tools I'd be looking at more specialized folks like Project Farm or Torque Test Channel.

          WC did cover the popular "pro" brands available in America (Milwaukee, DeWalt, Ridgid).  Potentially they should've included Makita but Festool and Hilti are way beyond the price point of the home gamer target audience.  Hilti especially goes after the fleet market, so even if you're a pro they're not necessarily going to be your goto brand unless you're at a larger company.  Anecdotally Milwaukee kit seems to be very popular amongst tradesmen out here.  But like with circular saws there's probably some regional variation.

          I think WC did miss some important stuff for home gamers and they definitely got it wrong with the Bosch drill.  It's small. It's tiny.  It's about as long as the DeWalt and about an inch and a half shorter in height.  You don't buy it for the power you buy it for the size.  If you need to stand it up on the battery, get a bigger one with a foot.

          [https://www.nytimes.com/wirecutter/reviews/the-best-drill-fo...](<https://www.nytimes.com/wirecutter/reviews/the-best-drill-for-common-household-projects/>)

  - **sschueller** · [2022-05-28 18:40 UTC](https://news.ycombinator.com/item?id=31542630)
    My assumption is that a "Full" filter has a reduced airflow which means the fan pulling air in has to work harder. If it is spected very tight then I could see it failing more quickly. ^c31542630

- **Havoc** · [2022-05-28 23:24 UTC](https://news.ycombinator.com/item?id=31544755)
  Nice. Bought some. ^c31544755

  The air here is already really good (\~10 reading) most of the time so I reckon I can run my filters much longer than Xiaomi thinks is appropriate.

  - **tym0** · [2022-06-08 12:14 UTC](https://news.ycombinator.com/item?id=31666133)
    Been running my filter for more than a year. When it tells you it's the filter is done you can just scratch the NFC tag and reset the counter by holding the back button. ^c31666133

- **causality0** · [2022-05-28 16:24 UTC](https://news.ycombinator.com/item?id=31541572)
  Interesting. The concept seems obvious but this is the first I've heard of air purifiers using printer-cartridge style artificial scarcity. ^c31541572

- **rbrtdrmpc-** · [2022-05-28 15:38 UTC](https://news.ycombinator.com/item?id=31541152)
  This is nice! And the timing is perfect for my purifier to complain about the second filter that I’ve so far ^c31541152

- **iSloth** · [2022-05-28 15:09 UTC](https://news.ycombinator.com/item?id=31540900)
  I've never experienced an air purifier, what's the general consensus? ^c31540900

  Do they make a difference? Perhaps a placebo? A must have?

  Genuinely interested if I'm missing out - For what it's worth I do live right on a main road in the UK, so I expect there is some level of pollution in the air.

  - **hammock** · [2022-05-28 15:27 UTC](https://news.ycombinator.com/item?id=31541036)
    I was so skeptical. Living in SF in 2018(?) during the wildfires, my apartment was drafty and I’d come home from work to a hazy indoor environment. I’d wake up with a sore throat and that’s what got me to take action (can’t sleep with an n95 on) ^c31541036

    I got the cheapest air purifier from Amazon and just put it on my bedside table. After one night my sore throat was gone.

    As simple as these machines are, they do work.

    - **CoastalCoder** · [2022-05-28 16:03 UTC](https://news.ycombinator.com/item?id=31541377)
      I can see how an air purifier makes sense in that 2018 scenario. ^c31541377

      I guessing that the benefits are less certain in more typical cases.

      - **imajoredinecon** · [2022-05-28 16:14 UTC](https://news.ycombinator.com/item?id=31541473)
        \> that 2018 scenario ^c31541473

        It’s a little hard to believe if you haven’t lived there recently, but basically the entire US west coast now has an annual fire season where you can expect at least several days of air quality in the “unhealthy” to “hazardous” range. AC (which does \~the same thing for air quality as a purifier) or a purifier is pretty much mandatory.

        - **samstave** · [2022-05-28 16:22 UTC](https://news.ycombinator.com/item?id=31541547)
          When the fires were raging, I was looking at all the areas air quality from purple air monitors and some areas near folsom California were at \~700 ^c31541547

          And healthy is something like \<100

          - **GekkePrutser** · [2022-05-29 00:39 UTC](https://news.ycombinator.com/item?id=31545124)
            Healthy is far lower than 100. 100 especially indoors is really bad. ^c31545124

      - **AlotOfReading** · [2022-05-28 18:29 UTC](https://news.ycombinator.com/item?id=31542562)
        Higher air pollution, especially during childhood, is also strongly linked to the development of asthma and other respiratory issues later in life. Pretty much everyone should at least be aware of their home air quality. ^c31542562

      - **hammock** · [2022-05-28 16:08 UTC](https://news.ycombinator.com/item?id=31541424)
        The benefits, yes. Those would be dependent on the local environment and if it’s causing you specific suffering. But that experience sold me on the functionality at least. ^c31541424

  - **Joeri** · [2022-05-28 15:36 UTC](https://news.ycombinator.com/item?id=31541134)
    We live in the city and always are struggling with allergies. The whole family is always coughing or sneezing. We bought a xiaomi air purifier like in the article last week, started using it in the bedrooms for a few hours in the evening, and the allergies cleared up overnight. The particulate sensor is mostly useless, a known problem with the xiaomi models, but running it at a fixed setting seems to clean the air quite effectively. ^c31541134

    - **andor** · [2022-05-28 17:41 UTC](https://news.ycombinator.com/item?id=31542207)
      The particulate sensor on my Xiaomi air purifier correlates really well with the numbers from my city's air quality network. ^c31542207

      What doesn't work well for me is the auto mode, it barely does anything at less than 50µg/m\^3, way too high even for the mediocre air in my area. So instead I use automation in their app to let it run at full speed for 30 or 60 minutes.

      - **5e92cb50239222b** · [2022-05-28 17:58 UTC](https://news.ycombinator.com/item?id=31542349)
        They use Chinese air quality standards, which are very high relative to most other countries for (probably) obvious reasons. ^c31542349

        [https://en.wikipedia.org/wiki/Ambient\_air\_quality\_criteria](<https://en.wikipedia.org/wiki/Ambient_air_quality_criteria>)

  - **legulere** · [2022-05-28 16:19 UTC](https://news.ycombinator.com/item?id=31541515)
    The soot they filter out of the air is very visible when you change the filters (they turn from shining white to grey). Air pollution is one of the world’s leading risk factors for death [https://ourworldindata.org/air-pollution\#air-pollution-is-on...](<https://ourworldindata.org/air-pollution#air-pollution-is-one-of-the-world-s-leading-risk-factors-for-death>) . Though that varies a lot from country to country, it is a problem you can strongly reduce with throwing a tiny bit of money on it. ^c31541515

    - **gruez** · [2022-05-28 18:03 UTC](https://news.ycombinator.com/item?id=31542380)
      If the filter is only turning Greg it sounds like what you're seeing is dust rather than soot. I have a pm2.5 meter and over the winter/spring the reading is almost always 0 or low single digits, and my filters still turn grey ^c31542380

  - **dxhdr** · [2022-05-28 15:56 UTC](https://news.ycombinator.com/item?id=31541314)
    \> Do they make a difference? Perhaps a placebo? A must have? ^c31541314

    Purchase an air quality monitor, something like the Dylos DC1100. Then run a HEPA filter in a closed room for 30 minutes. It will remove almost all particulates! They work extremely well. Whether it "makes a difference" for your health is less clear.

    - **criddell** · [2022-05-28 19:40 UTC](https://news.ycombinator.com/item?id=31543091)
      Are the lower priced options on Amazon junk compared to the DC1100? I’d like to get a monitor, but I know I’ll probably only use it 10 times. The Dylos would end up being about \$25 / reading… ^c31543091

      - **dxhdr** · [2022-05-28 21:03 UTC](https://news.ycombinator.com/item?id=31543835)
        Good question, I bought a Dylos back in 2015 and can't remember how the other options stacked up when I researched it. I've been happy with the purchase and would recommend it if you're interested in watching air quality. It has a convenient "monitor mode" where it will re-sample the air every hour so it's not constantly running. It's neat to see how the air quality in a room changes based on having the windows open or shut, after cooking, just being in the room, etc. ^c31543835

        I'd expect there are smaller / sleeker / more advanced monitors out now though. Generally speaking I think you want a laser detector instead of the cheaper infrared detectors.

        - **criddell** · [2022-05-28 21:27 UTC](https://news.ycombinator.com/item?id=31544031)
          I found this link with test results: ^c31544031

          [https://www.aqmd.gov/aq-spec/evaluations/summary-pm](<https://www.aqmd.gov/aq-spec/evaluations/summary-pm>)

  - **MengerSponge** · [2022-05-28 16:41 UTC](https://news.ycombinator.com/item?id=31541703)
    If you live on a main road, there's likely a lot of pollution in the air. How much is actually in your home will depend on a lot of complicated things (prevailing winds, home construction, etc), so it's best and easiest to just measure. ^c31541703

    HN's own [https://news.ycombinator.com/user?id\=ahaucnx](<https://news.ycombinator.com/user?id=ahaucnx>) has a company with a DIY version: [https://news.ycombinator.com/item?id\=27124671](<https://news.ycombinator.com/item?id=27124671>)

    I got a Dylos before I learned about AirGradient, and I really like it too. Depending on your budget and tech savviness, it's a great option too.

    One important note: these detectors don't do chemistry, and not *everything* that causes a spike of PM is actually a problem. Showering, for example, will cause a spike for hours, but those salts are probably fine. Running the oven will also cause a spike, and those particles probably *aren't* fine.

  - **arinlen** · [2022-05-28 15:29 UTC](https://news.ycombinator.com/item?id=31541058)
    \> *Do they make a difference? Perhaps a placebo? A must have?* ^c31541058

    It really depends on where you're coming from.

    I have one of those air purifiers from Ikea (Förnuftig). It's cheap but not the cheapest. On any high dust/polen concentration level day, a minute or so with the device turned on at full blast is enough to make any problem go away in that particular room.

  - **fragmede** · [2022-05-28 15:23 UTC](https://news.ycombinator.com/item?id=31540990)
    PM2.5 particles are considered harmful, ingest at your own peril. Some air filters will also include an air monitoring device, so you can just for yourself how many of those particles are present (partially burnt food is an extremely common source of these). ^c31540990

  - **jaqalopes** · [2022-05-28 15:50 UTC](https://news.ycombinator.com/item?id=31541266)
    Ancedotally they work 100\%. Not only do they remove noticeable odors, they suck up tons of allergenic dust and invisible particulates that can mess with your breathing (if you have a sensitive respiratory system). ^c31541266

    Non-anecdotally, I've heard it claimed that indoor air pollution is the \#1 factor in reducing the lifespans of otherwise healthy people. No idea if this is the case or what the evidence is, but I don't find it hard to believe.

    - **Rastonbury** · [2022-05-28 16:16 UTC](https://news.ycombinator.com/item?id=31541500)
      In developing countries they have poor stoves at home which give of smoke/CO which is harmful aka indoor air pollution. A good easy way to prevents deaths/harm from these is to provide them with quality stoves. So depending on where you heard it, air pollution could mean these stoves which typical don't exist in the developed world ^c31541500

      - **legulere** · [2022-05-28 16:25 UTC](https://news.ycombinator.com/item?id=31541575)
        Frying things even on induction still easily drives particulate matter pollution to levels of bad days in China/India. ^c31541575

      - **Rebelgecko** · [2022-05-28 19:05 UTC](https://news.ycombinator.com/item?id=31542807)
        Even in developed countries, I think most homes still have gas stoves which are bad for indoor air quality. ^c31542807

  - **phphphphp** · [2022-05-28 15:21 UTC](https://news.ycombinator.com/item?id=31540971)
    I (in London) bought one recently (a COWAY Airmega) to try and improve the air quality in my apartment, specifically, the dust which has been reeking havoc on my breathing because of allergies. ^c31540971

    There is a noticeable improvement but it has not solved the problem by any stretch: so while I don’t regret the purchase, and will keep using it, I am not how sure I’d recommend them for the someone without breathing difficulties / allergies etc.

    - **teaearlgraycold** · [2022-05-28 15:57 UTC](https://news.ycombinator.com/item?id=31541321)
      I got the same one and it’s amazing for California when the air is smokey. ^c31541321

  - **trompetenaccoun** · [2022-05-28 16:27 UTC](https://news.ycombinator.com/item?id=31541594)
    If you don't understand the purpose, it means you don't need it - as so often. The reason they exist is that in some parts of the world the air is so bad it literally has significant negative health effects just breathing it. That's why people use them, and for what it's worth as far as I understand the quality ones do work, in the sense that you can use an air quality meter and detect a noticeable improvement in air quality. They have filters that you need to change regularly. ^c31541594

    \-Edit- Since so many people are raving about them and recommending you buying an air purifier I want to add this: If you live in a place where the air is truly that bad, my main recommendation would be to move. I have personal experience with this, it's not worth it living like that. You may filter the air in your home but then whenever you go outside you're at risk, if you do sports even more so. Some people wear surgical or cheap cloth masks but these don't actually work.

    Don't listen to people who tell you that you can "see" pollution of "feel" the difference. I've lived in some of the most polluted cities in the world and the truth is in most cases for regular healthy people they don't notice anything for years, even at pollution levels far beyond the imagination of folks in Western countries. Most of this is their imagination or placebo like you suspect. For example I've had people complain to me that the air is "so bad" in a place that's naturally foggy and where visibility is often low, but had good air quality. Others were happy about the lovely "clean" skys in a city that gets lots of sunshine but was actually horribly polluted. Also sure, smoke from wildfires is visible (and short lived) but a lot of the pollution from industrial sources isn't. It's a slow and stealthy killer.

  - **ms4720** · [2022-05-28 19:49 UTC](https://news.ycombinator.com/item?id=31543168)
    Depends on a few things: ^c31543168

    1\. what that particular filter filters out: ppm, mold, chemicals 
    2\. What is in the air being filtered
    3\. How sensitive you are to the things in your air
    4\. How often the rooms air gets filtered through the filter
    5\. How effective the filter is

    I worked in Beijing for a while and going somewhere with filtered air literally felt like a weight was removed some days.

  - **DragonStrength** · [2022-05-28 15:50 UTC](https://news.ycombinator.com/item?id=31541265)
    The biggest effect is in homes without any sort of central air system, which would usually include various levels of filters up to HEPA and UV systems at this point. During the worst of fire season in the Bay Area though, a single Coway HEPA filter, basically a box fan with a HEPA filter strapped to it, kept my apartment in the "safe" range for AQI. Just stepping out my apt front door into the hallway I'd be hit with the heavy stench of smoke. ^c31541265

    Truly remarkable how well they work, but whether you need one or not depends on whether you have allergens/pollution as an issue in your home. You can purchase an air quality monitor (I have a Temtop M10) or check online measurements of AQI, pollen, etc. for your area. If you have an issue, they work, but not everyone has an issue.

    - **techwiz137** · [2022-05-28 15:54 UTC](https://news.ycombinator.com/item?id=31541298)
      Okay so I bought a cheap-ish Air Purifier, now because the brand is...I think it's Chinese(Rohnsonn), I can't determine if it really does anything, if these filters do anything at all to improve my air quality and if the UV light is even strong enough to kill germs. Is there a way to verify it's effectiveness? ^c31541298

      - **DragonStrength** · [2022-05-28 16:09 UTC](https://news.ycombinator.com/item?id=31541431)
        I'd look at what the purifier claims to eliminate and find a quality monitor that will give you a reading. Most are portable, so you can compare to outdoor values directly. You're going to need some baseline to compare to though. If you have an AQI in the safe range already in your home, you'd have to contrive some actual experiments or find someone who already has. ^c31541431

        I'll say I'm pretty distrustful of anything but filters personally. My mom purchased a purifier at one point which claimed to use UV light to purify but had no fan to actually pull air through the light, so obviously, it wasn't doing anything.

  - **haunter** · [2022-05-28 15:29 UTC](https://news.ycombinator.com/item?id=31541051)
    My parents live in a very old house (\~1700s) and it reduced the dust significantly. Not perfect but maybe it's on the model too. Like it's not an \$1000 one which would probably work much better ^c31541051

    - **input\_sh** · [2022-05-28 22:15 UTC](https://news.ycombinator.com/item?id=31544341)
      They're pretty much all the same, just a fan in front of a HEPA filter. If you can get a square fan and tape a HEPA filter in front of it you'd get pretty much the same result as many modern air purifiers. ^c31544341

      You're paying for convenience and some bells and whistles (like a mobile app and an air quality reader), but the underlying technology behind it is pretty bare-bones, heavily tested, and heavily used in industrial applications.

  - **azuredragon** · [2022-05-28 17:21 UTC](https://news.ycombinator.com/item?id=31542044)
    They also double as a mosquito trap. I used to suffer persistent mosquito annoyance at night, but, since I got an air filter, the problem is gone. I often clean out dead mosquitos from the air filter ^c31542044

  - **throwaway290** · [2022-05-28 15:45 UTC](https://news.ycombinator.com/item?id=31541220)
    There is no level of pm2.5 that is considered safe to breathe, and it is easy to find out levels in your area so make your own call based on that. ^c31541220

    It will be a placebo if your home cannot be isolated from outside air or if you don't make an effort to keep windows closed when air is bad.

    Also, many expensive purifiers are overpriced junk compared to even simple DIY solutions like those found on particlecounting Tumblr and similar. Ideally the first thing to do is get some reputable air quality monitors.

  - **Mister\_Snuggles** · [2022-05-28 22:47 UTC](https://news.ycombinator.com/item?id=31544548)
    One of my cats, who's since passed away, was asthmatic.  Air purifiers throughout the house and a motion activated box fan plus furnace filter near the litterboxes resulted in an immediate and noticeable improvement in his quality of life.  I've noticed a similar improvement in my own health. ^c31544548

    I've since ended up with a variety of air cleaners:

    \* IKEA FÖRNUFTIG\[0\] is a small and relatively quiet unit.  It can be wall-mounted, so it can take up virtually no space.  The unit is reasonably priced.  Filters are cheap.

    \* IKEA STARKVIND\[1\] is a much larger unit (also available in end table form\[2\] to save space), but also relatively quiet on the lower speeds.  It's an interesting unit - integrates into Home Assistant (the unit speaks Zigbee), and has a PM2.5 air quality sensor.  This unit is a lot more expensive than the FÖRNUFTIG, but the filters are reasonably priced.

    \* The box fan plus single furnace filter is incredibly noisy, but really good at dealing with cat litter dust.  There is a huge range of price/quality when it comes to filters\[, I just use the cheaper ones since I'm focusing on large dust particles.

    \* I have a couple of units that use Bionaire aer1 filters\[3\].  The units I have are quiet and reasonably sized, though they get louder as the filter fills up.  The filters are expensive, and one of the units takes two of them which doesn't help matters.  There is a variety of filters available.

    There's a huge spectrum of tradeoffs between noise, size of the unit, filtration effectiveness, replacement filter cost, and extra features.  I'm not convinced I've found the sweet spot yet.

    \[0\] [https://www.ikea.com/ca/en/p/foernuftig-air-purifier-white-5...](<https://www.ikea.com/ca/en/p/foernuftig-air-purifier-white-50461961/>)

    \[1\] [https://www.ikea.com/ca/en/p/starkvind-air-purifier-black-40...](<https://www.ikea.com/ca/en/p/starkvind-air-purifier-black-40501967/>)

    \[2\] [https://www.ikea.com/ca/en/p/starkvind-table-with-air-purifi...](<https://www.ikea.com/ca/en/p/starkvind-table-with-air-purifier-additional-gas-filter-stained-oak-veneer-dark-brown-s09471350/>)

    \[3\] [https://www.bionairecanada.com/en\_CA/service-and-support/aer...](<https://www.bionairecanada.com/en_CA/service-and-support/aer1-homepage.html>)

  - **radicality** · [2022-05-28 16:27 UTC](https://news.ycombinator.com/item?id=31541595)
    I recently got a Medify Air MA 125 after a lot of research. Can recommend the brand. ^c31541595

    And yes it definitely makes a difference. Sometimes when I open my windows to get some “fresh” air and remove the co2 from my room, the ppm momentarily goes up.
    Also very useful for cooking since I don’t have a great vent. Ocassionaly when frying something ppm goes over 200 but it quickly drops down with the air filter.

  - **KennyBlanken** · [2022-05-28 16:29 UTC](https://news.ycombinator.com/item?id=31541611)
    If you have central air heating/AC and a vacuum cleaner that has a hepa bag, you likely don't need one; just buy filters that aren't the blue spiderweb kind and vacuum regularly. ^c31541611

    - **dzhiurgis** · [2022-05-28 18:46 UTC](https://news.ycombinator.com/item?id=31542674)
      HRV frequently has filters too ^c31542674

  - **herbst** · [2022-05-28 17:47 UTC](https://news.ycombinator.com/item?id=31542259)
    If you smoke indoors it's a must have I would say. It's a difference between day and night. ^c31542259

  - **unknown** · [2022-05-28 16:13 UTC](https://news.ycombinator.com/item?id=31541466)
    [deleted] ^c31541466

- **stavros** · [2022-05-28 21:59 UTC](https://news.ycombinator.com/item?id=31544242)
  Is there something that works well for cat hair? I can't stand it everywhere, but I don't know if these filters will catch them. I tried to build a box fan filter, but it moved basically no air :( ^c31544242

  - **Gigachad** · [2022-05-29 00:18 UTC](https://news.ycombinator.com/item?id=31545049)
    Nothing is going to be able to pull cat hair out of the air before it hits the ground without creating extreme wind. ^c31545049

    - **stavros** · [2022-05-29 00:36 UTC](https://news.ycombinator.com/item?id=31545116)
      It's fine if it hits the ground, as long as it doesn't get disturbed over and over into my food and face. ^c31545116

      - **gh02t** · [2022-05-29 01:00 UTC](https://news.ycombinator.com/item?id=31545235)
        Wouldn't a robot vacuum work better than a fan? That's what I use to keep husky fluff somewhat under control. ^c31545235

        - **stavros** · [2022-05-29 08:35 UTC](https://news.ycombinator.com/item?id=31547499)
          Hmm, that's a good point, thank you! ^c31547499

  - **Aerialoo** · [2022-05-28 22:08 UTC](https://news.ycombinator.com/item?id=31544295)
    Use a bigger fan ^c31544295

- **tym0** · [2022-06-08 12:11 UTC](https://news.ycombinator.com/item?id=31666111)
  You can just scratch it off and press the back button for a bit. ^c31666111

- **qgin** · [2022-05-28 16:15 UTC](https://news.ycombinator.com/item?id=31541478)
  This is maybe the wrong place to post this, but with fire season approaching, a pretty decent high-volume air purifier can be made using filters, tape, and a box fan: ^c31541478

  [https://www.texairfilters.com/a-variation-on-the-box-fan-wit...](<https://www.texairfilters.com/a-variation-on-the-box-fan-with-merv-13-filter-air-cleaner/>)

  - **oppositelock** · [2022-05-28 16:22 UTC](https://news.ycombinator.com/item?id=31541542)
    I used box fan filter setup to get through a couple of CA wildfire seasons, but they're loud and take lots of room. I used 4" filters in a triangle with the fan as the base. This setup is far more effective than a single filter because it makes the fan work better with some air space behind it. ^c31541542

    These days, I have a BlueAir 211 in each room. It's the same idea, just professionally made, it's not an eyesore, and it's quiet. Going by my AQI meter, they're also more effective.

  - **muxneo** · [2022-05-28 16:37 UTC](https://news.ycombinator.com/item?id=31541668)
    Absolutely brilliant. Saved 100 to 300 bucks right there. ^c31541668

    - **Havoc** · [2022-05-28 23:27 UTC](https://news.ycombinator.com/item?id=31544774)
      Though for some compromises. The ones that autoscale fan speed are really neat. ^c31544774

      I've had more than one instant of airfilter going wild reminding me I had forgotten a cooking plate on

  - **unknown** · [2022-05-28 16:55 UTC](https://news.ycombinator.com/item?id=31541835)
    [deleted] ^c31541835

    - **unknown** · [2022-05-28 16:56 UTC](https://news.ycombinator.com/item?id=31541837)
      [deleted] ^c31541837

