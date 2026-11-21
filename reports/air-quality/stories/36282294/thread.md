# [Add \$4 WiFi Logging to IKEA’s \$12 Air Quality Sensor (Wemos and Vindriktning)](https://news.ycombinator.com/item?id=36282294)

Article: [https://hackaday.com/2021/07/24/esp8266-adds-wifi-logging-to-ikeas-air-quality-sensor/](<https://hackaday.com/2021/07/24/esp8266-adds-wifi-logging-to-ikeas-air-quality-sensor/>)

ck2 · 2023-06-11 15:29 UTC · 39 reported comments · archived 2026-11-08 13:06 UTC
Observation: 2026-11-08 13:06 UTC → 2026-11-08 13:06 UTC

## Comments

- **lathiat** · [2023-06-11 16:58 UTC](https://news.ycombinator.com/item?id=36283114)
  While these projects are cool it’s worth noting IKEA since released a Matter capable version in the last year. It is 3 times the cost though  (US \$50 it seems). Still quite cheap on the whole I think. ^c36283114

  - **eric-hu** · [2023-06-11 17:32 UTC](https://news.ycombinator.com/item?id=36283463)
    Worth mentioning for those who were ignorant like me: Matter looks like an IoT protocol that’s cross platform across most home sensors and controllers (Apple home, Google nest, Alexa, etc) ^c36283463

    - **vardump** · [2023-06-11 18:53 UTC](https://news.ycombinator.com/item?id=36284426)
      All I'm interested in is whether it can be cloud free or not. ^c36284426

      DIY Wifi addition obviously can, but not so sure of the alternative.

      - **omnicognate** · [2023-06-11 19:08 UTC](https://news.ycombinator.com/item?id=36284555)
        Matter devices are required to work without cloud: [https://matter-smarthome.de/en/benefits/benefits-of-matter-1...](<https://matter-smarthome.de/en/benefits/benefits-of-matter-1-local-connection/>) ^c36284555

        - **lathiat** · [2023-06-12 11:35 UTC](https://news.ycombinator.com/item?id=36291843)
          You can also use them with HomeKit, whatever androids is called and with home assistant. All local. ^c36291843

      - **cassianoleal** · [2023-06-11 19:20 UTC](https://news.ycombinator.com/item?id=36284663)
        \> Matter can also work entirely on your local network, so gadgets should respond more quickly and work even if your internet is down. ^c36284663

        [https://www.theverge.com/22832127/matter-smart-home-products...](<https://www.theverge.com/22832127/matter-smart-home-products-thread-wifi-explainer>)

  - **ck2** · [2023-06-11 17:06 UTC](https://news.ycombinator.com/item?id=36283206)
    Oh interesting, had not seen that, the "Vindstyrka" ^c36283206

    [https://www.ikea.com/us/en/p/vindstyrka-air-quality-sensor-s...](<https://www.ikea.com/us/en/p/vindstyrka-air-quality-sensor-smart-30498239/>)

- **PaulBGD\_** · [2023-06-11 17:04 UTC](https://news.ycombinator.com/item?id=36283183)
  If anyone is going to do it I highly recommend just going with esphome now for the firmware, it’s way simpler and better maintained. You can even update the firmware over the network. ^c36283183

  - **tga** · [2023-06-11 20:01 UTC](https://news.ycombinator.com/item?id=36285041)
    And if you want to turn your ESP8266 into a standalone appliance, with a web interface and directly editable config that doesn't need a build step, Tasmota is another great option. ^c36285041

    [https://tasmota.github.io/docs/](<https://tasmota.github.io/docs/>)

  - **ck2** · [2023-06-11 17:34 UTC](https://news.ycombinator.com/item?id=36283484)
    Thanks for the tip ^c36283484

    [https://esphome.io/components/sensor/pm1006.html](<https://esphome.io/components/sensor/pm1006.html>)

    [https://community.home-assistant.io/t/ikea-vindriktning-air-...](<https://community.home-assistant.io/t/ikea-vindriktning-air-quality-sensor/324599>)

    - **isoprophlex** · [2023-06-11 18:59 UTC](https://news.ycombinator.com/item?id=36284468)
      How on EARTH did I not know esphome existed?! Why am I bothering with this heterogeneous plate of home coded ESP and Arduino spaghetti throughout my house?! ^c36284468

      Thanks for sharing!

      - **stavros** · [2023-06-11 19:18 UTC](https://news.ycombinator.com/item?id=36284638)
        I do love ESPhome, but I don't know why they don't support a simple PIR sensor. ^c36284638

        - **tda** · [2023-06-11 20:26 UTC](https://news.ycombinator.com/item?id=36285263)
          A simple pir sensor just has a digital out that is either high or low. That is supported as a digital in sensor. Only for devices with a more complicated protocol (mostly i2c, spi and uart) you need a special sensor specific integration ^c36285263

          - **stavros** · [2023-06-11 20:31 UTC](https://news.ycombinator.com/item?id=36285336)
            Oh is it? I tried to look for that but couldn't find it, thanks! ^c36285336

            I can't wait for it to get Zigbee support!

  - **gerdesj** · [2023-06-11 20:21 UTC](https://news.ycombinator.com/item?id=36285221)
    If you install Home Assistant (HAOS or Supervised) on something then ESPHome is a one click install with a web GUI.  There's an OVA for HAOS as well as all the usual suspects - amd\_64, RPi and more. ^c36285221

    If you don't want all that stuff then do it from the command prompt, most Linux distros have it in the package manager and no doubt Mac n that have easy to install options.

- **xgbi** · [2023-06-11 16:53 UTC](https://news.ycombinator.com/item?id=36283060)
  I did it a few years ago, it was very easy to do, and integrated very fine with Home Assistant. ^c36283060

  It's not too hard to do, you just have to have the component, and some solder.

  The main issue I have is the noise, it is really noticeable (and the sound mode makes it less accurate: [https://github.com/Hypfer/esp8266-vindriktning-particle-sens...](<https://github.com/Hypfer/esp8266-vindriktning-particle-sensor/issues/47>))

  - **lannisterstark** · [2023-06-11 23:34 UTC](https://news.ycombinator.com/item?id=36286842)
    \>Home Assistant ^c36286842

    Man I can't wait until someone come with a more user friendly alternative to Home ASSistant.

    It's YAML hell. I work with YAML at work and then when I come home I have to fiddle with YAML again.

    - **Larrikin** · [2023-06-12 00:48 UTC](https://news.ycombinator.com/item?id=36287295)
      There are Python, C\#, and I believe JavaScript options. Can't totally avoid yaml but you don't have to use it that much. ^c36287295

    - **vGPU** · [2023-06-12 00:27 UTC](https://news.ycombinator.com/item?id=36287153)
      I set HASS up a year ago or so and it’s been great. Don’t need to fiddle with anything aside from having to migrate when my zigbee stick died. ^c36287153

  - **shrx** · [2023-06-11 18:25 UTC](https://news.ycombinator.com/item?id=36284142)
    I can happily report that the Vindstyrka is silent, so it's a reasonable upgrade (also supports Zigbee out of the box). ^c36284142

    - **Havoc** · [2023-06-12 19:46 UTC](https://news.ycombinator.com/item?id=36299854)
      Anything with a little fan in it won't be silent... ^c36299854

      Don't think there are any affordable particle sensors with fan though

- **Mutlut** · [2023-06-11 17:06 UTC](https://news.ycombinator.com/item?id=36283212)
  Unfortunat edoesn't support co2. ^c36283212

  Having co2 made it much much more aware to me to keep window open or open them and this effect is very long lasting for me, i'm doing this now for years and it stuck.

  I can highly recommend buying a \$60 or so co2 device.

  - **tosihakkeri** · [2023-06-11 17:31 UTC](https://news.ycombinator.com/item?id=36283451)
    Any particular devices or brands you could recommend? ^c36283451

    - **ahaucnx** · [2023-06-11 23:02 UTC](https://news.ycombinator.com/item?id=36286635)
      We maintain popular open source air quality monitor projects. You can source the components yourself or get a kit from us \[1\]. ^c36286635

      The indoor kits include a high quality NDIR CO2 Sensor from senseair.

      \[1\] [https://www.airgradient.com/kits/](<https://www.airgradient.com/kits/>)

    - **parhamn** · [2023-06-11 17:55 UTC](https://news.ycombinator.com/item?id=36283748)
      I use an Awair Element and it's been fine. The component parts on all these are pretty much the same though. ^c36283748

      - **eric-hu** · [2023-06-11 19:05 UTC](https://news.ycombinator.com/item?id=36284531)
        Oof, the Awair Element is 230 on Walmart and 275 on Amazon. That’s a fair bit more than the 60 that GP quoted. ^c36284531

        - **crazygringo** · [2023-06-11 20:21 UTC](https://news.ycombinator.com/item?id=36285214)
          It's \$157 now directly from their site -- \$209 with a 25\% off promo code. ^c36285214

          Still way more than \$60 but more reasonable for what you get. It's basically a \$60 sensor that costs more because of WiFi and phone integration.

          [https://www.getawair.com/products/element](<https://www.getawair.com/products/element>)

      - **crazygringo** · [2023-06-11 18:21 UTC](https://news.ycombinator.com/item?id=36284087)
        Yup me too. It's fairly attractive looking and integrates with your phone to view history and get alerts. ^c36284087

    - **abawany** · [2023-06-11 19:19 UTC](https://news.ycombinator.com/item?id=36284647)
      not the GP but I'm a fan of the Netatmo Indoor Air Quality Monitor. Price is fair imo (100usd), the app works well plus the data can be accessed via the web, and it includes humidity, temperature, and noise monitoring in addition to CO2 monitoring. ^c36284647

    - **Mutlut** · [2023-06-11 19:23 UTC](https://news.ycombinator.com/item?id=36284695)
      i only bought TFA Dostmann AirControl Mini CO2 Meter TFA 31.5006 Ambient Air Monitoring by accident, it does what it does and is super unflashy so i got another one a year later. ^c36284695

  - **eric-hu** · [2023-06-11 17:33 UTC](https://news.ycombinator.com/item?id=36283479)
    Do these \$60 CO2 devices also measure air pollution like IKEA’s? ^c36283479

    - **crazygringo** · [2023-06-11 18:19 UTC](https://news.ycombinator.com/item?id=36284070)
      Usually yes. PM2.5 sensors are usually the common denominator across all consumer air sensors. ^c36284070

    - **lathiat** · [2023-06-12 11:37 UTC](https://news.ycombinator.com/item?id=36291873)
      Most of the \$60 ones aren’t really measuring CO2. The usual giveaway is if the sensor also measures VOC or TVOC most are estimating the CO2 based on that. Which has only a vague correlation sometimes and not remotely close to useful. ^c36291873

      You need a device that specifically  quotes having an “NDIR” sensor and most are \$100+

      - **Mutlut** · [2023-06-25 09:34 UTC](https://news.ycombinator.com/item?id=36466399)
        The one i mentioned btw. only hsa that NDIR sensor and is at 60 bucks: "Hochwertiger NDIR Dual Beam Sensor" \<\> "high quality NDIR Dual beam sensor" ^c36466399

        And it doesn't meassure anything else. So a good point that its not the same thing and if you want both, you probably need to spend 100+

- **ck2** · [2023-06-11 15:31 UTC](https://news.ycombinator.com/item?id=36282315)
  direct links: ^c36282315

  [https://github.com/Hypfer/esp8266-vindriktning-particle-sens...](<https://github.com/Hypfer/esp8266-vindriktning-particle-sensor>)

  [https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor...](<https://www.ikea.com/us/en/p/vindriktning-air-quality-sensor-60515911/>)

- **quickthrowman** · [2023-06-11 17:08 UTC](https://news.ycombinator.com/item?id=36283235)
  What sort of control sequences are people using for the PM2.5 sensor? Something like ‘if particulate matter is above SETPOINT; then enable exhaust fan and open filtered fresh air intake damper; else if particulate matter is below SETPOINT and exhaust fan on and damper open, disable fan and close damper’? ^c36283235

  Or is this just for logging indoor PM2.5 values?

  - **crazygringo** · [2023-06-11 18:24 UTC](https://news.ycombinator.com/item?id=36284124)
    If indoor values go up you probably just want to turn on your air purifier. ^c36284124

    If the values are high because of pollution or wildfires you definitely don't want to increase air from outside.

- **deepspace** · [2023-06-12 18:55 UTC](https://news.ycombinator.com/item?id=36299087)
  Does anyone know if the IKEA sensor detects cigarette smoke?  Or, if not, is there any cheap sensor available to detect smoking (and vaping, if feasible)? ^c36299087

