# [Air pollution linked to “huge” reduction in intelligence](https://news.ycombinator.com/item?id=18219391)

Article: [https://www.unenvironment.org/news-and-stories/story/air-pollution-linked-huge-reduction-intelligence](<https://www.unenvironment.org/news-and-stories/story/air-pollution-linked-huge-reduction-intelligence>)

crunchiebones · 2018-10-15 13:17 UTC · 175 reported comments · archived 2026-11-08 10:53 UTC
Observation: 2026-11-08 10:52 UTC → 2026-11-08 10:53 UTC

## Comments

- **19h** · [2018-10-15 14:45 UTC](https://news.ycombinator.com/item?id=18220088)
  The actual study \[1\] isn't as much clickbait: ^c18220088

  \> We find that long-term exposure to air pollution impedes cognitive performance in verbal and math tests.

  \> We provide evidence that the effect of air pollution on verbal tests becomes more pronounced as people age, especially for men and the less educated.

  \> The damage on the aging brain by air pollution likely imposes substantial health and economic costs, considering that cognitive functioning is critical for the elderly for both running daily errands and making high-stake decisions.

  \[1\] [http://www.pnas.org/content/early/2018/08/21/1809474115](<http://www.pnas.org/content/early/2018/08/21/1809474115>)

- **asaph** · [2018-10-15 14:37 UTC](https://news.ycombinator.com/item?id=18220011)
  In case anyone else wanted to quantify "huge": ^c18220011

  \> “Polluted air can cause everyone to reduce their level of education by one year, which is huge,” Yale School of Public Health's Professor Xi Chen, one of the report's authors, said in an interview published in The Guardian.\[0\]

  \[0\] [https://www.unenvironment.org/news-and-stories/story/air-pol...](<https://www.unenvironment.org/news-and-stories/story/air-pollution-linked-huge-reduction-intelligence>)

  - **Bartweiss** · [2018-10-15 16:48 UTC](https://news.ycombinator.com/item?id=18221332)
    I'm glad Chen attempted to give an intelligible quantity, but I'm not really sure what to make of the metric. "Years of education" don't seem like an intuitive metric for cognitive impairment. Checking the abstract gets us: ^c18221332

    \> *Cutting annual mean concentration of particulate matter smaller than 10 μm (PM10) in China to the Environmental Protection Agency’s standard (50 μg/m3) would move people from the median to the 63rd percentile (verbal test scores) and the 58th percentile (math test scores), respectively.*

    For reference, another study in China found that top-decile levels of lead poisoning (\>10 micrograms per deciliter) cost children about two points of IQ on both math and verbal scales. That's not trivially convertible to percentile performance, and I don't know whether air pollution has long-tail effects anything like the horrible long-tail on lead poisoning.

    But it does suggest that particulate pollution has effects on the same general scale as childhood lead poisoning, which is pretty striking.

    Underlying study is here: [http://www.pnas.org/content/early/2018/08/21/1809474115](<http://www.pnas.org/content/early/2018/08/21/1809474115>)

    Lead study is here:
    [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3667072/](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3667072/>)

    - **ip26** · [2018-10-15 18:56 UTC](https://news.ycombinator.com/item?id=18222587)
      "So-and-so third grader reads & does math at a second grade level" is about the most intuitive metric we've got. ^c18222587

      - **Bartweiss** · [2018-10-15 19:41 UTC](https://news.ycombinator.com/item?id=18222997)
        It's a very easy way to talk about childhood progression under compulsory education, yes. But if not everyone is in school then I don't know whether "losing a year" means losing the schooling, or losing the year of development. ^c18222997

        More crucially, the main result here was about older adults losing capacities. If someone tells me that a 70 year old dementia patient has effectively "lost a year of education", I don't have any idea what I should expect.

        - **trobertson** · [2018-10-16 08:43 UTC](https://news.ycombinator.com/item?id=18227739)
          You might consider other metrics, like the school grade level that most journalistic entities write for. In the USA, it used to be that most journalists wrote towards a 5th grade reading ability. Assuming that the article is correct, then many journalists who sell to air-pollutant-exposed people (which is most people) should be targeting a 4th grade reading ability, perhaps even lower. ^c18227739

          On a wild tangent, there has been a huge increase in clickbait over the past several years.

          - **Bartweiss** · [2018-10-16 18:20 UTC](https://news.ycombinator.com/item?id=18231784)
            This got me curious: are most Americans exposed to these pollutants at a meaningful level? ^c18231784

            In short: no.

            In long:

            This study was done in China, and asked "what would happen if we lowered 10 micron particulate pollution levels to the US EPA standard?" Air pollution in China is substantially worse than in the US, and 10 micron particulates (PM10) are one of the largest points of divergence: China relies heavily on unfiltered coal burning for electricity, as well as conducting mining and road construction with minimal particulate control.

            Unfortunately I can't get the API data appendix for the study, and the paper's figures are functions of mean API, but the data shouldn't be paper specific. All sources I can find agree: fine particulate pollution levels in China are *horrifying*. Almost all of China is consistently exposed to more than 40 micrograms per cubic meter of PM10 particulates, and urban centers are consistently much higher. Recent progress has lowered average rates in many cities into the 40-100 microgram window, but in 2010 annual average rates commonly exceeded 150 micrograms, which is the *acute* (24 hour) threshold set by the EPA.

            The benchmark value in the study was 50 micrograms per cubic meter, which was (until 2006, when the standard was scrapped), the EPA's safe limit for annual average exposure. In America, across several hundred sites monitored in 2017, zero exceeded 100 micrograms, only four exceeded the 50 microgram threshold, and only twelve exceeded 40 micrograms. For 2016, those numbers are zero, four, and ten. The hardest-hit sites are all in the Southwestern US, which suffers from both dust and wildfire particulate matter frequently.

            Further, not all PM10 particulates are created equal. They're grouped in a single number because the usual focus of concern is inhalation leading to lung problems, but when discussing cognitive effects they're almost certainly not equivalent. In particular, PM2.5 (2.5 micron particles) are a subset of PM10, and are both more likely to enter the bloodstream and more likely to be bioactive substances like metal, organics, or soot. Particulates between 2.5 and 10 microns are more likely to be dust, pollen, or ash - damaging to lungs, but much less likely to cause systemic harm. This study did admirable work controlling for or disproving confounders - I'm genuinely very impressed by how well they covered that base. But the PM10/PM2.5 conflation was inescapable since PM2.5 is a subset of the variable and wasn't measured separately.

            (The study relied on an Air Pollution Index observing sulfur dioxide, nitrogen dioxide, and PM10, with the value controlled by the highest subfactor. From the references exclusively to PM10 and from China's other data, I assume that it was consistently the dominant factor, as it is in the US, but if it correlates with the other factors then one of them could potentially drive the effect. Nevertheless, SO2 and NO2 are essentially acute-only problems in the US, with average rates well below EPA thresholds.)

            The highest-PM10 sites in the US look prone to dust and ash pollutants, and indeed checking the data says that their PM2.5 levels, while high, trend linearly up from other sites while their PM10 levels rise exponentially. The worst PM10 sites have PM2.5:PM10 ratios of around 20\%. The highest PM2.5:PM10 ratios are between 50\% and 70\%. These are predictably found in industrial Rust Belt cities like Dearborn and Steubenville, but the total levels are still relatively low. 13 cities exceeded the annual EPA standard of 12 micrograms, and none exceeded 17 micrograms. 21 cities had 98th percentile rates in excess of the EPA daily standard of 35 micrograms; excluding outlier Phoenix (146 micrograms) the highest was 67 micrograms.

            Meanwhile, China's PM2.5 rates have only recently been measured, but are terrifyingly high. China sets 0-35 micrograms as a Grade I success and 35-75 micrograms as Grade II success. Wuhan, selected as an average Chinese city for a study in 2013, exceeded the Grade II standard 75\% of the time, and exceeded 150 micrograms (which, again, is the *acute PM10* threshold!) 25\% of the time. National samples show all cities profiled have PM2.5:PM10 ratios above 50\%, and some exceed 80\%. Most days in most cities in China, the PM2.5 level is higher than the highest observed rates for any site in the US except Phoenix.

            Where does this leave us? China's PM10 rates are vastly higher than the worst American rates. China's PM2.5 rates, which are likely more relevant, are even more divergent. Annual NO2 and SO2 rates in the US are insignificant. The available evidence suggests that under any plausible shape for this effect - linear or exponential, threshold or LNT - its effects would be immeasurable anywhere in the US except perhaps 2-3 weakly affected cities. In all cases, other known impairing pollutants like carbon monoxide would be far more impactful.

            This has been quite a tangent, but overall it's increased my appreciation for this study, while leading me to believe this result is basically irrelevant to US analyses.

            - **trobertson** · [2018-10-17 01:22 UTC](https://news.ycombinator.com/item?id=18234809)
              I imagine most people aren't going to read that whole comment, but I did. Thanks for the write up, and for showing that my knee-jerk interpretation was incorrect. ^c18234809

              - **Bartweiss** · [2018-10-17 14:48 UTC](https://news.ycombinator.com/item?id=18239589)
                Hey, I'm glad someone did! ^c18239589

                You offered an interesting thought, and I couldn't find anybody actually taking on "how does this compare to USA data?", so it was as much to settle my own curiosity as anything.

    - **r00fus** · [2018-10-15 17:28 UTC](https://news.ycombinator.com/item?id=18221698)
      I'd say that a "year of education" is a lot more quantifiable to your average person than "2 points of IQ". ^c18221698

      IQ isn't used for anything meaningful in terms of ability or qualifications, especially since it's age-adjusted and historically has been biased against minorities/foreigners.  A year of development however, is a graspable (if shocking) measure of lost opportunity/capability.

      - **Bartweiss** · [2018-10-15 19:35 UTC](https://news.ycombinator.com/item?id=18222942)
        How does "losing a year of education" relate to my ability to decide and remember which errands I need to do in what order? If people lose 'a year', how does that respond to varying levels of education? Are they losing a year of *education*, as in quitting school to work, or a year of *development*, as in comparing 15 year olds to 16 year olds? The two are substantially different, and seeing them conflated makes me think I'm not the only one confused. ^c18222942

        I have no idea at all. I'm not trying to be snarky, I completely failed to grasp what's being lost until I went and looked at the paper.

        A year of education is certainly quantifiable when we're talking about learned facts and skills, or even about economic success, but I don't understand it as a measure of cognitive impairment. The studied harms should still be relevant to a farmer who's never spent a single day in a classroom, and the analysis in the study focuses on older adults losing fundamental capacities that are important to decision-making and daily functioning. Using a metric that's based on education doesn't clearly convey losses like that, especially when we're talking about not missed advancement in children but decline in older adults.

        The actual result obtained in this study was performance on a set of scores on verbal and mathematical tests relative to a population average. The result in the lead study was a set of verbal and mathematical tests relative to a population average. Expressing one as percentiles and the other as IQ doesn't change the fact that those things are far more similar to each other than either is to keeping children in school for an extra year.

        (On a final note, I don't want to open the IQ debate, but I do think the usual problems are uncommonly irrelevant here. I specifically pulled a lead study which was conducted in China, used a Chinese baseline, and compared among same-age children, which avoids the biases mentioned. IQ may be a terrible general comparison, but if we don't need to compare between samples in different studies then it's really just a percentile.)

      - **pavelrub** · [2018-10-15 19:17 UTC](https://news.ycombinator.com/item?id=18222772)
        I disagree. "A year of education" is mostly about gaining knowledge. It's obvious that air pullution can't possibly make you forget one year of such knowledge, and I have no idea in what other intuitive way this can be interpreted that makes any sense to the average person. If it's meaningfull to someone then it's only because he understood it wrongly. ^c18222772

        - **yorwba** · [2018-10-15 21:14 UTC](https://news.ycombinator.com/item?id=18223826)
          \> It's obvious that air pullution can't possibly make you forget one year of such knowledge, ^c18223826

          Is it? What people remember of one year of education is probably very little to begin with and it only gets less over time; it doesn't seem unbelievable that pollution could cause those memories to decay faster.

          - **pavelrub** · [2018-10-16 06:49 UTC](https://news.ycombinator.com/item?id=18227201)
            Well if that seems plausible to you then it's only further proof of how misleading the wording is, as the actual study makes no claims about people forgetting a year of education. ^c18227201

      - **SketchySeaBeast** · [2018-10-15 17:33 UTC](https://news.ycombinator.com/item?id=18221735)
        I hope it's a year of my art degree.  2nd year didn't teach me a lot. ^c18221735

      - **aero142** · [2018-10-15 18:55 UTC](https://news.ycombinator.com/item?id=18222584)
        Yes, but I'm confused about the truthfulness of the statement.  Is it true that an additional year of education is equivalent to 2 points of IQ? ^c18222584

        - **jcranmer** · [2018-10-16 00:18 UTC](https://news.ycombinator.com/item?id=18225333)
          The original IQ tests were used to gauge what was termed "mental age", what age you were functionally acting at, and was a ratio of your mental age over your chronological age times 100--a ten year old working at an eleven-year old's level had an IQ of 110. ^c18225333

          That said, modern IQ doesn't use that definition, and all of the material you can easily find on the matter pretends that it does. Instead, IQ is a normalized bell curve, every 15 points is another standard deviation on the bell curve. Given that definition, a year's worth of education is probably guesstimated at roughly one standard deviation of IQ. This comes with the massive caveat that IQ and educational achievement can't be compared in that manner (since one is an absolute scale and the other is definitionally a statistical artifact).

  - **Bartweiss** · [2018-10-16 18:32 UTC](https://news.ycombinator.com/item?id=18231916)
    And to quantify pollution: the study looks at reducing 10 micron particulate pollution in China down to the EPA-approved limits, which almost all US cities are already below, and which Chinese cities are often 2-3 times above. ^c18231916

    I tried to take a serious stab at "what does this mean for air in the US?", and my best conclusion is "probably almost nothing". The full notes are here: [https://news.ycombinator.com/item?id\=18231784](<https://news.ycombinator.com/item?id=18231784>)

  - **tw1010** · [2018-10-15 16:37 UTC](https://news.ycombinator.com/item?id=18221188)
    My experience with some PhDs would suggest too much schooling might have the opposite effect... ^c18221188

- **Reason077** · [2018-10-15 14:44 UTC](https://news.ycombinator.com/item?id=18220085)
  Electrification of surface transport is the most obvious way to improve air quality in dense cities. This needs to be a priority. ^c18220085

  - **michaelbuckbee** · [2018-10-15 14:55 UTC](https://news.ycombinator.com/item?id=18220187)
    China is putting \~10k electric buses a month on the road: ^c18220187

    [https://www.weforum.org/agenda/2018/04/china-is-adding-a-lon...](<https://www.weforum.org/agenda/2018/04/china-is-adding-a-london-sized-electric-bus-fleet-every-five-weeks/>)

    - **baud147258** · [2018-10-15 15:23 UTC](https://news.ycombinator.com/item?id=18220445)
      And they are still using coal to produce electricity. ^c18220445

      - **Bartweiss** · [2018-10-15 16:55 UTC](https://news.ycombinator.com/item?id=18221396)
        This is probably still a positive change on several levels. Plants can be remediated better than vehicles, electrification delinks generation from use to ease later greening, and for particulate pollution (unlike CO2) moving emissions away from population centers is meaningful. ^c18221396

        That said... yes. Electrification is a massive improvement in the US, Canada, and Western Europe, but much less useful in Russia, China, and much of SE Asia. Adding to that, pushing pollution sources away from cities reinforces the demographic crisis China has had brewing for a long time, with everything from lead to lack of iodine creating serious permanent health issues in rural regions.

      - **aqme28** · [2018-10-15 15:43 UTC](https://news.ycombinator.com/item?id=18220626)
        That's a separate problem. If/when they switch to renewable plants, then they'll already have an electric bus fleet to take advantage of that. ^c18220626

      - **radium3d** · [2018-10-15 15:40 UTC](https://news.ycombinator.com/item?id=18220599)
        This World Resources Institute graph\^1 shows intense growth in solar electricity generation in China so they are at least moving away from fossil fuel electricity generation at a rapid pace and fossil fuel electricity generation is plateauing\^0
        \[0\] [https://en.wikipedia.org/wiki/Electricity\_sector\_in\_China\#/m...](<https://en.wikipedia.org/wiki/Electricity_sector_in_China#/media/File:Electricity_Production_in_China.png>)
        \[1\] [https://www.wri.org/blog/2018/08/distributed-solar-pv-china-...](<https://www.wri.org/blog/2018/08/distributed-solar-pv-china-growth-and-challenges>) ^c18220599

        - **adventured** · [2018-10-15 18:37 UTC](https://news.ycombinator.com/item?id=18222405)
          China is in fact not moving away from fossil fuels, they're aggressively expanding their fossil fuel use. They're adding a minority of renewable energy into the mix of their new energy demand, while building a very large number of new coal plants. They're very openly lying about their environmental efforts. They're also aggressively using their state companies to build coal plants external of their borders. ^c18222405

          This is the same tactic they use on trade. They're hyper protectionist about access to their economy, and then claim they're free traders.

          "China's leading role in financing a wave of new coal plants across Asia is drawing fresh scrutiny as the world’s top climate scientists weigh calling for much deeper cuts in emissions. China, India, Japan and the Philippines rank among the biggest investors in the 1,380 coal plants under construction or development worldwide, according to a study by the German pressure group Urgewald released Thursday."

          [https://www.bloomberg.com/news/articles/2018-10-04/china-s-f...](<https://www.bloomberg.com/news/articles/2018-10-04/china-s-funding-for-coal-draws-scrutiny-as-climate-concern-grows>)

          "The research, carried out by green campaigners CoalSwarm, suggests that 259 gigawatts of new capacity are under development in China. The authors say this is the same capacity to produce electricity as the entire US coal fleet. The report says that at present China has 993 gigawatts of coal power capacity, but the approved new plants would increase this by 25\%."

          [https://www.bbc.com/news/science-environment-45640706](<https://www.bbc.com/news/science-environment-45640706>)

          [https://www.nytimes.com/2017/07/01/climate/china-energy-comp...](<https://www.nytimes.com/2017/07/01/climate/china-energy-companies-coal-plants-climate-change.html>)

          [https://www.vox.com/energy-and-environment/2018/6/6/17427030...](<https://www.vox.com/energy-and-environment/2018/6/6/17427030/coal-plants-map-china-india-us-eu>)

          [https://www.cnbc.com/2018/04/06/china-is-massively-betting-o...](<https://www.cnbc.com/2018/04/06/china-is-massively-betting-on-coal-outside-its-shores--even-as-investment-falls-globally.html>)

        - **yorwba** · [2018-10-15 21:21 UTC](https://news.ycombinator.com/item?id=18223890)
          \> fossil fuel electricity generation is plateauing\^0 ^c18223890

          The graph you linked mostly shows exponential growth, with a slowdown in the last measured year. But similar kinks are visible twice before, with growth continuing at the same pace afterwards. I wouldn't call that "plateauing".

          - **radium3d** · [2018-10-19 17:08 UTC](https://news.ycombinator.com/item?id=18258165)
            Well, there is another factor, the actual push to renewable energy sources and the fact that the cost of the next trillion watts of renewable energy will cost half the first [https://www.bloomberg.com/news/articles/2018-08-02/green-ene...](<https://www.bloomberg.com/news/articles/2018-08-02/green-energy-capacity-passes-a-trillion-watts>) ^c18258165

      - **Taniwha** · [2018-10-15 18:35 UTC](https://news.ycombinator.com/item?id=18222367)
        I flew across China earlier this year, and saw thousands and thousands of windmills that weren't there a few years ago, many had been built around open cast coal mines (and power plants), obviously they're planning on replacing the coal with wind and reusing the sunk-cost transmission lines ^c18222367

      - **nerdponx** · [2018-10-15 16:45 UTC](https://news.ycombinator.com/item?id=18221288)
        From a pollution perspective, is it better to have 1 coal plant generating electricity for an electric bus fleet, or to have a fleet of buses that run on hybrid-electric diesel or CNG? ^c18221288

        - **WhompingWindows** · [2018-10-15 17:59 UTC](https://news.ycombinator.com/item?id=18222007)
          It's not a simple calculation. It depends whose numbers you use for the calculation. First off, do you only care about CO2, or are you interested in other by products of coal consumption like NOx? Which kind of coal plant, how efficient is it? What kind of coal is in use? Then, on the consumption side, it depends on your electric busses' efficiency, leakage of CNG into methane emissions, honestly there are too many specific parameters left unspecified in your question. ^c18222007

        - **Gibbon1** · [2018-10-15 18:25 UTC](https://news.ycombinator.com/item?id=18222252)
          An electric bus doesn't produce particulates and NOx right where people live and work. So it has the least effect on local air pollution. ^c18222252

          CNG is at least way better than diesel.

          If you have to use fossil fuels a combined cycle natural gas plant generating electricity and electric buses is your best option.

          That said I tend to discount arguments that compare things to coal since coal just needs to go away.

        - **Reason077** · [2018-10-15 17:28 UTC](https://news.ycombinator.com/item?id=18221697)
          Diesel busses stink and pollute no matter what - even the modern hybrid ones. I can tell you that as a Londoner! ^c18221697

          Natural gas might be better, but for whatever reason it’s never taken off here. Seems like electric is the way things are going.

        - **unknown** · [2018-10-15 17:28 UTC](https://news.ycombinator.com/item?id=18221691)
          [deleted] ^c18221691

      - **unknown** · [2018-10-15 15:52 UTC](https://news.ycombinator.com/item?id=18220707)
        [deleted] ^c18220707

      - **i88y6** · [2018-10-15 18:58 UTC](https://news.ycombinator.com/item?id=18222616)
        Just like the US ^c18222616

  - **jesstaa** · [2018-10-15 15:10 UTC](https://news.ycombinator.com/item?id=18220333)
    human powered transport like walking or cycling works great in dense cities, it's more space efficient so it scales better too. ^c18220333

    - **twelvechairs** · [2018-10-15 15:28 UTC](https://news.ycombinator.com/item?id=18220486)
      Plus it provides health benefits! ^c18220486

      Its not for everyone in every big city but certainly the Dutch model of transitioning cities from cars to transit and pedestrian/cycle focus is probably the clearest model for sustainable and healthy tansport out there.

      - **medoed** · [2018-10-15 16:02 UTC](https://news.ycombinator.com/item?id=18220848)
        I live in the Netherlands  and I can confirm that. In just a couple of decades they transformed all their car friendly cities and made cars second rate citizens ^c18220848

        Cycling infrastructure is amazing. It is almost always faster to travel by bike than by car.

        They did it so long ago and the world still hasn’t caught up. I’m very sad about that.

        Also somehow the amount of cars per capita is still very high in NL.

        - **InitialLastName** · [2018-10-15 16:52 UTC](https://news.ycombinator.com/item?id=18221367)
          \> Also somehow the amount of cars per capita is still very high in NL. ^c18221367

          That's OK.  We can keep up the consumerist "Everybody needs a car" mentality as long as the amount of driving per capita stays low.

          - **SahAssar** · [2018-10-15 18:50 UTC](https://news.ycombinator.com/item?id=18222524)
            The manufacturing of a car still consumes a lot of resources and lets out a lot of CO2 though, right? ^c18222524

            - **pcthrowaway** · [2018-10-16 07:38 UTC](https://news.ycombinator.com/item?id=18227424)
              A good alternative to this is carsharing. Lots of people in Vancouver don't own a car, they just take one from one of the 5 car-shares when they need one ^c18227424

          - **Reason077** · [2018-10-16 11:25 UTC](https://news.ycombinator.com/item?id=18228376)
            Parked cars take up a lot of space in city centres that could be used more productively. ^c18228376

        - **SuddsMcDuff** · [2018-10-15 16:41 UTC](https://news.ycombinator.com/item?id=18221237)
          How big of a problem is bike theft in the Netherlands? ^c18221237

          I live in the UK and I probably wouldn't consider getting a bike again, simply because I know it would be nicked within a month.

          - **medoed** · [2018-10-15 17:37 UTC](https://news.ycombinator.com/item?id=18221780)
            Pretty common in big cities. That's why everyone in Amsterdam rides cheap old omafietsen ("granny bikes") with huge locks that often cost more than the bike itself. ^c18221780

            I personally had 4 bikes stolen in 5 years.

          - **rixed** · [2018-10-15 16:57 UTC](https://news.ycombinator.com/item?id=18221419)
            Not so bigi would say. Lived \~3 years in Amsterdam with an average bike always loosely locked in the street and it has never been stolen.
            But to be honest, poverty in NL is also a problem that's been managed quite well ; which does not mean there is no crime (I've had 3 burglary attempts) but maybe crimes that paya bit more than stealing average bikes in the street. ^c18221419

    - **rcMgD2BwE72F** · [2018-10-15 15:29 UTC](https://news.ycombinator.com/item?id=18220492)
      Oh yes. As a Parisian and a big supporter of the electrification of all terrestrial transportation, I want as few EVs as city as possible. Cars simply don't make sense in dense cities (bikes do). ^c18220492

      - **justinator** · [2018-10-15 16:30 UTC](https://news.ycombinator.com/item?id=18221127)
        I lived in Paris for a spell, and one of the great things about the city is that it *is* so bike-able. It's not a large place! And it's dense. Lots of traffic, but the French seem to understand that bikes belong. ^c18221127

        We almost never used the Métro, what was the point? Saved money and no one ever stole my wallet!

        - **rcMgD2BwE72F** · [2018-10-17 12:20 UTC](https://news.ycombinator.com/item?id=18238229)
          I take my vélo at least twice a day (to commute) and I still find it far more distressing than taking the bus/métro. No wonder why so few people rides bikes, expect on the week-ends: with all the big petrol cars and aggresive motorbikes, it is still pretty dangerous to ride and not (yet) agreeable. But things are improving so I'm optimist and resigned. ^c18238229

    - **astrostl** · [2018-10-16 15:58 UTC](https://news.ycombinator.com/item?id=18230408)
      Related to the OP, I anecdotally have an acquaintance that is a bike messenger in the UK, who second-hand anecdotally reports that everyone who does it is an ostensible model of fitness until they 1) get hit by a car or 2) die at 50 of lung disease. There's a chicken/egg thing with regard to non-vehicle transport in that you're more directly exposed to exhaust, and aspirating it more quickly because of exercise. Which exacerbates the negative impact of pollution, which puts you back in a vehicle, which increases pollution :-/ ^c18230408

    - **wowzap** · [2018-10-15 15:24 UTC](https://news.ycombinator.com/item?id=18220453)
      Is there actually proof that it "works great"? Asking for myself every time I try to cross the street in downtown Manhattan and have to look for a cyclist on the sidewalk, going against traffic, blowing through a red light, or fighting with another cyclist. ^c18220453

      - **rcMgD2BwE72F** · [2018-10-15 15:48 UTC](https://news.ycombinator.com/item?id=18220668)
        A city that was never designed for bikes is hell for bikes, so you end up with only the most reckless bikers on the road. ^c18220668

        I commute with a bike every day in Paris, France. The infrastructure isn't great but it's OK, and it's improving. The thing is: I'm a big, strong guy who can legally outrun most cars and motorbikes in such a big, dense city. I can fight my way in traffic, mostly because the law authorizes bikes to go both ways in most streets, to run red lights [https://en.wikipedia.org/wiki/Idaho\_stop](<https://en.wikipedia.org/wiki/Idaho_stop>), to ride between traffic lanes, etc. Most people are terrified to ride here so you only have the most reckless persons on bikes, including me. Although I'm respect the law (which does not make riding safe because no one wants to be anywhere near a big bus/truck, or between vehicles, or stuck in a diesel tailpipe…), I end up riding dangerously making people think that biking is *only* for reckless guys.

        The worst is that, the more I respect the law, the more drivers get angry at me for taking to much space or slowing traffic down. So you move as quick and close as possible to vehicles and pedestrians. That's absurd but that how it is.

        It's an infrastructure problem. The more you give space to bikes, the more reckless bikers can finally ride prudently, or prudent people dare to ride (making reckless bikers a tiny minority). It's the same with cars: what would happen if the infrastructure made car driving dangerous? You would only have road hogs and people would just hate cars.

        - **stupidcar** · [2018-10-15 19:18 UTC](https://news.ycombinator.com/item?id=18222786)
          I definitely agree about the last part. I live in London, don’t drive, and cycling would definitely be preferable to relying entirely on the Tube and taxis. But when I see the hell cyclists here have to contend with, and how aggressive they need to be, I know there’s no way I am a skilled or confident enough rider to do the same. But if the infrastructure and vehicle congestion ever improved to the point where cyclists were adequately protected, I would definitely start cycling. ^c18222786

          - **Reason077** · [2018-10-16 11:32 UTC](https://news.ycombinator.com/item?id=18228421)
            Compared to many cities, London is actually pretty good for cycling now days, at least in central areas. We’re no Amsterdam, but there are some high-quality dedicated cycling routes and plenty of quiet side streets to use. Traffic speeds are relatively low and the vast majority of drivers are considerate and cycle-aware (occasional white-van idiots aside...) ^c18228421

        - **justinator** · [2018-10-15 16:33 UTC](https://news.ycombinator.com/item?id=18221163)
          I think I rode a taxi in Paris once or twice, but never a private car - and none of our friends had private cars, either. I assumed parking was a nightmare, and expensive. The narrow medieval roads didn't help, either. Many of the streets around our apartment were closed to cars (at least on Sunday). ^c18221163

          Being a cyclist, I thought I found a slice of heaven. I thought about being an urban planner when I got back to the States.

          - **rcMgD2BwE72F** · [2018-10-17 12:16 UTC](https://news.ycombinator.com/item?id=18238201)
            \>I assumed parking was a nightmare, and expensive. ^c18238201

            I've been a car driver and a cyclist there for \~10 years now. Believe me, being the former is much easier than the latter. If you're on a bike, many assume you're just having a good time (either on vacation or unemployed, as many people says) so the politicians/police/media won't care about your well being and focus instead of the transportation means of "serious people", i.e cars and motorbikes.

            It's insulting, because I do have a car (and a parking spot) but everything pushes me to drive it instead of riding my vélo (which makes no noise, does not emit anything, takes very little space, doesn't damage the road, is far less dangerous to others, makes me fit and save health insurance costs...). Go figure.

    - **trhway** · [2018-10-15 15:37 UTC](https://news.ycombinator.com/item?id=18220572)
      cycling isn't space efficient and doesn't really scales that good. It is a luxury ttransportation mode for low/mid density US cities not capable/not willing to build true mass transit modes. Look at the packed subway in say Moscow ([https://www.youtube.com/watch?v\=GCZKXHsZo68](<https://www.youtube.com/watch?v=GCZKXHsZo68>)) and compare to the best possible bicycle situation - mid-80s China [http://www.theurbancountry.com/wp-content/uploads/2013/02/83...](<http://www.theurbancountry.com/wp-content/uploads/2013/02/83.jpg>) \- around 10 times density difference :) Take that photo, cut 1/5th in height (2-3 abreast) and put large distance between very enthusiastic riders (incl. speeding electrics) - such modern bike lane shows very low efficiency of space utilization/bandwidth and very insufficient capacity to move any significant number of commuting bodies. ^c18220572

      - **ben\_w** · [2018-10-15 16:06 UTC](https://news.ycombinator.com/item?id=18220889)
        Cycling is at least four times the space efficiency of cars, unless all the cars are Smart Fourtwo or equivalent. And that’s when parked, the multiplier goes up with speed. ^c18220889

        Additionally, low density US cities are one of the worst places I’ve seen for cycling, because not only is everything spread out, but also the multi-lane roads everywhere make it much more dangerous than equivalently populated towns and cities in Europe. Despite having cycled through central London (UK) and just over 1,000 km along the Rhine, there’s no way you’d see me cycling around Salt Lake City or Sacramento. I’ve cycled around Davis (CA), but Davis has better than US average cycling infrastructure — almost as good as the average level in the UK.

        - **rienbdj** · [2018-10-15 16:24 UTC](https://news.ycombinator.com/item?id=18221084)
          wow, I was using London as an example of how NOT to do cycle infrastructure. ^c18221084

          - **Reason077** · [2018-10-15 17:21 UTC](https://news.ycombinator.com/item?id=18221638)
            London is getting there, slowly! There are some excellent examples of well-designed, well-used cycle infrastructure such as the new(ish) Cycle Superhighway along the Thames Embankment. This will hopefully serve as a model for future infrastructure. ^c18221638

            In general, traffic speeds are low in London and there are lots of quiet side routes that are well suited to cycling. We’re no Amsterdam, but cycling is certainly much more popular and visible than it was 5-10 years ago.

          - **ben\_w** · [2018-10-15 20:18 UTC](https://news.ycombinator.com/item?id=18223298)
            London is unpleasant and stressful, but as Reason077 says, traffic is slow. Compared to the American cities I’ve seen, though, it’s second only to Davis. ^c18223298

      - **SahAssar** · [2018-10-15 19:00 UTC](https://news.ycombinator.com/item?id=18222629)
        A subway is a high latency, high bandwidth carrier. A bike track is a low latency, high bandwidth carrier. That is in a subway all "packets" (people) need to wait for the next opportunity to depart, whereas in a bike system all packets move more slowly, but at a more continuous pace (set by the maximum speed of the transport). ^c18222629

        A lot more people can pass any point in a biketrack per hour than they can per subwaytrack, and they can often take a more direct path to their destination using bikes than they can by subway. That also means that a bike system is better suited to a city where both the departure and the destination are diverse among all "packets".

        That's not even starting to talk about how biketracks scale much better economically since they are much cheaper to build.

        - **trhway** · [2018-10-15 19:48 UTC](https://news.ycombinator.com/item?id=18223051)
          \>A subway is a high latency, high bandwidth carrier. ^c18223051

          Trains coming in each couple minutes - show me lower latency than that :)

          \>A lot more people can pass any point in a biketrack per hour than they can per subwaytrack

          several hundreds (up to a thousand in rush hour packing) people per train each couple of minutes - beat that.

          Anyway, the rest of what you're saying about biking is just a theory that doesn't come even close to the reality of any big dense city in Europe/Asia. This is why those cities has highly developed subway system - the low latency high bandwidth and high speed mode of transportation. You put all these people on bikes and they would choke the city.

          - **SahAssar** · [2018-10-15 20:09 UTC](https://news.ycombinator.com/item?id=18223224)
            I guess you have never visited Copenhagen or Amsterdam? Those two are pretty strong counterpoints to what you are saying. ^c18223224

            - **trhway** · [2018-10-15 20:21 UTC](https://news.ycombinator.com/item?id=18223336)
              I stated from the start that lower density smaller cities (which  Copenhagen or Amsterdam are - having density 1/3rd and 1/4th of San Francisco for example) may allow for luxury of letting people to enjoy their commute on bikes. ^c18223336

              - **SahAssar** · [2018-10-15 21:17 UTC](https://news.ycombinator.com/item?id=18223844)
                High density usually isn't the problem for American cities (though it might be for SF, I don't know that one specifically), but rather low density suburban sprawl is. Higher density usually makes it easier to walk or use personal transport like bikes. ^c18223844

                For it to be too dense for biking to be a viable transport they would have to be much denser than European cities which would by definition not allow for parking in the places where business takes place (in which case nobody would drive).

                Most American cities were clearly designed with cars in mind, while most European where not (having grown organically rather than being designed), and while the American decision might have seemed better for the better part of the last 100 years, that might not be the case for the next couple of decades.

        - **unknown** · [2018-10-15 23:15 UTC](https://news.ycombinator.com/item?id=18224912)
          [deleted] ^c18224912

      - **jellicle** · [2018-10-15 23:12 UTC](https://news.ycombinator.com/item?id=18224888)
        Bike lanes are incredibly efficient compared to automobile lanes. ^c18224888

        [https://www.cycling-embassy.org.uk/dictionary/capacity](<https://www.cycling-embassy.org.uk/dictionary/capacity>)

  - **nickik** · [2018-10-15 16:38 UTC](https://news.ycombinator.com/item?id=18221207)
    Using alcohole fuel would have been a very reasonable solution, specially if you care about air quality amd not carbon. ^c18221207

    China is using 100\% methanol and other lesser methanol fuel that are produced from coal. But in other places you could use gas.

    This would also be faster then full electrification. The US missed out massivly. The gas boom could have lead to very cheap and relativly clean fuel.

    It would also be great to have that infrastructure because you can also do fuel cells with the same infrastructure.

    - **jakewins** · [2018-10-15 16:48 UTC](https://news.ycombinator.com/item?id=18221317)
      Source for this? My understanding is that there is solid full-life-cycle analysis showing CO2 reduction from ethanol (35\% lower on average), but a total mixed bag when it comes to hydrocarbons and various other air pollutants - some better, some worse: [https://www.afdc.energy.gov/vehicles/flexible\_fuel\_emissions...](<https://www.afdc.energy.gov/vehicles/flexible_fuel_emissions.html>) ^c18221317

      - **nickik** · [2018-10-15 18:39 UTC](https://news.ycombinator.com/item?id=18222422)
        Ethanol is a different matter again. I was talking about methanol produced by fossil fuels. ^c18222422

        With these fuel it very much depends on a lot of factors.

        However a overall police towards use of fuel alcohol would overall be very benefical.

        Both in terms of emission and in terms of price competition.

  - **Symmetry** · [2018-10-15 15:00 UTC](https://news.ycombinator.com/item?id=18220227)
    If the new power is generated in coal plants that might actually be a net minus, at least in particulates and SO2 terms. ^c18220227

    EDIT:  I'm referencing this:

    *A series of studies by Tsinghua University, whose alumni includes the incumbent president, showed electric vehicles charged in China produce two to five times as much particulate matter and chemicals that contribute to smog versus gas-engine cars. Hybrid vehicles fare little better.*

    [https://www.scientificamerican.com/article/in-coal-powered-c...](<https://www.scientificamerican.com/article/in-coal-powered-china-electric-car-surge-fuels-fear-of-worsening-smog/>)

    - **swebs** · [2018-10-15 15:02 UTC](https://news.ycombinator.com/item?id=18220248)
      How so? A car's ICE is much less efficient than a power plant. ^c18220248

      - **VBprogrammer** · [2018-10-15 15:28 UTC](https://news.ycombinator.com/item?id=18220488)
        I found a series of videos on youtube a while back, a set of training videos for people working in steam turbine plans, which really cemented in my head the reasons why this is the case. ^c18220488

        For example: the final stages of a steam condensing turbine are actually operating under vacuum relative to atmospheric pressure. To start the turbine a vacuum pump first removes the the air from the turbine. After steams works its way through the turbine it is cooled by feed water (which is then used in the boiler) reducing it's volume by about 1000 times maintaining the vacuum.

        An ICE on the other hand expels a good portion of the input energy as hot exhaust gasses several PSI above atmospheric pressure.

      - **rcMgD2BwE72F** · [2018-10-15 16:34 UTC](https://news.ycombinator.com/item?id=18221168)
        EVs are better than average ICE everywhere: [https://en.wikipedia.org/wiki/The\_long\_tailpipe\#Carbon\_footp...](<https://en.wikipedia.org/wiki/The_long_tailpipe#Carbon_footprint_in_selected_countries>) ^c18221168

        - **unknown** · [2018-10-15 16:51 UTC](https://news.ycombinator.com/item?id=18221357)
          [deleted] ^c18221357

      - **village-idiot** · [2018-10-15 15:09 UTC](https://news.ycombinator.com/item?id=18220323)
        Depends on the pollutants you're looking at. ^c18220323

        From a CO2/efficiency standpoint, you're correct. A modern EV powered purely by coal power plants puts out less CO2 than a gasoline car, largely because of the efficiency difference between large power plants and ICE.

        From a SO2/NO2 standpoint, EVs powered by coal would be far far worse, assuming gasoline. Gas/Diesel these days is ultra low sulfur, which reduces SO2 significantly. The only remaining issue is NO2, which is why the catalytic converter is there.

        The only caveat is Diesel. Diesel engines, especially older ones, are pretty horrid things. It's only in the last couple of year have we started to get the particulate under control with DPFs, and the NOx issue remains very difficult to fix *cheaply* (see: VW). Chances are any diesel engines running in a place like China will be old and lack both DPFs and Urea based NOx control systems.

        I am uncertain as to whether old diesel trucks or coal power plants produce more NOx.

        - **olivermarks** · [2018-10-15 15:24 UTC](https://news.ycombinator.com/item?id=18220451)
          IMO hybrid is the way to go for transport. I live in an earthquake prone area where a power cut would equal limited range one way or no transport when I most needed it if I only had an EV. ^c18220451

          Modern ICE are amazingly sophisticated, EV in comparison have limited range, potential polluting issues, battery creation rare earth component scarcity issues and a massive dead battery disposal problem. We'll get there with a grid and more practical EV's but we're not there yet

          - **JoshCole** · [2018-10-15 16:37 UTC](https://news.ycombinator.com/item?id=18221190)
            Might want to refresh your information about electric vehicles. Nissan Leaf era range is no longer the status quo. Tesla has vehicles with 300+ miles of range and other auto manufacturer are now planning to release or releasing 200+ mile range vehicles. Charging times are also not a problem. In my experience, I can handle my daily commute without doing anything special whatsoever. Super convenient. Just get home and plug in and never worry about range at all. ^c18221190

            Total cost of ownership of an EV is getting close to a tipping point where EV is a better deal than electric. One thing pushing that way is the many moving parts of ICE vehicles leading to more maintenance needed. Another is that modern car batteries are turning out to have longevity much higher than what was projected by critics (early Tesla cars still have 90\% of initial battery capacity). Another is that the cost per mile in terms of energy is an order of magnitude cheaper. The only thing really stopping electric is that people have been wary to invest heavily in the factories that were necessary to produce the economies of scale that would lower the price. Since Tesla has done that, prices are dropping and everyone else is being forced to follow.

            ICE vehicles are losing market share, because the more practical EVs you mentioned are already here.

          - **FrojoS** · [2018-10-15 17:42 UTC](https://news.ycombinator.com/item?id=18221819)
            At most gas stations, the pump won’t work during a power outage. 
            [https://www.google.ch/amp/s/www.simplemost.com/gas-stations-...](<https://www.google.ch/amp/s/www.simplemost.com/gas-stations-pump-without-electricity/amp/>) ^c18221819

            With an EV, if you are not driving already, your car will likely be almost fully charged at your home or office while the earthquake strikes. You will then have about 300 miles of driving to a place with power.

        - **ben\_w** · [2018-10-15 16:11 UTC](https://news.ycombinator.com/item?id=18220933)
          Does it produce less CO2 than a coal plant? Yes big plants are more efficient than ICEs, but petrol and diesel have a lot of energy in hydrogen bonds, whereas coal is almost pure carbon, so I’d expect the CO2 emissions for a coal plant to be worse despite the efficiency boost. ^c18220933

          - **village-idiot** · [2018-10-15 18:17 UTC](https://news.ycombinator.com/item?id=18222176)
            Gasoline engines top out at about 50\% efficiency these days, but the average car does much worse. That’s not even including losses from the transmission, etc. ^c18222176

            According to the 2015 DOE analysis, the wheel to wheel emissions from EVs was less than half that of ICE cars. Even in WV, a coal heavy state, EVs produced less emissions than gasoline cars.

            [https://www.energy.gov/eere/vehicles/fact-950-november-7-201...](<https://www.energy.gov/eere/vehicles/fact-950-november-7-2016-well-wheel-emissions-typical-ev-state-2015>)

      - **olivermarks** · [2018-10-15 15:06 UTC](https://news.ycombinator.com/item?id=18220295)
        Planting a lot more trees will have a major impact on pollution reduction.
        [https://news.ycombinator.com/item?id\=18215002](<https://news.ycombinator.com/item?id=18215002>)
        Half the plastics on the planet were made in the last 13 years
        [https://www.theatlantic.com/science/archive/2017/07/plastic-...](<https://www.theatlantic.com/science/archive/2017/07/plastic-age/533955/?fbclid=IwAR1ECQUKm07faBnDLM_9sfcZaR20HGqP_xnK8npknAYiZyeq1okVd-SyjoQ&single_page=true>) 
        EV transport is currently limited and unless solar, wind or hydro is used electricity has to be generated somewhere. ^c18220295

        - **rcMgD2BwE72F** · [2018-10-15 16:02 UTC](https://news.ycombinator.com/item?id=18220847)
          How is that an argument? ^c18220847

          You can plant tree, reduce plastics production *AND* switch to EV. For some reason, every time the case for the electrification of transport is presented, other legitimate, complementary causes are put forward as opposable. As if reducing emissions was a zero-sum game…

          - **olivermarks** · [2018-10-15 17:13 UTC](https://news.ycombinator.com/item?id=18221566)
            Wasn't really an argument against EV's, just an observation that plastics production is a major use of oil and a pollutant (EV's are mostly plastic and alloys for example) at all levels, while the tree planting reality will have a massive positive impact on pollution and seems to be getting overlooked as it is not commercially attractive to big industrialists. ^c18221566

      - **wonderwonder** · [2018-10-15 16:26 UTC](https://news.ycombinator.com/item?id=18221090)
        Volume, coal plants produce massive amounts of pollutants. Cars as a source of pollution only just passed power generation and that's because of the switch to natural gas. Individual coal plants can burn millions of tons of coal per year each. Coal ash is also radioactive. ^c18221090

        [https://www.vox.com/2016/6/13/11911798/emissions-electricity...](<https://www.vox.com/2016/6/13/11911798/emissions-electricity-versus-transportation>)

      - **Symmetry** · [2018-10-15 16:48 UTC](https://news.ycombinator.com/item?id=18221327)
        In terms of energy in to energy out it is a lot more efficient.  But the amount of particulate matter created by burning a kilojoule of coal is much, much higher than the amount created by burning a kilojoule of gasoline. ^c18221327

        - **varjag** · [2018-10-15 17:04 UTC](https://news.ycombinator.com/item?id=18221493)
          It is not. Gasoline ICE typical thermal efficiency is \~20\%, large power generation turbine is 35-40\%. Also, to refine 92 octane gasoline takes about the same amount of energy as it releases when burning. ^c18221493

      - **unknown** · [2018-10-15 17:34 UTC](https://news.ycombinator.com/item?id=18221744)
        [deleted] ^c18221744

    - **DalasNoin** · [2018-10-15 15:04 UTC](https://news.ycombinator.com/item?id=18220272)
      Power plants can be in low population density areas. ^c18220272

      - **lawlessone** · [2018-10-15 15:07 UTC](https://news.ycombinator.com/item?id=18220305)
        it's easier to process the waste to, rather than sticking scrubbers to every car.. ^c18220305

      - **skj** · [2018-10-15 16:40 UTC](https://news.ycombinator.com/item?id=18221223)
        Just put them in some Native American reservations. ^c18221223

      - **ASalazarMX** · [2018-10-15 15:06 UTC](https://news.ycombinator.com/item?id=18220300)
        Better their intelligence than ours. ^c18220300

    - **rayiner** · [2018-10-15 15:05 UTC](https://news.ycombinator.com/item?id=18220291)
      Particulates are localized, and coal plants generallt aren’t in densely populated areas. ^c18220291

    - **mikeash** · [2018-10-15 15:17 UTC](https://news.ycombinator.com/item?id=18220399)
      So, don’t do that. Any solution can fail if you implement it badly. ^c18220399

    - **make3** · [2018-10-15 15:09 UTC](https://news.ycombinator.com/item?id=18220321)
      coal plants are much more efficient than individual machines ^c18220321

    - **gameswithgo** · [2018-10-15 15:04 UTC](https://news.ycombinator.com/item?id=18220273)
      solar, wind, nuclear. let's get on that too. ^c18220273

  - **tarboreus** · [2018-10-15 15:19 UTC](https://news.ycombinator.com/item?id=18220420)
    If by "electrification" you mean "switch to public transportation," I agree with you. If by electrification you mean "burn dinosaurs four miles away," then I don't agree with you. ^c18220420

    - **gregwtmtno** · [2018-10-15 17:00 UTC](https://news.ycombinator.com/item?id=18221446)
      This argument is dead wrong and impeding progress. As other commenters have mentioned, stationary sources are much easier to filter. They're also more efficient than thousands of small internal combustion engines. They also produce pollution away from where people are breathing it. ^c18221446

      Electrification of surface transportation is a huge win for people regardless of how the electricity is generated.

      - **lev99** · [2018-10-15 18:18 UTC](https://news.ycombinator.com/item?id=18222182)
        The argument for public transportation is not dead wrong nor impeding progress.  Expanding bus systems is something communities can do today in order to reduce their carbon footprint and their traffic levels. ^c18222182

        - **FooHentai** · [2018-10-15 21:06 UTC](https://news.ycombinator.com/item?id=18223738)
          The argument tarboreous put forward, as the parent, is presumably the one under discussion. ^c18223738

          The problem is it presents a false dichotomy, or at least a choice which highlights merely a current state and not a move towards future improvements, and uses that blindless to make a case against EVs.

          Thing is, even if a country is 100\% coal and ICE right now (which is already not the case, China is not 100\% coal), moving the fleet to EVs is still a good move. Putting aside an argument as to whether central power generation is 'cleaner' than distributed (ICE) generation, as long as a country *also* makes moves to renewables in it's centralized power generation, then the two things work in conjunction.

          A lot of the current 'omg greenwashing' push-back is people confusing arguments for 'better' solutions with those for 'perfect' solutions. Which don't exist. Better is still worth doing, and paralysis until 'perfect' comes along is a big ol' waste of everyone's time.

    - **ip26** · [2018-10-15 16:08 UTC](https://news.ycombinator.com/item?id=18220910)
      Not a power engineer, but I'd expect burning dinosaurs in one stationary place should allow for cleaner & more efficient combustion, with better scrubbing of noxious gasses from the exhaust. One really big, really heavy, really good catalytic converter instead of millions of small lightweight ones, clunking over bumps & quietly rusting out. ^c18220910

    - **rayiner** · [2018-10-15 15:25 UTC](https://news.ycombinator.com/item?id=18220465)
      In economic terms, the biggest impact from air pollution is particulate matter in densely populated areas, not CO2. Burning dinosaurs four miles away (more accurately, 40+) has a huge positive impact, because the worst of the particulate matter falls to the ground by then. ^c18220465

      - **flybrand** · [2018-10-15 16:31 UTC](https://news.ycombinator.com/item?id=18221145)
        As someone who works in filtration - one of the primary ways to reduce pollution - stationary sources are easier to filter. ^c18221145

        Vehicles have limited under the hood space and are distributed.

        - **Gibbon1** · [2018-10-15 18:32 UTC](https://news.ycombinator.com/item?id=18222331)
          Yeah you can use electrostatic scrubbers and wet scrubbers on stationary plants. Can't do that with a car. ^c18222331

    - **tfha** · [2018-10-15 15:22 UTC](https://news.ycombinator.com/item?id=18220441)
      Burning dinosaurs 40 miles away will improve air quality in cities, even if it's the same amount of pollution, the bulk is away from dense population ^c18220441

      - **sgc** · [2018-10-15 15:36 UTC](https://news.ycombinator.com/item?id=18220555)
        It's also much, much easier to filter the output from one plant instead of 40,000 cars. Even if the same amount of pollution were produced (it wouldn't be), nowhere near the same amount would be released into the air. ^c18220555

        But we definitely need to improve power plant emission standards as we move to electric.

      - **black6** · [2018-10-15 16:03 UTC](https://news.ycombinator.com/item?id=18220863)
        The solution to pollution is dilution! ^c18220863

    - **amyjess** · [2018-10-15 15:37 UTC](https://news.ycombinator.com/item?id=18220567)
      On top of the excellent comments made by rayiner, tfha, and jwr, we wouldn't even be burning dinosaurs miles away if we switched entirely to nuclear power. ^c18220567

      - **sxates** · [2018-10-15 17:36 UTC](https://news.ycombinator.com/item?id=18221760)
        Or Solar or Wind or Hydro. In places like California and parts of Europe renewable sources are 1/3 or more of the electricity mix. ^c18221760

        - **siderax** · [2018-10-15 19:39 UTC](https://news.ycombinator.com/item?id=18222984)
          But when we look at the datas, country that use nuclear power are way way ahead of those that use renewable mix. ^c18222984

          Easy to look at : [https://www.electricitymap.org](<https://www.electricitymap.org>)

          - **sxates** · [2018-10-15 20:53 UTC](https://news.ycombinator.com/item?id=18223634)
            I'm not arguing against Nuclear, just pointing out that it's one of several low-pollution options. ^c18223634

      - **justinator** · [2018-10-15 16:26 UTC](https://news.ycombinator.com/item?id=18221097)
        That's never going to happen. ^c18221097

        (but no mention of solar, wind, drastically reducing our energy consumption, etc?)

    - **jwr** · [2018-10-15 15:33 UTC](https://news.ycombinator.com/item?id=18220536)
      Burning dinosaurs is much more efficient in bulk at a huge power plant than by transporting them to your local storage (gas station) and burning them in your tiny engine. So even if you do burn dinosaurs, you're much better off burning them at scale. ^c18220536

    - **visarga** · [2018-10-15 17:09 UTC](https://news.ycombinator.com/item?id=18221533)
      \> burn dinosaurs four miles away ^c18221533

      It's mostly plants and zooplankton

    - **aj7** · [2018-10-15 15:54 UTC](https://news.ycombinator.com/item?id=18220719)
      Regenerative braking.
      Max efficiency at urban speeds. ^c18220719

      - **dsfyu404ed** · [2018-10-15 16:02 UTC](https://news.ycombinator.com/item?id=18220857)
        \>Max efficiency at urban speeds. ^c18220857

        If by "max efficiency" you mean "less terrible than just wasting that energy" then sure but it's still a lot less efficient than a highway cruise.

    - **api** · [2018-10-15 16:09 UTC](https://news.ycombinator.com/item?id=18220913)
      Public transportation that runs on the power grid also burns dinosaurs if it's powered by fossil fuels. ^c18220913

      Edit: why the downmod? Energy is energy.

      - **tarboreus** · [2018-10-15 18:35 UTC](https://news.ycombinator.com/item?id=18222363)
        Because moving a person on a train is so much more power efficient than moving one person in a car that they are barely even comparable? ^c18222363

  - **wonderwonder** · [2018-10-15 16:23 UTC](https://news.ycombinator.com/item?id=18221066)
    Transportation just passed power generation as the major polluter in 2016. Mainly because of the switch from coal to natural gas. If coal comes back on line expect the positions to switch again rapidly. I agree with your statement but getting rid of coal power plants would have the added benefit of reducing the production of coal ash, a source of particulate matter and heavy metal pollution. ^c18221066

    Both would be major living standard improvement.

    [https://www.vox.com/2016/6/13/11911798/emissions-electricity...](<https://www.vox.com/2016/6/13/11911798/emissions-electricity-versus-transportation>)

  - **75dvtwin** · [2018-10-15 18:06 UTC](https://news.ycombinator.com/item?id=18222073)
    I would argue that priority has to be 'de-urbanization' itself. Pollution is just one problem that will be solved by de-urbanization. ^c18222073

    - **lev99** · [2018-10-15 18:12 UTC](https://news.ycombinator.com/item?id=18222127)
      How will pollution be solved by de-urbanization? ^c18222127

      Urban citizens have better access to low carbon transportation (Walking, Biking, Mass Transit).

      Urban citizens are easier to reach in many last mile problems.  Power lines can be shared by more users.  Less network cable needs to be laid per user.  Fewer miles of water pipes are required.

      Apartments common in urban areas are more fuel efficient for heating/cooling than stand alone houses commonly seen in suburbs and rural areas.

      - **erikpukinskis** · [2018-10-15 18:17 UTC](https://news.ycombinator.com/item?id=18222175)
        If you think of pollution not as an issue with the total quantity, but instead spikes of concentrated, it makes sense. ^c18222175

  - **stellar678** · [2018-10-15 16:18 UTC](https://news.ycombinator.com/item?id=18221008)
    Studies have actually shown that electric cars produce more than 90\% as much particulate-matter air pollution as fossil fuel cars. ^c18221008

    The reason for this is two-fold:
    1\. Modern gasoline cars produce very clean exhaust.
    2\. Most of the particulate pollution comes from wear on tires, brake and the road surface. And electric cars, being heavier than average, produce more wear on tires and road surface.

    Electrification is part of the puzzle, but we also need to get people out of giant, heavy vehicles into right-sized vehicles for their trip. (And the majority of trips are less than 5 miles!)

    \--

    Edit for the people asking for sources:

    The lit review suggesting EVs have \>90\% as much particulate emissions as internal-combustion: [http://www.soliftec.com/NonExhaust\%20PMs.pdf](<http://www.soliftec.com/NonExhaust%20PMs.pdf>)

    Another review that acknowledges these numbers vary depending on rainy vs dry climate, use of snow tires, etc...

    [https://www.kau.edu.sa/Files/188/Researches/65862\_37290.pdf](<https://www.kau.edu.sa/Files/188/Researches/65862_37290.pdf>)

    - **Reason077** · [2018-10-15 16:29 UTC](https://news.ycombinator.com/item?id=18221112)
      Those “studies” are pretty much nonsense. ^c18221112

      It’s true that tire wear may be increased slightly due to weight, but electrics aren’t *that* much heavier than combustion vehicles: typically 10-20\% more for comparable vehicles of the same size/class.

      Under normal road/wear conditions, most tires degrade into relatively large particles that are not actually aerosolised. They end up on the road and get washed away by weather. The main place where they become a problem is in tunnels where the dry conditions and passing traffic keep picking them back up into the air.

      Finally, brake pads. Electric hugely *reduce* brake wear due to regenerative braking. Most EV owners will tell you that they’ve *never* had to replace their brake pads!

      - **aembleton** · [2018-10-15 16:36 UTC](https://news.ycombinator.com/item?id=18221183)
        Even a hybrid will rarely need brake pads to be changed. ^c18221183

    - **aembleton** · [2018-10-15 16:35 UTC](https://news.ycombinator.com/item?id=18221181)
      Electric cars will produce very little brake dust as they regenerative braking.  In an emergency braking situation they will use friction braking but not for day to day driving. ^c18221181

      That means 90\% of cars particulate matter must be coming from tyres and the road surface.  How far does this travel?  Does it just fall back quickly onto the road?  Does it get washed away in a rain storm?

      Do you have a source for that 90\% figure?

    - **justinator** · [2018-10-15 16:24 UTC](https://news.ycombinator.com/item?id=18221077)
      Do you have a link to the studies you're referencing? I don't *not* believe you, but I'd love to share them. Living in CO, there is a problem with electric cars, (somewhat) as the electric is usually produced by coal, so the pollution is simply moved away from the source (although potentially lowered - but not by much if you compare it to a gas-powered econo vehicle) ^c18221077

    - **gurumeditations** · [2018-10-15 16:26 UTC](https://news.ycombinator.com/item?id=18221092)
      Is the particulate pollution just as grave as emissions pollution or a completely separate issue? ^c18221092

      - **flybrand** · [2018-10-15 16:29 UTC](https://news.ycombinator.com/item?id=18221125)
        All pollution is some kind of particle - here it just means that emissions are coming out of the tail pipe as a byproduct of the internal combustion engine, as opposed to the particulate created from braking, etc. ^c18221125

        - **Reason077** · [2018-10-15 16:34 UTC](https://news.ycombinator.com/item?id=18221165)
          Particles are part of the story, but also toxic gasses such as NOx and CO. ^c18221165

          NOx in particular is a big problem in European cities due to the proliferation of diesel cars.

    - **collyw** · [2018-10-15 17:44 UTC](https://news.ycombinator.com/item?id=18221838)
      Do you work for Volkswagen? ^c18221838

- **titzer** · [2018-10-15 14:46 UTC](https://news.ycombinator.com/item?id=18220096)
  The actual study is linked early in the article here: ([http://www.pnas.org/content/early/2018/08/21/1809474115](<http://www.pnas.org/content/early/2018/08/21/1809474115>)) ^c18220096

  Quoting:

  \> ... Cutting annual mean concentration of particulate matter smaller than 10 μm (PM10) in China to the Environmental Protection Agency’s standard (50 μg/m3) would move people from the median to the 63rd percentile (verbal test scores) and the 58th percentile (math test scores), respectively. The damage on the aging brain by air pollution likely imposes substantial health and economic costs, considering that cognitive functioning is critical for the elderly for both running daily errands and making high-stake decisions.

- **tzs** · [2018-10-15 19:56 UTC](https://news.ycombinator.com/item?id=18223115)
  Meanwhile, the EPA is kicking academic scientists off advisory panels in this area, and replacing the panels with a small group consisting entirely of industry scientists and government officials from conservative state and local governments. ^c18223115

  [https://www.washingtonpost.com/energy-environment/2018/10/14...](<https://www.washingtonpost.com/energy-environment/2018/10/14/epa-scraps-pair-air-pollution-science-panels/?utm_term=.143dd8b161c8>)

- **peacetreefrog** · [2018-10-15 14:50 UTC](https://news.ycombinator.com/item?id=18220137)
  I'd be interested in how reading more about how they're controlling for non-air pollution factors, particularly since they say the effects are most pronounced among the non educated. ^c18220137

  - **peacetreefrog** · [2018-10-15 15:02 UTC](https://news.ycombinator.com/item?id=18220254)
    For example: assume in China that people in cities generally have more opportunities to get educated. ^c18220254

    That'd mean if you live in a city and have not had much education, it might be because you are less intelligent (on average).  While if you're in a rural area, a lack of education might not mean anything, because you have less opportunity to get educated in general, regardless of intelligence.

    If you did a simple regression in this case with years of education and air pollution (more common in cities) in the model, I think you'd find that -- controlling for education -- air pollution would be correlated with a reduction of intelligence, even if the air pollution itself wasn't causal.

    There are ways of controlling for this, and I'm not at all saying the study didn't take this into account, but it'd be useful to know more.  There are a lot of ways (as in any model) the relationship could be correlated without being causal.

  - **flybrand** · [2018-10-15 16:33 UTC](https://news.ycombinator.com/item?id=18221164)
    This is a major issue in many pollution studies.  High pollution tends to correlate with low income, low education and less access to healthcare worldwide.  One of the biggest sources of indoor air quality (IAQ) pollution is indoor fires - which are rare in many big cities. ^c18221164

- **dest** · [2018-10-15 15:03 UTC](https://news.ycombinator.com/item?id=18220261)
  I think it is misleading to display a picture of chimneys of nuclear power plants, when the only thing they release is clean water droplets: no SO2, NO2 or PM10. ^c18220261

  edit: Actually, not 100\% sure it's a nuclear power plant. Thanks for your comments

  - **MichaelApproved** · [2018-10-15 15:13 UTC](https://news.ycombinator.com/item?id=18220355)
    Do you know for sure that it's a nuclear plant in the picture? I'm asking because those iconic cooling towers are also used for coal plants. ^c18220355

    \> The hyperboloid cooling towers are often associated with nuclear power plants,\[1\] although they are also used in some coal-fired plants and to some extent in some large chemical and other industrial plants.

    \- [https://en.wikipedia.org/wiki/Cooling\_tower](<https://en.wikipedia.org/wiki/Cooling_tower>)

    Direct link to the picture from the article [https://www.unenvironment.org/sites/default/files/styles/art...](<https://www.unenvironment.org/sites/default/files/styles/article_billboard_image/public/2018-10/2010-10-Air%20pollution-CHINA-USA-CLIMATE.jpg>)

    Example cooling towers from a coal-fired power plant [https://www.alamy.com/stock-photo-eon-scholven-power-station...](<https://www.alamy.com/stock-photo-eon-scholven-power-station-coal-fired-power-plant-cooling-towers-gelsenkirchen-89211541.html>)

    - **khuey** · [2018-10-15 15:20 UTC](https://news.ycombinator.com/item?id=18220428)
      Even if it's not a nuclear power plant it's still a cooling tower releasing only water vapor. ^c18220428

      - **StavrosK** · [2018-10-15 15:36 UTC](https://news.ycombinator.com/item?id=18220557)
        Some new designs release both water vapor and other gases in the same tower, but yeah, those look like cooling towers releasing just vapor. ^c18220557

      - **Brakenshire** · [2018-10-15 17:04 UTC](https://news.ycombinator.com/item?id=18221488)
        It's a picture of a power station, the cooling towers are just the most noticeable feature. ^c18221488

    - **maccard** · [2018-10-15 15:18 UTC](https://news.ycombinator.com/item?id=18220406)
      And just to show what a nuclear plant can look like, \[0\] is a few miles away from me, and looks like \[1\] ^c18220406

      \[0\] - [https://en.wikipedia.org/wiki/Torness\_Nuclear\_Power\_Station](<https://en.wikipedia.org/wiki/Torness_Nuclear_Power_Station>)

      \[1\] [https://en.wikipedia.org/wiki/Torness\_Nuclear\_Power\_Station\#...](<https://en.wikipedia.org/wiki/Torness_Nuclear_Power_Station#/media/File:Torness_Nuclear_Power_Station_-_April_2016.jpg>)

      - **rcMgD2BwE72F** · [2018-10-15 15:20 UTC](https://news.ycombinator.com/item?id=18220426)
        It also looks like [https://commons.wikimedia.org/wiki/File:Torness\_Nuclear\_Powe...](<https://commons.wikimedia.org/wiki/File:Torness_Nuclear_Power_Station_Accident_18th_April_2017.jpg>) :) ^c18220426

      - **astrodust** · [2018-10-15 16:07 UTC](https://news.ycombinator.com/item?id=18220900)
        Some of these plants use a local source of water for cooling, not the traditional cooling towers. ^c18220900

        If it's inland or starved for water you need cooling towers.

    - **Brakenshire** · [2018-10-15 17:05 UTC](https://news.ycombinator.com/item?id=18221502)
      The same picture is used to illustrate a coal power station elsewhere: ^c18221502

      [https://international.thenewslens.com/article/81575](<https://international.thenewslens.com/article/81575>)

      It seems to be a coal station in China.

  - **jarvist** · [2018-10-15 15:26 UTC](https://news.ycombinator.com/item?id=18220469)
    Those are cooling towers (steam -\> water), and there is no indication whether that is a power station or industrial plant. ^c18220469

  - **unknown** · [2018-10-15 17:04 UTC](https://news.ycombinator.com/item?id=18221483)
    [deleted] ^c18221483

  - **mmphosis** · [2018-10-15 15:24 UTC](https://news.ycombinator.com/item?id=18220452)
    I agree there are worse types of power plants than nuclear: no SO2, NO2 or PM10, but at the risk of the release of Cesium-134, Cesium-137, Iodine-131, Xenon-133, strontium-90, plutonium-239. ^c18220452


    ```
      https://www.scientificamerican.com/article/radioactive-isotopes-from-fukushima-meltdown-detected-near-vancouver/
      https://www.cancer.gov/about-cancer/causes-prevention/risk/radiation/nuclear-accidents-fact-sheet
    ```

    - **StavrosK** · [2018-10-15 15:37 UTC](https://news.ycombinator.com/item?id=18220575)
      Depending on the rates, I'd take a risk of Cesium than the certainty of SO2, CO2, NO2, etc. ^c18220575

      - **saiya-jin** · [2018-10-15 15:46 UTC](https://news.ycombinator.com/item?id=18220643)
        Aren't coal plants releasing small amounts of heavy metals and radioactivity from burning coal too? I recall some discussion here couple of months ago mentioning oceans pollution (and thus mainly predatory fish) mainly comes down to all coal plants churning all this at slow but steady pace. ^c18220643

        Somebody also mentioned that old decommissioned plants have their smelter quite radioactive and need to be handled accordingly. Can't find it now though...

        - **wonderwonder** · [2018-10-15 16:14 UTC](https://news.ycombinator.com/item?id=18220966)
          Coal ash, the waste from burning coal has significant amounts of radioactive heavy metals. It is stored in 'ash ponds' which can leach into the ground water and the ash can be blown into surrounding neighborhoods as they are not capped. Analysis of EPA data found that living around a coal plant can give you up to a 1 in 50 chance of cancer. ^c18220966

          Clearly a biased source (not necessarily bad though) but the data is likely accurate, make of it what you will.

          [https://earthjustice.org/news/press/2009/epa-data-show-highe...](<https://earthjustice.org/news/press/2009/epa-data-show-higher-cancer-risks-for-those-who-live-near-coal-ash-dumps>)

          - **xkcd-sucks** · [2018-10-15 23:29 UTC](https://news.ycombinator.com/item?id=18225023)
            Does coal ash concentrate valuable metals found in coal? If so the ash could be a valuable source of radioisotopes... Presumably it's not profitable though, cause its not a very original idea ^c18225023

      - **crdoconnor** · [2018-10-15 16:32 UTC](https://news.ycombinator.com/item?id=18221150)
        I'd rather tariffs were taken off solar panels so they weren't rendered artificially uncompetitive. ^c18221150

    - **astrodust** · [2018-10-15 16:08 UTC](https://news.ycombinator.com/item?id=18220909)
      If you're concerned about radioactive elements, coal plants and fracking also release a lot of nuclear contamination. ^c18220909

  - **rc\_bhg** · [2018-10-15 15:19 UTC](https://news.ycombinator.com/item?id=18220412)
    Yeah there are a ton of pictures of Natural gas and Coal power plants. Either one of them could have been used in the picture. ^c18220412

- **dcx** · [2018-10-15 17:05 UTC](https://news.ycombinator.com/item?id=18221504)
  I don't think this has been mentioned on this thread yet: If you live in a place where air pollution is a concern, one solution to this issue is to buy a HEPA air filter. These filters are designed to trap a significant quantity of precisely the types of particles that air quality studies examine (2.5-10µm coarse dust particles and \<2.5µm fine particles). ^c18221504

  \> "To qualify as HEPA by industry standards, an air filter must remove (from the air that passes through) 99.97\% of particles that have a size greater-than-or-equal-to 0.3 µm." \[1\]

  \[1\] [https://en.wikipedia.org/wiki/HEPA](<https://en.wikipedia.org/wiki/HEPA>)

  - **amluto** · [2018-10-15 17:16 UTC](https://news.ycombinator.com/item?id=18221588)
    That’s only helpful while you’re at home. ^c18221588

    Also, the obsession with HEPA and its 99.7\% reduction of the relevant particles seems silly to me.  For a filter that recirculates air, the relevant figure of merit is the rate at which dirty air is replaced with clean air, which is roughly the air flow through the filter times the efficiency. So a 90\% efficient filter with 50\% more airflow is better. For a stand-alone unit, the “clean air delivery rate” is a more sophisticated measurement.

    You can do *very* well by upgrading your HVAC filter to MERV 13 or better and running the fan for a few hours a day. But check with an HVAC contractor before you change filter types — it may affect the overall performance of the system.

    For an outside air intake, the efficiency does matter, and HEPA is a good idea.

- **chadlavi** · [2018-10-15 14:57 UTC](https://news.ycombinator.com/item?id=18220202)
  I think that correlation works in both directions! ^c18220202

- **meesterdude** · [2018-10-15 18:24 UTC](https://news.ycombinator.com/item?id=18222236)
  I know a certain framework creator that will be all over this - and has been vocal on twitter about it. ^c18222236

  I went looking, this seems like a pretty good air quality monitor: [https://www.amazon.com/AirVisual-Quality-Monitor-Accuracy-Pa...](<https://www.amazon.com/AirVisual-Quality-Monitor-Accuracy-Particle/dp/B01MF6X1YK>) (\~\$400)

  There are cheaper ones too; but do your research, as accuracy (and ideas about what constitutes accurate) can vary from manuf. to manuf.

  [https://medium.com/@dhh/air-quality-matters-but-dont-trust-f...](<https://medium.com/@dhh/air-quality-matters-but-dont-trust-foobot-on-it-e2df4234a776>)

  also apparently, a box fan + filter ain't so bad. [https://www.youtube.com/watch?v\=kH5APw\_SLUU](<https://www.youtube.com/watch?v=kH5APw_SLUU>)

- **eneveu** · [2018-10-15 21:22 UTC](https://news.ycombinator.com/item?id=18223894)
  I recently learned that the parisian subway and suburban trains contain a lot of particulate pollution (e.g. PM10), caused by braking (electrical brakes would reduce this) and rail grinding (maintenance done to reduce squealing in curves). The small particulate pollution is actually worse than what you find in traffic jams in the city center... ^c18223894

  I'm looking into buying an anti-pollution mask. It will probably look weird, since nobody wears masks there... People will probably think I'm sick or something. Maybe I should buy some techwear clothing to complete the "goth-ninja" look, but I'm not sure how that will fly at work.

  I have an air purifier at home since 3 years (Philips AC4072/11). I think it's a good investment, since I spend around 50\% of the time at home. It also seems to have helped with my allergies, but that might be placebo.

  - **apta** · [2018-10-16 02:01 UTC](https://news.ycombinator.com/item?id=18225789)
    For what it's worth, I wear a respirator\[1\] when I take the subway. Some people may look at you, but I don't really care. ^c18225789

    That being said, I recall reading an article where they said studied long term subway commuters and did not find health issues due to commuting.

    Furthermore, you can apparently build an air filter for the fraction of the cost: [https://www.youtube.com/watch?v\=q45CkwKiOvw](<https://www.youtube.com/watch?v=q45CkwKiOvw>)

    \[1\] like the "3M Aura Particulate Respirator". There are also filter with activated charcoal

    - **imcoconut** · [2018-10-16 02:24 UTC](https://news.ycombinator.com/item?id=18225894)
      Do you live in NYC? and have you found that it helps? ^c18225894

      - **apta** · [2018-10-17 01:41 UTC](https://news.ycombinator.com/item?id=18235014)
        I commute to NYC. Yes it reduces the subway smell substantially. ^c18235014

- **yorwba** · [2018-10-15 14:51 UTC](https://news.ycombinator.com/item?id=18220152)
  Previous discussion of the same topic: [https://news.ycombinator.com/item?id\=17867085](<https://news.ycombinator.com/item?id=17867085>) ^c18220152

- **elektor** · [2018-10-15 16:44 UTC](https://news.ycombinator.com/item?id=18221273)
  If you're curious about your own exposure to air pollutants, I'd recommend Plume Labs. They also have a handheld device that I preordered and hope to take around my town to see where the hotspots are. [https://air.plumelabs.com/en/](<https://air.plumelabs.com/en/>) ^c18221273

- **robynsmith** · [2018-10-15 17:52 UTC](https://news.ycombinator.com/item?id=18221930)
  Is there a way to counteract the effects? Especially if you live in a large city? ^c18221930

  - **QasimK** · [2018-10-15 20:20 UTC](https://news.ycombinator.com/item?id=18223328)
    I’m going to hazard a guess and say exercise - yes, even outside in the pollution (though you should probably favour a park over a main road). ^c18223328

  - **aaron695** · [2018-10-16 01:21 UTC](https://news.ycombinator.com/item?id=18225647)
    [flagged] ^c18225647

    Yes.

    You buy air filters (ie HEPA) and an air quality (ie PM) detection device.

    Even skipping intelligence, it's important to stop cancer.

    Start googling.

    Normally you're talking about reducing PM10 and PM2.5

    If you're talking fixing damage once done to the body, currently there's no known way.

- **wireprotocol** · [2018-10-15 15:02 UTC](https://news.ycombinator.com/item?id=18220252)
  What's with the use of the word "linked"? Is thay synonymous with "correlated"? ^c18220252

  I feel like it's just another way to suggest causation without knowing that it is causation.

  - **wccrawford** · [2018-10-15 15:21 UTC](https://news.ycombinator.com/item?id=18220435)
    It's more of a weasel word than correlated is, even.  It suggests that there's a meaningful connection but it could just be coincidence, even moreso than correlation. ^c18220435

    - **singularity2001** · [2018-10-15 15:27 UTC](https://news.ycombinator.com/item?id=18220481)
      correlated is well defined. ^c18220481

      but can be used by weasels, so yes.

- **ct520** · [2018-10-15 16:49 UTC](https://news.ycombinator.com/item?id=18221340)
  china number 1 ^c18221340

- **baybal2** · [2018-10-15 15:40 UTC](https://news.ycombinator.com/item?id=18220598)
  Beijing central district anybody? ^c18220598

- **randyrand** · [2018-10-15 15:35 UTC](https://news.ycombinator.com/item?id=18220543)
  industrial places have less of a demand on higher education ^c18220543

- **ramijames** · [2018-10-15 16:22 UTC](https://news.ycombinator.com/item?id=18221054)
  Well that explains Los Angeles. ^c18221054

- **OnlyRepliesToBS** · [2018-10-15 15:27 UTC](https://news.ycombinator.com/item?id=18220478)
  [flagged] ^c18220478

  choosy mothers choose lead

- **ataturk** · [2018-10-15 15:39 UTC](https://news.ycombinator.com/item?id=18220594)
  [flagged] ^c18220594

  Having a hard time with this one--so many variables in play.  I mean, maybe overpopulation causes a drop in overall intelligence and air pollution is just a symptom of overpopulation?

- **throwawaymanbot** · [2018-10-15 18:50 UTC](https://news.ycombinator.com/item?id=18222525)
  [flagged] ^c18222525

  Lead made people more likely to commit crimes, so why wouldnt other pollutants affect us in different ways? And to think the GOP still want to make the air dirtier, and have legislated for it so.

- **Proven** · [2018-10-15 14:50 UTC](https://news.ycombinator.com/item?id=18220135)
  [flagged] ^c18220135

  Unpossible.

  First, it likely depends what kind of pollution
  Second, this title or the research is likely hyping up the results

  Can't even be bothered to click on the link...

- **strittmatter** · [2018-10-15 15:04 UTC](https://news.ycombinator.com/item?id=18220284)
  [flagged] ^c18220284

  [https://www.cbsnews.com/pictures/air-pollution-worst-us-citi...](<https://www.cbsnews.com/pictures/air-pollution-worst-us-cities-2018/18/>)

  It's pretty interesting to see how a lot of these cities place pretty low when it comes to education.

  [https://wallethub.com/edu/most-and-least-educated-cities/665...](<https://wallethub.com/edu/most-and-least-educated-cities/6656/>)

- **randyrand** · [2018-10-15 15:35 UTC](https://news.ycombinator.com/item?id=18220549)
  industrial places have less of a demand for education ^c18220549

- **vectorEQ** · [2018-10-15 15:04 UTC](https://news.ycombinator.com/item?id=18220282)
  do something about education and media - that has an actual HUGE impact... ^c18220282

- **ryeguy\_24** · [2018-10-15 17:29 UTC](https://news.ycombinator.com/item?id=18221705)
  I’ve always beleived that measuring intelligence is extremely ignorant. I find it funny that we try to take the insanely complex, multi-dimensional organ of the brain and try to map it to a one dimensional score (e.g. IQ, verbal, math tests). ^c18221705

- **m23khan** · [2018-10-15 15:11 UTC](https://news.ycombinator.com/item?id=18220342)
  With China and India leading the race in terms of producing intelligent people (in terms of quantity), it is rather hard to believe. Nonetheless, air pollution is a serious topic and needs to be dealt with ASAP. ^c18220342

  - **lostmsu** · [2018-10-15 15:19 UTC](https://news.ycombinator.com/item?id=18220417)
    What? Are you talking about percentages? ^c18220417

- **sneak** · [2018-10-15 15:04 UTC](https://news.ycombinator.com/item?id=18220265)
  Reminder: part of Google’s new Project Dragonfly is a feature that allows Beijing to lie about air pollution figures in real-time. ^c18220265

  [https://theintercept.com/2018/09/14/google-china-prototype-l...](<https://theintercept.com/2018/09/14/google-china-prototype-links-searches-to-phone-numbers/>)

