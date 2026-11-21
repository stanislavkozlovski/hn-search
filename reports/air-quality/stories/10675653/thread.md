# [World air pollution map](https://news.ycombinator.com/item?id=10675653)

Article: [https://air.plumelabs.com/](<https://air.plumelabs.com/>)

gnocchi · 2015-12-04 11:06 UTC · 29 reported comments · archived 2026-11-08 10:39 UTC
Observation: 2026-11-08 10:39 UTC → 2026-11-08 10:39 UTC

## Comments

- **cmsmith** · [2015-12-05 15:31 UTC](https://news.ycombinator.com/item?id=10682136)
  Can we get a scale bar? or legend? and what is being plotted here? and where does the data come from? what's the difference between the contours and the dots? ^c10682136

  Clicking the big dots just takes me to a completely different page that doesn't have that much more information. I'd expect a popup on the map that tells me what the color/size of the dot means.

  - **sdm** · [2015-12-05 17:23 UTC](https://news.ycombinator.com/item?id=10682541)
    Also the lack of differentiation between PM10 and PM2.5 numbers is very unhelpful. What's actually being measured? Just saying PM isn't useful. Plus, the scale only goes to 150 -- LOL, I'm in China, a scale that only goes 150 is useless.  Finally, for the activities, what's the difference between "take care" and "take it easy"? ^c10682541

    - **adventured** · [2015-12-05 21:10 UTC](https://news.ycombinator.com/item?id=10683288)
      The 600 micrograms per cubic meter type readings that have occurred in China or India, don't correlate to this site's scale. ^c10683288

  - **pavement** · [2015-12-05 17:00 UTC](https://news.ycombinator.com/item?id=10682445)
    If you click on the dots, it takes you to a city: ^c10682445

    [https://air.plumelabs.com/Dallas](<https://air.plumelabs.com/Dallas>)

    [https://air.plumelabs.com/London](<https://air.plumelabs.com/London>)

    [https://air.plumelabs.com/Bogota](<https://air.plumelabs.com/Bogota>)

    [https://air.plumelabs.com/Beijing](<https://air.plumelabs.com/Beijing>)

    [https://air.plumelabs.com/New-Delhi](<https://air.plumelabs.com/New-Delhi>)

    [https://plumelabs.files.wordpress.com/2015/12/world-air-map-...](<https://plumelabs.files.wordpress.com/2015/12/world-air-map-live.gif>)

    The unit/metric descibed by each graph seems to be:


    ```
      The Plume Air Quality Index™
    ```

    
    I'm not sure how the index value is determined, but it seems to factor in measured values for Nitrogen Dioxide, Ozone, Carbon Monoxide, and particulate matter (exhaust soot and toxic dust being worse than dust comprised of ambient organic material such as pollen).

  - **deepGem** · [2015-12-05 15:57 UTC](https://news.ycombinator.com/item?id=10682213)
    The data is most likely coming from govt owned sensors. 
    [http://aqicn.org/map/india/](<http://aqicn.org/map/india/>) ^c10682213

  - **jrcii** · [2015-12-05 15:57 UTC](https://news.ycombinator.com/item?id=10682211)
    The dots appear to be city-specific reports. Darker/brown appears to mean more pollution whereas lighter/blue appears to mean less. The size of the dot may mean population size. ^c10682211

    - **lobo\_tuerto** · [2015-12-05 16:14 UTC](https://news.ycombinator.com/item?id=10682279)
      Too bad the color of the dot doesn't always relate to the pollution level it represents. Take for example the one for Mexico City, if you click on it, you will get a different pollution level than what's indicated on the initial map. ^c10682279

  - **intrasight** · [2015-12-05 18:18 UTC](https://news.ycombinator.com/item?id=10682724)
    Agreed. Pretty much a fail as a visualization without that. ^c10682724

  - **smokinjuan** · [2015-12-05 16:57 UTC](https://news.ycombinator.com/item?id=10682431)
    Click on one of the dots to see the legend. ^c10682431

- **adorable** · [2015-12-05 21:54 UTC](https://news.ycombinator.com/item?id=10683403)
  I am David, one of Plume Labs' founders. Thank you for all your feedback! ^c10683403

  At Plume Labs we build tools to help people fend off pollution. This starts with an urban weather report (the Plume Air Report) that tells you when pollution will be high for a few hours or more in your city, and what you can do about it – timing your run, biking, activities with children – to take back control of your environment.

  The map discussed here is a near realtime visualization of air pollution levels worldwide. The colors and the Plume Index are based on WHO recommendations. (Blue corresponds to levels below the W.H.O. yearly recommendations, light blue is below the W.H.O. daily recommendations etc.) The map takes into account the main pollutants (NO2, O3, PM10, PM2.5) and is based on measurements made in 11,000 monitoring stations worldwide along with air quality models for the areas that are not covered by monitoring stations.

  More details as well as pollution predictions are available on the mobile version of the Plume Air Report

  iOS \=\> [https://itunes.apple.com/en/app/plume-air-report-pollution/i...](<https://itunes.apple.com/en/app/plume-air-report-pollution/id950289243?mt=8>)

  Android \=\> [https://play.google.com/store/apps/details?id\=com.plumelabs....](<https://play.google.com/store/apps/details?id=com.plumelabs.air>)

  We try to make the air we breathe more transparent, and we hope you find it useful!

  - **dstyrb** · [2015-12-06 00:48 UTC](https://news.ycombinator.com/item?id=10683897)
    It's a very interesting project and quite attractive. ^c10683897

    However as others mentioned it would be useful to see some sort of scale for the dots, scale for the colors, and specifics on those numbers. For example, I have no idea what "Blue corresponds to levels below the W.H.O. yearly recommendations, light blue is below the W.H.O. daily recommendations etc." means... Does that mean "In one day at a Blue dot you will breathe in a whole year's worth of particulates, while at a light blue dot for one day you will breathe in one day's worth of particulates?"

    As it stands, I will stick with aqicn.org for my Chinese pollution forecast simply because it has much more, more specific, information for me -- including intra-city maps. It would be more useful to me if there was perhaps a radio button where I could change between PM2.5 and NO2 for example.

    It is very cool to see this on a worldwide scale though. And don't US embassies have public air quality data that you can scrape to fill out things like Africa? Or is that just US embassies in China...?

    Anyways, thanks for your efforts.

  - **wodenokoto** · [2015-12-06 12:22 UTC](https://news.ycombinator.com/item?id=10685080)
    You sorely need a legend to go with that map. What are circles (when you click you learn they are cities, but I should be able to know that before I click) what does size of circle mean? What does the color mean? ^c10685080

    There is also something that looks like clouds. What are they? Also pollution? Are they on the same color scale as the circles?

- **aries1980** · [2015-12-05 00:25 UTC](https://news.ycombinator.com/item?id=10680158)
  I cycle from East London to Oxford Street every day, I found Plumelabs' data very strange: the air on the London Oxford street (the most polluted street: [http://www.independent.co.uk/environment/air-pollution-in-lo...](<http://www.independent.co.uk/environment/air-pollution-in-londons-oxford-street-has-already-breached-the-legal-limit-for-the-whole-of-2015-in-9960277.html>)) is better than the Vienna's average, which is considered to one of the cleanest city in Europe ([http://www.euronews.com/2015/03/31/how-does-your-city-rank-i...](<http://www.euronews.com/2015/03/31/how-does-your-city-rank-in-european-air-pollution-survey/>)). My nose tells the opposite. ^c10680158

  - **stinos** · [2015-12-05 14:26 UTC](https://news.ycombinator.com/item?id=10681942)
    Try checking other maps like [http://aqicn.org/map/europe/\#@g/50.9419/4.5137/9z](<http://aqicn.org/map/europe/#@g/50.9419/4.5137/9z>)? Also there was a rather detailed map I saw just a week ago, displaying something like 'average decrease in life expectancy due to combined air pollution' but I cannot find it anymore. It looked really depressing btw. ^c10681942

    - **aries1980** · [2015-12-05 21:53 UTC](https://news.ycombinator.com/item?id=10683402)
      Thanks for the link! ^c10683402

- **farresito** · [2015-12-05 16:30 UTC](https://news.ycombinator.com/item?id=10682335)
  I've always liked this one: [http://aqicn.org/map/europe/](<http://aqicn.org/map/europe/>)
  It's available for all continents. ^c10682335

- **11thEarlOfMar** · [2015-12-05 15:38 UTC](https://news.ycombinator.com/item?id=10682148)
  This article has a *little* information on Plume: ^c10682148

  [http://www.treehugger.com/health/worlds-first-global-real-ti...](<http://www.treehugger.com/health/worlds-first-global-real-time-air-pollution-map-app-launched.html>)

  "The map integrates some half a million data points each day from 11,000 environmental stations across the world,.."

- **aselzer** · [2015-12-05 17:19 UTC](https://news.ycombinator.com/item?id=10682525)
  How is there significantly less particulate matter and therefore less are quality in Cologne and Dortmund, which are located in a very densely populated area with a lot of traffic, than in Vienna? ^c10682525

  [http://aqicn.org/map/europe/](<http://aqicn.org/map/europe/>) tends to only shows areas where PM2.5 is even measured as polluted, so I guess this might be inaccurate due to a lack of sensors in some areas, falsely believing they are less polluted.

  You can easily see this by just looking at the air quality reports in Vienna: [http://aqicn.org/map/europe/\#@g/48.183/16.4118/12z](<http://aqicn.org/map/europe/#@g/48.183/16.4118/12z>)

- **arrayjumper** · [2015-12-05 15:19 UTC](https://news.ycombinator.com/item?id=10682108)
  What is the source for the data? ^c10682108

- **mynegation** · [2015-12-05 16:36 UTC](https://news.ycombinator.com/item?id=10682354)
  I get French language interface when I click Toronto or Ottawa and English one for Montreal, with no visible button for switching. They got it backwards. ^c10682354

- **ljegou** · [2015-12-05 16:44 UTC](https://news.ycombinator.com/item?id=10682383)
  The large circles often mask the little ones. No legend, no symbol scale, no color scale. That's not how you do thematic cartography. ^c10682383

- **analytically** · [2015-12-05 22:36 UTC](https://news.ycombinator.com/item?id=10683530)
  UI sucks. This is how you do it: [http://aqicn.org/city/france/limousin/limoges/aine/](<http://aqicn.org/city/france/limousin/limoges/aine/>) ^c10683530

- **simeondd** · [2015-12-05 14:39 UTC](https://news.ycombinator.com/item?id=10681975)
  Interesting map. Also a good thing that my country Bulgaria isn't there as probably the pollution index will be over 100. ^c10681975

  - **ashray** · [2015-12-05 16:50 UTC](https://news.ycombinator.com/item?id=10682410)
    Is it really that bad in Sofia? I checked it out on aqicn earlier and it looked alright there. ^c10682410

- **techaddict009** · [2015-12-05 15:39 UTC](https://news.ycombinator.com/item?id=10682152)
  How about easy selection of city based on country?
  This map based selection is bit uneasy to use. ^c10682152

  - **techaddict009** · [2015-12-05 15:40 UTC](https://news.ycombinator.com/item?id=10682157)
    Sorry its there below maps which I couldnt find at first. ^c10682157

- **StronglyTyped** · [2015-12-05 15:11 UTC](https://news.ycombinator.com/item?id=10682081)
  Any policy to reduce carbon emissions that does not include Asia is a scam to take your money. ^c10682081

  - **exabrial** · [2015-12-05 21:00 UTC](https://news.ycombinator.com/item?id=10683252)
    This is so true. It's so polluted and smoggy, there's a constant fog about when you walk around that never goes away. India and China are driving the climate change disaster, not the USA. ^c10683252

  - **mikeash** · [2015-12-05 17:48 UTC](https://news.ycombinator.com/item?id=10682625)
    This map has little to do with CO2 emissions. ^c10682625

