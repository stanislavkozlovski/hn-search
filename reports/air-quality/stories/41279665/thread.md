# [Air Quality Monitors Compared: AirGradient One vs. Airthings](https://news.ycombinator.com/item?id=41279665)

Article: [https://www.airgradient.com/blog/airgradient-vs-airthings/](<https://www.airgradient.com/blog/airgradient-vs-airthings/>)

ahaucnx · 2024-08-18 02:25 UTC · 56 reported comments · archived 2026-11-08 13:37 UTC
Observation: 2026-11-08 13:36 UTC → 2026-11-08 13:37 UTC

## Comments

- **strogonoff** · [2024-08-18 04:53 UTC](https://news.ycombinator.com/item?id=41280198)
  I bought IQAir AirVisual Pro (indoor), because California’s AQMD\[0\] tested it as fairly accurate (and, let’s be honest, because I have been  relying on their app). ^c41280198

  It cost more than \$400, and it lasted less than half a year.

  The unit is made of flimsy off-white plastic, has an insanely bright blue-white display that cannot be dimmed enough (not fit for the bedroom, at all),  slow menu with useless options, and (in 2024!) that  weird micro USB connector. That connector is  what broke after four  months.

  Turns out, precision is not everything.

  \[0\] Apparently, California government has a lab that tests various consumer air quality monitors and publishes results ([http://www.aqmd.gov/aq-spec/evaluations/criteria-pollutants](<http://www.aqmd.gov/aq-spec/evaluations/criteria-pollutants>)).

  Despite having dozens of evaluations, they do not seem to have tested AirGradient or Airthings or their respective sensors. I wonder if they take requests?

  - **ahaucnx** · [2024-08-18 05:23 UTC](https://news.ycombinator.com/item?id=41280291)
    The reason we did not do the AQ-Spec yet is that we are still doing a lot of research into fine tuning the accuracy of the monitor. For this we run a co-location project with more than 25 sites around the world. Here we compare the AirGradient to reference grade instruments to see exactly how they perform and which algorithms can tune them better. You can read more about this on our research page \[1\]. ^c41280291

    \[1\] [https://www.airgradient.com/research/](<https://www.airgradient.com/research/>)

  - **Urgo** · [2024-08-18 05:16 UTC](https://news.ycombinator.com/item?id=41280263)
    \> It cost more than \$400, and it lasted less than half a year. ^c41280263

    I have four of IQAir's indoor ones and one of their outdoor ones. I got the first one probably 8 or 9 years ago but the others maybe 3 or 4 years ago.  The original one was made before iqair bought airvisual.  They all are working fine currently.

    Also, for the indoor ones, you can set DND mode (I forget the exact name they use) and it'll turn off the display during the night. Does have one downside I'll cover in a sec though.

    That said, until this year I always just used their website to view the data or the app. It worked.. ok. But their graphs were tiny and not very easy to use. So this year I started digging in deeper and set tried to connect things to grafana. The indoor units have a samba share where you can pull down data, but the issue is they only update that data every 5-15 minutes (15 when its in DND mode).

    The outdoor unit does NOT have a samba share.  You need to use their API for that.  Now this is where I'm really unhappy and eventually looking at AirGradient or some other option. In order to get api access to my data on the outdoor unit I either need to pay (a lot, I forget how much) for api access, or I can get free api access if I allow iqair to sell my data to everyone else.

    .. not interested in that

    So I'm currently only getting data from my indoor units and only getting every \~5-15 min data points.. but they are working.  I did invest a lot in these devices so  not ready to upgrade to anything different just yet, but every time I see one of these air quality topics pop up here on HN it really makes me want to change.

    - **strogonoff** · [2024-08-18 07:49 UTC](https://news.ycombinator.com/item?id=41280839)
      I am sure the sensor is fine and the weird USB port can be fixed (though it looked like they do not make it easy to disassemble the body). However, the device is just so janky and unpleasant to use I am not sure I want to go through the trouble. I started looking at Airthings, though I was recommended AirGradient as well. ^c41280839

      \> until this year I always just used their website to view the data or the app

      Never used their app to check my own unit. My apartment is small. I am here in this room, the device is right here in this room, would I want to go fetch my phone to know the readings?

      \> Also, for the indoor ones, you can set DND mode (I forget the exact name they use) and it'll turn off the display during the night

      Of course, but it means it should be within reach to turn on and it will blast blue light in my face should I want to check it at night. An e-ink screen would work best, considering low refresh rate is not an issue in this scenario.

      - **Urgo** · [2024-08-18 14:51 UTC](https://news.ycombinator.com/item?id=41282713)
        \> Of course, but it means it should be within reach to turn on and it will blast blue light in my face should I want to check it at night. An e-ink screen would work best, considering low refresh rate is not an issue in this scenario. ^c41282713

        You can set a schedule. Mine automatically go into DND mode a little before bedtime and turn off after the sun is up.

        - **strogonoff** · [2024-08-19 01:57 UTC](https://news.ycombinator.com/item?id=41287148)
          Would you have a clock that requires being turned off at night, because it has an unbearably bright screen? ^c41287148

          I personally don’t want to fumble through DnD mode whenever I thought to take a glance at carbon dioxide or PM2.5 while it’s dark outside.

          There is only one thing I need from it, and that is to show air quality measurements in a non-painful way. Sadly, AirVisual Pro does not do that well for me.

  - **unknown** · [2024-08-18 08:20 UTC](https://news.ycombinator.com/item?id=41280963)
    [deleted] ^c41280963

- **ziml77** · [2024-08-18 04:36 UTC](https://news.ycombinator.com/item?id=41280155)
  I just got my AirGradient Ones a couple weeks ago. It was quite nice that I was able to set them up local-only with absolutely no fuss. Works wonderfully with Home Assistant. ^c41280155

  Also it was definitely worth saving money going with the DIY version. All that they leave for you is final assembly: plugging in 3 modules and wrenching down 4 self-tapping screws.

  - **anotherhue** · [2024-08-18 04:53 UTC](https://news.ycombinator.com/item?id=41280199)
    I had the same experience, and honestly was hoping for more work to do. ^c41280199

    90 seconds to assemble and it was auto discovered by home assistant in even less time.

    That said, it's probably overkill for a device whose only 'real' purpose is to tell you when to open your window. Sensible people can get a cheap CO2 meter for \$30 that will be accurate enough for that purpose.

    - **ahaucnx** · [2024-08-18 05:17 UTC](https://news.ycombinator.com/item?id=41280268)
      We used to have a DIY version that required soldering but the problem was that a number of people overestimated their soldering skills and couldn't get it done. Then obviously that is frustrating for them. So we discontinued it for now. I would love to bring back a more "advanced" version in the future. ^c41280268

      - **ploxiln** · [2024-08-18 08:41 UTC](https://news.ycombinator.com/item?id=41281046)
        I'm sad to hear that the DIY Basic is "discontinued for now", rather than just "out of stock". I built mine about a year ago and I'm quite happy with it. (I later got the "ONE indoor kit" for my parents, since it has a nicer case included.) But I understand if the customer support (and PR ...) were too difficult to deal with for this particular offering. ^c41281046

        It is rather open hardware... I notice now there are "gerbers" of the DIY basic PCB that you make available, so I should be able to order PCBs from PCBWay or JLC-PCB, and the other sensors and parts directly from you or from AliExpress. Though if not for that DIY Basic kit you offered before, I'd consider the project a bit risky for my level of design/part-sourcing. So, thanks!

        - **ahaucnx** · [2024-08-18 08:46 UTC](https://news.ycombinator.com/item?id=41281066)
          The DIY basic will be back in stock soon. What we discontinued is the DIY pro that was the larger unit but to be soldered. ^c41281066

          - **ploxiln** · [2024-08-18 15:59 UTC](https://news.ycombinator.com/item?id=41283132)
            Oh ok, sounds great. (... I did solder the pin headers and PM-sensor cable connector on my DIY basic, which was fun, but I still think it's a great option even if only available pre-soldered.) ^c41283132

  - **illiac786** · [2024-08-18 09:43 UTC](https://news.ycombinator.com/item?id=41281290)
    You’re forgetting the lab testing. The pre-assembled one has been tested to meet specific standards, something I will never be able to do at home. ^c41281290

    - **ziml77** · [2024-08-18 16:26 UTC](https://news.ycombinator.com/item?id=41283298)
      True, though I have to believe that the line the sensors themselves are coming off of has QC to ensure they the batches seem to be operating within spec. ^c41283298

      And I knew I wasn't getting the full factory testing, but for a home installation I am not worried about that. If the values happen to be a bit off, it's no big deal.

  - **etrautmann** · [2024-08-18 07:37 UTC](https://news.ycombinator.com/item?id=41280797)
    Thanks for the rec, decided to try it out based on your comment. ^c41280797

- **sxp** · [2024-08-18 03:51 UTC](https://news.ycombinator.com/item?id=41280005)
  What do the two ownerships clauses (quoted below) mean in practice? It's unlikely AirThings will come after me if I download all the data from my sensors and post them online. And is there any evidence that they've gone after people who have created open source interfaces to their APIs? It sounds like their lawyers just wrote aggressive clauses into their contracts to cover their asses in case they are acquired or want to utilize the data in other ways. ^c41280005

  \> In 15.4. of Airthings T&C it writes: “We own and shall retain ownership of all rights to all data and information collected via the Services provided to you…"

  \> Furthermore, in 15.2 Airthings claims all rights for modifications that you might carry out on the Airthings monitor: “You hereby assign to Airthings all right, title, and interest (including Intellectual Property Rights) that you may have in any custom developments, modifications, or derivative works of the Services and Products created or developed by or for you, including but not limited to design, artwork, technology, software, data, functionality, and documentation."

  - **ahaucnx** · [2024-08-18 04:03 UTC](https://news.ycombinator.com/item?id=41280038)
    Achim from AirGradient here. You raise an excellent point. ^c41280038

    Often T&C are indeed just written by lawyers and potentially not being enforced at all.

    However, it really does restrict what you can do with the monitors in practical ways.

    Let's say you want to build a business around using AirThings monitors with your own dashboard analysing the data and giving value added services. If you don't officially own the data, are you actually allowed to use it and monetize it for your own purposes?

    With these T&Cs and if you do this (and I actually know a few companies that do exactly that) you open a legal liability that AirThings could come after you.

  - **sliken** · [2024-08-20 07:12 UTC](https://news.ycombinator.com/item?id=41297591)
    If you don't want airthings to own your data, do not upload it to them. ^c41297591

    Airthings has a git repo allowing you to read your own data, keep it inside your network, and graph it with graphana or anything you want.

    However if you use their free, er, no charge service to view your data, then they own what they upload.

    If you want to own your data, buy the airthings, don't use their service, and do anything you want with your data.

- **mbStavola** · [2024-08-18 03:43 UTC](https://news.ycombinator.com/item?id=41279986)
  I plan to pick up some AirGradient units and phase out my AirThings devices simply because I want to keep all my data local and open. However, I do wish 1) it could monitor Radon and 2) had a PoE powered sku. ^c41279986

  - **ahaucnx** · [2024-08-18 04:13 UTC](https://news.ycombinator.com/item?id=41280079)
    Yes, these things have come up quite a few times. Regarding Radon there are unfortunately no 3rd party sensor modules available that we know off (and are reasonably priced). If you know any, please let us know. ^c41280079

    Regarding PoE, we have made a survey some time ago and less than 5\% of the users were interested in PoE. However, the hardware integration is not straight forward and it would increase the price of the unit for all customers. This is the main reason we did not do it yet.

    However our open hardware has an extension plug and this could be an excellent community project for somebody to develop this as an extension card and then share the design.

    - **xoa** · [2024-08-18 11:45 UTC](https://news.ycombinator.com/item?id=41281749)
      So fully recognizing upfront my own bias towards this feature, and that lack of immediate interest makes something a business risk regardless of how it might turn out over time. Still, just 2 cents towards the long term: ^c41281749

      \>*Regarding PoE, we have made a survey some time ago and less than 5\% of the users were interested in PoE*

      1\. I'm not sure surveys are that useful for features a lot of users aren't aware of or might have outdated views on. I think a better survey would be on whether users wanted ethernet at all, because that's the only real differentiator there in an age where a basic PoE+ switch can be had for \$55. If it's already going to be on a hardline, then having it be powered that way too is ultra useful and zero extra work. Ethernet is also something people can do without being electricians. There is a bit of chicken/egg challenge with features like that where not many people know because there isn't much stuff.

      2\. I hope you're normalizing to some degree for purchase volume. 5\% of customers isn't the same as 5\% of sales.

      That said I certainly wouldn't want to see you face any challenges over something like that and your reasons are fair enough. It is just a bit of a bummer to not have more options on that front. But the native HA integration added back in June with no firmware flash already sold me on a bunch of AirGradients anyway and was much more important! Thank you so much for that.

      - **ahaucnx** · [2024-08-18 12:59 UTC](https://news.ycombinator.com/item?id=41282123)
        I am not ruling it out in the long term. I actually also would love to have a wired Ethernet connection and if we grow further we might very well come to the point where the 5\% really matter and we have more resources available to develop it. ^c41282123

  - **sliken** · [2024-08-20 07:14 UTC](https://news.ycombinator.com/item?id=41297607)
    Why not just use Airthings, don't use their service, and own your data. ^c41297607

    They say in the license if you use their service (i.e. you upload your data to them) they own it.  But if you don't, you own it.  Seems fair to give them their data if they are going to store it for you and provide you an app and website to view it.

    They publish a github repo to let you download direct from airthings (not using anything cloud) and graph it with graphana or whatever you want.

    - **mbStavola** · [2024-08-21 17:43 UTC](https://news.ycombinator.com/item?id=41312470)
      This isn't the case for their newer products afaict-- with the ViewPlus (which is what I have) you \_must\_ go through their cloud offering in order to get your data. ^c41312470

      I do not want to roundtrip for something that shouldn't have left my house in the first place. Their older products allowed me to keep it local, why shouldn't their newer ones?

- **felixtany** · [2024-08-18 03:48 UTC](https://news.ycombinator.com/item?id=41280000)
  After spending a decent amount on Sensibo equipment and finding its accuracy is laughably bad, I did a heap of research into PurpleAir and the other sensors on the market. I already had a couple of Aranet4 devices and wanted the same high level of accuracy they provided - and so it was really down to PurpleAir or AirGradient given the SenseAir and Planter sensors. I'd say clinched my decision - and I dropped quite a bit of money on 2 outdoors and 4 indoors, split between me and a friend. ^c41280000

  Why didn't I do with PurpleAir?
  \- The order above with AirGradient was about USD\$800 (for kit form devices, excluding freight). PurpleAir for the same models is USD\$1774.
  \- PurpleAir seemed to require a Google login to put the devices on a map, and I don't like the big-vendor-lock-in.
  \- Browsing the AirGradient forums, Achim (the founder) is really involved, and the open-source nature of the platform appealed.

  For a (what appears to me to be, anyway!) small organisation, the quality and deliverable of the AirGradient system is exceptional. The equipment looks professional, joining it to the AirGradient dashboard is surprisingly easy, and the dashboard itself is really slick. It's fast, it works as direct icon on my iPhone, and does it's job (giving me key info) really well.

  In saying all that, I'd better clarify I'm getting nothing out of this glowing review! I just love it when tech works well, as it should, and when it does it should be recognised and supported.

- **lrhegeba** · [2024-08-18 12:30 UTC](https://news.ycombinator.com/item?id=41281953)
  Am very satisified with [https://en.air-q.com/funktionen/air-q-science-option](<https://en.air-q.com/funktionen/air-q-science-option>) that offers a lot of sensors ([https://en.air-q.com/messwerte](<https://en.air-q.com/messwerte>)). Good UI, API-accessible and integration in HA works just fine. Rather pricey though, depending how many sensors you choose. ^c41281953

- **haswell** · [2024-08-18 13:17 UTC](https://news.ycombinator.com/item?id=41282206)
  I appreciate that AirGradient has open source products, but the company repeatedly posting its own content here is starting to feel increasingly spammy. ^c41282206

  Air quality is a hot topic here so the posts often succeed, but why does this product hold so much sway with this community? Genuine question.

  Most companies self-promoting their own “we’re better than X competitor” content are not so well received. Am I missing some context/history, or are people just really happy with their AirGradient gear?

  - **ahaucnx** · [2024-08-18 13:52 UTC](https://news.ycombinator.com/item?id=41282394)
    Achim Founder of AirGradient here. Yes, I'm curious about this too. ^c41282394

    Could you clarify what exactly in this post you think is spammy?

    We do try to write interesting and informative blog posts and also highlight important aspects that are not that generally known. Like in this article the data ownership issue of the AirThings.

    In fact as part of our open-source philosophy we also see our responsibility creating awareness and informing about these things.

    Why shouldn't we then try and distribute these posts to for example hacker news?

    The posts only get traction if people like the content and upvote it. What's wrong with that?

    - **haswell** · [2024-08-18 14:51 UTC](https://news.ycombinator.com/item?id=41282712)
      \> *Could you clarify what exactly in this post you think is spammy?* ^c41282712

      In just the last 12 months, you’ve submitted your own domain 26 times. When you’re not submitting your own domain, you’re almost universally submitting content about your product.

      Self promotion is directly addressed in the site guidelines.

      \> *Please don't use HN primarily for promotion. It's ok to post your own stuff part of the time, but the primary use of the site should be for curiosity.*

      While I think some of the content is actually good, my reaction is to the fact that it has increasingly felt like pure self promotion, and the data backs that up.

      \> *The posts only get traction if people like the content and upvote it. What's wrong with that?*

      See above. But for me, I’m just sharing how I feel after seeing these posts repeatedly. I’m tired of them to a degree that I felt compelled to comment about guidelines, which is something I generally try to avoid.

      If it was an organically hot topic getting submitted by dozens of different people, I’d accept it as the current buzz in the zeitgeist and move on. Because it’s all coming from one account, it feels engineered, and yes, spammy. The quality of your content isn’t enough to excuse the behavior, and the behavior is now one of the lenses through which I’m seeing your product.

      Too much of a good thing perhaps.

      - **ahaucnx** · [2024-08-18 15:10 UTC](https://news.ycombinator.com/item?id=41282830)
        You raise some good points. I will reflect on them. Thanks! ^c41282830

- **daft\_pink** · [2024-08-18 07:03 UTC](https://news.ycombinator.com/item?id=41280675)
  Why no radon on the airgradient? I’d really like a device that also prevents cancer. ^c41280675

  - **progbits** · [2024-08-18 07:46 UTC](https://news.ycombinator.com/item?id=41280830)
    I've built some DIY air quality monitors. Radon sensors are hard to find. ^c41280830

    In general from easiest to hardest:

    \- Temperature, humidity, pressure: many cheap, small and accurate sensors available.

    \- Particulate matter: many options as well though if you want good accuracy and silent fans you need to pay more.

    \- CO2: most sensors are actually just measuring other stuff (TVOC) and guessing CO2 concentration from that. You can get good true CO2 sensors from eg. Sensirion for \$30+.

    \- VOC, CO, NO, O3 and other gasses: hard to measure reliably. Most sensors are comparatively large (few small SMD MEMS types exist), are power hungry (basically a heater element) and give you a crude estimate as they react to bunch of different gasses and the output is a mix of their concentrations.

    \- Radon: basically impossible for hobbyist. If you know of any sensor module I can buy below \$100 in unit quantities please share.

    Edit: I know airgradient are not hobbyists and they probably could get some radon sensors but it is still harder than for large companies. Their product definitely has the DIY vibe (but high quality) and I really like that it is easy to recreate and source all parts for it yourself, except the custom injection mold case.

  - **scire** · [2024-08-18 12:46 UTC](https://news.ycombinator.com/item?id=41282057)
    Why not measure something like CO2 and use that as a proxy? ^c41282057

    The logic being that whenever you bring in fresh air, you decrease radon concentration.

    And a high CO2 level means you need to bring in fresh air anyway, and you incidentally also reduce radon concentration.

    I could be way off here though, happy to learn more on the topic as I don’t have experience with (dealing with) radon.

    - **daft\_pink** · [2024-08-21 14:04 UTC](https://news.ycombinator.com/item?id=41310417)
      Because Radon actually causes cancer and ventilation is expensive.  I’ve read many articles about people going nuts trying to manage CO2, but I think it’s useful to know if I’m being exposed to something that would actually result in early death as I’m more likely to take immediate action on that. ^c41310417

  - **stephenitis** · [2024-08-18 07:05 UTC](https://news.ycombinator.com/item?id=41280683)
    I agree, I'd like to go with air gradient but i need a radon sensor ^c41280683

    - **madspindel** · [2024-08-18 07:14 UTC](https://news.ycombinator.com/item?id=41280717)
      [https://aranet.com/en/home/products/aranet-radon-sensor](<https://aranet.com/en/home/products/aranet-radon-sensor>) ^c41280717

      - **daft\_pink** · [2024-08-21 14:07 UTC](https://news.ycombinator.com/item?id=41310451)
        I just want to point out that the other device being compared actually includes a radon sensor and the cost of that device would be cheaper than the airgradient plus the radon sensor. ^c41310451

    - **anotherhue** · [2024-08-18 13:23 UTC](https://news.ycombinator.com/item?id=41282243)
      You can get a cheap analogue radon sensor. As others have pointed out, even if you do detect radon the typical solution is add ventilation. ^c41282243

      Which is exactly what you do if you had a high CO2 reading.

      - **daft\_pink** · [2024-08-21 14:07 UTC](https://news.ycombinator.com/item?id=41310455)
        Do you have any links to this?  I’m very curious. ^c41310455

        - **anotherhue** · [2024-08-22 16:21 UTC](https://news.ycombinator.com/item?id=41321880)
          Just lookup radon test kit and how to deal with radon. ^c41321880

          [https://kagi.com/search?q\=radon+test+kit+&r\=us&sh\=fA8r72RApl...](<https://kagi.com/search?q=radon+test+kit+&r=us&sh=fA8r72RAplql06lpaDqDbA>)

- **Xen9** · [2024-08-18 20:07 UTC](https://news.ycombinator.com/item?id=41285017)
  I've recently realized that one can effectively cross-ventilate studio apartment by adding to their mail slots a PC-fan filtered by small HEPA-filter (to remover outdoor odors) combined with a window-attached ventilator pulling air to outdoors, possibly with a normal fan in the middle of the studio. Feel free to Kickstart this. ^c41285017

- **montjoy** · [2024-08-18 03:55 UTC](https://news.ycombinator.com/item?id=41280017)
  I have both the Airthings Wave+ and the AirGradient Pro. I like them both. The Wave+ can connect to Home Assistant just fine with Bluetooth so there’s no worry about “owning” the data etc. I didn’t care for the initial software that came with the AirGradient but it was easy enough to flash once I understood how ESPHome worked. ^c41280017

  - **ahaucnx** · [2024-08-18 04:06 UTC](https://news.ycombinator.com/item?id=41280053)
    With our latest firmware we now natively support Home Assistant and the monitors are auto discovered. So no need to flash ESPHome anymore. ^c41280053

    We also expose a local API that makes it very easy to make GET requests to the monitor within your local network and basically gives you all possibilities for easy integration.

    \[1\][https://www.airgradient.com/home-assistant/](<https://www.airgradient.com/home-assistant/>)

    \[2\][https://github.com/airgradienthq/arduino/blob/master/docs/lo...](<https://github.com/airgradienthq/arduino/blob/master/docs/local-server.md>)

- **ck2** · [2024-08-18 13:29 UTC](https://news.ycombinator.com/item?id=41282271)
  Airgradient teardowns and reports are like the Backblaze reports, always such a great service to the community. ^c41282271

  But I really wish Airgradient would get on the national US map for AQI

  PurpleAir really has a massive headstart and Google even puts Purple on googlemaps so you can't compete with that.

  I keep saying AirGradient needs to massively discount if not just give for free their monitors to all the WeatherSTEM sites in the USA which ALL do NOT have air-quality monitoring. Now -THAT- would get them on the map.

  compare

  [https://map.purpleair.com/](<https://map.purpleair.com/>)

  [https://www.airgradient.com/map/?zoom\=4](<https://www.airgradient.com/map/?zoom=4>)

  [https://www.weatherstem.com/sites](<https://www.weatherstem.com/sites>)

- **bhouston** · [2024-08-18 11:45 UTC](https://news.ycombinator.com/item?id=41281743)
  I bought this no-name CO2 monitor (can be found on Amazon and AliExpress and probably elsewhere): ^c41281743

  [https://www.aliexpress.com/item/1005006483766478.html](<https://www.aliexpress.com/item/1005006483766478.html>)

  It is \~ \$50.

  It actually works really well.  I tested it in a number of situations and it appeared to be relatively accurate.  It led me to make some ventilation changes in the house.

  I didn't need it on all the time, I just do spot checks if I think there is an issue now.  I like the portability as well.

  - **ahaucnx** · [2024-08-18 13:55 UTC](https://news.ycombinator.com/item?id=41282409)
    I had a look but it's unclear that it is an NDIR CO2 sensor. There are cheap Chinese CO2 sensors that actually do not measure CO2 but estimate it from VOCs.
     You can test this easily. Spray some Ethanol around your sensor and see if the CO2 rises a lot. If so then it's not a real CO2 sensor. ^c41282409

    - **bhouston** · [2024-08-20 01:12 UTC](https://news.ycombinator.com/item?id=41295917)
      I think it is a VOC-based estimator.  Seems to work well though in most cases. ^c41295917

- **nov21b** · [2024-08-18 06:10 UTC](https://news.ycombinator.com/item?id=41280461)
  I have the Airthings Wave+ and one thing that bugs me is the relative humidity threshold. Anything above 60\% will give a yellow led warning. If you have many indoor plants, live in a forest, or even just ventilate a lot on rainy days the sensor will show an air quality warning. I would like to take humidity out of the equation as I much rather focus on CO2, VOC and Radon. Otherwise a great sensor that was easy to integrate in my own scripts as you can easily get all sensor readings over bluetooth. ^c41280461

- **antirez** · [2024-08-18 12:30 UTC](https://news.ycombinator.com/item?id=41281954)
  The Awair Element works very well in my experience. If you check the sensors list, the sum of the cost of just the sensors (that are very high quality ones) will match the total cost of the device. And the software and the design are great as well. ^c41281954

- **emmanuel\_1234** · [2024-08-18 13:04 UTC](https://news.ycombinator.com/item?id=41282132)
  I unplugged my AirGradient a couple days ago. It's quite the useless piece. ^c41282132

  The CO2 sensor does not read CO2 levels, and recalibrates automagically. I have completely wacky readings from it, from 200ppm to 2000ppm.

  The VOC sensor also apparently does not read VOC levels, see discussion here: [https://forum.airgradient.com/t/measurement-values-for-the-a...](<https://forum.airgradient.com/t/measurement-values-for-the-airgradient-one-tvoc-readings/1027/12>).

  All in all, I'm frustrated I fell for the regular free advertising they get on HN.

  - **ahaucnx** · [2024-08-18 13:44 UTC](https://news.ycombinator.com/item?id=41282352)
    Achim from AirGradient here. ^c41282352

    I'm often personally going on Zoom call with customers to make sure they get 100\% out of the monitor and address these types of questions. Please send me a note through our support form and I'm happy to help \[1\]. Please make a note in the support ticket to this link so that it will get assigned right to me.

    Now regarding the CO2 sensor. We use the SenseAir S8 which is one of the best NDIR sensors out there. If you do not like the auto calibration, you can now switch this off in the dashboard or change the automatic baseline calibration to longer periods. To do this, go to Place Settings, General Place Settings.

    In case you still have these wild swings, contact our support with your sensor ID and we will have a look.

    Regarding VOC, this has also recently addressed and you can now change the learning gain offset to make it more behave like an absolute sensor. We clearly describe the behavior of the VOC sensor on our website and this is actually the behavior of all newer generations of VOC sensors. We use the Sensirion SGP41 which is regarded one of the best ones.

    Now, you are free to call it a "useless piece" but I'd appreciate if we keep the discussion fact based. As far as I know, there is no other air quality monitor in the same price range that is substantially better than ours.

    Measuring air quality pollutants is not as simple as measuring temperature so there are inherent shortcoming in some of them. It is part of our mission to educate people on these. This is why we published for example the air quality cheatsheet. \[2\]

    \[1\] [https://www.airgradient.com/support/](<https://www.airgradient.com/support/>)

    \[2\] [https://www.airgradient.com/documents/infographics/AQ-Monito...](<https://www.airgradient.com/documents/infographics/AQ-Monitor-Cheatsheet.pdf>)

  - **rssoconnor** · [2024-08-18 14:51 UTC](https://news.ycombinator.com/item?id=41282714)
    I bought a pair of sensors based on the HN mentions, and so far I'm pretty happy.  I was mainly interested in their PM sensor, which isn't on your list of complaints, and works quite well. ^c41282714

    I discovered my rangehood, which doesn't have an outdoor exhaust, is even more useless than I had imagined.  I bought a HEPA filter for my kitchen to run while I'm cooking (a Blueair based on other HN comments) and based on the PM sensor readings of the AirGradient the HEPA filter is quite effective.

    I did have to configure the CO₂ sensor recalibration period to keep the numbers sensible.  It wasn't so easy to set different recalibration periods for the indoor and outdoor sensors, but with some curl commands, I was able to get things configured to my liking.  I do appreciate that, in principle, I can edit the firmware to my liking in the future.

- **eisa01** · [2024-08-18 08:24 UTC](https://news.ycombinator.com/item?id=41280982)
  The batteries in the AirThings View Plus are nice, as you can bring it with you on vacation. There’s quite some variety in indoor air quality! ^c41280982

- **chomp** · [2024-08-18 04:13 UTC](https://news.ycombinator.com/item?id=41280083)
  I just got a pi zero w and a adafruit spg30. Not perfect, but good enough, I own the data, and I send it to grafana for alerting. ^c41280083

  - **oloapiu** · [2024-08-18 08:32 UTC](https://news.ycombinator.com/item?id=41281014)
    Yeah all these consumer-grade air quality sensors are nothing more than a Sensirion SPS30 or a Plantower PMS5003 and a Wi-Fi module in a box. ^c41281014

    To get more than just that you need to look at professional-grade indicative AQ sensors such as [https://clarity.io/](<https://clarity.io/>) and [https://www.aeroqual.com/](<https://www.aeroqual.com/>)

    These are what government agencies and municipalities use for dense sensor networks. E.g. [https://www.breathelondon.org/](<https://www.breathelondon.org/>)

    - **ahaucnx** · [2024-08-18 15:20 UTC](https://news.ycombinator.com/item?id=41282886)
      The clarity also uses the Plantower sensor. A high price does not necessarily mean better sensor modules. ^c41282886

- **gjs278** · [2024-08-18 06:09 UTC](https://news.ycombinator.com/item?id=41280457)
  [flagged] ^c41280457

  \[dead\]

