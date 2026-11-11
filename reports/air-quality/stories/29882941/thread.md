# [Windy.com: See the wind, temperature, rain and air quality around you](https://news.ycombinator.com/item?id=29882941)

Article: [https://www.windy.com](<https://www.windy.com>)

LinuxBender · 2022-01-10 21:34 UTC · 35 reported comments · archived 2026-11-08 11:55 UTC
Observation: 2026-11-08 11:55 UTC → 2026-11-08 11:55 UTC

## Comments

- **fshbbdssbbgdd** · [2022-01-11 00:48 UTC](https://news.ycombinator.com/item?id=29885508)
  I feel like this app gives the illusion of higher-fidelity data than it can really provide. It gives a temperature reading for any pixel I select, but appears to be interpolating from a relatively limited number of real-world data points. ^c29885508

  I live in the flatlands near some mountains. I can look at one of the websites that show data from personal weather stations to see that the temperature is 15 degrees cooler up on the mountains. But windy shows the temp there being the same as here. I figure it’s just averaging the various locations around (but not on) the mountains. Better data exists, but they don’t seem to have it.

  - **nkurz** · [2022-01-11 02:42 UTC](https://news.ycombinator.com/item?id=29886669)
    \> It gives a temperature reading for any pixel I select, but appears to be interpolating from a relatively limited number of real-world data points. ^c29886669

    I think you are misinterpreting what Windy is showing.  It's not trying to show the current temperature at the selected location, it's showing the current forecast for the temperature at that location according to a particular model.  On the lower right, you can choose from different forecast models, and the "temperature" at the location you select will probably change.   If you choose a finer grained model than the default (there are different third party models available for different locales) you might find one that does a better job of dealing with mountains.  And on the lower left, you can change the "time" slider to show the forecast for the next few days according to the chosen model.

    So yes, there is interpolation happening, but it's interpolation from a model that is already based on an artificial grid, and not based on interpolating from the actual temperatures as recorded on the ground.  What I find useful about Windy is the ability to compare the output of different weather models, and thus get a idea of the uncertainty of the forecast.  To access this, choose a location, and then click "Compare" on the bottom bar.  If all 5 models available to me agree, it's probably a good guess.  If one of them is radically different, one should be slightly skeptical.  If they all disagree, probably best to assume that the forecast is inherently unpredictable.

  - **cconcepts** · [2022-01-11 01:10 UTC](https://news.ycombinator.com/item?id=29885715)
    I agree, was recently using it in a remote area for reasonably important decision making. The high level of detail fooled me into thinking it had a high level of accuracy. ^c29885715

    Turns out being very specifically wrong is more convincing than just being generally wrong.

    EDIT: I should add that windy may be the best forecasting app there is. I was more commenting on the fact that the specificity made me follow it blindly when I should have been treating it like any other forecast.

  - **deepsun** · [2022-01-11 15:50 UTC](https://news.ycombinator.com/item?id=29892920)
    The truth is, all the weather in the world is interpolated. Most people don't know that new \_forecasts\_ are usually made only twice a day (at 00:00Z and 12:00Z) (more frequent \_forecast updates\_ are actually just changing times in forecasted ranges). ^c29892920

    That's why pilots don't like Windy actually. We prefer to read source readings and forecasts and guess-interpolate manually, no need in extra layer of complexity.

    E.g. if I want to check visibility at my small airport, where no weather forecasts are made, I check a few larger airports around, and also learn today's "big picture" weather state (fronts? inversions?), to estimate what should I expect at my local airport.

    It's like debugging a website software having raw DB data vs. screenshot.

  - **rhodysurf** · [2022-01-11 01:25 UTC](https://news.ycombinator.com/item?id=29885862)
    I work in this field and this is exactly true ^c29885862

    - **LeoPanthera** · [2022-01-11 02:11 UTC](https://news.ycombinator.com/item?id=29886352)
      Can you elaborate? ^c29886352

- **kingsloi** · [2022-01-10 23:28 UTC](https://news.ycombinator.com/item?id=29884595)
  I’m working on something like Windy.com for my local community in Gary, IN at [https://millerbeach.community](<https://millerbeach.community>) but with more emphasis on the air quality. I’ve just deployed an AQMesh pod to track NO, NO2, SO2, CO, and soon H2S that I’ll be adding to the dashboard soon. I’m just storing the wind bearing right now, but would love to track local pressure/wind patterns like Windy does! ^c29884595

  - **vosper** · [2022-01-10 23:44 UTC](https://news.ycombinator.com/item?id=29884809)
    Could you talk more about the air quality system you deployed? I'd love to see air quality data being more available and visible. ^c29884809

    - **kingsloi** · [2022-01-11 00:13 UTC](https://news.ycombinator.com/item?id=29885141)
      Sure! Here’s website for the AQMesh sensor I just deployed [https://www.aqmesh.com/products/aqmesh/](<https://www.aqmesh.com/products/aqmesh/>) probably explain it better than I could! ^c29885141

      It has PM1, 2.5, 4, and 10  sensors, and CO, NO, NO2, SO2, and soon to be H2S (which will replace CO or SO2 as there’s a specific configuration/limit) electrochemical sensors.

      There is no noise sensor in this one, but I do plan on measuring the noise too.

      I’d like people to report when they experience bad air quality, and eventually have enough data to say under these specific conditions, people report X, and then use that data to notify people.

      I plan on deploying more pods in Gary, lil grass roots project!

      - **plumeria** · [2022-01-11 01:59 UTC](https://news.ycombinator.com/item?id=29886235)
        Would this sensor help in measuring pollution from an abattoir (measure the stench from burning of residues and also from oxidation lagoons)? ^c29886235

        Edit: Also, how much does the AQMesh sensor cost?

        - **kingsloi** · [2022-01-11 02:30 UTC](https://news.ycombinator.com/item?id=29886558)
          I never associated an abattoir to air pollution (the more you know) but just doing some quick googling, it looks like this sensor would help exactly in measuring pollution from an abattoir! ^c29886558

          [https://www.sciencedirect.com/science/article/pii/S240584402...](<https://www.sciencedirect.com/science/article/pii/S2405844020312093>)

          \> All the HQ values exceeded the threshold value, set at the unity, implying that H2S, SO2 and NH3 are likely to cause adverse health effects in the area. Conclusively, continuous operation of this abattoir within the residential area can constitute a great environmental menace to the residents of the area and can result in complication to those with existing health challenge.

          RE cost: I'm currently on a 3 month rental through [https://ambilabs.com](<https://ambilabs.com>), but plan on renting longer, and possibly purchase down the line. I think purchase price is somewhere around \$10,000+ with a \$1000/yr fee. I got a special deal, but it's a few thousand dollars for a few months, definitely not cheap, but grade A service so far!

          - **plumeria** · [2022-01-11 02:39 UTC](https://news.ycombinator.com/item?id=29886642)
            Thanks for the information! This seems like something my community should look into. ^c29886642

  - **aardvark179** · [2022-01-11 00:03 UTC](https://news.ycombinator.com/item?id=29885034)
    Maybe I’m misunderstanding what you’re doing, but it sounds like you’re running a weather station, whereas windy and other sites are combining the data from many weather stations and running forecasting algorithms based on it. ^c29885034

    - **nkurz** · [2022-01-11 03:08 UTC](https://news.ycombinator.com/item?id=29886903)
      \> whereas windy and other sites are combining the data from many weather stations and running forecasting algorithms based on it ^c29886903

      There may be other sites that are doing this, but I don't think Windy creates any forecasts on its own.  Instead, it provides a nice graphical interface to show forecasts that have been made by others.  In my US location, they offer the choice of ECMWF 9km (European Centre for Medium-Range Forecasts), GFS 22km (Basic free model provided by NOAA), NAM 5km (Regional mesoscale model run by NCEP), ICON 13km (German DWD), and Meteoblue (Swiss from the University of Basel).

      - **a\_square\_peg** · [2022-01-11 08:48 UTC](https://news.ycombinator.com/item?id=29889091)
        This is correct - Windy explicitly says that they don't do any forecasting on their own and they don't have any meteorologists on staff. The usefulness and the quality of apps such as Windy is really a testament to how good the public (and free) weather forecast models are. ^c29889091

    - **kingsloi** · [2022-01-11 00:59 UTC](https://news.ycombinator.com/item?id=29885612)
      I'm not running a weather station, I'm running air quality sensors and an AIS antenna. I pull traffic, trains, aircraft, weather, and lake advisories from some public/private APIs and combine all the data. I want to track air pollutants on a local level, and see how traffic, industry, and weather play a role in the air quality here, and I'd love to be able to forecast it ^c29885612

  - **notatoad** · [2022-01-11 00:18 UTC](https://news.ycombinator.com/item?id=29885198)
    for general air quality there's also IQAir - it was really helpful during the wildfire smoke this summer ^c29885198

    [https://www.iqair.com/ca/air-quality-map?lat\=41.59337&lng\=-8...](<https://www.iqair.com/ca/air-quality-map?lat=41.59337&lng=-87.34643&zoomLevel=10&placeId=5bc822d541fdcdf1939e7587>)

- **merricksb** · [2022-01-11 03:09 UTC](https://news.ycombinator.com/item?id=29886917)
  Major discussion 4 months ago: ^c29886917

  [https://news.ycombinator.com/item?id\=28486389](<https://news.ycombinator.com/item?id=28486389>) (1052 points/215 comments)

  Also:

  4 years ago: [https://news.ycombinator.com/item?id\=15094639](<https://news.ycombinator.com/item?id=15094639>) (580 points/Aug 24, 2017/103 comments)

- **cozzyd** · [2022-01-11 02:34 UTC](https://news.ycombinator.com/item?id=29886593)
  We used Windy to predict when we were likely to have north winds at Summit Station in Greenland. During north winds we weren't allowed to do certain activities (e.g. ride snomos) in order to reduce emissions at the NOAA air monitoring lab. Hilariously, when the NOAA weather station at Summit went down, the predictions got noticeably worse, which makes total sense.  ECMWF seemed to have the best predictions of the available models. ^c29886593

  What's great is that despite the complexity of the presentation, the data itself is a simple image (jpg, strangely?) and everything is just animated in javascript, so other than the scripts (which are cached), it doesn't download a huge amount of data.

- **prawn** · [2022-01-10 23:54 UTC](https://news.ycombinator.com/item?id=29884927)
  I work with a team shooting tourism content outside (often along the coast) and we use the Windy app all the time to pick times for each location. Being able to swipe to see the weather for a particular location at a future time is very helpful. Helps decide "OK, we'll shoot Wreck Beach first while the wind is light and offshore, then by 3pm when we've moved to the Point, the direction will have changed but we'll be protected by the headland." ^c29884927

  We also use long-range agricultural rain forecasts to try to schedule larger trips for decent weather windows, but this is obviously a lot riskier!

- **mbesto** · [2022-01-10 23:55 UTC](https://news.ycombinator.com/item?id=29884934)
  And if you're a sailor (or any other wind sports) there's WindyApp...not that that's confusing or anything: ^c29884934

  [https://windy.app/](<https://windy.app/>)

- **gpestana** · [2022-01-11 00:25 UTC](https://news.ycombinator.com/item?id=29885262)
  I do paragliding and this app is part of my every day toolbox to prepare the flights and decide where to fly. The forecasting is pretty accurate, specially if there's a weather station close to the area I'm checking the wind intensity and direction. Great app, can't recommend enough! ^c29885262

- **tyronehed** · [2022-01-10 23:01 UTC](https://news.ycombinator.com/item?id=29884227)
  Then, there's this lovely place: [https://earth.nullschool.net/\#current/wind/surface/level/ort...](<https://earth.nullschool.net/#current/wind/surface/level/orthographic=-83.56,26.01,1366>) ^c29884227

  - **unknown** · [2022-01-10 23:36 UTC](https://news.ycombinator.com/item?id=29884683)
    [deleted] ^c29884683

- **a\_square\_peg** · [2022-01-10 23:34 UTC](https://news.ycombinator.com/item?id=29884663)
  This seems to be posted on a fairly regular basis every few months. ^c29884663

  - **livinglist** · [2022-01-10 23:36 UTC](https://news.ycombinator.com/item?id=29884694)
    well.. there are many urls that got posted repeatedly tbh ^c29884694

- **adzm** · [2022-01-10 23:52 UTC](https://news.ycombinator.com/item?id=29884897)
  The app is really nice too with a lot of different features and layers. Between this, NOAA Weather, and RadarScope I feel like my weather needs are fulfilled on my Android device. ^c29884897

- **lqueenan** · [2022-01-10 23:57 UTC](https://news.ycombinator.com/item?id=29884966)
  For sailing, I prefer PredictWind for the mountainous coast and inlets of Vancouver BC. The NAM and HRRR models give most accurate results here. ^c29884966

- **wyclif** · [2022-01-11 02:14 UTC](https://news.ycombinator.com/item?id=29886382)
  I switched to Windy from Ventusky and I'm liking the way they present the data. ^c29886382

- **rajishx** · [2022-01-14 12:26 UTC](https://news.ycombinator.com/item?id=29933632)
  For cycling i am big fan of mywindsock.com ^c29933632

- **mongol** · [2022-01-10 23:11 UTC](https://news.ycombinator.com/item?id=29884379)
  It looks pretty but I don't find it particularily useful. ^c29884379

- **samspenc** · [2022-01-10 22:50 UTC](https://news.ycombinator.com/item?id=29884059)
  JFYI for anyone interested in this space: I believe VentuSky - www.ventusky.com - is the most popular website in this space and has comprehensive & free weather information from around the world. I use it on a weekly basis after I first heard about it a few years ago. ^c29884059

  Looking at the website now, it includes temperature, precipitation, radar, satellite, clouds, wind speed, air pressure, thunderstorm, humidity, waves, snow cover and air quality. As well as past 3 days and predictions for upcoming 3-4 days.

  - **ageofwant** · [2022-01-11 00:53 UTC](https://news.ycombinator.com/item?id=29885559)
    Windy is known and used by every sailor, kiter and windsurfer I know. Never heard of VentuSky... ^c29885559

  - **darkteflon** · [2022-01-10 23:17 UTC](https://news.ycombinator.com/item?id=29884463)
    When you say “this space”, do you mean weather apps generally? Or is there something that Windy / VentuSky do that sets them apart from any other weather app? It’s not clear to me from looking at these what the advantage is but maybe I’m not the target. ^c29884463

  - **et-al** · [2022-01-10 23:22 UTC](https://news.ycombinator.com/item?id=29884529)
    Maybe I'm missing some nuance here, but VentuSky seems like a copy of Windy (or maybe vice versa, but I've heard about Windy ever since it was windytv). ^c29884529

    Seems like there's also [https://earth.nullschool.net](<https://earth.nullschool.net>), but it's not as fully featured.

  - **tiagod** · [2022-01-10 23:33 UTC](https://news.ycombinator.com/item?id=29884659)
    It's slower than Windy on my browser, and doesn't have ECMWF and AROME models. ^c29884659

