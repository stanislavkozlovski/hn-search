# [Build an Air Quality Monitor with InfluxDB, Grafana and Docker on a Raspberry Pi](https://news.ycombinator.com/item?id=19506983)

Article: [https://www.balena.io/blog/build-an-environment-and-air-quality-monitor-with-raspberry-pi/](<https://www.balena.io/blog/build-an-environment-and-air-quality-monitor-with-raspberry-pi/>)

alexandros · 2019-03-27 22:46 UTC · 67 reported comments · archived 2026-11-08 11:00 UTC
Observation: 2026-11-08 10:59 UTC → 2026-11-08 11:00 UTC

## Comments

- **betimsl** · [2019-03-28 10:07 UTC](https://news.ycombinator.com/item?id=19510751)
  Measuring a sensor is so complicated...Influx, Grafana and Docker is not enough. You may want to throw in AWS, some Google API and not to forget: Tensorflow. A pinch of opencv with GPU support might make it *real* software. Cross compile all this for windows that runs on RPi so corporate clients can trust it -- because buying a license always reflects seriousness. ^c19510751

  - **scrollaway** · [2019-03-28 12:13 UTC](https://news.ycombinator.com/item?id=19511378)
    What is this, off-brand sarcasm? ^c19511378

    \> *Measuring a sensor is so complicated*

    Well, you need something to ingest & query the data. InfluxDB or Prometheus is a good choice.

    You need something compatible to display it. Grafana is perfect for that.

    Docker is a pretty simple and decently-lightweight choice to standardize how this installs and runs.

    And letting it run on a Pi makes it cheap and accessible.

    What exactly is the problem with this setup? Not enough NIH?

    - **moosingin3space** · [2019-03-28 22:55 UTC](https://news.ycombinator.com/item?id=19517477)
      Also, one very nice benefit this has is that balenaOS has safe, automatic updating of the base system. ^c19517477

  - **crispyambulance** · [2019-03-28 13:00 UTC](https://news.ycombinator.com/item?id=19511726) ^c19511726

    ```
        > Measuring a sensor is so complicated...
    ```

    
    I get the sarcasm, but sometimes it is useful to exercise "big boy" tools for projects that don't need it.

    What better way is there to learn/explore these things than with a very simple project that does something remotely interesting or useful?

    - **tarsinge** · [2019-03-28 18:56 UTC](https://news.ycombinator.com/item?id=19515344)
      I think on the contrary we need to seriously reconsider these tools that don't make sense at the scale of the vast majority of projects. It's sad we've gone full circle to the 00's, didn't miss those Java EE days of real big boy tools. ^c19515344

      Edit: current real-life example: I am currently developing a core tool for helping business users of a big industrial group. Client is amazed I was able to quickly develop a custom tool to answer their business needs. Code repo: 3 files: one HTML page, one vanilla JS file (less than a thousand lines), one lib to open XLSX files in JS.

      - **crispyambulance** · [2019-03-29 11:02 UTC](https://news.ycombinator.com/item?id=19520560)
        Yeah, I remember the bad old days. The most spectacular P.O.S. from those days, for me, was SOAP. It makes me clench just thinking about it and it's wildly ironic name "SIMPLE object access protocol." What, like there are even more complicated protocols to transfer data? FML! ^c19520560

        That said, sometimes you need/want to pick up some skills. I think it's good to do these on tractable problems that one can imagine scaling up smoothly, like this one. It's better than overly simple "hello world" and also better than trying to learn from a project where the technology is appropriately scaled and it would take weeks just to figure out what's going on.

    - **MisterTea** · [2019-03-28 13:40 UTC](https://news.ycombinator.com/item?id=19512057)
      \> "big boy" tools ^c19512057

      I read that as "big boy stools".

  - **mschaef** · [2019-03-28 12:30 UTC](https://news.ycombinator.com/item?id=19511504)
    I've built one of these types of systems without a lot of that technology stack. I have my own dashboard, use in-process HSQLDB for the back end, and have a deployment process build around uberjars, shell scripts, and init scripts. ^c19511504

    [https://github.com/mschaef/metlog](<https://github.com/mschaef/metlog>)

    There are reasons I made the choices I did, and I think they still make sense, but there's been enough of various sorts of implementation pain that I am absolutely sympathetic to the idea that this person used some off the shelf software.

    You should probably be more aware of your target's constraints and goals before you start questioning the means they used to achieve them.

  - **nakkaya** · [2019-03-28 18:38 UTC](https://news.ycombinator.com/item?id=19515188)
    At work one of the projects I work on is the telemetry system for a solar race car. I have pretty much the exact setup. We grab the data from the CAN bus transmit it over the radio to the chase vehicle. Data needs to be logged so you can create/test algorithms for predicting optimum speed for the car and also run the algorithms during the race. We don't use PI but a headless linux box will receive all data. During the race both the electrical and mechanical teams needs to see this data. Grafana pools the DB and everyone with a PC, Smart phone or tablet has access to the telemetry. Computers break if the server on the chase vehicle (centos box) breaks I will have reasonable confidance that I can run the telemetry system on my laptop (ubuntu box) with a couple of docker commands. So on top of OP I have a pinch of Clojure, Matlab, Postgres. ^c19515188

  - **rlonn** · [2019-03-28 15:47 UTC](https://news.ycombinator.com/item?id=19513339)
    If you don't feel like setting up and maintaining your own data storage &  visualisation solution for your time series data, you could use adafruit.io or blynk.io. And if you're really lazy or impatient you can try my ridiculously-low-friction service pushdata.io :) ^c19513339

  - **Ysx** · [2019-03-28 10:47 UTC](https://news.ycombinator.com/item?id=19510936)
    I'd have solved it same way as the article, as they're tools I'm familiar with - feels like overkill though. How would you have managed it? ^c19510936

    - **mschaef** · [2019-03-28 12:41 UTC](https://news.ycombinator.com/item?id=19511575)
      Not OP, but here's how I did solve it: ^c19511575

      [https://github.com/mschaef/metlog](<https://github.com/mschaef/metlog>)

      This was mainly an exploratory thing to learn some new technologies, but the gist is that it's a Clojure/Clojurescript application with HSQLDB on the back end. It runs reliably and has for years, but the more 'roll your own' experience means continually finding out that there's some other bit of missing functionality you either need to implement or live without.

      A couple specific observations on various elements of the tech stack:

      \* HSQLDB - Nice little database, well documented, and has served its purpose well. Just now getting to the point where query lengths on long running time series are a performance issue. I think my mitigation strategy will be to do more in memory.

      \* core.async - I use this in the front end to manage sourcing data from the server and getting it into the graphing components. Three or four different approaches later, I'm still not sure I fully get how or why this should be used.

      \* Reagent - Definitely the right choice. About the perfect level of abstraction. Wish I'd spent a bit more time reading the docs ahead of time, though.

      \* Clojure - This has been a great choice, but to be honest, there's not much code on the server side, so it's not at all heavily used.

      \* ClojureScript - Also a good choice (Figwheelr helps), but it's fundamentally a different language with different core data structures sitting in a land that's solidly entrenched in JavaScript. That impedence mismatch is a continual low grade annoyance.

      \* HTML Canvas - Easy to use, but lots of tricky little edge cases to worry about. (The latest being how to find a way to get non-blurry pixel accurate display on a Retina laptop.)

      - **dmix** · [2019-03-28 15:38 UTC](https://news.ycombinator.com/item?id=19513246)
        So you'd design your own UI + graphs? ^c19513246

        - **mschaef** · [2019-03-28 16:06 UTC](https://news.ycombinator.com/item?id=19513549)
          I did. It's simple, but intentionally so - essentially just a linear list of stripcharts and some basic formatting. ^c19513549

          The general idea was that in steady-state operation, the only thing that should really be seen is the data of interest.

          Honestly, the thing that's been the most time-consuming is getting data transported efficiently and quickly to the front end for rendering. The rendering itself hasn't been a huge deal, and is essentially the one part of the system where I haven't thought seriously about replacing it with something 'real'.

          (The stripchart plot code itself is here, and I haven't touched it in three years. [https://github.com/mschaef/metlog/blob/master/metlog-vault/s...](<https://github.com/mschaef/metlog/blob/master/metlog-vault/src-client/metlog_client/tsplot.cljs>) )

    - **IanSanders** · [2019-03-28 12:18 UTC](https://news.ycombinator.com/item?id=19511417)
      Arduino nano, a few sensors, display, and a few buttons ^c19511417

- **zensavona** · [2019-03-28 09:25 UTC](https://news.ycombinator.com/item?id=19510567)
  Probably want to add a PM (particulate matter) sensor to the mix. ^c19510567

  I've built a few similar devices using ESP chips and various laser dust sensors, highly recommend the Plantower PMS5003 - laser defraction, PM1-PM10 accuracy, \~\$20 and there are good libraries available on GitHub for interacting with it.

  Edit: [https://twitter.com/zensavona/status/1091949965306257409](<https://twitter.com/zensavona/status/1091949965306257409>)

  - **luma** · [2019-03-28 11:15 UTC](https://news.ycombinator.com/item?id=19511038)
    I'm using a very similar stack!  I've built 20 devices using the PMS5003, Spec Sensors O3 digital gas sensor, and a cheap GPS module connected to an ESP32.  6 have been mounted in the field (more coming soon!).  They report sensor readings via LoRaWAN to a public-facing dashboard visible here: [https://graqm.org](<https://graqm.org>) ^c19511038

    Devices being tested at an EPA air quality monitoring station: [https://imgur.com/a/joQvj](<https://imgur.com/a/joQvj>)

    Desktop version: [https://imgur.com/a/yT1IK](<https://imgur.com/a/yT1IK>)

- **Animats** · [2019-03-28 07:47 UTC](https://news.ycombinator.com/item?id=19510162)
  What's impressive is that you can get a sensor for temperature, air pressure, "air quality", and humidity for \$12.80 in quantity 1. "Air quality" is strange. It measures volatile organic components, not CO, CO2, or particulates. Sensors for those cost much more. So this is measuring what's easy to measure, not what's useful for, say, HVAC control. ^c19510162

  8GB and Docker, plus a "cloud" server, seems a bit much.

  - **TeMPOraL** · [2019-03-28 11:38 UTC](https://news.ycombinator.com/item?id=19511161)
    How accurate are these, anyway? ^c19511161

    I run a Luftdaten module myself (with SDS011 particulate sensor), but with no government meteorological station next to me, I don't really have a reference point. All I can say is that this SDS011 spews out some numbers, and when testing indoors those numbers got higher when I turned on my air humidifier. I have a similar concern about DHT11/DHT22 - it's a random small box I got mail-ordered from China, which purports to tell the temperature and humidity of air. But again, those are two arbitrary numbers I don't have anything to calibrate again.

    Just using these sensors and trusting the results is an accepted practice in DIY electronics community. But I keep wondering - are those sensors actually calibrated, or it's that people don't really care if they get garbage results?

    (Related, it's also my number one complaint against a particular air quality startup in my country. They rent out air sensors which you can't inspect (there are contractual penalties involved), and they happily market their map as a vital tool for air quality, but nobody really knows what sensors they're using, and they don't even bother to put error bars on the values they show. I mean, I thought including measurement error is how adults behave.)

    - **tpxl** · [2019-03-29 10:40 UTC](https://news.ycombinator.com/item?id=19520456)
      If you establish a baseline you can still figure out when things get worse from the baseline (for some definition of worse) ^c19520456

  - **TheSpiceIsLife** · [2019-03-28 08:15 UTC](https://news.ycombinator.com/item?id=19510287)
    Assuming I have no idea about these things, which is true—I don’t—how much is a decent CO2 sensor that can be connected to a Pi or similar setup? ^c19510287

    I recently upgraded to double glazed windows in half the house, including all the bedrooms, and put a heat pump in each of the two used bedrooms. So I want to keep the windows closed for heat retention, but also want to keep them slightly open to reduce CO2 build up.

    I sleep in my small bedroom with my two 16kg dogs, so it seems reason the CO2 level may rise to suboptimal during the night if the window is shut.

    What I would like to do is make a DIY ventilation system that can move fresh, HEPA filtered, air from outside, in to the room.

    Or am I over complicating things? Could I just use a small fan, something sized to replace, say, half the volume of the room every few hours, and just leave it constantly on? Or should I put a larger fan on a timer so it runs for a few minutes every hour?

    Does any of this really matter?

    Edit to add: any good resources to lose myself down a rabbit hole?

    - **joshvm** · [2019-03-28 09:32 UTC](https://news.ycombinator.com/item?id=19510598)
      A good CO2 sensor that uses infrared absorption to measure concentration costs about \$100. ^c19510598

      [https://www.co2meter.com/collections/co2-sensors](<https://www.co2meter.com/collections/co2-sensors>)

      - **TheSpiceIsLife** · [2019-03-28 10:15 UTC](https://news.ycombinator.com/item?id=19510791)
        Thank you ^c19510791

    - **Nanite** · [2019-03-28 10:27 UTC](https://news.ycombinator.com/item?id=19510849)
      Search for : NDIR CO2 sensor module. The ones without auto-calibration go for under \$20 in China. ^c19510849

  - **gsich** · [2019-03-28 12:41 UTC](https://news.ycombinator.com/item?id=19511579)
    CO2 sensors are available for about 20€. MH-Z19 or MH-Z14 are common ones. ^c19511579

  - **arcturus17** · [2019-03-28 08:07 UTC](https://news.ycombinator.com/item?id=19510252)
    Can anyone recommend a better sensor? I’d like to build an upgraded version of this - that way I’ll also learn more. ^c19510252

- **wuyishan** · [2019-03-28 06:53 UTC](https://news.ycombinator.com/item?id=19509880)
  A similar, yet completely different project:
  [https://luftdaten.info/en/home-en/](<https://luftdaten.info/en/home-en/>) 
  Can be seen as a "worldwide crowd sourced air quality measurement projects using cheap DIY sensor/data collector" ^c19509880

- **Uhhrrr** · [2019-03-28 01:48 UTC](https://news.ycombinator.com/item?id=19508371)
  The Docker part seems thoroughly unnecessary. ^c19508371

  - **alexandros** · [2019-03-28 03:50 UTC](https://news.ycombinator.com/item?id=19509072)
    Hey there - BalenaOS is built to run containerised workloads on small devices and is quite stripped down otherwise, kinda like coreOS. So in that sense our architecture allows you to have less stuff you don't need floating around, saving you overhead. We focused on Docker containers since balenaCloud is built for fleets. It's important that our stack supports not just one but many copies of the same device running the same code, and then it can be updated in production etc, just like a set of servers. If one is optimizing for a single device, just naked Raspbian will do fine of course. Our approach has a bit of overhead up front in terms of setup, but you get a production ready setup from day one in return. ^c19509072

  - **StreakyCobra** · [2019-03-28 09:14 UTC](https://news.ycombinator.com/item?id=19510521)
    If you do not want to need 10 different RPIs for running 10 different functionalities (Pi-hole, RetroPie, remote access, cloud, side-projects, air quality monitoring, etc.), docker is a good solution to easily deploy several services on a single RPI, and it prevents dependency hell. ^c19510521

  - **tylerflick** · [2019-03-28 02:15 UTC](https://news.ycombinator.com/item?id=19508536)
    I can't understand why they would add anymore overhead on such a low powered device. ^c19508536

    - **viraptor** · [2019-03-28 04:34 UTC](https://news.ycombinator.com/item?id=19509283)
      Zero and original raspberries can be low-powered. 3+ is a quad core with 1gb memory. Docker doesn't even show up on CPU monitor and takes 2\% shared memory in my case. The overhead of a namespace is not really noticeable either, unless you're doing lots of processing. (My influx+grafana+monitors sit under 5\% CPU almost all the time) ^c19509283

    - **jjeaff** · [2019-03-28 03:14 UTC](https://news.ycombinator.com/item?id=19508874)
      Ease of setup and reproducibility probably. And docker doesn't add much overhead, especially when running natively on Linux. ^c19508874

    - **Gigablah** · [2019-03-28 03:14 UTC](https://news.ycombinator.com/item?id=19508878)
      What overhead? ^c19508878

      "Docker induces no significant overhead on CPU nor memory usage, compared to a native execution (worse observation: -4\%; 0\% on all others)" \[1\]

      \[1\]: [https://roudier.io/2015/08/docker-vs-kvm-vs-native-performan...](<https://roudier.io/2015/08/docker-vs-kvm-vs-native-performance-comparison/>)

      - **krageon** · [2019-03-28 07:44 UTC](https://news.ycombinator.com/item?id=19510149)
        Think about how the stack works. I'm not saying this measurement is definitely wrong, but if you're finding exactly 0 overhead then you have to suspect there is something weird going on with how you're measuring it. ^c19510149

        - **Gigablah** · [2019-03-28 11:08 UTC](https://news.ycombinator.com/item?id=19511014)
          The processes are still running natively. The most common overheads would be due to network and storage driver and those can be mitigated with some simple settings. The Docker daemon is more or less a process supervisor at this point. ^c19511014

          - **krageon** · [2019-03-28 12:55 UTC](https://news.ycombinator.com/item?id=19511684)
            I think we have a fundamentally different view of what "natively" means and what it means to be "more or less a process supervisor". That's fine, but it also means we won't get to an agreement that we are both at peace with in this case. ^c19511684

            - **tinco** · [2019-03-28 18:28 UTC](https://news.ycombinator.com/item?id=19515100)
              What feature of Docker makes you consider it significantly more than a process supervisor? ^c19515100

  - **viraptor** · [2019-03-28 04:28 UTC](https://news.ycombinator.com/item?id=19509256)
    It gives you easy upgrades and nice dependency separation. It's not required in this case, but it sure makes operations easier. (Doing the same for multiple services on rpi) ^c19509256

  - **dikei** · [2019-03-28 03:44 UTC](https://news.ycombinator.com/item?id=19509046)
    Agree, an Ansible playbook would have easily suffice. ^c19509046

    - **joshvm** · [2019-03-28 09:27 UTC](https://news.ycombinator.com/item?id=19510576)
      One downside of Ansible on the Pi is that a lot of stuff involves building from scratch, because aren't armhf packages available, or what's available in apt is hopelessly outdated. I have a stack at work that takes a day to build on the hardware. With Docker I can build once and pull the image later. I guess you could do similar with Ansible and copy build artefacts over, but Docker is a simpler solution. ^c19510576

    - **flo123456** · [2019-03-28 07:06 UTC](https://news.ycombinator.com/item?id=19509928)
      While I do like Ansible, it‘s not really the right tool for a tutorial about sensors. ^c19509928

      It‘s a lot easier to explain that you need to pull & run some image than it is to explain installing python, get your ansible host configuration right and then run a playbook. There’s just a lot more variance (and therefore margin for error) that you don’t want to deal with when you’re explaining something else entirely.

- **TheSpiceIsLife** · [2019-03-28 08:30 UTC](https://news.ycombinator.com/item?id=19510342)
  I'm curious to hear from anyone who runs air quality monitors at home: how has knowledge of the quality of the air in your house affected your behaviour? ^c19510342

  My house is 56 years old. I'm guessing the kitchen upgrade is at least 5 years old. The carpet is probably at least a 5 years old. There isn't much fresh paint in here.

  Am I about right to assume I probably don't have much in the way off off-gassing from anything in here, or does carpet / furniture / melamine continually off-gas for it's entire life?

  Anyway, I've got some idea that CO2 buildup is a thing, and humidity, and off-gassing, so... I tend to ventilate the house frequently even during winter. Even when it's -5 outside, I'll occasionally open one or more windows / doors and turn the kitchen exhaust fan on in order to draw fresh air in and across the house. I'll also occasionally open multiple doors / windows for 10 minutes or so in an effort to replace the majority of the air in the house.

  I tend to eschew yet-another-device that needs maintenance / power / charging / monitoring / fiddling because I tend to do a lot of that at work and would rather just come home and not-have-to-maintain-another-97-machines.

  So I'm interested in the *on average / sort of good enough / sometimes over-shoot-the-mark* behavioural changes that would result *if I did have air quality monitors*.

  - **msisk6** · [2019-03-28 14:01 UTC](https://news.ycombinator.com/item?id=19512230)
    We have a new house--about a year old now--here in Texas with all the efficiency and insulation stuff. I noticed  after working in my office with the door and windows closed I didn't feel so good after awhile. ^c19512230

    I got one of those trendy Awair monitors and stuck it on my desk and hooked up the iPhone app. And sure enough, when I started not feeling well it was because the CO2 was over 1500 ppm.

    I don't know about the accuracy of the actual CO2 measurement, but I figure the delta is at least good enough to spot trends. And yeah, those times I don't feel well is always associated with a rise of CO2. I "fix" it by either opening the door and/or window or running the fan of the central air system. Our system also has a "bleed air" adjustment for outside air. I turned that up a bit, too.

    The Awair also does "chemicals" and PM2.5. I'm surprised our new house doesn't an issues with those, but I do see PM2.5 go up when the window in my office is open and "chemicals" fluctuates throughout the day but at a low level. I'm not exactly sure what "chemicals" means in this context; I haven't really looked into it yet.

    You might consider the Awair; I've been happy with it. I have several thousand systems that need tending at work and, same as you, I don't need to come home and do more. My wife's Windows gaming rig needs enough of that as it is...

  - **hadlock** · [2019-03-28 09:15 UTC](https://news.ycombinator.com/item?id=19510526)
    Most air quality measurement involves particulate matter, specifically PM 2.5. This is primarily wood smoke, car exhaust and a couple of other combustion-related. When the news talks about air quality, most commonly they are referring to PM 2.5. ^c19510526

    If you are looking for out-gassing (paints, carpets, furniture etc) you probably need to invest in formaldehyde and other gas sensors. In your case you ought to look at your furniture and electronics as they will produce the most out-gassing. This is different from the above particulate matter.

- **pookieinc** · [2019-03-28 08:55 UTC](https://news.ycombinator.com/item?id=19510441)
  We've been on the hunt for the most accurate Air Quality Monitor since we've just moved to the Middle East and have had a really tough time finding something accurate. Aside from building one and having it receive questionable ratings, does anyone have any suggestions on a super reliable machine they've been happy with that has proven its accuracy in some way? ^c19510441

  - **mike\_h** · [2019-03-28 10:46 UTC](https://news.ycombinator.com/item?id=19510933)
    Here’s a lab writeup comparing a few models from about a year ago: ^c19510933

    [https://smartairfilters.com/en/blog/are-cheap-particle-count...](<https://smartairfilters.com/en/blog/are-cheap-particle-counters-accurate/>)

    Depending on which part of the Middle East you’re in, you may need a PM10 (dust) monitor.  The devices here just do PM2.5 (smog).

  - **joshvm** · [2019-03-28 09:23 UTC](https://news.ycombinator.com/item?id=19510559)
    What do you want to measure? Saying you need it to be super accurate doesn't mean much on its own. Air quality is subjective in any case. ^c19510559

    The BME680 (like other chips) measures VOC content - organic stuff like alcohol. You can also measure dust concentration, for example if you lived in China, PM2. 5 would be good to know. And you can also use CO2 concentration, but good CO2 sensors cost a lot. Some chips measure "equivalent CO2" but it's not the same.

- **djhworld** · [2019-03-28 13:10 UTC](https://news.ycombinator.com/item?id=19511790)
  Has anyone been running this in the field for a few months/weeks. ^c19511790

  I'm wondering how the SD card gets on with the constant writes into InfluxDB (assuming the samplesa are taken frequently)

  - **Already\_\_Taken** · [2019-03-28 13:44 UTC](https://news.ycombinator.com/item?id=19512101)
    SD cards fail but they're not a house of cards. I've logged into couch dB every minute for nearly 5 years. only about a million entries bit since it's replicated to other nodes a failed card is ok. ^c19512101

- **shawnps** · [2019-03-28 04:37 UTC](https://news.ycombinator.com/item?id=19509298)
  If you're interested in purchasing an air quality monitor, Awair is nice: ^c19509298

  [https://getawair.com/](<https://getawair.com/>)

  I learned about it from DHH's talk on air quality:

  [https://www.youtube.com/watch?v\=MRqh8oLY7Ik](<https://www.youtube.com/watch?v=MRqh8oLY7Ik>)

  - **zantana** · [2019-03-28 13:56 UTC](https://news.ycombinator.com/item?id=19512193)
    I was really keen on the Awair, but the necessity to be connected to wifi to function was a deal killer for me.
    From what I've seen this will never change which is disappointing. ^c19512193

  - **bhargav** · [2019-03-28 04:42 UTC](https://news.ycombinator.com/item?id=19509322)
    Did you simply use one Awair device around your entire house? ^c19509322

  - **borumpilot** · [2019-03-28 11:32 UTC](https://news.ycombinator.com/item?id=19511123)
    Unfortunately, only shipping to the US & Canada. ^c19511123

    - **Luc** · [2019-03-28 13:38 UTC](https://news.ycombinator.com/item?id=19512042)
      Did you try [https://getawair.co.uk/](<https://getawair.co.uk/>) ? ^c19512042

- **bayesian\_horse** · [2019-03-28 07:14 UTC](https://news.ycombinator.com/item?id=19509984)
  I'm working on similar things, and at the moment I prefer Redis and Postgres. Redis just got streams, a bit like Kafka, and Postgres has extensions for timeseries. ^c19509984

- **gpm** · [2019-03-28 02:46 UTC](https://news.ycombinator.com/item?id=19508720)
  What do people think about the recommended sensor? ^c19508720

  Is it reasonably accurate? Are there better alternatives?

  - **retSava** · [2019-03-28 10:53 UTC](https://news.ycombinator.com/item?id=19510953)
    Since indoor air quality/IAQ is a composite metric, I'd say that some of the interesting things to measure are: ^c19510953


    ```
        PM2.5/PM10 - particles from combustion, exhaust, traffic (wheels against asphalt) etc
        CO, NOx - from traffic exhaust
        CO2 - from humans
        VOC - volatile organic compounds, IIRC correlated with cancer and lots of unpleasant stuff. Comes mostly from paint and manufactured stuff (furniture etc) at home.
    ```

    
    I'm about to make a small sensor thingee that measures these plus relative humidity (too dry at home, 30--50\% should be good, we're at 10-15\%), temperature (16-20 when sleeping), and for fun barometric pressure, ambient light.

    For this I'm going to use a Honeywell HPMA-115S0, and IIRC BME680 and some other stuff. If interesting I can have a closer look. Battery-operated devices are a little bit of a challenge since often some of these sensors internally use a heating element for a long duration, so they consume quite a lot of power.

    The Plantower looks interesting, thanks for the link.

  - **peferron** · [2019-03-28 03:16 UTC](https://news.ycombinator.com/item?id=19508890)
    The sensor doesn't appear to measure particulate matter, so I'd take the air quality reading with a large grain of salt. ^c19508890

    - **flo123456** · [2019-03-28 07:08 UTC](https://news.ycombinator.com/item?id=19509939)
      To add on that, if you want to measure particulate matter take an SDS11 and have a look at [https://luftdaten.info](<https://luftdaten.info>) ^c19509939

    - **gpm** · [2019-03-28 03:26 UTC](https://news.ycombinator.com/item?id=19508951)
      Agreed - it's pretty explicitly just a volatile organic compound (gas) detector. On the other hand VOCs, especially as a proxy for CO2 and air circulation, are also interesting. ^c19508951

    - **ekianjo** · [2019-03-28 04:49 UTC](https://news.ycombinator.com/item?id=19509367)
      It does not even measure Ozone concentration which is one of the key things you would want to look at for air quality... ^c19509367

  - **gpm** · [2019-03-28 02:52 UTC](https://news.ycombinator.com/item?id=19508763)
    For anyone else who goes looking for the datasheet - the link from the shop is broken but is saved in the wayback machine. ^c19508763

    [https://web.archive.org/web/20180130060734/https://ae-bst.re...](<https://web.archive.org/web/20180130060734/https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BME680-DS001-00.pdf>)

  - **gpm** · [2019-03-28 03:08 UTC](https://news.ycombinator.com/item?id=19508847)
    Someone replied with this interesting and then deleted their comment. It doesn't include the same sensor, but it does include a related one and it's a wonderfully detailed analysis: ^c19508847

    Thank you for linking it!

    [https://www.kandrsmith.org/RJS/Misc/Hygrometers/calib\_many.h...](<https://www.kandrsmith.org/RJS/Misc/Hygrometers/calib_many.html>)

  - **unknown** · [2019-03-28 02:57 UTC](https://news.ycombinator.com/item?id=19508787)
    [deleted] ^c19508787

- **unknown** · [2019-03-28 05:56 UTC](https://news.ycombinator.com/item?id=19509639)
  [deleted] ^c19509639

- **bugsense** · [2019-03-28 09:59 UTC](https://news.ycombinator.com/item?id=19510714)
  Ditch Grafana+Influx for Netdata and you are golden :) ^c19510714

  - **tpxl** · [2019-03-29 10:49 UTC](https://news.ycombinator.com/item?id=19520505)
    Real question, why? ^c19520505

    I'm running grafana + influx and it's doing the job well. The netdata git repo is full of marketing fluff and fails to convince me it's any better.

  - **alexandros** · [2019-03-28 13:45 UTC](https://news.ycombinator.com/item?id=19512107)
    That's a good point! We should try that as an alternative next :) ^c19512107

