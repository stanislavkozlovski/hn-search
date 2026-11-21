# [Show HN: DIY 80€ 3D Printer Basement Ventilation](https://news.ycombinator.com/item?id=42349574)

Article: [https://hajo.me/blog/2024/12/07/diy-80eur-3d-printer-basement-ventilation/](<https://hajo.me/blog/2024/12/07/diy-80eur-3d-printer-basement-ventilation/>)

fxtentacle · 2024-12-07 13:10 UTC · 23 reported comments · archived 2026-11-08 13:41 UTC
Observation: 2026-11-08 13:40 UTC → 2026-11-08 13:41 UTC

## Comments

- **iLoveOncall** · [2024-12-10 22:56 UTC](https://news.ycombinator.com/item?id=42382627)
  This is by far not enough for a resin printer. You need an enclosure and to vent out the air much faster. ^c42382627

  That said, it doesn't have to be more expensive. I bought a 30€ inline bathroom fan, 8€ of tubing, and a 40€ cabinet from Ikea.

  From there I cut a hole on the side of the cabinet, 3D print a "liner" to attach the tubing to the hole and vent it out through a 3D printed cover with a vent hole where I attached the rest of the tubing.

  It is much much safer and vastly more efficient, while remaining affordable. The main advantage is that this is also suitable in an apartment without basement since the fan is much more powerful, and looks a lot better for a room which is not supposed to look like a basement.

  Here's a guide I recommend: [https://www.asianjoyco.com/resources-tutorials/ventilation-u...](<https://www.asianjoyco.com/resources-tutorials/ventilation-upgrades-for-3d-resin-printing>)

  The author here seems extremely ignorant regarding the risks of 3D printing with resin. You must wear full PPE including a respirator at all times when working with resin, even if you don't smell anything.

  - **fxtentacle** · [2024-12-12 09:08 UTC](https://news.ycombinator.com/item?id=42397541)
    Author here. I fully agree with you that cheap Chinese resin should never be used in a living area, not even with my improvised ventilation. That's why I said in the first paragraph to "never use \[China resin\] outside a ventilated factory". That said, I now switched to using locally produced resin which is intended for dentists and is biocompatible (when hardened) and certified for indoor use and only has a class 1 warning level, telling you not to drink it or pour it down the drain. (As opposed to level 3 aerial lung damage with Anycubic resin.) It's quite expensive, but in my case that is tolerable. ^c42397541

    And I believe this issue is not black and white. For most people who currently have no ventilation system at all, just adding something like mine will already be a huge improvement. Your article looks great and I agree that that might be even better, but it was not possible in my case:

    I did not have any way to properly attach an exhaust, which is why I needed to use a solution that works with the existing window. And when I go on vacation, I need to close that window for insurance reasons. So I needed something that was easily removable, too.

    Also, I sometimes work with Epoxy glue and Acrylic paint and I solder electronics and I wanted to make sure that the exhaust will cover these use-cases, too. That said, I think the best solution would be to combine your article and my window cover. I could probably connect a tube from the active coal filter port on my GKtwo directly to one of those fans. That way, it'd be sucking 25\% of the airflow through the resin printer and the remaining 75\% from the ambient air in the room.

    And yes, I wear gloves, goggles, and respirator every time I handle resin. I thought that part was common knowledge, which is why I did not explicitly mention it.

  - **postit** · [2024-12-10 23:01 UTC](https://news.ycombinator.com/item?id=42382672)
    I’ve build a similar setup recently. My partner even got excited thinking I’d finally start growing only to be disappointed when I explained what I was doing. ^c42382672

  - **Symbiote** · [2024-12-10 23:29 UTC](https://news.ycombinator.com/item?id=42382890)
    There's no way I'd have a resin printer in an apartment. ^c42382890

    What's your plan when you spill resin on the floor?

    - **iLoveOncall** · [2024-12-11 00:13 UTC](https://news.ycombinator.com/item?id=42383208)
      Ignoring the fact that there's no way I can spill resin on the floor with my current printing / curing setup, I would just wipe most of it off with paper towels, then clean with water (or IPA but I use water-washable resin), and then if really needed I would cure it and scrape it off. ^c42383208

      I don't have a single drop of resin anywhere on the desk where I take care of prints, so it's not that hard.

      Note that it's in a room that I dedicate as my workshop, so I'm the only one that goes in and only for DYI purpose (and rarely).

      - **Ruthalas** · [2024-12-11 23:03 UTC](https://news.ycombinator.com/item?id=42394030)
        Parent may be imagining a carpeted apartment, which would make cleanup more difficult. ^c42394030

        When I was in such a location I used silicone project mats with raised edges fastidiously to avoid ever dripping on the carpet.

        - **iLoveOncall** · [2024-12-12 08:59 UTC](https://news.ycombinator.com/item?id=42397491)
          Yes that's what I was thinking of after leaving my own comment, but it's a lot less common outside of the US. I have wooden floors. ^c42397491

          Otherwise I would definitely either avoid it entirely or cover the whole floor area one way or another.

        - **Symbiote** · [2024-12-12 10:31 UTC](https://news.ycombinator.com/item?id=42397989)
          Carpet or cracks between wooden floor planks, plus the fumes from the spill will then be in the room and need ventilating. ^c42397989

          When I was briefly considering buying a resin printer, I was horrified by the comments on Reddit from teenagers who were printing D&D figures in their bedrooms, handling spills by rubbing them into the carpet, or assuming "low odour" meant "safe".  In these discussions, comments from a chemist who claimed to work for a company producing the resin were downvoted, they didn't want to know.

          "Well, I'll be careful" generally isn't an adequate safety precaution in industry or academia.

- **zactato** · [2024-12-10 23:08 UTC](https://news.ycombinator.com/item?id=42382725)
  I just ordered by first 3D printer, I'm not normally sensitive to air quality issues, but my partner is, so I spent some time doing some research on the issue. ^c42382725

  It's amazing how many people believe "if you can't smell it, there's no problem" and quite incorrectly assume that things like PLA won't hurt them. Surely minimal exposure is fine, but 3d printers run over many hour periods and those VOCs can build up.

  I decided to be safe and bought a basic fabric enclosure with an exhaust fan that vents to the outdoors. It's probably not perfect, but maintaining negative pressure inside the enclosure should remove most particulates. I wouldnt handle bromine in it.

  I'm worried about all the folks running print farms in their house with minimal ventilation.

  - **iLoveOncall** · [2024-12-10 23:11 UTC](https://news.ycombinator.com/item?id=42382748)
    And you're talking about an FDM printer but the author talks about resin printers which are hundreds of times more harmful. ^c42382748

    That said fabric enclosure with something that goes up to 250 degrees Celsius isn't the best idea. There are fireproof 3D printing enclosures.

    - **ofrzeta** · [2024-12-11 03:17 UTC](https://news.ycombinator.com/item?id=42384372)
      I recently learned that now there's some kind of "bio resin" that seems to be less toxic. So maybe that would be ok? ^c42384372

      - **fxtentacle** · [2024-12-12 07:14 UTC](https://news.ycombinator.com/item?id=42396957)
        A lot of the so-called "water washable" bio resins need to be diluted down to 1L of resin + 1 million L of clean water before they are considered safe enough that you're allowed to flush them down the toilet. So I would never touch them without gloves. ^c42396957

        And while you are correct that some plant-based resins are not a class 3 lung poison anymore, they are still a class 2 eye irritant and can cause burns in your eyes purely through aerial exposure. Which means you need to wear goggles whenever you're in the same room.

      - **terribleperson** · [2024-12-11 04:54 UTC](https://news.ycombinator.com/item?id=42384922)
        I doubt it's any safer. Things that UV cure tend not to be nice. ^c42384922

        - **ofrzeta** · [2024-12-11 09:45 UTC](https://news.ycombinator.com/item?id=42386290)
          Hm, they say it's safe for children's toys, according to some certification: ^c42386290

          [https://store.anycubic.com/collections/uv-resin/products/bio...](<https://store.anycubic.com/collections/uv-resin/products/bio-resin>)

          - **fxtentacle** · [2024-12-12 07:17 UTC](https://news.ycombinator.com/item?id=42396972)
            It's similar to 2 component epoxy: The raw materials are highly poisonous, but the reaction end product is safe. It's just that you need to be 100\% sure that there are no un-reacted resin leftovers anywhere on your part. And that part is very difficult. ^c42396972

          - **iLoveOncall** · [2024-12-11 09:58 UTC](https://news.ycombinator.com/item?id=42386361)
            Once it's cured maybe, that doesn't mean it's at all safe until then. ^c42386361

    - **manfre** · [2024-12-11 13:24 UTC](https://news.ycombinator.com/item?id=42387436)
      The nozzle will hit that temp, but air temp will be much closer to room temp. A porous and poorly insulated fabric enclosure will probably not add more than 10 C temp increase. ^c42387436

      - **iLoveOncall** · [2024-12-11 17:36 UTC](https://news.ycombinator.com/item?id=42390360)
        Air temperature is not the issue and is not how 3D printers catch on fire, I should have clarified in my previous comment. ^c42390360

        Nozzle clogs can happen frequently, and if left unmonitored, can quickly turn into a disaster. If your nozzle is clogged it can essentially destroy your printer and cause an electrical fault that can set the printer on fire.

        Printer fires are a lot less frequent in recent years than a decade ago, but it can still definitely happen.

        - **Doxin** · [2024-12-12 13:23 UTC](https://news.ycombinator.com/item?id=42398911)
          A nozzle clog won't set a 3d printer on fire either. It'll make a good mess of the hot-end. There'll be a bunch of charred filament, and heat creep will clog the nozzle nicely. It won't however magically get any hotter than it does while printing with an unclogged nozzle. ^c42398911

          What *does* cause fires is failed thermistors. These days most firmware will detect unreasonably high or unreasonably low temperature readings and turn off the heaters. You thermistor can still however fail with a reasonable reading if you're very unlucky.

          Another factor is MOSFET failure. MOSFETs have a failure mode where they can fail closed. This can turn a heater on permanently. Modern firmwares will detect the temperature going unreasonably high, but most hardware is not set up such that the firmware can do much about it.

- **ryandetzel** · [2024-12-10 23:11 UTC](https://news.ycombinator.com/item?id=42382746)
  The problem for me is it's 23 degrees f outside so if I vent outside I'm losing money ^c42382746

  - **beala** · [2024-12-11 01:44 UTC](https://news.ycombinator.com/item?id=42383821)
    Not sure why you're getting down voted. If you're venting air outside, that air must get replaced with other air. Unless you have a fancy heat recovery system, pointing a fan out the window on a freezing day is just as bad as pointing one in the window. Maybe it's worth it given the health risks, but let's not pretend the tradeoffs aren't there. ^c42383821

  - **LegitShady** · [2024-12-11 05:56 UTC](https://news.ycombinator.com/item?id=42385198)
    its not just losing money - it will drop the air temps around your printer and that will do weird things to your print. all of these "direct vent" solutions are in warm areas or summer only. Its -2 f / -19c outside right now. I can't direct vent anything. Vapor from inside will turn to ice outside wherever I'm venting. It can't be done half assed. ^c42385198

- **Tempest1981** · [2024-12-11 02:25 UTC](https://news.ycombinator.com/item?id=42384056)
  Here's a similar version to the German link, but US store and voltage: ^c42384056

  [https://www.amazon.com/dp/B0C99834TW](<https://www.amazon.com/dp/B0C99834TW>)

  Any suggestions for something similar, but with temperature controlled speed?

