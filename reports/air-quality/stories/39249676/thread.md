# [Association of long-term exposure to air pollution w retinal neurodegeneration](https://news.ycombinator.com/item?id=39249676)

Article: [https://www.sciencedirect.com/science/article/abs/pii/S0013935123011684](<https://www.sciencedirect.com/science/article/abs/pii/S0013935123011684>)

bookofjoe · 2024-02-04 12:21 UTC · 9 reported comments · archived 2026-11-08 13:30 UTC
Observation: 2026-11-08 13:30 UTC → 2026-11-08 13:30 UTC

## Comments

- **blagie** · [2024-02-04 14:30 UTC](https://news.ycombinator.com/item?id=39250454)
  This is a very good paper. The effect size is quite significant (\>60\% speed-up for ageing). ^c39250454

  I will reiterate: Correlation does not imply causation. The next step is to look for root causes.

  \* Air pollution is correlated with traffic is correlated with carbon monoxide.

  \* Air pollution is correlated with dirty areas is correlated with water population.

  \* Air pollution is correlated with city (rather than rural) life which is correlated with spending time in-doors.

  ... and so on. My experience is that nine times out of ten, a paper like this does not point to a root cause, but is rather the start of detective work to figure out what's actually going on.

  That first clue is essential. The problem is the media than picks up on this and says PM2.5 \=\= blindness, and we waste a bunch of resources on something which usually does not turn out to be a significant effect.

  (As a footnote: PM2.5 is significant enough for many other things that I recommend every room have a basic air filter, or for once with forced air, a furnace filter with a high MERV rating. However, I don't recommend people spend a lot here.)

  - **bookofjoe** · [2024-02-04 14:36 UTC](https://news.ycombinator.com/item?id=39250487)
    Concur re: furnace filter with high MERV rating — but they are very expensive. ^c39250487

    I use 3M Filtrete MPR 2800 (MERV 14)

    [https://www.filtrete.com/3M/en\_US/p/d/b00039984/](<https://www.filtrete.com/3M/en_US/p/d/b00039984/>)

    - **blagie** · [2024-02-04 14:53 UTC](https://news.ycombinator.com/item?id=39250617)
      They're not if you use them well! ^c39250617

      Factoids:

      \- These furnace filters have a 3-month lifespan due to big particles. Adding a cheap, coarse prefilter in front will expand the lifespan to be very, very long, indeed. It won't impede airflow much either (it will be limited by the MERV14 one).

      \- At least in my environment, even cheap room filters make the steady-state air in normal rooms clean enough to not matter. I have a bigger one, mostly so I can run it on the lowest setting and have no noise.

      \- Most filters usually last many times their manufacturer-rated life, and continue to filter fine until they look pretty decrepit. Even this can be expanded by vacuuming them once in a while. With room air filters, this is easy. With HVAC, you do need to be a little bit careful since you don't want to impede airflow. An older filter will continue to filter fine, but will not pass through air nearly as easily.

      \- With room filters, there is very little difference between HEPA and a high MERV rating. It's air flow times \% particles removed. An 85\% efficient filter with a fan 20\% faster will be cheaper and better than a 100\%. HVAC is more complex.

      Even if you use them the manufacturer-rated way, costs are a tiny fraction of expected cost of health care almost any way you run the numbers.

      - **bookofjoe** · [2024-02-04 15:09 UTC](https://news.ycombinator.com/item?id=39250749)
        \>Adding a cheap, coarse prefilter in front will expand the lifespan to be very, very long, indeed. It won't impede airflow much either... ^c39250749

        Can you direct me to a reference on this statement? Is there any guidance from 3M on employing an added filter or vacuuming them? I couldn't find any. How much longer a lifespan is "very, very long...? I did not know this and I would like to learn more.

        I am always struck by how pitch black and opaque my filters are when I replace them at the prescribed 3-month intervals.

        One more thing: my ancient oil furnace/heat pump only has the capacity to accept one air filter at a time: without rebuilding it, there is no way to add a prefilter.

        \>... costs are a tiny fraction of expected cost of health care almost any way you run the numbers.

        I concur with your conclusion completely: this is the best investment you can make in your future and the futures of those who reside in your domicile.

        - **blagie** · [2024-02-04 16:08 UTC](https://news.ycombinator.com/item?id=39251377)
          I can't direct you to a reference. Most of what I wrote is based on two things: ^c39251377

          1) My own experiments.

          You can monitor PM2.5 levels accurately with a PMS5003 (\$40 on Adafruit) plugged into an ESP32 (\$10 on Adafruit) and ESPHome + Home Assistant, or you can splurge and get a full suite of sensors (\<\$100). That's what I did because it's fun and educational. Expect to spend a few hours setting it up. It's well-documented, but it's not quite plug-and-play. Friday evening will likely suffice, but it might be a full weekend if you run into problems.

          Heck, if you want to monitor pressure drop across your filter, you can get a pair of pressure sensors (\$7 each, or \$20 for a fancier multisensor like a BME688).

          Or you can get an Apollo Air or an AirGradient for \<\$200. Or you can get something from a company like Ambient Weather for easy and fully integrated.

          Don't go for cheap on Aliexpress / Amazon / eBay, though, since many of these are fakes.

          Monitoring PM2.5 levels in my room, I would see a drop in filtration if I needed to replace a filter due to filtration issues. Fans also get louder when they're overloaded. That's a good sign I need to vacuum something. You could do acoustic monitoring too, if you were fancy :)

          2) Basic theory.

          A good book on -- of all things -- acoustics will show you how to model air pressure as voltage, something like a filter as a resistor, and a fan as a source. That gives good intuition for how filters stack.

          3) Reading web forums, where others did similar. That matches what I see and theory.

          From that:

          The best design I see (e.g. a Coway AirMega 200) has three layers:

          \- Washable prefilter

          \- Carbon filter

          \- HEPA filter

          Just using it, I see most of the stuff caught by the prefilter, followed by carbon, followed by HEPA. It's visible. I see the same thing on things I've built (e.g. box fan + high MERV + super-cheap filter duct-taped together in my basement), and in things like vacuum cleaners.

          So there you have it. My comments were based on my intuition backed up by my measurements at my house. Your mileage may vary. I can well imagine these things being different in a rural home with all sorts of pollens versus a city home with pollution from cars.

          The washable prefilter is very thin. A sheet would fit without modification. But if it were me, I'd modify and use a full stack, because it's fun to make things :)

          - **bookofjoe** · [2024-02-04 17:02 UTC](https://news.ycombinator.com/item?id=39251992)
            Yes, it's fun to make things. If only I had 1\% of your technical knowledge.... Alas, I'm a 75-year-old retired neurosurgical anesthesiologist (38 years in practice through 2015 when I hung up my laryngoscope) whose expertise in mechanical and computer technology outside my specialty is essentially zilch. But I love reading about stuff as you described it. For me, building Lego constructions with my grandson is as good as it's ever gonna get. ^c39251992

            - **blagie** · [2024-02-04 22:55 UTC](https://news.ycombinator.com/item?id=39255382)
              Good news is as retired neurosurgical anesthesiologist, you can afford \$50 every 3 months, so it probably doesn't matter. ^c39255382

              Regarding Lego, it can get better! Horrible web site, but have a look at Engino Discovering STEM. The kits are waaay better than Legos for creative building with kids.

              - **bookofjoe** · [2024-02-06 12:57 UTC](https://news.ycombinator.com/item?id=39273707)
                Super. I'm on it. Thanks for the Engino tip! ^c39273707

                - **bookofjoe** · [2024-02-09 17:19 UTC](https://news.ycombinator.com/item?id=39317411)
                  Just got him this for his upcoming 8th birthday: ^c39317411

                  [https://www.amazon.com/dp/B087MZ3SJV?ref\=ppx\_yo2ov\_dt\_b\_prod...](<https://www.amazon.com/dp/B087MZ3SJV?ref=ppx_yo2ov_dt_b_product_details&th=1>)

- **unknown** · [2024-02-04 13:27 UTC](https://news.ycombinator.com/item?id=39250026)
  [deleted] ^c39250026

