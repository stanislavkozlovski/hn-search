# [Are Our Articles Disguised Ads?](https://news.ycombinator.com/item?id=37669965)

Article: [https://www.airgradient.com/blog/are-our-articles-disguised-ads/](<https://www.airgradient.com/blog/are-our-articles-disguised-ads/>)

ahaucnx · 2023-09-27 04:07 UTC · 7 reported comments · archived 2026-11-08 13:14 UTC
Observation: 2026-11-08 13:14 UTC → 2026-11-08 13:14 UTC

## Comments

- **geerlingguy** · [2023-09-27 04:28 UTC](https://news.ycombinator.com/item?id=37670140)
  I think there's a massive difference between spam and companies that align with the hacker ethos submitting their own content. ^c37670140

  Though I've been dinged in the past for submitting my own content, I still think HN has a decent track record of flagging down blatant spam. I love what airgradient has done with their hardware, and am planning on buying a few of their units for a new office space, integrating them with local Home Assistant.

  With other vendors like AirThings, it's not as easy and requires apps and accounts to get things tracked. The simplicity is nice, but these are devices with sometimes sensitive environmental data, I'd rather control that data and do the harder work of setting it up custom one time.

  - **korse** · [2023-09-27 14:30 UTC](https://news.ycombinator.com/item?id=37675187)
    This response reads like a paid promotion. ^c37675187

    - **geerlingguy** · [2023-09-28 07:40 UTC](https://news.ycombinator.com/item?id=37686532)
      It is not. ^c37686532

- **ahaucnx** · [2023-09-27 04:25 UTC](https://news.ycombinator.com/item?id=37670108)
  I wrote this in response to a comment in yesterday's discussion \[1\]. It would be great to hear some thoughts and feedback. ^c37670108

  \[1\] [https://news.ycombinator.com/item?id\=37652832](<https://news.ycombinator.com/item?id=37652832>)

  - **verdverm** · [2023-09-27 06:10 UTC](https://news.ycombinator.com/item?id=37670800)
    I think you're generally the right type of project & company to do well on HN, and your submission history backs that up, many highly upvoted and commented posts. This post is a great reflection piece, definitely in the spirit of HN! ^c37670800

    Some titles are on the line of being too click baity for HN, but for the most part, LGTM. There is often more than zero, but still a minority, of HNers that will have a take like you are worried about. My advice would be to listen and learn like you have, but don't dwell on it.

    nit: It's "Hacker News" not "Hackernews"

    \---

    it would be great to see more hands on, code containing (even repos), based content

    - **ahaucnx** · [2023-09-27 06:16 UTC](https://news.ycombinator.com/item?id=37670844)
      Thank you for the feedback. Very appreciated. We are actually working on an "integration" section of our website that would show code examples and link to repos that provide code samples on how to link our monitors with all kinds of different backends and data platforms. ^c37670844

  - **GOTO95** · [2023-09-27 07:35 UTC](https://news.ycombinator.com/item?id=37671370)
    \>It would be great to hear some thoughts and feedback ^c37671370

    Not sure if this is the feedback you want... but:


    ```
      <meta property="og:image" content="/images/blog/feature/">
    ```

    
    Your \<meta\> og:image is not an image.


    ```
      <img src=/images/logos/logo.svg alt=AirGradient width=160px>
      <img src=/images/logos/icon.svg alt=AirGradient width=40px>
    ```

    
    You have \<img\> tags with width set to pixels but you can only specify units in CSS, not HTML.

    Also you have loads of \</li\> tags with no start tag (duplicates?) and loads of other html errors. Yeah, I tested your page with a parser I am working on :D

