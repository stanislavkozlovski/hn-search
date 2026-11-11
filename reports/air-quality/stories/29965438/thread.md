# [UK schools receive 300k CO2 monitors in gov initiative to reduce COVID19 spread](https://news.ycombinator.com/item?id=29965438)

Article: [https://www.imperial.ac.uk/news/233154/curbing-covid-19-schools-imperial-scientists-support/](<https://www.imperial.ac.uk/news/233154/curbing-covid-19-schools-imperial-scientists-support/>)

OJFord · 2022-01-17 11:18 UTC · 71 reported comments · archived 2026-11-08 11:59 UTC
Observation: 2026-11-08 11:59 UTC → 2026-11-08 11:59 UTC

## Comments

- **Youden** · [2022-01-17 13:00 UTC](https://news.ycombinator.com/item?id=29966091)
  I was curious about the specific equipment they were using and found a list of spec sheets on page 11 of \[0\]. I'm really happy they decided to use models that all have manual fresh-air calibration. ^c29966091

  A big problem with DIY projects is that most of the sensors have a built-on, on-by-default auto calibration function, which assumes it will consistently see fresh air for \~1h per day (or other period), which isn't always the case in an environment that doesn't have commercial HVAC (like a house or small school).

  When the assumption is broken, the calibration is too and the data are close to useless as absolute measurements (they still have some small value as relative measurements).

  The assumption that a fresh air baseline will always be seen is particularly easy to break right now. It's winter, so you're less likely to open the windows and due to COVID, you may be working from home, leaving very little time for CO2 to disperse.

  \[0\]: [https://www.coschools.org.uk/resources/RP24.4\%20How\%20to\%20U...](<https://www.coschools.org.uk/resources/RP24.4%20How%20to%20Use%20CO%E2%82%82%20monitors%20in%20education%20and%20childcare%20settings.pdf>)

  - **ahaucnx** · [2022-01-17 13:26 UTC](https://news.ycombinator.com/item?id=29966299)
    Yes. It is important to use CO2 sensors that do not have a short automatic baseline calibration like the MH-Z19 that is popular in DIY projects but calibrates every 24h. ^c29966299

    Better use a sensor like the Senseair S8 that only calibrates every 8 days and you most likely have a weekend of low occupancy that should bring CO2 down to ambient levels.

    - **ysleepy** · [2022-01-17 14:25 UTC](https://news.ycombinator.com/item?id=29966806)
      You can set the calibration mode to manual using either the serial port or a pin on the mh-z19. Mine is configured to manual and after a few months it still reads reasonable values for outside air. ^c29966806

      But yes, the default is autocalibration. But honestly, the difference isn't that bad, it's probably like 100ppm offset for stale room air from outside, and 100 doesn't make a huge difference when you are trying to measure around 1500.

    - **5e92cb50239222b** · [2022-01-17 13:39 UTC](https://news.ycombinator.com/item?id=29966420)
      I haven't been able to open a window for about a month due to extreme air pollution outside, and I think my Senseair S8 is broken now. If it sees fresh air with normal CO₂ levels it goes from "normal" 1.5-2k PPM (which are really closer to 4k) to zero and then shoots up to \~65000 PPM, and stays there. It spent the last two weeks in a room with an open window and still shows 65k PPM. Does anyone know of any way to recalibrate it, except for the obvious solution of putting it in a closed box and slowly lowering the amount of CO₂ there? ^c29966420

      - **janekm** · [2022-01-17 13:50 UTC](https://news.ycombinator.com/item?id=29966512)
        There is a calibration pin which you can connect to GND for 4-8s to force a manual calibration (if you can bring the sensor into an environment of \~400ppm): [https://emariete.com/en/meter-co2-esp8266-nodemcu-sensor-sen...](<https://emariete.com/en/meter-co2-esp8266-nodemcu-sensor-senseair-s8/>) ^c29966512

      - **nemetroid** · [2022-01-17 14:10 UTC](https://news.ycombinator.com/item?id=29966679)
        According to its datasheet, the S8 reports CO2 level as a 16 bit integer, so values around 2\^16 (65535) sound like underflow issues. ^c29966679

      - **ahaucnx** · [2022-01-17 13:57 UTC](https://news.ycombinator.com/item?id=29966569)
        I think 65k ppm is outside the measurement range of the S8. It might be a communication or code issue that causes this and not from actual measurements. ^c29966569

- **AlbertoGP** · [2022-01-17 11:37 UTC](https://news.ycombinator.com/item?id=29965572)
  This might be one of the good things to come out of the pandemic if it stays as it would improve the kids’ attention and mental performance. ^c29965572

  The article mentions that in passing: “As well as being a good ‘proxy’ for ventilation, lower CO2 levels have been linked to improved learning outcomes and better cogitative performance.”

  I’d rather have fixed sensors so that they would stay, but these are portable and I imagine most will be left in a drawer after the pandemic goes away: «The portability of the CO2 monitors, supplied by the Department for Education (DfE), means schools can move them around to test different areas, starting with those they suspect may be poorly ventilated.»

  At least the air cleaners might stay («distributing between 7,000 and 8,000 air cleaning units.») and I hope the CO₂ monitors will keep being used once people see the difference.

  - **pasabagi** · [2022-01-17 12:36 UTC](https://news.ycombinator.com/item?id=29965920)
    7 or 8 thousand air cleaning units is a bit pointless, though, given that there are over 32,000 schools. ^c29965920

    Presumably, 300,000 CO2 monitors is in the right range for one per classroom? Is ten classrooms per school a reasonable average?

    - **andylynch** · [2022-01-17 13:23 UTC](https://news.ycombinator.com/item?id=29966268)
      It’s not clear from the press release whether this is a UK rollout or just in England- I suspect the latter - at last count there were 302 thousand classes in English schools, so this number makes sense. ^c29966268

    - **OJFord** · [2022-01-17 16:25 UTC](https://news.ycombinator.com/item?id=29968183)
      But maybe they were for the ones where they're use was (particularly) not pointless? I.e. those with consistent high readings, with simple measures like opening windows not helping (or for some reason not being practical). ^c29968183

      It would make more sense to me to send 7-8k of them to say London schools than 20k to country schools.

      Seems a bit tough to ever make them practical without central AC though, which is not common (nor any AC) in the UK.

      - **pasabagi** · [2022-01-17 17:08 UTC](https://news.ycombinator.com/item?id=29968737)
        One interview I heard called it 'gesture politics'. Sadly, I think that assessment is on the money. It's just not plausible that there are only 7k classrooms in the UK that  have bad ventilation. ^c29968737

        I think it's the deep malaise of UK politics that they just *hate* spending money on anything, even if it will save far more money in the future. It's why the UK has the GDP-per-capita of Japan, but mostly looks like Serbia.

    - **jamessb** · [2022-01-17 12:53 UTC](https://news.ycombinator.com/item?id=29966047)
      \> Is ten classrooms per school a reasonable average? ^c29966047

      That sounds low: a secondary school with no sixth-form will have students in 5 different year groups, and will typically have more than two classes per year group.

      - **iso1631** · [2022-01-17 14:55 UTC](https://news.ycombinator.com/item?id=29967118)
        There are 8,911,853 pupils in England alone with an average class size of 26.6 ^c29967118

        That's 335,032 classes, and thus at least 335k classrooms (add extra ones for specialist classrooms)

        However that number includes private schools. Remove those and you're looking at 8.3 million, with a larger class size, so potentially just 277k classes assuming 30 people per room (plus specialist classrooms like IT, Art, D+T, PE, etc)

      - **mavhc** · [2022-01-17 14:47 UTC](https://news.ycombinator.com/item?id=29967017)
        But most schools are primary schools ^c29967017

        [https://explore-education-statistics.service.gov.uk/find-sta...](<https://explore-education-statistics.service.gov.uk/find-statistics/school-pupils-and-their-characteristics>)

        Headcount 8,911,853
        Number of schools 24,413
        Average class size 26.6

        So 335000 classes

        that's just England, which is 83\% of uk, so 402000 classes total

  - **rand49an** · [2022-01-17 13:30 UTC](https://news.ycombinator.com/item?id=29966332)
    I've visited a lot of new UK schools over the last few years and fixed CO2 monitors are in almost every classroom everywhere I visit, even pre COVID. I assume it's a DfE requirement now. ^c29966332

- **ahaucnx** · [2022-01-17 12:45 UTC](https://news.ycombinator.com/item?id=29965988)
  I recently made built instructions \[1\] for a WiFi enabled CO2 monitor that can be used in schools and is a great project to built together with students. ^c29965988

  It shows the current CO2 levels with a large green, yellow red LED matrix.

  The kit comes with a custom PCB and 3D printable enclosure and is completely open source and open hardware.

  It uses the Senseair S8 NDIR sensor that we made really good experience with and can be programmed with the Arduino environment.

  More than happy to help any school (or anybody else) who wants to build these.

  \[1\]  [https://www.airgradient.com/resources/](<https://www.airgradient.com/resources/>)

  - **DavideNL** · [2022-01-17 18:07 UTC](https://news.ycombinator.com/item?id=29969497)
    fyi related info: [https://www.jeffgeerling.com/blog/2021/airgradient-diy-air-q...](<https://www.jeffgeerling.com/blog/2021/airgradient-diy-air-quality-monitor-co2-pm25>) ^c29969497

- **Besticle** · [2022-01-17 12:46 UTC](https://news.ycombinator.com/item?id=29966000)
  CO2 as a proxy to air ventilation is a good start BUT doesn't show the full picture of what makes up IAQ (indoor air quality). ^c29966000

  Better (but more expensive) would be monitors that could measure PM2.5 molecules in the air like that of the airborne aerosols that transmit Covid (phlegm, spittle etc).

  - **parkingrift** · [2022-01-17 13:17 UTC](https://news.ycombinator.com/item?id=29966226)
    A recent study from the University of Bristol suggests that Covid particles become 90\% less infectious within as little as five minutes. I don’t know whether the UK will get much benefit from measuring PM2.5. The CO2 monitors will alert them to open windows and that’s about all that can be done. ^c29966226

    [https://www.medrxiv.org/content/10.1101/2022.01.08.22268944v...](<https://www.medrxiv.org/content/10.1101/2022.01.08.22268944v1.full.pdf>)

    - **Besticle** · [2022-01-17 14:01 UTC](https://news.ycombinator.com/item?id=29966604)
      Will help in generally combatting absenteeism as well as things like seasonal cold/flu. ^c29966604

  - **ahaucnx** · [2022-01-17 12:58 UTC](https://news.ycombinator.com/item?id=29966077)
    Yes I agree. Often there is also the dilemma if you live in a polluted area and have purifiers in the classrooms. ^c29966077

    Opening the windows will reduce CO2 but increase PM2.5. Not opening will lead to lower PM2.5 but high CO2.

    Here in Asia in highly polluted areas, positive pressure systems are getting more and more popular at home as well as in classrooms\[1\].

    \[1\] [https://www.airgradient.com/resources/positive-pressure-syst...](<https://www.airgradient.com/resources/positive-pressure-systems-for-clean-air/>)

  - **yourusername** · [2022-01-17 12:52 UTC](https://news.ycombinator.com/item?id=29966040)
    In urban areas increased ventilation might increase PM2.5 (unless it is filtered).
    30 mcg/M\^3 PM2.5 might mean a lot of covid particles or the house across the street just lit their wood heater. ^c29966040

    - **Besticle** · [2022-01-17 14:02 UTC](https://news.ycombinator.com/item?id=29966612)
      Yeah measuring both PM2.5 and CO2 will help in balancing the two. ^c29966612

- **toyg** · [2022-01-17 13:20 UTC](https://news.ycombinator.com/item?id=29966246)
  I wonder which schools are getting them. In some areas they're probably counterproductive, in the sense that the air outside might be less safe than the one in the classroom (without HVAC systems, this will probably be the case in pretty much all major English cities, which is why the government was forced by the courts to do something and mandated the implementation of Clean Air Zones). ^c29966246

  - **noneeeed** · [2022-01-17 13:32 UTC](https://news.ycombinator.com/item?id=29966352)
    The current top comment indicates that the model being used is calibratable (presumably by placing outside to work out the background rates). Of course this assumes that they will be properly calibrated by school staff. ^c29966352

- **OJFord** · [2022-01-17 11:21 UTC](https://news.ycombinator.com/item?id=29965454)
  Full (sub)title that wouldn't fit, and had \`\>\` stripped: ^c29965454

  \> UK schools have received more than 300,000 CO2 monitors as part of a government initiative to reduce COVID-19 spread in classrooms

  Actual title that I skipped because I thought the subtitle was more informative:

  \> Curbing COVID-19 in schools: Imperial scientists support CO2 monitor rollout

  Happy to edit (while I can) if people disagree..

- **nmeofthestate** · [2022-01-17 13:47 UTC](https://news.ycombinator.com/item?id=29966486)
  The article claims the Department of Education is distributing monitors to UK schools, but the DofE doesn't operate across the UK, so perhaps the story is actually about schools in England. ^c29966486

  - **egeek** · [2022-01-17 14:25 UTC](https://news.ycombinator.com/item?id=29966805)
    The story seems to be about England, but the monitors are being rolled out to other areas as well by the other departments. For example, Northern Ireland \[0\], and Scotland \[1\],\[2\]. It's anecdotal, but the monitors have started to arrive in my kids schools here in Northern Ireland. ^c29966805

    \[0\] - BBC News - [https://www.bbc.co.uk/news/uk-northern-ireland-58790302](<https://www.bbc.co.uk/news/uk-northern-ireland-58790302>)

    \[1\] - Scottish Parliament Report - [https://www.parliament.scot/chamber-and-committees/committee...](<https://www.parliament.scot/chamber-and-committees/committees/current-and-previous-committees/session-6-education-children-and-young-people-committee/correspondence/2021/learning-estate-co2-monitoring>)

    \[2\] - Scottish COVID guidance for schools - [https://education.gov.scot/media/ttkbrnde/reducing-risks-in-...](<https://education.gov.scot/media/ttkbrnde/reducing-risks-in-schools-guidance-version-7-2-05-01-21.pdf>)

    (edited to break up the links)

- **bloopernova** · [2022-01-17 12:37 UTC](https://news.ycombinator.com/item?id=29965927)
  Somewhat related: I'm hooking up some sensors to my raspberry pi InfluxDB instance using Python. It's end goal is a very hobbyist project: monitoring cat litter boxes and alerting before they stink. ^c29965927

  The CO2 levels in my office at home are \~400ppm at night, but head past 900ppm during the day. I'm going to add another alert to remind us to open windows! Although our townhouse is part of a back to back block, so only has windows on one side.

- **yalogin** · [2022-01-17 15:02 UTC](https://news.ycombinator.com/item?id=29967190)
  I haven’t been keeping up with the dynamics of covid spread, I thought covid is mostly spread by close proximity and over water particles. How much of the covid spread is attributed to transmission through air? I am curious because covid also needs enough density of viruses(forgot the term for this) to infect, wonder what happens to the density of the viruses as they go through the hvac system. ^c29967190

  - **70rd** · [2022-01-17 15:05 UTC](https://news.ycombinator.com/item?id=29967224)
    [https://www.wired.com/story/the-teeny-tiny-scientific-screwu...](<https://www.wired.com/story/the-teeny-tiny-scientific-screwup-that-helped-covid-kill/>) ^c29967224

    \^Great and accessible write up on the misconceptions of aerosol transmission and droplets.

  - **jordanrobinson** · [2022-01-17 15:09 UTC](https://news.ycombinator.com/item?id=29967269)
    Worth bearing in mind that regardless of the rest of your comment, that probably less than 1\% of schools in the UK have a hvac system. ^c29967269

- **an9n** · [2022-01-17 18:47 UTC](https://news.ycombinator.com/item?id=29970172)
  Treat anything out of Imperial with extreme caution - they are one of the most loathsome core participants of the Great Reset/Coronavirus conspiracy, employing deeply discredited quack 'Professor' Neil Ferguson and his truly laughable 'modelling' (Never Once Right™). ^c29970172

- **656565656565** · [2022-01-17 12:26 UTC](https://news.ycombinator.com/item?id=29965859)
  Great except they are being ignored ^c29965859

  EDIT; being downvoted for sharing what is actually happening on the ground

  - **Resinderate** · [2022-01-17 12:32 UTC](https://news.ycombinator.com/item?id=29965895)
    Yeah partner is a teacher and have heard the same. "Hey, the monitor is too high what should we do?", "Open the door", "It is open", "Open the windows.", "They are open.", "Okay, never mind". ^c29965895

    - **656565656565** · [2022-01-17 12:34 UTC](https://news.ycombinator.com/item?id=29965914)
      Several academies at least have rooms in constant red with doors windows opened ^c29965914

      - **raverbashing** · [2022-01-17 12:46 UTC](https://news.ycombinator.com/item?id=29965994)
        Well if the windows and doors are open they can't do much more (there's also measurement inertia, it might be getting ventilated but it will take some time to register) ^c29965994

        Lack of ventilation plays a big role on the spread

        - **giantg2** · [2022-01-17 12:49 UTC](https://news.ycombinator.com/item?id=29966016)
          They can do more. The HVAC systems should increase air exchange, to reduce recirculation, and likely need higher output (more cfm - larger ducts, more ducts, and/or higher velocity). ^c29966016

          - **JamesMcMinn** · [2022-01-17 12:55 UTC](https://news.ycombinator.com/item?id=29966061)
            Very few schools in the UK have a HVAC system. Some of the more modern ones perhaps, but the majority of schools in the UK are likely older than the students grandparents. ^c29966061

            - **giantg2** · [2022-01-17 13:23 UTC](https://news.ycombinator.com/item?id=29966269)
              True. I'm just saying that technically they could upgrade (or implement) the HVAC system to meet the new demands. Working with the existing hardware and not making any changes makes the CO2 meters practically worthless. Now we've added the stress or placebo effect of knowing that it's a detrimental environment on top of it actually being one. ^c29966269

              - **janekm** · [2022-01-17 13:53 UTC](https://news.ycombinator.com/item?id=29966541)
                If all they achieve is getting the windows opened that is already a huge success.
                I would expect adding a simple fan to speed up the air exchange would help a lot too... ^c29966541

                - **giantg2** · [2022-01-17 13:55 UTC](https://news.ycombinator.com/item?id=29966553)
                  I would hope. Although based on other comments it sounds like even with the windows and doors open it's still high. Maybe a window fan would be beneficial, but I wonder if the heating system would keep up with it in the winter. ^c29966553

              - **pjc50** · [2022-01-17 13:44 UTC](https://news.ycombinator.com/item?id=29966469)
                Technically maybe. Within the budget set by central government? No. ^c29966469

          - **xxs** · [2022-01-17 14:50 UTC](https://news.ycombinator.com/item?id=29967054)
            cfm - darn, this the UK, it's quite metric. ^c29967054

      - **jdavis703** · [2022-01-17 14:13 UTC](https://news.ycombinator.com/item?id=29966710)
        They allow doors to be propped open? Doesn’t this endanger the students with increased risks from active shooters? ^c29966710

        - **oxidising** · [2022-01-17 14:19 UTC](https://news.ycombinator.com/item?id=29966765)
          Luckily we don't have gunmen running through schools in the UK. ^c29966765

          - **mavhc** · [2022-01-17 14:49 UTC](https://news.ycombinator.com/item?id=29967036)
            We did once, so we banned guns. ^c29967036

        - **mbg721** · [2022-01-17 15:17 UTC](https://news.ycombinator.com/item?id=29967360)
          Well, if they're airsoft guns, the decreased CO2 renders them unfireable. ^c29967360

        - **C19is20** · [2022-01-17 15:13 UTC](https://news.ycombinator.com/item?id=29967310)
          I laughed out loud - best ever humour on hn, ever. ^c29967310

        - **kwhitefoot** · [2022-01-17 14:51 UTC](https://news.ycombinator.com/item?id=29967061)
          Was that seriously meant?  Or are you trolling? ^c29967061

          - **jdavis703** · [2022-01-17 18:30 UTC](https://news.ycombinator.com/item?id=29969919)
            No, this is literal school policy in the US. ^c29969919

            - **kwhitefoot** · [2022-01-18 20:08 UTC](https://news.ycombinator.com/item?id=29984984)
              I'm glad my children didn't have that to worry about in Norway nor myself in the UK (many years ago). ^c29984984

  - **JamesMcMinn** · [2022-01-17 12:51 UTC](https://news.ycombinator.com/item?id=29966028)
    This is my understanding having spoken to a couple of teachers. The only real option they have to increase ventilation is to open windows, however when it's below freezing outside and windy, this isn't a good solution and doesn't actually help all that much in most instances. ^c29966028

    A more robust air purification and ventilation system is what's actually needed, but good luck getting the Government to fund that, especially with the age and general run-down state of many of the UKs schools.

    For what it's worth, you're probably being down-voted because you presented no evidence or context, rather than for the message itself.

    - **nicoburns** · [2022-01-17 13:34 UTC](https://news.ycombinator.com/item?id=29966371)
      \> good luck getting the Government to fund that, especially with the age and general run-down state of many of the UKs schools. ^c29966371

      Given how expensive the pandemic has been, I wonder if they might actually do this at some point. If covid doesn't just fade away it's probably one of the most effective things they could do to lessen the impact.

      - **cjrp** · [2022-01-17 13:39 UTC](https://news.ycombinator.com/item?id=29966418)
        Given how expensive the pandemic has been, I expect we'll see *less* funding of schools, not more. ^c29966418

    - **lbriner** · [2022-01-17 14:27 UTC](https://news.ycombinator.com/item?id=29966820)
      Why do people constantly talk about the Government funding things? The Tax Payer funds government spending, the government simply allocates is, so to spend X 100 million + requires cutting other services or raising taxes, neither of which are popular. ^c29966820

      Taxation also causes all sorts of other issues since a large percentage of the population don't pay tax (or much tax), so then there are issues of fairness. Add it to VAT? Income tax? Corporation tax?

      - **neilwilson** · [2022-01-17 15:43 UTC](https://news.ycombinator.com/item?id=29967665)
        Somebody who needs to read [https://new-wayland.com/blog/how-the-governments-super-plati...](<https://new-wayland.com/blog/how-the-governments-super-platinum-credit-card-works/>) ^c29967665

        The people who work on school renovations earn money and spend it into the economy. Lots of people will earn more because of it. The only downside is that some private projects will be delayed or scrapped because people are working on school renovations instead. That's the actual cost of public projects.

        It's never a matter of money. Only ever a matter of alternative uses for the effort of real people.

  - **chrisco255** · [2022-01-17 17:00 UTC](https://news.ycombinator.com/item?id=29968612)
    Because it is excessively cautious and basically useless. ^c29968612

    Virus particles are everywhere. There is no avoiding them.

- **Rickthedick** · [2022-01-17 22:31 UTC](https://news.ycombinator.com/item?id=29972427)
  Wouldnt a portable CO2 Detector and frequent inspections be more performance and cost effective? ^c29972427

- **Proven** · [2022-01-17 12:28 UTC](https://news.ycombinator.com/item?id=29965877)
  [flagged] ^c29965877

- **chrisco255** · [2022-01-17 17:16 UTC](https://news.ycombinator.com/item?id=29968837)
  This is excessive cautionary crap. It won't do anything to reduce the spread. It just makes people excessively fearful of a virus they are going to contract no matter what they do. Instead of telling kids to be strong and enjoy life, they're robbing these children of their precious childhood. Fear and toxic paranoia is the worst thing you can spread. ^c29968837

  - **Daishiman** · [2022-01-17 18:15 UTC](https://news.ycombinator.com/item?id=29969625)
    No, this has been supported by scientists since way before this pandemic as an easy proxy for air circulation, which has been known for over a century to reduce transmission of respiratory diseases. If anything it's a wonder that it took so long. ^c29969625

- **giantg2** · [2022-01-17 12:45 UTC](https://news.ycombinator.com/item?id=29965985)
  Generally a good idea, but probably not necessary for permanent installation (or allotment since they are portable), just during HVAC design and testing. ^c29965985

  Also, if the kids are wearing masks then the cognitive benefits go out the window with CO2 concentration being above 20,000ppm.

  [https://pubmed.ncbi.nlm.nih.gov/33858372/](<https://pubmed.ncbi.nlm.nih.gov/33858372/>)

  - **vertnerd** · [2022-01-17 14:21 UTC](https://news.ycombinator.com/item?id=29966785)
    As someone who wears a kn95 mask all day I think the results of linked study should be taken with a grain of salt. The CO2 concentrations they measured with conventional masks are effectively similar to the concentrations in exhaled air, which means they may only be measuring the concentration in the stale air sitting inside the mask between each inrush of fresh air that occurs with each inhalation. ^c29966785

    In other words, I don't care what the CO2 concentration is in my mask. I care what the average concentration is in each inhaled breath, which consists of the stale air in my mask, combined with the (presumably larger volume of) fresh air that is introduced by breathing in. I doubt the study methodology properly captured that.

    - **giantg2** · [2022-01-17 14:45 UTC](https://news.ycombinator.com/item?id=29966985)
      That's largely irrelevant if you look at the constraints of the system we are discussing. ^c29966985

      1- the beneficial level in the article is to keep CO2 under 800ppm for learning benefit.

      2- tidal volume in *adults* is 400-500ml.

      3- volume inside an N95 varies based on model and face geometry, but is presumably 20ml or much larger, especially for children with smaller faces.

      4- indoor CO2 concentrations are typically not lower than 600ppm.

      Based on this info, average concentration easily exceeds 1000ppm. This is even more likely for children who have smaller tidal volumes and presumably more volume under the mask.

      - **jve** · [2022-01-17 15:39 UTC](https://news.ycombinator.com/item?id=29967621)
        \> 4- indoor CO2 concentrations are typically not lower than 600ppm. ^c29967621

        Out of curiosity, just looked at my PPM monitor behind my laptop... it reads 600 :) We have a good ventilation here. But humidity suffers (very low)

      - **vertnerd** · [2022-01-18 09:43 UTC](https://news.ycombinator.com/item?id=29977021)
        I think your take is fine, but it's a far cry from saying we're spending the day at the 15 minute limit for CO2 concentration. The classroom I teach in easily hits the 1000 ppm level (I measured it at the start of the 2020-21 school year), so we're already suffering *before* the masks go on. The masks just make it a little bit worse. ^c29977021

  - **r\_hoods\_ghost** · [2022-01-17 15:14 UTC](https://news.ycombinator.com/item?id=29967324)
    This is the UK. Even in modern buildings you often don't need air conditioning since the climate is temperate, although that's beginning to change. Forget about retrofitting air con in the average Victorian or 1960s era school, they're just not designed for it. ^c29967324

  - **ahaucnx** · [2022-01-17 12:51 UTC](https://news.ycombinator.com/item?id=29966029)
    With a permanent installation you can link the sensor CO2 data with the hvac system for a demand controlled ventilation. ^c29966029

    This will allow energy savings and maintain an optimum level of CO2 in the classrooms.

    We often see big differences in our data comparing different classroom sizes, age of students and activities inside the classroom. So often a fixed hvac setting is not the best solution.

    - **giantg2** · [2022-01-17 13:16 UTC](https://news.ycombinator.com/item?id=29966214)
      "With a permanent installation you can link the sensor CO2 data with the hvac system for a demand controlled ventilation." ^c29966214

      That may be the best *greenfield* solution. Yet this is not a greenfield situation. These sensors are assigned to the school, but they are not permanently installed, and they cannot control the systems. Most existing systems aren't even capable of being controlled that way.

  - **netizen-936824** · [2022-01-17 12:49 UTC](https://news.ycombinator.com/item?id=29966012)
    Something interesting about that study: the CO2 levels are okay for short term use ^c29966012

    Students are wearing them *literally all day*

