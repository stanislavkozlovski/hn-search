# [China builds ‘world’s biggest air purifier’ and it seems to be working](https://news.ycombinator.com/item?id=16156942)

Article: [https://www.scmp.com/news/china/society/article/2128355/china-builds-worlds-biggest-air-purifier-and-it-seems-be-working](<https://www.scmp.com/news/china/society/article/2128355/china-builds-worlds-biggest-air-purifier-and-it-seems-be-working>)

cesis · 2018-01-16 09:49 UTC · 77 reported comments · archived 2026-11-08 10:47 UTC
Observation: 2026-11-08 10:47 UTC → 2026-11-08 10:47 UTC

## Comments

- **jhugg** · [2018-01-16 14:22 UTC](https://news.ycombinator.com/item?id=16158325)
  So... to drop the PM2.5 amount by 15\%, this tower must be removing many many tons of particulate matter every day. How is it removed from the filters they speak of? How expensive is that to do? I have some questions about the practicality. ^c16158325

  On the other hand, I wonder if anyone's ever built a 100m placebo before. It could be a *really* interesting university study on the placebo effect in disguise.

  - **LeifCarrotson** · [2018-01-16 15:49 UTC](https://news.ycombinator.com/item?id=16159005)
    \> many many tons of particulate matter every day ^c16159005

    Let's do the math.

    Guidelines state that the limit on PM2.5 particulates is approximately 10 micrograms per cubic meter for an annual average.  Xian, where the tower was installed, is currently ([http://aqicn.org/city/xian/](<http://aqicn.org/city/xian/>)) under 231 ug/m\^3 of pollution. The tower is supposed to process 10 million cubic meters of air per day.


    ```
        10^7 m^3 x 231 x 10^-6 g/m^3 x 10^-3 g/kg x 0.15 = 231 x 0.15 x 10^-2 =>
    ```

    
    0\.34 kg of particulate contamination removed per day.  Not many tons.  But someone check my math, please - that seems impossibly low, unless combustion is cleaner and generates lower quantities of PM2.5 particulates than I'm imagining.  I did assume that it only removes PM2.5 contaminants, ignoring larger dust particles and PM10 pollution.

    Let's also check the amount of air it should be processing.  It's about 100 meters tall, and intended to cover 10 square kilometers.  We'll conservatively assume that this volume represents the total quantity of air it needs to process.  Ihe volume is:


    ```
       10 km^2 x 10^3 m/km x 10^3 m/km x 10 ^ 2 m = 10^8 m^3
    ```

    
    or 100 million cubic meters, so it's intended to process one tenth of that volume per day.

    The math still seems low. Micrograms per cubic meter are hard to intuit.

    - **kragen** · [2018-01-16 17:32 UTC](https://news.ycombinator.com/item?id=16160023)
      0\.35 kg of particulate contamination removed per day; you rounded incorrectly, but the rest of your math is right. ^c16160023

      There's the issue that it's probably removing nearly all of the particulates from the air it actually processes, say over 90\%, which works out to 2.1 kg.  It doesn't reduce the PM2.5 level in the area by 90\%, but only by 15\%, because it's only able to process some 16\% of the air in its area during whatever the relevant time interval is, which seems like a good match to your 10\%-per-day.

      However, you got the volume of that area wrong: it's 10⁹ m³, not 10⁸ m³.  That suggests that the natural lifetime of PM2.5 particulates is closer to a week than a day.

      As for jhugg's question about how the filters are cleaned, a common way to remove particulates from flue gas or indoor spaces is using electrostatic precipitators, which are flat plates at a high voltage.  The voltage sticks the particulates to the plates, and when the coating is thick enough, you close the valves to stop the gas flow and vibrate the plates to unstick the dust, and it falls out the bottom of the filter into a bucket (or, say, a truck).  Other systems clean the plates with water (either spray or immersion) and possibly soap or lye.

      - **LeifCarrotson** · [2018-01-16 19:44 UTC](https://news.ycombinator.com/item?id=16161582)
        Thanks for verifying my result and catching my mistake. 
        You're right, it's a volume of 10 x 10⁸ cubic meters, which is 10⁹. ^c16161582

        That's what I get for interweaving a mantissa of 10 with scientific notation! Too late to edit now, but people should see this comment thread.

      - **nullbyte** · [2018-01-16 18:38 UTC](https://news.ycombinator.com/item?id=16160772)
        I love HN comment like this. Seems like there's an expert in everything here! ^c16160772

        - **kragen** · [2018-01-23 00:48 UTC](https://news.ycombinator.com/item?id=16209766)
          I am not an expert in air pollution control systems, or even an amateur.  I don't even have an air filter installed in my house.  I read some Wikipedia articles over the last couple of years, Googled, and watched some videos on YouTube (including "how-to" videos on the care and feeding of electronic air cleaners.)  That doesn't make me an expert.  That makes me some sort of approximation of a journalist — and if you've ever read those people writing about something you know about, you know how much they get wrong. ^c16209766

      - **AstralStorm** · [2018-01-17 09:24 UTC](https://news.ycombinator.com/item?id=16166606)
        Considering how a lot of China electricity is generated by coal plants, electroscrubbing the filters might not be the best way. ^c16166606

        Three are alternative chemical processes to clean up such filters.

    - **OskarS** · [2018-01-16 16:48 UTC](https://news.ycombinator.com/item?id=16159548)
      Using your numbers, I get the same thing: [http://www.wolframalpha.com/input/?i\=(10,000,000+m3)+\*+(0.15...](<http://www.wolframalpha.com/input/?i=%2810,000,000+m3%29+*+%280.15+*+231+micrograms%2Fm%5E3%29>) ^c16159548

      The microgram is a very small unit :) I mean, a gram is already pretty dinky, a millionth of it is even tinier! The whole point of these particles is that they're miniscule and can pass through tissue other particles can't, so maybe it's not so surprising that it's not a massive amount when you pile them up.

    - **jhugg** · [2018-01-16 16:58 UTC](https://news.ycombinator.com/item?id=16159682)
      That's really interesting. Maybe the pm2.5 is less visible than the PM10, but maybe I'm just way way off. ^c16159682

      As for the volume of air, I'm most curious where the 15\% measurement was taken and how consistent it was. How far from the tower? How many different places were measured? How many days are in the sample? What's the P-Value?

      But still, thanks. Makes this interesting to think about.

      - **OskarS** · [2018-01-16 17:05 UTC](https://news.ycombinator.com/item?id=16159750)
        I think PM10 rates are in similar orders of magnitude, in the "micrograms per cubic meter" range, so i don't think it would be that different. Maybe an order of magnitude larger, but not much more. ^c16159750

        I agree, this is very surprising. Before I saw LeifCarrotson's calculation, I would have thought "tons" was the right unit as well. There's so much polluted air, you'd think that it would add up to some significant amount of matter, but apparently not.

        - **jhugg** · [2018-01-16 18:03 UTC](https://news.ycombinator.com/item?id=16160360)
          Well, 10km\^2 is pretty tiny in a country the size of China, and I'm not sure how high up the pollution goes (higher than buildings but lower than planes). ^c16160360

          So it's still a lot of pollution, just much less actual mass than I would have guessed.

        - **staplers** · [2018-01-16 17:27 UTC](https://news.ycombinator.com/item?id=16159974)
          Puts into perspective how much PM burning coal puts into the atmosphere.. ^c16159974

          EDIT: In 2016, the United States burned roughly 728 million tons of coal, enough to fill a typical railroad car every 4 seconds

  - **lawlessone** · [2018-01-16 14:43 UTC](https://news.ycombinator.com/item?id=16158482)
    \>I wonder if anyone's ever built a 100m placebo before. It could be a really interesting university study on the placebo effect in disguise. ^c16158482

    See the protests that erupt over mobile(Cell) phone towers. People claiming towers that weren't even on made them sick etc.

    [https://idle.slashdot.org/story/10/01/15/1516245/tower-switc...](<https://idle.slashdot.org/story/10/01/15/1516245/tower-switch-off-embarrasses-electrosensitives>)

- **gressquel** · [2018-01-16 14:36 UTC](https://news.ycombinator.com/item?id=16158431)
  Please refrain from using AMP links.
  We need to take a stance against Googles abuse of monopoly. ^c16158431

  - **captainmuon** · [2018-01-16 15:37 UTC](https://news.ycombinator.com/item?id=16158890)
    Devil's advocate: Google is generous by caching AMP sites on their own servers. The only thing you can't do is to include your own invasive third party tracking (ok, you can use Google's of course), which is bad anyway. But you can still include your ad just as a \<img\> in the page, no JS and tracking. Like a dumb print ad. I don't really have a problem with that. ^c16158890

    - **Hello71** · [2018-01-16 15:40 UTC](https://news.ycombinator.com/item?id=16158924)
      "Google is generous by storing your email on their own servers." ^c16158924

      "Facebook is generous by storing your posts and friend lists on their own servers."

      - **send\_computers** · [2018-01-16 16:04 UTC](https://news.ycombinator.com/item?id=16159137)
        I agree ^c16159137

        - **acct1771** · [2018-01-16 18:39 UTC](https://news.ycombinator.com/item?id=16160788)
          With the nonsensical sarcastic point? Or the real point? ^c16160788

    - **moron4hire** · [2018-01-16 17:18 UTC](https://news.ycombinator.com/item?id=16159891)
      There is no such thing as a generous corporation. It goes completely against maximizing shareholder value. Google gets something out of AMP, something they can quantify monetarily. ^c16159891

      - **chrismcb** · [2018-01-20 05:54 UTC](https://news.ycombinator.com/item?id=16192283)
        You do know that a corporation does not maximize shareholder value, nor is that their purpose.
        A company can do something generous.
        Sometimes something that helps the customer also helps the company. ^c16192283

  - **pcx** · [2018-01-16 15:02 UTC](https://news.ycombinator.com/item?id=16158628)
    Isn't AMP open source? How is it bad, and an abuse by Google? ^c16158628

    - **gressquel** · [2018-01-16 15:34 UTC](https://news.ycombinator.com/item?id=16158860)
      AMP is all fine, but most of the newspapers are lured to implement it by Google with promise of higher page rank on its search results. It all ends up in a walled garden and when the publishers are reliant on it, Google will control the chain of supply. Disgusting behaviour. Just waiting for more people to lobby in EU so they get another fine. ^c16158860

    - **Something1234** · [2018-01-16 15:05 UTC](https://news.ycombinator.com/item?id=16158647)
      I believe that it routes them into a proprietary cache by google. Taking page views from the provider or at least that is my understanding of it. ^c16158647

      - **fenwick67** · [2018-01-16 21:39 UTC](https://news.ycombinator.com/item?id=16162932)
        I can't speak for everyone, but my objection to the AMP cache is that it's just another way for Google to collect your browsing data. ^c16162932

- **makethetick** · [2018-01-16 13:48 UTC](https://news.ycombinator.com/item?id=16158086)
  More readable non-mobile link: [http://www.scmp.com/news/china/society/article/2128355/china...](<http://www.scmp.com/news/china/society/article/2128355/china-builds-worlds-biggest-air-purifier-and-it-seems-be-working>) ^c16158086

- **SurrealSoul** · [2018-01-16 13:39 UTC](https://news.ycombinator.com/item?id=16158036)
  I wish there was more than anecdotal evidence for this. China has very strong statistics for their pollution levels that are often recorded in their weather reports. ^c16158036

  For a project this big, they should be able to quantify the results instead of just relying on what people say about the air :/

  EDIT: I'm a dummy, although the article leaves with an anecdotal, there are some nuggets of stats "The average reduction in PM2.5 – the fine particles in smog deemed most harmful to health – fell 15 per cent during heavy pollution."  & "Cao said the results were preliminary because the experiment is still ongoing. The team plans to release more detailed data in March with a full scientific assessment of the facility’s overall performance."

  - **amelius** · [2018-01-16 16:38 UTC](https://news.ycombinator.com/item?id=16159452)
    \> I wish there was more than anecdotal evidence for this. ^c16159452

    Perhaps this will help:

    [http://www.esa.int/Our\_Activities/Observing\_the\_Earth/Copern...](<http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Sentinel-5P/Sentinel-5P_brings_air_pollution_into_focus>)

- **radarsat1** · [2018-01-16 13:21 UTC](https://news.ycombinator.com/item?id=16157929)
  I really like how simple this solution is.  Just using the sun to heat up air and have it go up through a bunch of filters, no moving parts.  It strikes me as the right way to go about it.  I wonder if you could use the greenhouses for growing plants, and the rising air to run small turbines.. ^c16157929

  - **IanDrake** · [2018-01-16 14:56 UTC](https://news.ycombinator.com/item?id=16158583)
    As far as running turbines go... ^c16158583

    [https://en.m.wikipedia.org/wiki/Solar\_updraft\_tower](<https://en.m.wikipedia.org/wiki/Solar_updraft_tower>)

- **xkcd-sucks** · [2018-01-16 17:28 UTC](https://news.ycombinator.com/item?id=16159992)
  Such a mainland solution... The air's dirty, install an air filter. There's lots of air and it's really dirty? Build a bigger air filter! ^c16159992

  ...especially if my uncle manufactures air filter membranes and needs to get rid of some extra inventory

- **quadcore** · [2018-01-16 14:07 UTC](https://news.ycombinator.com/item?id=16158209)
  Side node: is China doing ok in terms of innovation? If yes, how come in such a regime? I would expect everything to be stuck in bureaucracy. ^c16158209

  - **mtw** · [2018-01-16 15:03 UTC](https://news.ycombinator.com/item?id=16158634)
    The government is communist but in terms of business, it's more capitalistic than many western countries. People are also hard-working and very ambitious, and there is wild innovation in places like Shenzen (hardware) or Beijing (AI). Although innovation sometimes simply means copying/stealing. There are ingenuous innovation though. ^c16158634

    - **jeffbax** · [2018-01-16 19:07 UTC](https://news.ycombinator.com/item?id=16161146)
      There's a lot of market dynamism in China, but businesses don't generally do much without a permission slip -- at least once they reach a certain size. Business in China is very tied to government… so capitalistic, but generally of the crony variety ^c16161146

  - **eksemplar** · [2018-01-16 15:34 UTC](https://news.ycombinator.com/item?id=16158863)
    The bureaucracy typically help business when it works. It’s not meant to be directed by day-to-day driven politicians or exposed to lobbyism. It’s supposed to be a safety net to make sure society keeps on track as it speeds along. ^c16158863

    That’s what it is in China, with the added benefit of it actually supporting their local and hindering foreign businesses.

    In a lot of areas it’s us in the west who are stuck behind a hopelessly inefficient bureaucracy, but on the upside, you’re less likely to drop through a poorly constructed escalator or have your local lake filled with industrial waste (well, unless you’re American I guess).

    - **seanmcdirmid** · [2018-01-16 15:38 UTC](https://news.ycombinator.com/item?id=16158896)
      Our local lakes are still pretty clean, Trump hasn’t dismantled the EPA (yet). Western bureaucracy differs from Chinese bureaucracy in that it is more deterministic, the rules are more obvious and more fairly enforced. In China, there is a huge difference based on your guanxi level. I wouldn’t trade our system for theirs. ^c16158896

      - **justicezyx** · [2018-01-16 17:23 UTC](https://news.ycombinator.com/item?id=16159932)
        According to Trump, Hillary escaped jail time because "Guanxi", or whatever equivalent things to guanxi. ^c16159932

        - **seanmcdirmid** · [2018-01-16 18:53 UTC](https://news.ycombinator.com/item?id=16160968)
          Ya, Trump also said Obama was born in Kenya and that he’d release his tax returns eventually. ^c16160968

  - **seanmcdirmid** · [2018-01-16 14:30 UTC](https://news.ycombinator.com/item?id=16158379)
    China is authoritarian on political issues but extremely laissez faire on almost everything else, which is how they grew their economy so quickly but also got into this pollution mess in the first place. There is a bureaucracy for sure, but you can often ignore it if you are prepared to ask for forgiveness rather than permission (or they eventually crackdown). ^c16158379

  - **stelonix** · [2018-01-16 15:01 UTC](https://news.ycombinator.com/item?id=16158613)
    If anything, it goes to show representative democracy plus unrestrained capitalism is not the only way to run a modern, advanced civilization. ^c16158613

    - **briandear** · [2018-01-16 17:49 UTC](https://news.ycombinator.com/item?id=16160207)
      China a "modern, advanced civilization?" You've clearly never lived in China. China is all about the façade. And a MODERN, advanced civilization wouldn't be polluting their entire country like it was a tannery in 1758. ^c16160207

      Taihu lake, near Suzhou, is practically radioactive. Fish in pretty much any freshwater within the entire country is toxic. I lived in China for 3 years or so and as soon as my son was born, we got the hell out -- it's a fun place, but no "modern, advanced" civilization operates like China. It's a country of mostly uneducated, superstitious peasants who suddenly got a lot of money and are kept in line with the threat of "re-education" or death. Even an artist has to fear for his life. [http://aiweiwei.com](<http://aiweiwei.com>)

      Then there's Lui Xiaobo.

      Remember, this "modern, advanced" civilization still has Traditional Chinese Medicine as a "thing." It's a complete fraud with zero scientific basis: [https://sciencebasedmedicine.org/retconning-traditional-chin...](<https://sciencebasedmedicine.org/retconning-traditional-chinese-medicine/>)

      This "modern, advanced" civilization is responsible for massive worldwide poaching to satisfy demand for quack TCM remedies: [https://www.forbes.com/sites/jamesconca/2014/08/08/extinctio...](<https://www.forbes.com/sites/jamesconca/2014/08/08/extinction-by-traditional-chinese-medicine-an-environmental-disaster/#c42db405bd31>)

      Really, powdered rhino horn? That's has the chemical composition of human fingernails -- and works just as "effectively."

      They still do "postpartum confinement" [http://edition.cnn.com/2015/08/11/china/chinese-postpartum-c...](<http://edition.cnn.com/2015/08/11/china/chinese-postpartum-confinement/index.html>) \-- based on pretty much nothing but old wives tales and dangerous superstition.

      Then there's the atrocious human rights record: [https://www.hrw.org/world-report/2017/country-chapters/china...](<https://www.hrw.org/world-report/2017/country-chapters/china-and-tibet>)

      I actually like China -- but the CCP isn't running a "modern, advanced civilization." They're the Beverly Hillbillies.

      - **com2kid** · [2018-01-16 19:19 UTC](https://news.ycombinator.com/item?id=16161308)
        \> They still do "postpartum confinement" [http://edition.cnn.com/2015/08/11/china/chinese-postpartum-c...](<http://edition.cnn.com/2015/08/11/china/chinese-postpartum-c..>). -- based on pretty much nothing but old wives tales and dangerous superstition. ^c16161308

        And a short time ago Americans were electro-shocking homosexuals to try and make them straight.

        \> Remember, this "modern, advanced" civilization still has Traditional Chinese Medicine as a "thing." It's a complete fraud with zero scientific basis: [https://sciencebasedmedicine.org/retconning-traditional-chin...](<https://sciencebasedmedicine.org/retconning-traditional-chin..>).

        America has chiropractors covered under insurance, people who believe in homeopathy, and a growing culture of vaccine denial.

        No culture is perfect. Not too long ago we had horribly polluted waters, and in a lot of places we still do. Have you seen the impact of pollution from pig farms\[0\]\[1\]?

        I'm not trying to play what-about-ism here, I am just saying that "modern, advanced civilizations" do all the things you listed.

        The Chinese government is capable of undertaking massive infrastructure projects, and they do an incredible job of picking industries for government protectionism, allowing for growth of local talent. Multiple areas of technology and  advanced automation are both areas where China has invested heavily in education and building a huge local talent pool. Pulling off multi-decade economic growth plans is impressive, they plotted a path from basic industry all the way to an advanced technology sector, and then executed on that plan.

        That more than qualifies them as an advanced modern society.

        \[0\][http://observer.com/2017/05/pig-waste-factory-farming-north-...](<http://observer.com/2017/05/pig-waste-factory-farming-north-carolina/>)
        \[1\][http://www.businessinsider.com/mishka-henners-photos-of-amer...](<http://www.businessinsider.com/mishka-henners-photos-of-american-feedlots-2014-8>)

    - **quadcore** · [2018-01-16 17:02 UTC](https://news.ycombinator.com/item?id=16159722)
      Already you're jumping to conclusions :D ^c16159722

  - **bluGill** · [2018-01-16 16:18 UTC](https://news.ycombinator.com/item?id=16159263)
    When a bureaucracy decides to do something they do it well. This usually means high level leaders tell everybody that X is a priority so they do X - at the expense of all the other things (both important and unimportant) that they are looking after. ^c16159263

  - **zxcvvcxz** · [2018-01-16 14:58 UTC](https://news.ycombinator.com/item?id=16158601)
    \>If yes, how come in such a regime? I would expect everything to be stuck in bureaucracy. ^c16158601

    Haha you're funny... It's us in the West stuck with bureaucracy. China's growth is unprecedented, with a labor force that's becoming more educated and has always been very hungry for work (no beer or foosball needed). We're finally starting to see engineers and scientists trained here going back after they graduate. For a startup, China potentially has all the following advantages:

    \- Lower operating costs
    \- Less regulations 
    \- Bigger market

    Those are pretty huge.

    Of course there's the big authoritarian elephant in the room, but in practice this is less detrimental to most startups than one would think.

    - **briandear** · [2018-01-16 17:55 UTC](https://news.ycombinator.com/item?id=16160257)
      Less regulations? LOL. ^c16160257

      [https://www.lexology.com/library/detail.aspx?g\=137e018c-80cb...](<https://www.lexology.com/library/detail.aspx?g=137e018c-80cb-4f16-ac38-64bd616615e9>)

    - **quadcore** · [2018-01-16 16:19 UTC](https://news.ycombinator.com/item?id=16159265)
      Can you become a billionaire there and not get all your money taxed? ^c16159265

  - **sangnoir** · [2018-01-16 22:15 UTC](https://news.ycombinator.com/item?id=16163235)
    \> Side node: is China doing ok in terms of innovation? ^c16163235

    Despite that the HN consensus saying otherwise - I'll say yes, China is innovating just fine. Just a few days back, I got downvoted for stating that DJI was forcing competitors to exit the drone market by out-innovating them.

    \> If yes, how come in such a regime?

    Perhaps because innovation and governance model aren't as coupled as some would assume/like?

  - **JamesBarney** · [2018-01-16 18:05 UTC](https://news.ycombinator.com/item?id=16160404)
    They are doing ok, but remember it's a country of a billion people and the second biggest economy in the world.  So they are not nearly as innovative as they could be. ^c16160404

  - **Robotbeat** · [2018-01-16 23:23 UTC](https://news.ycombinator.com/item?id=16163864)
    Perhaps by having 5 times the population of the US, they can accomplish quite a lot even if the authoritarianism hinders innovation. ^c16163864

    More brains, more dreams, more ideas.

- **ChuckMcM** · [2018-01-16 17:22 UTC](https://news.ycombinator.com/item?id=16159923)
  Seems like a reasonable way to pump air through a filter. It will be interesting to see long term effects and maintenance costs (eventually the filters need to be replaced as efficiency would go down with increased air resistance in the tower). ^c16159923

  This FastCompany article from 2013 ([https://www.fastcompany.com/2682151/5-imaginative-buildings-...](<https://www.fastcompany.com/2682151/5-imaginative-buildings-that-breathe-pollution-and-clean-the-air>)) had some additional concepts that could be added.

- **Kayou** · [2018-01-16 14:09 UTC](https://news.ycombinator.com/item?id=16158227)
  \>Xian can experience heavy pollution in winter, with much of the city’s heating relying on coal. ^c16158227

  Have they tried to filter directly the air at the source of pollution? For instance, placing filters on the coal heating facilities. It should be more efficient, as you wouldn't release as many particles in the air in the first place.

  - **seanmcdirmid** · [2018-01-16 14:35 UTC](https://news.ycombinator.com/item?id=16158418)
    Filtering at the source reduces efficiency and has overhead in capital costs, so most people ignore it, even at big power plants and factories (otherwise they get creamed by their competitors who are ignoring it). China’s pollution problem is basically a rule of law problem, and it is difficult to fix it barring external solutions (this) or inevitable blanket restrictions (the banning of coal completely this year in and around Beijing). ^c16158418

  - **chapium** · [2018-01-16 14:12 UTC](https://news.ycombinator.com/item?id=16158250)
    Article mentions coal based heating being a big culprit, which is most likely used residentially in homes and small businesses. ^c16158250

    - **Kayou** · [2018-01-16 14:38 UTC](https://news.ycombinator.com/item?id=16158455)
      I thought it was a central source of coal heating, but if it's in every home, it's probably too difficult to filter then. ^c16158455

      - **seanmcdirmid** · [2018-01-16 14:44 UTC](https://news.ycombinator.com/item?id=16158487)
        In city heating is typically central, in then countryside it is by home. When I visited Tianjin in 1999, however, the apartment I was staying at had a coal furnace. ^c16158487

- **alex\_duf** · [2018-01-16 13:16 UTC](https://news.ycombinator.com/item?id=16157899)
  Edit: as pointed bellow it's using filters. Sorry didn't see that ^c16157899

  If I understand correctly this "air purifier" is just shooting polluted air up, bringing cleaner air from above.

  That sounds like a very short term solution, but it's interesting

  - **radarsat1** · [2018-01-16 13:22 UTC](https://news.ycombinator.com/item?id=16157934)
    "The hot air then rises through the tower and passes through multiple layers of cleaning filters." ^c16157934

- **whoiskevin** · [2018-01-16 13:53 UTC](https://news.ycombinator.com/item?id=16158126)
  I couldn’t help but think of the book “The Water Knife”.  In the book it is the the Chinese that build massive liveable spaces that recycle the water and purify the air. Just a small step in that direction. ^c16158126

  - **jefurii** · [2018-01-16 17:56 UTC](https://news.ycombinator.com/item?id=16160271)
    Or the Two Rivers solar updraft tower in Suarez' "Freedom TM". ^c16160271

- **jostmey** · [2018-01-16 15:56 UTC](https://news.ycombinator.com/item?id=16159066)
  I don't see Humanity becoming less destructive on the environment, so this represents our future. It would be nice if an outside source could verify its effectiveness ^c16159066

  - **anon151516888** · [2018-01-16 16:53 UTC](https://news.ycombinator.com/item?id=16159628)
    It'll be much better when/if the third world poor countries enact similar pollution policies as the Western developed world has. Have faith. ^c16159628

    - **jcbrand** · [2018-01-16 18:01 UTC](https://news.ycombinator.com/item?id=16160345)
      The "Western developed" world uses more energy per capita than most developed countries (the gulf states being an exception), with the US having one of the highest energy consumption per capita ratings. ^c16160345

      [https://en.wikipedia.org/wiki/List\_of\_countries\_by\_energy\_co...](<https://en.wikipedia.org/wiki/List_of_countries_by_energy_consumption_per_capita>)

- **\_salmon** · [2018-01-16 15:07 UTC](https://news.ycombinator.com/item?id=16158657)
  Has it not been completely built? The article features a few pictures of it under construction and then an artist's impression of how it would look. ^c16158657

  - **SurrealSoul** · [2018-01-16 15:12 UTC](https://news.ycombinator.com/item?id=16158691)
    They are building several towers, the project should be completed in march ^c16158691

- **darethas** · [2018-01-16 15:29 UTC](https://news.ycombinator.com/item?id=16158824)
  This may sound like a naive question, but how does this compare to say, trees? ^c16158824

  - **seanmcdirmid** · [2018-01-16 15:34 UTC](https://news.ycombinator.com/item?id=16158862)
    Trees don’t do much for PM2.5. They are a reasonable solution for dust storms, which do generate lots of (but not all) PM10. ^c16158862

    - **darethas** · [2018-01-16 16:49 UTC](https://news.ycombinator.com/item?id=16159561)
      Follow up, can you define much here? I am just interested in this, I read this paper as a primer to my own question, and it seems that with proper city and road planning combined with the effect trees have locally on the air quality it seems we could have noticeable improvement, especially during the leafy seasons. ^c16159561

      [https://www.sciencedirect.com/science/article/pii/S135223101...](<https://www.sciencedirect.com/science/article/pii/S1352231016307336>)

      - **seanmcdirmid** · [2018-01-16 16:52 UTC](https://news.ycombinator.com/item?id=16159611)
        Trees can help with carbon, but we are talking about small particles here. I guess they could trap them or something, but not on the scale of a typical polluted day in say Beijing. Anyways, in northern china, this wouldn’t be very workable as the pollution season corresponds to leafless tree season (and the trees turn a dreary brownish grey due to dust). ^c16159611

        - **darethas** · [2018-01-16 18:48 UTC](https://news.ycombinator.com/item?id=16160902)
          Correct my understanding here where I am wrong - In my mind, if a leaf of a tree or any vegetation photosynthesizes, it is pulling in air (dirty air by your account which is why those leaves are brown) By the very virtue of that fact, it would be pulling in those small particles as well. The paper I referenced states that this happens to an extent, which is why trees during the leafy season are more effective at reducing PM2.5 than when they are bare. ^c16160902

          - **seanmcdirmid** · [2018-01-16 19:19 UTC](https://news.ycombinator.com/item?id=16161312)
            You are probably right, but a better solution would be to create breeze ways that would allow wind to blow out the pollution more easily. These could be coupled with forests, of course. These cities have plenty of trees, but they aren’t newrly enough and anyways winter is the worst season. ^c16161312

- **reacharavindh** · [2018-01-16 13:23 UTC](https://news.ycombinator.com/item?id=16157945)
  I wish there was some technical background of what such a "purification tower" does.
  If they found a genuinely innovative way of purifying air and dumping the toxins and by products sensibly, that is mazing for all of us kudos to them! 
  However, if they tried to push the problem away by shooting polluted air away and sucking in fresher air, then it sucks. ^c16157945

  - **Knufen** · [2018-01-16 13:25 UTC](https://news.ycombinator.com/item?id=16157952)
    It says in the article that ^c16157952

    \>"The hot air then rises through the tower and passes through multiple layers of cleaning filters."

    Meaning you just have to clean the filters

    - **ocardoso** · [2018-01-16 15:42 UTC](https://news.ycombinator.com/item?id=16158933)
      I think we should find a better way to heat ourselves without burning coal, because this air purifier will reach a limit in the future and we will be back on step one. ^c16158933

      - **tqkxzugoaupvwqr** · [2018-01-16 16:14 UTC](https://news.ycombinator.com/item?id=16159216)
        To reduce air pollution the Chinese government forbad heating with coal in some regions and installed gas pipes there. It turned out they severely underestimated the spike in demand in winter and the rising gas prices. Residents illegally switched back to coal heating because heating with gas was 2-3x more expensive. Later, the government officially sanctioned coal heating for the time being. So the Chinese government tries to get away from coal but it’s not as easy. ^c16159216

    - **Overtonwindow** · [2018-01-16 17:46 UTC](https://news.ycombinator.com/item?id=16160178)
      Those filters must be epic in size. ^c16160178

    - **elnurmen** · [2018-01-16 15:31 UTC](https://news.ycombinator.com/item?id=16158836)
      maybe they can just shower them with water? ^c16158836

- **golem14** · [2018-01-16 17:35 UTC](https://news.ycombinator.com/item?id=16160044)
  Maybe also an attempt to test solar updraft power generation ? ^c16160044

