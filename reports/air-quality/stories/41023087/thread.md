# [Ventilation Made Easy](https://news.ycombinator.com/item?id=41023087)

Article: [https://www.mpg.de/16075350/1127-chem-ventilation-made-easy-152990](<https://www.mpg.de/16075350/1127-chem-ventilation-made-easy-152990>)

Tomte · 2024-07-21 07:01 UTC · 37 reported comments · archived 2026-11-08 13:36 UTC
Observation: 2026-11-08 13:35 UTC → 2026-11-08 13:36 UTC

## Comments

- **hedgehog** · [2024-07-21 17:36 UTC](https://news.ycombinator.com/item?id=41026649)
  This is a pretty cool project, it's basically a retrofit approach to what in industry is known as "displacement ventilation" or "stratification ventilation". In the US our typical approach is "mixing ventilation" where you try to mix and equalize the air everywhere within a space, then cycle a portion of the air through an air conditioner to get the temperature and humidity to the desired level. This is mechanically intensive, needs big ducts, and has the downside that contaminants in the air tend to get spread everywhere. Displacement ventilation uses the fact that hot and humid air rise, instead of mixing everything together it removes the most stale air at the top of the room and replaces it. Trickier to get right, but quieter and more effective in many cases. ^c41026649

  Here's a blog post with illustrations:

  [https://blog.hoffman-hoffman.com/blog/the-basics-of-displace...](<https://blog.hoffman-hoffman.com/blog/the-basics-of-displacement-ventilation>)

  - **kurthr** · [2024-07-21 17:45 UTC](https://news.ycombinator.com/item?id=41026703)
    For efficiency you need to minimize leakage of outside conditions, but you also really need a heat/energy exchanger (HRV/ERV) at the fresh air input so that you're not recirculating stale air. ^c41026703

    - **toast0** · [2024-07-21 20:43 UTC](https://news.ycombinator.com/item?id=41027928)
      School buildings with operable windows often don't condition the air. This design collects / guides air from around the pupils towards an exhaust window and suggests leaving a door or opposite site window to get fresh air in. It's not a solution for highly conditioned spaces. ^c41027928

      - **kurthr** · [2024-07-22 15:30 UTC](https://news.ycombinator.com/item?id=41035591)
        Just thinking about Germany, I'm wondering when peak infections occur. I'd guess that it's during the winter? ^c41035591

        I have not heard that Germany's winters have become particularly mild. In fact Mainz, where this was developed, often has high temperatures below freezing during the winter months. Having significant airflow without an HRV might make people a bit chilly in the morning.

        Or would this still require the expensive filtration system in the winter?

        - **hedgehog** · [2024-07-22 17:23 UTC](https://news.ycombinator.com/item?id=41036942)
          I'm not sure what the overall calculation looks like but if you remove 10-15 liters per minute per occupant to match normal respiration that's a pretty small loss of heat. Maybe a net win if it reduces need for other ventilation and dehumidification enough. It's not just an infection control thing, the building needs some fresh air anyway to get fresh air in and remove CO2 + all the other nasties that accumulate indoors (cleaning chemicals, radon, various solvents plasticizers, even stuff wafting out of the floor if like some major offices in the valley you're built on contaminated ground). ^c41036942

          - **kurthr** · [2024-07-22 23:01 UTC](https://news.ycombinator.com/item?id=41040723)
            So call it 400 liters/min at 30C delta with air's heat capacity about 1kJ/kg/C and 800 liters/kg. You're at 15kJ/min or 250W just for that airflow. Figure there are 40 rooms and you're at 10kW of heating just for that fresh air flow. An ERV can cut that by 90\%. ^c41040723

            You just saved 9kW of continuous power for the building during the winter with an ERV.

- **adolph** · [2024-07-21 17:37 UTC](https://news.ycombinator.com/item?id=41026655)
  *Due to its low material and operating costs, it could turn out to be a clever alternative to expensive filter systems and ventilation by shortly wide opening the windows.* ^c41026655

  This is a neat idea that seems penny smart and pound foolish. For one, the article does not address overall system reliability and maintenance tempo. Given a low material to install cost ratio this is an important factor since repeated re-installation or rework will moot any cost savings from materials.

  For two, ejecting the gases that have been expensively conditioned for thermal and humidity properties will drive up operating costs since replacement gasses will be required.

  For three, hopefully they carefully plan for where the system exhausts since they have made something that concentrates contaminants as well as it evacuates them. To the extent that it uses tragedy of the commons to get better odds for people indoors by worsening odds for people outside that building, the primary innovation of the system is statistical arbitrage based on a larger outdoor volume.

  - **toast0** · [2024-07-21 20:35 UTC](https://news.ycombinator.com/item?id=41027871)
    \> For two, ejecting the gases that have been expensively conditioned for thermal and humidity properties will drive up operating costs since replacement gasses will be required. ^c41027871

    This application optimizes exhaust in rooms with operable, high mounted windows for exhaust. Most rooms with expensive conditioning don't have operable windows, so it's not really an option to use this design for those anyway. In a heavily conditioned space, the expectation would be external air ventilation would be managed near the centralized air handlers. Plenty of options there, like HRV/ERV depending on climate specifics.

    It might be possible to use a similar design to augment air returns from a conditioning system, but it's going to depends on the system if it would be useful or reasonable.

- **danjc** · [2024-07-21 17:44 UTC](https://news.ycombinator.com/item?id=41026690)
  (2020) ^c41026690

- **aaron695** · [2024-07-22 03:27 UTC](https://news.ycombinator.com/item?id=41030668)
  [flagged] ^c41030668

  \[dead\]

- **jkljl** · [2024-07-22 13:04 UTC](https://news.ycombinator.com/item?id=41033880)
  [flagged] ^c41033880

  \[flagged\]

- **lihli** · [2024-07-24 15:18 UTC](https://news.ycombinator.com/item?id=41057967)
  [flagged] ^c41057967

  \[flagged\]

- **constantcrying** · [2024-07-21 16:05 UTC](https://news.ycombinator.com/item?id=41026034)
  What a time that was... ^c41026034

  Really glad it is over and that it never got the point of me ever seeing such a thing.

  - **nequo** · [2024-07-21 17:07 UTC](https://news.ycombinator.com/item?id=41026439)
    This is about more than pandemics, it is about indoor air quality in crowded spaces: ^c41026439


    ```
      “Our system also solves the long-standing problem of CO2 in classrooms, because it not only transports aerosols outside. It also cuts CO2 accumulation, helping students to concentrate better on their lessons.”
    ```

    - **constantcrying** · [2024-07-21 17:27 UTC](https://news.ycombinator.com/item?id=41026584)
      Oh, so Europeans have finally invented air conditioning? ^c41026584

      Of course when I was in school we opened the windows to solve this massive issue, but times change I guess. Hopefully they also have an app, for the kids.

      - **jimkleiber** · [2024-07-21 17:34 UTC](https://news.ycombinator.com/item?id=41026634)
        I'm not sure if you've ever lived in a place where you're not supposed to drink the tap water because it can bring a lot of disease. I think we as humans realized that water carried a lot of disease and in many places started treating water much better to protect our health. To me it seems very logical that we should also treat the air to protect our health from diseases carried in the air. ^c41026634

        - **constantcrying** · [2024-07-21 17:41 UTC](https://news.ycombinator.com/item?id=41026670)
          \>I'm not sure if you've ever lived in a place where you're not supposed to drink the tap water because it can bring a lot of disease. ^c41026670

          Can't say I have ever done that.

          \>To me it seems very logical that we should also treat the air to protect our health from diseases carried in the air.

          There is an absolutely great feature of air, which makes it totally distinct from water. If you open the window inside and outside air will mix. I know this is kind of miraculous and might just be a very big deal, but I think it could allow us to replace the stale air in the inside with fresh air from the outside.

          - **jimkleiber** · [2024-07-21 17:55 UTC](https://news.ycombinator.com/item?id=41026769)
            Fair point on that its vastness allows quick recycling. They do this in Germany a lot, where even in deep winter they'll open windows to recycle the air. ^c41026769

            I think there are a few challenges to this:

            1) It's mostly manual, compared to an automatic ventilation system. Perhaps if it were more automated, I'd agree with you.

            2) If it's very hot or cold or humid outside, I think doing this can impact indoor conditions and I'm not sure how much that energy cost compares to other forms of ventilation.

            3) Not every part of an indoor space is very close to a window. Large indoor spaces, underground indoor spaces, small ebclosed areas such as bathrooms in the middle of homes, etc., may make it hard to just open a window and flush out the "bad" air.

      - **pixelfarmer** · [2024-07-23 13:14 UTC](https://news.ycombinator.com/item?id=41045653)
        This whole system was aimed at minimizing the infection rates between students which you won't solve by just opening the windows. Imagine you have some smoker indoors: How do you transport off that cancer inducing poisonous cloud without distributing it in the whole place? ^c41045653

        Plus in Germany there are quite a few schools located directly at heavily used streets, so just opening windows will not exactly give you really fresh air (I mean, it will lower the CO2, but otherwise its going from one bad state into another), plus it increases the noise levels considerably.

        And yes, ACs are still uncommon in Germany. In return, most buildings, including suburb style homes, are not just made from cardboard. This means the buildings have a lot of thermal inertia which can be used to manage heat during hotter phases.

      - **nequo** · [2024-07-21 17:42 UTC](https://news.ycombinator.com/item?id=41026682)
        Your dismissive response is uncalled for. Air conditioning does not dispose of CO2 in the air, and opening the windows is not always feasible. For example, if the outside air is hot or humid. Ventilation has actual use cases. ^c41026682

        - **constantcrying** · [2024-07-21 17:45 UTC](https://news.ycombinator.com/item?id=41026706)
          \>Air conditioning does not dispose of CO2 in the air ^c41026706

          Anything which circulates the air will remove it.

          \>and opening the windows is not always feasible. For example, if the outside air is hot or humid.

          I can tell you with 100\% certainty that hot or humid air does not prevent you from opening a window. I myself have done this multiple times.

          - **adolph** · [2024-07-21 18:59 UTC](https://news.ycombinator.com/item?id=41027282)
            \>\>Air conditioning does not dispose of CO2 in the air ^c41027282

            \> Anything which circulates the air will remove \[CO2\]

            Circulation does not remove CO2, only displace it from one place to another. To remove it, you need a scrubber \[0\].

            0\. [https://en.wikipedia.org/wiki/Carbon\_dioxide\_scrubber](<https://en.wikipedia.org/wiki/Carbon_dioxide_scrubber>)

          - **nequo** · [2024-07-21 17:49 UTC](https://news.ycombinator.com/item?id=41026737)
            Beyond a certain point, humid air causes mold and hot air makes it hard to get any work done. This is not some esoteric idea. The northern hemisphere has just gone through a two week heat wave. ^c41026737

            If your bio is up to date, I wish you the best in whatever your life situation.

            - **constantcrying** · [2024-07-21 17:57 UTC](https://news.ycombinator.com/item?id=41026787)
              \>If your bio is up to date, I wish you the best in whatever your life situation. ^c41026787

              Thankfully it isn't. And I escaped from writing software.

      - **adolph** · [2024-07-21 17:41 UTC](https://news.ycombinator.com/item?id=41026672)
        It would be an interesting experiment to inject additional oxygen into school air supplies. ^c41026672

        On the other hand, following the principle of “train high, play low” it might be better to educate in lower oxygen and then add oxygen to workplaces.

        - **constantcrying** · [2024-07-21 17:46 UTC](https://news.ycombinator.com/item?id=41026713)
          Maybe, of course putting people permanently on oxygen to improve performance is not a viable alternative. ^c41026713

  - **redrove** · [2024-07-21 16:59 UTC](https://news.ycombinator.com/item?id=41026386)
    Are you actually insinuating there still isn’t a pandemic going on or am I misreading your comment? ^c41026386

    I don’t see how this couldn’t possible be anything but beneficial in public places.

    - **\_def** · [2024-07-21 17:18 UTC](https://news.ycombinator.com/item?id=41026513)
      Maybe they are referencing that the article is from Dec 2020. I agree, it still seems highly useful. ^c41026513

    - **constantcrying** · [2024-07-21 17:22 UTC](https://news.ycombinator.com/item?id=41026544)
      Not a pandemic that has any relevance to me, above the prevalence of the common cold. ^c41026544

    - **baggy\_trough** · [2024-07-21 17:02 UTC](https://news.ycombinator.com/item?id=41026403)
      I mean, there isn't? Just endemic viruses, as we always have had, and always will have. ^c41026403

      - **redrove** · [2024-07-21 17:05 UTC](https://news.ycombinator.com/item?id=41026415)
        Putting that aside, don’t you then agree ventilation in public spaces is useful for obvious health reasons? ^c41026415

        - **constantcrying** · [2024-07-21 17:23 UTC](https://news.ycombinator.com/item?id=41026550)
          Hilariously Air conditioning is very common in the US but very uncommon in Europe. ^c41026550

          Is there actually any evidence of a positive effect?

          - **eep\_social** · [2024-07-21 17:33 UTC](https://news.ycombinator.com/item?id=41026631)
            The Minergie (Swiss) folks probably have a 90 page application guide that goes into those kinds of details: [https://www.minergie.com/media/guia\_de\_aplicacion\_latam\_v202...](<https://www.minergie.com/media/guia_de_aplicacion_latam_v2023_1_en.pdf>) ^c41026631

            - **constantcrying** · [2024-07-21 17:42 UTC](https://news.ycombinator.com/item?id=41026681)
              Why are you just sending me a 90 page PDF about housing regulation. Obviously that does not contain a shred of scientific evidence that filtering certain particles reduces transmission of infectious diseases. ^c41026681

              Genuinely no idea what you are thinking with this or what the point of that PDF is.

              - **eep\_social** · [2024-07-21 18:29 UTC](https://news.ycombinator.com/item?id=41027057)
                \> housing regulation ^c41027057

                is it? I think you may want to do some research of your own.

                - **constantcrying** · [2024-07-21 18:45 UTC](https://news.ycombinator.com/item?id=41027192)
                  Your document contains zero relevant information and you refused to point to any specific part of its 90 pages. Obviously you have no evidence for your claims and you made stuff up by linking to an irrelevant document and then being extremely obtuse and annoying when being asked to substantiate what you are saying or even to specify why the document contains relevant information. ^c41027192

                  If you have zero evidence of a claim being true, stop making it.

                  - **eep\_social** · [2024-07-22 02:24 UTC](https://news.ycombinator.com/item?id=41030361)
                    Great discussion thanks! ^c41030361

                    - **Vegemeister** · [2024-07-22 15:18 UTC](https://news.ycombinator.com/item?id=41035454)
                      Clown if you want, but he's absolutely right. There is exactly one sentence in that entire damn thing that comes close to touching on the question of *why* ventilation is desirable, and it is: ^c41035454

                      \>Pleasant, healthy air to breathe is the most important food
                      for human beings.

                      - **eep\_social** · [2024-07-22 19:50 UTC](https://news.ycombinator.com/item?id=41039034)
                        I’m clowning because OP seems to be mostly dedicated to whining. ^c41039034

                        To your point, the original post requested information specific to European standards where AC is not common. I don't care to spend time solving internet stranger’s problems but Minergie would be a good place to start because they presumably didn’t fabricate their standards. A curious, motivated person could track down whatever they’ve published, which is most likely in German.

        - **baggy\_trough** · [2024-07-22 04:51 UTC](https://news.ycombinator.com/item?id=41031011)
          That case would have to be made scientifically by credible researchers, which is a lot to ask these days. ^c41031011

