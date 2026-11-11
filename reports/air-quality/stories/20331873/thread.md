# [Cutting through the smog: making an air quality bot with Haskell](https://news.ycombinator.com/item?id=20331873)

Article: [https://engineering.linecorp.com/en/blog/cutting-through-the-smog-making-an-air-quality-bot-with-haskell/](<https://engineering.linecorp.com/en/blog/cutting-through-the-smog-making-an-air-quality-bot-with-haskell/>)

moleike · 2019-07-02 03:20 UTC · 11 reported comments · archived 2026-11-08 11:04 UTC
Observation: 2026-11-08 11:04 UTC → 2026-11-08 11:04 UTC

## Comments

- **t0mek** · [2019-07-02 08:56 UTC](https://news.ycombinator.com/item?id=20333368)
  I've been working on a side project related to the air quality too, for a few months now. However, the technology stack is less impressive than Haskell: plain PHP7 + MySQL. I just wanted to have a single page presenting the air quality stats \[1\], fetched from the DIY detector Luftdaten \[2\], that can be hosted anywhere (so other people can grab the code from github \[3\] and use it too). ^c20333368

  Then, people started to requesting new features and I had ideas for new features and it was no longer a single-page project.

  Then, people started to reporting issues with their PHP hosting accounts, so I was spending time debugging problems in their deployments.

  Then, I thought it may be easier to introduce multi-tenancy so I can just support a single environment, the one that I own. So I added registration, dashboard, maps, Let's Encrypt, etc.

  This way I ended up owning a small, open-source SaaS written in PHP7 and MySQL \[4\]. If I knew how my single-page app will grow, I'd choose something more suitable, like Rails or Dropwizard. On the other hand, it works, is usable and maintainable, so maybe it's fine the way it is.

  \[1\] [https://smolna.aqi.eco/](<https://smolna.aqi.eco/>)
  \[2\] [https://luftdaten.info/](<https://luftdaten.info/>)
  \[3\] [https://github.com/trekawek/air-quality-info/](<https://github.com/trekawek/air-quality-info/>)
  \[4\] [https://aqi.eco/](<https://aqi.eco/>)

- **arunarunarun** · [2019-07-02 12:29 UTC](https://news.ycombinator.com/item?id=20334337)
  I recently wrote something similar to pull data from Kaiterra Laser Eggs (also in Haskell!) -- [https://github.com/ford-prefect/laser-egg/](<https://github.com/ford-prefect/laser-egg/>) ^c20334337

- **psandersen** · [2019-07-02 10:13 UTC](https://news.ycombinator.com/item?id=20333694)
  On a related note, I've been looking for a good sensor that is hopefully plug & play and reliable for integration with home assistant. Is something like [https://www.banggood.com/Geekcreit-Nova-PM-Sensor-SDS011-Hig...](<https://www.banggood.com/Geekcreit-Nova-PM-Sensor-SDS011-High-Precision-Laser-PM2_5-Air-Quality-Detection-Sensor-Module-Tester-p-1144246.html?cur_warehouse=CN>) really the best way to go about it rather than an Awair? Would be keen on VOCs and CO2 as well. ^c20333694

  edit: Looks like esphome with the following low-cost sensors is the way to go:
  \* MH-Z19 for co2  (or CCS811 CO\_2 for VOCs as well)
  \* SDS011 for particle counts

  - **jsingleton** · [2019-07-02 11:39 UTC](https://news.ycombinator.com/item?id=20334038)
    This looks like an interesting project: [https://learn.pimoroni.com/tutorial/sandyj/enviro-plus-and-l...](<https://learn.pimoroni.com/tutorial/sandyj/enviro-plus-and-luftdaten-air-quality-station>) ^c20334038

    This sensor also looks good: [https://shop.pimoroni.com/products/adafruit-sgp30-air-qualit...](<https://shop.pimoroni.com/products/adafruit-sgp30-air-quality-sensor-breakout-voc-and-eco2>)

    - **psandersen** · [2019-07-12 07:18 UTC](https://news.ycombinator.com/item?id=20418895)
      Thanks for the link, already ordered the other sensors. Looks like SGP30 isn't quite as easy to use with ESPHome right now, so something to upgrade to within a year. 
      Its really amazing how great the ecosystem is with ESPHome, I was always a bit scared buying the chips and getting really DIY with the likes of Arduino but this is no more difficult than most other tech. ^c20418895

- **maweki** · [2019-07-02 08:20 UTC](https://news.ycombinator.com/item?id=20333213)
  I know it is hard to strike a good balance between academic and technical focus, especially when writing about haskell, but I think starting out with language extensions and imports without writing about what and how we're going to do it, makes for difficult reading. ^c20333213

  The smaller parts with the types and small implementations should be at the top and only at the end all is easily combined.

  And I highly doubt that the author went about writing the chatbot by writing out all the language extensions and imports first (which makes the coding-along line at the and a bit cynical).

  Edit: This sounds so negative. I think the article is good and shows how the small pieces work together but I think the order is all wrong.

  - **moleike** · [2019-07-02 09:06 UTC](https://news.ycombinator.com/item?id=20333406)
    Hi, author here. I agree that straight away throwing a bunch of language extensions without an explanation of why we need them at all wasn't a good idea. The original blog post was written in literate Haskell, that's the reason why the code is organized that way. ^c20333406

    I will think about rearranging the code blocks or add more explanations to make it all fit more naturally. Thanks for your feedback!

    - **maweki** · [2019-07-02 09:21 UTC](https://news.ycombinator.com/item?id=20333460)
      When I teach or write about Haskell I try to break down the parts in a way that the parts can be tested using ghci and just composing it at the end. ^c20333460

      I think there are quite a few parts in there that one can easily "try out on their own".

- **mark\_l\_watson** · [2019-07-02 13:15 UTC](https://news.ycombinator.com/item?id=20334649)
  A good article! I agree with another commenter that explaining the language extensions would have been good. ^c20334649

  I liked the comment at the end:

  \>\> It’s the same bot as we have detailed in the tutorial with the exception that it uses PostGIS instead of a transactional variable to store users.

  I am not a Haskell expert (I use Haskell a lot but I consider myself a student) so this is probably horrible advice, but recently I have started using embedded SQLite for transactional data instead of TVars. In some sense it is the same thing since the Simple SQLite wraps the SQLite code in an IO. I always try to minimize impure code. I write as much pure code as I can in a REPL and then study/research how to handle the impure parts.

- **bayesian\_horse** · [2019-07-02 05:34 UTC](https://news.ycombinator.com/item?id=20332402)
  I hope I never have to move to a place where I want to monitor the air quality at all. ^c20332402

  - **yakshaving\_jgt** · [2019-07-02 11:59 UTC](https://news.ycombinator.com/item?id=20334160)
    With the way things are going, you might not have to — the bad air quality moves to you. ^c20334160

