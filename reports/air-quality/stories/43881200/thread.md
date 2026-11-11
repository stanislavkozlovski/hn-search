# [Show HN: Live Air Quality Monitor](https://news.ycombinator.com/item?id=43881200)

Article: [https://github.com/benb0jangles/Air\_Quality\_monitor](<https://github.com/benb0jangles/Air_Quality_monitor>)

benbojangles · 2025-05-03 18:51 UTC · 13 reported comments · archived 2026-11-08 13:53 UTC
Observation: 2026-11-08 13:53 UTC → 2026-11-08 13:53 UTC

A comprehensive indoor air quality monitoring system built with ESP32-C3 Super Mini and multiple environmental sensors. This project helps you monitor CO2, temperature, humidity, volatile organic compounds (VOCs), nitrogen oxides (NOx), and particulate matter (PM1.0, PM2.5, PM10) to maintain healthy air quality in your home or office.

## Comments

- **sneak** · [2025-05-03 22:53 UTC](https://news.ycombinator.com/item?id=43883019)
  How does this compare to ESPHome?  I understand it can do this job relatively straightforwardly and can pipe the data into either Home Assistant or Prometheus, so as to not reinvent the web interface wheel. ^c43883019

  - **benbojangles** · [2025-05-04 08:53 UTC](https://news.ycombinator.com/item?id=43885471)
    I guess this board setup has more freedom over sensor code control and adjustment, is not limited to local network it can be monitored anywhere. The user could easily setup the board to use esphome too ^c43885471

- **ssuds** · [2025-05-04 04:36 UTC](https://news.ycombinator.com/item?id=43884519)
  Cool project, but I’m curious how this is different from other open source air quality monitoring projects like AirGradient? ^c43884519

  - **benbojangles** · [2025-05-04 08:55 UTC](https://news.ycombinator.com/item?id=43885480)
    This is a DIY board and roughly 150 cheaper than airgradient ^c43885480

    - **ssuds** · [2025-05-04 23:26 UTC](https://news.ycombinator.com/item?id=43890493)
      For sure. Was just curious as they started out with a super basic DIY setup [https://www.airgradient.com/documentation/diy/](<https://www.airgradient.com/documentation/diy/>) (which can be implemented without the PCB even, as another commenter in this thread suggested) so I was wondering if there was a functionality you found was missing that sparked you to create this project! ^c43890493

      - **benbojangles** · [2025-05-05 16:29 UTC](https://news.ycombinator.com/item?id=43896829)
        From reading their specs, my pcb uses higher spec components (esp32, scd41, sgp41), newer technology, better accuracy, more sensing capability (VOC, & N0x) ^c43896829

    - **wkat4242** · [2025-05-04 09:44 UTC](https://news.ycombinator.com/item?id=43885682)
      It probably doesn't even need a board, you can just wire all the sensors in a box and solder the cables. Each sensor only has 3 or 4 and so does the display. ^c43885682

      But a board is cleaner and they're super cheap to get made in China unless you're shipping to the US I guess lol.

      I've built sensor boards like these too. But more with Dallas one wire sensors to measure temperature in different locations of central heating systems.

      - **benbojangles** · [2025-05-04 09:56 UTC](https://news.ycombinator.com/item?id=43885731)
        Wires are chaotic and a point of failure ^c43885731

        - **wkat4242** · [2025-05-04 10:03 UTC](https://news.ycombinator.com/item?id=43885756)
          True but they do facilitate more flexible placement. I use them a lot for one off projects. ^c43885756

          - **benbojangles** · [2025-05-04 11:07 UTC](https://news.ycombinator.com/item?id=43886028)
            Have you tried kicad ^c43886028

            - **wkat4242** · [2025-05-04 11:11 UTC](https://news.ycombinator.com/item?id=43886044)
              No I usually use CircuitMaker. I like their big footprint database. ^c43886044

- **Emmarof** · [2025-05-07 11:01 UTC](https://news.ycombinator.com/item?id=43914212)
  Where did you buy your components from? ^c43914212

  - **benbojangles** · [2025-05-07 13:20 UTC](https://news.ycombinator.com/item?id=43915303)
    Where did I buy my components? Or where can people buy their own components? YMMV. ^c43915303

