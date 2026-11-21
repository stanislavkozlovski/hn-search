# [Realtime California Air Quality](https://news.ycombinator.com/item?id=24254117)

Article: [https://www.purpleair.com/map?opt\=1/i/mAQI/a10/cC4\#7.22/37.494/-120.928](<https://www.purpleair.com/map?opt=1/i/mAQI/a10/cC4#7.22/37.494/-120.928>)

gdi2290 · 2020-08-23 18:33 UTC · 59 reported comments · archived 2026-11-08 11:25 UTC
Observation: 2026-11-08 11:25 UTC → 2026-11-08 11:25 UTC

## Comments

- **ilyagr** · [2020-08-23 20:05 UTC](https://news.ycombinator.com/item?id=24254873)
  I've found [http://www.airnow.gov](<http://www.airnow.gov>) very helpful and faster to load than the Purple Air map. They also have a simple but efficient app. ^c24254873

  Airnow's map is slow to load, but shows smoke, air monitors (including the Purple Air ones\^\[footnote\]), and fires all at once: [https://fire.airnow.gov/?lat\=37.40&lng\=-122.077&zoom\=10\#](<https://fire.airnow.gov/?lat=37.40&lng=-122.077&zoom=10>)

  A less detailed, fast, static map for the SF Bay Area is available at [http://www.baaqmd.gov](<http://www.baaqmd.gov>).

  Last, but not least, there is a forecast of surface-level smoke available at [https://hwp-viz.gsd.esrl.noaa.gov/smoke/](<https://hwp-viz.gsd.esrl.noaa.gov/smoke/>). I found it from [https://twitter.com/NWSBayArea](<https://twitter.com/NWSBayArea>), which is a good source of news for the Bay Area.

  \[footnote\]: To make the numbers match, I had to set PurpleAir to show One-Hour Averages with the LRAPA scoring. See [https://imgur.com/a/d6yFtow](<https://imgur.com/a/d6yFtow>).

  - **rz2k** · [2020-08-23 20:37 UTC](https://news.ycombinator.com/item?id=24255085)
    I hooked up a PM2.5 sensor\[1\] I ordered during wildfires a few years ago, and the EPA's AirNow has been far more consistent with what I'm measuring than Purple Air or IQAir. ^c24255085

    I think the source for that static map is here: [https://gispub.epa.gov/airnow/](<https://gispub.epa.gov/airnow/>), and includes some projections.

    Accuweather and Windy.com have pretty good forecasts, but the ones that have been the most accurate this week for me are the US Forest Service's BlueSky models.

    California (might miss northern smoke)
    \- [https://tools.airfire.org/websky/v2/run/standard/CANSAC-1.33...](<https://tools.airfire.org/websky/v2/run/standard/CANSAC-1.33km/current>)

    CA, OR, ID, NV, UT, AZ
    \- [https://tools.airfire.org/websky/v2/run/standard/CANSAC-4km/...](<https://tools.airfire.org/websky/v2/run/standard/CANSAC-4km/current>)

    \[1\] Plantower PMS7003 are less than \$20 on AliExpress. Here's a quick plot of the data [https://i.imgur.com/FjABgpP.png](<https://i.imgur.com/FjABgpP.png>) including a spike where it was above a grill.

    - **ilyagr** · [2020-08-23 23:27 UTC](https://news.ycombinator.com/item?id=24256178)
      I found the "CANSAC-1.33km" California BlueSky forecast you linked to very helpful, thank you! ^c24256178

  - **krat0sprakhar** · [2020-08-23 20:12 UTC](https://news.ycombinator.com/item?id=24254926)
    Didn't know about airnow.gov - thanks! ^c24254926

    I'm surprised though why the data is so different between airnow and purpleair. On AirNow, SF currently shows unhealthy air (150\~) whereas purpleair shows 88 (moderate). Which one of these is more reliable and real-time?

    - **karlding** · [2020-08-23 20:19 UTC](https://news.ycombinator.com/item?id=24254968)
      Someone posted a Medium article \[0\] on the /r/bayarea subreddit where they did some digging into this. Apparently the sensors used by Purple Air rely on a constant that represents the average density of the particles it detects. Because wood smoke particles are less dense than typical PM 2.5 particles, the resulting AQI values are too high. ^c24254968

      The Lane Regional Air Protection Agency has developed a conversion formula that is built into Purple Air (if you apply the LRAPA conversion factor in the UI), so you can have a better comparison.

      \[0\] [https://medium.com/@16fcali/understanding-purpleair-vs-airno...](<https://medium.com/@16fcali/understanding-purpleair-vs-airnow-gov-measurements-of-wood-smoke-pollution-562923a55226>)

      - **aaroninsf** · [2020-08-24 21:27 UTC](https://news.ycombinator.com/item?id=24265720)
        \^\^\^ this ^c24265720

        That article is well worth a read. I now am using PA in this mode.

    - **tjohns** · [2020-08-23 20:19 UTC](https://news.ycombinator.com/item?id=24254979)
      AirNow uses official EPA sensor sites, which are professionally maintained but fewer in number. These will have the highest quality data. ^c24254979

      That said, the PurpleAir devices use high quality laser particulate sensors, so they're still significantly more accurate than most consumer devices.

      Both are real time, but during a wildfire where smoke is shifting between neighborhoods, I'd go with the PurpleAir site to get a score for your particular neighborhood. Just be sure to turn on the LRAPA scoring model, as others have mentioned.

    - **gnutun** · [2020-08-23 20:16 UTC](https://news.ycombinator.com/item?id=24254953)
      A useful explanation of the differences: [https://medium.com/@16fcali/562923a55226](<https://medium.com/@16fcali/562923a55226>) ^c24254953

    - **tmpz22** · [2020-08-23 20:15 UTC](https://news.ycombinator.com/item?id=24254946)
      Purple air has a mix of indoor sensors, try using the filter to hide indoor sensors and you should see more of a parity between the two. ^c24254946

    - **unsrsly** · [2020-08-23 20:44 UTC](https://news.ycombinator.com/item?id=24255132)
      In addition to what other commenters have said, I'd guess that some purpleair sensors are placed in garages or other places with a local concern for air quality. That may explain some of the local variation you see on purpleair. ^c24255132

    - **ilyagr** · [2020-08-23 20:21 UTC](https://news.ycombinator.com/item?id=24254991)
      I think the main difference is that airnow mainly relies on expensive sensors with government-approved calibration.  There are only a few such sensors per county. ^c24254991

      Airnow's map shows both the government sensors and the Purple Air sensors, but that seems to be a recent "pilot project". I doubt they use the low-cost sensor data anywhere else.

    - **gonehome** · [2020-08-23 20:15 UTC](https://news.ycombinator.com/item?id=24254947)
      I think purple air is better. ^c24254947

      Purple air relies on a bunch of devices people have bought and installed all over. I think airnow is just a handful of government ones?

  - **scurvy** · [2020-08-23 20:34 UTC](https://news.ycombinator.com/item?id=24255070)
    AirNow's data \_can\_ be less accurate. For example, punching in a Lamorinda ZIP code only returns results for Oakland ("Oakland reporting area"), even if the ZIP correctly shows the right locale. ^c24255070

    PurpleAir lets me see my neighbor's air quality stats...two houses away. PurpleAir is much more relevant and accurate for me.

  - **jxramos** · [2020-08-26 18:11 UTC](https://news.ycombinator.com/item?id=24285375)
    The shortcoming of the AirNow data is the sparse sampling. If you search for your city you can see the caveat underneath with something like "AnyTown Reporting Area". When you look at the sensor coverage it's much more sparse than the corresponding PurpleAir sensor coverage. ^c24285375

    There's also the fire map that includes both public and private sensors, the regular interactive map I don't believe uses all the available sensors.
    [https://fire.airnow.gov/](<https://fire.airnow.gov/>)
    \> Notice: The Sensor Data Pilot adds a new layer of air quality data from low-cost sensors.

  - **peterhj** · [2020-08-23 22:12 UTC](https://news.ycombinator.com/item?id=24255732)
    Direct URL to one of the combined AQI maps for the Bay Area: ^c24255732

    [https://files.airnowtech.org/airnow/today/cur\_aqi\_sanfrancis...](<https://files.airnowtech.org/airnow/today/cur_aqi_sanfrancisco_ca.jpg>)

  - **labster** · [2020-08-23 22:14 UTC](https://news.ycombinator.com/item?id=24255750)
    There's doesn't seem to be any way to to get air quality in terms of ozone on PurpleAir, but there is on AirNow. ^c24255750

  - **toomuchtodo** · [2020-08-23 20:09 UTC](https://news.ycombinator.com/item?id=24254900)
    Thank you for sharing this! ^c24254900

    - **unknown** · [2020-08-23 20:12 UTC](https://news.ycombinator.com/item?id=24254922)
      [deleted] ^c24254922

- **modeless** · [2020-08-23 19:43 UTC](https://news.ycombinator.com/item?id=24254680)
  I like PurpleAir's air quality map but felt it was a bit too slow to check frequently. So I used their API to make the fastest air quality site around: [https://aqi.today](<https://aqi.today>) ^c24254680

  - **unknown** · [2020-08-23 20:10 UTC](https://news.ycombinator.com/item?id=24254907)
    [deleted] ^c24254907

- **khuey** · [2020-08-23 19:26 UTC](https://news.ycombinator.com/item?id=24254557)
  For those who don't live here, a series of dry thunderstorms last weekend sparked a number of wildfires that have combined to burn more than 1500 square miles (more than 4000 square kilometers) in less than a week. ^c24254557

  - **RobLach** · [2020-08-23 19:33 UTC](https://news.ycombinator.com/item?id=24254613)
    Unfortunately the same conditions are reappearing which will negatively compound the situation: ^c24254613

    [https://www.chicoer.com/2020/08/23/national-weather-service-...](<https://www.chicoer.com/2020/08/23/national-weather-service-upgrades-fire-weather-watch-to-red-flag-warning-in-parts-of-northern-california/>)

    - **avmich** · [2020-08-23 19:36 UTC](https://news.ycombinator.com/item?id=24254635)
      \> A map of the Red Flag Warning can be found on the US National Weather Service’s Facebook page. ^c24254635

      Anything more available?

      - **tjohns** · [2020-08-23 20:10 UTC](https://news.ycombinator.com/item?id=24254909)
        It's on the top of the NWS Bay Area homepage right now: ^c24254909

        [https://www.weather.gov/mtr/](<https://www.weather.gov/mtr/>)

        Their Twitter feed is also worth subscribing to:

        [https://twitter.com/NWSBayArea](<https://twitter.com/NWSBayArea>)

      - **jeffbee** · [2020-08-23 20:17 UTC](https://news.ycombinator.com/item?id=24254957)
        The map basically shows the entire state of California. Saved you a click. ^c24254957

    - **coronadisaster** · [2020-08-23 19:35 UTC](https://news.ycombinator.com/item?id=24254627)
      at least, those 1500 square miles can't burn again... maybe CA need to do controlled burns like FL does (if they don't already do it).  IE: Burn dry brush in the forests. ^c24254627

      - **kec** · [2020-08-23 19:47 UTC](https://news.ycombinator.com/item?id=24254708)
        I believe California does, but the scale of the problem is completely different compared to a sate like Florida. California has 2.5x as much land as Florida and a significantly higher percentage of the total land is wilderness or otherwise undeveloped. ^c24254708

        - **shaftway** · [2020-08-24 18:18 UTC](https://news.ycombinator.com/item?id=24263644)
          Not just wilderness or undeveloped, but highly inaccessible to firefighting crews. The Bay Area has peaks over 4000 feet with lots of fairly sheer areas. Often firefighters have to be dropped in by helicopter. ^c24263644

          Florida is mostly low rolling hills with the highest point in the state being \~350 feet above sea level. If Florida has a fire in an inaccessible area, it's usually inaccessible due to water, so more of a help to firefighters than a hindrance.

      - **vondur** · [2020-08-23 19:46 UTC](https://news.ycombinator.com/item?id=24254706)
        There's an article about this very subject in Mother Jones:
        [https://www.motherjones.com/environment/2019/11/californias-...](<https://www.motherjones.com/environment/2019/11/californias-wildfire-controlled-prescribed-burns-native-americans/>) ^c24254706

      - **athms** · [2020-08-23 23:34 UTC](https://news.ycombinator.com/item?id=24256219)
        The federal government owns about 45\% of California land. Of the forests, 57\% are owned by the federal government; 39\% are privately owned by individuals, corporations, or land trusts; and the state, county, or local governments control only 2\%. ^c24256219

        Also, most fires start in grassy areas. The Camp Fire that destroyed Paradise started as a grass fire on federal land before it spread to shrubs and burned through mostly private land. California has almost 8 million acres of shrubs.

        The Woosley Fire that burned almost half of Malibu was started on industrial property owned by Boeing and spread through chaparral along the steep Santa Monica Mountains.

      - **squidlogic** · [2020-08-23 19:48 UTC](https://news.ycombinator.com/item?id=24254714)
        As I recall, Bureau of Land Management tried this and there was a lot of backlash from residents. It’s also quite a bit of land to do a controlled burn, so might not be that feasible. ^c24254714

      - **claydavisss** · [2020-08-23 20:29 UTC](https://news.ycombinator.com/item?id=24255040)
        [flagged] ^c24255040

        It may be too late. The high-risk areas are very close to homes (as is evidenced by the destruction of property). A controlled burn near homes will produce high volumes of smoke even if they are controlled. If they are not adequately controlled, you can lose a town.

        Depopulating these areas won't need to happen by edict, insurances premiums will do that. If these trends continue, there will be no one living in the quaint gentleman-farmer communities in wine country within twenty years.

        I predict the sierras will be the next danger zone - as more people move to the Tahoe area, all of the mistakes of sprawl will be repeated.

  - **casefields** · [2020-08-23 19:37 UTC](https://news.ycombinator.com/item?id=24254642)
    Here's a great map: [https://pbs.twimg.com/media/EgHuZ8XUcAEii18?format\=png&name\=...](<https://pbs.twimg.com/media/EgHuZ8XUcAEii18?format=png&name=900x900>) ^c24254642

    - **dylan604** · [2020-08-23 20:08 UTC](https://news.ycombinator.com/item?id=24254894)
      I found this interactive map compelling: [https://nifc.maps.arcgis.com/apps/View/index.html?appid\=69fc...](<https://nifc.maps.arcgis.com/apps/View/index.html?appid=69fca73a82df4fefa7c0e48b66d0899d&extent=-123.2395,36.6849,-119.5618,38.1032>) ^c24254894

      - **guerrilla** · [2020-08-23 21:52 UTC](https://news.ycombinator.com/item?id=24255583)
        There's these two using satellite data as well \[1\]\[2\]. Live webcams for a bonus \[3\]. ^c24255583

        \[1\]. [https://firemap.sdsc.edu/](<https://firemap.sdsc.edu/>)

        \[2\]. [https://mappingsupport.com/p2/gissurfer.php?basemap\=USA\_base...](<https://mappingsupport.com/p2/gissurfer.php?basemap=USA_basemap&overlay=VIIRS_24_hours,MODIS_24_hours,ESRI_roads_and_labels&txtfile=https://mappingsupport.com/p2/special_maps/disaster/USA_wildland_fire.txt>)

        \[3\]. [http://www.alertwildfire.org/northbay/index.html?camera\=Axis...](<http://www.alertwildfire.org/northbay/index.html?camera=Axis-StHelenaSouth&v=518dd6b>)

  - **coding123** · [2020-08-23 19:54 UTC](https://news.ycombinator.com/item?id=24254772)
    For those that DO live here, a number of somewhat similar thunderstorms are in the forecast for the exact same days as last week (Sunday - Tuesday). ^c24254772

- **supernova87a** · [2020-08-23 21:31 UTC](https://news.ycombinator.com/item?id=24255445)
  Maybe someone can share/explain -- ^c24255445

  Purple Air *sells* you a sensor that you can install, and then takes the data, displays it on their website for lots of people to view, and then presumably makes money off the data you send them?   Why should you have to pay for the sensor then?

  - **suzakus** · [2020-08-23 22:45 UTC](https://news.ycombinator.com/item?id=24255929)
    You don't have to make it public. I bought a sensor from them and marked it private, so it doesn't appear on the map. ^c24255929

    From installation guide:

    [https://www2.purpleair.com/pages/install](<https://www2.purpleair.com/pages/install>)

    If you set your sensor to private, you may view it by logging in to the PurpleAir map using a Gmail address that matches the "Owner's Email" in the registration form. Alternatively, you can use the link provided in the registration confirmation email. You may share this link with family and friends.

  - **IvyMike** · [2020-08-23 23:34 UTC](https://news.ycombinator.com/item?id=24256223)
    Here's a NYT article on the origins of Purple Air. ^c24256223

    [https://www.nytimes.com/2018/11/30/style/air-quality-polluti...](<https://www.nytimes.com/2018/11/30/style/air-quality-pollution-monitors.html>)

    I have a Purple Air sensor; I view the money I spent on it as helping to sponsor a "citizen science" project. Could the nature of the project change in the future, to where I feel like I was taken advantage of?  Sure, I guess.  But I'm ok taking that risk.

    - **supernova87a** · [2020-08-24 03:39 UTC](https://news.ycombinator.com/item?id=24257352)
      I see.  Ok, well at least it's not some tech app service trying to charge on the front end and make money off the back too. ^c24257352

  - **bittercynic** · [2020-08-23 21:48 UTC](https://news.ycombinator.com/item?id=24255549)
    Personally, I probably wouldn't, but if you wanted to know about the air quality at your home this would be one way to do it. ^c24255549

- **gdi2290** · [2020-08-23 18:50 UTC](https://news.ycombinator.com/item?id=24254279)
  also see how bad the fires are from Santa Cruz
  [https://twitter.com/robwormald/status/1296709260429029378](<https://twitter.com/robwormald/status/1296709260429029378>) ^c24254279

- **ahaucnx** · [2020-08-24 05:13 UTC](https://news.ycombinator.com/item?id=24257683)
  We are a new startup (currently doing Startup School) to provide air quality monitoring solutions especially for schools. ^c24257683

  From the beginning it was important for us to give back to the community so we setup AirGradient for Education providing free tutorials and advise.

  We just published our open source and open hardware air quality sensor measuring PM2.5, CO2, Temperature and Humdity. So you can build your own sensor with a small display to measure the air quality in and around your home. We call it the AirGradient DIY sensor.

  Build instructions, Code and Hardware files can be found on our project page:
  [https://www.airgradient.com/diy/](<https://www.airgradient.com/diy/>)

  It would be great to hear feedback from you!

  PS: We are also looking for schools that are interested in improving air quality to learn more about their needs and possible solutions. Please PM me for more information.

- **Zhenya** · [2020-08-23 21:41 UTC](https://news.ycombinator.com/item?id=24255503)
  Submitted a quick instruction on how to make an air purifier. ^c24255503

  Link: [https://news.ycombinator.com/item?id\=24251509](<https://news.ycombinator.com/item?id=24251509>)

  Copy/pasta to help folks:

  Note: this is not my idea, but I have used it for 2 Cal fire seasons successfully.

  1) Acquire a box fan

  2) Acquire a large "FPR 10" rated filter from home depot

  3) Duct tape filter to the out flow side of the box fan. Make sure the arrows on the filter point in the correct airflow direction.

  This works dramatically well for very little dollars and can help save your lungs if air purifiers are not available or expensive.

  - **ilyagr** · [2020-08-24 03:13 UTC](https://news.ycombinator.com/item?id=24257252)
    How loud is it? ^c24257252

    - **Zhenya** · [2020-08-24 03:47 UTC](https://news.ycombinator.com/item?id=24257384)
      Not loud at all. Just a background hum. However, I'm sure it's a function of the box fan motor. I have a cheap one and it's perfectly fine to sleep in the same room. ^c24257384

- **Fauntleroy** · [2020-08-23 19:29 UTC](https://news.ycombinator.com/item?id=24254576)
  It's useful to see the pollution numbers on the sensors, but it's also just as interesting to see which sensors have been destroyed and for how long. You can track the fire just by seeing when sensors go offline, if you know where to look. ^c24254576

  - **anamexis** · [2020-08-23 19:33 UTC](https://news.ycombinator.com/item?id=24254615)
    Not necessarily destroyed, but at least without power. ^c24254615

- **oski** · [2020-08-23 19:42 UTC](https://news.ycombinator.com/item?id=24254670)
  Make sure to use the “LRAPA” conversion on purpleair.com ^c24254670

  [https://twitter.com/rengiec/status/1296486310123905024?s\=20](<https://twitter.com/rengiec/status/1296486310123905024?s=20>)

- **dang** · [2020-08-23 19:49 UTC](https://news.ycombinator.com/item?id=24254728)
  See also: a thread from 2018: [https://news.ycombinator.com/item?id\=18714777](<https://news.ycombinator.com/item?id=18714777>) ^c24254728

- **Animats** · [2020-08-24 05:31 UTC](https://news.ycombinator.com/item?id=24257766)
  Site down: ^c24257766


  ```
      Over Quota
      This application is temporarily over its serving quota.
      Please try again later.
  ```

- **ericand** · [2020-08-23 19:44 UTC](https://news.ycombinator.com/item?id=24254690)
  What's with indoor sensors being default on? Is there some value to then that I don't understand? ^c24254690

  - **stbtrax** · [2020-08-23 19:49 UTC](https://news.ycombinator.com/item?id=24254734)
    This is very frustrating. Agreed, they should turn them off by default. ^c24254734

    - **mjrpes** · [2020-08-23 23:18 UTC](https://news.ycombinator.com/item?id=24256117)
      I sent their team an email two years ago with exactly that feedback, and their response was: ^c24256117

      "Thank you for the feedback. We are working on an update that will 'save' your preferred map view when logged in on the PurpleAir website. However, it is not published yet."

      See my post above how I am able to bookmark the site after I choose the settings I want and it remember these choices when I visit again.

  - **mjrpes** · [2020-08-23 23:14 UTC](https://news.ycombinator.com/item?id=24256098)
    If you bookmark the website after you have zoomed in on your area and toggled settings (unchecked indoor sensors, LRAPA), it will remember your settings. ^c24256098

  - **wmichelin** · [2020-08-23 19:48 UTC](https://news.ycombinator.com/item?id=24254721)
    Seriously. My partners school was saying they will open this week (on top of COVID, of all things) if the AQI is not in the red. The sensor they're using is indoor. This website is actively doing harm with these configurations, granted, so is the school administration. ^c24254721

    COVID is bringing out the worst in all parts of our society. It has been such a stressful time, and I am someone who has some financial security. I can't imagine how tough things are on the average American right now.

    Stay strong everybody. We will make it out of this.

- **tempsy** · [2020-08-23 20:24 UTC](https://news.ycombinator.com/item?id=24255003)
  this year is like a sad joke. if covid didn’t kill San Francisco these fires will be the breaking point. it has become that for me. ^c24255003

  - **scurvy** · [2020-08-23 20:51 UTC](https://news.ycombinator.com/item?id=24255185)
    What about the fires last year? Or two years ago? Those were worse for SF proper. It looked like Mars or the end of days 2 years ago. ^c24255185

    - **novok** · [2020-08-23 21:44 UTC](https://news.ycombinator.com/item?id=24255527)
      No covid...  Can't meet people inside or outside now, plus an economy that is close to starving people.   Most places are 3 meals away from a revolution. ^c24255527

- **archarios** · [2020-08-23 20:05 UTC](https://news.ycombinator.com/item?id=24254859)
  It seems like they're out of indoor sensors by the way I ordered one and they printed a shipping label then canceled it. ^c24254859

- **snoshy** · [2020-08-23 19:36 UTC](https://news.ycombinator.com/item?id=24254637)
  What is the source for this data? ^c24254637

  - **unknown** · [2020-08-23 20:08 UTC](https://news.ycombinator.com/item?id=24254896)
    [deleted] ^c24254896

  - **stbtrax** · [2020-08-23 19:49 UTC](https://news.ycombinator.com/item?id=24254738)
    They have devices that you can buy and install. Check out their website ^c24254738

