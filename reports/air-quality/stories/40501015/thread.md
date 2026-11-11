# [An air quality model that is evolving with the times](https://news.ycombinator.com/item?id=40501015)

Article: [https://eos.org/science-updates/an-air-quality-model-that-is-evolving-with-the-times](<https://eos.org/science-updates/an-air-quality-model-that-is-evolving-with-the-times>)

Brajeshwar · 2024-05-28 14:22 UTC · 44 reported comments · archived 2026-11-08 13:33 UTC
Observation: 2026-11-08 13:32 UTC → 2026-11-08 13:33 UTC

## Comments

- **culi** · [2024-05-28 16:04 UTC](https://news.ycombinator.com/item?id=40502158)
  \> Since its creation, STEM has evolved to cover a broader set of key air pollutants, such as ozone and particulate matter, ^c40502158

  I've always found air quality metrics focusing on particle size confusing. E.g. PM2.5 (which describes fine inhalable particles, with diameters that are generally 2.5 micrometers and smaller)

  But surely there must be a massive qualitative difference between particulate matter of, e.g., lead vs particulate matter of, e.g., pollen or fungal spores, right? How useful is it really to lump all of these together?

  - **jvanderbot** · [2024-05-28 16:16 UTC](https://news.ycombinator.com/item?id=40502335)
    Yes - there are other poisons as well hidden behind those particles, but it's *very* hard to measure the composition of those particles in real time. Particulate matter *can* be measured with a \$20 sensor from Sparkfun, so it's an often-used proxy. ^c40502335

    As for why the particles sizes are differentiated, I think it's because some sizes can cross barriers into the blood - and are therefore concerning regardless of the contents. pm 2.5 can reach the deepest parts of the lungs and just muck up that whole area regardless and cause all kinds of systemic inflammation. pm 10.0 generally doesn't reach that deep but still causes eye/ nose/ throat problems IIRC.

    If there is near-zero or undetectable particulate matter, then that would preclude lead particles as well, obviously.

    - **hatmatrix** · [2024-05-29 01:51 UTC](https://news.ycombinator.com/item?id=40507516)
      It's widely thought but not conclusively found that there are certain constituents that are more toxic than others. As you say, the problem lies in the ability to measure these constituents more widely. ^c40507516

      However, there is a hypothesis \[1\] that maybe there is something about the collective mass as negative association with health effects have been found all over the world where the composition changes drastically. A more recent hypothesis \[e.g., 2\] is that many health problems from particles stem from persistent reactive oxygen species that cause oxidative stress, and these reactive species form from many different mechanisms so likely scales with the collective mass, which has been serving as a surrogate metric.

      \[1\] [https://doi.org/10.1016/S0048-9697(99)00513-6](<https://doi.org/10.1016/S0048-9697%2899%2900513-6>)

      \[2\] [https://doi.org/10.1038/srep32916](<https://doi.org/10.1038/srep32916>)

    - **culi** · [2024-05-28 20:05 UTC](https://news.ycombinator.com/item?id=40504979)
      This seems like a reasonable explanation, thanks ^c40504979

  - **wnevets** · [2024-05-28 16:26 UTC](https://news.ycombinator.com/item?id=40502476)
    Focusing on PM 2.5 makes sense because anything that size and smaller tend to cause the most harm. \[1\] ^c40502476

    \[1\] [https://www.epa.gov/pm-pollution/particulate-matter-pm-basic...](<https://www.epa.gov/pm-pollution/particulate-matter-pm-basics>)

    \> Particulate matter contains microscopic solids or liquid droplets that are so small that they can be inhaled and cause serious health problems. Some particles less than 10 micrometers in diameter can get deep into your lungs and some may even get into your bloodstream. Of these, particles less than 2.5 micrometers in diameter, also known as fine particles or PM2.5, pose the greatest risk to health.

    - **BobaFloutist** · [2024-05-28 16:50 UTC](https://news.ycombinator.com/item?id=40502739)
      Presumably smaller particles are also more difficult to filter (and therefore more likely to make their way indoors without dedicated filtration), and also expected to remain airborne for a greater distance and duration (because of square cube things). ^c40502739

      - **LordDragonfang** · [2024-05-28 17:42 UTC](https://news.ycombinator.com/item?id=40503334)
        \>Presumably smaller particles are also more difficult to filter ^c40503334

        So, that may or may not be true for just passive filtering (like door and window frames), but it's actually not true for actual hepa-style filters, because the physics of particulate filtering is totally unintuitive from the macro level -- past a certain point, finer particulates actually become easier to filter, because the physics is dominated by two different effects at different sizes.

        [https://dynomight.net/ikea-purifier/\#on-physics](<https://dynomight.net/ikea-purifier/#on-physics>)

        - **tsimionescu** · [2024-05-29 00:09 UTC](https://news.ycombinator.com/item?id=40506884)
          I don't think it's all that un intuitive, as long as you know that there is an electrostatic effect used for filtering. We all know that it's easier to attract a lighter object with an electrostatically charged ruler, so it's quite easy to imagine that very fine (so, light) particles are easier to to attract than larger heavier ones as well. ^c40506884

      - **hedgehog** · [2024-05-28 17:42 UTC](https://news.ycombinator.com/item?id=40503331)
        PM2.5 is around the hardest size to filter, I don't understand the physics but both larger and smaller are actually easier to remove from the air. Given that 2.5 is a useful estimate of worst case performance for a given setup. ^c40503331

        - **TylerE** · [2024-05-28 17:55 UTC](https://news.ycombinator.com/item?id=40503496)
          Basically a HEPA/electrostatic filter works in two ways. ^c40503496

          As a “physical” filter (think fishing net), works well on big particles.

          As an electrostatic filter, works best with really small, works by electrically attracting particles and having them stick.

          2\.5 micron is in the middle crossover range where total net effectiveness is worst. Respirators are rated at the same size for the same reason.

    - **4death4** · [2024-05-28 16:52 UTC](https://news.ycombinator.com/item?id=40502763)
      Yes, but isn’t lead getting into your bloodstream worse than pollen? I mean oxygen gets into your bloodstream via inhalation… ^c40502763

      - **wnevets** · [2024-05-28 17:06 UTC](https://news.ycombinator.com/item?id=40502899)
        Which plant produces pollen at PM2.5 tho? Pollen usually isn't entering your bloodstream through your lungs, its too large. ^c40502899

        - **semi-extrinsic** · [2024-05-28 17:37 UTC](https://news.ycombinator.com/item?id=40503271)
          Pollen particles are quite fragile and tend to break up into PM2.5 and smaller, especially during rain events. See for instance the reference below. ^c40503271

          [https://doi.org/10.1016/j.aeaoa.2022.100177](<https://doi.org/10.1016/j.aeaoa.2022.100177>)

        - **culi** · [2024-05-28 20:08 UTC](https://news.ycombinator.com/item?id=40505001)
          In addition to pollen, there are spores from both mushrooms and ferns. Both of which are common cloud-seeding particles and can often be PM2.5 ^c40505001

      - **tomrod** · [2024-05-28 19:31 UTC](https://news.ycombinator.com/item?id=40504621)
        Most pollen is captured at pm10 or higher level. PM2.5 tends to be created by humans ^c40504621

        Crossing the blood brain barrier exacerbates not only asthma but other vascular/heart and related diseases, including diabetes, as well as lung diseases.

      - **bluGill** · [2024-05-28 16:55 UTC](https://news.ycombinator.com/item?id=40502805)
        Worse in what way?  Lead is a long term neurotoxin, but pollen triggers the immune system and makes you miserable.  Both are bad but in different ways. ^c40502805

        - **4death4** · [2024-05-28 18:04 UTC](https://news.ycombinator.com/item?id=40503595)
          It’s really unclear to you why a long term neurotoxin that leads to lifelong disability is worse than allergy producing pollen? ^c40503595

          - **bluGill** · [2024-05-28 18:27 UTC](https://news.ycombinator.com/item?id=40503856)
            It isn't clear until you are suffering from allergies, and notice that old people who used to chew on lead fishing weights are not all that bad off. Most people with high lead in their bodies don't realize the issue nor to the people they know. ^c40503856

            - **alright2565** · [2024-05-28 19:13 UTC](https://news.ycombinator.com/item?id=40504399)
              \> used to chew on lead fishing weights ^c40504399

              Chunks of lead just aren't that bad. [https://doi.org/10.2146/ajhp060175](<https://doi.org/10.2146/ajhp060175>) lists common sources of lead poisoning, and none of them are lead weights.

              Common sources involve things like airborne lead powder (from grinding or smelting), lead compounds dissolved in food & water, paint, and lead in soil.

  - **luma** · [2024-05-28 22:52 UTC](https://news.ycombinator.com/item?id=40506454)
    PM2.5 is of interest because it’s a size that your body has a harder time getting rid of.  Larger size particles have an easier time being captured by the upper respiratory system. Smaller things might make it into the blood stream and hopefully be filtered by the kidneys.  2.5 microns is right at the point between where either thing is less likely to happen and instead the stuff might get stuck in your lungs. ^c40506454

  - **nonamousnoose** · [2024-05-28 16:20 UTC](https://news.ycombinator.com/item?id=40502391)
    They are separated by size because that determines which airways they migrate to, and which can enter the bloodstream. Yes, what they're made of matters - the latter is also measured in specific studies, but the former is a lot easier/cheaper to systematically measure. ^c40502391

  - **photochemsyn** · [2024-05-28 18:09 UTC](https://news.ycombinator.com/item?id=40503668)
    Getting the data on the chemical composition of the PM2.5 fraction of air pollution requires fairly advanced instrumentation and lab capabilities.  It is the important data in estimating toxicity, for example: ^c40503668

    [https://meetingorganizer.copernicus.org/EGU24/EGU24-881.html](<https://meetingorganizer.copernicus.org/EGU24/EGU24-881.html>)

    \> "It was found that PM chemical composition was major determinant in toxicity assessment rather than its mass concentration."

  - **BunsanSpace** · [2024-05-28 16:50 UTC](https://news.ycombinator.com/item?id=40502746)
    Canada is updating their model to be the worst of PM2.5 and their traditional models of common pollutants. ^c40502746

    Part of the issue is the existing model does an average over 3 hours, where PM2.5 can change rapidly (fire, traffic surge, &c). So they have a second metric that is averaged over an hour.

    - **hadlock** · [2024-05-29 18:49 UTC](https://news.ycombinator.com/item?id=40515390)
      Putting a frozen pizza in the oven can spike most apartments to 300 in under 10-12 min, especially if you leave it in too long at 450F ^c40515390

  - **londons\_explore** · [2024-05-28 16:08 UTC](https://news.ycombinator.com/item?id=40502214)
    Indeed - clearly it matters what the particles are made from.   Some stuff won't even be toxic, like particles of water (fog). ^c40502214

  - **taeric** · [2024-05-28 16:18 UTC](https://news.ycombinator.com/item?id=40502369)
    I mean, yes, toxins in the air are worse than non-toxins in the air.  I don't think anyone will really debate that. ^c40502369

    The banal answer to your question is you measure what is easy to measure.  And it is easier to build a device that can measure size of particles than one that can enumerate all of the types.  Especially since you will take the same actions regardless?  Put up a filter and run it.

    - **hollerith** · [2024-05-28 16:24 UTC](https://news.ycombinator.com/item?id=40502453)
      \>Put up a filter and run it. ^c40502453

      It's not that simple because any filtration media that will filter out, e.g., diesel exhaust or pollen will lyse the bacteria that are always floating in the air, thereby adding to the air that leaves the filtration device the lipopolysaccharide (LPS) toxin that without the action of the filtration device would remain relatively-safely inside the bacterium. Yes, even without any air purifiers, you will absorb some LPS toxin from the bacteria in the air you breath, but running an air purifier approximately doubles the dose. I claim to be able to tell the difference in that when I'm in a small room with an air purifier running at high fan speed, I am much more likely to feel a certain kind of non-severe, but not-good headache-like feeling.

      I.e., you don't want to run an air purifier that removes very small particles from the air when you don't need to -- at least if you are as sensitive to LPS as I am. And you don't want the fan speed of the purifier's being higher than necessary.

      - **InitialLastName** · [2024-05-28 16:52 UTC](https://news.ycombinator.com/item?id=40502771)
        I'm gonna need a source on that, as the only relevant thing that comes up on a search for "lipopolysaccharide toxin air filter" is a single study \[0\] that tested a single air purifier (whose filter had not been changed in a year) in a single room. It includes the telling phrase: "The conclusions here, however, should be interpreted cautiously due to the small sample size here." ^c40502771

        \[0\] [https://www.sciencedirect.com/science/article/pii/S016041202...](<https://www.sciencedirect.com/science/article/pii/S016041202031833X>)

        - **hollerith** · [2024-05-28 17:45 UTC](https://news.ycombinator.com/item?id=40503373)
          \>I'm gonna need a source on that ^c40503373

          Sadly, I was unable to find a link to the study I got my info from after searching my notes for about 7 minutes.

      - **taeric** · [2024-05-28 18:00 UTC](https://news.ycombinator.com/item?id=40503553)
        It can be more complicated, yes.  I assert that it usually isn't.  You don't spend time worrying as much about what the contaminants are, you just drive them to zero. ^c40503553

        I grant the point that you don't want to just stir up the air.  Which is why you don't just run a fan, necessarily.

- **hendler** · [2024-05-28 16:58 UTC](https://news.ycombinator.com/item?id=40502832)
  Air quality is not thought enough of in terms of localized data. Some modeling works at larger scales,  but if you want to know the forecast for other pollutants (especially ones that disperse or transition) or the source of methane leaks, you need very localized data from many modalities (wind direction, temperature, topographic, seasonal, traffic, etc). ^c40502832

  I worked at [https://aclima.io](<https://aclima.io>) on air quality for 6.5 years. My role was managing backend data pipelines, but I worked with scientists and data scientists who were pushing the boundaries of models' capabilities. Models are complex and expensive - any advancement here, like Graphcast, is very important. \[1\] One job our team was responsible for is to reduce the cost of high quality data, so we drove vehicles around to collect very localized data, which ended up being temporally sparse. Modeling can fill gaps to some measurable level of certainty.

  It should also be said that policy is far behind the science, but the burden will remain on science and data to continue make conclusions irrefutable.

  \[1\] - [https://deepmind.google/discover/blog/graphcast-ai-model-for...](<https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/>)

  - **selimthegrim** · [2024-05-28 19:31 UTC](https://news.ycombinator.com/item?id=40504623)
    Is there a good email address/way to reach you? I have a couple questions about your past job as well as the product at your current gig. ^c40504623

    - **hendler** · [2024-05-29 00:09 UTC](https://news.ycombinator.com/item?id=40506878)
      sure - twitter.com/Hendler ^c40506878

- **banish-m4** · [2024-05-28 22:28 UTC](https://news.ycombinator.com/item?id=40506286)
  The costs of changing from say a model like the US EPA AQI to something else is it creates fragmentation and breaks comparability and infrastructure that came before. An agreed-upon international "AQ" metric should reflect real risk to sensitive groups and long-term health outcomes. ^c40506286

- **wiz21c** · [2024-05-29 12:24 UTC](https://news.ycombinator.com/item?id=40511179)
  It uses [https://people.cs.vt.edu/\~asandu/Software/Kpp/](<https://people.cs.vt.edu/~asandu/Software/Kpp/>)
  which is free software !!! ^c40511179

- **perlpimp** · [2024-05-29 03:39 UTC](https://news.ycombinator.com/item?id=40508218)
  I like how that freon patent was running out and people coaxed up ozone hole scare alleging that using hair spray and freezers as it would irradiate everyone and kill life on earth. Science establishment gave generous window dressing to this, now firmly forgotten as adjacent patented and as "ozone depleting" as previous ones. ^c40508218

- **jgord** · [2024-05-28 23:48 UTC](https://news.ycombinator.com/item?id=40506768)
  One reason we might want the best possible model of sulphur particulates .. ^c40506768

  .. is because we might need to use them to reduce warming :

  [https://e360.yale.edu/features/aerosols-warming-climate-chan...](<https://e360.yale.edu/features/aerosols-warming-climate-change>)

  Its one of the very few levers we have to pull.

  \[  keep in mind net-zero \=\= max-CO2 \=\= max-heat .. were arguably on track for +2.0C by 2040 .. the heat itself may not be 'survivable' for large populations \]

- **foreverobama** · [2024-05-28 15:20 UTC](https://news.ycombinator.com/item?id=40501588)
  [flagged] ^c40501588

  \[dead\]

- **m3kw9** · [2024-05-28 16:09 UTC](https://news.ycombinator.com/item?id=40502243)
  [flagged] ^c40502243

  \[flagged\]

- **geniium** · [2024-05-28 16:25 UTC](https://news.ycombinator.com/item?id=40502461)
  We don't need a model, we need to take care of our planet. ^c40502461

  - **BobaFloutist** · [2024-05-28 16:51 UTC](https://news.ycombinator.com/item?id=40502753)
    California wildfires are an important, natural part of the ecosystem, but I still like to know when it's worth wearing an N95 mask and turning on my air filter to prevent that important, natural part of the ecosystem from permanently damaging my lungs. ^c40502753

  - **culi** · [2024-05-28 16:31 UTC](https://news.ycombinator.com/item?id=40502537)
    We don't need passwords, everyone just needs to be nice to each other ^c40502537

  - **waveBidder** · [2024-05-28 19:00 UTC](https://news.ycombinator.com/item?id=40504222)
    The first step in getting people to care is proving there's a problem, and accurate models help with that. Not as much as actual data mind you. ^c40504222

  - **anonporridge** · [2024-05-28 18:02 UTC](https://news.ycombinator.com/item?id=40503566)
    We don't need lightning rods, we just need to pray to Zeus. ^c40503566

    - **Spivak** · [2024-05-28 18:15 UTC](https://news.ycombinator.com/item?id=40503742)
      Steelmanning the parent's argument. Having a better model of how fucked we are when there there's no appetite to actually do anything about is high-effort doing nothing. ^c40503742

      - **thfuran** · [2024-05-28 18:30 UTC](https://news.ycombinator.com/item?id=40503909)
        But if you don't have a good model, you can't reliably identify the good ways of unfucking. ^c40503909

