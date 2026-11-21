# [Indoor air quality and learning: Evidence from large field study in schools \[pdf\]](https://news.ycombinator.com/item?id=34570007)

Article: [https://papers.ssrn.com/sol3/papers.cfm?abstract\_id\=4296077](<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4296077>)

elsewhen · 2023-01-29 16:57 UTC · 62 reported comments · archived 2026-11-08 12:36 UTC
Observation: 2026-11-08 12:36 UTC → 2026-11-08 12:36 UTC

## Comments

- **simonsarris** · [2023-01-29 17:07 UTC](https://news.ycombinator.com/item?id=34570125)
  These seem like crazy differences. Some classrooms have over 6x the CO2 concentration than others. Some classrooms have \> 2000ppm every day. ^c34570125


  ```
      Panel A: Classroom Ventilation              Mean St. Dev. Min. Max.
      Daily Peak of CO2 (in ppm)                  1495 624      737  4665
      Daily Average CO2 (in ppm)                  988  336      485  2783
      % of days w CO2 in classroom > 1000 ppm     77   29       0    100
      % of days w CO2 in classroom > 2000 ppm     15   26       0    100
  ```

  
  Note they claim there's no relationship observed between teacher quality and classroom ventilation

  Their conclusion: "An increase in classroom CO2 level during the school term by one standard deviation reduces subsequent test scores by 0.11 standard deviations. Our findings imply that exposure to poor indoor air quality directly interferes with learning, highlighting the role of physical school infrastructure in determining educational outcomes."

  - **dahart** · [2023-01-29 17:42 UTC](https://news.ycombinator.com/item?id=34570511)
    \> These seem like crazy differences. Some classrooms have over 6x the CO2 concentration that others. ^c34570511

    6x seems plausible just because some classrooms are more crowded than others, and kids are probably breathing harder at the start of class, during first class, during first class after lunch or breaks or P.E…

    “The variation in CO2 levels inside classrooms that we observe in our sample is almost fully caused by indoor sources, i.e. human breathing, with negligible variation from outdoor levels.”

    I wonder if peak rates could be easily misinterpreted? This chart doesn’t say how long peaks last or when they happen. Did they verify that a single sensor is a good proxy for distribution of CO2 in the room? It depends on where the sensor is located, for example. Near the door will see higher peaks as people come in and out than in the far corner, and air might flow toward the door. Looking at the average tells a more meaningful story, but even that may need more context, right?

  - **antisthenes** · [2023-01-29 17:40 UTC](https://news.ycombinator.com/item?id=34570486)
    \> Some classrooms have over 6x the CO2 concentration than others. Some classrooms have \> 2000ppm every day. ^c34570486

    That's basically the difference between having an open window or not. If your ventilation system is designed to get fresh air from the outside, you'll have \<600 PPM, if not, you'll have 2000+

    How do I know? I bought a CO2 meter and worked in an old office building that didn't get fresh air from the outside.

    - **dzhiurgis** · [2023-01-30 09:07 UTC](https://news.ycombinator.com/item?id=34577461)
      My dad has a shoddy heat recovery ventilation system which he throttled down to a minimum. I bought co2 meter and turns out it barely does anything, but he won’t believe me. ^c34577461

      - **stuaxo** · [2023-01-30 09:30 UTC](https://news.ycombinator.com/item?id=34577603)
        Sounds counter productive turning it to a minimum ? ^c34577603

        (I guess it could be shoddy in many other ways too!).

        - **dzhiurgis** · [2023-01-30 10:47 UTC](https://news.ycombinator.com/item?id=34578111)
          Over 60\% it becomes quite audible, at 100\% it can be annoying. ^c34578111

          It’s a ducted balanced system. If we have 4-5 adults in living room - it doesn’t keep up even at 100\%. Ir I keep most doors open at night - it’s okay.

          Air quality is always good there, it’s mostly to manage humidity and it does it too well once it’s freezing outside.

  - **nomorewords** · [2023-01-29 19:28 UTC](https://news.ycombinator.com/item?id=34571738)
    I'm not American, but when we were in up to the 9th grade, every break between classes we would play football (soccer) outside. Almost the whole class (our schools aren't like american HS where you go to a class with different people every period, we are like a "unit" and we do all our classes always together) would play football (soccer) every period. Most of the boys from other classes didn't do this. We always went sweaty into class, and I guess we breathed a lot at the beginning of every class. ^c34571738

  - **culi** · [2023-01-29 17:24 UTC](https://news.ycombinator.com/item?id=34570328)
    Agreed that's a huge Std Dev. I'm surprised they were able to achieve statistical significance with just 216 classrooms, but I guess the results are quite consistent: ^c34570328

    \> The coefficient shows high stability in terms of its magnitude, sign, and statistical significance.

  - **stuaxo** · [2023-01-30 09:28 UTC](https://news.ycombinator.com/item?id=34577591)
    This tracks, I bought an Aranet 4 and just testing at home. ^c34577591

    With myself and one other person WFH it's easy to find r the room to go from 600 to 1800ppm if the door or window isn't open.

- **graeme** · [2023-01-29 17:58 UTC](https://news.ycombinator.com/item?id=34570713)
  Tangentially related: management of these issues would be greatly improved by funding CO2 and AQI meters in relevant spaces ^c34570713

  Right now people’s attitude to indoor air quality is roughly: can’t see it, isn’t real

  But if you’re told:

  \* Under 1,000 is good
  \* This room is 2,200 ppm

  Many people would start asking why the air quality wasn’t good.

  Ventilation systems work, I’ve measured CO2 in an incredible crowded airport and found under 800 ppm. But without such monitoring there’s no visibility into which spaces are and aren’t ventilated

  - **nannal** · [2023-01-30 00:09 UTC](https://news.ycombinator.com/item?id=34574210)
    I recently bought a PMSA003 sensor and started logging the results indoors in a capital city. Three big discoveries were that opening the windows made the air quality way worse, sometimes the air quality is bad indoors and out without any clear coloration with other weather events and finally deodorant is absolutely awful. ^c34574210

    We're about to start messing around with filters, I built a home brew one with a duct fan and an inline activated carbon filter, but we've bought a retail filter that will be here soon so that will be interesting.

    I do think more people should be aware of their air quality.

    - **jackvalentine** · [2023-01-30 04:11 UTC](https://news.ycombinator.com/item?id=34575690)
      I bought an air purifier a few years ago and if you use spray type deodorant in the same room as it the thing kicks in to hyper mode for a while. ^c34575690

      We’ve taken to saying ‘you made it angry’.

      Even farting directly in to it doesn’t make it do that.

      - **nannal** · [2023-01-30 22:02 UTC](https://news.ycombinator.com/item?id=34587080)
        Yeah, either I move to roll on or the world learns to live with my musk. ^c34587080

    - **graeme** · [2023-01-30 04:36 UTC](https://news.ycombinator.com/item?id=34575812)
      Yeah if you live in a place with pollution outdoors and no indoor HVAC there is a real severe trade off between co2 and aqi ^c34575812

      If a place is sub say 70-100 in AQI then usually indoors will be 4-13 AQI with windows open but above that you’ll see indoor increases with open windows.

      - **dzhiurgis** · [2023-01-30 09:11 UTC](https://news.ycombinator.com/item?id=34577486)
        Cold climates also suck for co2. There are very cheap hrv’s but I think they are noisy. ^c34577486

        - **graeme** · [2023-01-30 21:51 UTC](https://news.ycombinator.com/item?id=34586952)
          That one’s actually easier. Air circulates much better when there is a temperature difference. ^c34586952

          A single window opened a crack will generally ventilate most homes or apartments.

          There will be somewhat higher heating costs but usually not excessive. Less than a lot of non-essential things people already spend money on

          - **graeme** · [2023-01-31 01:18 UTC](https://news.ycombinator.com/item?id=34589492)
            To manage high AQI and high CO2 and you need the windows open enough to ventilate and enough hepa to lower the AQI pollutants that comes in ^c34589492

- **ahaucnx** · [2023-01-29 19:29 UTC](https://news.ycombinator.com/item?id=34571749)
  At AirGradient we are specialized in measuring indoor air quality in schools and monitor thousands of classrooms in real-time for CO2, PM2.5, temperature, humidity and TVOCs. ^c34571749

  We do see very similar CO2 ranges in our data as presented in this study and observe the best results in modern schools buildings with demand constrolled ventilation linked to specific indoor air quality targets \[1\].

  The schools that we monitor that have the best indoor air quality often use positive pressure systems with high performance HEPA and carbon filters \[2\].

  We encourage schools to be transparent about their data and share it with the community as this encourages discussion and lays the base for continous improvements.

  Some schools now publish real-time data on air quality on their website together with an explanation why healthy indoor air quality is so important for students. Here is a good example of a well done air quality webpage of a school with real-time data \[3\].

  If you want to know more about the air you breath and build your own monitor - either yourself or with students- we maintain a popular open source air quality monitor project \[4\].

  \[1\] [https://www.airgradient.com/open-airgradient/blog/we-measure...](<https://www.airgradient.com/open-airgradient/blog/we-measured-the-co2-level-in-a-classrooms-this-is-what-we-found-out/>)

  \[2\] [https://www.airgradient.com/open-airgradient/blog/air-purifi...](<https://www.airgradient.com/open-airgradient/blog/air-purifier-vs-positive-pressure-fresh-air-system-an-unfair-battle/>)

  \[3\] [https://ptis.ac.th/aqi-at-prem/](<https://ptis.ac.th/aqi-at-prem/>)

  \[4\] [https://www.airgradient.com/open-airgradient/kits/](<https://www.airgradient.com/open-airgradient/kits/>)

  - **amluto** · [2023-01-29 19:53 UTC](https://news.ycombinator.com/item?id=34571992)
    Where were you that infiltration increased PM2.5 to over 50 ug/m3 in two hours?  That seems rather extreme. ^c34571992

    I’m also interested in what PPS this was. The link for more information is broken:

    [https://www.airgradient.com/blog/2020/01/08/positive-pressur...](<https://www.airgradient.com/blog/2020/01/08/positive-pressure-systems-for-clean-air/>)

    - **ahaucnx** · [2023-01-29 20:49 UTC](https://news.ycombinator.com/item?id=34572599)
      We are based in Nortern Thailand. In March / April every year the air quality is very poor, often beyond 100 ug/m3.
      I will check the link. ^c34572599

      - **ahaucnx** · [2023-01-29 20:52 UTC](https://news.ycombinator.com/item?id=34572617)
        Here is the working link: [https://www.airgradient.com/open-airgradient/blog/positive-p...](<https://www.airgradient.com/open-airgradient/blog/positive-pressure-systems-for-clean-air/>) ^c34572617

  - **Siecje** · [2023-01-29 19:37 UTC](https://news.ycombinator.com/item?id=34571840)
    Do you have plans to measure radon? ^c34571840

    - **ahaucnx** · [2023-01-29 19:44 UTC](https://news.ycombinator.com/item?id=34571907)
      Yes but so far we did not find suitable radon sensor modules available in the market that we could easily integrate into our monitor. ^c34571907

- **ck2** · [2023-01-29 18:03 UTC](https://news.ycombinator.com/item?id=34570789)
  Someday every smartphone is going to have an on-chip air quality meter and it will instantly become something people learn to monitor, it will change everything. ^c34570789

  Just imagine all the social media posts from every location.

  The problem is quality, apparently all consumer air quality chips are very poor and inconsistent.

  Some neat DIY hacks have appeared on HN though

  [https://news.ycombinator.com/item?id\=33025995](<https://news.ycombinator.com/item?id=33025995>)

  [https://news.ycombinator.com/item?id\=27124671](<https://news.ycombinator.com/item?id=27124671>)

  [https://news.ycombinator.com/item?id\=28457135](<https://news.ycombinator.com/item?id=28457135>)

  - **dzhiurgis** · [2023-01-30 09:52 UTC](https://news.ycombinator.com/item?id=34577759)
    Smart speakers and laptops especially - you already have a fan running all the time! ^c34577759

  - **a1371** · [2023-01-29 18:53 UTC](https://news.ycombinator.com/item?id=34571342)
    Interesting vision ^c34571342

- **nwah1** · [2023-01-29 17:20 UTC](https://news.ycombinator.com/item?id=34570278)
  We are willing to spend endless trillions on administrators, elaborate facilities, tablet computers, tutoring, lowering student-teacher ratios... ^c34570278

  But not willing to spend any time or money figuring out how to provide kids with fresh air, nutritious food, sunlight, and adequate sleep.

  It almost seems like the lack of need to spend a lot of money on these effective interventions is precisely why they are given no attention.

  Advocates should pitch people on overpriced solutions to these.

  - **simonsarris** · [2023-01-29 17:40 UTC](https://news.ycombinator.com/item?id=34570487)
    \> figuring out how to provide kids with fresh air, nutritious food, sunlight, and adequate sleep ^c34570487

    Most of these are already *known,* which is the more frustrating thing. The 1001st paper on teenage sleep isn't going to suddenly make schools change their tune. They simply do not care. In the US it is illegal to offer whole milk in elementary school because the USDA says so because of completely insane rules from the 1980's when nutrition science was at its worst.

    The only way you can really fight these forces is by exiting (homeschooling, private schooling).

    - **azemetre** · [2023-01-29 18:49 UTC](https://news.ycombinator.com/item?id=34571300)
      No, the only way you can truly fight these issues is running for local office, getting on school boards, townships, and development boards and actually pushing for this. ^c34571300

      Just giving up and doing your own thing is a complete antithesis to democracy and modern society.

      You act like these institutions are set in stone when it doesn't make much force to enact local change at all. We're talking about positions of power that get decided in an election of maybe 300-600 voters.

      - **zamfi** · [2023-01-29 18:56 UTC](https://news.ycombinator.com/item?id=34571371)
        No, the only way you can truly fight these issues is by convincing *parents* not only that these issues matter, but that the conventional thinking is wrong. You won't be able to do that from a school or township board. ^c34571371

        Get on a school board, try to push for whole milk in schools, and you'll see how quickly ill-informed parents and vested interests fight back.

        School starts early because most adults work, and their kids can't leave home after they do.

        It's easy to think that each of these issues continues to be an issue because someone "doesn't care", but the reality in many cases is the much more challenging "someone cares a lot, but *has the opposite opinion*."

        - **azemetre** · [2023-01-29 19:10 UTC](https://news.ycombinator.com/item?id=34571543)
          There's always challenges for everything in life, and wanting to give up at the slightest bit of hardship is so odd. ^c34571543

          I've done zero research on this, but I have to assume societal movements have a much much shorter shelf life since the advent of modern social media.

          But hey it's okay, by not caring about these local institutions or political races just means people that don't agree with do care and are actively showing up and making changes.

          - **zamfi** · [2023-01-31 13:25 UTC](https://news.ycombinator.com/item?id=34594724)
            O...kay? No one's saying to "give up" here -- I'm just saying a local leadership post is not typically the position of influence you're implying: an elected representative who is consistently pushing an agenda that's unsupported by constituents isn't going to last very long, and is certainly not going to change many minds. Frankly you'd have better luck as an "influencer"... ^c34594724

      - **giantg2** · [2023-01-29 19:04 UTC](https://news.ycombinator.com/item?id=34571483)
        Just an FYI, this wouldn't work for their example of USDA regulations. Some states have laws about start times, or maybe it was just recently proposed. ^c34571483

        There is a massive amount of state and federal regulation on most school issues. There's still a lot that can be done at the local level, but there's not as much autonomy as most people initially think.

    - **giantg2** · [2023-01-29 18:29 UTC](https://news.ycombinator.com/item?id=34571077)
      Just because we know certain things, doesn't mean we know how to apply those things to maximum benefit. ^c34571077

      Yes, starting school after 9am could be better for *some* kids. It could be worse for *some* others. Then the main issue is that the majority of adults are at work prior to 8am, making schools essentially babysitters. We'd have to change a lot about society to really make later start times work well for everyone. I haven't really seen good solutions in practice so far since the solutions are usually one size for all, or ignore the effects of socital factors.

      Perhaps the common issue at the center of most school complaints is that it's essentially authoritarian imposition of what *someone* thinks is best for the child. Whether that's low fat milk and cardboard "whole wheat", or whitelisting approved snacks (down to the brand) for personal snacks, or when to start classes, or what speech and images are allowed.

    - **apocalypstyx** · [2023-01-29 17:58 UTC](https://news.ycombinator.com/item?id=34570727)
      As a former home-schooled child, don't do this. ^c34570727

      - **mleonhard** · [2023-01-29 19:00 UTC](https://news.ycombinator.com/item?id=34571439)
        Second.  I was homeschooled K-12 and missed a lot of opportunities to learn social skills.  Learning these skills later in life is very very very hard.  Now, I would pay a lot of money for live role-playing classes to help me develop the missing mental habits, but I have not found such classes offered anywhere. ^c34571439

        - **omginternets** · [2023-01-29 20:04 UTC](https://news.ycombinator.com/item?id=34572103)
          Do you have examples that might illustrate what it means, concretely, to have missed opportunities to learn social skills?  I understand why and how it can happen, but it's all a bit abstract.  I have a hard time imagining a concrete situation in which that handicap would manifest. ^c34572103

      - **nosecreek** · [2023-01-29 19:15 UTC](https://news.ycombinator.com/item?id=34571594)
        Also a former home-schooled child, and I say go ahead and do it. Like any other kind of schooling, homeschooling does have some downsides, so be aware of them and do your best to mitigate those things (i.e. be very intentional about finding other avenues for your kids to socialize like clubs, sports, etc.) ^c34571594

      - **omginternets** · [2023-01-29 18:37 UTC](https://news.ycombinator.com/item?id=34571170)
        Could you elaborate? ^c34571170

        - **apocalypstyx** · [2023-01-29 19:56 UTC](https://news.ycombinator.com/item?id=34572015)
          Most people are not going to have the requisite knowledge of pedagogy.
          We think we know X, Y, Z, or we actually know X, Y, Z, but teaching that (especially to children) is a whole other ballgame. ^c34572015

          When your parents are your teachers, the disappointment quotient to your failure isn't double but a power of 2 because, whether they know it or not, their ego is on the line twice over as both teacher and parent.

          They tend to start telling you or others that 'you're so mature for your age', where you are expected to be adult in mentality but without the actual ability to act upon that mentality (that is, they want to reference how 'adult' you are --- because of their parenting/education style --- and by definition of being underage, you have no autonomy.  So have all the expectations of being or interacting like an adult without any of the autonomy, so you end up in your 20s feeling closer to 40 --- most especially if there is a lack of socialization with children your own age, and you the vast majority of the first two decades of your life around people your parents' or grandparents' age. So when you're in college, you feel alien from everyone who is your own age.)

          All of this goes double if the reasons for homeschooling are religious fundamentalism, or add a disbelief in autism or ADHD into the mix.

          My experience is that the vast majority of people who homeschool their kids don't do so because the education system is 'failing' but because of control --- my kid isn't going to be infected by evolution, etc (and transness nowadays).

          This is, of course, not all homeschools, but it remains by far the majority of what I have seen in person and online.

          Also there is a sense of illegitimacy.
          When your high-school diploma is just a sheet signed by your father stuck in a folder that you have to send out when official transcripts are required, it's a constant worry of if these records are going to be accepted or not, or that this school has no XYZ ID number because there was never any such thing back then, etc.
          All of the educational records that would you would normally request to be transferred between institutions, you have to manage.

          - **apocalypstyx** · [2023-01-29 20:43 UTC](https://news.ycombinator.com/item?id=34572521)
            While I'm on this (literally just saw this). ^c34572521

            *Inside a US Neo-Nazi Homeschool Network With Thousands of Members*

            [https://www.vice.com/en/article/z34ane/neo-nazi-homeschool-o...](<https://www.vice.com/en/article/z34ane/neo-nazi-homeschool-ohio>)

        - **unknown** · [2023-01-29 18:53 UTC](https://news.ycombinator.com/item?id=34571346)
          [deleted] ^c34571346

      - **seany** · [2023-01-30 06:39 UTC](https://news.ycombinator.com/item?id=34576537)
        as a former home-schooled kid. It might be the only reasonable option. ^c34576537

    - **saiya-jin** · [2023-01-29 19:24 UTC](https://news.ycombinator.com/item?id=34571706)
      Walling yourself from societal problems generally is not a long term solution in any way, neither for you/your kids nor for society. You harm your kids in myriad other ways, while you keep pounding your chest how great parent you are. ^c34571706

      So you are not fighting anything, you just gave up. Great example for kiddos. Look at society with similar approach to even greater issues - South Africa. Everybody rich walled away from everybody else, moving around only in cars, praying not that they aren't robbed as much as not catching thieves at their houses. No personal freedom at all, a sad place.

    - **robocat** · [2023-01-29 20:11 UTC](https://news.ycombinator.com/item?id=34572183)
      \> exiting (homeschooling ^c34572183

      I imagine that there is a bimodal distribution of ability in parents because of the different reasons parents choose to homeschool. Blanket advice also captures unwise parents who nurture badly, and lack the wisdom to understand the negative parts of the compromises.

  - **abadger9** · [2023-01-29 17:50 UTC](https://news.ycombinator.com/item?id=34570615)
    There was a phrase in the recent Netflix show "Recruit" - everything in America tastes like sugar and everyone's struggling. Having lived in Finland, SE Asia, and Calfornia it's completely true. We mask our real issues and replace them with processed foods, drugs, and entertainment. I hope as a society we wake up to our coping mechanisms and lift up our communities, I can teach good values to my kids as my parents taught me but it'll get lost eventually. ^c34570615

  - **jeffbee** · [2023-01-29 17:42 UTC](https://news.ycombinator.com/item?id=34570522)
    Well, my kids go to a school where sunlight and nutritious food are revered ... there is a kitchen garden managed by Alice Waters and half the rooms have so much sunlight that they can't be cooled to a reasonable temperature even in the winter. But the big problem is I also live in one of those frozen-in-amber American cities that hasn't built a new building since Eisenhower. The school I mentioned was built in 1920 and has no good ventilation, and the local attitude is so opposed to modernization and replacement that there are not any prospects for having well-ventilated schools at any point in the foreseeable future. ^c34570522

    I am actually quite jealous of the schools studied in the paper with an average building age of 29 years. In my city you'd need to walk pretty far to find a building less than 30 years old. The vast majority of existing buildings in America need to be replaced in the next 50 years on efficiency grounds, and now with what we learned from the pandemic we also know that most buildings are underventilated, and we've learned a lot about noise impacts on health, too. But we are stuck with this attitude that old buildings are somehow good. I don't understand it.

  - **danhon** · [2023-01-29 18:14 UTC](https://news.ycombinator.com/item?id=34570912)
    Oh, we have figured out that we should provide kids with nutritious food. It's also that many, or enough, people believe that not every kid deserves nutritious food, and that if they don't have it, they're to be punished for the actions or lack thereof of their parents -- even if it isn't the parents' fault. ^c34570912

    - **giantg2** · [2023-01-29 18:35 UTC](https://news.ycombinator.com/item?id=34571145)
      Are we talking about the same thing here? ^c34571145

      A lot of the complaints about the stuff like the whole milk mentioned is that someone has set rules about what is nutritious and what is not, or what food is allowed for personal snacks etc.

      The USDA has a free lunch program for disadvantaged kids. They recently did away with the free lunch for everyone program. Even under these programs, it's debatable whether or not the food is really nutritious or even appetizing.

  - **sssilver** · [2023-01-29 18:44 UTC](https://news.ycombinator.com/item?id=34571246)
    Having to wake up every morning at 0645 for my daughters school is wreaking havoc on my family’s health. We will never get used to it. It’s insanely inhuman. ^c34571246

    - **papito** · [2023-01-29 19:20 UTC](https://news.ycombinator.com/item?id=34571657)
      I wake up at 4-5 in the morning to see my wife out the door. She comes home early. We still get our 8 hours of sleep because we start winding down at around 19:00 and are in bed by 20:00-21:00. I live in the U.S. so perhaps you can appreciate me using what we call "military time" ;) ^c34571657

      6:45 sounds like a reasonable time IF you don't try to juice another extra hour at night and go to sleep around 22:00 (10PM). People very often go all they way to midnight and later to squeeze in that one more Netflix show episode, and then they feel like a drunken fly all day the next day. It's not worth it.

      BTW, I had to wake up to go to school at 5:45 every morning, but I did not have that sleep discipline. It's a miracle that Sony alarm clock survived without deadly injuries.

  - **jeff\_carr** · [2023-01-29 17:35 UTC](https://news.ycombinator.com/item?id=34570446)
    [https://www.jamesgmartin.center/2022/11/administrators-have-...](<https://www.jamesgmartin.center/2022/11/administrators-have-seized-the-ivory-tower/>) ^c34570446

  - **culi** · [2023-01-29 17:26 UTC](https://news.ycombinator.com/item?id=34570343)
    I think it's just that we try to be data-driven about what we spend on. Unfortunately the first set of variables you mentioned we already have good data on and can study easily. The latter set of variables can be more complex to measure the impact of and so the science lags behind ^c34570343

- **ummonk** · [2023-01-29 17:33 UTC](https://news.ycombinator.com/item?id=34570420)
  Note also that the spread of infectious diseases is likely also highly correlated with lack of ventilation. ^c34570420

- **FriedPickles** · [2023-01-29 19:25 UTC](https://news.ycombinator.com/item?id=34571717)
  The paper doesn't discuss the physiological mechanism by which poor air quality impairs performance. Perhaps the idea just that a higher ppCO2 impairs CO2 excretion, creating back pressure against all aerobic metabolism. If so this raises some interesting questions: ^c34571717

  Could we achieve "superhuman" performance by breathing CO2 depleted air (below \~420 ppm)? Is the rising atmospheric CO2 level making us all stupider? Should teachers begin class with a breathing exercise?

  - **unknown** · [2023-01-29 22:03 UTC](https://news.ycombinator.com/item?id=34573262)
    [deleted] ^c34573262

- **Spooky23** · [2023-01-29 17:13 UTC](https://news.ycombinator.com/item?id=34570197)
  I’d believe it. In my NYC public school, 4th grade in mid May circa 1988 was like 95 degrees, 90\% humidity and no air movement. It was awful. ^c34570197

- **bluecalm** · [2023-01-29 18:01 UTC](https://news.ycombinator.com/item?id=34570755)
  We still allow smoking in public and cars in cities including poisonous and carcinogenic diesel. No wonder we also don't care what kids breathe at school. It's just a result of convenience being valued higher than health even if the cost of convenience is ridiculous (like carrying a 2 ton metal box powered by a diesel engine everywhere you go in a city). ^c34570755

- **londons\_explore** · [2023-01-29 20:10 UTC](https://news.ycombinator.com/item?id=34572167)
  The usual caveat that this is correlation not causation applies. ^c34572167

  It seems entirely plausible that better teachers get assigned the more modern classrooms with better ventilation, while inexperienced/poor performing teachers end up in the unventilated storeroom converted into a classroom...

  - **londons\_explore** · [2023-01-29 20:13 UTC](https://news.ycombinator.com/item?id=34572206)
    I wonder how much an intervention study would cost? ^c34572206

    Ie. you enrol 200 classes into the study, then select 100 at random and fit a free ventilation system.   Then look at test scores at the end of the year.

    School systems where the same students are assigned to the same room for the whole year would be a perfect fit for this.

    The study could be extended to various different air treatment options - eg. fresh air vs filtered room air.  HEPA filters against particulates and viruses, vs carbon filters for volatile organics.  Maybe even include CO2 scrubbing systems to see if you can get the CO2 levels in the classroom *below* 400ppm.

- **papito** · [2023-01-29 19:24 UTC](https://news.ycombinator.com/item?id=34571697)
  It's not only a problem in schools. I am shocked by how employers and employees do not care about stifled air and poor circulation in offices. I had to literally bring a CO2 meter in to show that the air in the office was not conducive of productivity and clear thinking. ^c34571697

  How many studies do we need that show people's basic thinking abilities starting to suffer as the CO2 ppm goes up? I have that CO2 meter at my home office. If it's above 700ppm, I open the window wider.

  There is a dollar amount attached to air quality, but most people just suffer through it like it's something that HAS to be suffered.

- **unknown** · [2023-01-29 19:38 UTC](https://news.ycombinator.com/item?id=34571845)
  [deleted] ^c34571845

- **anonu** · [2023-01-29 19:15 UTC](https://news.ycombinator.com/item?id=34571599)
  Did they control for demographics of each school? A quick review of the paper seems like no... ^c34571599

  Maybe lower socioeconomic households live in places with poorer air quality?

  - **jeffbee** · [2023-01-29 19:22 UTC](https://news.ycombinator.com/item?id=34571676)
    Perhaps you should "quickly scan" the paper again, since you obviously scanned it too quickly the first time. Their outcome variable correlates test scores to recent CO2 levels repeatedly for the *same person*. ^c34571676

  - **dtech** · [2023-01-29 19:30 UTC](https://news.ycombinator.com/item?id=34571760)
    This is addressed in the *abstract*, it's individual student scores. ^c34571760

