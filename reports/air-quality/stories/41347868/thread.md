# [Study: Air purifier use at daycare centres cut kids' sick days by a third (2023)](https://news.ycombinator.com/item?id=41347868)

Article: [https://yle.fi/a/74-20062381](<https://yle.fi/a/74-20062381>)

mji · 2024-08-25 15:15 UTC · 265 reported comments · archived 2026-11-08 13:39 UTC
Observation: 2026-11-08 13:37 UTC → 2026-11-08 13:39 UTC

## Comments

- **PaulKeeble** · [2024-08-25 17:07 UTC](https://news.ycombinator.com/item?id=41349045)
  There has been a number of these studies in schools and hospitals showing HEPA filters reduce up to about 2/3rd of infections. We now know many viruses are airborne including Covid and Al Hubbard's studies on how long virus is viable has shown it can be hours and it's helped by high CO2. Air circulation and reducing CO2 makes a big difference as well. ^c41349045

  - **lolinder** · [2024-08-25 18:22 UTC](https://news.ycombinator.com/item?id=41349792)
    Do we have evidence that CO2 is causal or is it still just a correlation? In general, poor ventilation + humans \= high CO2, so unless there was a controlled experiment done that's a pretty strong confounding factor. ^c41349792

    - **rockinghigh** · [2024-08-25 18:27 UTC](https://news.ycombinator.com/item?id=41349847)
      \> Results showed increasing the CO2 concentration to just 800 ppm, a level identified as well ventilated, resulted in an increase in viral aerostability. After 40 minutes, when compared to clean air, around 10 times as much virus remained infectious when the air has a CO2 concentration similar to that of a crowded room (3,000 ppm). ^c41349847

      \> Dr Haddrell said: “This relationship sheds important light on why super spreader events may occur under certain conditions. The high pH of exhaled droplets containing the SARS-CoV-2 virus is likely a major driver of the loss of infectiousness. CO2 behaves as an acid when it interacts with droplets. This causes the pH of the droplets to become less alkaline, resulting in the virus within them being inactivated at a slower rate.

      [https://www.bristol.ac.uk/cabot/news/2024/virus.html](<https://www.bristol.ac.uk/cabot/news/2024/virus.html>)

      Ambient carbon dioxide concentration correlates with SARS-CoV-2 aerostability and infection risk

      [https://www.nature.com/articles/s41467-024-47777-5](<https://www.nature.com/articles/s41467-024-47777-5>)

      - **lolinder** · [2024-08-25 18:42 UTC](https://news.ycombinator.com/item?id=41350007)
        Thanks! This is exactly what I was looking for. ^c41350007

    - **LordKeren** · [2024-08-25 19:32 UTC](https://news.ycombinator.com/item?id=41350508)
      I have never seen a evidence that CO2 is a casual agent of disease (extremely obvious exceptions excluded) ^c41350508

    - **icelancer** · [2024-08-25 18:25 UTC](https://news.ycombinator.com/item?id=41349834)
      CO2 in terms of illness is merely a proxy for good air movement and exposure to the outside environment. It has its own impact on mental capacities of course. ^c41349834

  - **dzhiurgis** · [2024-08-25 22:36 UTC](https://news.ycombinator.com/item?id=41352130)
    Do you still need HEPA/air purifier if you have decent ERV/HRV? ^c41352130

    - **amluto** · [2024-08-26 00:10 UTC](https://news.ycombinator.com/item?id=41352692)
      Maybe. ^c41352692

      I have a “decent” ERV. The manufacturer claims that it’s great against air pollution, wildfire smoke, etc, and those claims do not come with numbers. Empirically (as measured by an actual particle counter), it’s crap.  It does have real numbers for ventilation rate, and it works great for ventilation.  This is a high end ERV, and I see no evidence that any other model is better. And it can’t be: a good, energy efficient filter is large, and all the manufacturers want their devices to be small.

      My solution: put a great honking filter in front of it. This increases the lifetime of its crap internal supply filter to effectively infinity (or I could remove it), adds basically no resistance, and reduces supply particulates to effectively zero.

      “Great honking” here means a 24"x24"x12" “nominal” HEPA filter with a MERV 8 prefilter. The prefilter costs basically nothing. I expect the HEPA filter to last for years.  I would have preferred a not-quite-HEPA 99.5\% or 99.9\% filter instead, but those are surprisingly hard to buy. Big HEPA filters are easy to buy. Two big MERV 16 filters in series would do the trick, too.

      (The filter efficiency math is entirely different for a ventilation system than for a recirculating filter. For recirculation, MERV 13 is fine and MERV 16 is a bit better. For once—and-done ventilation, you want to reduce outdoor crap to your preferred levels in a single pass, and MERV 13 is not even close to good enough in places with pollution or smoke issues.)

      Coversely, a poorly filtered fresh air system is fine for reducing air contaminants from indoors but will actively fight against a standalone air purifier if your goal is to reduce outdoor pollutants.

    - **bradlys** · [2024-08-26 16:15 UTC](https://news.ycombinator.com/item?id=41358704)
      Probably depends more on the air changes per hour. You'd have to compare running a filter in your room/house and the air changes it'd go through in an hour compared to your ERV/HRV. My bet is that an ERV is better if they're the same. But, it is much easier to add capacity to individual rooms with a standalone air filter than it is to change your ERV to be higher output. ^c41358704

    - **eleveriven** · [2024-08-26 13:20 UTC](https://news.ycombinator.com/item?id=41356855)
      I think using a HEPA air purifier can still be beneficial. ERV and HRV typically have standard filters that may not capture very fine particles, allergens, or airborne pathogens as effectively as HEPA filters do. ^c41356855

- **retrochameleon** · [2024-08-25 20:03 UTC](https://news.ycombinator.com/item?id=41350806)
  [https://youtu.be/gaQTYrisieA](<https://youtu.be/gaQTYrisieA>) ^c41350806

  This is an extremely well researched and presented video that exposes the fact that HEPA purifier marketing is a bit of a scam. The most important factor in air purifiers is not the filter but Clean Air Delivery Rate. You can only make a difference if you are moving air through the filters faster than particulate is introduced into the air.

  I just returned a Medify filter because their advertised square footage is way higher than what the purifier should support based on the info in the video; it is inadequate. No idea how they are calculating their numbers - not to mention it's probably at the max speed setting - but it doesn't align with the sources from the video.

  On top of that, smaller air purifiers must move air faster, be noisier, and the smallest sizes of particulate are captured most effectively at low velocities.

  Use something like this to make a nicer version of a CR box:
  [https://acinfinity.com/component-cooling/cabinet-fan-systems...](<https://acinfinity.com/component-cooling/cabinet-fan-systems/airplate-s7-home-theater-and-av-quiet-cabinet-cooling-fan-system-12-inch/>)

  Or buy one of these:
  [https://www.cleanairkits.com/](<https://www.cleanairkits.com/>)

  Those seem to be the best options that ACTUALLY work.

  - **schiffern** · [2024-08-25 20:36 UTC](https://news.ycombinator.com/item?id=41351158)
    Yes, almost all websites give the filter "square footage" at a measly 1 air change per hour. So essentially they take the CADR, divide it by the (assumed) height of the room, and that's the square footage or square meters. Very flawed methodology! ^c41351158

    Typically for respiratory pathogens you want to shoot for 6+ ACH, so as a very rough initial guess I often simply divide the rated area by 10.

    And yes, every manufacturer only gives specs for the highest fan setting. This is misleading because typically this fan setting is very loud, so few people actually run it 24/7 (and those who do will probably suffer hearing loss).

- **thinkcontext** · [2024-08-25 16:01 UTC](https://news.ycombinator.com/item?id=41348299)
  If borne out this is pretty big. A huge amount of productivity is lost by parents taking care of sick kids or who get sick from their kids. Further it might even lessen the overall spread of seasonal diseases. ^c41348299

  - **readthenotes1** · [2024-08-25 16:33 UTC](https://news.ycombinator.com/item?id=41348621)
    If it reduces the strength of the child's immune system, this may rebound in horrible ways ^c41348621

    - **jph00** · [2024-08-25 18:08 UTC](https://news.ycombinator.com/item?id=41349642)
      This is a common misunderstanding of the poorly-named “hygiene hypothesis”. For a fuller explanation of how immunologists think about this today, see this article: [https://rachel.fast.ai/posts/2024-08-13-crowds-vs-friends/](<https://rachel.fast.ai/posts/2024-08-13-crowds-vs-friends/>) ^c41349642

      In short - viruses can actually harm your immune system and lead to long term problems. OTOH, we co-evolved with certain parasites that can help us.

      Airborne pathogens are not likely to be the helpful type we’ve co-evolved with — they’re much more likely to be the type we’ve only had to deal with since the creation of higher density living and rapid long distance travel. Therefore air filters are likely to help children’s health both short and long term.

      - **dennis\_jeeves2** · [2024-08-25 18:14 UTC](https://news.ycombinator.com/item?id=41349709)
        To sort of complement what you are saying, the 'hygiene hypothesis' also ends up being a an excuse for not looking at other factors. (very similar to blaming genes alone for health issues) ^c41349709

      - **wodenokoto** · [2024-08-26 05:22 UTC](https://news.ycombinator.com/item?id=41354226)
        Completely off-topic, but why is that blog post hosted on Fast.ai's domain? ^c41354226

        - **lbotos** · [2024-08-26 10:04 UTC](https://news.ycombinator.com/item?id=41355607)
          from her about page: cofounder of fast.ai ^c41355607

    - **Terr\_** · [2024-08-25 16:55 UTC](https://news.ycombinator.com/item?id=41348890)
      What you've written is unproven, and I see two facets of confusion: ^c41348890

      First, there's a huge difference between "strong" immune responses and "good" immune responses.

      Triggering the adaptive immune system is dangerous, like unleashing Skynet robots against a zombie apocalypse. You don't nuke a city at the first police report of one person biting another. Your body has a ton of cascading safety interlocks to try to avoid triggering more than is absolutely necessary.

      Second, there's a difference between "we need dangerous exposure to actual pathogens" versus "we need calibration against a mileu of benign species we co-evolved with."

      There's no evidence our immune systems are somehow "weaker" than our ancestors', but they do seem to be miscalibrated and trigger-happy.

      - **sitkack** · [2024-08-25 17:26 UTC](https://news.ycombinator.com/item?id=41349247)
        There *are* immune system benefits to vaginal delivery which is primarily about the the transfer microbiota from the mother to the child. ^c41349247

        I am not disagreeing with anything you are saying, but often these are often conflated.

        [https://www.phind.com/search?cache\=f5pj4u7f9v0y8ri853qmaxg1](<https://www.phind.com/search?cache=f5pj4u7f9v0y8ri853qmaxg1>)

        - **thelastparadise** · [2024-08-25 18:03 UTC](https://news.ycombinator.com/item?id=41349591)
          What is the primary source of the bacteria? Is it somehow the vagina/labia itself? ^c41349591

          It seems C-section would have about as much overall fluid exchange, if not more.

          - **amanaplanacanal** · [2024-08-25 18:07 UTC](https://news.ycombinator.com/item?id=41349623)
            I believe some of it is from the rectum, which you wouldn’t get from a c-section. ^c41349623

          - **chongli** · [2024-08-25 18:35 UTC](https://news.ycombinator.com/item?id=41349933)
            No, it's the vagina itself which is heavily colonized with bacteria (lactofermenting bacteria and friends). With a C-section you're removing the baby directly from the amniotic sac into the world. ^c41349933

      - **unknown** · [2024-08-25 19:29 UTC](https://news.ycombinator.com/item?id=41350480)
        [deleted] ^c41350480

      - **MichaelZuo** · [2024-08-25 17:31 UTC](https://news.ycombinator.com/item?id=41349296)
        Practically 100\% of children will have "dangerous exposure to actual pathogens" multiple times before they turn 20. ^c41349296

        If parents only get a choice as to when, I think nearly all would choose for them to be exposed younger and before the critical high school/college years, when the stakes are much higher.

        - **cogman10** · [2024-08-25 17:50 UTC](https://news.ycombinator.com/item?id=41349472)
          When a disease is dangerous depends a lot on the specific disease.  Measles for an adult is mostly a non-issue.  Measles for a child carries a high risk of deafness and blindness.  Chickenpox for an infant can be deadly, for a child is normal, and for an adult man can cause sterility. ^c41349472

          There's no blanket "best time" to get sick with an infectious disease.  And some diseases, like chickenpox, later surface as painful shingles (which in the worst case can result in permanent nerve damage).

          The best thing to do is vaccination.  It's safe for the vast majority of the population and sidesteps complications completely.  Get your flu shot.

          - **bugglebeetle** · [2024-08-25 18:37 UTC](https://news.ycombinator.com/item?id=41349960)
            It’s funny on how we can be on a site where people spend all day working on how to account for things like dynamic conditionals, but immediately become absurdly reductive and incapable of applying the same logic to anything outside software. Real life also has a lot of if statements! ^c41349960

            - **cogman10** · [2024-08-25 21:04 UTC](https://news.ycombinator.com/item?id=41351410)
              Life is a bunch of statistics and probabilities and we humans have a strong tendency to want to simplify those away.  We are further very naturally bad at stats (probably due to our amazing pattern finding abilities). ^c41351410

              Heck, I think what makes a programmer good is something that can easily get in the way of fields like medicine.  Good programmers like to create abstractions to put things into neat boxes.  Programming is an exercise in generalization and specialization and, unfortunately, that can drive people to thinking "Oh, these diseases are alike so lets put them in the same box".  That particularly gets in the way because MOST people won't experience complications from illness.  Consider measles blindness, 30 million people get measles a year, 60,000 will get blindness.  That's a 0.2\% chance of developing blindness as a result of measles (1 in 500).  That can lead to unfounded skepticism because your observed reality "I don't know anyone that's been blinded by measles!" might make you think that the risks are lower than they are.

              And, heck, as a programmer if you have a method that fails at 1 in 500 cases you might even be justified in punting fixing that thing.

              - **bugglebeetle** · [2024-08-25 22:11 UTC](https://news.ycombinator.com/item?id=41351938)
                \> And, heck, as a programmer if you have a method that fails at 1 in 500 cases you might even be justified in punting fixing that thing. ^c41351938

                I don’t necessarily disagree, but if I intentionally ignored a fix to a method that resulted in a service-level equivalent of a user going blind every 1 in 500 times it ran, I’d get fired pretty quickly. But then again, I have also met many programmers who, when presented with such cases, pretend they do not exist.

    - **pjc50** · [2024-08-25 16:37 UTC](https://news.ycombinator.com/item?id=41348678)
      There's no good evidence for "you need to get sick in order to have a healthy immune system", and it leads to dangerous nonsense like measles parties. ^c41348678

      - **DiggyJohnson** · [2024-08-25 16:39 UTC](https://news.ycombinator.com/item?id=41348697)
        There’s a lot of evidence that exposure is required for immunity. That’s how immunity works, no? ^c41348697

        - **DistractionRect** · [2024-08-25 17:06 UTC](https://news.ycombinator.com/item?id=41349023)
          This is what they were talking about, exposure \_\_does not require\_\_ you get sick. You can still be exposed, but you don't need to let the concentrations of pathogens to build up in stale air over the course of a school day. ^c41349023

          The results aren't in yet, and of course will be subject to reproduction/duplicatation, but I suspect that's what we're seeing here. People (children) are still getting sick, just less so, presumably because they're getting exposed to lower concentrations of pathogens. The article doesn't make it clear (or I missed it) if the reduction is in severity (time spent recovering from being sick), frequency (number of times one gets sick), or a combination thereof. If I'm right, I'd expect it to be a reduction stemming from both reduced frequency/severity.

          - **newaccount74** · [2024-08-26 11:56 UTC](https://news.ycombinator.com/item?id=41356282)
            Most low-level infections probably go unnoticed, and won't show up in the study at all. ^c41356282

            Some days the kids are just a bit off, and taking their temperature shows slightly elevated temperature (37.2°C in ear). I'm pretty sure they are fighting some mild infection, but they aren't really ill.

        - **maxerickson** · [2024-08-25 16:51 UTC](https://news.ycombinator.com/item?id=41348836)
          The other poster made a statement about the strength of the immune system. I don't think there's much evidence that exposure to virus A ends up contributing to a robust response to virus Z. There's some benefit if the infections are somewhat related, but not if they are dissimilar. So sure, exposure to a particular infection is likely to make your immune system more responsive to that infection, but it's probably not reasonable to say that it has gotten stronger. ^c41348836

          And then, measles in particular can actually damage existing immunity to other infections, making exposure to it quite a lot more dangerous than just the immediate infection. [https://asm.org/articles/2019/may/measles-and-immune-amnesia](<https://asm.org/articles/2019/may/measles-and-immune-amnesia>)

        - **dv\_dt** · [2024-08-25 17:59 UTC](https://news.ycombinator.com/item?id=41349552)
          There is a lot of evidence that exposure to Covid induces long term permanent damage to tissue and the ability of the immune system to fight off other infections. ^c41349552

        - **ClumsyPilot** · [2024-08-25 19:48 UTC](https://news.ycombinator.com/item?id=41350629)
          \> There’s a lot of evidence that exposure is required for immunity ^c41350629

          Think about - immune system evolved over millions of years, is it plausible that it needed wild tribes of hunter gatherers to huddle in a nearly airtight box for 8 hours and infect each other to work

          - **DiggyJohnson** · [2024-08-28 20:11 UTC](https://news.ycombinator.com/item?id=41383722)
            I'm fine with arguing about degrees of exposure, but I'm arguing against the black and white statement that exposure doesn't affect immunity. ^c41383722

        - **thebruce87m** · [2024-08-25 16:46 UTC](https://news.ycombinator.com/item?id=41348777)
          Maybe there is still exposure, but at a lower viral load? ^c41348777

        - **api** · [2024-08-25 16:48 UTC](https://news.ycombinator.com/item?id=41348805)
          In the extreme there is evidence that *no exposure* to pathogens might weaken immunity, but that is not going to be a problem unless someone is living in a bubble or on a space station. ^c41348805

        - **noxer** · [2024-08-25 16:48 UTC](https://news.ycombinator.com/item?id=41348803)
          [flagged] ^c41348803

          \[flagged\]

          - **Kirby64** · [2024-08-25 16:54 UTC](https://news.ycombinator.com/item?id=41348880)
            In your hypothetical of it only costing a few dollars a year the economic savings just by not having children be sick even once would easily outweigh any downsides. Also, we already have this for many diseases. They’re proven and they work just fine. Nobody reasonable is advocating you avoid the flu shot just because “everyone now has the same immunities”. ^c41348880

            - **noxer** · [2024-08-25 17:07 UTC](https://news.ycombinator.com/item?id=41349039)
              [flagged] ^c41349039

              \[flagged\]

      - **The28thDuck** · [2024-08-25 16:39 UTC](https://news.ycombinator.com/item?id=41348696)
        Silly question: how does an immune system get “trained”? I imagine some of it is through familial transmission but getting sick seems to kick it into high gear. ^c41348696

        - **calmbonsai** · [2024-08-25 17:16 UTC](https://news.ycombinator.com/item?id=41349145)
          Ideally, their own mother's milk. ^c41349145

        - **loloquwowndueo** · [2024-08-25 17:04 UTC](https://news.ycombinator.com/item?id=41349002)
          Vaccines. Vaccines teach your immune system to fight specific viruses. ^c41349002

          - **\_xiaz** · [2024-08-26 07:32 UTC](https://news.ycombinator.com/item?id=41354823)
            This ignores the fact that the vast majority of airborne common-cold viruses are not covered by a vaccine ^c41354823

        - **CuriousCosmic** · [2024-08-25 17:59 UTC](https://news.ycombinator.com/item?id=41349553)
          So this is an extremely simplified answer but essentially some pathogen gets into the body. If they find a cell first, they generally get to do their job and try to kill the cell and replicate. But if a macrophage (a type of white blood cell) finds them first betfore they've intruded upon a cell, the macrophage eats it and disassembles it into little tiny pieces. ^c41349553

          The macrophage then hands over some of the important pieces to undifferentiated T cells. Those T cells then "differentiate" into one of two forms.

          The first are "Helper T cells" which carry the "design" for antibodies (immunoglobulins, i.e. proteins that bind to pathogens directly. These then share those antibody designs with B-Cells.

          The other type are "Killer T cells" which carry the "design" for T-cell-receptors that can detect "sick" cells for this specific pathogen or defect. They go hunt after the specific cell and essentially cause them to explode with the power of hydrogen peroxide. Then the macrophages eat up the dead infected cell and all the pathogens inside it and start the process anew.

          Now those B-Cells get the "design" for antibodies from the helper T cells and differentiate into two types.

          The first is essentially a factory that mass produces the antibodies and dumps them into the body. Those antibody proteins then bind to the pathogens and the macrophages can then directly attack the pathogens (because they have a bunch of big flags/alarms on them).

          The other type of B-Cell that they can differentiate into are memory B-cells. These keep the designs stored inside them and keep detectors for the pathogen on their cell membrane. Then they "go to sleep" until their detectors are activated by the pathogen. They live out their lives and replicate as needed to continue their lineage. When a pathogen shows up, they bind to either the pathogen directly or to some of the proteins it produces and they turn their factories on at full speed and start mass producing antibodies to start the immune response as fast as possible locally before the pathogen can do damage. They get depleted in this effort of course but if things go okay, the following immune response should trigger the creation of more memory B cells. (and when they don't you get stuff like immune amnesia).

          There are also "memory T-cells" but how they come about and how exactly they work is fuzzy and not super well understood. It's similar to memory B-cells but it's way more complicated and a bit "magic".

          But yeah eventually then your body beats the infection and things go back to normal with the memory cells hanging out in the body.

          Now the important thing with intensity of infection is that a mild infection will generally guarantee your body learns a sane, moderate response but a major infection can send your body into a panic and put the immune system into overdrive. That can train a response that attacks the pathogen but also attacks a lot of other stuff in the process (auto-immune response).

          You can think of this kind of like an analog version of machine learning on proteins (the training input). A bad fit can end up mischaracterizing healthy cells and bodily structures as "pathogens" and cause long term issues or even just severe reactions when you get a reinfection.

          Now for getting "trained" from the parent, this happens during pregnancy by diffusion of a subset of the antibodies from the mother to the fetus (not all types can but many do). Those stick around for a good while and eventually the child gets minor exposure to various pathogens and those shared antibodies kickstart the child's immune response enough to build up its own memory.

          Hope this helps.

          [https://upload.wikimedia.org/wikipedia/commons/4/41/Primary\_...](<https://upload.wikimedia.org/wikipedia/commons/4/41/Primary_immune_response_1.png>)

      - **sitkack** · [2024-08-25 17:32 UTC](https://news.ycombinator.com/item?id=41349309)
        I think measles parties are hold over from before the advent of the measles vaccine (early 1970s). Now that we have a vaccine for it, the vaccine is vastly superior for many reasons. ^c41349309

        [https://www.phind.com/search?cache\=va2btahy5d5gjx0ejd888ue5](<https://www.phind.com/search?cache=va2btahy5d5gjx0ejd888ue5>)

        [https://historyofvaccines.org/history/measles/timeline](<https://historyofvaccines.org/history/measles/timeline>)

        - **pjc50** · [2024-08-25 18:48 UTC](https://news.ycombinator.com/item?id=41350051)
          Still a problem: [https://inews.co.uk/news/measles-parties-risk-children-life-...](<https://inews.co.uk/news/measles-parties-risk-children-life-2873278>) ^c41350051

          Vaccine misinformation has been a disaster.

    - **nemonemo** · [2024-08-25 16:43 UTC](https://news.ycombinator.com/item?id=41348744)
      "sick days reduced by a third" does not seem to be a level of reduction that could induce a problematic rebound. ^c41348744

    - **DrNosferatu** · [2024-08-26 11:12 UTC](https://news.ycombinator.com/item?id=41356033)
      They might have a point. Only anecdotes, but I hear that kids born during Covid (and therefore confinement) get a lot sicker than other generations. ^c41356033

      Your experience?

    - **bluGill** · [2024-08-25 16:39 UTC](https://news.ycombinator.com/item?id=41348706)
      The immune system isn't a muscle. ^c41348706

      - **ipsum2** · [2024-08-25 17:01 UTC](https://news.ycombinator.com/item?id=41348956)
        Memory B and T cells would disagree with you. This is the basic knowledge for how vaccines work. ^c41348956

        - **jph00** · [2024-08-25 18:11 UTC](https://news.ycombinator.com/item?id=41349676)
          They would not disagree with you after, say, a measles infections, which thoroughly destroys the immune system at many levels. ^c41349676

          It’s not a good idea to confuse the impacts of vaccines and infections. Vaccines are carefully developed specifically to help the immune system.  Viruses evolve to hurt it.

    - **wiether** · [2024-08-26 14:46 UTC](https://news.ycombinator.com/item?id=41357680)
      Dwight, is that you? ^c41357680

- **\_dain\_** · [2024-08-25 16:06 UTC](https://news.ycombinator.com/item?id=41348352)
  This is one of the three educational interventions with solid evidence of it working. The other two are air conditioning and free school lunches. People don't get excited over them though, because they have nothing to do with teachers or curriculum or educational theory. ^c41348352

  - **mmcloughlin** · [2024-08-25 16:58 UTC](https://news.ycombinator.com/item?id=41348933)
    Perhaps there is some evidence that people do get excited about free school lunches: Governor Tim Walz’s lunch policy in Minnesota has been a part of the buzz surrounding his recent Vice Presidential nomination. ^c41348933

    [https://www.cnbc.com/2024/08/19/universal-free-school-lunche...](<https://www.cnbc.com/2024/08/19/universal-free-school-lunches-harris-walz-campaign.html>)

  - **stevenwoo** · [2024-08-25 16:14 UTC](https://news.ycombinator.com/item?id=41348444)
    There's also the accidental study of air filters where the outside air quality was not that bad.
    study
    [https://www.edworkingpapers.com/ai20-188](<https://www.edworkingpapers.com/ai20-188>)
    background
    [https://wfis.org/installing-air-filters-in-classrooms-has-su...](<https://wfis.org/installing-air-filters-in-classrooms-has-surprisingly-large-educational-benefits/>) ^c41348444

    - **amluto** · [2024-08-25 17:43 UTC](https://news.ycombinator.com/item?id=41349400)
      Wow.  That paper made no effort to even contemplate whether the improvement was related to reduced particulate matter or to reduced organic gasses.  The filters were installed in response to a *gas* leak — one would imagine they were carbon filters. ^c41349400

      Sadly, the literature on the effect of gas concentrations on human intellectual function is incredibly muddy.

  - **olalonde** · [2024-08-25 17:38 UTC](https://news.ycombinator.com/item?id=41349363)
    \> free school lunches ^c41349363

    What are you referring to?

    - **pjc50** · [2024-08-25 18:54 UTC](https://news.ycombinator.com/item?id=41350114)
      They're referring to free school lunches. That is, a lunch, at school, which is free. In the sense that it does not have to be paid for on the spot or by the child or family on account. i.e. part of the educational provision itself. ^c41350114

      (carefully phrased to avoid "no free lunch" nonsense)

      - **olalonde** · [2024-08-25 21:44 UTC](https://news.ycombinator.com/item?id=41351730)
        I understand, I meant what solid evidence that it is working and what is meant by that? ^c41351730

        - **lucubratory** · [2024-08-26 00:58 UTC](https://news.ycombinator.com/item?id=41352955)
          It improves educational, health etc outcomes significantly and unlike a lot of proposed interventions in education, it has solid scientific evidence backing it up. Specifically it significantly improves child health (e.g. fewer hospital visits), improves maths and English test scores, lowers the incidence of suspensions of students, and there's no evidence that free school lunch policies increase BMI in those with access to them. For the cost, it is a very effective intervention in improving educational outcomes. ^c41352955

          [https://www.jandonline.org/article/S2212-2672(23)00301-5/ful...](<https://www.jandonline.org/article/S2212-2672%2823%2900301-5/fulltext>)

          [https://www.brookings.edu/articles/schoolwide-free-meal-prog...](<https://www.brookings.edu/articles/schoolwide-free-meal-programs-fuel-better-classroom-outcomes-for-students/>)

          [https://onlinelibrary.wiley.com/doi/abs/10.1002/pam.22175](<https://onlinelibrary.wiley.com/doi/abs/10.1002/pam.22175>)

- **elric** · [2024-08-25 17:53 UTC](https://news.ycombinator.com/item?id=41349500)
  I installed a Zehnder ComfoAir Q ventilation system in my home. It has heat and moisture recuperation capabilities. It's currently refreshing the air at around 100m³/hour. It has an F7 (aka "ISO Fine" or "MERV 13") filter. Since installing it, my asthma has improved a fair bit, and I'm sneezing a lot less. Added benefit, virtually no mosquitoes have been able to enter my home. I'm still considering getting an extra filter addon to filter out more fine soot from car exhaust etc, but even without that option I've been very happy with the results. ^c41349500

  Edit: hit reply too soon. Wanted to add: are air purifiers as effective as increased ventilation? Should we combine the two?

  - **amluto** · [2024-08-26 16:04 UTC](https://news.ycombinator.com/item?id=41358579)
    That Zehnder unit is fantastic. The filter, not so much. (“ISO Fine” is IMO particularly embarrassing. It should say something more like “ISO ePM 1 40\%”, and then buyers would think “40\%? that’s lousy!”). Even the fancier ComfoWell filter is crap. And they’re overpriced, have lots of resistance, and don’t last long.  You can confirm how poorly it works with a portable particle counter. ^c41358579

    Get something like this if you have space:

    [https://www.hvacquick.com/products/residential/Air-Filters/P...](<https://www.hvacquick.com/products/residential/Air-Filters/Powered-HEPA-Filters/HVACQuick-IFHB-Series-Inline-HEPA-Filter-Boxes>)

    And consider putting it upstream of the Zehnder unit in the outdoor intake duct. Then it will extend your ISO Fine filter’s lifetime to effectively infinity. Or you could replace it with ISO Coarse. Or with nothing :)

    - **elric** · [2024-08-26 21:39 UTC](https://news.ycombinator.com/item?id=41362496)
      I did consider filter addons, but sadly my house is too small, fitting the unit was already a pretty big challenge. ^c41362496

  - **dzhiurgis** · [2024-08-25 22:47 UTC](https://news.ycombinator.com/item?id=41352205)
    I've installed HRV myself too. I have a reasonably easy to access roof space, but for a large guy still took over half a day. Cost 1.5k NZD, but not mosquito free, it's warmer indoors plus when neighbours fire up their fireplaces I only get an occasional little whiff of it. ^c41352205

    Best thing I did for my house so far!

  - **unknown** · [2024-08-25 18:28 UTC](https://news.ycombinator.com/item?id=41349859)
    [deleted] ^c41349859

  - **turtlebits** · [2024-08-25 18:19 UTC](https://news.ycombinator.com/item?id=41349754)
    Get an AQ monitor and a standalone filter, it will be able to constantly filter air vs the once during fresh air intake. ^c41349754

    Also my ERV only runs on demand (\~1/3 of the time, which is not  enough filtration)

    - **elric** · [2024-08-25 18:35 UTC](https://news.ycombinator.com/item?id=41349934)
      Why does it run on demand? Mine runs 24/7, though it ramps down to lower speeds at night or when I'm away. ^c41349934

      - **turtlebits** · [2024-08-26 03:42 UTC](https://news.ycombinator.com/item?id=41353819)
        Because my CO2/VOC levels are low enough that keeping in on all the time doesn't provide any additional benefit- while adding unwanted cool/hot air (no ERV is 100\% efficient).   The minimum airflow on my unit is 35 CFM (\~60 m3/hr). ^c41353819

        - **elric** · [2024-08-26 06:14 UTC](https://news.ycombinator.com/item?id=41354476)
          That makes sense. Though I imagine that depending on where your CO2 sensors are, it could take a while for higher concentrations to reach the sensor, and then more time for the concentrations to go down once the fan starts spinning. ^c41354476

          One of the reasons why mine also runs when I'm away is that it helps prevent mould growth in the heat/moisture exchanger, as that thing is a bit of a pain to clean.

- **plasticchris** · [2024-08-25 17:00 UTC](https://news.ycombinator.com/item?id=41348947)
  With my experience around poorer schools in the USA I would worry that the filter wouldn’t get replaced for decades and itself become a breeding ground for molds. ^c41348947

  - **erikvanoosten** · [2024-08-26 10:53 UTC](https://news.ycombinator.com/item?id=41355932)
    You don't need poor schools for that. Just \~3 years ago exactly this happened to a public primary school in a rich neighborhood of Haarlem (The Netherlands). If I remember correctly, the filters had not been replaced for 8 years. ^c41355932

- **swagasaurus-rex** · [2024-08-25 15:55 UTC](https://news.ycombinator.com/item?id=41348242)
  There was a great deal of interest in how to remove airborne viruses during Covid. ^c41348242

  One of the biggest takeaways seemed to be that UV light destroys viruses in seconds.

  Seems like there a lot of things we could do

  - **viraptor** · [2024-08-25 22:27 UTC](https://news.ycombinator.com/item?id=41352058)
    I found it interesting that I haven't really seen the UV sterilisation to be popular at healthcare points at large. Where I grew up, the local surgery had the UV on in the whole building after hours, and that was in early 90s EE. None of the places I've seen since then used it (as far as I'm aware), across many countries. ^c41352058

  - **slyall** · [2024-08-26 01:15 UTC](https://news.ycombinator.com/item?id=41353058)
    Naomi Wu did some videos/articles about this and was working on some sort of product you could setup. Things like a light that shone upwards in a room to clean the air above people's heads. ^c41353058

    My main take-away was this was very easy to screw up and cause eye damage, especially in an home setting where less care would be taken.

  - **plasticchris** · [2024-08-25 16:55 UTC](https://news.ycombinator.com/item?id=41348891)
    Yeah, even a single UV bulb in the cold air return might be effective. This is well known in hiking circles where UV is used to sanitize water. ^c41348891

    I might hook one up now that I have the idea.

    - **schiffern** · [2024-08-25 18:09 UTC](https://news.ycombinator.com/item?id=41349658)
      I looked into implementing this once. Some surprising things I learned: ^c41349658

      1\. You need UV-C (typically 222 nm), not just any old UV bulb off Alibaba/Wish/Amazon.

      2\. You need an extremely high UV light intensity to kill viruses if the air is just flowing past the bulb (vs shining UV on a coil to prevent bacterial/fungal growth, which is the typical usage), and you need more intensity the faster the air is flowing. Usually this requires multiple bulbs.

      3\. You need to replace your UV-C bulbs every 1,000 hours or so, because they rapidly lose intensity with operating time.

      Just putting a "black light poster" bulb in your ducts won't accomplish anything, other than perhaps giving you a false sense of security.

      - **bri3d** · [2024-08-25 18:59 UTC](https://news.ycombinator.com/item?id=41350160)
        \> You need to replace your UV-C bulbs every 1,000 hours or so ^c41350160

        I don't think this should need to be the case. Low pressure mercury arc lamps (253.7nm) last 10,000 hours in water treatment applications - a much more palatable replacement timeline (1 year) vs every few weeks!

        The short-lifetime bulbs are usually 222nm Far-UVC bulbs, which are safe for human exposure. These shouldn't be necessary to treat air as part of an enclosed HVAC system. I feel that the hype around 222nm / "safe" UVC has done a disservice to just using "dirty" 253nm UVC, which kills everything just as well as long as you keep people from being able to look at it.

        - **schiffern** · [2024-08-25 19:07 UTC](https://news.ycombinator.com/item?id=41350243)
          Thanks for the correction. It's been a while since I looked into it! ^c41350243

          Even replacing bulbs every 1 year seems like a lot more than people are bargaining for. Most people seem to expect UV will be a "Set It And Forget It" solution (hence why they prefer it over filters), so they risk neglecting the necessary replacement interval.

          - **dzhiurgis** · [2024-08-25 23:11 UTC](https://news.ycombinator.com/item?id=41352355)
            Sounds like it needs software subscription added /s ^c41352355

            IMO people wouldn't mind replacing it if it was easy to access.

      - **mandmandam** · [2024-08-26 10:18 UTC](https://news.ycombinator.com/item?id=41355685)
        \> You need an extremely high UV light intensity to kill viruses if the air is just flowing past the bulb ^c41355685

        Could you put a long tube-shaped 222-UV bulb inside a larger tube with a UV-reflective coating inside to enhance the efficiency?

        ... And, can UV bulbs be mirrored, so they reflect as well?

        - **mab122** · [2024-08-26 11:52 UTC](https://news.ycombinator.com/item?id=41356257)
          This sounds exacly as UV water treatment lamps ^c41356257

          - **mandmandam** · [2024-08-26 12:00 UTC](https://news.ycombinator.com/item?id=41356309)
            I don't know if this is a silly question but, if it works for water then why not air? Is it an overheating issue? ^c41356309

    - **elric** · [2024-08-25 17:46 UTC](https://news.ycombinator.com/item?id=41349433)
      Hmm, I wonder how effective that would be. My small home's ventilation system is currently taking in about 100m³ of fresh air per hour. That's about 1600L/minute. Let's assume the intake duct is about 20cm in diameter, and assume we can place a bulb to illuminate a 50cm stretch of pipe. That's a volume of about 16 liters. So the air would be in visible range of the bulb for about half a second. Would that be enough for a UV bulb to do anything? ^c41349433

      This was back of napkin maths, could be way off.

      Edit: sanitizing incoming air is probably pretty useless, as the outdoor concentration of pathogens is likely very low to begin with.

      - **thedougd** · [2024-08-26 03:55 UTC](https://news.ycombinator.com/item?id=41353878)
        No, not enough exposure time. ^c41353878

        I’ve seen some claims that it can destroy viruses on some medium. Imagine a filter in the light catching virus particles or particles that have viruses. The light destroys them while they’re stuck in place. I would need some independent testing to verify that claim.

      - **thelastparadise** · [2024-08-25 18:07 UTC](https://news.ycombinator.com/item?id=41349620)
        Low in pathogens, maybe, but high in pollutants such as diesel particulates, second hand cannabis, wildfire emissions, etc. ^c41349620

    - **amluto** · [2024-08-25 17:08 UTC](https://news.ycombinator.com/item?id=41349049)
      If you have an appropriately sized filter holder, I would just install a MERV 13 or 16 filter. They’re very cost effective, widely available, and they will remove non-living crud, too. ^c41349049

      The main problem is that many central air systems use crappy *thin* filter holders. A good low-resistance filter needs a lot of area, and a 4” or 5” thick format works well, 2” is marginal, and 1” sucks.  A good filter holder costs under \$200, takes very little effort to install in a new system, and is an incredible pain to retrofit into an existing system. And good filters are essentially unsupported in ductless systems.

    - **morkalork** · [2024-08-25 17:03 UTC](https://news.ycombinator.com/item?id=41348986)
      You can use UV to sanitize water to drink? Must be better tasting than those gross iodine tablets! ^c41348986

      - **mauvehaus** · [2024-08-25 17:49 UTC](https://news.ycombinator.com/item?id=41349458)
        You can, but it does not leave any residual ability for the water to neutralize pathogens once you're done treating the water. ^c41349458

        If you dip a Nalgene bottle to fill it, then purify the contents, you would typically then bleed the threads by holding the bottle upside down and loosening the cap.

        With chemical treatment, the iodine in the water works to neutralize any pathogens that aren't flushed out of the threads. If you've used UV, you're kind of hoping that the flushing action has physically washed out anything lingering in the threads.

        Anecdotally, people using UV get more cases of waterborne illness, but I don't know if anyone has rigorously studied this. Hikers are naturally resistant to controlled experiments.

        If you don't like the flavor of iodine tablets, I recommend AquaMira instead.

        Source: AT ME-MA 2003, GA-ME 2010. UV was pretty popular by 2010 and for a couple years after. Not planning a thru hike at the moment, but I believe the Sawyer squeeze filter is super popular now.

      - **mdp2021** · [2024-08-25 18:15 UTC](https://news.ycombinator.com/item?id=41349721)
        It is a standard method for disinfecting water in aqueducts. ^c41349721

        [https://en.wikipedia.org/wiki/Ultraviolet\_germicidal\_irradia...](<https://en.wikipedia.org/wiki/Ultraviolet_germicidal_irradiation>)

        \> *UVGI for water treatment // Using UV light for disinfection of drinking water dates back to 1910 in Marseille, France. The prototype plant was shut down after a short time due to poor reliability. In 1955, UV water treatment systems were applied in Austria and Switzerland; by 1985 about 1,500 plants were employed in Europe. In 1998 it was discovered that protozoa such as cryptosporidium and giardia were more vulnerable to UV light than previously thought; this opened the way to wide-scale use of UV water treatment in North America. By 2001, over 6,000 UV water treatment plants were operating in Europe*

        And yes, there are also commercial products for home use.

      - **amluto** · [2024-08-25 17:10 UTC](https://news.ycombinator.com/item?id=41349063)
        You can!  It works best if the water isn’t cloudy. ^c41349063

        You can also get chlorine dioxide tablet systems that are less nasty tasting.

- **LinuxBender** · [2024-08-25 16:00 UTC](https://news.ycombinator.com/item?id=41348297)
  Anecdotally can vouch for air purifiers.  I bought an old earth bermed home.  I suspected radon may be an issue.  Purchased 2 AirThings and they were off the government charts so to confirm Radon Daughters were being produced I bought more air purifiers and an Alpha Geiger Counter.  I can hold it 2 inches from any of my filters and the alarm sounds.  640 CPM alpha radiation.  That changed my project priorities.  The filters only bought me some time as the air away from the filters is the same level of radiation as outdoor background noise but obviously the source is still emitting gas.  I will probably just bulldoze this place. ^c41348297

  - **ComputerGuru** · [2024-08-25 16:07 UTC](https://news.ycombinator.com/item?id=41348368)
    Radon mitigation systems work. And they’re cheap. ^c41348368

    - **LinuxBender** · [2024-08-25 16:10 UTC](https://news.ycombinator.com/item?id=41348403)
      You're right but it won't help in my case.  I created an ad-hoc system that does the same thing but the source is not at ground level.  Through some form of convection *I suspect around the chimney* the gas is being pushed into the attic and then coming down in rooms they did not join the wall to the ceiling correctly.  Most of the radioactive dust is being produced in the attic which nobody has touched for 60+ years.  If I put the geiger counter in the attic it goes nuts.  I'm just going to level this place and build something correctly. ^c41348403

      - **ComputerGuru** · [2024-08-25 16:14 UTC](https://news.ycombinator.com/item?id=41348447)
        That sounds wild. I don’t know where you are but in the USA you could reach out to a university extension program/office and ask them to look into it. It’s bizarre enough to catch their interest and come at no cost to you. ^c41348447

        Edit: it really is bizarre because Radon is primarily produced by reactions underground/in the earth and has a relatively short half life (3.5 days). I don’t see how it could be atmospherically sourced without it being a hazard to the whole community, regardless of the bizarre convection currents that bring it into your house. It’s unlikely to be produced in your attic.

        If I were you, I’d want to know more and understand how this is all happening lest you raze and rebuild and find you still have a problem.

        - **rini17** · [2024-08-25 16:44 UTC](https://news.ycombinator.com/item?id=41348752)
          Radon decays into other longer lived radioactive elements, mostly isotopes of lead, which then condense down as dust and cause more problems than radon itself. So it might happen that these cumulate in the attic if circulation is just right. ^c41348752

          - **amluto** · [2024-08-25 16:58 UTC](https://news.ycombinator.com/item?id=41348931)
            Can you share your math?  Radon does indeed have extremely nasty decay products, but they are very short lived (which is why they’re so nasty).  They’re not accumulating in your attic. ^c41348931

            I would suspect fly ash as a possible source if the house ever had a coal-burning furnace.  Or maybe someone had a watch-painting operation or mixed radioactive glazes or paints there.  Someone with appropriate equipment could do a much better job identifying the source.

            - **rini17** · [2024-08-26 15:18 UTC](https://news.ycombinator.com/item?id=41357980)
              No math. Only noticed 210-Pb has half life 22 years and thus can cumulate. ^c41357980

        - **rightbyte** · [2024-08-25 16:37 UTC](https://news.ycombinator.com/item?id=41348670)
          Some forms of uranium rich slate when mixed into concrete can dispose radioactive gases. ^c41348670

          - **LinuxBender** · [2024-08-29 22:54 UTC](https://news.ycombinator.com/item?id=41396196)
            I'm leaning towards this.  My state has a tremendously high uranium concentration and many uranium mines.  It would not surprise me if people were not checking for this in the 60's in concrete mix. ^c41396196

      - **pbowyer** · [2024-08-25 16:41 UTC](https://news.ycombinator.com/item?id=41348718)
        With the mention of "radioactive dust" are you sure it's radon, as that should not produce dust, and not some other source of radiation in the attic? Like I don't kow what, a lot of old gas mantle filaments. ^c41348718

        Any notion of whether it's  β or ɣ radiation you're detecting?

        Demolition is going to need careful monitoring to ensure you don't contaminate the entire site.

        - **LinuxBender** · [2024-08-26 12:38 UTC](https://news.ycombinator.com/item?id=41356539)
          I have 3 geiger counters that do Gamma, Beta and X-Ray.  They do not register anything beyond the background noise.  My Alpha detector is the only one that picks up the spikes from the hepa filters and my attic. ^c41356539

      - **Vecr** · [2024-08-25 16:16 UTC](https://news.ycombinator.com/item?id=41348468)
        Have you done the risk calculations? Are you assuming LNT? Really, at the construction costs now you could probably pay someone to do it and have that be profitable. ^c41348468

- **chriscjcj** · [2024-08-25 19:15 UTC](https://news.ycombinator.com/item?id=41350320)
  Can anyone provide or link to some solid guidelines on what kind/brand of air purifiers actually do real effective filtration vs. garbage products? I have found that a great many of these "air purifiers" have great marketing and make amazing claims. ^c41350320

  - **bjoli** · [2024-08-25 19:31 UTC](https://news.ycombinator.com/item?id=41350500)
    4x merv 13 filters. ^c41350500

    A fan.

    Now you have yourself a high performing air purifier.

    - **ceejayoz** · [2024-08-25 19:34 UTC](https://news.ycombinator.com/item?id=41350524)
      Yup. We have several of these running. Helps with allergies and when one of us got COVID the rest did not. ^c41350524

      [https://en.wikipedia.org/wiki/Corsi\%E2\%80\%93Rosenthal\_Box](<https://en.wikipedia.org/wiki/Corsi%E2%80%93Rosenthal_Box>)

  - **sbochins** · [2024-08-25 19:23 UTC](https://news.ycombinator.com/item?id=41350418)
    I’ve been happy with Austin Air purifiers. Most of the other brands help, but don’t handle most VOCs. If you have allergies or other issues, it’s better to stick with top quality brands.
    [https://housefresh.com/austin-air-healthmate/](<https://housefresh.com/austin-air-healthmate/>) ^c41350418

  - **evilmusic** · [2024-08-26 06:09 UTC](https://news.ycombinator.com/item?id=41354457)
    Some good tips here [https://youtu.be/nE3u-2EyW-s](<https://youtu.be/nE3u-2EyW-s>) ^c41354457

  - **alliao** · [2024-08-25 21:25 UTC](https://news.ycombinator.com/item?id=41351596)
    cr box basically owns everything else go build a couple yourself, it's great, if you live in the US you can order kits too ^c41351596

  - **tiahura** · [2024-08-25 19:26 UTC](https://news.ycombinator.com/item?id=41350444)
    A 20” box fan and 4 20” furnace filters ^c41350444

    - **Rebelgecko** · [2024-08-25 21:12 UTC](https://news.ycombinator.com/item?id=41351483)
      Unless you live in a place with very cheap electricity, you'll save money in the long run by getting a purpose built air purifier ^c41351483

      - **alliao** · [2024-08-25 21:28 UTC](https://news.ycombinator.com/item?id=41351619)
        nothing comes close to crbox in terms of performance... the gold standard IQAir do give you close to perfect single pass filtration but the cfm is so low and noise much higher... ^c41351619

      - **tedunangst** · [2024-08-25 21:19 UTC](https://news.ycombinator.com/item?id=41351533)
        How much money over how much time? ^c41351533

        - **Rebelgecko** · [2024-08-26 01:08 UTC](https://news.ycombinator.com/item?id=41353013)
          It depends on the box fan and your electricity prices. When I did the math for me, the break even point for buying a \$150 purifier was on the order of months. But I'm in California where electricity is relatively expensive ^c41353013

  - **ClumsyPilot** · [2024-08-26 01:24 UTC](https://news.ycombinator.com/item?id=41353125)
    Basically all filters work l, they just need to be big enough. The largest air purifier from Xiaomi is okay, ones from ikea are a little small but nicely made ^c41353125

- **encoderer** · [2024-08-25 16:19 UTC](https://news.ycombinator.com/item?id=41348489)
  Even better (where weather allows) is fully outdoor daycare. We were fortunate to have only the briefest of shut downs during COVID. ^c41348489

  Obviously impractical in many areas but it's part of the California dividend

  - **kjkjadksj** · [2024-08-25 16:49 UTC](https://news.ycombinator.com/item?id=41348808)
    So long as you are far enough from a major freeway, major road, major airport, or major port. With those requirements the number of californian daycares or schools that meet that criteria shortens significantly. ^c41348808

  - **Rendello** · [2024-08-25 16:22 UTC](https://news.ycombinator.com/item?id=41348524)
    It was a big thing in the early 1900s too: ^c41348524

    [https://en.wikipedia.org/wiki/Open\_air\_school](<https://en.wikipedia.org/wiki/Open_air_school>)

  - **esafak** · [2024-08-25 16:25 UTC](https://news.ycombinator.com/item?id=41348558)
    And it's good for your eyesight. ^c41348558

    - **euroderf** · [2024-08-25 19:01 UTC](https://news.ycombinator.com/item?id=41350187)
      Yes. Lots of new results in this topic. Get outside and exercise those eyes. ^c41350187

  - **dzhiurgis** · [2024-08-25 23:15 UTC](https://news.ycombinator.com/item?id=41352380)
    Unless you don't want to expose your kids to sun screen, eeek /s ^c41352380

- **switch007** · [2024-08-25 15:49 UTC](https://news.ycombinator.com/item?id=41348185)
  Good news. Hopefully a country as wealthy as Finland can just roll this out countrywide without much thought, if not already standard ^c41348185

  - **readthenotes1** · [2024-08-25 16:34 UTC](https://news.ycombinator.com/item?id=41348636)
    Without much thought? Without much thought I would say that the recent experience of preventing children from catching communicable diseases have shown it to be a devil's bargain and we would be wise to keep their immune systems constantly exercised ^c41348636

    - **unsupp0rted** · [2024-08-25 16:51 UTC](https://news.ycombinator.com/item?id=41348837)
      What evidence is there that it’s possible to “exercise” an immune system? ^c41348837

    - **terminatornet** · [2024-08-25 18:46 UTC](https://news.ycombinator.com/item?id=41350036)
      Getting sick to stay healthy. Makes sense to me. Now will you be exposing yourself to zika virus or HIV? Seems like those would exercise your immune system quite a bit. ^c41350036

    - **error\_logic** · [2024-08-25 17:18 UTC](https://news.ycombinator.com/item?id=41349161)
      As mentioned elsewhere in the thread, one can be exposed (and have an immune response) to a viral load below what's normally considered symptomatic. Then the immune system learns, but doesn't have to go into over-drive which taxes the rest of the body more destructively. ^c41349161

      In other words: Filtering part of it from the air can make exposure more like vaccination than full blown infection, which is great.

    - **hirsin** · [2024-08-25 16:54 UTC](https://news.ycombinator.com/item?id=41348886)
      What recent experience? Do you mean keeping them home from school for covid? I don't think the knock on effects from that are remotely traceable to their immune systems. ^c41348886

    - **switch007** · [2024-08-25 16:43 UTC](https://news.ycombinator.com/item?id=41348748)
      Without much thought regarding cost. Calm down lol ^c41348748

- **taeric** · [2024-08-25 15:56 UTC](https://news.ycombinator.com/item?id=41348259)
  So from 10-13 down to 7-9?  Nice. ^c41348259

  Will be neat to see if the kids were still carriers, but managed to keep the viral loads down such that they weren't "sick" during that time.  I recall a study a few years back that said kids at that age were basically always sick, just not often symptomatic.

- **xyst** · [2024-08-25 17:21 UTC](https://news.ycombinator.com/item?id=41349190)
  Any HVAC professionals or plumbers know if a mini-split A/C system can  be outfitted with UV bulbs? ^c41349190

  Have a few Levoit air purifiers that sit flush against the wall. But would be nice to have an extra layer at the source.

  - **thedougd** · [2024-08-26 03:59 UTC](https://news.ycombinator.com/item?id=41353898)
    I would imagine it would destroy the plastic. A common problem with retrofitting stardard split systems. They require a UV resistant drain pans. ^c41353898

  - **abracadaniel** · [2024-08-25 23:22 UTC](https://news.ycombinator.com/item?id=41352429)
    REME Halo was recommended to me and I bought one. Hard to know if you’re making a difference, but it’s something. ^c41352429

- **photochemsyn** · [2024-08-25 16:11 UTC](https://news.ycombinator.com/item?id=41348409)
  I wouldn't call this a statistically significant result, and the fact that the buildings in question had good mechanical air ventilation could very well explain the results: ^c41348409

  \> "Utilizing the model, we used portable air cleaners in two day care units (A and B, number of children participating in the study n \= 43) and compared infection incidents between the two intervention units to the rest of the units in city of Helsinki (n \= 607). The intervention buildings had mechanical supply and exhaust air ventilation."

  [https://www.sciencedirect.com/science/article/pii/S295036202...](<https://www.sciencedirect.com/science/article/pii/S2950362024000043>)

  You also have to consider external air quality, as ventilating a building with polluted air would have negative effects like increased asthma.  In that case perhaps a sealed building with air purifiers is a better option, but then CO2 buildup is a concern, so you'd need CO2 scrubbers, which are expensive.

  That's why clean air regulations matter, and getting off fossil fuel combustion as an energy source (and limiting pesticide/herbicide use in agricultural zones) is the easiest route forward.

- **duxup** · [2024-08-25 16:39 UTC](https://news.ycombinator.com/item?id=41348703)
  Is there any information on the type / price of these air purifiers? ^c41348703

  There's a lot of "air purifiers" out there on the market.

  - **PaulKeeble** · [2024-08-25 17:10 UTC](https://news.ycombinator.com/item?id=41349066)
    In a lot of tests Corsi Rosenthal boxes tend to outperform most commercial offerings and they are very cheap as they are a box fan duct taped to some MERV13 filters. Effectiveness is a lot about air exchanges an hour. ^c41349066

    - **amanaplanacanal** · [2024-08-25 18:15 UTC](https://news.ycombinator.com/item?id=41349717)
      I have one of these set up on each floor of my two story house to cut down on particulates from dust, pets, and cooking. If they also help protect from disease that’s just icing in the cake. ^c41349717

    - **djmips** · [2024-08-25 19:15 UTC](https://news.ycombinator.com/item?id=41350314)
      Box fans are noisy and in my experience fail early when running constantly. When their bearings fail they can atomize the grease. ^c41350314

  - **amluto** · [2024-08-25 17:16 UTC](https://news.ycombinator.com/item?id=41349140)
    It would be awesome if they were IKEA purifiers. Cheap media and excellent CADR/W. ^c41349140

- **rajnathani** · [2024-08-26 07:17 UTC](https://news.ycombinator.com/item?id=41354748)
  Given that air purifiers could increase airborne endotoxin levels \[0\], that instead better ventilation should be prioritized as it also solves the higher CO2 problem, where we know cognitive function slows down due to higher CO2 levels \[1\]. Given that OSHA sets an upper limit on CO2 in the workplace, I wonder whether daycare centers have such norms enforced too. ^c41354748

  \[0\] [https://www.sciencedirect.com/science/article/pii/S016041202...](<https://www.sciencedirect.com/science/article/pii/S016041202031833X>)

  \[1\] [https://www.ucl.ac.uk/bartlett/energy/news/2018/dec/study-mi...](<https://www.ucl.ac.uk/bartlett/energy/news/2018/dec/study-mitigating-effects-higher-co2-levels-productivity-receives-widespread-coverage>)

- **throw7** · [2024-08-25 19:00 UTC](https://news.ycombinator.com/item?id=41350169)
  Indoor air environments are usually poor.  Just having outside air from open windows would be an improvement. ^c41350169

  - **dzhiurgis** · [2024-08-25 23:19 UTC](https://news.ycombinator.com/item?id=41352403)
    Which easily excludes 80\%+ of the places either due cold, heat or pollution. ^c41352403

    - **ClumsyPilot** · [2024-08-26 01:41 UTC](https://news.ycombinator.com/item?id=41353237)
      Proper ventilation systems address that issue ^c41353237

- **unglaublich** · [2024-08-25 15:46 UTC](https://news.ycombinator.com/item?id=41348152)
  Yes, please. My colleagues, who are parents, are constantly sick whenever their children are at daycare, and I have no interest in the constant coughing and/or getting sick myself. ^c41348152

  - **wredue** · [2024-08-25 16:53 UTC](https://news.ycombinator.com/item?id=41348872)
    There’s some studies showing parents of kids in daycare are sick upwards of 90\% of the time. ^c41348872

    I don’t know if it was that much, but when my kids were in daycare, it was definitely A LOT for sure. Work doesn’t provide nearly enough sick time for that period of being a parent. So what are parents to do if they’re not able to work from home?

    - **MikeRichardson** · [2024-08-26 11:58 UTC](https://news.ycombinator.com/item?id=41356289)
      I was a kid in daycare a lot. Also, my mom (sole caregiver, besides daycare) was a registered nurse and at the time specialized in staff (i.e, direct patient care) nursing. ^c41356289

      No way was she sick 90\% of the time, or even 10\% of the time, despite the numerous alleged opportunities for infection ("daycare", staff nursing, etc).

    - **\_\_turbobrew\_\_** · [2024-08-26 02:51 UTC](https://news.ycombinator.com/item?id=41353598)
      An unpopular opinion: one of the parents is a full time care giver. ^c41353598

    - **tuna74** · [2024-08-25 18:21 UTC](https://news.ycombinator.com/item?id=41349770)
      I totally felt that! ^c41349770

      My kids almost never got sick in daycare (1-2 days per year), but especially the first year I felt like I had a cold most of the time. But it improved later years.

    - **eleveriven** · [2024-08-26 13:27 UTC](https://news.ycombinator.com/item?id=41356908)
      And reducing the productivity loss associated with parental responsibilities could benefit everybody! ^c41356908

  - **BenoitP** · [2024-08-25 16:10 UTC](https://news.ycombinator.com/item?id=41348404)
    On child \#2, can confirm. We actually planned for it. By planning for no activities. Just bunkering and resting for 2 months straight. ^c41348404

    We began partial daycare on Thursdays + Fridays in winter. Daycare is like Cancun for bacteria. Dry cold can weaken the skin, and cold is good for bacterial protein stability.

    The cycle begins: kid starts incubating on Thursday. On Saturday he's sick, and you hope for a good lottery. Diarrhea? Puking? Maybe not. But a runny nose most probably. These may ruin your nights, still.

    Sunday they are sick, and you begin to feel unwell. Monday the kids is recovering, but you're still in it. By Wednesday you should be good though. And then it's Thursday again.

    On another topic air filtering is great for the kids I'm sure; but I can't help wonder if it's just kicking the can down the road.

  - **eleveriven** · [2024-08-26 13:25 UTC](https://news.ycombinator.com/item?id=41356894)
    Schools and daycares are often places where illnesses spread quickly ^c41356894

- **modeless** · [2024-08-25 16:23 UTC](https://news.ycombinator.com/item?id=41348536)
  Near UV seems really promising for preventing indoor disease transmission as well. Has there been any more research on it lately? ^c41348536

  - **amluto** · [2024-08-25 16:46 UTC](https://news.ycombinator.com/item?id=41348773)
    Do you mean far-UVC, around 222nm?  It seemed like the major issues were the sources being expensive, the sources being from dubious vendors with no standard certification (I would be concerned that my “222nm” source might have a lot of inadvertent emission at other wavelengths), and possible damage over time to whatever you aim it at. ^c41348773

    - **PaulKeeble** · [2024-08-25 17:11 UTC](https://news.ycombinator.com/item?id=41349086)
      The bulbs only last maybe 1000 hours as well which combined with their price narrows their usage. ^c41349086

    - **modeless** · [2024-08-25 18:18 UTC](https://news.ycombinator.com/item?id=41349736)
      Yes. Those problems seem relatively easy to fix compared to the immense benefit of a significant reduction in disease transmission across the board. ^c41349736

      - **ClumsyPilot** · [2024-08-26 01:55 UTC](https://news.ycombinator.com/item?id=41353307)
        Do you actually know they are easy to fix? ^c41353307

        Here on hacker news we have a long tradition of software people claiming that some  property of a tangible world, like ‘no such material physically exists’ are easy to fix.

        - **modeless** · [2024-08-26 04:24 UTC](https://news.ycombinator.com/item?id=41354005)
          "relatively easy to fix *compared to the immense benefit*" is what I said. Even a few percent reduction in cases of these illnesses would likely be worth tens of billions of dollars for the economy every year. And it could also be justified as defense against bioweapons. A hundred billion dollar program to improve cost and establish certifications could easily be justified if efficacy and safety are good enough. And I'm certain at that level of investment (much lower, probably) cost and certification problems would be very solvable. ^c41354005

  - **emeril** · [2024-08-25 16:57 UTC](https://news.ycombinator.com/item?id=41348927)
    isn't UV light dangerous for people? ^c41348927

    perhaps there's certain wavelengths that kill viruses/bacteria but don't increase cancer risk?

    - **PaulKeeble** · [2024-08-25 17:12 UTC](https://news.ycombinator.com/item?id=41349102)
      254nm is used as part of GUV and it's not good for people and black out blinds are used in hospitals where they are installed when sanitising. Far UV 222nm is not damaging to humans that we know of but it's a peak of destruction for viruses, bacteria and fungus. ^c41349102

- **Fire-Dragon-DoL** · [2024-08-25 17:39 UTC](https://news.ycombinator.com/item?id=41349370)
  This would he huge. Aside from the huge benefit, it would be great not having runny nose or cough 6 months of the year. ^c41349370

- **coding123** · [2024-08-25 19:00 UTC](https://news.ycombinator.com/item?id=41350170)
  I actually hope building codes eventually include some kind of positive pressure system in the future where incoming air is hepa'd. PPSystems tend to clean the air the most. ^c41350170

- **thrance** · [2024-08-25 16:05 UTC](https://news.ycombinator.com/item?id=41348349)
  I'd like to see the study first, how can we know that this year's flu variant wasn't just less infectious ? What was the sample size ? What's the p-value ? ^c41348349

  - **vhcr** · [2024-08-25 16:53 UTC](https://news.ycombinator.com/item?id=41348868)
    Flu variants infectionness variability is just a so well known variable that the researchers would have to be really mediocre to not take that into account, the official press release mentions they're performing the studies on four kindergartens, so they're most probably comparing against each other. ^c41348868

    [https://www.pandemicresponse.fi/post/can-the-spread-of-flu-b...](<https://www.pandemicresponse.fi/post/can-the-spread-of-flu-be-limited-by-purifying-the-indoor-air>)

  - **Retric** · [2024-08-25 16:23 UTC](https://news.ycombinator.com/item?id=41348542)
    I get your concern, but large effect sizes make up for a multitude of sins. ^c41348542

- **DrNosferatu** · [2024-08-26 11:09 UTC](https://news.ycombinator.com/item?id=41356014)
  What kind of purifiers did they use? ^c41356014

  (couldn’t find in the posted article)

- **elevatedastalt** · [2024-08-25 16:13 UTC](https://news.ycombinator.com/item?id=41348430)
  Could this be combined with masks for greater efficacy? ^c41348430

  - **PaulKeeble** · [2024-08-25 17:16 UTC](https://news.ycombinator.com/item?id=41349147)
    N95/FFP2 Masks are even higher effectiveness. Even just one wearer can often avoid infections for years if the mask is used and fitted well. If most people are wearing them we would wipe out most respiratory disease spread. They are ridiculously effective and it's why they have been used in hospitals for decades when dealing high contagious conditions. ^c41349147

  - **tgsovlerkhgsel** · [2024-08-25 18:31 UTC](https://news.ycombinator.com/item?id=41349893)
    Certainly, but the cost (in this case probably even the *actual* cost, but mostly in terms of impact on everyday life) is vastly higher with masks - they're inconvenient and annoying, and make social interaction harder. ^c41349893

    Meanwhile, air purifiers use a bit of power (probably less of an environmental impact than the inevitable littering of masks which are basically all microplastic while looking like harmless paper), probably cost less per filter change than a week's supply of mask, and have a relatively negligible comfort impact.

  - **bluGill** · [2024-08-25 16:45 UTC](https://news.ycombinator.com/item?id=41348769)
    Most likely but nobody will allow you to suggest that. ^c41348769

    - **roywiggins** · [2024-08-25 17:14 UTC](https://news.ycombinator.com/item?id=41349122)
      Kids of daycare age probably can't wear masks effectively enough to make a difference, and if they can, it's not obvious that it's worth the effort. ^c41349122

      *Adults* could probably reduce how many colds they get by wearing masks everywhere, but most people don't think it's worth the effort.

      - **eleveriven** · [2024-08-26 13:30 UTC](https://news.ycombinator.com/item?id=41356928)
        Young children often struggle with keeping masks on properly and consistently, leading to frequent touching and adjusting... ^c41356928

  - **dumbo-octopus** · [2024-08-25 16:57 UTC](https://news.ycombinator.com/item?id=41348929)
    Masks have directly contributed to a speech development epidemic amongst youth who were deprived of their ability to see and mimic mouth movements during their prime developmental stages. This has hit underprivileged kids who do not have english spoken at home especially hard. Masks aren’t free. ^c41348929

    - **maeil** · [2024-08-25 17:37 UTC](https://news.ycombinator.com/item?id=41349352)
      Is there research that shows this? Should be incredibly easy to prove given a large percentage of the world consistently masked and another large percentage of the world consistently did not mask. ^c41349352

      For reference, I live in a country that had one of the highest masking rates in the world (probably top 10), and this does not seem to be an issue here whatsoever. Not a single time I've heard it mentioned, and given just how huge the focus on child development is here, there's no way it wouldn't be a massive topic.

      - **dumbo-octopus** · [2024-08-25 18:08 UTC](https://news.ycombinator.com/item?id=41349637)
        I’ve spoken at length with individuals directly responsible for rehabilitation of such children. But of course if the facts go against the government narrative, the “studies” will not report them. Talk to people, not studies. ^c41349637

        Do you have many cases of children being in homes where they have limited access to people speaking the national language? Do you talk to individuals who are directly responsible for teaching those folks the language?

        - **maeil** · [2024-08-25 18:21 UTC](https://news.ycombinator.com/item?id=41349774)
          I think it was clear from my comment that I haven't heard a single person (not just study) here talk about it. ^c41349774

          While it's reasonable such an adverse effect would be stronger in cases where at home a different language is spoken than the national language, it's very unlikely that it would *only* have a noticeable effect for exactly those families, with zero noticeable effect otherwise. And here, where masking rates were extremely high and amount of attention put on/money spent on child development is higher than almost anywhere else in the world, no one has ever brought it up.

          This doesn't even touch upon the fact that unprivileged families are much harder hit by epidemics (let alone Covid) in general, due to a host of other factors.

          \> But of course if the facts go against the government narrative, the “studies” will not report them.

          The studies showing that masks were incredibly effective at preventing disease spread went against the US "government narrative" at the time, since I imagine you're talking about the US.

          - **dumbo-octopus** · [2024-08-25 18:33 UTC](https://news.ycombinator.com/item?id=41349911)
            [flagged] ^c41349911

            \[flagged\]

        - **NorthTheRock** · [2024-08-25 19:16 UTC](https://news.ycombinator.com/item?id=41350326)
          \> Talk to people, not studies. ^c41350326

          So literally calling for anecdotes over data?

          - **dumbo-octopus** · [2024-08-25 19:40 UTC](https://news.ycombinator.com/item?id=41350568)
            Anecdotes are data. ^c41350568

            - **consteval** · [2024-08-26 13:46 UTC](https://news.ycombinator.com/item?id=41357057)
              Yes, incredibly small scale data. I can find someone somewhere who has experienced just about anything. Hell, they don't even have to experience it - they just need to say they do. ^c41357057

              I've known multiple people who swore potatoes cured their sickness. Yes, potatoes. No, not eaten - worn.

              My sample size is greater than yours. Does that mean potatoes cure illness purely by being in proximity to people? Probably not.

              People are dumb and unreliable. People are fueled by beliefs. And when those beliefs are challenged, almost every time this is taken as PROOF of the belief. They are untouchable. Agree with them and that's great, disagree and you're being silenced or the government or something thereby giving validity to their belief.

              Anecdotes are not meaningful data.

              - **dumbo-octopus** · [2024-08-26 13:58 UTC](https://news.ycombinator.com/item?id=41357157)
                Sure. Now dismantle “scientific” papers published by government agencies with a political motive. ^c41357157

                This is beside the point however. Both the government studies and the boots on the ground in fact agree that masking causes significant developmental disabilities, the only disagreement is the extent.

                - **consteval** · [2024-08-26 14:29 UTC](https://news.ycombinator.com/item?id=41357488)
                  I don't necessarily disagree. But I am extremely wary of people who have a "government bad" mentality. It's very easy for such people to slip into outright science denial. And then suddenly the Earth is flat, covid was planned, climate change isn't real, and 5G controls your mind. ^c41357488

                  Yes, things can have a political motive. But you ALSO have political motives, you just don't know it. For example the climate change denial has a very real political motive - to protect the oil and gas industry. Oil and gas have been denying climate since the 60s, and our government backed them because of political will.

                  Masking, during the pandemic, saved lives. This is not up for debate. Whether it's a good idea now is another question all together.

                  - **dumbo-octopus** · [2024-08-29 01:50 UTC](https://news.ycombinator.com/item?id=41386446)
                    I don’t really have much interest in engaging with your “you think X? you probably also think X Y and Z” strawmanning. It’s bad logic and makes for poor debate. ^c41386446

                    As for masking during the pandemic, it might have save some lives. It probably did. But it also contributed to long term damage of many others. Refraining from sniping an active gunman “saves lives” too, but that’s hardly the end of the discussion. Context matters.

                    - **consteval** · [2024-08-29 16:06 UTC](https://news.ycombinator.com/item?id=41392270)
                      \> you think X? you probably also think X Y and Z ^c41392270

                      That's not what I'm saying. What I'm saying is that simply distrusting the government isn't enough. It isn't enough to support any stance. You need more than that.

                      \> As for masking during the pandemic, it might have save some lives. It probably did. But it also contributed to long term damage of many others

                      I mean... no, this just isn't true. Masks didn't hurt anyone because they literally can't.

                      This is what I'm talking about. The reason people didn't want to wear masks isn't because they thought they were harmful, but rather because they were TOLD to. They didn't have anything past that.

                      Even in the worst-case scenario where masks do nothing, there's still zero reason not to wear a mask. the only reason is "gov bad". That, to me, is not enough. That's a nothing-burger. But millions ran with that. There was also some misinformation about CO2 buildup or something but, go figure, that was entirely made up by alex jones types to justify the fact they didn't want to wear a mask.

            - **dumbo-octopus** · [2024-08-25 19:42 UTC](https://news.ycombinator.com/item?id=41350584)
              “Data” is anecdotes obfuscated and p-hacked to fit the narrative the reviewers mandate. Anyone who has published in journals knows this. ^c41350584

    - **terminatornet** · [2024-08-25 18:50 UTC](https://news.ycombinator.com/item?id=41350078)
      not true [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9637007/](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9637007/>) ^c41350078

      - **dumbo-octopus** · [2024-08-25 19:02 UTC](https://news.ycombinator.com/item?id=41350193)
        I’ve talked to the boots on the ground. Government scientists publishing the official narrative are useless. ^c41350193

        - **immibis** · [2024-08-25 19:37 UTC](https://news.ycombinator.com/item?id=41350553)
          Why can't you provide any information, then? ^c41350553

          - **dumbo-octopus** · [2024-08-25 19:40 UTC](https://news.ycombinator.com/item?id=41350572)
            I just did. The specifics are of course confidential personal information from minors, you want me to publish them here? ^c41350572

            - **jbm** · [2024-08-25 22:54 UTC](https://news.ycombinator.com/item?id=41352239)
              I'm sympathetic to your views about government policies manipulating which items get studied (see: previous conservative Canadian government muzzling scientists who made comments about oil) ^c41352239

              I also agree that personal anecdotes from trusted parties are more valuable to my decision making than "data" — but those are personal anecdotes, not anecdotes from anonymous Internet personas.

              We aren't your friends and we don't know you.  Why should we trust you if you are vaguebooking about something that is a common conspiracy trope?

              - **dumbo-octopus** · [2024-08-26 13:35 UTC](https://news.ycombinator.com/item?id=41356971)
                While we’re all internet anons yapping, you shouldn’t trust me. What I implore however, is that if you or someone you share a school with develop a savior complex and start to push for involuntary masking of your children, you should damn sure make time to find some actual boots on the ground to have a good long discussion about how they personally saw those measures affect development during covid. ^c41356971

                - **terminatornet** · [2024-08-27 04:19 UTC](https://news.ycombinator.com/item?id=41364528)
                  Curious what they'd say about the effects of long covid amongst children from repeated covid infections. Seems like fatigue, brain fog, dizziness, gastrointestinal issues and heart palpitations is probably not great for learning either. ^c41364528

                  [https://www.nbcnews.com/health/kids-health/symptoms-long-cov...](<https://www.nbcnews.com/health/kids-health/symptoms-long-covid-kids-rcna167188>)

                  - **dumbo-octopus** · [2024-08-27 04:51 UTC](https://news.ycombinator.com/item?id=41364664)
                    Then ask them. ^c41364664

                    - **terminatornet** · [2024-08-29 23:05 UTC](https://news.ycombinator.com/item?id=41396265)
                      you won't tell me who they are!!! ^c41396265

            - **terminatornet** · [2024-08-25 20:38 UTC](https://news.ycombinator.com/item?id=41351176)
              source: trust me ^c41351176

              - **dumbo-octopus** · [2024-08-25 20:55 UTC](https://news.ycombinator.com/item?id=41351343)
                Even if you do elect to trust the government mandated studies more than the special education teachers directly involved in the situation, the very study the parent cited attempting to discredit me also reaches the same conclusion as me: masks cause developmental damage and their use must be carefully considered, especially as it pertains to forcing young children who can’t say “no” to comply. ^c41351343

- **eleveriven** · [2024-08-26 13:18 UTC](https://news.ycombinator.com/item?id=41356831)
  Improving indoor air quality could be a simple yet impactful measure to promote health and reduce the spread of infections ^c41356831

- **optymizer** · [2024-08-26 12:31 UTC](https://news.ycombinator.com/item?id=41356491)
  This 󠁗󠁥is 󠀠󠁤silly. 󠁯󠀠We 󠁩󠁴can 󠀠󠁦encode 󠁯󠁲data 󠀠󠁴in 󠁨󠁥plaintext. 󠀠󠁬What 󠁵󠁬then? ^c41356491

  (this 󠁺󠀮message contains a hidden secret)

- **patrickhogan1** · [2024-08-26 06:33 UTC](https://news.ycombinator.com/item?id=41354551)
  Now if they would just open the windows :) ^c41354551

- **donnaalbert** · [2024-08-27 02:13 UTC](https://news.ycombinator.com/item?id=41364034)
  [flagged] ^c41364034

  \[dead\]

- **unknown** · [2024-08-25 16:23 UTC](https://news.ycombinator.com/item?id=41348540)
  [deleted] ^c41348540

- **tgsovlerkhgsel** · [2024-08-25 18:26 UTC](https://news.ycombinator.com/item?id=41349843)
  It's amazing that this seems surprising to people after COVID. ^c41349843

  Next up:

  \* Air purifiers in schools cut parent's sick days too (not just "I need to care for my kid" days - "parent is sick" and "childless coworker of parent is sick" sick days)

  \* Air purifiers in strategic locations (high density offices, public transit, schools, ...) cut sick days across the population.

  I think this will be our generations "realizing that washing your hands before surgery makes patients die less", and it's quite embarrassing that with all the knowledge about viral transmission we couldn't figure this out *before* the pandemic, and even more embarrassing that we couldn't figure it out immediately after we tested many of these things at a large scale.

  - **JoshTriplett** · [2024-08-25 18:44 UTC](https://news.ycombinator.com/item?id=41350023)
    The challenge isn't just "figuring it out"; the challenge is also *actually putting it in place* even knowing that. Because, astonishingly, there seem to be *actual people against the concept of air purification*. (Just read through this comments section.) ^c41350023

    There were doctors and surgeons against the concept of handwashing, too, but fortunately they lost. Unfortunately, it took a long time for them to lose, and a lot of people died as a result. How do we skip that part?

    - **euroderf** · [2024-08-25 18:59 UTC](https://news.ycombinator.com/item?id=41350159)
      \> There were doctors and surgeons against the concept of handwashing, too, but fortunately they lost. ^c41350159

      Did the thinking go something like "Every pathogen that does not kill our patients only makes them stronger"?

      - **schiffern** · [2024-08-25 19:00 UTC](https://news.ycombinator.com/item?id=41350176)
        The controversy predates the germ theory of disease and the concept of "pathogens." ^c41350176

        [https://en.wikipedia.org/wiki/Ignaz\_Semmelweis](<https://en.wikipedia.org/wiki/Ignaz_Semmelweis>)

      - **mminer237** · [2024-08-25 21:15 UTC](https://news.ycombinator.com/item?id=41351509)
        It was more thinking that made no logical sense and was a bit of personal insult. Remember, the leading scientific theory at the time was that illness was caused by bad air. It would be the same as you suggesting to your doctor today that he wouldn't have killed his patient if he was wearing more deodorant. He would both think you are completely crazy and insulting. ^c41351509

        - **JoshTriplett** · [2024-08-25 22:21 UTC](https://news.ycombinator.com/item?id=41352010)
          If you had evidence showing that it seems to *work*, then whether the mechanism of action was understood yet or not, they *shouldn't* be perceiving it as crazy or insulting; they should be *doing* it, and in parallel seeking to *understand* it. ^c41352010

          (It's also possible for a study to be flawed, but even then, the reaction should be to do better, not to react with "crazy and insulting".)

      - **immibis** · [2024-08-25 19:08 UTC](https://news.ycombinator.com/item?id=41350254)
        The thinking went something like "If this were true, I'd be wrong, therefore it is not true." ^c41350254

        and possibly "If this were true, I'd be responsible for killing a hundred people, therefore it is not true."

        - **JoshTriplett** · [2024-08-25 19:15 UTC](https://news.ycombinator.com/item?id=41350313)
          Those are definitely dangerous patterns. Another dangerous one doesn't even perfunctorily start with "if this were true", but instead starts with dismissal as a perceived status-challenge ("Bah, why would we do a low-status thing?") ^c41350313

          \> some doctors were offended at the suggestion that they should wash their hands and mocked him for it

          The common thread in *all* of these, though, is not embracing a fundamental mindset of "If I'm wrong I want to know that and change and improve".

    - **maxerickson** · [2024-08-25 18:51 UTC](https://news.ycombinator.com/item?id=41350081)
      Lots of places are going to do the regulatory minimum for ventilation, and I sure haven't seen any much change to regulations. ^c41350081

    - **schiffern** · [2024-08-25 18:53 UTC](https://news.ycombinator.com/item?id=41350106) ^c41350106

      ```
        >fortunately they lost
      ```

      
      ...only after they caused a delay of 2-3 decades, directly leading to thousands of unnecessary patient deaths.

      [https://www.sciencedirect.com/science/article/abs/pii/S18788...](<https://www.sciencedirect.com/science/article/abs/pii/S1878875019330402>)

      [https://www.npr.org/sections/health-shots/2015/01/12/3756639...](<https://www.npr.org/sections/health-shots/2015/01/12/375663920/the-doctor-who-championed-hand-washing-and-saved-women-s-lives>)

      - **bugglebeetle** · [2024-08-25 19:00 UTC](https://news.ycombinator.com/item?id=41350171)
        Yeah and we’re also going to end up with decades worth of dead and disabled people to end this willful ignorance/malicious stupidity. The “COVID is over” crowd already demonstrated this. Bad ideas rarely die until all or most of the people who have them do. And even then, only sometimes! ^c41350171

        - **immibis** · [2024-08-25 19:09 UTC](https://news.ycombinator.com/item?id=41350258)
          This is downvoted because it is true but inconvenient. Humans tend to prioritize feelings over facts - just like with handwashing, "if this were true, I'd have killed people, therefore it is not true." ^c41350258

      - **JoshTriplett** · [2024-08-25 19:04 UTC](https://news.ycombinator.com/item?id=41350220)
        Yeah, I'm very aware. I'd love to know what it'd take to skip over that part. ^c41350220

    - **mdp2021** · [2024-08-25 18:50 UTC](https://news.ycombinator.com/item?id=41350068)
      \> *air purification* ^c41350068

      «Air purification» interpreted as "destroying all life in the air you breathe"? That would be an extraordinary claim and you would have to prove that it is a good idea.

      ("Air purification" can be interpreted to be about chemical and mechanical qualities, before the consideration of the living entities in the air.)

      - **jstummbillig** · [2024-08-25 19:02 UTC](https://news.ycombinator.com/item?id=41350191)
        Let's go with "air purification" as in "what air purifiers are supposed to effect, as observed in the study being discussed in this thread" ^c41350191

        - **mdp2021** · [2024-08-25 19:08 UTC](https://news.ycombinator.com/item?id=41350255)
          \> *what air purifiers are supposed to effect, as observed in the study* ^c41350255

          Which would be? Have you seen details in the submitted article? I suppose this is the study (but the page is bouncing me): [https://www.sciencedirect.com/science/article/pii/S240584402...](<https://www.sciencedirect.com/science/article/pii/S2405844024067550>)

          I have an air purifier working not two meters from me - and it is an HEPA filter with forced ventilation. Not an "air disinfectant".

          - **jstummbillig** · [2024-08-25 19:40 UTC](https://news.ycombinator.com/item?id=41350571)
            Per this study, the number of sick days. ^c41350571

            - **mdp2021** · [2024-08-26 07:40 UTC](https://news.ycombinator.com/item?id=41354856)
              No, you got confused there. The point is "what kind of air purification" should we pursue. Correctly you wrote that it should be probably that of the study - but the submission does not say what it is... Rotating mallets? HEPA? Death rays? Carbon? ^c41354856

      - **ClumsyPilot** · [2024-08-26 02:01 UTC](https://news.ycombinator.com/item?id=41353343)
        \> «Air purification» interpreted as "destroying all life in the air you breathe"? ^c41353343

        Is this sarcasm? Do you want ‘extra’ life inside your body, like tapeworms and other parasites?

        - **mdp2021** · [2024-08-26 07:55 UTC](https://news.ycombinator.com/item?id=41354925)
          \> *Is this sarcasm? Do you want ‘extra’ life inside your body* ^c41354925

          Not at all: perfectly serious. We are in a system surrounded by living entities - some innocuous, some threatening, some helpful, some being the threatening food of helpful ones...

          Your body already hosts living entities that live with you symbiotic. Some of them have the extremely important role to keep the worse others at bay through geopolitical control (you remove them, the damaging ones have free course...).

          There are many more things around you than «tapeworms and other parasites». And they could be active part of a system (which could get unbalanced without a part).

          So: before stating e.g. that all other life (e.g. in the air) should be wiped out, an intellectual inquiry about the model must be given. You do not embrace what superficially sounds like a good idea.

  - **AtlasBarfed** · [2024-08-25 20:20 UTC](https://news.ycombinator.com/item?id=41351007)
    The medical establishment  for years told everyone that viruses were spread by contact and not by air. ^c41351007

  - **dzhiurgis** · [2024-08-26 01:59 UTC](https://news.ycombinator.com/item?id=41353332)
    Hand washing mania throughout the respiratory virus pandemic was comical tho. ^c41353332

  - **mdp2021** · [2024-08-25 18:37 UTC](https://news.ycombinator.com/item?id=41349952)
    \> *I think this will be our generations "realizing that washing your hands before surgery makes patients die less"* ^c41349952

    Surely not the same thing as Semmelweis. We want to destroy microbes (and viruses) in specific contexts, not indiscriminately.

    - **pjc50** · [2024-08-25 18:50 UTC](https://news.ycombinator.com/item?id=41350072)
      \> We want to destroy microbes (and viruses) in specific contexts, not indiscriminately. ^c41350072

      Apart from the known useful ones, like gut flora: no, we really do want to destroy them indiscriminantly. We bleach surfaces to do this, we can bleach air too.

      - **jMyles** · [2024-08-25 19:06 UTC](https://news.ycombinator.com/item?id=41350234)
        Let's be a little more cautious and observant in our approach to antimicrobial stewardship. ^c41350234

        Yes, we can bleach surfaces, but pathogens (in relatively rapid terms) develop resistance \[0\].

        Yes, we can reduce bacteria at factory farms to small numbers with the indiscriminate use of antibiotics in animal feed, but it's easy to observe that this trains pathogens to avoid our most powerful chemical antibiotics.

        And so it is with fomites, respiratory pathogens, STDs, and probably even with measures to control arboviruses.

        We live in an ecological balance, and discretion is the better part of valor with regard to ensuring that this ecology becomes more likely to nurture increasingly better health outcomes.

        0: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7464077/](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7464077/>)

        - **unknown** · [2024-08-25 19:17 UTC](https://news.ycombinator.com/item?id=41350338)
          [deleted] ^c41350338

        - **immibis** · [2024-08-25 19:10 UTC](https://news.ycombinator.com/item?id=41350265)
          Humans actually live way outside of the ecological balance point. We can move the balance point, or the ecology will return us to that balance point. ^c41350265

- **64bittechie** · [2024-08-25 16:31 UTC](https://news.ycombinator.com/item?id=41348605)
  [flagged] ^c41348605

  \[dead\]

- **lurking\_swe** · [2024-08-25 16:05 UTC](https://news.ycombinator.com/item?id=41348350)
  have we learned nothing from the covid pandemic? ^c41348350

  - **pjc50** · [2024-08-25 16:39 UTC](https://news.ycombinator.com/item?id=41348702)
    Evidently not. There was lots of early good results on air purification and UV, but there was absolutely no action or even official advocacy as a result. ^c41348702

    - **mdp2021** · [2024-08-25 18:20 UTC](https://news.ycombinator.com/item?id=41349765)
      Probably a matter of cost. E.g. in some territories plexiglass screens were put everywhere between clerks and customers - as a measure that was considered more easily mandated and done (basically, simply cheaper) than modifying air treatment infrastructure. ^c41349765

      - **ClumsyPilot** · [2024-08-26 02:04 UTC](https://news.ycombinator.com/item?id=41353357)
        \> air treatment infrastructure ^c41353357

        What do you mean, like a window?

        I think we have a word for this approach - lazy

        - **mdp2021** · [2024-08-26 07:57 UTC](https://news.ycombinator.com/item?id=41354945)
          \> *What do you mean, like a* ^c41354945

          Like air disinfectants through UV (following the post mine replied to).

  - **elric** · [2024-08-25 17:22 UTC](https://news.ycombinator.com/item?id=41349206)
    What do you mean? ^c41349206

- **funnym0nk3y** · [2024-08-25 15:59 UTC](https://news.ycombinator.com/item?id=41348278)
  However I think it is important for children to get sick. Humans need pathogens to train their immune system. ^c41348278

  - **candiddevmike** · [2024-08-25 16:03 UTC](https://news.ycombinator.com/item?id=41348325)
    The hygiene hypothesis is tenuous at best and dangerous (especially for immunocompromised peers!) at worst: [https://publichealth.jhu.edu/2022/is-the-hygiene-hypothesis-...](<https://publichealth.jhu.edu/2022/is-the-hygiene-hypothesis-true>) ^c41348325

    - **dabedee** · [2024-08-25 16:23 UTC](https://news.ycombinator.com/item?id=41348535)
      From the linked article: ^c41348535

      "Almost no virus is protective against allergic disease or other immune diseases. In fact, infections with viruses mostly either contribute to the development of those diseases or worsen them.

      The opposite is true of bacteria. There are good bacteria and there are bad bacteria. The good bacteria we call commensals. Our bodies actually have more bacterial cells than human cells. What we’ve learned over the years is that the association with family life and the environment probably has more to do with the microbiome. So one thing I would say is sanitizing every surface in your home to an extreme is probably not a good thing. Our research team showed in animals that sterile environments don’t allow the immune system to develop at all. We don’t want that."

      - **jph00** · [2024-08-25 18:18 UTC](https://news.ycombinator.com/item?id=41349741)
        Commensal bacteria are generally not airborne, whilst viruses that harm the immune system often are. So surface hygiene can be overdone, but air hygiene is a good idea. ^c41349741

    - **actuallyalys** · [2024-08-25 16:19 UTC](https://news.ycombinator.com/item?id=41348486)
      Like your article states, there’s some evidence for exposure to *benign* microbes reducing *allergies*, but that is completely different than pathogens strengthening the immune system. Unfortunately some people seem to have remembered the hygiene hypothesis as meaning that microbes of all kinds are actually good. ^c41348486

      There’s also a concept of immunity debt, although that’s more of an explanation for certain diseases being especially bad the year following COVID restrictions than an argument for exposure.

    - **elevatedastalt** · [2024-08-25 16:15 UTC](https://news.ycombinator.com/item?id=41348457)
      Hardly anyone even thinks about peanut allergies in a nation of 1.4 billion people (India) and kids don't drop dead like flies here. ^c41348457

      But sure, let's just call the hygiene hypothesis tenuous.

      - **elric** · [2024-08-25 17:21 UTC](https://news.ycombinator.com/item?id=41349194)
        I thought the recommendation was to introduce some peanuts at an early age in order to reduce the risk of getting peanut allergies? ^c41349194

      - **yreg** · [2024-08-25 16:28 UTC](https://news.ycombinator.com/item?id=41348578)
        Peanut allergy prevalence in India seems to be 0.3\%, while in the western countries it's 1.5-3\%. ^c41348578

      - **kylehotchkiss** · [2024-08-25 16:43 UTC](https://news.ycombinator.com/item?id=41348751)
        Or even seasonal allergies to like pollen too, right? There’s just much more pressing breathing related issues to be concerned with (AQI etc) ^c41348751

      - **candiddevmike** · [2024-08-25 16:18 UTC](https://news.ycombinator.com/item?id=41348480)
        That's not at all the same thing. ^c41348480

      - **consteval** · [2024-08-26 13:52 UTC](https://news.ycombinator.com/item?id=41357112)
        Could it be that people in India have different genetic makeup than people in other countries? ^c41357112

        I mean, many populations have more/less risk of many physiological things. That's just how it goes.

        Black men are at much higher risk of prostate cancer. White people of melanoma. As a man, I pretty much don't have to worry about autoimmune disorders because my risk is 1/10th that of a woman's. But, my risk of heart disease is much higher - even at the same weight!

      - **arresin** · [2024-08-25 16:55 UTC](https://news.ycombinator.com/item?id=41348896)
        A: different genes, B: Different reporting standards, C: different access to healthcare for it to be reported ^c41348896

  - **switch007** · [2024-08-25 16:46 UTC](https://news.ycombinator.com/item?id=41348779)
    I've had COVID multiple times and each time my immune system takes a bigger and bigger battering, leading to many other issues. ^c41348779

    Are the benefits of this theory meant to start appearing any time soon...?

  - **WithinReason** · [2024-08-25 16:01 UTC](https://news.ycombinator.com/item?id=41348306)
    How often and how sick? The more the better? ^c41348306

    - **appplication** · [2024-08-25 16:08 UTC](https://news.ycombinator.com/item?id=41348385)
      It’s a good question. Obviously infinite sick is not desirable. If it were possible to induce antibodies via e.g. broad spectrum vaccinations would we see less sick kids in total? ^c41348385

      After all the merits are supposedly eventual conferred immunity, not physically being ill. No reason to think you need to be sick to benefit.

  - **Etheryte** · [2024-08-25 16:12 UTC](https://news.ycombinator.com/item?id=41348422)
    This oversimplifies the original idea behind what you're trying to recall. Being sick in and of itself is not the beneficial part, it's exposure that can be beneficial in certain cases. If you can get the exposure without actually falling ill it's all the better, it's a win-win. Note that not all exposure is good, for example you never want to be exposed to the bubonic plague if at all possible. ^c41348422

  - **\_dain\_** · [2024-08-25 16:09 UTC](https://news.ycombinator.com/item?id=41348396)
    Immune system won't help against air pollution from traffic and factories and forest fires. ^c41348396

  - **Arnt** · [2024-08-25 16:07 UTC](https://news.ycombinator.com/item?id=41348372)
    That sounds plausible, but do you think it's better to be more sick than less? ^c41348372

    Or do you just think that having a few sick days per year is better than marching into work no matter what state you're in? A very different proposition.

    - **nradov** · [2024-08-25 16:32 UTC](https://news.ycombinator.com/item?id=41348617)
      I suspect it's probably better to shift the sick days earlier in life. We probably can't significantly reduce the total. There are hundreds of endemic upper respiratory viruses and we all eventually get infected with most of them. It's just a matter of time. Our immune systems generally degrade as we age, so over the long run it's probably better to get infected when we're younger so that we can build immunity that protects us when we're older. ^c41348617

      - **coryrc** · [2024-08-25 17:07 UTC](https://news.ycombinator.com/item?id=41349038)
        \> We probably can't significantly reduce the total ^c41349038

        That's ridiculous. During the crisis times of covid, the incidences of other communicable disease dropped significantly. Plus, to be frank, this is just an idiotic suggestion with zero reasons to think there's some set number of days people are sick. Before having kids in daycare I was rarely sick. I had a child not in daycare and was never sick. Now we're sick all the time, which wouldn't happen if my wife could stay home with them or we didn't have kids.

        - **Izkata** · [2024-08-25 19:56 UTC](https://news.ycombinator.com/item?id=41350712)
          "Other" meaning "flu", which only dropped because they stopped tracking it to give resources to SARS-CoV-2.  There was a note on the CDC website that very few people actually noticed, and almost all claims of reduced transmission used the CDC's FluView as their evidence. ^c41350712

        - **nradov** · [2024-08-25 17:19 UTC](https://news.ycombinator.com/item?id=41349179)
          That's ridiculous. The interventions put in place during the crisis times of COVID were obviously unsustainable. When restrictions were lifted, the incidence of all other types of respiratory viruses spiked up. ^c41349179

          I've had kids in daycare as well. Occasionally you get the sniffles. So what.

          - **Arnt** · [2024-08-26 08:51 UTC](https://news.ycombinator.com/item?id=41355212)
            The story describes something that cut the average number of sick days by around 30\%. Is 30\% significant, in your opinion? ^c41355212

      - **consteval** · [2024-08-26 13:54 UTC](https://news.ycombinator.com/item?id=41357128)
        \> We probably can't significantly reduce the total ^c41357128

        Considering it used to be commonplace to have 10 children and then maybe 2/3 make it to adulthood, I would say we absolutely can and have reduced the total number of sick days. We've also reduced the severity of sickness.

      - **pjc50** · [2024-08-25 18:56 UTC](https://news.ycombinator.com/item?id=41350127)
        \> We probably can't significantly reduce the total ^c41350127

        We can and we have. Through things such as the measles vaccine.

        People forget that child mortality used to be a thing.

        - **nradov** · [2024-08-25 19:53 UTC](https://news.ycombinator.com/item?id=41350671)
          Sure, childhood immunization is great but we're not discussing measles here. Measles is a single, relatively stable virus that's easy to vaccinate against. But children in daycare facilities mostly get infected with upper respiratory viruses. There are literally hundreds of such endemic viruses, especially rhinoviruses but also coronaviruses and others. We aren't likely to have effective vaccines against those any time soon. If children aren't exposed to them in daycare then they'll be exposed somewhere else. Those viruses aren't going away and will continue circulating through the population no matter what we do. ^c41350671

  - **lbrito** · [2024-08-25 19:55 UTC](https://news.ycombinator.com/item?id=41350706)
    Don't worry, there will still be plenty of sickness. The article says 1/3 reduction. If you have kids, you'll know that the resulting number of sick days is still huge. ^c41350706

  - **duxup** · [2024-08-25 16:38 UTC](https://news.ycombinator.com/item?id=41348687)
    They're still getting sick. ^c41348687

  - **AwaAwa** · [2024-08-25 16:01 UTC](https://news.ycombinator.com/item?id=41348305)
    While I personally agree with this sentiment, the last few years have made it amply clear that the population prefers padded rooms to icky playground sandlots. ^c41348305

    - **error\_logic** · [2024-08-25 17:25 UTC](https://news.ycombinator.com/item?id=41349236)
      Nuance: They're still getting exposed and thus gaining immunity with the environmental filtering, just not so much viral load as to be out of school \[as often\]. ^c41349236

      It's a win-win from that perspective and dismissing that serves no one in the end.

      - **Sakos** · [2024-08-25 18:24 UTC](https://news.ycombinator.com/item?id=41349822)
        This tiny but significant factor is also why masks, even surgical masks, are so helpful. They don't need to prevent 100\% transmission, just reduce the viral load received or passed on. ^c41349822

- **jimberlage** · [2024-08-25 21:12 UTC](https://news.ycombinator.com/item?id=41351484)
  As much as I hate the amount of illnesses my kids get from daycare - maybe this shouldn't be a goal?  In workplaces, hospitals, etc. we definitely want to reduce illness.  In daycares, the kids are all building their immune systems and the contact with germs is a vital part of that. ^c41351484

  I definitely understand the teachers don’t want to be sick, and it’s a hardship on parents to keep kids home, so it’s not all about the kids’ health.  But the kids’ health might be better served by letting them get more minor illnesses, not less.

  - **analog31** · [2024-08-25 21:20 UTC](https://news.ycombinator.com/item?id=41351542)
    Even a third less is probably still plenty. And the putative immune system benefit strikes me as hypothetical unless the exposure and effect are quantified. ^c41351542

    - **stoperaticless** · [2024-08-25 21:22 UTC](https://news.ycombinator.com/item?id=41351560)
      What do you think about vaccines? ^c41351560

      - **analog31** · [2024-08-25 21:28 UTC](https://news.ycombinator.com/item?id=41351621)
        Well, I've got all mine, unless another booster is available that I don't know about. One thing about vaccines is that you know exactly who got them, and who didn't. This probably makes it a lot easier to study. ^c41351621

        And I'm willing to believe that some childhood exposure to pathogens is beneficial, but I don't think we know how much of a good thing is enough, or too much.

        - **jimberlage** · [2024-08-26 10:14 UTC](https://news.ycombinator.com/item?id=41355666)
          Do you think that we’ve discovered and cataloged the sum total of milder pathogens that protect against worse illnesses in a lab?  Got all mine means “got all the ones we currently know enough about to develop a vaccine for.” ^c41355666

          - **analog31** · [2024-08-26 22:24 UTC](https://news.ycombinator.com/item?id=41362840)
            No, I don't think we've discovered the sum total of milder pathogens. ^c41362840

  - **alliao** · [2024-08-25 21:24 UTC](https://news.ycombinator.com/item?id=41351569)
    I'd agree based on my own bias which appeals to nature, and thus can only agree if the environment's somewhat untouched. but we've introduced so much into our environment, from tyre/brake dust to micro plastic to covid, I'd really much rather we just clean the air. we are not anime protagonist that evolve in real time, evolution in the real world consists of the unfit dying, and the ones that lives reproduce etc ^c41351569

  - **4fterd4rk** · [2024-08-25 21:21 UTC](https://news.ycombinator.com/item?id=41351553)
    There is zero proof that this is the case. ^c41351553

