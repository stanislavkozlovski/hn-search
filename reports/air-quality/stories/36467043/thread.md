# [Air quality reporting on iOS](https://news.ycombinator.com/item?id=36467043)

Article: [https://intergalactic.systems/posts/post-1965946732.html](<https://intergalactic.systems/posts/post-1965946732.html>)

owl110 · 2023-06-25 11:20 UTC · 95 reported comments · archived 2026-11-08 13:07 UTC
Observation: 2026-11-08 13:06 UTC → 2026-11-08 13:07 UTC

## Comments

- **counters** · [2023-06-25 17:10 UTC](https://news.ycombinator.com/item?id=36470413)
  The problem here is twofold. ^c36470413

  First, many countries have their own laws and policies regarding air quality exposure. Often times these regulations use metrics about time-average exposure (e.g. the annual average 8-hr maximum ozone concentration) and can't trivially be converted between agencies. It causes very negative user experiences when your air quality summary disagrees with what a regulatory agency is putting out to the public due to a measurement technicality - much easier just to localize the data in the same way you'd localize the rest of the UI.

  Second, we're stuck with AQI and similar indices because air quality is a multi-faceted problem with different components measured wildly differently. For instance, PM2.5 and PM10 are typically reported in ug/m\^3 - but who actually knows what these measurements mean? What's the difference between 15 and 30 ug/m\^3? It's  very far outside of the experiences that many individuals have, so end users really struggle to interpret these values, even when you translate them into simple "low"/"medium"/"high" categories. Then of course gas-phase pollutants are typically reported in volume concentrations like parts-per-billion or parts-per-million. Aside from the fact that these values are very commonly misinterpreted as much smaller than they actually are, the difference in units adds another bit of complexity into users interpreting what they're seeing.

  A well-designed air quality index could factor our all these challenges. I definitely h/t Breezometer for their attempts there, even if it is generally poorly received. But it's a very challenging problem no matter how you slice it.

  - **owl110** · [2023-06-25 17:22 UTC](https://news.ycombinator.com/item?id=36470590)
    These are very good points but at least Apple could give the user a choice to report air quality consistently when traveling. At the core, this is not a measurement problem (the underlying data is likely the same) but it is a user experience issue since a user cannot use the color coding as a way to compare different scales across locations. ^c36470590

    - **counters** · [2023-06-25 17:36 UTC](https://news.ycombinator.com/item?id=36470734)
      Well, the underlying data might not actually be the same. ^c36470734

      One country may lump in PM10 into their AQI, so if there is a dust storm or similar event, the AQI could spike. Other countries may only include PM2.5 or not include PM at all, which wouldn't capture the dust storm.

  - **908B64B197** · [2023-06-25 19:52 UTC](https://news.ycombinator.com/item?id=36471935)
    \> many countries have their own laws and policies regarding air quality exposure. Often times these regulations use metrics about time-average exposure (e.g. the annual average 8-hr maximum ozone concentration) and can't trivially be converted between agencies. It causes very negative user experiences when your air quality summary disagrees with what a regulatory agency is putting out to the public due to a measurement technicality ^c36471935

    Ultimately, why not simply compute it and give the user a warning that the local measurement isn't compatible with proper AQI measurement?

    Also, does my body magically changes the way it reacts to air pollution as soon as I take my first step abroad?

    - **counters** · [2023-06-25 22:04 UTC](https://news.ycombinator.com/item?id=36473091)
      \> Ultimately, why not simply compute it and give the user a warning that the local measurement isn't compatible with proper AQI measurement? ^c36473091

      You totally could, but in practice it doesn't always or obviously lead to a positive user experience our outcome.

    - **cyanydeez** · [2023-06-27 12:17 UTC](https://news.ycombinator.com/item?id=36491783)
      Likely incompatible measurements combined with regulatory laws regarding reporting. ^c36491783

      Remember when Donald Trump drew on a NOAA map and multiple outlets reported that was essentially a felony?

      Imagine doing that all over the world. You're gonna find a couple jurisdictions not taking kindly. Remember, this is Apple, any negative pushback is a PR problem disguised as UI to it's walled garden.

- **apwheele** · [2023-06-25 15:06 UTC](https://news.ycombinator.com/item?id=36468967)
  Of interest to folks looking at this post -- Chris Said has a deeper dive on US air quality metrics and their provenance, [https://chris-said.io/2023/06/19/the-air-quality-index-doesn...](<https://chris-said.io/2023/06/19/the-air-quality-index-doesnt-make-any-sense/>). ^c36468967

  The attempt to make things easy to interpret using a nice relative scale ends up in the end make them very opaque to interpret the number itself in any meaningful way.

  - **mrob** · [2023-06-25 21:33 UTC](https://news.ycombinator.com/item?id=36472813)
    The "inexplicable" addition of 0.4 to the round multiples of 50 looks like it's there to stop people claiming that limits apply after rounding to the nearest fifty. ^c36472813

    If the threshold is 50, people might claim 74 is acceptable because it rounds to 50. If the threshold is 50.4 this is obviously false.

- **sandworm101** · [2023-06-25 15:15 UTC](https://news.ycombinator.com/item?id=36469071)
  \>\> I noticed something strange in the iOS weather app: The air quality index seems to be defined relative to the country from which one accesses the air quality map. ^c36469071

  Yup.  And if you look closely the underlying map also sometimes changes based on which country one is standing in (Crimea/Taiwan).  Services like iOS are not scientific but consumer and government-focused services.  They exist to appease a host of interested parties, not to render dispassionate information.

  - **mfer** · [2023-06-25 16:54 UTC](https://news.ycombinator.com/item?id=36470219)
    Who defines  what is “good” air quality in a dispassionate way? Or any of the other levels. ^c36470219

    If they just showed numbers without colors, how would the UX work for the general public who isn’t all that knowledgeable?

    Building a useful \[1\] experience while dealing with groups who read things differently isn’t easy and it’s not going to lead to global consistency because people are diverse and inconsistent

    \[1\] [https://www.nngroup.com/articles/usability-101-introduction-...](<https://www.nngroup.com/articles/usability-101-introduction-to-usability/>)

    - **mattnewton** · [2023-06-25 16:58 UTC](https://news.ycombinator.com/item?id=36470277)
      I think the poster is referring to governments that want to control this information too. There are often allegations that China is censoring AQI information for political purposes on iOS [https://9to5mac.com/2018/01/30/weather-app-air-quality/](<https://9to5mac.com/2018/01/30/weather-app-air-quality/>) ^c36470277

      I believe one of the controversial aspects of Google’s “project dragonfly”, (the now scrapped reintroducing-google-search-for-China initiative) were modules that check with Chinese government servers for displaying knowledge cards deemed sensitive, and air quality reports were one of those.
      [https://amp.theguardian.com/technology/2018/nov/27/google-em...](<https://amp.theguardian.com/technology/2018/nov/27/google-employees-letter-censored-search-engine-china-project-dragonfly>)

    - **moritzwarhier** · [2023-06-25 17:40 UTC](https://news.ycombinator.com/item?id=36470770)
      Maybe the WHO? ^c36470770

      If the air makes people sick is a pretty objectively quantifiable question.

      The differences go beyond unit conversion and a main issue is how much we are used to tolerate people dying early or having seriously reduced quality of their lives because of pollution.

      Especially in urban and industrial areas.

      What adds to the complexity is that air quality can vary significantly within a city. Compare having a flat between two busy roads and a nice house in the suburbs.

      And compare that flat between two busy roads to a room next to a factory in the global south, or the US, or in Europe.

      It's a question of how many suicides, cancers, strokes etc we want to tolerate.

      There are studies quantifying the effects of these "local differences". And they are easy to find.

      To me, pretending this was a question of culture or genetics is malicious obfuscation of the actual issues - not accusing you personally, but this is the essence of the combination of many of the comments here.

      Air quality is measurable using several objective categories of pollutants.

      Standardizing the units is one issue, facing the reality of millions of casualties per year is another one.

  - **brookst** · [2023-06-25 15:52 UTC](https://news.ycombinator.com/item?id=36469538)
    Many products have multiple stakeholders. I can't think of a single product that exists "to render dispassionate information" and nothing else. ^c36469538

    - **crazygringo** · [2023-06-25 17:01 UTC](https://news.ycombinator.com/item?id=36470308)
      Really not sure what your point is? The temperature and humidity values that iOS Weather reports are objective and "dispassionate", no? Likewise wind speed and so forth? ^c36470308

      AQI is unique in this case, in that it is a color-coded *interpretation* of combining multiple underlying objective values (PM2.5, etc.). And different governments have chosen different official national schemes for this, according to what they want the population to consider "normal"/green.

      Which means that air-polluting industry in one country might lobby for a wider "green" band. Nothing like that is happening around temperature or humidity as far as I'm aware on iOS.

      (Though I do believe Beijing had a history of under-reporting official maximum daytime summer temperatures, since people couldn't work outdoors above a certain threshold.)

      - **mistercheph** · [2023-06-25 20:32 UTC](https://news.ycombinator.com/item?id=36472310)
        No, they are neither objective nor dispassionate, despite being grounded in empirical data and methods. ^c36472310

        Factors like building shade, vehicle density, wind cover, terrain, cloud coverage, and variations in humidity, mean that thermometers placed at different points in any selected area will report massive variations in temperature, and the naive (and impossible) approach of even distributions of identical sensors taking measurements at the same clock times placed across some given weather area will yield numbers that are not helpful for most people.

        For example, about 1/3 of the area of Burbank, CA is recreation and park spaces that are in the verdugo mountains, at their highest point within Burbank limits 1800 ft. above sea level, and with almost zero residents. The other 2/3 of Burbank are about 600 ft. above sea level. How would you offer a number that summarized the weather in Burbank?

        Imagine factoring time into this. There is no temperature of the hour, there are individual measurements taken at specific moments in time in specific places, using differing methodologies, different equipment, variations in MoE, and at varying frequencies. Put all this together, and the work of the observational meteorologist to produce daily or hourly temperature averages becomes extremely complicated, and the first question they would ask is, "What will the averages be used for?"

        Here are some examples from the *large* literature on these problems:

        [https://www.tandfonline.com/doi/full/10.1080/07055900.2015.1...](<https://www.tandfonline.com/doi/full/10.1080/07055900.2015.1135784>)

        [https://www.sciencedirect.com/science/article/abs/pii/S00221...](<https://www.sciencedirect.com/science/article/abs/pii/S0022169496031289>)

        [https://link.springer.com/chapter/10.1007/978-1-935704-35-5\_...](<https://link.springer.com/chapter/10.1007/978-1-935704-35-5_14>)

        - **crazygringo** · [2023-06-25 21:15 UTC](https://news.ycombinator.com/item?id=36472661)
          You make a good point that the phone isn't (usually) reporting a direct measurement, but is rather interpolating weather station temperatures for a single coordinate. (And cities generally have a single lat/lon "center" for weather reporting, although your iPhone will attempt to report the weather for *your* location rather than the nearest city's center.) ^c36472661

          But nevertheless, a correct, objective, dispassionate temperature reading for that coordinate does exist in reality. And the phone's weather service is trying to approximate that as closely as possible. And you can objectively measure the error to improve future models.

          My point is still that this is qualitatively different from composite air quality indexes, which are politically designed, and therefore designed differently for different countries.

      - **rodgerd** · [2023-06-25 21:37 UTC](https://news.ycombinator.com/item?id=36472841)
        \> The temperature and humidity values that iOS Weather reports are objective and "dispassionate", no? ^c36472841

        You sound like someone who has never lived anywhere that people bitch and moan about the temperature on the weather reports being wrong because people think it's warmer than weather stations report, and get into arguments that the weather stations aren't placed correctly.

      - **calsy** · [2023-06-26 00:37 UTC](https://news.ycombinator.com/item?id=36474243)
        Air quality is not a weather measurement like temperature or humidity, far from it.  Air quality is greatly influenced by human activity and is an extremely contentious issue in many countries. ^c36474243

      - **benatkin** · [2023-06-25 17:37 UTC](https://news.ycombinator.com/item?id=36470746)
        \> air-polluting industry ^c36470746

        Like producing food? A wider green band than what, the Netherlands map?

        I think it's nice to be able to aspire to live in a green area. That one leaves little options, and paints a bleak picture.

      - **thebruce87m** · [2023-06-25 18:07 UTC](https://news.ycombinator.com/item?id=36471028)
        The way things are going I’m sure there will be some questioning the temperature and humidity values and how we really know if they are true or not. ^c36471028

        - **crazygringo** · [2023-06-25 18:18 UTC](https://news.ycombinator.com/item?id=36471123)
          As long as we can buy thermometers and hygrometers to verify with our own eyes, I don't think too many people will be questioning them. ^c36471123

          And as long as ice continues to freeze at 32°F and water continues to boil at 212°F, I don't think anybody will be questioning the accuracy of the thermometers they buy.

    - **wahnfrieden** · [2023-06-25 16:40 UTC](https://news.ycombinator.com/item?id=36470059)
      To recognize stakeholders says nothing of their power dynamics. You're obfuscating by generalizing ^c36470059

    - **verelo** · [2023-06-25 16:34 UTC](https://news.ycombinator.com/item?id=36469986)
      I guess you don’t own a TV /s ^c36469986

- **hombre\_fatal** · [2023-06-25 12:27 UTC](https://news.ycombinator.com/item?id=36467497)
  Interesting. This seems like the reasonable way to do it. ^c36467497

  What global scale would you pick otherwise? And would it be sensitive enough to show gradients in the least/most polluted countries and cities or would it just fill them in with one color?

  - **owl110** · [2023-06-25 13:15 UTC](https://news.ycombinator.com/item?id=36467895)
    I think the problem is that the colors have different meaning. The values in the screenshot for Amsterdam using the NL scale translates to 'insufficient' and while the DE scale translates to 'good' for the same city at the same time. ^c36467895

    At the very least, it means that a user cannot use these scales for inference without knowing/understanding the technology behind them. This is probably not the intention behind showing an air quality indicator in the iOS app.

    - **klausa** · [2023-06-25 14:43 UTC](https://news.ycombinator.com/item?id=36468671)
      The colors are usually defined by the same bodies that define the scales. ^c36468671

      The German LQI has associated colors, I know for sure the American does too, and I’ll bet the Dutch in the screenshots also comes directly from the definition of the scale.

      And iOS defaulting to \_local\_ standards is a good thing! It means people get the same information they would from watching TV or reading newspaper, which is much more useful for most people than comparing their air quality to that of a neighboring country.

      - **cyanydeez** · [2023-06-27 12:23 UTC](https://news.ycombinator.com/item?id=36491802)
        The point though is they can't actually compare it to their neighbors. There's no objective standard, just local baselines and hazard lines decided by political will and history. ^c36491802

        - **klausa** · [2023-06-27 13:17 UTC](https://news.ycombinator.com/item?id=36492283)
          And that’s the correct tradeoff. ^c36492283

          - **cyanydeez** · [2023-06-27 16:06 UTC](https://news.ycombinator.com/item?id=36494769)
            For Apple, yes.  For people who want more valid info for health reasons, no. ^c36494769

            - **klausa** · [2023-06-27 18:03 UTC](https://news.ycombinator.com/item?id=36496493)
              No, that is the correct tradeoff for the \_vast\_ majority of the users. ^c36496493

              The built-in weather services in the OS should cater to the majority of the use cases, not a tiny and narrow minority.

              And I hope we can agree that „people who distrust their own and neighboring countries pollution scales and need to compare them frequently” is not a wide-spread and mainstream position.

              - **cyanydeez** · [2023-06-28 21:40 UTC](https://news.ycombinator.com/item?id=36512996)
                As I said, teres people with health conditions wo don't care what the relative scales are. They want to know the absolute value to determine their health choices. ^c36512996

                Sure, they aren't traveling enough to be catered to by apple, but it's a valid criticism.

    - **joshgachnang** · [2023-06-25 14:06 UTC](https://news.ycombinator.com/item?id=36468320)
      The colors having different meanings shouldn't come up in typical cases, because who's looking at their air quality map from two different countries? There's also a key to the upper left. ^c36468320

      It's interesting and well designed IMO. I don't think this actually causes issues for any users.

      - **capitainenemo** · [2023-06-25 14:31 UTC](https://news.ycombinator.com/item?id=36468527)
        The difficulty seems to be that depending on what country you are in, the colours you are used to will have different meanings. ^c36468527

        Hopefully the german definition of good air quality isn't too overly optimistic, or someone with actual health issues might get a surprise if they are used to being ok on days with a certain "colour" when traveling.

        - **hombre\_fatal** · [2023-06-25 14:52 UTC](https://news.ycombinator.com/item?id=36468777)
          Well, they said the AQ for NL was “insufficient” but the same value was “good” according to Germany. So it’s not just different colors, it’s different standards for AQ. ^c36468777

          I guess you’re proposing that the AQ meter always use the scale of your home country. Doesn’t seem unreasonable but also seems like a quibble so tiny that it could be defeated if someone more knowledgeable offered a single reason against it.

          - **capitainenemo** · [2023-06-25 14:57 UTC](https://news.ycombinator.com/item?id=36468824)
            Hm. That seemed unnecessarily contentious.  We were largely in agreement.  Yes, the german one is using more lax standards, as I was saying, hopefully not too lax, but yes, the colours indicate entirely different standards. ^c36468824

            And yes, I think a simple solution would be to use the colour of your home country that you are used to.  Presumably if you moved, you could just learn the standards of your new country.  A consistent standard that you can rely on in your phone when on a trip to another country definitely seems more useful if you are actually relying on this iOS app.  It could be a simple app pref, a little toggle switch..

      - **stapled\_socks** · [2023-06-25 15:52 UTC](https://news.ycombinator.com/item?id=36469528)
        \> The colors having different meanings shouldn't come up in typical cases, because who's looking at their air quality map from two different countries? ^c36469528

        Anyone who travels between countries?

      - **seszett** · [2023-06-25 16:07 UTC](https://news.ycombinator.com/item?id=36469710)
        \> who's looking at their air quality map from two different countries? ^c36469710

        I do it a few times per week while I commute from Belgium to France and when I'm doing my groceries in whichever country is best for what I need. I'm interested in the air quality in France when I'm leaving Belgium, and in the quality in Belgium when I'm leaving France.

        I don't look at them from iOS though so I don't really have any problem. But crossing borders is a rather common thing around here.

      - **kortilla** · [2023-06-25 15:11 UTC](https://news.ycombinator.com/item?id=36469022)
        \> because who's looking at their air quality map from two different countries ^c36469022

        People that travel. Are you serious?

      - **unknown** · [2023-06-25 14:36 UTC](https://news.ycombinator.com/item?id=36468581)
        [deleted] ^c36468581

  - **treffer** · [2023-06-25 12:29 UTC](https://news.ycombinator.com/item?id=36467516)
    And the image shows that the scale is named differently. ^c36467516

    So very likely tied to the most common national air quality scale.

    So it's explicit in what it shows.

  - **yosito** · [2023-06-25 12:50 UTC](https://news.ycombinator.com/item?id=36467686)
    I use US AQI, and hadn't really realized that many countries have their own measurement. I also usually look at µg/m3 of PM2.5, which is a universal standard, but of course doesn't tell the whole story of air quality. ^c36467686

  - **amelius** · [2023-06-25 12:50 UTC](https://news.ycombinator.com/item?id=36467685)
    Aren't these countries both in the EU? I'd expect an EU-wide scale. ^c36467685

    - **mikerg87** · [2023-06-25 13:04 UTC](https://news.ycombinator.com/item?id=36467793)
      You are correct they should both be using the Common Air Quality Index (CAQI). There is a new standard the EAQI and perhaps Germany has already switched to that standard. ^c36467793

      [https://en.wikipedia.org/wiki/Air\_quality\_index](<https://en.wikipedia.org/wiki/Air_quality_index>)

- **nullindividual** · [2023-06-25 16:08 UTC](https://news.ycombinator.com/item?id=36469721)
  I should be able to translate what my local government/news says about air quality, just like any other portion of the weather forecast (C, F, etc). ^c36469721

  Information based on user locality seems like an excellent design.

  - **908B64B197** · [2023-06-25 16:42 UTC](https://news.ycombinator.com/item?id=36470089)
    \> what my local government/news says about air quality ^c36470089

    That's assuming the local government is giving the truth regarding air quality and that their "official scale" is made to reflect reality and not obscure some measurements.

    - **nullindividual** · [2023-06-25 17:08 UTC](https://news.ycombinator.com/item?id=36470393)
      Let's not go there. Unsubstantiated conspiracy theories do not add to this discussion. ^c36470393

      - **calsy** · [2023-06-25 19:32 UTC](https://news.ycombinator.com/item?id=36471771)
        Unlike basic weather metrics like temperature, humidity etc. Air quality measurements are directly impacted by human activity and are extremely contentious. ^c36471771

        In my hometown, there is a fight between locals and waste operators over excessive burn offs. The validity of air quality readings from the area are being tested in court.

        In the past, the Vietnamese government removed IQAir from the App Store and Google Play as citizens became increasingly concerned about the air quality in the capital cities.

        You wont learn much if you label everything you don't understand a 'conspiracy theory'. Air quality is not just another weather measurement.

      - **908B64B197** · [2023-06-25 17:36 UTC](https://news.ycombinator.com/item?id=36470737)
        \> Unsubstantiated ^c36470737

        \[0\] [https://www.sciencedaily.com/releases/2021/04/210421151224.h...](<https://www.sciencedaily.com/releases/2021/04/210421151224.htm>)

        \[1\] [https://www.globaltimes.cn/page/202106/1225792.shtml](<https://www.globaltimes.cn/page/202106/1225792.shtml>)

      - **bluecalm** · [2023-06-25 17:17 UTC](https://news.ycombinator.com/item?id=36470514)
        A Government massaging the data to make the situation look better than it is doesn't qualify as a conspiracy theory. Rather as expected outcome if anything. ^c36470514

        The point is that the raw data is always the most valuable. Translating it is an easy task that can be done if the user wishes so.

    - **cyanydeez** · [2023-06-27 12:27 UTC](https://news.ycombinator.com/item?id=36491821)
      Or that it's legal to translate national information. ^c36491821

      Remember when trump defaced a NOAA weather map? Everyone knew he broke a law.

      Now imagine advertising a local quality data set and giving it your own advisory information.

      Great: open source

      Not a chance: Apple

- **teekert** · [2023-06-25 21:43 UTC](https://news.ycombinator.com/item?id=36472912)
  I live in the Netherlands, I've tried to get this air quality report out of the iOS app, so have others. It just tells me every day the air is shit. I mean when you tap on it, it tells you not to exercise outside for example. It's rarely "good", mostly it is "insufficient", sometimes it's "very bad". ^c36472912

  Is it really so bad? You don't hear anything about it from other sources... Tapping on, one finds the main pollutant to be ozone, "usually caused by traffic and it can be transported over large distances."

  Idk what to think of this. Many people seem confused. Are we really in such poor air all the time?

  Sometimes I bike through the fields in the morning, sniff the fresh humid air that has a coldness in it, I smell grass and flowers... Apple tells me: Insufficient (don't bike to fast!) :(.

  Maybe they are right, maybe they are forcing us to come to terms with the things we do to our air.

  - **esafak** · [2023-06-25 22:34 UTC](https://news.ycombinator.com/item?id=36473359)
    Sounds like a bug. I don't recall the Netherlands having bad air; it's pretty green. I wonder how this can be reported? ^c36473359

- **can16358p** · [2023-06-25 14:32 UTC](https://news.ycombinator.com/item?id=36468540)
  I've never ever seen air quality in iOS. Probably not available where I live. You guys at least, well, have it. ^c36468540

  - **pridkett** · [2023-06-25 15:12 UTC](https://news.ycombinator.com/item?id=36469037)
    You might have to dig for it - I didn’t know this feature was available before this post. You need to click on the map button then toggle the air quality layer. ^c36469037

    Seems to cover most of the US, Canada, Mexico. Western Europe is largely present but is missing a handful of countries (Belgium, Luxembourg, Ireland, Switzerland, Austria, Liechtenstein, Portugal, and Iceland). Also covers most of Japan and South Korea and small localized portions of India and China.

    - **can16358p** · [2023-06-26 02:06 UTC](https://news.ycombinator.com/item?id=36474880)
      Well I live in Turkey so it doesn't seem covered. ^c36474880

  - **smileybarry** · [2023-06-25 15:06 UTC](https://news.ycombinator.com/item?id=36468966)
    Apple don't have it enabled for all regions, even if Breezometer have data there. (E.g.: looks like they have \[fairly good\] data here \[in Israel\], but AQI is disabled in Apple Maps) ^c36468966

    - **almokhtar** · [2023-06-25 15:26 UTC](https://news.ycombinator.com/item?id=36469216)
      you mean palestine ? ^c36469216

- **DangerousPie** · [2023-06-25 13:51 UTC](https://news.ycombinator.com/item?id=36468173)
  I have never understood how to interpret AQI in iOS. Confusingly, the UI will (edit: or at least used to?) say "Air Quality: Low" when what it means is that the pollution level is low (ie. air quality is high). Somewhat disappointing coming from Apple. ^c36468173

  - **evanriley** · [2023-06-25 13:56 UTC](https://news.ycombinator.com/item?id=36468223)
    Hmm, what country does this happen in? I've never seen it use Low/High, only from Good to Hazardous. ^c36468223

    - **jsjohnst** · [2023-06-25 14:23 UTC](https://news.ycombinator.com/item?id=36468444)
      Same for me in US English. For example, right now it’s “18 - Good”. It was “469 - Hazardous” just three weeks ago though. ^c36468444

      - **calsy** · [2023-06-26 00:39 UTC](https://news.ycombinator.com/item?id=36474249)
        Happen to have any large fires nearby? ^c36474249

        - **jsjohnst** · [2023-06-28 10:38 UTC](https://news.ycombinator.com/item?id=36504641)
          Yep, the Ontario Canada wildfires destroyed air quality for the NE part of the US. ^c36504641

    - **DangerousPie** · [2023-06-25 14:00 UTC](https://news.ycombinator.com/item?id=36468268)
      In the UK for example. ^c36468268

      - **cjrp** · [2023-06-25 14:11 UTC](https://news.ycombinator.com/item?id=36468345)
        Right now mine says “Air pollution: low. Air quality index is 3”. Apparently using the DAQI for classification ^c36468345

        - **DangerousPie** · [2023-06-25 14:45 UTC](https://news.ycombinator.com/item?id=36468694)
          Huh, looks like you're right. Maybe they fixed it at some point? ^c36468694

  - **hombre\_fatal** · [2023-06-25 14:41 UTC](https://news.ycombinator.com/item?id=36468644)
    Did the green color on the green to yellow to orange to red scale bar never tip you off? ^c36468644

- **zerealshadowban** · [2023-06-25 15:58 UTC](https://news.ycombinator.com/item?id=36469601)
  I've been using the PurpleAir website (map.purpleair.com) for many years now, mostly out of concern for heavy wildfire pollution and winter inversions vs personal outdoor+athletic activities; one interesting aspect is that you can buy your own sensor and thus join the community of local sensors for increased accuracy of measurements. They let you pick between various international standards and types of pollutants. They seem to have a dense network of sensors in North America, not sure about the rest of the world. ^c36469601

- **bilekas** · [2023-06-25 15:03 UTC](https://news.ycombinator.com/item?id=36468926)
  In Italy I have noticed that the air quality is usually considered bad only in places that actually have data. For a lot of the places that are considered good, checking the sources for them usually result in only 1 device. ^c36468926

  It's a nice to have certainly but I wish it was more consistent.

  - **studmuffin650** · [2023-06-25 15:14 UTC](https://news.ycombinator.com/item?id=36469067)
    As someone who just visited Italy for the first time in 10 years, I was surprised how polluted the air was (especially around the coast). While the air quality was marked as “OK”, it was quite hazy and you could actually see the smog in the air. Just something that really took me by surprise as when I think of polluted areas, the Amalfi coast is not an area that comes to mind ^c36469067

- **davidkuennen** · [2023-06-25 13:07 UTC](https://news.ycombinator.com/item?id=36467828)
  I'm also curious why there's no data for countries like Belgium, Switzerland and Austria. ^c36467828

- **rkapsoro** · [2023-06-25 18:04 UTC](https://news.ycombinator.com/item?id=36471012)
  Yeah, I've noticed this too. ^c36471012

  It looks like the air quality models that iOS Weather is using are integrated into a single system, and then that system is asked to render maps in any of the different regions' AQI systems.

  Which means, as OP has observed, if you open the map from one region, and then navigate the map viewer to another region, you can see how the AQI scoring system from the first region would evaluate the second. Which is rather interesting.

  Also fwiw I've reckoned that these AQI models are clearly highly algorithmic, extrapolating and synthesizing data where sensors are not available.

- **404mm** · [2023-06-25 14:30 UTC](https://news.ycombinator.com/item?id=36468521)
  Somewhat related, Apple’s Air Quality data source (breezometer) is now owned by Google. ^c36468521

  I wonder what Apple is going to do about it. Will it be just one of their data sources or are they going to acquire their own?

  - **lotsofpulp** · [2023-06-25 14:48 UTC](https://news.ycombinator.com/item?id=36468721)
    I am curious how reliable that air quality data is in the first place.  I cannot find anything about Breezometer having invested in installing air quality meters all around the world. ^c36468721

    [https://www.calcalistech.com/ctechnews/article/sycbrdpbi](<https://www.calcalistech.com/ctechnews/article/sycbrdpbi>)

    This article says they are using “machine learning” and “AI”.  Makes me think it is all fake.

    [https://www.breezometer.com/pdfs/Ultimate-Guide-to-BreezoMet...](<https://www.breezometer.com/pdfs/Ultimate-Guide-to-BreezoMeter_s-Air-Quality-Technology.pdf>)

    Their own documentation indicates the air quality measures they provide are just guesses based on their models.  Page 4 basically says actually measuring particulates in the air is very costly, and so their solution is to come up with models to predict what it might be.

    - **pnpnp** · [2023-06-25 14:58 UTC](https://news.ycombinator.com/item?id=36468845)
      Yes - it’s much like now weather forecasting works. ^c36468845

      Data points may come from 2 places 100 mi apart, but what if someone lives between them?

      Temperature or other weather data is often an extrapolation based on official weather data collection points, and AQI data is no different.

      *How* that data gets extrapolated varies wildly by implementation.

      *edit:* Also a fun fact, I live 2000ft above and 50mi from the nearest forecasting center in a valley. “Weather apps” are about as accurate as throwing darts at a board up here, because the models used to extrapolate known data completely fall apart with all the variables.

      Our best source of data is the “short term weather discussion” by NOAA, which just gives some generalizations based on local weather knowledge.

      - **crazygringo** · [2023-06-25 15:56 UTC](https://news.ycombinator.com/item?id=36469575)
        Not just forecasting, but reporting values *right now*. ^c36469575

        Spatial interpolation is much more non-obvious than you might initially assume, when the data points are coming from arbitrary locations and not a regular grid. For anyone curious, here \[1\] is a good place to start, or look up "Kriging interpolation".

        The basic implementation of any kind of continuous temperature estimation is to have a generic equation that relates how temperature naturally varies by altitude, use that normalize the temperature reported by weather stations according to altitude to create a "flat" temperature map, interpolate to create a smooth continuous temperature map using something like Kriging, and then de-normalize the temperature at a desired point according to the altitude of that location.

        There are always going to be hyper-local variations that won't account for (are you on the sunny side or shaded side of a mountain? is there an air current? how is vegetation/buildings/asphalt affecting it?), but it's the basic starting point.

        \[1\] [https://geobgu.xyz/r-2020/spatial-interpolation-of-point-dat...](<https://geobgu.xyz/r-2020/spatial-interpolation-of-point-data.html>)

        - **counters** · [2023-06-25 17:04 UTC](https://news.ycombinator.com/item?id=36470335)
          Eh, kriging is overkill relative to the skill you end up with since fine-grain spatial variability in weather can arise from a lot more than the static factors you can pull into such a scheme. This is why objective analysis techniques are typically preferred. ^c36470335

          More importantly, high-resolution priors are universally available from weather models, so there is no need to just to ever naively interpolate between weather observation stations very far apart.

          One of the reasons that consumer weather apps perform poorly is because in many cases, the companies producing them arbitrarily choose some sort of spatial or temporal resolution requirements, and then throw the problem to an engineer or data scientist who probably doesn't know much more than these simple interpolation techniques (and I absolutely lump kriging into the 'simple' category these days). A modicum of domain knowledge applied here produces a much better product with substantially less effort.

          - **crazygringo** · [2023-06-25 18:15 UTC](https://news.ycombinator.com/item?id=36471102)
            I'm curious if you could expand -- I researched this a while ago but what I'm describing is as deep as I got from various online tutorials. ^c36471102

            What kind of objective analysis techniques? And where does someone get high-resolution priors from? Are you saying that companies have gone out and done a one-time mapping of temperature etc. at a e.g. 1-mile grid across the US? (Which would be over 3 million points at that scale, compared to the \~10,000 US weather stations?)

            - **counters** · [2023-06-25 22:03 UTC](https://news.ycombinator.com/item?id=36473080)
              Probably the two most common and simplest are Barnes and Cressman interpolation (see \[1\] for a modern implementation of Barnes), which use inverse distance weighting to combine observations within a neighborhood. An improvement to these techniques frequently used to grid statistical weather forecasts is the BCDG method (see \[2\]). ^c36473080

              The core idea of any objective analysis/interpolation scheme is that you model spatial relationships with some sort of function. Kriging exemplifies this - you fit a spatial covariance model and use that to predict values in the far field, using combinations of nearby values. I don't really have a good link or textbook reference at arms reach, but you can quickly re-frame this entire interpolation problem as a data assimilation one where you're attempting to approximate a solution to some 2D or 3D field using sparsely sampled observations; in the weather world, the Real-time Mesoscale Analysis used in the USA is a good example of a system which hybridizes a weather model and observations to create a high-resolution analysis \[3\].

              A problem arises when the field you're analyzing can have shocks or variability much smaller than the scale that you're able to measure from your network. A front is a great example - across a front, temperature and wind direction will change over a very small distance, but most interpolation schemes will smear this out. The problem is that you really do care about that front and its location - that's where the interesting weather happens!

              \> And where does someone get high-resolution priors from?

              A high-resolution weather forecast model, which uses physics to simulate the atmosphere and produce reference states. 3-km forecasts are readily and easily available in the US.

              \> Are you saying that companies have gone out and done a one-time mapping of temperature etc. at a e.g. 1-mile grid across the US?

              No, this probably wouldn't be useful. Especially because we get a \~1-km mapping of lower troposphere temperatures from geostationary weather satellites every 10-15 minutes across the entire globe. May not be exactly "surface temperature", but it tells you a whole lot about high-frequency variability in temperature fields.

              \[1\]: [https://gmd.copernicus.org/preprints/gmd-2022-116/gmd-2022-1...](<https://gmd.copernicus.org/preprints/gmd-2022-116/gmd-2022-116.pdf>)
              \[2\]: [https://journals.ametsoc.org/view/journals/wefo/24/2/2008waf...](<https://journals.ametsoc.org/view/journals/wefo/24/2/2008waf2007080_1.xml>)
              \[3\]: [https://journals.ametsoc.org/view/journals/wefo/26/5/waf-d-1...](<https://journals.ametsoc.org/view/journals/wefo/26/5/waf-d-10-05037_1.xml>)

              - **crazygringo** · [2023-06-25 22:07 UTC](https://news.ycombinator.com/item?id=36473106)
                Thank you so much, that's all so fascinating! And makes perfect sense that priors come from high resolution physics solutions. ^c36473106

                Much appreciated for all that info.

      - **aziaziazi** · [2023-06-25 15:40 UTC](https://news.ycombinator.com/item?id=36469365)
        Two differences between weather and AQI forecast: ^c36469365

        \- AQI strongly varies with local human activities, e.g. a coal power plant in between the 2 places 100 miles appart.

        \- temporal and hardly predictable human activities, e.g. a chem industry without good attenuation system that boost its production to fill a special command. Or an attenuation system that breaks.

  - **booi** · [2023-06-25 14:31 UTC](https://news.ycombinator.com/item?id=36468534)
    Is this really an issue? I bet Apple users use gmail too. ^c36468534

    - **404mm** · [2023-06-25 14:41 UTC](https://news.ycombinator.com/item?id=36468646)
      I don’t know. That’s not for me to judge :). I am just pointing it out because they seemed to have an issue with a similar concept in the past (Maps… moving to their own product). ^c36468646

      Unlike Google as their default search engine, accessing weather or air quality API costs money. (While they probably get paid for keeping Google as their default search engine)

    - **speedgoose** · [2023-06-25 14:36 UTC](https://news.ycombinator.com/item?id=36468577)
      They also use Google Search by default. ^c36468577

  - **zitterbewegung** · [2023-06-25 14:36 UTC](https://news.ycombinator.com/item?id=36468579)
    Since its Google, Apple will probably be forced to do something once Google kills it off. ^c36468579

- **tekstart** · [2023-06-26 13:47 UTC](https://news.ycombinator.com/item?id=36479618)
  As a point of clarification, Apple's AQ data is due to their licensing agreement with BreezoMeter (Israel). [http://Breezometer.com](<http://Breezometer.com>)  As a data broker, they acquire/license the data from a variety of sources and the sell the compiled data to licensees with customer-specific data unit (eg. USA \= AQI (EPA std). ^c36479618

- **dylan604** · [2023-06-25 14:02 UTC](https://news.ycombinator.com/item?id=36468279)
  “I noticed something strange in the iOS weather app” ^c36468279

  I’ve noticed that the weather app on my iOS, iPadOS, and watchOS all show differing forecasts with all 3 devices within 18” of each other. AQI is just one of the parts of the forecast that I just don’t pay attention too. Around here in the summer, it is always an alert saying don’t go outside

  - **SkyPuncher** · [2023-06-25 14:13 UTC](https://news.ycombinator.com/item?id=36468361)
    I’m giving up on Apple Weather (despite recently saying it was fine). ^c36468361

    I got burned this past weekend when painting my deck. Forecast was absolutely clear in the window I needed to paint/dry. Just after I started, forecast changed to nearly 100\% rain this wasn’t a case of “oh maybe the chance of rain was wrong”. No, it went from 0 to having a hundred of mile wide storm pass through.  The type of storm that doesn’t just pop up.

    It’s insane how they killed dark sky.

    - **jeffgreco** · [2023-06-25 15:46 UTC](https://news.ycombinator.com/item?id=36469446)
      By killing Dark Sky and their own weather app and pushing me to an annual CARROT Weather subscription, they made themselves a profit of 30\% of the CARROT Weather subscription -\_- ^c36469446

    - **sp332** · [2023-06-25 15:11 UTC](https://news.ycombinator.com/item?id=36469028)
      The past week has been super weird. My local weather station kept predicting rain every day and it barely rained at all. This week, once again, they say thunderstorms every day. We'll see how it goes. ^c36469028

- **Jacobinski** · [2023-06-26 01:12 UTC](https://news.ycombinator.com/item?id=36474488)
  The air quality index displayed is based on the current location that you have set to view the weather. If you want to switch to a different scale: add a new saved location, switch to it, and the view the AQI map. ^c36474488

- **unknown** · [2023-06-25 12:30 UTC](https://news.ycombinator.com/item?id=36467521)
  [deleted] ^c36467521

- **mensetmanusman** · [2023-06-25 13:53 UTC](https://news.ycombinator.com/item?id=36468199)
  'This air quality level is known to cause cancer in California' ^c36468199

  - **dylan604** · [2023-06-25 14:03 UTC](https://news.ycombinator.com/item?id=36468292)
    California air quality used to cause acid rain, so cancer was the least of the problems. So at least they’ve gotten to the point where you can now worry about the cancer ^c36468292

  - **404mm** · [2023-06-25 14:27 UTC](https://news.ycombinator.com/item?id=36468479)
    Wildfires will do that :( ^c36468479

- **andix** · [2023-06-25 20:24 UTC](https://news.ycombinator.com/item?id=36472229)
  I didn't know that there is actually any data for this view. With an Austrian iPhone the air quality map is always empty "no data". Also for Germany and the Netherlands. ^c36472229

- **Arn\_Thor** · [2023-06-25 13:19 UTC](https://news.ycombinator.com/item?id=36467919)
  That’s why I like Air Matters. You can choose your scale ^c36467919

- **Nocturium** · [2023-06-25 13:47 UTC](https://news.ycombinator.com/item?id=36468139)
  [flagged] ^c36468139

  \[flagged\]

- **Havoc** · [2023-06-25 13:02 UTC](https://news.ycombinator.com/item?id=36467785)
  I mean tech is full of conflicting standards. (see relevant xkcd...) ^c36467785

  In this particular case the actual values just happen to land on the edge of two colours in the scales with very different connotations - orange vs green.

  - **unknown** · [2023-06-25 18:53 UTC](https://news.ycombinator.com/item?id=36471420)
    [deleted] ^c36471420

  - **unknown** · [2023-06-25 17:39 UTC](https://news.ycombinator.com/item?id=36470759)
    [deleted] ^c36470759

