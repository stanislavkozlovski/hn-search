# [AirGradient Air Quality Monitor Pro Kit Review](https://news.ycombinator.com/item?id=37194244)

Article: [https://bubelov.com/blog/2023/06/airgradient-pro-kit-review/](<https://bubelov.com/blog/2023/06/airgradient-pro-kit-review/>)

ahaucnx · 2023-08-19 23:05 UTC · 23 reported comments · archived 2026-11-08 13:12 UTC
Observation: 2026-11-08 13:11 UTC → 2026-11-08 13:12 UTC

## Comments

- **ck2** · [2023-08-20 02:55 UTC](https://news.ycombinator.com/item?id=37195635)
  Air quality monitoring is definitely the future. ^c37195635

  In home and all over every city.

  They really should be in every K-12 school and college university on a public open network.

  PurpleAir's network is the best we have right now because the federal airnow network is absolutely terrible with too few sensors.

  Hopefully AirGradient can build their public network, I've suggested before they try to get integrated with the WeatherSTEM network which has everything but air quality nationally.

  - **jiggawatts** · [2023-08-20 03:29 UTC](https://news.ycombinator.com/item?id=37195826)
    \> absolutely terrible with too few sensors. ^c37195826

    Different country, different government, same problem.

    I've dealt with the air quality services department in my state and they're so, *so* far away from what they ought to be doing that it's almost a joke.

    The best analogy I can come up with is the NASA/Boeing Space Launch System, which is so absurdly expensive that one of its single-use rocket engines costs more than several entire flights of a Falcon 9.

    Yet, everybody keeps moving on with the SLS project as-if it wasn't an absurd monstrosity. It's like the emperor's new clothes, there gets to a point where nobody will even admit the enormity of the error, so in some sense it ceases to exist.

    Back on the topic of air quality: I attended a meeting where they finally got a decent budget (a few million) and started talking about big data, scalable cloud services, and IoT.

    "Great," I said, "how many IoT devices were you thinking of? Ten thousand? Twenty? Fifty?"

    "Fifty" they replied.

    "Finally, we can get some decent coverage and accurate maps!"

    "No, not fifty thousand. Fifty."

    "Err... they're like \$100 each. If you're only buying \$5000 worth, where is the rest of the money going?"

    "Oh, we've spent that already on the planning phase. We don't have any budget left! What can you set up for free?"

    "Nothing."

  - **ahaucnx** · [2023-08-20 03:28 UTC](https://news.ycombinator.com/item?id=37195821)
    One more thing that could be of interest. We are currently running a very large global co-location project where we place our open hardware monitor next to reference devices. ^c37195821

    The aim is to develop algorithms to compensate for different environmental conditions (eg high humidity) in a structured way.

    These algorithms will then be publicly available and can be used to enhance the accuracy of low cost monitors.

    More information: [https://www.airgradient.com/research/](<https://www.airgradient.com/research/>)

  - **ahaucnx** · [2023-08-20 03:19 UTC](https://news.ycombinator.com/item?id=37195779)
    Yes this is a really good suggestion and still on my to do list. If anybody is involved in the WeatherSTEM project and can make an introduction please reach out to me. ^c37195779

- **jh00ker** · [2023-08-20 06:34 UTC](https://news.ycombinator.com/item?id=37196749)
  In Nov 2018, during the Camp Fire, I was in the Bay Area and was thrilled to have an air quality tracker from Wynd \[1\].  It is small, but seemingly accurate (when comparing outdoor readings with PurpleAir\[2\] readings).  It allowed me to identify drafts of contaminated air coming into my home and seal them up, such as the fireplace (of course) and the gap under the door to the garage.  I was running a few HEPA air purifiers and within a couple hours I was at 0 AQI for the whole weekend in the whole home. ^c37196749

  I remember Monday morning all my co-workers had raspy voices.  They did keep their windows shut, but even with HEPA air purifiers running, that wasn't sufficient to create a living space with clean air.  You really had to have the ability to find and seal up the drafts!

  The Wynd air quality tracker has been sold out for a long time, but it's part of another product, a personal air purifier / tracker bundle \[3\], too.

  1: [https://hellowynd.com/products/wynd-air-quality-tracker?vari...](<https://hellowynd.com/products/wynd-air-quality-tracker?variant=44077938082065>)

  2: [https://purpleair.com/](<https://purpleair.com/>)

  3: [https://hellowynd.com/products/wynd?variant\=25232063299](<https://hellowynd.com/products/wynd?variant=25232063299>)

  - **BHSPitMonkey** · [2023-08-20 16:27 UTC](https://news.ycombinator.com/item?id=37200607)
    Most living spaces (especially in older homes) rely on those "leaky" spots unless they are mechanically ventilated. It can be detrimental/dangerous to make a house perfectly sealed if it wasn't designed for it. ^c37200607

  - **kortilla** · [2023-08-20 06:52 UTC](https://news.ycombinator.com/item?id=37196831)
    Their voices weren’t raspy, you just had brain damage from too much carbon dioxide ^c37196831

    - **stavros** · [2023-08-20 13:48 UTC](https://news.ycombinator.com/item?id=37199103)
      You mean monoxide? You can feel too much dioxide. ^c37199103

- **yannvon** · [2023-08-20 08:41 UTC](https://news.ycombinator.com/item?id=37197271)
  I received a free PCB from AirGradient a few years back, and am very happy with it. The only thing I was surprised by, was that by default the Arduino code asks for WiFi connection and then sends the collected data back to AirGradient. ^c37197271

  - **FirmwareBurner** · [2023-08-20 08:54 UTC](https://news.ycombinator.com/item?id=37197331)
    *\>The only thing I was surprised by, was that by default the Arduino code asks for WiFi connection and then sends the collected data back to AirGradient.* ^c37197331

    That sounds absolutely terrible. This behavior should be shamed.

    - **ahaucnx** · [2023-08-20 09:01 UTC](https://news.ycombinator.com/item?id=37197368)
      I think there is a misunderstanding here. The product and firmware is fully open source. We just prepopulated the endpoint with our server as many people want to use our dashboard. However you can just change the endpoint to your own server or flash ESPHome on it and it will not send anything to us. ^c37197368

      - **stavros** · [2023-08-20 13:49 UTC](https://news.ycombinator.com/item?id=37199116)
        As a consumer who hasn't tried your product, that sounds reasonable to me. I can always change to my own server if I want, but having a third party server as default for convenience is useful as well. ^c37199116

        EDIT: If you create an open API with worldwide air quality data, that would be fantastic.

        - **ahaucnx** · [2023-08-20 17:32 UTC](https://news.ycombinator.com/item?id=37201213)
          We have a partnership with openAQ and share the public outdoor data with them automatically. ^c37201213

- **infogulch** · [2023-08-20 03:27 UTC](https://news.ycombinator.com/item?id=37195810)
  I got the pro kit and it really is very easy to assemble. I want to connect it to my HomeAssistant server but apparently that requires manual configuration (firmware update? just config change? I'm not sure) by plugging it into the HA server directly. It does have a web portal but apparently that goes away once you give it your WiFi password. I wish I could configure it from the web interface instead of being funneled to the cloud service which I reject on principle. ^c37195810

  - **ahaucnx** · [2023-08-20 03:34 UTC](https://news.ycombinator.com/item?id=37195852)
    You can connect the monitor directly to your home assistant. Many people do this and use ESPHome with the AirGradient configuration file \[1\]. ^c37195852

    \[1\] [https://devices.esphome.io/devices/AirGradient-DIY](<https://devices.esphome.io/devices/AirGradient-DIY>)

    The only thing you need to do is flash the D1 mini with ESPHome. Feel free to reach out to me if you need any support.

  - **xvfLJfx9** · [2023-08-20 09:56 UTC](https://news.ycombinator.com/item?id=37197671)
    I still think it would be so much better if they have a version that uses ZigBee for data exchange.
    Lower battery usage, and no need to worry that someone gets your WiFi password when they steal the device. ^c37197671

    - **stavros** · [2023-08-20 13:50 UTC](https://news.ycombinator.com/item?id=37199126)
      I do love Zigbee, but AFAIK the ESP32 chops with support are still in beta. I hope it will be stabilized soon, as I would love an explosion of compatible Zigbee devices. ^c37199126

    - **infogulch** · [2023-08-20 12:44 UTC](https://news.ycombinator.com/item?id=37198562)
      Agreed, ZigBee is great. ^c37198562

- **gr33nman** · [2023-08-27 15:45 UTC](https://news.ycombinator.com/item?id=37283761)
  Excited to learn about this. From my limited research, metal oxide VOC sensors are not very accurate due to sensor drift, instability, and cross sensitivity to temperature, humidity and inorganic gases. ^c37283761

  How do you manage this and did you consider using an electrochemical or photoionization sensor?

- **unknown** · [2023-08-20 03:08 UTC](https://news.ycombinator.com/item?id=37195703)
  [deleted] ^c37195703

- **Havoc** · [2023-08-20 08:55 UTC](https://news.ycombinator.com/item?id=37197332)
  Keep in mind that auto calibration generally requires exposure to outside air so best to keep it near somewhere where you can open a windows. ^c37197332

- **ghostpepper** · [2023-08-21 01:14 UTC](https://news.ycombinator.com/item?id=37204436)
  It's too bad their shipping lead time is 6+ weeks, this looks like a nice open-source competitor to PurpleAir. ^c37204436

  \> We currently ship approximately 1-3 weeks after receipt of payments. Delivery takes 2-3 weeks to most destinations (North America, Europe, Australia).

- **user3939382** · [2023-08-20 06:27 UTC](https://news.ycombinator.com/item?id=37196716)
  Aqara has a PM2 sensor that connects to HomeKit too FYI, it’s gotten a handful of firmware updates too so it’s reasonably mature/stable. ^c37196716

  - **gerogerke** · [2023-08-20 14:20 UTC](https://news.ycombinator.com/item?id=37199396)
    I have a IKEA Vindstyrka running in my Home Assistant, which reports PM2.5 and a proprietary VOC value from the sensor manufacturer. For 40€ + ZigBee / HA Setup quite reasonable as well. ^c37199396

