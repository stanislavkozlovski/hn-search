# [Air quality monitors: paying more does not get you more accuracy](https://news.ycombinator.com/item?id=36234790)

Article: [https://www.airgradient.com/open-airgradient/blog/expensive-air-quality-monitors-not-more-accurate/](<https://www.airgradient.com/open-airgradient/blog/expensive-air-quality-monitors-not-more-accurate/>)

ahaucnx · 2023-06-07 22:53 UTC · 213 reported comments · archived 2026-11-08 13:05 UTC
Observation: 2026-11-08 13:04 UTC → 2026-11-08 13:05 UTC

## Comments

- **ahaucnx** · [2023-06-08 01:19 UTC](https://news.ycombinator.com/item?id=36235954)
  Author here. ^c36235954

  I wrote this article a few weeks ago after discovering that a well known air quality monitor in the market that retails for more than USD 1000 actually uses a PM module that costs less than USD 20.

  Often people assume that the more expensive, the better but as you can see in the article this is often not the case -especially when it comes to the accuracy of the monitor.

  If you are looking for an open source / open hardware air quality monitor kit that uses high quality sensor modules and is very easy to assemble, have a look at the project we maintain. Instructions to built an indoor monitor \[1\], instructions to built an outdoor monitor \[2\] and overview of the kits \[3\]. All is open source (firmware, schematics, 3d files for enclosure, etc).

  \[1\] [https://www.airgradient.com/open-airgradient/instructions/di...](<https://www.airgradient.com/open-airgradient/instructions/diy-pro-v42/>)

  \[2\] [https://www.airgradient.com/open-airgradient/instructions/di...](<https://www.airgradient.com/open-airgradient/instructions/diy-open-air-presoldered-v11/>)

  \[3\] [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>)

  - **hammock** · [2023-06-08 03:34 UTC](https://news.ycombinator.com/item?id=36236853)
    The same is true of digital bathroom scales. In fact almost all consumer grade digital scales have “fake accuracy” built into the firmware that ensures the same exact weight shows up when you step on the scale twice in a row, even if you pick up e.g a quarter-pound weight in your hand the second time ^c36236853

    - **aulin** · [2023-06-08 05:39 UTC](https://news.ycombinator.com/item?id=36237675)
      I wouldn't say it's the same. ^c36237675

      Low cost air quality measurement is difficult. PM is tricky but almost manageable with laser scattering, toxic gases at typical inquinant concentrations are almost impossible to get right with electrochemical sensors, no matter how much money you throw at them.

      Weight measurement is easy, they could give you precise and accurate results but most customer base doesn't understand anything of physical quantities measurement and would panic they gained 50g in a minute if they showed up the real fluctuating values by stepping on the scale twice.

      - **jjoonathan** · [2023-06-08 13:40 UTC](https://news.ycombinator.com/item?id=36241721)
        No, they lie to cover up the cheapness and inadequacy of their flextures. "Users can't handle the truth" is a bullshit excuse and you should be ashamed for making it. ^c36241721

        - **riskable** · [2023-06-08 14:36 UTC](https://news.ycombinator.com/item?id=36242557)
          Whoah there:  Your typical (cheap) consumer scale will have four (50kg) load cells hooked up to an hx711 (or clone) and the cheapest microcontroller the manufacturer could find that can drive an LCD directly. ^c36242557

          Even the *cheapest* load cell is pretty damned accurate and the average between the four of them is going to be accurate within 0.1kg (\~0.22lbs).  Having said that, load cells have this problem where their values drift over time but *only if there's a constant weight on them*.  If you step off the scale and allow it to re-calibrate itself (which is what it does every time it turns on) there will definitely not be enough drift to matter from a, "how much do I weigh?" standpoint.  All it takes is like 2 seconds without weight for a load cell to "settle down" back to its not-actually-very-noisy resting position.

          I've tested *loads* of the cheapest possible load cells money could buy along with some load cells I took from an expensive transparent scale that had cracked.  They were all *far* more accurate than I was expecting and any differences between them was negligible.

          The longer you wait before weighing something the less accurate it'll be but only by tiny, negligible amounts.  Like, if you're weighing something that's 100kg and you waited ten minutes after calibration (something most scales won't allow because they all have something like a 30-second timeout) you'd still get a value that's within 0.01 of 100kg.  They don't drift *that* much at rest unless there's some serious temperature variations or you had something resting on the scale the entire time.

          - **jjoonathan** · [2023-06-08 14:57 UTC](https://news.ycombinator.com/item?id=36242927)
            When you cheap out on flextures, it's not the accuracy under ideal perpendicular loads that goes, and cheap housings struggle to provide ideal perpendicular loads. These are not particularly difficult things to get right, but the construction of even relatively expensive (\$150) scales is so cheap that it screws this up and results in \>1\% deviation over the surface of the scale if you bypass the digital cheating mechanism. ^c36242927

            Is it a big problem? No, but there's a fake decimal *and an attempt to hide that the decimal is fake*. Not cool.

            - **riskable** · [2023-06-08 15:46 UTC](https://news.ycombinator.com/item?id=36243863)
              What the heck are you talking about?  The only flexure to speak of is within the load cell itself and...  Can you even call that a flexure?  It's a teeny tiny strain gauge mounted on a piece of steel that's going to bend *ever so slightly* when a weight is put on it.  Even the cheapest load cells are precision-manufactured well within the tolerances necessary for the strain gauge to give you *damned* accurate results. ^c36243863

              I've never seen a human weight scale that went beyond a single decimal place and in all honestly they're going to be very accurate.  If you get on the scale and it says 201.2lbs that measurement is going to be accurate within ±0.1lbs (actually, more than that but you only get one decimal point of precision).  If you put the scale next to something that's emitting a ton of electrical noise then *maybe* it'll be off by 0.2lbs but I doubt it.

              - **mrguyorama** · [2023-06-08 16:51 UTC](https://news.ycombinator.com/item?id=36244945)
                Meanwhile, a precision of +-0.1lbs to measure humans is entirely superfluous. You can fluctuate an entire pound over the course of a day and your weight is not normally stable day to day. Analog scales only gave you about 2 sig figs, and that was probably a better outcome. ^c36244945

          - **verall** · [2023-06-09 14:45 UTC](https://news.ycombinator.com/item?id=36258622)
            Thanks for posting, this explains why a \$20 scale I got off Amazon which for some reason doesn't have the memory/smoothing feature is so impressively linear. ^c36258622

            My cat sat on it, read 9.4lb. I stood on it, it gave my weight, then I picked up my cat and it read (my weight + 9.4)lb.

            I was impressed!

        - **pagana** · [2023-06-08 14:16 UTC](https://news.ycombinator.com/item?id=36242243)
          That seems like an unnecessary escalation. It's possible that OP has observed what they're describing before. ^c36242243

          - **jjoonathan** · [2023-06-08 15:02 UTC](https://news.ycombinator.com/item?id=36243012)
            Yeah, but I've observed patronizing excuses for corporate misbehavior before and they trigger me a bit, what can I say. ^c36243012

            - **aulin** · [2023-06-08 15:35 UTC](https://news.ycombinator.com/item?id=36243665)
              My point was not to patronize anyone. My point was that one measurement (air quality) is difficult from a physics and technology standpoint. Low cost accurate air quality measurement at consumer level is not possible no matter how much you are willing to spend. ^c36243665

              The other one, weight, is easy enough and if it's not accurate it is for commercial reasons. Either because what I said or what you said. Both could be true.

      - **q87b** · [2023-06-08 11:38 UTC](https://news.ycombinator.com/item?id=36240201)
        Easy solution though, just limit the scale's display to a magnitude that it can accurately measure reproducible. ^c36240201

        - **riskable** · [2023-06-08 14:55 UTC](https://news.ycombinator.com/item?id=36242898)
          This is how the market for scales works:  You buy a scale for the weight class you're planning on measuring.  For example, you can't buy a scale made for weighing humans and expect it to be useful for weighing herbs or jewelry. ^c36242898

          It's because of how load cells (and scales) are manufactured.  They're made for weight classes like 100g, 1kg, 2kg, 3kg, 5kg, 10kg, etc.  So to make a scale for a particular weight you pick the load cells you'll need for the range you want.

          Higher quality scales don't select higher quality load cells; they're all the same (reasonable quality) for the most part!  Instead they just use *more* load cells and just take an average of all their values, multiplied by the number of cells, to measure weight.

          So if you want a *damned accurate* industrial scale for measuring weights around 1kg you'd use like twelve 100g load cells rather than a single 2kg load cell or two 1kg load cells.  Of course, then the hard part becomes, "how do I distribute this weight perfectly evenly across all of them?" so you have to take tolerances into account to make sure that at no point can weighing part of your scale rub against the side of its container or accidentally get something wedged between the scale part and the case.

          There's loads of other things to consider as well but *for the most part* the accuracy of the scale is a factor of how many load cells its using, not the quality/manufacturing tolerances of the load cells themselves.  Because even with the most precise manufacturing methods load cells *will* still drift and be impacted by temperature.  All you can do is calibrate regularly, *test them*, and hope for the best (or use a completely different technology).

        - **aulin** · [2023-06-08 15:25 UTC](https://news.ycombinator.com/item?id=36243475)
          Easy solution if your customer understands accuracy. They don't. ^c36243475

          They want the highest resolution so they can see their 10 gram progress when dieting. But they want the measurement to be stable enough to not cause them too much anxiety.

          - **pnt12** · [2023-06-09 12:58 UTC](https://news.ycombinator.com/item?id=36257187)
            \>They want the highest resolution so they can see their 10 gram progress when dieting. ^c36257187

            Do they? 100g is already quite granular, and you can lose that in a day.

            I have two scales which are giving me different measures - I've been weighting myself and assume I'm in the middle of both. It's a bit annoying, but works for my goals.

    - **ignite** · [2023-06-08 04:08 UTC](https://news.ycombinator.com/item?id=36237067)
      I just pick up a five pound weight and step on the scale, then put it down and step off. Step on again, and get he correct weight. ^c36237067

      Annoying, but it works.

      - **MaxikCZ** · [2023-06-08 06:34 UTC](https://news.ycombinator.com/item?id=36238078)
        Thats like having a car that always drives me somewhere I don't want before it drives me where I want. What the actual f\*ck. How are people okay with having such garbage in their homes. Why not just buy an analog spring scale... ^c36238078

        - **rootusrootus** · [2023-06-08 13:40 UTC](https://news.ycombinator.com/item?id=36241717)
          \> Why not just buy an analog spring scale... ^c36241717

          Because digital scales have features that analog ones do not.  And contrary to an earlier assertion that 'almost all' scales lie to get consistent results, this is very much not true.  There are reputable digital scales that do not behave that way.

        - **rocketbop** · [2023-06-08 10:34 UTC](https://news.ycombinator.com/item?id=36239679)
          I suspect the scale being accurate +-30g is sufficient for personal weight management unless you’re a professional boxer or need it to be exact for some reason. ^c36239679

        - **drukenemo** · [2023-06-08 06:41 UTC](https://news.ycombinator.com/item?id=36238114)
          Because like anything analog these days, they are hard to find? ^c36238114

          - **chronogram** · [2023-06-08 08:01 UTC](https://news.ycombinator.com/item?id=36238658)
            I can find mechanical scales very easily in the Netherlands, but they're more expensive. On Alibaba I see that digital bathroom scales are about \$2.50 and with WiFi/Bluetooth it's \$6, mechanical scales are double that at \$12 while also taking up more volume (more pallets and containers). With volume scale and unique designs, your own skin on the apps, and market specific packaging the margins are only going to get better for the (connected) digital scales. ^c36238658

            - **unknown** · [2023-06-08 11:58 UTC](https://news.ycombinator.com/item?id=36240399)
              [deleted] ^c36240399

            - **autoexec** · [2023-06-08 09:43 UTC](https://news.ycombinator.com/item?id=36239334)
              You have to take into account that a digital scale, especially one with an app, is going to be collecting endless amounts of data about you and selling it to anyone willing to pay. Your digital scale will end up costing you again and again for the rest of your life, every time someone uses that data against you. You'll just never be told when it's happening. ^c36239334

              - **ilyt** · [2023-06-08 11:18 UTC](https://news.ycombinator.com/item?id=36239998)
                ...get one without WiFi ? My takes one CR2032 battery every \~7 years ^c36239998

                - **autoexec** · [2023-06-08 11:22 UTC](https://news.ycombinator.com/item?id=36240036)
                  You're right that they're probably harmless if they're not connected to the internet and can't interact with a cell phone. ^c36240036

          - **cinntaile** · [2023-06-08 06:59 UTC](https://news.ycombinator.com/item?id=36238241)
            No they're not. ^c36238241

    - **Al-Khwarizmi** · [2023-06-08 07:12 UTC](https://news.ycombinator.com/item?id=36238344)
      That should be outright illegal... Why do they allow equipment that deliberately lies to the user? ^c36238344

      - **varjag** · [2023-06-08 08:13 UTC](https://news.ycombinator.com/item?id=36238741)
        Because the user otherwise will spot the discrepancy and pronounce "these scales are rubbish" (which in a way they are). ^c36238741

        - **lo\_zamoyski** · [2023-06-08 11:22 UTC](https://news.ycombinator.com/item?id=36240040)
          So why not fix the scale so it isn't rubbish? ^c36240040

          - **misnome** · [2023-06-08 13:07 UTC](https://news.ycombinator.com/item?id=36241237)
            That costs more, and the consumer wouldn’t buy it. ^c36241237

          - **mankyd** · [2023-06-08 13:10 UTC](https://news.ycombinator.com/item?id=36241274)
            Cost. ^c36241274

            They system has found an equilibrium: customers are willing to pay \~\$X for a scale. For \$X you can afford Y accuracy.

            If you increase the accuracy, great, but now your scale costs more then \$x.

      - **Cthulhu\_** · [2023-06-08 13:47 UTC](https://news.ycombinator.com/item?id=36241833)
        I'm not actually sure now you mention it; it used to be a serious crime to mess with weights and scales, when they were used for weighing coins. Probably still is. ^c36241833

        - **acka** · [2023-06-09 13:16 UTC](https://news.ycombinator.com/item?id=36257360)
          Most consumer grade personal scales are not certified medical devices like the blood pressure meters and scales at your GP's office. ^c36257360

      - **whamlastxmas** · [2023-06-08 13:29 UTC](https://news.ycombinator.com/item?id=36241546)
        Why are pharmaceutical companies allowed to sell medicine that has no improvement over placebo? See phenlyephrine which is in every single OTC decongestant/cold medication ^c36241546

        - **ch4s3** · [2023-06-08 13:54 UTC](https://news.ycombinator.com/item?id=36241926)
          That’s specifically because the DEA and congress cracked down on the useful alternative. ^c36241926

          - **93po** · [2023-06-10 16:47 UTC](https://news.ycombinator.com/item?id=36272144)
            That doesn't explain why they're allowed to sell something that doesn't actually do anything while claiming it does. It just explains why they want to. ^c36272144

      - **ffgjgf1** · [2023-06-08 07:52 UTC](https://news.ycombinator.com/item?id=36238586)
        Because users want to be lied to? ^c36238586

      - **atoav** · [2023-06-08 07:16 UTC](https://news.ycombinator.com/item?id=36238372)
        Because "they" have more influence in politics than the user. ^c36238372

        - **misnome** · [2023-06-08 13:08 UTC](https://news.ycombinator.com/item?id=36241248)
          Ah yes, the political conspiracies of “Big Scales”. ^c36241248

          - **atoav** · [2023-06-09 06:48 UTC](https://news.ycombinator.com/item?id=36254218)
            So you are claiming corporations affect regulations less than users? Doesn't match what I am observing as someone literate in (at least some) norms and regulations. ^c36254218

            What I wrote sounded more conspiratorial than I am planned, but I stand by the opinion that coperate interests are overrepresented in regulations.

    - **sidmitra** · [2023-06-08 03:42 UTC](https://news.ycombinator.com/item?id=36236907)
      Yes, but do you(or someone else) have a recommendation of which scale does not do this? Something that's not consumer grade, but not "enterprise cost" ^c36236907

      - **Luc** · [2023-06-08 08:00 UTC](https://news.ycombinator.com/item?id=36238652)
        I have looked for this myself, and come to the conclusion that it doesn't exist unless you're willing to buy a second hand, bulky hospital scale. ^c36238652

        Measuring human weight is harder than it seems (we don't stay still).

        Most scales use a strain gauge sensor that detects bending of a metal arm through changes in resistance. It's pretty noisy and needs averaging. There's some integrated circuits to relate the resistance to weight. Most do some factory calibration only around the target weights (median adult weights).

        Look instead for a scale that explicitly states that it is accurate over the whole range (e.g. baby to 220lbs). Usually there's tradeoffs - e.g. the displayed weight won't 'settle down'. I have one like this and it works better than any previous one I had (tested by adding calibrated weights), but I hesitate to recommend since it's a low cost consumer model.

        - **ilyt** · [2023-06-08 11:21 UTC](https://news.ycombinator.com/item?id=36240035)
          My \$10 +decade old one CR2032 powered one does that just fine. ^c36240035

          Accurate enough for weight control (doesn't drift from day to day), no "stuck weight" problem mentioned either. Just need to wait 2 seconds for self calibration to finish

          - **mrguyorama** · [2023-06-08 16:58 UTC](https://news.ycombinator.com/item?id=36245062)
            If your scale doesn't give you a different weight from one day to the next, either you are a very unusual human that doesn't ever change weight somehow, the scale only gives two sig figs, or it's lying to you. ^c36245062

            Humans are constantly changing weight, with every single breath you take.

            - **ilyt** · [2023-06-08 17:57 UTC](https://news.ycombinator.com/item?id=36245938)
              I eat once a day and weight myself in the morning before eating or drinking anything, hence the consistency. If I weight myself in other parts of the day I get different results so it isn't just weight stuck at same level. So I can see the trend based on what I ate last few days pretty quickly. ^c36245938

              I also tested on small weight and what my kitchen weight calls 3.016KG my bathroom weight calls 3.0KG so I'm pretty sure it's still reasonably accurate in absolute scale.

              - **justsomehnguy** · [2023-06-08 21:12 UTC](https://news.ycombinator.com/item?id=36249156)
                \> I also tested on small weight ^c36249156

                You need to weight youself and then weight yourself again with something of known weight in your hands.

                Floor scales usually aren't good at a small weights, though I wouldn't be surprised if they are not bad at it nowadays.

        - **rkagerer** · [2023-06-08 17:37 UTC](https://news.ycombinator.com/item?id=36245629)
          Even without endorsing, could you at least tell us the model? ^c36245629

          - **Luc** · [2023-06-16 09:30 UTC](https://news.ycombinator.com/item?id=36353804)
            Avec Maman AM05 ^c36353804

      - **kencausey** · [2023-06-08 03:53 UTC](https://news.ycombinator.com/item?id=36236973)
        There are still inexpensive purely mechanical scales.  I wouldn't expect much accuracy from a spring-based scale, but it should be consistent barring significant temperature variation. ^c36236973

      - **rootusrootus** · [2023-06-08 13:43 UTC](https://news.ycombinator.com/item?id=36241754)
        The Withings scales definitely do not. ^c36241754

        Personally, I've only ever had one scale in my life that I thought might be using memory to give false consistency.  But even then, it was short-term, not long term.  I.e. if you stepped off and back on, it might bias towards giving you the same weight.  If you walked away for a bit, then came back with a small extra weight in your hand, it was accurate.

      - **lajupechere** · [2023-06-08 05:07 UTC](https://news.ycombinator.com/item?id=36237473)
        My withings is constantly .2 fluctuating. If it’s faking that I’m going to chuck it out the window. It’s a very good scale, in aggregate the readings are useful. ^c36237473

        - **Lewton** · [2023-06-08 10:12 UTC](https://news.ycombinator.com/item?id=36239516)
          Another shout out for Withings, I definitely do not recognize the fake accuracy problem with this scale ^c36239516

      - **viraptor** · [2023-06-08 06:54 UTC](https://news.ycombinator.com/item?id=36238213)
        A cool tip I've seen before is to buy medical/laboratory equipment for scales. No fancy features, just durable build and accurate results. ^c36238213

      - **aSockPuppeteer** · [2023-06-08 06:14 UTC](https://news.ycombinator.com/item?id=36237927)
        Eufy smart scale P2 Pro. \$79.99 ^c36237927

        It has wifi and bluetooth, so it always syncs up with your phone and can track multiple people. I don't really trust the body measurement stuff but use it for measurement per measurement information. The heart rate is kind of nice to track too.

        - **rootusrootus** · [2023-06-08 13:45 UTC](https://news.ycombinator.com/item?id=36241798)
          Even cheaper, and IMO slightly more reputable, the \$50 withings scale is pretty great, and it's half the price of the version with useless body composition measurements. ^c36241798

          - **aSockPuppeteer** · [2023-06-11 18:34 UTC](https://news.ycombinator.com/item?id=36284240)
            Looks good too. I bought pre-doorbell controversy along with a doorbell. It appears Eufy/Anker is doing better now.(0) After having a couple different webcams taken over by security holes, mine only point outside and are hidden. ^c36284240

            0\. [https://www.theverge.com/23573362/anker-eufy-security-camera...](<https://www.theverge.com/23573362/anker-eufy-security-camera-answers-encryption>)

      - **zo1** · [2023-06-08 06:48 UTC](https://news.ycombinator.com/item?id=36238166)
        What about getting two cheap scales and averaging their values? From my third-world perspective, it sure beats the other suggestion from one of the other commenters to get a \$80 digital scale with bluetooth, wifi, fridge and Amazon prime integration. ^c36238166

      - **criddell** · [2023-06-08 11:21 UTC](https://news.ycombinator.com/item?id=36240034)
        The Nintendo Wii balance board is the only good scale you can get and it isn't expensive. A balance board, Wii, and small TV is probably around \$500. ^c36240034

        - **gsliepen** · [2023-06-08 13:11 UTC](https://news.ycombinator.com/item?id=36241291)
          You don't even need the Wii itself! You can connect to the balance board via Bluetooth, and there are several libraries out there that can read out its data (and that of the Wiimotes as well). ^c36241291

          - **criddell** · [2023-06-08 16:39 UTC](https://news.ycombinator.com/item?id=36244720)
            Do they give you the same feedback about shifting your weight so that you get an acceptably small deviation between the four sensors? ^c36244720

            - **gsliepen** · [2023-06-08 20:58 UTC](https://news.ycombinator.com/item?id=36248940)
              Yes, you get all the data. Sometimes you can see even more than what the Wii shows you. For example, with the Wiimotes, it actually shows you the position and brightness of the top 3 or 4 infrared light sources in its field of view (from that it can derive the position of the "sensor" bar). ^c36248940

              - **criddell** · [2023-06-09 02:18 UTC](https://news.ycombinator.com/item?id=36252289)
                If you have a link, it would be much appreciated. When I looked I didn’t see anything that came close to the functionality that the Balance Board had when attached to the Wii. It’s nice that the raw data is available, but unless it’s presented in a way that’s useful, it’s not that interesting. ^c36252289

                The only project I found was FitScales and it has been dead for a long time now because Android Bluetooth changes made it incompatible with newer devices.

      - **steve1977** · [2023-06-08 05:07 UTC](https://news.ycombinator.com/item?id=36237479)
        I made good experience with an Omron BF 511. As far as I know it doesn’t do this, would have to test though. ^c36237479

        The bodyfat measurement is good enough to be usable and the same scale is working in our household for almost 10 years now I believe.

    - **RicoElectrico** · [2023-06-08 11:36 UTC](https://news.ycombinator.com/item?id=36240176)
      I can recommend Xiaomi Smart Scale 2 (*not* the body composition one, it's nonsense). It is very accurate and repeatable. So much so, that you can see your weight drop after you go to the toilet. ^c36240176

      It is fascinating how much one's weight fluctuates during the day (or night which is even weirder if you don't eat/drink anything!)

      - **glauber** · [2023-06-08 12:30 UTC](https://news.ycombinator.com/item?id=36240780)
        Can confirm that! My morning routine includes “removing” any extra weight before weighting myself. It is very accurate. ^c36240780

        - **LazyMans** · [2023-06-08 15:21 UTC](https://news.ycombinator.com/item?id=36243388)
          It's like a game comparing the measurements ^c36243388

      - **stonemetal12** · [2023-06-08 13:12 UTC](https://news.ycombinator.com/item?id=36241308)
        At night you still sweat and breathe.  In fact weight loss in general occurs by breathing. Your body gets energy by breaking carbon bonds, then disposes of the carbon via breathing out CO2. ^c36241308

        - **whamlastxmas** · [2023-06-08 13:27 UTC](https://news.ycombinator.com/item?id=36241521)
          There is zero way your body is losing a quarter pound at night through either process in a room at 70 degrees ^c36241521

          - **mecsred** · [2023-06-08 13:57 UTC](https://news.ycombinator.com/item?id=36241958)
            According to \[0\], humans exhale about 11.0L of CO2 per hour at night. 02 in, CO2 out, so we can get mols of gas with ideal gas law and mass loss with molecular weight of carbon. If I did my math right, it comes out to 53.9g over 8 hours of sleep (if you can get that much ). (Americans: 0.118 lb/night). Not quite a quarter pound but maybe closer than you thought! ^c36241958

            \[0\][https://onlinelibrary.wiley.com/doi/10.1111/ina.12911](<https://onlinelibrary.wiley.com/doi/10.1111/ina.12911>)

            - **s1artibartfast** · [2023-06-08 18:15 UTC](https://news.ycombinator.com/item?id=36246236)
              Another way to look at this is the human body stores energy in glucose and fat ^c36246236

              Fat is 77\% carbon by weight, and glucose is 40\% carbon by weight (C18H34O2, C₆H₁₂O₆) . All off that carbon is broken down to CO2 and removed by the blood and lungs.

              2000 calories of fat is 0.57 lbs, and 0.44lbs of carbon. 2000 calories of glucose is 1.14 lbs, and 0.46lbs of carbon.

              The carbon masses are similar because the energy we use comes from breaking the carbon-carbon bonds these molecules.

              This means you exhale about a 0.45 lbs of carbon per day for baseline metabolism. Each pound of fat you lose is another 0.77 lbs of carbon on top of this (over however long you lost it).

              Compairing to your numbers, the approach above means you exhale 200g of carbon a day, and 8.3g/hr. If you sleep for 7 hours, that is 58 grams of carbon exhaled (pretty close).

            - **meragrin\_** · [2023-06-08 14:35 UTC](https://news.ycombinator.com/item?id=36242537)
              We also lose H20 through exhalation.  I imagine that can make up the difference. ^c36242537

              - **mecsred** · [2023-06-08 16:52 UTC](https://news.ycombinator.com/item?id=36244958)
                For sure, I would expect it to be more than the carbon difference. I think it would depend a lot more on circumstance so I couldn't really put concrete numbers to it here. ^c36244958

            - **jjoonathan** · [2023-06-08 14:03 UTC](https://news.ycombinator.com/item?id=36242050)
              Also, a Quarter Pounder is 417 Calories which is a bit less than 2000\*8/24, so that checks out. ^c36242050

          - **Cthulhu\_** · [2023-06-08 13:46 UTC](https://news.ycombinator.com/item?id=36241821)
            A quarter pound is only just over 100 grams, or about two shot glasses; you'll just breathe that out as water vapor, and then some. Plus sweating happens even when you're not feeling moist. ^c36241821

          - **NullPrefix** · [2023-06-08 16:58 UTC](https://news.ycombinator.com/item?id=36245073)
            Veritasium did a video on this. He lost around 250g each night, which is over half a pound. Some of that lost weight was CO2, some of it was water vapor and some of it was sweat. ^c36245073

            [https://www.youtube.com/watch?v\=lL2e0rWvjKI](<https://www.youtube.com/watch?v=lL2e0rWvjKI>)

            - **unknown** · [2023-06-10 16:48 UTC](https://news.ycombinator.com/item?id=36272171)
              [deleted] ^c36272171

            - **whamlastxmas** · [2023-06-10 16:49 UTC](https://news.ycombinator.com/item?id=36272185)
              Thanks for info - happy to accept I was wrong :) ^c36272185

          - **unknown** · [2023-06-08 17:49 UTC](https://news.ycombinator.com/item?id=36245824)
            [deleted] ^c36245824

      - **justsomehnguy** · [2023-06-08 12:38 UTC](https://news.ycombinator.com/item?id=36240873)
        \> So much so, that you can see your weight drop after you go to the toilet. ^c36240873

        That works with my NoName NoSmart TwentyBucks Scale scales too.

    - **rrrrrrrrrrrryan** · [2023-06-09 22:42 UTC](https://news.ycombinator.com/item?id=36265278)
      My bathroom scale shows tenths of a pound, but I think it's just because it's actually measuring some other unit (tenths of a kilo, maybe?), then converting that to pounds. ^c36265278

      I say that because it seems like certain tenths of a pound are outright impossible to achieve.

    - **michaelcampbell** · [2023-06-09 00:23 UTC](https://news.ycombinator.com/item?id=36251347)
      The one I have at least registers \~1 or 1.5\#, uhmmm, shall we say "sudden losses of weight". ^c36251347

    - **ilyt** · [2023-06-08 11:16 UTC](https://news.ycombinator.com/item?id=36239982)
      Source on that ? Never saw that and just checked my cheapo, it doesn't do it ^c36239982

      - **neogodless** · [2023-06-08 11:30 UTC](https://news.ycombinator.com/item?id=36240122)
        My Bowflex scale does this. I tend to switch modes / user profiles if I care about accuracy. ^c36240122

        - **ilyt** · [2023-06-08 13:41 UTC](https://news.ycombinator.com/item?id=36241740)
          See mine is too cheap to have any logic or memory in it ^c36241740

          - **neogodless** · [2023-06-08 14:47 UTC](https://news.ycombinator.com/item?id=36242755)
            *shrug* I bought it for \$39 about 11 years ago. ^c36242755

            - **ilyt** · [2023-06-08 18:02 UTC](https://news.ycombinator.com/item?id=36246039)
              I paid \$8 at least decade+ ago. I'm actually surprised it haven't fallen apart by now, it was "designed" by local company and of course made in china. ^c36246039

    - **xmdx** · [2023-06-08 10:34 UTC](https://news.ycombinator.com/item?id=36239684)
      Surprisingly my random scales off of Amazon do not do this. Accurate both times. ^c36239684

  - **dognotdog** · [2023-06-08 02:07 UTC](https://news.ycombinator.com/item?id=36236274)
    While I admire the efforts of the SC-AQMD, and generally agree with the article, using R2 from a higher-end, but not quite perfect instrument, can be quite misleading, and is not a great indicator of actual sensor performance. Also, there are a lot of potential improvements in sensor tech, but instead almost everyone is relying on the same cheap sensor modules instead of innovating, which have have pretty bad deficiencies, especially in detecting particulates in the ultra-fine range, and don’t age very well. But, they are the cheapest. ^c36236274

    - **ahaucnx** · [2023-06-08 03:30 UTC](https://news.ycombinator.com/item?id=36236821)
      The R2 is between the tested monitor and the AQMD reference instruments (BAMs and Grimms). They also test if the two reference instruments agree with each other before calculating the correlation to the tested monitor. ^c36236821

      So I believe their testing method is quite accurate.

      - **dognotdog** · [2023-06-08 12:37 UTC](https://news.ycombinator.com/item?id=36240865)
        This is probably a longer discussion, but PM0.3 (anything less than 0.3 microns) is quite difficult to measure, especially optically, as light scattering drops off very steeply once your particle sizes are around the wavelength of the light being used. Anything short of an SMPS class instrument that “grows” small particles through condensation so that they appear large enough to be counted, will not see much below 0.3 microns. Also, the total MASS of small particles might be low, but if you look at count, or lung-deposited surface area, we get a different picture. Especially around 0.3um, particulate matter is prone to get deep into the lungs, instead of being caught in the upper airways, and the small size means larger relative surface area, and thus higher reactivity. Even smaller nano particles might not go as deep, but are more likely to enter cells or the bloodstream due to their minuscule size. ^c36240865

  - **joshvm** · [2023-06-08 13:12 UTC](https://news.ycombinator.com/item?id=36241304)
    \> I wrote this article a few weeks ago after discovering that a well known air quality monitor in the market that retails for more than USD 1000 actually uses a PM module that costs less than USD 20. ^c36241304

    This may be true for off the shelf air sensors, but in general the base cost of the sensor is not necessarily correlated with achievable accuracy. There are even manufacturers like Maxim who will sell you sensors for cheap, but you pay a lot to license firmware to get the best performance (and in this case actually a smoke/particle detector if I remember right - the MAX30105).

    You might pay thousands for a third party calibration on top of the OEM device. For example an infrared calibration target is a puck of coarsely machined metal, a heater cartridge and some black paint, but you're paying \$\$\$ for NIST traceability, guaranteed measurements of the emissivity, etc.

    [https://hackaday.com/2017/04/11/ask-hackaday-how-does-this-a...](<https://hackaday.com/2017/04/11/ask-hackaday-how-does-this-air-particle-sensor-work/>)

    [https://www.sciencedirect.com/science/article/pii/S002185022...](<https://www.sciencedirect.com/science/article/pii/S0021850221005644>)

  - **RobotToaster** · [2023-06-08 11:49 UTC](https://news.ycombinator.com/item?id=36240307)
    You appear to be using CC BY-NC (although it's ambiguous if that applies to the schematics/3d files or only the instructions?) which isn't an open source licence, as it violates point 6 of the open source definition. \[0\] ^c36240307

    Sorry to be pedantic, but it spoils an otherwise interesting looking project.

    \[0\] [https://opensource.org/osd/](<https://opensource.org/osd/>)

    - **ahaucnx** · [2023-06-08 12:19 UTC](https://news.ycombinator.com/item?id=36240643)
      We use CC BY-SA 4.0, see for example here \[1\] which is open-source 'compatible'. We used -for a short time NC- but not anymore. Where did you see the NC license? Maybe we forgot to update it somewhere? ^c36240643

      We also wrote a blog post about our decision to use CC BY-SA \[2\].

      \[1\] [https://www.airgradient.com/open-airgradient/instructions/di...](<https://www.airgradient.com/open-airgradient/instructions/diy-pro-presoldered-v37/#license>)

      \[2\] [https://www.airgradient.com/open-airgradient/blog/thoughts-o...](<https://www.airgradient.com/open-airgradient/blog/thoughts-on-licensing/>)

      - **RobotToaster** · [2023-06-08 12:26 UTC](https://news.ycombinator.com/item?id=36240730)
        It's at the bottom of the first link you posted [https://www.airgradient.com/open-airgradient/instructions/di...](<https://www.airgradient.com/open-airgradient/instructions/diy-pro-v42/#license>) ^c36240730

        It's great that you chose to switch to an open source compatible licence.

        - **ahaucnx** · [2023-06-08 12:33 UTC](https://news.ycombinator.com/item?id=36240811)
          Thanks for spotting this. I will change it later today. ^c36240811

          - **ahaucnx** · [2023-06-08 14:11 UTC](https://news.ycombinator.com/item?id=36242168)
            Fixed ^c36242168

  - **BestGuess** · [2023-06-10 02:32 UTC](https://news.ycombinator.com/item?id=36266997)
    You might know or know what kind of academics or something I could ask, but how do I go about photographing and videoing and proving cigarette smoke? Best I can figure blue lasers or very strong blue LED lights but "this smoke is cigarette smoke" is givin me trouble got asthma keep getting "smoke free" apartments that put me next to chronic smokers and all the law will do if I ain't got proof is let me break the lease. That's happened several times so far but if I can get proof "this is cigarette smoke it only comes from this apartment" I can get rid of the person instead of being forced to move for the 5th time ^c36266997

  - **reassembled** · [2023-06-08 09:48 UTC](https://news.ycombinator.com/item?id=36239359)
    Have you compared the Sensirion SEN55 against the Plantower sensors? I ask because I’ve recently picked up both and have played around with them each individually but haven’t compared them for accuracy yet. The nice thing about the SEN55 is that it contains all of the sensors in one unit (PM1.0 to PM10.0, temperature, Relative Humidity, NOX and VOC). ^c36239359

    They do cost a little bit more than the Plantower units, about \$30-40USD. For anyone looking at the Sensirion sensors, be aware that the SEN5x products span a range, and only the SEN55 has all of the above sensors in one unit. I’ve found the Sensirion software to be pretty nice to work with. I was able to port their embedded i2c example repo to ESP32 with little trouble.

    - **ahaucnx** · [2023-06-08 10:53 UTC](https://news.ycombinator.com/item?id=36239813)
      Yes, we are looking at the SEN55. The reason we currently still use the Plantowers is that there is a lot more research out there on the Plantower and how it behaves in different environments. ^c36239813

      - **sarabveer** · [2023-06-08 15:54 UTC](https://news.ycombinator.com/item?id=36244005)
        I would definitely like some research into the SEN5x line of sensors. I have three air quality monitors in the house. Two of them are AirGradient kits (Basic and Pro), with the other one I made myself using a SEN55 and SCD41. All of them are using ESPHome for the firmware. ^c36244005

        With the current very bad air quality in the US Northeast, I noticed that the SEN55 was reading much higher than the two Plantowers in the AirGradients. At one point, the SEN55 was reading around 200µg/m³, while the Plantowers were reading around 100µg/m³. I am planning on buying a second SEN55 to check this.

    - **hyperbovine** · [2023-06-08 14:22 UTC](https://news.ycombinator.com/item?id=36242329)
      \+1 for the SEN5X. Incredible little sensor. I picked up a devkit a year ago when it first came out, intending to build an OSS AQM around it, but alas, time and young kids got in the way. I'm really hoping it gains traction in the community. ^c36242329

  - **kiney** · [2023-06-08 13:18 UTC](https://news.ycombinator.com/item?id=36241383)
    I am actually not surprised as ai noticed similiar non-correlation of price and quality with different products. ^c36241383

    For headphones someone made a small analysis regarding at leat frequency response and price:
    [https://pubs.aip.org/asa/jasa/article/141/6/EL526/917945/No-...](<https://pubs.aip.org/asa/jasa/article/141/6/EL526/917945/No-correlation-between-headphone-frequency>)

  - **mnw21cam** · [2023-06-08 11:44 UTC](https://news.ycombinator.com/item?id=36240241)
    Please could you consider changing the CSS on the article. At the moment, the web page has "display: block" on almost everything, which does exactly what it says on the tin and produces a blank white page, which does make it a little difficult to read the content. ^c36240241

    - **DHPersonal** · [2023-06-08 13:52 UTC](https://news.ycombinator.com/item?id=36241908)
      \`Display: block\` doesn't hide content; that's what \`display: none\` does. ^c36241908

    - **83** · [2023-06-08 17:23 UTC](https://news.ycombinator.com/item?id=36245445)
      [https://www.w3schools.com/cssref/pr\_class\_display.php](<https://www.w3schools.com/cssref/pr_class_display.php>) ^c36245445

      - **mnw21cam** · [2023-06-08 19:26 UTC](https://news.ycombinator.com/item?id=36247349)
        I stand corrected. But anyhow, *something* in the css is making it show just a blank white page. ^c36247349

    - **whamlastxmas** · [2023-06-08 13:48 UTC](https://news.ycombinator.com/item?id=36241843)
      Browser reading mode is good for fixing this ^c36241843

  - **smcleod** · [2023-06-08 03:46 UTC](https://news.ycombinator.com/item?id=36236930)
    Out of interest what are your thoughts on the Aranet4? (other than it's quite high price of course). ^c36236930

    - **ahaucnx** · [2023-06-08 04:33 UTC](https://news.ycombinator.com/item?id=36237239)
      As far as I know the Aranet uses NDIR CO2 sensor modules from SenseAir. We do use the same brand in our DIY kits and they are very accurate and probably one of the best low-cost CO2 sensors. ^c36237239

      - **smcleod** · [2023-06-08 08:15 UTC](https://news.ycombinator.com/item?id=36238760)
        Cool, good to know. Thank you for taking the time to respond! ^c36238760

  - **supermatt** · [2023-06-08 07:51 UTC](https://news.ycombinator.com/item?id=36238582)
    What is the difference between the indoor/outdoor kit? It seems the outdoor one contains more sensors but is less expensive? (or is this a nod to the article in some way ;)) ^c36238582

    My partner has a pottery studio with a kiln, it can get pretty smoggy in there when a firing is taking place (its unoccupied during, but it takes a while to settle afterwards), so I want to get a sensor. Are there any add-on sensors you can think of that would be useful in addition to assess off-gassing of VOCs (or something else?) from the kiln firing?

    - **ahaucnx** · [2023-06-08 10:57 UTC](https://news.ycombinator.com/item?id=36239839)
      The outdoor kit focuses on PM measurements with dual PM modules for enhanced accuracy. The indoor kit has in addition CO2 and an optional TVOC sensor. ^c36239839

      I think for a pottery studio to measure PM and VOCs is a good start (and CO2 to see how well the ventilation works).

      - **gh02t** · [2023-06-08 14:08 UTC](https://news.ycombinator.com/item?id=36242129)
        Have you looked into the longevity of the Plantower PM sensors outdoors? I have long wanted to have one outside but I've always been reluctant because there is a *lot* of pollen around where I am during the warmer months and I assumed that would clog them up fairly quickly. ^c36242129

        - **ahaucnx** · [2023-06-08 14:13 UTC](https://news.ycombinator.com/item?id=36242198)
          Outdoors we see quite different lifetimes with the Plantower. Sometimes insects are getting into it and reduce the lifetime. No experience with pollen. ^c36242198

      - **supermatt** · [2023-06-09 04:17 UTC](https://news.ycombinator.com/item?id=36253068)
        Thanks! Order placed :) ^c36253068

  - **casenmgreen** · [2023-06-08 09:54 UTC](https://news.ycombinator.com/item?id=36239391)
    I would buy a couple of these in an instant, it's *exactly* what I want, *except* it's so BIG.  I want something as small as reasonably possible. ^c36239391

    - **ahaucnx** · [2023-06-08 10:55 UTC](https://news.ycombinator.com/item?id=36239824)
      We originally designed a smaller monitor but it makes it very difficult to get an accurate temperature reading because the enclosure heats up and you cannot have a good distance from the active components to the temperature sensor. ^c36239824

      - **ilyt** · [2023-06-08 11:24 UTC](https://news.ycombinator.com/item?id=36240056)
        Wouldn't just correction factor be enough ? If device takes constant power it should also heat the sensor by constant amount ^c36240056

        - **ahaucnx** · [2023-06-08 11:35 UTC](https://news.ycombinator.com/item?id=36240168)
          Yes to some extent but the correction factors will be influenced by absolute temperature levels, airflow in the room etc. ^c36240168

          - **ilyt** · [2023-06-08 13:21 UTC](https://news.ycombinator.com/item?id=36241430)
            Would probably be easier in all-in-one integrated sensor and not "a bunch of separate parts" as then the temp sensor could just be near incoming air so any heating from the board would be offseted by that ^c36241430

      - **casenmgreen** · [2023-06-09 07:15 UTC](https://news.ycombinator.com/item?id=36254405)
        Thank you very much for explaining. ^c36254405

        I'm happy with that, and I will place an order.

  - **wintermutestwin** · [2023-06-08 15:41 UTC](https://news.ycombinator.com/item?id=36243779)
    Just a note to say that I bought the Air Gradient pre-soldered indoor monitor kit. It was simple to put together and I appreciate the lack of a required cloud server connection. I'm glad to the the outdoor monitor kit is now available - just in time for fire season! ^c36243779

  - **psyklic** · [2023-06-08 05:50 UTC](https://news.ycombinator.com/item?id=36237744)
    Interesting analysis! ^c36237744

    Minor typo throughout: It's R\^2 instead of R\_2.

    Also surprised the dataset doesn't include Awair's products!

    - **ahaucnx** · [2023-06-08 07:26 UTC](https://news.ycombinator.com/item?id=36238437)
      Thanks! Fixed. ^c36238437

- **AceJohnny2** · [2023-06-08 04:34 UTC](https://news.ycombinator.com/item?id=36237252)
  It seems a lot of air quality monitors, such as the PurpleAir PA-II \[1\] , are just wrapping the Plantower PMS5003 \[2\], which is a turnkey particle sensor which integrates laser sensors, airflow, and MCU to perform measurements and spit out results on a serial bus. ^c36237252

  I'm pretty surprised by the lack of diversity in the "consumer" market.

  \[1\] [https://www2.purpleair.com/products/purpleair-pa-ii?variant\=...](<https://www2.purpleair.com/products/purpleair-pa-ii?variant=40067691708513>)

  \[2\] available e.g. [https://www.adafruit.com/product/3686](<https://www.adafruit.com/product/3686>)

  - **samtho** · [2023-06-08 05:54 UTC](https://news.ycombinator.com/item?id=36237772)
    I’ve used a lot of different sensors for random purposes and it’s almost always the same few companies (or a knockoff of them) at each the price point. ^c36237772

    Building a sensor-on-ic is more comparable to the process that pharmaceutical companies go through in their R&D rather than traditional logic chip makers. It’s a lot of experimenting, use of non-standard materials, and pushing fabrication techniques to their limits. They don’t have to disclose how it’s made in the same way as pharmaceutical companies are required to, however, which means they have a monopoly on the tech until someone decaps the IC and reverse engineers it.

- **ioulian** · [2023-06-08 07:30 UTC](https://news.ycombinator.com/item?id=36238461)
  For people who use Home Assistant, I've gone with DIY route with ESPHome \[1\] and senseair CO2 sensor. You can buy those sensors for +- 26 USD on AliExpress. Together with 5 USD, ESP32 devkit, it's mostly "solder"-n-play. ^c36238461

  Of course, I only have one of them, so I can't say if they are accurate, but I just need to know if the CO2 levels are normal (+- 400ppm) or high (+1000ppm), to open a window. I have tested it with just blowing on it, the CO2 value jumps up, putting it near a window, goes directly to +- 400.

  I haven't had any strange readings with it, ESPHome developers really made an excellent product, that is stable and "just works". You can even calibrate the sensor by putting the it outside (but I haven't really bothered with it).

  ESPHome has also support for a lot of other sensors that you combine on a single ESP32 module.

  \[1\] [https://esphome.io/components/sensor/senseair.html](<https://esphome.io/components/sensor/senseair.html>)

  - **plett** · [2023-06-08 08:19 UTC](https://news.ycombinator.com/item?id=36238782)
    I attached a cheap IKEA Vindriktning PM2.5 sensor to esphome to get air cleanliness data into Home Assistant \[1\]. That's also very simple to do - solder some wires and write a few lines of yaml and it shows up in the web UI. I bought two of them and they are accurate to each other, so the sensors appear to be acceptable. ^c36238782

    \[1\] [https://plett.uk/posts/ikea-air-sensor/](<https://plett.uk/posts/ikea-air-sensor/>)

    - **jve** · [2023-06-08 11:49 UTC](https://news.ycombinator.com/item?id=36240302)
      They are extremely inaccurate. But relative measurement is OK - you can see rising or falling pollution. When I put one in kitchen it "died" pretty fast - I think the cooking oil grease got onto the sensor and it is game over for me. Shows MAX PM2.5 all the time. ^c36240302

    - **noja** · [2023-06-08 11:51 UTC](https://news.ycombinator.com/item?id=36240319)
      Do you know if the new ikea air quality sensor has the same fan as the first one? The original had a fan that would turn on and off every ten seconds. ^c36240319

      - **joecool1029** · [2023-06-13 21:03 UTC](https://news.ycombinator.com/item?id=36317307)
        It does but it's a different sensor and doesn't pulse as frequently (I think it has a weekly pulse to clean it... SENS54 is the sensor if you want to look it up) ^c36317307

  - **eternauta3k** · [2023-06-08 14:03 UTC](https://news.ycombinator.com/item?id=36242056)
    You could measure (almost) pure CO2 sensitivity by putting it in a pot with a glass of sparkling water. ^c36242056

  - **whamlastxmas** · [2023-06-08 13:53 UTC](https://news.ycombinator.com/item?id=36241920)
    Can’t wait for the Thread ESP32 units to be better developed ^c36241920

- **mnw21cam** · [2023-06-08 11:52 UTC](https://news.ycombinator.com/item?id=36240326)
  The article is about PM2.5 consumer units, and I can well believe that price doesn't make much difference. ^c36240326

  However, I'd like to point out CO\_2 - there are two kinds of sensor. One of them measures volatile organic compounds and assumes that CO\_2 correlates with them, and the other actually measures CO\_2. The second type costs around £40 for the raw sensor - if your sensor is cheaper than that then it probably isn't actually measuring CO\_2.

  - **ImaCake** · [2023-06-08 12:38 UTC](https://news.ycombinator.com/item?id=36240883)
    If it's measuring VOCs and you live in a city then chances are it would be measuring car exhaust! ^c36240883

    - **michaelcampbell** · [2023-06-09 00:28 UTC](https://news.ycombinator.com/item?id=36251395)
      Is that bad?  I mean, VOC's are VOC's regardless of source, no? ^c36251395

      - **ImaCake** · [2023-06-13 07:42 UTC](https://news.ycombinator.com/item?id=36306898)
        Depends if you care about CO2 and presumably the CO2 from breathing humans. The VOCs from cars in a busy city will mask/overwhelm/confound any measure of human body produced CO2 in that location. But a more suburban or rural location will be fine. ^c36306898

- **toomuchtodo** · [2023-06-08 01:13 UTC](https://news.ycombinator.com/item?id=36235912)
  Does anyone have experience with the open air monitor version \[1\]? I am looking for an affordable outdoor air sensor that will be used to collect data from certain urban and suburban areas to use as evidence in efforts to dissuade (through public comment periods and possible litigation) industrial rezoning near residential areas due to pm2.5 and other combustion emission pollution (and deploying a sensor network to establish a baseline). ^c36235912

  \[1\] [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>)

  - **ahaucnx** · [2023-06-08 01:24 UTC](https://news.ycombinator.com/item?id=36235991)
    Thank you for mentioning our kits. ^c36235991

    The Open Air outdoor monitor has been designed in co-operation with scientists and is currently undergoing co-location testing on four continents to collect a large dataset and being able to completely understand the performance in different environments and to develop accurate compensation algorythms if required. The first results look very good. You can read more about it on our research page \[1\].

    We get a lot of interest and support from the research community on this monitor as it is completely open hardware / open source.

    \[1\] [https://www.airgradient.com/research/](<https://www.airgradient.com/research/>)

    - **toomuchtodo** · [2023-06-08 01:35 UTC](https://news.ycombinator.com/item?id=36236066)
      Thank you for taking the time to reply! Genuinely appreciate it. ^c36236066

- **flanbiscuit** · [2023-06-08 14:05 UTC](https://news.ycombinator.com/item?id=36242081)
  A relevant discussion about air quality sensors from less than a year ago: ^c36242081

  "Many indoor air quality sensor products are a scam" - [https://news.ycombinator.com/item?id\=33025995](<https://news.ycombinator.com/item?id=33025995>)

  I almost bought Airgradient's pre-soldered kit\[1\] but I went with the Airthings View Plus\[2\] because it came with a Radon sensor. It's pricey (US\$299), but not \$1000 pricey as mentioned in the article. But I think I might still get the Airgradient sensor for another room just because it's cheaper and I don't need more than one Radon sensor.

  1\. [https://www.airgradient.com/open-airgradient/shop/\#!/DIY-Pro...](<https://www.airgradient.com/open-airgradient/shop/#!/DIY-Pro-Kit-Pre-Soldered-version-4-2/p/476627519/category=0>)

  2\. [https://www.airthings.com/en/view-plus](<https://www.airthings.com/en/view-plus>)

- **Johnny555** · [2023-06-08 04:11 UTC](https://news.ycombinator.com/item?id=36237094)
  I was glad to see that the PurpleAir PA-II sensor (which I have outside and refer to often during wildfire season) has relatively good performance, at least for PM1.0 and PM2.5. ^c36237094

  PM1.0 R2 \> 0.96, PM2.5 R2 \> 0.93

  [https://www.aqmd.gov/docs/default-source/aq-spec/summary/pur...](<https://www.aqmd.gov/docs/default-source/aq-spec/summary/purpleair-pa-ii---summary-report.pdf?sfvrsn=16>)

- **synack** · [2023-06-08 01:30 UTC](https://news.ycombinator.com/item?id=36236033)
  There's some good empirical data about the cheap PM2.5 sensors that Adafruit sells on their forum. The sensor itself has a microcontroller that filters the raw values and you need to keep this in mind when interpreting the data. ^c36236033

  [https://forums.adafruit.com/viewtopic.php?f\=48&t\=136528&p\=76...](<https://forums.adafruit.com/viewtopic.php?f=48&t=136528&p=767725#p767725>)

- **pawelduda** · [2023-06-08 11:55 UTC](https://news.ycombinator.com/item?id=36240357)
  For CO2 I'm satisfied with airthings sensor. Hard to say how accurate the readings are because I didn't compare it to anything, it self-calibrated for a week first. From random tests I can see it reacts properly in indoor/outdoor/open window/few people sitting in unventilated room/someone exercising/cooking scenarios. Integrates with HomeAssistant through their cloud and seems like it's being pooled for readings so it's not perfect but not why I bought it. ^c36240357

  The main takeaway is that it takes more than I thought to keep indoor CO2 at bay, especially during winter when you have to deal with low temp/air pollution outside.

- **bullen** · [2023-06-08 08:09 UTC](https://news.ycombinator.com/item?id=36238714)
  I bought the Pimoroni one and it broke after 6 months. ^c36238714

  Interesting to see the particles spike when frying food but other than that I only learned in which direction the wind has to blow for my air to be polluted (straight south so in the future might enable ionization then if pollution goes ballistic).

  What you need is a sensor that measures CO, CO2, all the hydrocarbons AND particles at different sizes. The Pimoroni could measure 1!, 2.5 and 10 PPM.

  Just use: [https://maps.sensor.community](<https://maps.sensor.community>) and [https://www.ventusky.com](<https://www.ventusky.com>)

  - **asdff** · [2023-06-08 08:14 UTC](https://news.ycombinator.com/item?id=36238751)
    That website isn't so useful outside of central europe for what its worth. Purple air is pretty good. ^c36238751

- **tuatoru** · [2023-06-08 02:09 UTC](https://news.ycombinator.com/item?id=36236283)
  Calibrating PM2.5 sensors looks difficult. Relative humidity, temperature, different mixes of inorganic and organic aerosols, probably air pressure, integration times -- lots of dimensions. ^c36236283

  PALMA\[1\] has a lot of work.

  1\. [https://www.mdpi.com/2076-3417/11/19/9014](<https://www.mdpi.com/2076-3417/11/19/9014>)

- **athollywood** · [2023-06-08 02:02 UTC](https://news.ycombinator.com/item?id=36236232)
  I bought a fairly expensive air quality monitor. Accuracy wasn’t what caused me to go with a more expensive model. I wanted CO2 readings, which most models under \$200 don’t provide. ^c36236232

  - **bombcar** · [2023-06-08 02:23 UTC](https://news.ycombinator.com/item?id=36236398)
    I suspect I know exactly which one you bought ;) ^c36236398

    I wish I could find a good source for "outside CO2 levels" as I think they've been elevated but I have no way to prove it (beyond my indoor sensor showing high).

    - **newman314** · [2023-06-08 02:28 UTC](https://news.ycombinator.com/item?id=36236430)
      Aranet4 is the way to go. ^c36236430

      Tried going cheap and getting a bunch of Vitalights later as additional monitors but ended up finding out that their results were all over the place.

      Returned the Vitalight. Kept the Aranet4.

      I do have plans to build a few Airgradients when I have time.

      - **trog** · [2023-06-08 05:38 UTC](https://news.ycombinator.com/item?id=36237667)
        co2.click also worth a look: [https://www.co2.click/](<https://www.co2.click/>) ^c36237667

        - **\_zoltan\_** · [2023-06-08 08:58 UTC](https://news.ycombinator.com/item?id=36239027)
          uf, looks so ugly. I can't justify putting this into my home. ^c36239027

          - **autoexec** · [2023-06-08 09:48 UTC](https://news.ycombinator.com/item?id=36239361)
            it's a box? You could put a sticker on it, bedazzle it, or paint it with nail polish if you want something fancier. ^c36239361

      - **victor106** · [2023-06-08 15:00 UTC](https://news.ycombinator.com/item?id=36242981)
        It does not seem to have PM2.5 ^c36242981

    - **athollywood** · [2023-06-08 02:30 UTC](https://news.ycombinator.com/item?id=36236445)
      Airthings! It’s great. ^c36236445

  - **gfd** · [2023-06-08 02:46 UTC](https://news.ycombinator.com/item?id=36236543)
    Airgradient's kit has CO2! ^c36236543

  - **agos** · [2023-06-08 07:37 UTC](https://news.ycombinator.com/item?id=36238496)
    can you share which one was it? I'm also looking for one, and CO2 is surprisingly uncommon. I'd also love for it to be HomeKit compatible, which makes it nearly impossible ^c36238496

    - **sjf** · [2023-06-08 08:38 UTC](https://news.ycombinator.com/item?id=36238906)
      I have the Airthings view plus. It measures PM2.5, PM1, CO2, VOC, Radon. It was kind of expensive but I am happy with it. ^c36238906

- **kingsloi** · [2023-06-08 14:24 UTC](https://news.ycombinator.com/item?id=36242369)
  Interesting article - good to know, too! ^c36242369

  I've been tracking air quality in Gary, IN for a few years now. It started with a PurpleAir (\$), then a AQMesh pod (\$\$\$\$\$) for a few months, now I'm rocking a Sensit RAMP (\$\$\$). Just haven't spent too much time updating the dashboard I built to showcase the data: [https://millerbeach.community](<https://millerbeach.community>). I had one sensor up and running at a time, so couldn't compare all 3 (PM only) against each other.

  Indoors, I've been using a Canairi Air Quality Sensor, but that's just a simple CO2 monitor, along with my Dyson hot/cool air purifier.

  I'm looking for a rough idea of what my family are breathing, I don't mind if numbers aren't 100\% accurate (hopefully as small -/+ \%, though).

- **zX41ZdbW** · [2023-06-08 09:08 UTC](https://news.ycombinator.com/item?id=36239113)
  Good instruction on building your own sensor here: [https://sensor.community/en/sensors/airrohr/](<https://sensor.community/en/sensors/airrohr/>) ^c36239113

  As a bonus, the collected data by the sensors.community project is public, and here is the walkthrough of data analysis with ClickHouse: [https://clickhouse.com/docs/en/getting-started/example-datas...](<https://clickhouse.com/docs/en/getting-started/example-datasets/environmental-sensors>)

- **pachico** · [2023-06-08 05:22 UTC](https://news.ycombinator.com/item?id=36237567)
  This is not a joke, I am really asking: how do you measure the accuracy of an air quality monitor? Comparing it to another monitor? Creating an air pollution condition and seeing how close to that is the measurement? ^c36237567

  - **Rebelgecko** · [2023-06-08 07:01 UTC](https://news.ycombinator.com/item?id=36238259)
    The state of the art for reasonably priced CO2 monitors seems to be that they hard code in the "ambient" Co2 level and  instructions tell you to let it sit outside every once in a while. The the sensor adjusts can adjust it's baseline accordingly , assuming that the lowest CO2 level it's seen in the last week or so is equivalent to the "ambient" outside level. Ofc this is susceptible to issues and can require even more adjustments since CO2 levels go up every year. A sensor from 10 years ago might read 5\% lower than a modern one because it's using an out of date baseline CO2. ^c36238259

    - **EVa5I7bHFq9mnYK** · [2023-06-08 09:13 UTC](https://news.ycombinator.com/item?id=36239147)
      Here we are talking about 1-2 ppm accuracies. I don't need more than 100ppm accuracy from my CO2 monitor. Hell, just show me one of 4 values: 400, 600, 800 and 1000+ but don't lie. ^c36239147

      - **electroly** · [2023-06-09 14:49 UTC](https://news.ycombinator.com/item?id=36258677)
        The second part of OP's post maybe, but not the first part about needing to place the device outside to set the ambient baseline. They basically can't measure *at all* without that. ^c36258677

        My Aranet4 was more like *1000* ppm off before putting it outside for awhile, despite being labeled as calibrated from the factory. It was going absolutely ballistic thinking my apartment was full of smog. After sitting outside to get a taste of ambient air, suddenly the inside of my apartment was fine.

    - **adhesive\_wombat** · [2023-06-08 08:14 UTC](https://news.ycombinator.com/item?id=36238750)
      New shareholder value opportunity: Pay an extra 10\% and get a dynamic baseline model that hardcodes a baseline level and expected *gradient* of 0.5\% per year. ^c36238750

      By the time the device lands in landfill, it probably won't ever have been too far off. And if the CO2 curve derivative starts to underperform and risk your deployed calibrations, throw some dollars an some anti-nuclear campaigns as that's cheaper than doing an update!

    - **nicbou** · [2023-06-08 07:59 UTC](https://news.ycombinator.com/item?id=36238642)
      That last sentence was a punch in the gut ^c36238642

  - **crazygringo** · [2023-06-08 15:53 UTC](https://news.ycombinator.com/item?id=36243996)
    You don't really need super accuracy in the way you do for a body weight scale where a 2\% change matters. ^c36243996

    You watch the readings go up and down as you close windows and cook and then open windows and let the fresh air in. You'll watch CO2 go up to 1200 and then back down to 500. Or PM2.5 go from 2 to 25 and back.

    They're big changes that obviously correlate in logical ways with what is happening in your home.

    And then it's really the relative changes you're watching. Even if values are off by 20\% it doesn't really matter a ton for private personal use.

    Because you're really just learning what the baseline values are for fresh air, how quickly values grow, and therefore when you prefer to open some windows. (Or this week, close them.)

  - **Leo\_Germond** · [2023-06-08 07:44 UTC](https://news.ycombinator.com/item?id=36238543)
    One way is to set up a flottila of sensors around a certified control sensor, such as an aerotrack, and measure how they evolve in regards to age, temperature, wind, level of pollutants, ans measurement time. That is a pretty rich task, because low cost sensors will vary wildly in performance due to mechanical variations. ^c36238543

  - **baq** · [2023-06-08 05:49 UTC](https://news.ycombinator.com/item?id=36237739)
    Generalized, this is unsurprisingly a field of science: [https://en.m.wikipedia.org/wiki/Metrology](<https://en.m.wikipedia.org/wiki/Metrology>) ^c36237739

- **baby-yoda** · [2023-06-08 01:26 UTC](https://news.ycombinator.com/item?id=36236011)
  Does AirGradient have any options that are connected and powered via PoE? The Awair Omni looks like a great option for what I imagine I'd like to set up but it would be nice to support Air Gradient if possible. ^c36236011

  - **ahaucnx** · [2023-06-08 01:47 UTC](https://news.ycombinator.com/item?id=36236148)
    We currently don't have PoE but since it's open hardware and firmware people can look into adding it themselves. All documentation is open source. ^c36236148

  - **Rebelgecko** · [2023-06-08 07:05 UTC](https://news.ycombinator.com/item?id=36238287)
    One thing that's cool is that Airgradient's designs are super modular. I am on a crusade against micro-USB, so when I made an Airgradient Basic board I just used an ESP board with USB-C instead. If you can get a board with PoE with a similar form factor you might be able to just plop it on. Otherwise you can tweak the PCB and STLs to make it work. ^c36238287

    - **ahaucnx** · [2023-06-08 07:13 UTC](https://news.ycombinator.com/item?id=36238354)
      Fully agree. All our PRO kits have USB C and we also now use the D1 mini with USB C plug. ^c36238354

  - **veemjeem** · [2023-06-08 15:48 UTC](https://news.ycombinator.com/item?id=36243913)
    The AirGradient uses the D1 wemos as the microcontroller & network connectivity.  There are D1 ethernet shields that have PoE that would make it pretty easy to slap on top of the d1 and provide this exact feature, however you might need to tweak the code a bit to switch the network access from wifi to ethernet. ^c36243913

- **amatecha** · [2023-06-08 04:10 UTC](https://news.ycombinator.com/item?id=36237078)
  My three AirGradient DIY units are going strong.  They seem very accurate -- strongly correlating with nearby weather stations and online services.  Definitely nice to have high-granularity/accuracy details both indoors and outdoors.  It's also really interesting to see different "trends" and how different weather conditions correlate with (and/or affect) air quality! ^c36237078

  - **2rsf** · [2023-06-08 07:43 UTC](https://news.ycombinator.com/item?id=36238538)
    Are there online co2 measurements from weather stations? I couldn't find any for Sweden ^c36238538

    - **amatecha** · [2023-06-09 22:32 UTC](https://news.ycombinator.com/item?id=36265184)
      Oh, not that I know of.  I was more comparing against nearby stations in terms of temperature. Yeah, I couldn't find any CO2 either.  I just check on aprs.fi to see nearby stations reporting their data via the APRS-IS network :) ^c36265184

- **GuB-42** · [2023-06-09 17:26 UTC](https://news.ycombinator.com/item?id=36261051)
  Don't go too low either. ^c36261051

  There are CO2 sensors on AliExpress for less than \$10, they are scams. What they do is that they take the cheapest sensor available that reacts to something in the air, and extrapolate a reading. It may give you an indication that the air is "stuffy", but the numbers are completely made up.

- **mdp2021** · [2023-06-08 08:09 UTC](https://news.ycombinator.com/item?id=36238712)
  Slightly parallel: does anybody know if there exist products to detect more "local" pollution? Like an electronic nose that would be able to detect "sources", e.g. of mould or chemicals (for disinfection or fixing). I.e. not just the "room air quality", but spots causing it. ^c36238712

  (It is for a bit of an urgency that emerged in a building.)

  - **dementik** · [2023-06-08 10:31 UTC](https://news.ycombinator.com/item?id=36239655)
    Afaik there are no simple sensors for this but havong gone through probably similar situation here, few things what I have learned:
    \- voc sensor can detect lots of stuff, but reports just total value, still, voc sensor can be good way to detect if there is something wrong
    \- our local laboratories have test sets which can be ordered home. Those cost something like 200eur, are placed e.g. on the table for an hour and those collect air. Then the unit is sent to laboratory which will report total voc (good to get a clue how right your own sensor is) and also detailed info on chemicals. For moulds there are different test sets
    \- if some material is suspected to emit something, they can also identify material tvoc and detailed chemicals (so if there is some "bad" chemical on air sample, this is usually to confirm the source) ^c36239655

  - **unknown** · [2023-06-08 17:36 UTC](https://news.ycombinator.com/item?id=36245620)
    [deleted] ^c36245620

- **varjag** · [2023-06-08 08:16 UTC](https://news.ycombinator.com/item?id=36238765)
  Lots of consumer things are basically layers of fancy molded plastic, marketing and some UI/convenience electronics above the same technology. For instance microphones. ^c36238765

- **chaxor** · [2023-06-08 14:43 UTC](https://news.ycombinator.com/item?id=36242679)
  This is probably a stupid question regarding the equipment, but it seems to be a good addition for the user, even if additional hardware underneath is required - why is CO not more common on these devices? ^c36242679

  Additionally, where are all the ppbv CO detection capabilities? (most are ppm, likely to not be a scare to humans but always reading "0", but it makes determining sensitivity or any response at all pretty difficult)

  - **StrictDabbler** · [2023-06-08 14:51 UTC](https://news.ycombinator.com/item?id=36242833)
    CO detectors are life-safety equipment. The regulatory burden for laboratory certification and approval is much higher for them. ^c36242833

    If you put an air-quality detector into your device and it's reading 30\% lower than reality it's no big deal.

    If you put a CO detector into your device and it's reading 30\% lower than reality you may face massive liabilities.

    It isn't a "hey, why not" feature.

- **thenickdude** · [2023-06-08 10:15 UTC](https://news.ycombinator.com/item?id=36239538)
  Has anybody found an accessible solution for sensing PM0.1 (nanoparticles)? ^c36239538

  As far as I know the state of the art on these is condensation particle counters, which use a supersaturated gas (e.g. of isopropyl alcohol or butanol) to glom onto the tiny particles to make them big enough to be sensed optically.

  Are there any novel approaches, or maybe a cheaper CPC?

- **Havoc** · [2023-06-08 07:48 UTC](https://news.ycombinator.com/item?id=36238557)
  To a point. Eg I bought both a bme680 and scd41. ^c36238557

  Ie one co2 equivalent and one real one. The difference is sizable. Equivalent is basically garbage data. Correlates a bit with say opening a window but that’s about it

  Esp in absolute values. The trend seems vaguely ok

- **vbezhenar** · [2023-06-08 07:00 UTC](https://news.ycombinator.com/item?id=36238250)
  I recently bought one air quality monitor (levenghuk wezzer something). Generally it works, but after few dozens of minutes its temperature sensor starts to display like +5 degrees compared to proper temperature. Very weird. ^c36238250

  - **Leo\_Germond** · [2023-06-08 07:33 UTC](https://news.ycombinator.com/item?id=36238477)
    Membrane sensors have to get very high in temp locally in order to do a membrane cleanup, thos being large compared to a temp probe, the probe is probably catching of the heat because it is not properly isolated. Some SW model for heat flux can somewhat reduce this effect but in general this is AFAIK an open problem for miniaturized AQ sensors. ^c36238477

  - **Wolfenstein98k** · [2023-06-08 07:37 UTC](https://news.ycombinator.com/item?id=36238493)
    I think it's because the unit heats up over time, and its sensor can't adequately adjust for that. ^c36238493

    My baby monitor does the same thing - the temperature tracks up after a half hour or so. The unit is warm to the touch by that point.

- **cinntaile** · [2023-06-08 07:05 UTC](https://news.ycombinator.com/item?id=36238285)
  Has anyone opened up their [https://www.birdie.design/](<https://www.birdie.design/>) and checked what sensor they use? They don't disclose it. ^c36238285

  - **supermatt** · [2023-06-08 10:42 UTC](https://news.ycombinator.com/item?id=36239731)
    Not sure, but its just CO2 - not PM. ^c36239731

- **alexk307** · [2023-06-08 14:18 UTC](https://news.ycombinator.com/item?id=36242279)
  I wired up an SDS011 to an ESP8266 running esphome, and then integrated that to home assistant. All in all under \$40 USD, and I’ve found it very sensitive and reliable ^c36242279

- **noja** · [2023-06-08 09:25 UTC](https://news.ycombinator.com/item?id=36239223)
  Well maybe not, but I was \_very\_ happy with Qing Ping Lite until its firmware update bricked it. I've never had an Eve device brick itself. ^c36239223

- **ruph123** · [2023-06-08 05:01 UTC](https://news.ycombinator.com/item?id=36237421)
  I would not recommend the Airgradient diy kit to anyone. Have been using one for a while but the CO2 sensor is really unreliable and often spits out wrong values. VERY OFTEN. Last time this issue was wildly discussed by people using it e.g. in the link below which is using Prometheus but also in the forums of airgradient. All with no solution. ^c36237421

  [https://github.com/geerlingguy/airgradient-prometheus/issues...](<https://github.com/geerlingguy/airgradient-prometheus/issues/24>)

  - **ahaucnx** · [2023-06-08 05:09 UTC](https://news.ycombinator.com/item?id=36237491)
    This was an issue we had in one of the previous versions of the kit. Since then we have improved the hardware (now at version 4.2) as well as fixed it in the firmware. ^c36237491

    If you still have issues, please contact me through the link on my profile.

    - **\_zoltan\_** · [2023-06-08 05:30 UTC](https://news.ycombinator.com/item?id=36237619)
      the above linked GitHub issue is still open. ^c36237619

      - **rgovostes** · [2023-06-08 05:51 UTC](https://news.ycombinator.com/item?id=36237752)
        The above linked GitHub issue has been closed for over 6 months, and aside from that was posted to the wrong project rather than to an official AirGradient channel. ^c36237752

        - **ahaucnx** · [2023-06-08 05:59 UTC](https://news.ycombinator.com/item?id=36237801)
          This has been analysed extensively on our forum and the root cause was a bug in the software serial Arduino library as well as a slightly wrong command send from our library. Details \[1\] ^c36237801

          \[1\] [https://forum.airgradient.com/t/co2-reading-of-3-constantly/...](<https://forum.airgradient.com/t/co2-reading-of-3-constantly/605/6>)

          - **mtlmtlmtlmtl** · [2023-06-08 09:24 UTC](https://news.ycombinator.com/item?id=36239218)
            Arduino library eh? Would definitely recommend getting away from that as soon as possible. When I worked with avr controllers we eventually ended up writing all of our own library code because it was still faster than trying to debug these strange heisenbugs caused by gnarly bugs in the libraries. ^c36239218

            I specifically remember softserial was very problematic, and actually reading the code convinced me to dump it. Might be fixed now, but there's timing code in there that could easily break on a compiler update because it's still written in C++ and has handcounted delays based on counting instructions in compiler output. Now, maybe they recheck those on every single release of avr-gcc to make sure the count didn't change, but why rely on that? We're talking about the same maintainers here who kept conditionally compiled ASM code to manually push and pop the stack in every function because some absolutely ancient MacOS 9(or something like that) version of GCC somehow didn't emit those instructions. That was still there in 2015, hopefully they removed it since then...

            It also sets interrupts. I don't like library code doing this at all. I wanted complete control over that so I always *know* what interrupts might occur. And even worse it uses a circular buffer for storing data but IIRC offers no method of detecting a full buffer. Which led to a lot of "fun" debugging.

            Arduino libraries are fine for simple prototyping, but they're not high quality enough for writing reliable microcontroller code.

            - **rgovostes** · [2023-06-12 02:22 UTC](https://news.ycombinator.com/item?id=36287751)
              Is there a library that you do recommend using for serial comms? ^c36287751

  - **CommanderData** · [2023-06-08 05:56 UTC](https://news.ycombinator.com/item?id=36237789)
    I purchased a soldered unit and the CO2 monitor seems defective and I can't trust the readings. ^c36237789

    Sometimes it reports 0 if left on for extended periods, other times the readings are wildly out of range of what the module is listed to support. I have emailed them regarding a different issue and didn't have the best response back and hasn't inspired confidence to raise this one.

    On the plus side the module is replaceable and I'll probably just source it myself rather go through support.

    - **FPGAhacker** · [2023-06-08 07:05 UTC](https://news.ycombinator.com/item?id=36238290)
      Maybe you are having this issue. [https://forum.airgradient.com/t/co2-reading-of-3-constantly/...](<https://forum.airgradient.com/t/co2-reading-of-3-constantly/605/6>) ^c36238290

- **FloatArtifact** · [2023-06-09 04:59 UTC](https://news.ycombinator.com/item?id=36253401)
  Why do you no longer sell the Pro PCB/ enclosure kit? In fact selling Pro PCB would make the project much more accessible. ^c36253401

- **idontwantthis** · [2023-06-08 06:02 UTC](https://news.ycombinator.com/item?id=36237819)
  Reminds me of dash cams which almost all use the same image sensor even if they advertise different levels of image quality. ^c36237819

  - **2rsf** · [2023-06-08 08:24 UTC](https://news.ycombinator.com/item?id=36238816)
    That's actually a good example- in addition to the sensor a camera needs a lens, a body to hold everything together aligned and steady, power supply and some logic to control the device. ^c36238816

- **Khaine** · [2023-06-08 06:56 UTC](https://news.ycombinator.com/item?id=36238226)
  So how does the Awair air monitoring compare? ^c36238226

- **Snuupy** · [2023-06-08 11:22 UTC](https://news.ycombinator.com/item?id=36240043)
  Can you buy only the PCB of the AirGradient Pro (and not the entire kit)? ^c36240043

  - **ahaucnx** · [2023-06-08 11:36 UTC](https://news.ycombinator.com/item?id=36240179)
    Yes possibly. Please send us a message through our support form. ^c36240179

- **nabla9** · [2023-06-08 07:16 UTC](https://news.ycombinator.com/item?id=36238375)
  If you want more accuracy, buy 2-3 different cheap air quality monitors and average. ^c36238375

- **Avlin67** · [2023-06-08 09:12 UTC](https://news.ycombinator.com/item?id=36239143)
  just open the windows the more you can ^c36239143

- **spoonjim** · [2023-06-08 02:46 UTC](https://news.ycombinator.com/item?id=36236545)
  They probably all use the same Taiwanese component ^c36236545

- **fuzzehchat** · [2023-06-08 09:41 UTC](https://news.ycombinator.com/item?id=36239323)
  This is plainly not true at all. ^c36239323

  Cheap sensors aren't as good as expensive ones.

  This is like saying a DHT11 has the same accuracy as a SHT31.

  - **AlfeG** · [2023-06-08 09:57 UTC](https://news.ycombinator.com/item?id=36239407)
    But they don't compare sensor modules, they compare consumer devices ^c36239407

- **sacnoradhq** · [2023-06-08 04:14 UTC](https://news.ycombinator.com/item?id=36237108)
  PMS9003M is \$15 shipped, add another \$6 for an Arduino and a display. ^c36237108

  You can bet the \$1000 ones are Better Technology Through Beautiful Marketing and Design(tm). Anyone who pays that deserves to be separated from their money.

  - **ARandomerDude** · [2023-06-08 04:21 UTC](https://news.ycombinator.com/item?id=36237153)
    \> Anyone who pays that deserves to be separated from their money. ^c36237153

    This a sad statement and simply untrue.  The vast majority of people are in other fields, don’t know anything about hardware, and have never even heard the word “Arduino.”

    They don’t deserve to be scammed by con artists using fancy packaging as the hook.

    - **sacnoradhq** · [2023-06-08 20:55 UTC](https://news.ycombinator.com/item?id=36248869)
      Ignorance isn't something to be defended, celebrated, or excused. Find hypothetical victims elsewhere because you're preaching against the ethos of this community. ^c36248869

