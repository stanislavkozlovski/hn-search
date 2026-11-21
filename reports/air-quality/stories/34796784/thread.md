# [IKEA launches VINDSTYRKA – a smart sensor to measure indoor air quality](https://news.ycombinator.com/item?id=34796784)

Article: [https://about.ikea.com/en/newsroom/2023/02/14/ikea-launches-vindstyrka-a-smart-sensor-to-measure-indoor-air-quality](<https://about.ikea.com/en/newsroom/2023/02/14/ikea-launches-vindstyrka-a-smart-sensor-to-measure-indoor-air-quality>)

bribroder · 2023-02-14 22:01 UTC · 29 reported comments · archived 2026-11-08 12:41 UTC
Observation: 2026-11-08 12:41 UTC → 2026-11-08 12:41 UTC

## Comments

- **makeitdouble** · [2023-02-14 23:36 UTC](https://news.ycombinator.com/item?id=34797828)
  Too bad it doesn’t monitor CO2 as well, but I guess the cost would be pretty different ? ^c34797828

  Having a screen is still an improvement over their current monitor \[0\], and the out of the box hub support is sure a plus.

  PS: to note, IKEA also has a new air purifier\[1\], but won’t benefit from any auto control apparently. Feels like a missed opportunity.

  \[0\] [https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor...](<https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor-60515911/>)

  \[1\] [https://www.ikea.com/us/en/p/uppatvind-air-purifier-60498228...](<https://www.ikea.com/us/en/p/uppatvind-air-purifier-60498228/>)

  - **ralfd** · [2023-02-15 19:44 UTC](https://news.ycombinator.com/item?id=34809521)
    Ask hn: Any recommendations for a CO2 sensor? ^c34809521

- **Tijdreiziger** · [2023-02-14 23:36 UTC](https://news.ycombinator.com/item?id=34797827)
  This looks great. It looks like the existing VINDRIKTNING sensor, but with more sensors and compatible with their existing smarthome hub (which implies Zigbee connectivity, I think). ^c34797827

  The only question is whether the fan will be as obnoxious as the one in the VINDRIKTNING. It’s audible and constantly spins up and down, so it’s extremely distracting. I often just unplug it for that reason, which is unfortunate.

  - **wkat4242** · [2023-02-15 02:51 UTC](https://news.ycombinator.com/item?id=34799407)
    There's a mod for that, connect the fan to constant power (3.3V instead of 5V if you want it quieter too) ^c34799407

  - **wkat4242** · [2023-02-15 10:11 UTC](https://news.ycombinator.com/item?id=34801942)
    It's a bit annoying that this doesn't work with the tradfri hub by the way, only the much more expensive dirigera one. Both are zigbee so they both have the technical capability. ^c34801942

    - **euroderf** · [2023-02-15 20:21 UTC](https://news.ycombinator.com/item?id=34809988)
      So it should talk Zigbee to a Conbee 2 (or other Zigbee hub) and be able to hook into a Matter network ? ... he asked hopefully. ^c34809988

      - **wkat4242** · [2023-02-15 20:25 UTC](https://news.ycombinator.com/item?id=34810048)
        Probably yes, but it depends of course on whether the Zigbee stack supports it. There's several zigbee stacks for HA and they each support their own subset of hardware. ^c34810048

        This is in fact what Matter/Thread is supposed to solve with more standardisation.

        Check this excellent site for an overview of which device is compatible with this stack (and see what a mess it is!!)

        [https://zigbee.blakadder.com/](<https://zigbee.blakadder.com/>)

- **mc32** · [2023-02-14 23:48 UTC](https://news.ycombinator.com/item?id=34797945)
  I'm glad a known brand is taking this line of product. ^c34797945

  I am unsure about IKEA quality.  I'd like to see someone like Apple (or Google or even MS take this up)

  I question IKEA because they are all over the place quality-wise.  Some things are built with quality in mind, whereas others are semi-disposable and I cannot tell what this will be.  Will it require and enable periodic recalibration?

  - **jerlam** · [2023-02-15 00:46 UTC](https://news.ycombinator.com/item?id=34798490)
    Amazon makes one but to view data, it's app based and that's a dealbreaker for me: [https://www.theverge.com/22971411/amazon-smart-air-quality-m...](<https://www.theverge.com/22971411/amazon-smart-air-quality-monitor-iaq-review>) ^c34798490

    - **starky** · [2023-02-15 07:02 UTC](https://news.ycombinator.com/item?id=34800904)
      Yeah, I bought one and am pretty disappointed by it. Not only does the Amazon app suck for looking at the data, but it has CO instead of CO2 for some idiotic reason. ^c34800904

      At least it convinced me to finally figure out how to get my AirGradient working with Home Assistant.

      - **russianGuy83829** · [2023-02-15 16:14 UTC](https://news.ycombinator.com/item?id=34805837)
        measuring CO2 is more expensive than CO, a decent sensor alone would cost more than \$20 ^c34805837

  - **makeitdouble** · [2023-02-15 01:21 UTC](https://news.ycombinator.com/item?id=34798796)
    I have their previous air monitoring device (just displays a range of color from red -\> orange -\> yellow -\> green), and regularly compare it to the air quality display of a Sharp air purifier in the same room. ^c34798796

    It's no scientific measurement, but both devices seem to be mostly reacting the same. There's some time lag between the two, and the air flow seems to impact a lot of what they'll detect (the air purifier is more stable in that respect as it's the one creating the airflow), but the IKEA sensor doesn't seem to be too bad in that respect. At least I haven't seen the SHARP one go berserk while the IKEA sensor stays green, if that's what you would be fearing.

    - **mc32** · [2023-02-15 02:24 UTC](https://news.ycombinator.com/item?id=34799235)
      So most air quality monitors need to be "cleaned" and recalibrated by cycling them in a clean air enviro for a few mins, especially if they have been exposed to high levels of pollutants otherwise they may be "off" in their measurements. ^c34799235

      Anyhow, it's worth giving them a try it seems.

- **Larrikin** · [2023-02-15 01:37 UTC](https://news.ycombinator.com/item?id=34798931)
  The product looks nice, but the most important question will be whether it works with Home Assistant. I'll pass if it's locked down. ^c34798931

  - **gedy** · [2023-02-15 03:07 UTC](https://news.ycombinator.com/item?id=34799552)
    Just FYI that their current\[0\] can be somewhat easily (for hacker types) be modified to integrate with Home Assistant\[1\] ^c34799552

    \[0\] [https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor...](<https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor-60515911/>)

    \[1\] [https://style.oversubstance.net/2021/08/diy-use-an-ikea-vind...](<https://style.oversubstance.net/2021/08/diy-use-an-ikea-vindriktning-air-quality-sensor-in-home-assistant-with-esphome/>)

  - **tecleandor** · [2023-02-16 12:33 UTC](https://news.ycombinator.com/item?id=34817860)
    Seems like this new sensor supports the "Matter" standard, so it should be easy to connect it to Home Assistant... ^c34817860

- **mdmglr** · [2023-02-15 03:18 UTC](https://news.ycombinator.com/item?id=34799646)
  What’s the sensor IC? This is just a nice paperweight with a screen if it’s like all to other indoor air quality sensors which are way off and improperly calibrated. ^c34799646

- **anigbrowl** · [2023-02-14 22:15 UTC](https://news.ycombinator.com/item?id=34796959)
  Wish they included price information ^c34796959

  - **CharlesW** · [2023-02-15 00:26 UTC](https://news.ycombinator.com/item?id=34798303)
    It’s rumored to be priced at under \$50. Their screen-less air quality sensor is \$16. ^c34798303

- **slaw** · [2023-02-15 08:24 UTC](https://news.ycombinator.com/item?id=34801365)
  I got PM 2.5 sensor from Xiaomi for \$24.99. I am not sure if it works correctly. It shows 002-003 all the time. ^c34801365

  [https://a.aliexpress.com/\_Eu7cPbR](<https://a.aliexpress.com/_Eu7cPbR>)

  - **wkat4242** · [2023-02-15 10:15 UTC](https://news.ycombinator.com/item?id=34801961)
    That's pretty normal in a home. The sensor of my Xiaomi air purifier always shows similar levels. But one time there was a slight smell of burning outside (a little bin fire 100m away) and it immediately went to 200+ despite there not being visible smoke. ^c34801961

    Also, my await lite tracks the graph of the Xiaomi pretty well. I guess most fine dust comes from outside. Unless you're frying or 3D printing which elevates levels here in my house for sure.

    - **wkat4242** · [2023-02-15 18:21 UTC](https://news.ycombinator.com/item?id=34808238)
      Sorry that should be "Awair Lite" ^c34808238

  - **coldslawslay** · [2023-02-15 08:46 UTC](https://news.ycombinator.com/item?id=34801483)
    Yet you spam an affiliate link. ^c34801483

    Mods, please take a look at this user's comment history, it seems like spam is their main purpose...

    - **Octopuz** · [2023-02-15 11:06 UTC](https://news.ycombinator.com/item?id=34802318)
      If you look up a product in the AliExpress app and copy the link, this is what you get. It does not give you any commission unfortunately. So it's not an affiliate link. ^c34802318

      - **slaw** · [2023-02-15 16:24 UTC](https://news.ycombinator.com/item?id=34806029)
        That's correct. I posted a link from a product I just bought and received. ^c34806029

- **Am4TIfIsER0ppos** · [2023-02-15 00:43 UTC](https://news.ycombinator.com/item?id=34798468)
  I wouldn't suggest it if is like all the crap I have around me.  They're wood and metal not electronics and software. ^c34798468

  - **makeitdouble** · [2023-02-15 01:25 UTC](https://news.ycombinator.com/item?id=34798839)
    What would your point of comparison be ? ^c34798839

    I have a bias in that I went for the whole IKEA home automation, and it sure has rough edges, but I also was under the impression the other brands were in a similar situation (perhaps Phillips HUE system has a better reputation at this point ? provided their range of devices is more limited)

    - **Am4TIfIsER0ppos** · [2023-02-15 17:17 UTC](https://news.ycombinator.com/item?id=34807160)
      I don't think their macro sized wood and metal is very good so I doubt their microelectronics and software will be any different. ^c34807160

      - **makeitdouble** · [2023-02-16 00:33 UTC](https://news.ycombinator.com/item?id=34813215)
        It’s tough to assume different product line qualities are related for any major brand IMHO. ^c34813215

        Would you shun Microsoft keyboards because of the direction they took for Windows 11 ? Do you stay away from iPhones because mac Pros are really not a good deal ? Or trust Sony to make good computers because their headphones are really top notch ?

