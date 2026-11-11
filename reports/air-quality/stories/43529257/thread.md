# [Installing air filters in classrooms has surprisingly large educational benefits (2020)](https://news.ycombinator.com/item?id=43529257)

Article: [https://www.vox.com/2020/1/8/21051869/indoor-air-pollution-student-achievement](<https://www.vox.com/2020/1/8/21051869/indoor-air-pollution-student-achievement>)

tangjurine · 2025-03-31 00:22 UTC · 142 reported comments · archived 2026-11-08 13:47 UTC
Observation: 2026-11-08 13:46 UTC → 2026-11-08 13:47 UTC

## Comments

- **Aurornis** · [2025-03-31 01:49 UTC](https://news.ycombinator.com/item?id=43529859)
  I'm all for installing air filters in classrooms for a number of reasons, but I also think the extreme results from this study aren't going to hold up to further research. ^c43529859

  From the paper:

  \> To do so, I leverage a unique setting arising from the largest gas leak in United States history, whereby the offending gas company installed air filters in every classroom, office and common area for all schools within five miles of the leak (but not beyond). This variation allows me to compare student achievement in schools receiving air filters relative to those that did not using a spatial regression discontinuity design.

  In other words, the paper looked at test scores at different schools in different areas on different years and assumed that the only change was the air filters. Anyone who has worked with school kids knows that the variations between classes from year to year can be extreme, as can differences produced by different teachers or even school policies.

  Again, I think air filtration is great indoors, but expecting test scores to improve dramatically like this is not realistic. This feels like another extremely exaggerated health claim, like past claims made about fish oil supplements. Fish oil was briefly thought to have extreme positive health benefits from a number of very small studies like this, but as sample sizes became larger and studies became higher quality, most of the beneficial effects disappeared.

  - **AngryData** · [2025-03-31 04:39 UTC](https://news.ycombinator.com/item?id=43531116)
    I would also think there is a bias of schools spending extra money and effort towards student improvements if they are willing to go so far as allocate funding for air filtration systems. A better method would be to just give some schools air filtration for free and see if things help without any other major changes. ^c43531116

    To me its like looking at schools that buy newer buses and trying to show new buses improve test scores. When in practice the only schools that are buying any significant number of new buses have far more money coming in than in the past and have a lot more to spend on students compared to other schools, which is way more relevant than what year a kid's bus is made. Maybe better buses would improve scores too, but there is no way to tell if 95\% of an improvement is due to other unrelated factors based on funding.

    - **Aurornis** · [2025-03-31 04:45 UTC](https://news.ycombinator.com/item?id=43531165)
      \> A better method would be to just give some schools air filtration for free and see if things help without any other major changes. ^c43531165

      This is what the study looked at.

      The problem was that it wasn’t randomized within schools or across teachers. They also looked at a very limited time window. They also note that some teachers weren’t using the air filters. They also found that the VOCs they were trying to filter weren’t even detected before the filters were used. They also used some questionable regressions to imply larger trends.

      The list of problems goes on and on. It’s fascinating how easily people are tricked into pivoting around this one study, though, simply because it’s the one introduced by the headline.

      - **jancsika** · [2025-03-31 06:20 UTC](https://news.ycombinator.com/item?id=43531732)
        \> They also looked at a very limited time window. They also note that some teachers weren’t using the air filters. ^c43531732

        To correct and clarify:

        They also looked at a very limited time window. They also note that*\-- after this very limited time window--* some teachers *stopped* using the air filters. *In the words of the authors, this made long-run results "difficult to interpret."*

  - **stdbrouw** · [2025-03-31 08:38 UTC](https://news.ycombinator.com/item?id=43532636)
    I would also expect the estimated magnitude of the effect to go down over time, but that's just my general attitude to these kinds of things, the fact is that the discontinuity design that they use already accounts for variations between classes, teachers, schools, years. The way it works is that some unexpected event that applies to some people but not others is taken to represent a natural experiment, and then variation between groups before the event is compared to variation between groups after the event. The comparison is never against no variation. ^c43532636

    The smoking gun is really in Table 3 and Table 4, where you can see that the effects that were observed are compatible with a population effect of 0, or alternatively you can look at Figure 2 and note that you could draw a straight line (no effect) within the confidence bands. Doesn't mean the effect is not there, but that there's insufficient evidence that it is, and that we should indeed be very careful about taking the estimates at face value.

  - **mmooss** · [2025-03-31 02:29 UTC](https://news.ycombinator.com/item?id=43530174)
    Based on your comment, the effect could be larger as well as smaller. ^c43530174

    All research is met on HN by people who know better and will tell you why it's flawed. There isn't a greater collection of expertise in the history of the world than on HN.

    Edit: I meant to add: What value can we find in this research? It wasn't published as scripture, the perfect answer to all our problems. It's one study of some interesting events and data; what can we get out of it?

    - **Aurornis** · [2025-03-31 04:28 UTC](https://news.ycombinator.com/item?id=43531037)
      \> Based on your comment, the effect could be larger as well as smaller. ^c43531037

      The reality of any underpowered study could always be “larger as well as smaller”. This statement doesn’t add anything to the conversation.

      The mistake is pivoting around poorly structured and underpowered research.

      \> All research is met on HN by people who know better and will tell you why it's flawed.

      This is a misunderstanding. People who know how to read studies will always be aware of the limitations.

      There’s a difference between saying “everything is flawed” and pointing out the limitations. Most early research comes with significant limitations like small sample sizes or large cofounders. You have to understand these in conjunction with the results to know how to interpret it.

      There’s a cynical approach where people see discussion of limitations, don’t understand it, and instead go into a mode where they think it’s smarter to ignore all criticisms equally because every paper attracts criticisms.

      This is just lazy cynicism, though. There are different degrees of criticisms and you have to be able to see the difference between something like a slightly underpowered study, and something like this paper where the authors threw a lot of regressions at a lot of numbers and kind of sort of claimed to have found a trend.

      - **TheOtherHobbes** · [2025-03-31 10:59 UTC](https://news.ycombinator.com/item?id=43533499)
        In this case, it only takes a few seconds to find multiple studies confirming the effect. ^c43533499

        For example

        [https://onlinelibrary.wiley.com/doi/10.1111/ina.12042](<https://onlinelibrary.wiley.com/doi/10.1111/ina.12042>)

        [https://onlinelibrary.wiley.com/doi/10.1111/j.1600-0668.2010...](<https://onlinelibrary.wiley.com/doi/10.1111/j.1600-0668.2010.00686.x>)

      - **mmooss** · [2025-03-31 04:48 UTC](https://news.ycombinator.com/item?id=43531183)
        [flagged] ^c43531183

        \[flagged\]

        - **bdauvergne** · [2025-03-31 08:19 UTC](https://news.ycombinator.com/item?id=43532514)
          99\% of times it's smaller, saying there is an equal chance it's smaller or bigger is also false. It could be, probability is strong that it won't. ^c43532514

    - **conformist** · [2025-03-31 03:32 UTC](https://news.ycombinator.com/item?id=43530609)
      Conditional on “the study being published and getting attention” the real effect is likely smaller and not larger. ^c43530609

      Eg if you assume there is a real effect plus a lot of noise, given the study has been published etc the noise will have more likely acted in the favourable direction.

      IMHO given the relatively large size of the effect it seems quite likely that the noise part is in fact potentially large (this is much more subjective) which makes is less clear that there is measurable signal at all here. I’d have to see a lot of replication or a very strong explanation of the underlying mechanism to believe the magnitude of the effect, but will very easily believe the sign (with a small magnitude).

    - **graemep** · [2025-03-31 08:48 UTC](https://news.ycombinator.com/item?id=43532696)
      \> All research is met on HN by people who know better and will tell you why it's flawed ^c43532696

      It is almost certainly flawed, and it is probably wrong: [https://journals.plos.org/plosmedicine/article?id\=10.1371/jo...](<https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124>)

      If you are discussing research at all it is important to discuss the flaws too. The alternative I can see would be to take every published paper as proven true even though we know this is not the case.

    - **bawolff** · [2025-03-31 02:42 UTC](https://news.ycombinator.com/item?id=43530276)
      Science succeeds when people lean towards the side of cynicism instead of optimism. Scientific research should be read critically. ^c43530276

      - **mmooss** · [2025-03-31 02:47 UTC](https://news.ycombinator.com/item?id=43530320)
        Critical thinking and skepticism are good, but much of what happens on HN is not that. ^c43530320

        Thinking critically includes, most of all, finding value - you need to think critically (and skeptically) to avoid assigning value to things that don't have it, but you must find value. The goal is to build knowledge - just like the study author needs to find knowledge among flawed data, you must find knowledge among flawed studies - and they are all flawed, of course.

        Focusing on the flaws and trying to shoot down everything is just craven recreation.

        - **jval43** · [2025-03-31 06:02 UTC](https://news.ycombinator.com/item?id=43531612)
          Science is a long game, it's not about sales where you need to sell right now. Extreme results will be attempted to be replicated, which in turn costs a lot of funding. That is money and time, sometimes a whole persons career. ^c43531612

          This money and time is taken directly away from funding other, potentially more worthy or more likely to be correct studies.

          There is no point of looking at every (flawed) study in the most positive way, unless you have unlimited time and money to pursue every avenue of research.

          Often (not always), the studies that are most heavily promoted among the news and in business or politics are really not the best research and other, less visible but more solid research gets ignored in favor of whats popular or what has had good marketing.

          This is very frustrating for people doing solid good research, because every so often someone else will come along with wild, exaggerated claims and very little data to back it up, and then gets funding for it.

          It takes literal years away from good science just because someone markets and speaks well.

          Which is fine in business, but in science this is not something "the market" can or will correct for well, simply because the timespans are so long.

          - **mmooss** · [2025-03-31 06:58 UTC](https://news.ycombinator.com/item?id=43531997)
            \> There is no point of looking at every (flawed) study in the most positive way ^c43531997

            This line epitomizes the nonsense in the discussion. I didn't say *every* study, you can't know it's *flawed* without seriously examining it, and I didn't say *in the most positive way* at all.

            By using these exaggerations, you damage any serious discussion - you give people nothing to respond to except your emotional state.

            What I said was, the point is to build knowledge, and so the way to examine research is to find the valuable knowledge - which includes evaluating the accuracy, etc. of that knowledge. There's no other point to it - we're not awarding tenure here, so there's point in keeping some overall score. We just want to learn what we can.

            - **jval43** · [2025-03-31 08:11 UTC](https://news.ycombinator.com/item?id=43532472)
              I did not say *this* study is flawed or that *every* study is flawed. And I have made no exaggerations or said that *you* personally look at it the most positive way. ^c43532472

              Reading comprehension is important, and especially important in a discussion like this.

              I do however really mean that some studies are not worth looking at all in more detail: if the methodology is flawed, the results are meaningless. At most the premise of such a hypothetical (not saying this one necessarily!) study could be used as an idea for further research, but not to build knowledge on or derive knowledge from the results.

          - **ryandrake** · [2025-03-31 17:06 UTC](https://news.ycombinator.com/item?id=43537260)
            Are there some examples of "non flawed" research that is getting ignored? Because (as a non-academic) I feel like I'm seeing the same HN attitude that OP describes. No study is good enough for HN. There are always nit pickers that come out of the woodwork. For every science article about some study or finding, the top comment is *always* a variation on: "This study is flawed because..." Almost without exception. Also, the standard is so high: A single flaw found is grounds for dismissing the whole study as flawed. ^c43537260

            My guess is if you raise examples of "good science" the HN peanut gallery will jump in to point out the flaws in that science, too.

        - **Aurornis** · [2025-03-31 04:47 UTC](https://news.ycombinator.com/item?id=43531176)
          \> you need to think critically (and skeptically) to avoid assigning value to things that don't have it, but you must find value. ^c43531176

          This isn’t critical thinking.

          This is toxic positivity.

          It’s okay to admit that some studies don’t have value to add. If you don’t accept this, you’re going to be tricked by a lot of people trying to get your attention with bad data.

          Being able (and willing!) to filter out bad sources, even when they say something you want to hear, is a critically important skill. If you force yourself and others to find something positive about everything then you’re a dream come true to purveyors of low quality or even deliberate misinfo.

          - **mmooss** · [2025-03-31 04:49 UTC](https://news.ycombinator.com/item?id=43531192)
            lol ^c43531192

            \> some studies

            It's almost every study on HN, not some studies, which you'd understand if you read my comment.

            - **jval43** · [2025-03-31 05:48 UTC](https://news.ycombinator.com/item?id=43531528)
              Yes because most studies that end on up HN are there because they were reported on somewhere as news. ^c43531528

              This usually happens in usually these cases:

              1\. when a paper is extremely good and it's results are groundbreaking, or

              2\. when a study itself claims it has groundbreaking results, or

              3\. when it's a regular study that's gotten some great marketing/promotion e.g. by their university.

              The case of 1. is extremely rare, and even when everyone believed the results and they were peer reviewed by a reputable paper like Science, some of them turned out to be academic fraud that was later retracted.

              Most studies that pop up on HN are of types 2. and 3. That's just because otherwise they would not get news attention.

              But most studies in general are in category 4: the ones an academic or professional would read going about their daily business / research. These range from terrible, to OK, to really great, but 99\% never make the news.

              As a (former) academic, I've read lots of papers and like in real life it's usually the people (papers) that get attention who scream the loudest. There are some gems too of course, and it's right to not ignore anything.

              But in my personal experience and over time, I've been very right to be very sceptical once a result turns up in the news because of the 3 ways it can get there.

              This is amplified even more so with papers that base their results / outcome purely on statistics, such as most experimental studies done. These derive their results *from* the statistics (sample size, experiment design, etc) so their power and the probability of their result being correct (what the authors say) it directly coupled.

        - **strken** · [2025-03-31 04:16 UTC](https://news.ycombinator.com/item?id=43530932)
          Focusing on the flaws is vital context for helping ordinary people understand the world. Any given study with a surprising result is likely wrong. Yeah, some of them are going to be right, but you're going to get many false positives and only a handful of studies that replicate to a convincing degree. ^c43530932

          I've made this mistake time and time again, most recently with vitamin D association studies, and I'm grateful to all the people who urged everyone else to take a wait-and-see approach.

        - **Jensson** · [2025-03-31 03:50 UTC](https://news.ycombinator.com/item?id=43530762)
          \> Focusing on the flaws and trying to shoot down everything is just craven recreation. ^c43530762

          No, its a valuable job to find flaws because its much easier to fix and work on known flaws than to stumble in the dark.

          Removing flaws and problems is one of the easiest ways to add value.

          - **mmooss** · [2025-03-31 04:58 UTC](https://news.ycombinator.com/item?id=43531229)
            It's not valuable. People who do this at work are people who have no value to offer so they try to sound smart (and valuable) by finding flaws in someone else's work. All work is limited and flawed - it's easy to find them. Add the common hyperbolic statements on HN dismissing the entire study or whole fields of research, and it's misinformation. ^c43531229

            The real significance is that things like sample size, to pick a common example here, is easy to understand in a theoretical way and so people apply it to the actual (not theoretical) practice of real research, which they don't understand the practicalities of, and also they overemphasize it because that's pretty much all they understand.

            The first thing they look at in a paper is sample size - and hey, now sometimes they have something to 'contribute'! It's just reinforcing the same misunderstandings in others.

            It sucks, a little, to have nothing to contribute, but it's a great opportunity to learn from people who do know.

    - **robertlagrant** · [2025-03-31 08:26 UTC](https://news.ycombinator.com/item?id=43532558)
      \> All research is met on HN by people who know better and will tell you why it's flawed. There isn't a greater collection of expertise in the history of the world than on HN. ^c43532558

      It seemed like a pretty valid criticism. These studies should be taken with a massive pinch of salt because they're fairly uncontrolled.

    - **im3w1l** · [2025-03-31 17:54 UTC](https://news.ycombinator.com/item?id=43537762)
      Installing air filters is an intervention that has a cost and thus needs to be verified and proven. You don't roll such a thing out on a broad scale based on "the effect *could* be large". ^c43537762

      - **dzhiurgis** · [2025-03-31 19:05 UTC](https://news.ycombinator.com/item?id=43538555)
        I find it bonkers we have better regulation around growing battery chickens than growing kids. ^c43538555

        You don’t need massive study to find out that kids don’t like suffocating in classrooms.

        It’s a bit like mandating reversing cameras on cars. Study says economically they do not make sense, but not squishing your kids trumps that.

        - **im3w1l** · [2025-04-01 06:24 UTC](https://news.ycombinator.com/item?id=43543449)
          Suffocating would be CO2 rather than particles? ^c43543449

    - **LorenPechtel** · [2025-03-31 22:01 UTC](https://news.ycombinator.com/item?id=43540444)
      Things which reach the level of getting on here are basically always outliers.  And is the outlier real or a false positive?  There's a huge selection bias towards the false positives. ^c43540444

    - **eru** · [2025-03-31 03:54 UTC](https://news.ycombinator.com/item?id=43530786)
      \> Based on your comment, the effect could be larger as well as smaller. ^c43530786

      Yes, but since we know that there's a huge bias to publish and publicise larger results, you know what way to bet.

    - **noosphr** · [2025-03-31 03:37 UTC](https://news.ycombinator.com/item?id=43530654)
      [https://xkcd.com/882/](<https://xkcd.com/882/>) ^c43530654

    - **lazyeye** · [2025-03-31 04:36 UTC](https://news.ycombinator.com/item?id=43531093)
      Yes most responses on HN appear to fall into 2 broad categories:- ^c43531093

      1\. Why this blog post study is flawed and dumb

      2\. America is bad and shameful.

      - **mmooss** · [2025-03-31 05:06 UTC](https://news.ycombinator.com/item?id=43531275)
        That's an interesting comparison, how people analyze and evaluate research and how they do the same with public affairs. ^c43531275

        I would have said that the point of research is to find the value and build knowledge, while the point of discussing public affairs is to identify problems to fix.

        Thinking about it, I'm not sure the latter can't find things that are constructive. But in either field, the exaggerated, dismissive comments/rants are not just a waste but damaging to progress.

  - **MPSFounder** · [2025-03-31 02:46 UTC](https://news.ycombinator.com/item?id=43530314)
    I wish we made more efforts to check air quality. I went to a great school, and the water filter hadnt been replaced since 2005 (it was 2012 at the time, and filters were supposed to be replaced every 6 months). My point is people take it for granted that air quality or water quality in the US is great, but if we checked, I bet most of us are exposed to cancerous materials all the time that could be easily prevented (the water stations rn are made of plastic (PVC), which leaches in the water over time and leads to nanoplastics accumulating in all of us. Easily prevented through more expensive steel pipes). Hell, my office had asbestos in the ceiling that was painted over! It sucks we lack regulation, as I do not believe it is my job to check these things and report them, and I got tired of it. Given the EPA is lacking funds, it is imperative all of us do due diligence so our children do not experience the cancer rates that are ravaging us (our cancer rates are 30\% higher than Europe once you rule out lung cancer, which is a result of their smoking habits. The europeans love their cigs). ^c43530314

    - **eru** · [2025-03-31 04:25 UTC](https://news.ycombinator.com/item?id=43531006)
      They would have probably been better off without a water filter? ^c43531006

      Your local utility should send you water that doesn't need further filtering.

    - **LorenPechtel** · [2025-03-31 22:54 UTC](https://news.ycombinator.com/item?id=43540874)
      Steel pipes?  You realize steel that can be made into a pipe contains some metals you want to minimize your exposure to? ^c43540874

      As for painting over asbestos--that's actually considered acceptable.  Asbestos sitting there isn't going to hurt you.  Asbestos only hurts you when it's disturbed.  Removing intact asbestos is likely to increase your exposure, not decrease it.

      As for cancer--why are you so sure it's chemicals and not lifestyle?

      - **MPSFounder** · [2025-04-01 04:31 UTC](https://news.ycombinator.com/item?id=43542865)
        I cannot be sure. Causation is very difficult to pinpoint. Not all steel leaches (hell, we use stainless steel cups often). I will take steel over plastics any given day of the week. Regarding paint, sure, but paint peels, and next you are breathing microdoses of asbestos. ^c43542865

  - **d--b** · [2025-03-31 04:13 UTC](https://news.ycombinator.com/item?id=43530901)
    Maybe or maybe not. Further research should tell. ^c43530901

    Maybe the tests results are better because the children are more rested on the day of the test. Maybe the hum of the machine creates some kind of meditative noise that helps children concentrate. Or maybe none of that is true..

  - **7thaccount** · [2025-03-31 02:32 UTC](https://news.ycombinator.com/item?id=43530203)
    I'm a big fan of air filters and have many in my own home that have made a big difference in quality of life as I live in a high pollen area. They can help with a lot more irritants as well that some students may be sensitive to (i.e., some students may study better if their immune system isn't in overdrive for half the school year like mine was). I'm not sure how these would help with natural gas though. I can't read the article due to paywall. Some VOCs can be filtered out (at least I think) with a baking soda filter ...those have to be changed more often than the HEPA filters (at least on my model that has one). Again, that should help with some scents (a major issue for me - even the dishwasher running can cause problems for me), but it isn't going to help if there is a gas leak (not sure if that is what the article is suggesting). ^c43530203

    - **pizzly** · [2025-03-31 03:59 UTC](https://news.ycombinator.com/item?id=43530815)
      I'm not sure what it was but I remember learning where with a continuous runny noise in certain classes (buildings) with AC. Outside and different buildings were fine at least for me. In those effected buildings I estimate that 5\% were also effected by hearing people sniff every minute or so. This definitely caused distraction while learning. A good filter on the AC would properly have solved this. ^c43530815

    - **maxerickson** · [2025-03-31 03:03 UTC](https://news.ycombinator.com/item?id=43530444)
      The article and study are both explicit that natural gas wouldn't have been an issue (the leak was fixed and the gas was gone). The impact from the filters would be from other indoor air pollutants. ^c43530444

      - **7thaccount** · [2025-03-31 03:27 UTC](https://news.ycombinator.com/item?id=43530582)
        Thank you! ^c43530582

    - **LorenPechtel** · [2025-03-31 22:08 UTC](https://news.ycombinator.com/item?id=43540499)
      The gas was long gone, it wasn't being filtered. ^c43540499

      However, I don't see that it proves pollution is the cause.  What about infection?  Air filtration can reduce the spread of pathogens.  Schools throw together a large pool of people, the bug of the day will go around.  Less if there are good filters.

  - **evil-olive** · [2025-03-31 02:58 UTC](https://news.ycombinator.com/item?id=43530415)
    \> but I also think the extreme results from this study aren't going to hold up to further research. ^c43530415

    there already is further research. and the results do seem to be holding up.

    the study you're quoting from is the one linked in the 2nd paragraph of the article. this is from the 3rd paragraph:

    \> But it’s consistent with a growing literature on the cognitive impact of air pollution, which finds that everyone from chess players to baseball umpires to workers in a pear-packing factory suffer deteriorations in performance when the air is more polluted.

    that paragraph links to an earlier Vox article \[0\] which goes into more detail, and well as linking to all of the various studies:

    \> A wide range of studies about the impact of pollution on cognitive functioning have been published in recent years, showing impacts across a strikingly wide range of endeavors. Stripe CEO Patrick Collison has taken an interest in this subject and compiled much of the key research on his personal blog. Among the findings he’s highlighted include:

    \> - Exposure to fine particulates over the long term leads to increased incidences of dementia and Alzheimer’s disease in the elderly (a second study confirms this).

    \> - A study of 20,000 older women found that 10 micrograms of additional long-term particulate exposure is equivalent, across the board, to about two additional years of aging.

    \> - The impacts are not limited to the elderly, however, nor are they exclusively long-term. A range of specialized professionals also seem to suffer short-term impairment due to air pollution. Skilled chess players, for example, make more mistakes on more polluted days. Baseball umpires are also more likely to make erroneous calls on days with poor air quality. Politicians’ statements become less verbally complex on high-pollution days, too.

    \> - Ordinary office workers also exhibit these impacts, showing higher scores on cognitive tests when working in low-pollution ( or “green”) office environments. Individual stock traders become less productive on high-pollution days.

    \> - The same also appears to be true for blue collar work. A study of a pear-packing factory found that higher levels of outdoor particulate pollution “leads to a statistically and economically significant decrease in packing speeds inside the factory, with effects arising at levels well below current air quality standards.”

    \> - Last but by no means least, the cognitive impacts appear to be present in children, with a Georgia study that looked at retrofits of school buses showing large increases in English test scores and smaller ones in math driven by reduced exposure to diesel emissions.

    0: [https://www.vox.com/future-perfect/2019/12/11/20996968/air-p...](<https://www.vox.com/future-perfect/2019/12/11/20996968/air-pollution-cognitive-impact>)

    - **Aurornis** · [2025-03-31 04:34 UTC](https://news.ycombinator.com/item?id=43531074)
      \> there already is further research. and the results do seem to be holding up. ^c43531074

      You’re conflating different results.

      The results *of the headline study* are dramatic in ways that aren’t holding up. The test score increase happened after a single year of putting air filters in class rooms. That’s minimal exposure to purified air for a fraction of the day, 5 days a week, for less than a year of classes.

      The other studies are much longe term and look at things like decades of exposure at city scale.

      Do you see the difference? The study tried to claim that purifying air immediately improved test scores by dramatic amounts.

      There are other serious limitations in the study, like the fact that they can’t even identify which air purifiers were installed or how effective they were. There’s a footnote that says many weren’t even used. There’s a section on air quality monitoring that says they didn’t even detect the VOCs they were trying to filter before they started filtering.

      This is the type of study that people implicitly believe because it makes logical sense, but when you read the details you realize that there isn’t much substance in it.

      - **fc417fc802** · [2025-03-31 10:32 UTC](https://news.ycombinator.com/item?id=43533312)
        \> The other studies are much longe term and look at things like decades of exposure at city scale. ^c43533312

        Are they? Several towards the end of the list are specifically about short term day-to-day effects across a range of situations.

        \> There’s a footnote that says many weren’t even used.

        Quite damning if true.

        \> they didn’t even detect the VOCs they were trying to filter before they started filtering

        That is confusing the reasoning that led to the company footing the bill versus what was being looked at here. The lack of VOCs is actually in the author's favor as it eliminates "exposure to atypical VOCs" as an otherwise fairly severe confounding factor.

  - **xattt** · [2025-03-31 01:54 UTC](https://news.ycombinator.com/item?id=43529891)
    If anything, schools able to implement air filtration and fresh air exchanges systems are likely those flush with cash and supportive parents. ^c43529891

    - **permo-w** · [2025-03-31 02:17 UTC](https://news.ycombinator.com/item?id=43530067)
      in this case the filtration systems were installed on the dime of a local natural gas company after a leak, although that was as a result of the interference of interested parents ^c43530067

    - **dzhiurgis** · [2025-03-31 19:12 UTC](https://news.ycombinator.com/item?id=43538629)
      These systems are not that expensive and save money. ^c43538629

      If parents would be allowed to contribute towards it like a 10year bond it would pay for itself…

    - **xwolfi** · [2025-03-31 02:13 UTC](https://news.ycombinator.com/item?id=43530045)
      And the resulting backlash 10 years down the line ? I don't think science should be used that way: who would trust it eventually ? ^c43530045

      Would you support a small study saying a medicine or a vaccine produces a 20 year life expectancy increase, all that to end up 20 years later with no improvement, everyone on that medicine, and the anti-everything yelling on every platform that the big pharma lobby poisoned our children ?

      Even when the studies are on large samples, double-blind, long time range with a clear explanation as to why there's an effect, we have people trying to kill the resulting health campaigns. Don't encourage fake ones !

      - **eru** · [2025-03-31 04:22 UTC](https://news.ycombinator.com/item?id=43530981)
        \> I don't think science should be used that way: who would trust it eventually? ^c43530981

        There's no single party controlling 'science'.  It's all just individuals many of them under 'publish or perish' rules.

    - **calvinmorrison** · [2025-03-31 02:33 UTC](https://news.ycombinator.com/item?id=43530211)
      only ycombinator would have a hard time with the concept of 'open the window' and instead expect a capital installment of \$2B to retrofit classrooms ^c43530211

      - **do\_not\_redeem** · [2025-03-31 02:55 UTC](https://news.ycombinator.com/item?id=43530392)
        Do you think everyone lives in California where there's comfortable sunny temperatures and no rain 360 days a year? Classic ycombinator post ^c43530392

        - **eru** · [2025-03-31 04:24 UTC](https://news.ycombinator.com/item?id=43531000)
          German schools open their windows in winter. ^c43531000

          It's the classic German Stoßlüften in action.

          However, the air outside also has lots of dusts.  Opening the windows does nothing for that, but air filtration can potentially help.

          - **dzhiurgis** · [2025-03-31 19:14 UTC](https://news.ycombinator.com/item?id=43538652)
            We did it too, but it was huge ceremony around it. Kids shouldn’t be begging and screaming “too cold” for fresh air. ^c43538652

            - **eru** · [2025-04-01 00:24 UTC](https://news.ycombinator.com/item?id=43541533)
              The ceremony is part of the fun. ^c43541533

              Though for us the ceremony was only one or two mild complaints from the kids near the window, and the teacher firmly stating that the room reeks of sweaty teenagers and needs some airing out.

        - **nottorp** · [2025-03-31 13:55 UTC](https://news.ycombinator.com/item?id=43535113)
          When I was in school we opened the windows to let "fresh air" in even at -20 C... not all day ofc but every day. ^c43535113

          And rain? What's the problem with opening a window when it's raining? Only if there's a rain storm... and not even then, depending on wind direction.

      - **lazyasciiart** · [2025-03-31 02:49 UTC](https://news.ycombinator.com/item?id=43530342)
        Yes, silly gas company, should just tell the local schools to open the windows and let the natural gas in. ^c43530342

        You have heard of air pollution, I assume. Some schools are in places that *regularly* have polluted air.

      - **ajb** · [2025-03-31 07:45 UTC](https://news.ycombinator.com/item?id=43532272)
        In many areas the source of air pollution is outside. Opening windows helps with house dust and mold spores, but not with particulates from diesel, tyres or with pollen. ^c43532272

  - **dzhiurgis** · [2025-03-31 18:59 UTC](https://news.ycombinator.com/item?id=43538480)
    Perhaps we shouldn’t need a large cohort study to give little humans the right to breathe as good as battery chickens. ^c43538480

  - **ninetyninenine** · [2025-03-31 04:02 UTC](https://news.ycombinator.com/item?id=43530828)
    You ever heard of the paradox of IQ? ^c43530828

    IQ has about a 0.2 correlation with income. The paradox arises when you zoom out for a more macro view. National IQ has about a 0.6-0.8 correlation with GDP per capita.

    Performance in class rooms is definitely an IQ thing and different view points will likely generate different sets of data.

    I'm interested in seeing controlled trials on individual performance, not just observing real world scenarios.

  - **VladVladikoff** · [2025-03-31 02:05 UTC](https://news.ycombinator.com/item?id=43529985)
    One problem with nutrition based science is it suffers from nutrigenomics bias. It’s possible to study small cohorts of similar genetics and come to conclusions which fail to extrapolate to larger populations. 
    It’s possible that this same problem does not apply to air filtration. ^c43529985

    - **ted\_dunning** · [2025-03-31 03:02 UTC](https://news.ycombinator.com/item?id=43530434)
      It's possible, but much less likely since they controlled for demographics and cited a number of related studies that show comparable effects. ^c43530434

  - **fasthands9** · [2025-03-31 03:41 UTC](https://news.ycombinator.com/item?id=43530679)
    It also seems possible that students do better on tests when the air is cleaner, but that doesn't necessarily mean the students learned more. ^c43530679

    Imagine if some schools installed air conditioning in their gym one year. Running times around an indoor track would improve considerably, but mostly because conditions at the point of testing improved. Not necessarily because the air conditioning made the students actually improve their stamina or speed.

  - **facile3232** · [2025-03-31 04:37 UTC](https://news.ycombinator.com/item?id=43531102)
    \> but expecting test scores to improve dramatically like this is not realistic ^c43531102

    That seems like a problem for the reader, not a problem with the text. Why would the reader expect this? Is it the use of present tense in the title rather than past tense?

    - **Aurornis** · [2025-03-31 04:42 UTC](https://news.ycombinator.com/item?id=43531135)
      What do you mean? The article implies it from the title through the text. ^c43531135

      They hedge by saying “could” but like most articles in this vein it goes on to pivot around the outlier study.

      - **facile3232** · [2025-03-31 17:21 UTC](https://news.ycombinator.com/item?id=43537427)
        Ah! I just skipped the article. The paper is much more straightforward. ^c43537427

- **rayiner** · [2025-03-31 01:37 UTC](https://news.ycombinator.com/item?id=43529773)
  Someone writes whether the data actually shows what it purports to show: [https://statmodeling.stat.columbia.edu/2020/01/09/filters-be...](<https://statmodeling.stat.columbia.edu/2020/01/09/filters-benefits/>) ^c43529773

  \> The whole thing is driven by one data point and a linear trend which makes no theoretical sense in the context of the paper (from the abstract: “Air testing conducted inside schools during the leak (but before air filters were installed) showed no presence of natural gas pollutants, implying that the effectiveness of air filters came from removing common air pollutants”) but does serve to create a background trend to allow a big discontinuity with some statistical significance.

  I’m reminded of the walkback of scientific studies showing massive benefits from giving kids in third world countries deworming medications: [https://www.theguardian.com/society/2015/jul/23/research-glo...](<https://www.theguardian.com/society/2015/jul/23/research-global-deworming-programmes>).

  My beef with Matt Y.’s worldview of “scientifically driven public policy” is that the costs and benefits of public policy interventions are so devilishly difficult to study that you can’t meaningfully use them on realistic time scales to drive policy. This is an exceedingly simple hypothesis—filtering air improves test scores—that can easily be tested while controlling for confounding factors. But even then it’s hard!

  - **rnjailamba** · [2025-03-31 05:17 UTC](https://news.ycombinator.com/item?id=43531351)
    Andrew Gelman: "No, I don’t think that this study offers good evidence that installing air filters in classrooms has surprisingly large educational benefits."
    [https://statmodeling.stat.columbia.edu/2020/01/09/no-i-dont-...](<https://statmodeling.stat.columbia.edu/2020/01/09/no-i-dont-think-that-this-study-offers-good-evidence-that-installing-air-filters-in-classrooms-has-surprisingly-large-educational-benefits/>) (Adding this older link here for cross reference) ^c43531351

    A thread on Gelman's article is here: [https://news.ycombinator.com/item?id\=22006595](<https://news.ycombinator.com/item?id=22006595>).

  - **Analemma\_** · [2025-03-31 02:29 UTC](https://news.ycombinator.com/item?id=43530172)
    The study itself is pretty explicit that it is just one encouraging case study which the authors believe merits follow-up research, rather than something conclusive. Matt Y's reporting isn't as forthcoming about this as it probably should've been, but he does also say the same thing at the end. He sort of buried the lede but didn't lie or anything. ^c43530172

    - **rayiner** · [2025-03-31 05:16 UTC](https://news.ycombinator.com/item?id=43531346)
      I'm not accusing Matt Y. of lying. I like him and subscribe to his Substack. I'm just saying that the article illustrates the shortcoming of his approach to public policy. His data-driven approach to public policy is based on an overly optimistic view of reliability of the data. ^c43531346

  - **sudoshred** · [2025-03-31 02:21 UTC](https://news.ycombinator.com/item?id=43530105)
    The material impacts associated with the recommendations a study makes can influence the results in a way that does not favor objectivity. ^c43530105

- **amluto** · [2025-03-31 02:50 UTC](https://news.ycombinator.com/item?id=43530351)
  I wish there was more data on the effects of gasses in the air on people. ^c43530351

  We seem to know:

  \- Elevated CO2 in rooms impairs cognitive performance.

  \- Elevated CO2 in submarines, at levels *far* higher than you would see in a normal room does not appear to impact cognitive performance.

  \- Installing *carbon* filters (what this study actually looked at) might improve classroom performance.

  \- People don’t like stuffy rooms.

  All this is consistent with multiple hypotheses.  It could be that we just don’t know anything about it. Or maybe there is some gas or gasses emitted by people *that isn’t CO2* that makes people mildly uncomfortable and have worse cognitive performance.

  CO2 is certainly a good proxy for ventilation quality in a space where air is exchanged with outdoors but where the gasses in the air are not otherwise changed. Carbon-filtered classrooms and submarines are not examples of this.

  - **jedc** · [2025-03-31 03:30 UTC](https://news.ycombinator.com/item?id=43530599)
    (Former submariner here.) ^c43530599

    Elevated CO2 in submarines absolutely impairs performance.  One example: there was a guy on my boat who got migraines when CO2 got too high - he was useless.  Luckily the fix is simple - just turn on another CO2 scrubber.

    There's nothing special about a submarine that makes CO2 somehow different than anywhere else.

    - **amluto** · [2025-03-31 03:47 UTC](https://news.ycombinator.com/item?id=43530736)
      I recall this study and maybe another one: ^c43530736

      [https://pubmed.ncbi.nlm.nih.gov/29789085/](<https://pubmed.ncbi.nlm.nih.gov/29789085/>)

      I’m definitely not an expert.

    - **4gotunameagain** · [2025-03-31 06:44 UTC](https://news.ycombinator.com/item?id=43531906)
      What if you're low on sorbent and can't turn on another scrubber ? ^c43531906

      I wonder if sorbent quantity correlates with performance

  - **frognumber** · [2025-03-31 03:52 UTC](https://news.ycombinator.com/item?id=43530772)
    CO2 is a proxy for many other gasses. Cheap CO2 sensors sense volatile organic compounds (VOCs), and use those to estimate CO2. ^c43530772

    Many of those gasses do impact cognitive performance. It's not obvious to me why CO2 would, but if CO2 is going up, so is everything else we breathe out. CO2 where I am is somewhere in the ≈400ppm-1000ppm range -- 0.04\% or 0.1\% -- and it's pretty inert. I'm not sure what harm it does.

    If it does to harm, rising CO2 levels should be much more concerning than "just" climate change.

    But I suspect it's other gasses.

    - **vlovich123** · [2025-03-31 04:10 UTC](https://news.ycombinator.com/item?id=43530883)
      Rising co2 levels I believe are nowhere near the differential inside vs outside when windows are closed. There’s lots of reason to believe that rising co2 specifically lowers cognitive performance - our brains work on o2 and our body actively works to expel co2 as a waste product - increasing co2 levels means the body has less O2 available and has to work harder on co2 expulsion for survival instead of powering the brain. ^c43530883

      - **LorenPechtel** · [2025-03-31 23:19 UTC](https://news.ycombinator.com/item?id=43541054)
        Crowding out O2 isn't going to be meaningful, the amount of CO2 is simply too small.  If there's an effect it's from reducing the rate at which the body can expel the CO2. ^c43541054

        If crowding out O2 was relevant why do I feel the same on our local mountain at 10,000'+ vs 0'- in Death Valley?  To crowd out that much O2 with CO2 would be lethal.  (That's not to say that my performance is the same.  There's a big difference in the heart rate I can sustain.)  What we feel is the CO2 level in our blood rising because it isn't diffusing into the lungs.  Lowering O2 is only detectable with training and that's based on noting the symptoms of oxygen deficiency on brain function.  (Such training is relevant in the world of aviation where it might give warning that you need to grab that oxygen mask.  The average person will never encounter such conditions, nor have the resources at hand to make use of the knowledge even if they did realize it.)

      - **frognumber** · [2025-03-31 11:44 UTC](https://news.ycombinator.com/item?id=43533821)
        This is not quite correct. ^c43533821

        1) CO2 levels have risen from under 300PPM in 1860 to over 400PPM right now -- by around 150PPM -- with a rise of about 25PPM per decade for the past four decades.

        The difference in CO2 levels in my bedroom with windows open and closed is a couple hundred PPM (500-800ppm range in my bedroom, with windows open and closed, respectively). I can definitely feel a difference in performance if I don't let in fresh air. It's more than climate change  (300ppm versus 150ppm range), but not big-O more, and climate change is on-track to get there in another few decades. Conference rooms might be over 1000ppm, but it still big-O similar.

        2) CO2 levels are measured in parts-per-MILLION. That argument simply doesn't make sense. The atmosphere is 21\% oxygen. Crowding out oxygen is simply not an issue. Critically, from personal experience, if I have some dry ice in a room, I generally don't suffer.

        People run into problems when CO2 levels reach a out 5000 ppm over many hours. Even the most dense conference rooms don't hit that.

        - **vlovich123** · [2025-03-31 13:48 UTC](https://news.ycombinator.com/item?id=43535030)
          Here’s what Claude says. ^c43535030

          1\. Direct effects on brain physiology: When CO2 levels rise in the blood (hypercapnia), it causes vasodilation of cerebral blood vessels. While this initially increases blood flow, sustained elevation disrupts the brain's normal pH balance, affecting neural function.

          2\. Acid-base imbalance: Elevated CO2 in the blood forms carbonic acid, decreasing blood pH. This acidosis affects enzyme function, neurotransmitter activity, and neuronal excitability throughout the brain.

          3\. Oxygen displacement: While not typically reaching dangerous levels in standard indoor environments, higher CO2 concentrations can slightly reduce oxygen availability to brain tissues in enclosed spaces.

          4\. Inflammatory responses: Research suggests prolonged exposure to elevated CO2 may trigger low-grade neuroinflammatory responses, potentially impairing cognitive processes.

          5\. Disruption of neurotransmitter systems: CO2-induced acidosis appears to affect several neurotransmitter systems, particularly GABA and glutamate, which are critical for cognitive functions like attention, memory, and decision-making.

          Studies have shown measurable cognitive effects at CO2 concentrations as low as 1,000 ppm, with more significant impairment at 2,500+ ppm - levels commonly found in poorly ventilated meeting rooms, classrooms, and offices.

          As for indoor vs outdoor:

          \> Rising atmospheric CO2 levels from global warming don't pose the same cognitive risks as elevated indoor CO2. While indoor environments can reach 1,000-5,000+ ppm, causing measurable cognitive decline through mechanisms like acid-base imbalance and neurotransmitter disruption, global atmospheric CO2 is only about 420 ppm. Even with projected increases to 500-1,000 ppm by 2100 in worst-case scenarios, these levels remain below thresholds for significant cognitive impairment. Our bodies can also better adapt to gradual atmospheric changes compared to rapid indoor CO2 accumulation, making climate change impacts the primary concern rather than direct cognitive effects.

- **aetherspawn** · [2025-03-31 03:54 UTC](https://news.ycombinator.com/item?id=43530780)
  I’m so confused why they installed HEPA filters to filter out LNG and methane. ^c43530780

  And HEPA filters don’t really scrub CO2 that effectively, even with a carbon membrane, so can we really expect lower CO2 levels?

  Considering this, what’s the actual takeaway here? Cleaner air (dust/virus free?) is better for productivity?

  I am asking because I want to buy the same filter for work, but I am doubtful that the \$700 HEPA filter sounds like the same filter they used, even though the article mentions they used readily accessible 5 stage filters.

  - **amluto** · [2025-03-31 04:42 UTC](https://news.ycombinator.com/item?id=43531145)
    Having tried to dig into this a while ago, they installed *carbon* filters. ^c43531145

    Most of the stuff for sale as “carbon” filters has too little carbon to do much. You want quite a lot, and, for some gasses, you can get special impregnated carbon or other media.

    - **aitchnyu** · [2025-03-31 05:37 UTC](https://news.ycombinator.com/item?id=43531471)
      Tangential, are there DIY methods of activated carbon? I got pellets, impregnated sheets and a packaged one for my air purifier, but I dont know when they are helping and when they are exhausted. ^c43531471

      - **schiffern** · [2025-03-31 08:38 UTC](https://news.ycombinator.com/item?id=43532638)
        To tell when carbon filters are exhausted, the best way is to use an indoor VOC monitor. ^c43532638

        Air filter AC is specially prepared, so making your own DIY charcoal (while possible) isn't nearly as effective. You can mostly regenerate/desorb the carbon by heating it to 400F. Never use your regular oven though, not least of which because it *reeks*. Get a cheap toaster oven and disposable foil pans and do it outside, in a location where it can't possibly catch anything on fire.

        - **aitchnyu** · [2025-03-31 14:41 UTC](https://news.ycombinator.com/item?id=43535616)
          Can you share an Amazon product which is real air filter carbon? And an enclosure? ^c43535616

          - **amluto** · [2025-03-31 15:45 UTC](https://news.ycombinator.com/item?id=43536346)
            Some of the stuff on Amazon sold for indoor marijuana growing is probably legit, and you can easily buy cylindrical cartridges and attach an axial fan. ^c43536346

            Or you can buy from one of the most reliable e-commerce sites in the US:

            [https://www.mcmaster.com/product/3722T98](<https://www.mcmaster.com/product/3722T98>)

            [https://www.mcmaster.com/product/2169K16](<https://www.mcmaster.com/product/2169K16>)

            You’re on your own as to buying the correct size.

            For what it’s worth, the IKEA carbon filters are inexpensive and appear to be legit.

  - **tangjurine** · [2025-03-31 04:07 UTC](https://news.ycombinator.com/item?id=43530858)
    I'm guessing someone had a hunch and wanted to buy some HEPA filters. Also, all HEPA filters should filter air similarly, the price should be based on the rate  at which air is filtered. I bought a HEPA air filter for \$150 for my room. ^c43530858

    - **sokoloff** · [2025-03-31 04:14 UTC](https://news.ycombinator.com/item?id=43530913)
      There are ratings spanning H10, H11, H12, and H13 for HEPA filters. ^c43530913

- **jwpapi** · [2025-03-31 01:36 UTC](https://news.ycombinator.com/item?id=43529769)
  Personal anecdote getting an airthings that reminds me to open the window (along with a pushover api setup) has probably been the biggest productivity improvement in 10 years. ^c43529769

  - **Cthulhu\_** · [2025-03-31 09:41 UTC](https://news.ycombinator.com/item?id=43533009)
    It's kinda worrying you need an app / appliance to remember to open the window. Rule of thumb is to have the windows open at least 10 minutes a day, every day. ^c43533009

    - **jwpapi** · [2025-04-09 21:12 UTC](https://news.ycombinator.com/item?id=43638056)
      Sometimes I’m just too much in the zone working and I forget, leading to 10 mins more in the zone, but less overall focused work through the day. ^c43638056

    - **LorenPechtel** · [2025-03-31 23:21 UTC](https://news.ycombinator.com/item?id=43541073)
      You realize a lot of us live in places where that would be very expensive?  Not to mention that the HVAC plants are usually not sized with that in mind. ^c43541073

      - **socksy** · [2025-04-01 06:41 UTC](https://news.ycombinator.com/item?id=43543542)
        Why is opening the window expensive? Climate control? ^c43543542

        - **willlma** · [2025-04-01 20:02 UTC](https://news.ycombinator.com/item?id=43550770)
          Yep, it's cold outside. So there's a CO2, energy, comfort (choose two) tradeoff. ^c43550770

- **tangjurine** · [2025-03-31 00:39 UTC](https://news.ycombinator.com/item?id=43529364)
  \>For a sense of scale, Mathematica Policy Research’s best evidence on the effectiveness of the highly touted KIPP charter school network finds that after three years at KIPP there is significant improvement on three out of four test metrics — up 0.25 standard deviations on one English test, 0.22 standard deviations on another, and 0.28 standard deviations on one of two math tests. ^c43529364

  I wasn't sure what .22 std deviations meant, so I looked stuff up a bit. For a normal distribution, going from the average to 1 standard deviation above is going from the 50th percentile to the 84th percentile. Going up .22 standard deviations from the average is going from the 50th percentile to about the 55th percentile.

- **fifteenforty** · [2025-03-31 01:34 UTC](https://news.ycombinator.com/item?id=43529754)
  Also, turns out preventing kids from getting sick improves educational outcomes. ^c43529754

  - **sheepscreek** · [2025-03-31 01:45 UTC](https://news.ycombinator.com/item?id=43529835)
    My dad made a similar observation, assuming the children were young. However, upon reviewing the article, I noticed it doesn’t explicitly mention the grade level. Considering younger children have weaker immune systems, this could potentially lead to fewer missed classes and improved grades. Personally, my first grader misses out on a considerable number of classes. ^c43529835

    However, if these results were observed in grades 3 or higher, it could suggest a more substantial phenomenon. I randomly picked the third grade, but perhaps there’s a specific age after which the medical community considers a child’s immunity to be significantly enhanced.

    - **fifteenforty** · [2025-03-31 01:54 UTC](https://news.ycombinator.com/item?id=43529894)
      Ventilation and air purification have a strongly theoretical basis and there have been real-world studies showing a clear benefit. ^c43529894

      [https://cleanaircrew.org/](<https://cleanaircrew.org/>)

      [https://www.cleanairschools.com.au/](<https://www.cleanairschools.com.au/>)

    - **xwolfi** · [2025-03-31 02:17 UTC](https://news.ycombinator.com/item?id=43530071)
      But then, what about being protected from sickness from a young age, to end up sick all the time as an adult ? You had a better education, we can agree, but your body got weaker as a result and now you can't be as productive as an adult. ^c43530071

      I exaggerate a bit, but I found that during covid, where the mask was mandatory in my place, I was never sick. The only few years in my life where I was actually healthy continuously for YEARS, I and my friends could not believe the impact of the mask. But then we were stuck at home, living in constant misery and stress.

      Once the masks disappeared, finally we could live again, and got extremely sick the first few years... Maybe a more normal balance would have been better ? Sick a bit continuously ? I think trying to avoid sickness is like trying to swim against the current, nature just works that way.

      - **fifteenforty** · [2025-03-31 02:58 UTC](https://news.ycombinator.com/item?id=43530405)
        I just keep wearing an N95. I've had maybe 3 infections in 5 years. ^c43530405

      - **tehjoker** · [2025-03-31 05:35 UTC](https://news.ycombinator.com/item?id=43531461)
        getting sick is bad for us. we should clean the air. i’ve been wearing n95 indoors for years, 1 cold (neg for c19) in 5 years ^c43531461

    - **permo-w** · [2025-03-31 02:21 UTC](https://news.ycombinator.com/item?id=43530110)
      do younger children have weaker immune systems? ^c43530110

      - **LorenPechtel** · [2025-03-31 23:50 UTC](https://news.ycombinator.com/item?id=43541314)
        It's not that they are weaker, but that many things actually confer long term immunity.  The "common cold" is actually many viruses, once you've beaten one it's not likely to get you again but it's cousins will. ^c43541314

      - **Balgair** · [2025-03-31 02:37 UTC](https://news.ycombinator.com/item?id=43530242)
        Not as much as their immune systems haven't been around very long and seen as many diseases. ^c43530242

        - **permo-w** · [2025-03-31 12:24 UTC](https://news.ycombinator.com/item?id=43534164)
          I was under the impression that younger kids had stronger immune systems for that reason, which is why the common wisdom is to expose your kid to as much as possible when they're young, because it's easier for them to fight it off and later rely on resistance? ^c43534164

          - **Balgair** · [2025-03-31 13:26 UTC](https://news.ycombinator.com/item?id=43534802)
            I guess it's a quibble over the meaning of 'stronger', but that seems overly pedantic. Let's get data. ^c43534802

            A good overview of the allergy situation is here: [https://en.wikipedia.org/wiki/Hygiene\_hypothesis](<https://en.wikipedia.org/wiki/Hygiene_hypothesis>)

            Though that article goes into more about young human immune systems too. TLDR: Yeah ... it's complicated, but the evidence seems to, just maybe, lean towards more exposure being better. So, you're right, I think?

            - **permo-w** · [2025-03-31 13:56 UTC](https://news.ycombinator.com/item?id=43535125)
              the impression I got from the article is that it's a somewhat unsolved problem. the article mentions an "old friends" hypothesis that suggests that it's not exposure to dangerous pathogens that's important in childhood, but exposure to benevolent ones. but yeah, you're right, it's semantics really. kids have a different kind of strength. I would actually suggest it's quite analogous to brain development. kids are more adaptive and I'd argue creative, but adults are more experienced. ^c43535125

- **Balgair** · [2025-03-31 02:42 UTC](https://news.ycombinator.com/item?id=43530271)
  Anecdote: Our daycare was a plague ship right after covid 'ended'. None of the kids had any immunities, and they made up for it in a hurry. Man, what a terrible year. ^c43530271

  As a result, the daycare got a grant to get N-95 air filters installed and those UV lights that Chinese restaurants tend to have in the bathrooms. One per room.

  What. A. Difference.

  The infants and kids coming up are not nearly as sick, and when they do get sick, it's not nearly as terrible. The RSV vaccine has also been a godsend.

  I can't really tell/feel what what the silver bullet here, but the combinations have been amazing. So much so that we got them for the house.

  - **HPsquared** · [2025-03-31 08:48 UTC](https://news.ycombinator.com/item?id=43532697)
    I wonder how much of the improvement was due to reversion to the mean. When bringing everyone back, you would expect a sharp peak of infections which would decay to normal levels after a while - filters or not. I'm sure they do still have some positive effect though. ^c43532697

    - **Balgair** · [2025-03-31 13:29 UTC](https://news.ycombinator.com/item?id=43534830)
      Anecdotally: it was a big effect. ^c43534830

      Rigorously: no way to tell now, the time has passed.

      Likely: you're right. But what little staff is there from pre-covid says that they have helped a lot too.

      Reality: here's \$500/wk and my kid, in return I get really sick for a year no matter what.

  - **LorenPechtel** · [2025-03-31 23:47 UTC](https://news.ycombinator.com/item?id=43541289)
    What lights are you talking about?  UV capable of disinfecting isn't something you want to be looking at.  (Are you perhaps thinking of the bug-zapper lamps that are sometimes described as UV?  Way up at the top of the visual spectrum, a lot of bugs go for them.  But they're just a lure to get the bug between the high voltage wires that actually kill it.) ^c43541289

    The only disinfecting UV lights I've heard of for use in occupied areas are hanging things that only point up where nobody's going to be exposed.  I have heard of some research for safe UV lights that are high up in the UV, they actually still burn but without enough penetration to get through the dead skin layer.

  - **throwaway2037** · [2025-03-31 08:43 UTC](https://news.ycombinator.com/item?id=43532671)
    Nice story.  I can believe it.  I was surprised that you mentioned the RSV vaccine.  Last I checked, they were still working on it.  I was wrong: There are three competitors now: (1) Arexvy (GSK), (2) Abrysvo (Pfizer), and (3) Mresvia (Moderna) ^c43532671

    Ref: [https://en.wikipedia.org/wiki/Respiratory\_syncytial\_virus\_va...](<https://en.wikipedia.org/wiki/Respiratory_syncytial_virus_vaccine>)

    Normally, I use this clinic in Thailand to compare prices for vaccines: [https://www.thaitravelclinic.com/cost.html](<https://www.thaitravelclinic.com/cost.html>)

    The RSV vaccine is crazy expensive, even more than the HPV one.  Over 200 USD is incredibly expensive in a developing country (like Thailand).


    ```
        > those UV lights that Chinese restaurants tend to have in the bathrooms
    ```

    
    I never heard of this.  Does anyone have a link to one of these on Amazon or Alibaba?  I am curious to learn more.

- **craigdalton** · [2025-03-31 10:05 UTC](https://news.ycombinator.com/item?id=43533157)
  There are well established hierarchies of evidence in health studies and this study would rank as low quality evidence due to inability to control for other factors. See [https://gdt.gradepro.org/app/handbook/handbook.html\#h.3183vu...](<https://gdt.gradepro.org/app/handbook/handbook.html#h.3183vuv3ey12>) for  background. ^c43533157

  In studies of pollution and impacts on health, the confounding factors often have a larger impact on the health outcome than the pollutant, such as particulate level, and therefore significant control of confounders is required to estimate any impact on the health outcome. The strong effect in this study is highly suggestive of a confounder rather than a real effect from particles or other pollutants and therefore would require a much better study design to support tacking action at a policy level with an expectation of a huge impact.

  Fine to put filters into improve overall air quality but just not with the benefit rationale suggested in this study.

- **theoreticalmal** · [2025-03-31 02:04 UTC](https://news.ycombinator.com/item?id=43529975)
  Only marginally relevant, this is one reason I use swamp coolers in my home. My windows are open 24/7, 4 months of the year. I hear the birds in the morning and it’s so much more pleasant than shutting in an air conditioned box, in my opinion ^c43529975

  - **Mistletoe** · [2025-03-31 02:07 UTC](https://news.ycombinator.com/item?id=43529997)
    Does the humidity not cause problems?  What is the relative humidity in your home? ^c43529997

    - **SoftTalker** · [2025-03-31 02:16 UTC](https://news.ycombinator.com/item?id=43530061)
      I'd guess somewhere dry. Swamp coolers don't really work in humid climates. ^c43530061

    - **IneffablePigeon** · [2025-03-31 08:02 UTC](https://news.ycombinator.com/item?id=43532415)
      Unlikely to be a problem if the windows are open, in most climates. ^c43532415

  - **meroes** · [2025-03-31 02:18 UTC](https://news.ycombinator.com/item?id=43530086)
    Do you not get massive amounts of dust? ^c43530086

    - **mmooss** · [2025-03-31 02:31 UTC](https://news.ycombinator.com/item?id=43530191)
      Why would opening the windows result in dust, except where there a lot of dust outside (near a construction site)? ^c43530191

      - **wahnfrieden** · [2025-03-31 04:35 UTC](https://news.ycombinator.com/item?id=43531086)
        Having any roads/cars around is a major problem. Brake and tire dust. Many people live near roads and traffic. ^c43531086

      - **bluGill** · [2025-03-31 03:11 UTC](https://news.ycombinator.com/item?id=43530498)
        swamp coolers work -  imples desert - implies dust ^c43530498

- **amai** · [2025-03-31 11:04 UTC](https://news.ycombinator.com/item?id=43533545)
  Many air filters are generating annoying sounds. You get better air, but the distraction by the constant noise of the filter might be more than counter productive. ^c43533545

  - **brody\_hamer** · [2025-03-31 11:53 UTC](https://news.ycombinator.com/item?id=43533891)
    My first thought was the exact opposite. Ambient noise in classroom (from other students) can be very distracting, and I wonder if adding white noise helps kids to focus (in the same way that accoustic dampening would) ^c43533891

- **yoshuaw** · [2025-03-31 02:24 UTC](https://news.ycombinator.com/item?id=43530138)
  A study published just yesterday \[1\] showed that just two airborne diseases \[2\] were responsible for approximately 85\% of all sicks days in Greece during 2023-2024. Disregarding the common-sense argument that reducing collective suffering is a good thing overall - even by the cold hard logic of capital, being able to reduce company sick days by up to 85\% is a huge opportunity. ^c43530138

  Imo we're way overdue standards and controls for clean indoor air that are on par with standards for drinking water and food. Like this article shows, we have the tech to provide clean air today. All we're missing is policy to uniformly deploy it.

  \[1\]: [https://www.sciencedirect.com/science/article/abs/pii/S01966...](<https://www.sciencedirect.com/science/article/abs/pii/S0196655325002846>)

  \[2\]: SARS-CoV-19: \~75\% of sick days, Influenza: \~10\% of sick days

  - **socksy** · [2025-04-01 06:50 UTC](https://news.ycombinator.com/item?id=43543604)
    Might this be related to the fact that Greeks tend not to take sick days compared to other European countries\[1\]? Not coming to work because you have covid is far more culturally accepted (and maybe expected) than a common cold. ^c43543604

    \[1\]: [https://www.ekathimerini.com/economy/1255154/greek-work-ethi...](<https://www.ekathimerini.com/economy/1255154/greek-work-ethic-debunks-lazy-myth/>)

- **knotimpressed** · [2025-03-31 01:42 UTC](https://news.ycombinator.com/item?id=43529810)
  Does anyone have any details on what kind of filter this was? I bought a relatively high-MERV filter for my home, but I’m wondering what I should actually be trying to filter out. ^c43529810

  - **PaulKeeble** · [2025-03-31 01:58 UTC](https://news.ycombinator.com/item?id=43529933)
    MERV 13's are optimal for particle removal because compared to a HEPA some of the removal requires multiple passes but the filters are a lot less restrictive and allow higher airflow. Corsi and Rosenthal looked into this with the CR box and came to the conclusion its technically faster at clearing a room than using HEPA standard filters. For infections and damaging PM2.5 particles mechanical filtration with MERV13 is the best you are  going to get. ^c43529933

    You could also add potentially get a HEPA with a carbon filter which will get rid of volatile organic compounds which can also be damaging (but also just be the smell of food) but they don't tend to be as effective and depending on the mix of VOCs verses particles one filter may run out before the other and carbon really doesn't capture all that much or well. It is a good way to get rid of smell at least for a while.

    There is a whole world of different standards for filtration for industrial and hazard chemicals which the FFP2/3 and N95 standards for Personal Protective Equipment respirators will lead you into if you want to go into that rabbit hole, but for a household typically its mostlt about Particulate matter, Volatile organic compounds and CO2. CO2 is about bringing in fresh air from outside.

    Then when outside of the household N95/99 or FFP2/3 respitators do the same job in unclean air environments which is basically everywhere, outside or indoors in public places pretty much never meet the World Health Organisations levels for PM2.5 and often exceed CO2 (a proxy for re-breathing and a high change of viral infection spread) standards too.

    - **permo-w** · [2025-03-31 02:25 UTC](https://news.ycombinator.com/item?id=43530146)
      for infections you can use UVC, which is something people often overlook, although of course that has its downsides ^c43530146

  - **Aurornis** · [2025-03-31 01:54 UTC](https://news.ycombinator.com/item?id=43529895)
    The paper is here: [https://edworkingpapers.com/sites/default/files/Gilraine\_Air...](<https://edworkingpapers.com/sites/default/files/Gilraine_AirFilters_1.pdf>) ^c43529895

    I didn't see the model specified. They also said some schools got carbon filters, which is a different type of filter.

    There's footnote saying many filters weren't even installed because some teachers thought they made the air "too dry", which is major placebo effect at work (air purifiers don't extract moisture from the air).

    The entire paper is really not good quality, to be honest.

    You can get a small HEPA purifier for a single room to remove particulates. The size of the filter, noise level, and amount of air moved are things to look for. Stepping up to activated carbon would remove VOCs, but cost significantly more (see IQAir, Austin Air, but ignore the cheap models that don't have 10-20lbs or more of activated carbon).

  - **fifteenforty** · [2025-03-31 01:56 UTC](https://news.ycombinator.com/item?id=43529916)
    Higher does not necessarily mean better. Higher grade filters filter more in each pass, but can overall provide worse performance as the air flow rate goes down. The air is being recirculated in a portable unit or in a standard domestic ducted heating/cooling situation. ^c43529916

- **dang** · [2025-03-31 04:38 UTC](https://news.ycombinator.com/item?id=43531108)
  Related. Others? ^c43531108

  *A review of the effects of installing air filters in classrooms* \- [https://news.ycombinator.com/item?id\=22006595](<https://news.ycombinator.com/item?id=22006595>) \- Jan 2020 (26 comments)

  *Installing air filters in classrooms has large educational benefits?* \- [https://news.ycombinator.com/item?id\=22006033](<https://news.ycombinator.com/item?id=22006033>) \- Jan 2020 (48 comments)

- **PaulKeeble** · [2025-03-31 02:02 UTC](https://news.ycombinator.com/item?id=43529961)
  There have been some classroom studies in the UK showing a reduction in illness as well. They were a bit better run than this because they had some some pupils in filtered air and some not and even with the mixing at break time the reduction of illness met clinical significance. Given Covid is doing its thing all year around its quite an easy thing to do to drastically reduce the time teachers and pupils spend away from school and its a fairly easy measure to adopt. They do need to have the filters running however and that will involve explaining to the teachers how they work and why they are needed because in a lot of studies compliance has been a big issue usually due to misinformation rather than issues with the devices. ^c43529961

- **joeevans1000** · [2025-03-31 07:15 UTC](https://news.ycombinator.com/item?id=43532099)
  i'm sure it's because they were white noise generators essentially. ^c43532099

- **culopatin** · [2025-03-31 22:47 UTC](https://news.ycombinator.com/item?id=43540798)
  I wonder how smart I’d be if I didn’t sit in a classroom full of metal tables that got painted with such a thick layer of oil paint that it stunk of paint thinner until Spring ^c43540798

  - **LorenPechtel** · [2025-03-31 23:04 UTC](https://news.ycombinator.com/item?id=43540953)
    Yeah, I got driven out of college by one bad building.  (This was back before it was understood that a building can be a problem.)  I simply couldn't think properly while in it.  A problem with classes, a showstopper when the labs were in the building.  I'm sure I would have flunked out if I had tried to take those classes.  I have no idea what I was reacting to but there sure was something.  (It felt a lot like one house where I had the same sense of something bad walking in the door--and long later a wall full of black mold was discovered.) ^c43540953

- **tehjoker** · [2025-03-31 05:31 UTC](https://news.ycombinator.com/item?id=43531438)
  Given that SARS2 affects cognition negatively, I would expect schools with universal air filtration to have larger improvements than we would have expected prior. ^c43531438

- **Animats** · [2025-03-31 07:47 UTC](https://news.ycombinator.com/item?id=43532289)
  What are they "filtering"? You can filter particulates, but methane removal is more complicated. ^c43532289

- **MemexXx** · [2025-03-31 08:45 UTC](https://news.ycombinator.com/item?id=43532683)
  Now let's see if the filters are not changed in a while, and how that effects the studies (not on purpose, I'm guessing that the upkeep is not very good with filters in general) ^c43532683

- **acstorage** · [2025-03-31 03:14 UTC](https://news.ycombinator.com/item?id=43530513)
  Makes sense ^c43530513

- **throwaway81523** · [2025-03-31 02:46 UTC](https://news.ycombinator.com/item?id=43530315)
  From 2020. ^c43530315

- **yimby2001** · [2025-03-31 01:35 UTC](https://news.ycombinator.com/item?id=43529760)
  [flagged] ^c43529760

  \[dead\]

- **ribcage** · [2025-03-31 07:55 UTC](https://news.ycombinator.com/item?id=43532340)
  [flagged] ^c43532340

  \[dead\]

- **unknown** · [2025-03-31 03:48 UTC](https://news.ycombinator.com/item?id=43530740)
  [deleted] ^c43530740

- **aaron695** · [2025-03-31 07:57 UTC](https://news.ycombinator.com/item?id=43532364)
  [flagged] ^c43532364

  \[dead\]

- **hollerith** · [2025-03-31 02:01 UTC](https://news.ycombinator.com/item?id=43529951)
  Install air filters in classrooms *in Los Angeles* has. ^c43529951

  Places with clean outdoor air probably won't see much benefit.

  - **sebastiennight** · [2025-03-31 03:58 UTC](https://news.ycombinator.com/item?id=43530811)
    Which begs the question. How many of those places are there, and how many large groups of humans with children would you believe live in such places? ^c43530811

