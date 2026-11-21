# [Launch HN: Electric Air (YC W23) – Heat pump sold directly to homeowners](https://news.ycombinator.com/item?id=35138319)

cmui · 2023-03-13 16:45 UTC · 789 reported comments · archived 2026-11-08 12:48 UTC
Observation: 2026-11-08 12:43 UTC → 2026-11-08 12:48 UTC

Hi HN! I’m Chris Mui, founder of Electric Air ([https://electricair.io](<https://electricair.io>)). We’re building a residential heat pump system. This will be an all-electric replacement for your home’s furnace and air conditioner that enables more centrally ducted installs, manages your indoor air quality, and saves you money on monthly energy bills. We also streamline purchase, finance and install by selling directly to homeowners. You can place a preorder today at [https://electricair.io](<https://electricair.io>).

Heat pumps work by using refrigerant and a compressor to move energy against a temperature gradient. If you put 1 kWh of energy into a heat pump, you get 3-5 kWh of heating in your home. But this isn’t breaking the laws of physics because heat pumps don’t make heat, they move it around. The extra 2-4kWh gets absorbed from the outdoors, even when it is cold outside. The low pressure refrigerant in the outdoor heat exchanger is colder than the outdoor air, so it has to absorb energy. After the compressor the refrigerant in the indoor heat exchanger is hotter than the indoor air, and energy flows into your home. This happens in a continuous cycle. A great feature in this system is a reversing valve that allows the flow of refrigerant to be flipped and your heat pump becomes an air conditioner.

There’s a big push to end fossil fuel use in US homes by electrifying all end-uses, and heat pumps are a critical part of this. Space heating is 50\% of the average homeowners energy consumption, and makes up 10\% of overall US energy use. Recognizing the importance of heat pump adoption, the recently passed Inflation Reduction Act contains \$4.3B in heat pump rebates for low and middle income families, and a \$2000 tax credit that applies to everyone. Heat pumps can also save homeowners on their monthly utility bills vs. heating with natural gas, propane, fuel oil, and electric resistance. And thanks to the popularity of vapor injection systems, heat pumps now work well even in the cold climates of the Northeast.

Quick technical aside on vapor injection systems -  this is an improvement to the basic vapor compression cycle. Gas from the condenser outlet is injected halfway into the compression process. This increases the compressor efficiency, increases the mass flow rate of refrigerant through the compressor, and also lowers the discharge temperature. The result is higher system efficiency, higher heating capacity, and the ability to operate across large temperature gradients (say -15F outside temp to 72F in your home) without exceeding the discharge temperature limit and damaging the compressor.

I’ve spent my career building and designing thermal systems—first in aerospace, then at Tesla working on Model 3 and Semi Truck, and most recently in vertical farming. I got really excited about residential heat pumps when I realized that we’re about to go through a huge transition where the 80M single family homes in the US replace their furnaces with heat pumps.

But the products on the market today have a number of shortcomings. The homeowner experience sucks because the integration of thermostat, heat pump equipment and air quality systems is terrible. Nothing works together well, and the best thermostats are not fully compatible with inverter driven heat pumps. In addition the process of getting a heat pump is painful, including finding a trustworthy contractor, sorting out financing, and wading through rebates. And finally contractors struggle with installs because of the difficulty of properly sizing the system, and understanding if your duct work is compatible with a heat pump

I wanted to approach home heating and cooling from a product design approach, improve the end-to-end experience for homeowners and make a product that was compelling beyond its climate motivations. Electric Air is building a thermostat as well as heat pump equipment (air handler and condenser) and a contractor web-app.

Better air quality is achieved through a thermostat with PM2.5 and CO2 sensors, as well as an air quality module on the air handler that controls HEPA filtration, fresh air intake and modification of the home’s humidity. The thermostat algorithm combines demand-response with weather and time-of-use rate plans to reduce monthly utility bills through pre-cooling and pre-heating. Unlike a Nest or Ecobee, the thermostat will be able to run the heat pump in variable speed mode. A more powerful air handler blower and contractor software enables more ducted installs - no wall units required. The most common heating system in the US is a natural gas furnace connected to ductwork, with the hot air ultimately coming out of vents in each room. This heat pump is a great replacement for the furnace and air conditioner in these ducted systems. The same software used for ducts also helps contractors perform simple load disaggregation (turn a utility bill into a thermal load calculation) to properly size a heat pump system. In addition there’s actually some industrial design going into the outdoor condenser, meaning you don’t have to hide it in an alley. And finally homeowners can purchase this system online. We help with financing and rebates, and connect them with a contractor to do the actual install.

How come no one’s doing this? Heat pump manufacturers are bad at making consumer products like thermostats and the thermostat manufacturers are IOT companies that don’t have the know-how to wade into heat pump equipment manufacture. For heat pump manufacturers, their end customer is largely HVAC contractors, and not homeowners. Also selling direct means disrupting their current distribution strategy which normally involves selling to regional distributors, and sometimes straight to contractors. Getting this right is a big systems integration problem that the current players are ill equipped to handle.

While we don't have any physical prototypes at the moment, we have the industrial design and also largely understand how this will be built. The core technology risk is quite low, it's really about executing the scope well and also finding the right product that homeowners find compelling. I'm working on building traction via preorders ([https://electricair.io](<https://electricair.io>)), and will start building hardware once fundraising is complete, likely in the next few weeks.

What issues have you had with your existing heat and cooling, and do you have any interesting stories around a heat pump install or use? I would love to hear your ideas, experiences, and feedback on any and all of the above!

## Comments

- **sokoloff** · [2023-03-13 17:15 UTC](https://news.ycombinator.com/item?id=35138895)
  I tried like hell to install an air-to-water heat pump instead of a replacement gas boiler and it didn't make anything close to economic sense to do so. ^c35138895

  What do I want from a heat-pump:

  I want it to work with a contact-closure (TT/XX) input to call for heat/cooling. Sure, if you have a fancy thermostat that works better, I'm going to read the brochure, but I'm not buying it if I find out it won't work with just a dry contact input.

  I want it to use parts that are in stock at my local HVAC supply house. I don't want to be without heat for 3+ days while some obscure custom part is shipped in from someplace across the country.

  I want it to have an open interface to extract data (similar to the open interface of a dry-contact closure) about run-time, performance, etc. (I will, however, buy it without this.)

  I want it to be sold/serviced by multiple competing suppliers in my area. (This is what ultimately undid the chance to install an A2W heat pump: only one company was in the business of supplying them and they priced it accordingly.)

  For a mini-split system, I want to be able to run the refrigerant and condensate lines inside the building so I don't have hideous lineset covers festooning my house.

  I'm happy to chat more as a homeowner interested in the space (but with a 6 month old Bosch boiler on the wall and possibly interested in the minisplit for shoulder season heating and summer cooling).

  - **Mvandenbergh** · [2023-03-13 18:01 UTC](https://news.ycombinator.com/item?id=35139759)
    Nobody will build a heat-pump system with an on/off control system like that because the performance will be awful. Certainly not an air-to-water system. ^c35139759

    - **oceanplexian** · [2023-03-13 18:31 UTC](https://news.ycombinator.com/item?id=35140257)
      It already exists. Check out Mr. Cool Universal and Gree Flexx. Heat pumps that work with a normal thermostat exist. ^c35140257

      Most of the info about this stuff online is trash because HVAC is the most toxic online community compared to any other contracting profession. One of the reasons highly efficient mini splits haven’t took off in the USA- the self proclaimed experts want to charge \$2000 to drill a hole and charge a line set, so most people DIY.

      - **thaeli** · [2023-03-13 18:51 UTC](https://news.ycombinator.com/item?id=35140566)
        I've often wondered why this is. My best guess is that the EPA cert (not actually hard to get) has been turned into some sort of weird quasi-guild-membership thing. ^c35140566

        I can walk right in to a "to the trade" electrical or plumbing supply and they'll deal with me, no problem, no questions asked. With HVAC.. they won't even talk to you without an EPA number, even if you're not buying refrigerant.

        DTC for whole house systems, if they can make the regulatory side work and provide a good customer experience, is the most important part of this.

        - **jijji** · [2023-03-14 01:05 UTC](https://news.ycombinator.com/item?id=35145867)
          when dealing with HVAC you either have to have a friend on the inside who has a license for mechanical or you have to buy everything on eBay... because you're right most of the supply houses won't talk to you unless you have an HVAC license of some sort, That's why most of the stuff I get is on eBay.... things like capacitors, blower motors, heat strips, R410A refrigerant etc either eBay or Facebook marketplace is the best place for it.... and then being in the house rental business I'm constantly buying this equipment and then just having people install it because it's just cheaper that way.... I save about 5 to \$7,000 on average per install doing it that way ^c35145867

          - **midoridensha** · [2023-03-14 02:20 UTC](https://news.ycombinator.com/item?id=35146512)
            Here in Japan, every home store and electronics/appliance store sells mini-split HVAC systems directly to consumers.  It's no different than buying a washing machine. ^c35146512

            - **Danieru** · [2023-03-14 03:03 UTC](https://news.ycombinator.com/item?id=35146855)
              Yup, and a vanilla install will cost say 150\$. Non vanilla installs still exist on the price list. ^c35146855

              Mini splits transform HVAC into Lego, and a competitive market for install is the future.

        - **sokoloff** · [2023-03-13 18:59 UTC](https://news.ycombinator.com/item?id=35140703)
          I'm a potential customer for DTC/DIY installation, but I think that's a pretty small slice of the market. Many of my friends are entirely willing to drop \$4-5K for a single zone mini-split install (that's \$1-1.5K of equipment and 2 hours of labor) and wouldn't dream of drilling a hole in the side of their house to save \$3K. ^c35140703

          - **abakker** · [2023-03-13 19:40 UTC](https://news.ycombinator.com/item?id=35141304)
            I recently got quoted \$17k for 2 zone mini split. I bought the tools, instructions, and watched youtube and spent \$4500 total. At that savings, I don't need a warranty. I can just buy and install another system if it fails. ^c35141304

            - **rnk** · [2023-03-14 00:05 UTC](https://news.ycombinator.com/item?id=35145213)
              Can you explain a little more what you did? Just a little bit, like what brand, did you replace an existing home system. Who did the electrical, did you need duct work? I already have a forced gas system, you can just connect it up? If I only had say 4-5 rooms on one story it would be a lot easier. ^c35145213

              - **sokoloff** · [2023-03-14 00:29 UTC](https://news.ycombinator.com/item?id=35145460)
                Lots of good YouTube videos and good DIY HVAC content on garagejournal.com (the latter will have good discussion on brands as well as DIY installs). ^c35145460

                For a case where you have a ducted gas furnace, you are probably better off with a traditional A coil evaporator, especially if you want invisible in the living area of the house. Those are not as DIY-friendly (but anything is DIY-able if you're skilled and bold enough, willing to learn, and willing \[or eager\] to buy some tools :) ).

              - **abakker** · [2023-03-14 18:43 UTC](https://news.ycombinator.com/item?id=35156488)
                Durastar 36k Dual head unit from ACwholesalers, buy 2 stage harbor freight vacuum pump, micron gauge from amazon, a bunch of manifolds, and fittings and adaptors from amazon, some NICE shredder core extraction tools, a NICE line set flaring tool, a pipe cutter, pre-insulated line set, 14/4 cable from outdoor unit to indoor units, 5/8 AC condensate pipe from indoor units outside, lots of zip ties, pipe wrap, and line hide. I pre-provisioned a 40amp breaker and an outdoor disconnect/breaker panel (and an extra 120v GFCI plug so i could easily run the vacuum pump). Sub-panels are your friend. ^c35156488

                I used all Aluminum SER cable to run the sub panel and a copper whip from the outdoor unit to the breaker (terminals on the AC unit are rated for copper wire).

                If you had a forced air gas system, you can get a heat pump coil and condenser to replace the AC unit. ACwholesalers has those too. If you are able to, you can add one to your system and run "dual fuel" where the heat pump runs down to about freezing, and only kicks on the gas for heat when it is outside the efficiency range of the heat pump (model dependent).

                My house is annoying to condition. It was built in 1987 by people who had interesting notions about efficiency, space usage, and material selection. As a result, the surface area to volume ratio is pretty poor and it is not very efficient. the duct design is...TERRIBLE...and so a lot of the house wasn't served well by the HVAC.

                I added a mini split to address the considerable heat load on the southern side of the house, and am working to replace the air handler and duct work entirely for the rest of the house.

                Central air can do several things mini splits can't do, and that's why I want to keep it instead of just adding 4-8 more zones of minis splits, which would be WAY easier. 1. Air filtration, 2. Fresh air intake 3. Humidification 4. air mixing. it also seems to be the cheapest way to solve heat/cool + the things I just mentioned. Even with ducting. Design/Sizing/install is worse and harder. Leaking/poorly insulated ductwork can also cost a lot of energy and so takes a lot of effort to prevent.

                HVAC as a mechanical system in homes is pretty awful, and the load calculations are frequently not well in line with the "theory" of system capabilities. Static pressure, air exchanges, etc all play Major roles in system sizing and make it very hard for technicians who do not live in a house to accurately evaluate the "real" load vs the theorized one.

      - **vl** · [2023-03-13 23:35 UTC](https://news.ycombinator.com/item?id=35144851)
        This is different problem though: contractors just don't want to do small jobs since it doesn't make economic sense to them. Try to hire someone to paint single room or install single outlet, etc. and you'll see it is nearly impossible. ^c35144851

        Thus the bill for the small job is outrageously high.

      - **KennyBlanken** · [2023-03-14 07:42 UTC](https://news.ycombinator.com/item?id=35148427)
        \$50 says their units are the same units that the Mr. Cool and Gree Flexx units come out of, just with a fancy panel. ^c35148427

    - **thaeli** · [2023-03-13 18:46 UTC](https://news.ycombinator.com/item?id=35140474)
      As a backup option, the incumbents already make this. Carrier Infinity is a good example. Proprietary protocol (RS-485 based, so it can run over existing thermostat wiring) between the smart thermostat and the furnace, and between the furnace and outside condenser unit. Even with all these smarts, there is still a fallback mode provided with a regular old dry-contacts control wires that can hook to any standard thermostat. Yeah, the system won't operate at peak performance, but it will operate, and that's very important when every HVAC tech carries a standard thermostat with them, or even uses basic jumper wires, in an emergency until they can return with correct parts. ^c35140474

    - **lsaferite** · [2023-03-14 12:33 UTC](https://news.ycombinator.com/item?id=35150444)
      Heatpumps are essentially pretty dumb devices at core. They use 24v AC for control, there's a reversing valve contactor to control if it's heating or cooling, there's a contactor for the fan, and one for each stage of the pump. Maybe there's another contactor for the emergency heating element. If you are fancy you might have contactors for UV sterilization, humidification, and/or dehumidification. ^c35150444

      Literally the 'smartest' part of my HVAC system, beyond the thermostat, is the blower fan. It's a variable speed motor and has a speed controller integrated into the motor housing with multiple 'taps' that let you control the fan speed in steps. It's configurable if you have the programming hardware.

    - **yencabulator** · [2023-03-13 21:43 UTC](https://news.ycombinator.com/item?id=35143276)
      My Carrier wall unit has a button for manual operation: ^c35143276

      \> MANUAL CONTROL is intended for testing purposes
      and emergency operation only.

  - **LeonM** · [2023-03-14 12:44 UTC](https://news.ycombinator.com/item?id=35150578)
    \> I want it to work with a contact-closure (TT/XX) input to call for heat/cooling. Sure, if you have a fancy thermostat that works better, I'm going to read the brochure, but I'm not buying it if I find out it won't work with just a dry contact input. ^c35150578

    \> I want it to have an open interface to extract data (similar to the open interface of a dry-contact closure) about run-time, performance, etc. (I will, however, buy it without this.)

    FWIW, there is a standard called OpenTherm which most off the shelf thermostats support and HVAC systems support. It's a 2-wire serial 2-way protocol, quite simple.

    IIRC OpenTherm even has a fallback compatibility mode where closing the loop will enable the system at full power, though I am not sure this will work with heat pumps, as they can both heat and cool.

    You could even rig up a Raspberry Pi or equivalent with an OpenTherm interface and attach it to any OpenTherm compatible heater/cooler to control it and read stats.

  - **RetpolineDrama** · [2023-03-13 18:23 UTC](https://news.ycombinator.com/item?id=35140125)
    \>but I'm not buying it if I find out it won't work with a dry contact input. ^c35140125

    But... why?

    - **sokoloff** · [2023-03-13 18:35 UTC](https://news.ycombinator.com/item?id=35140315)
      Because it's from a new entrant to the market and I don't know that their complex interface will be available, supported, and serviceable 12 years into the 20 year lifetime of the equipment. I do know that I will always be able to provide a dry contact closure in the event they go belly-up and the thermostat goes unsupported. ^c35140315

      I have my current gas boiler working via an outdoor reset mechanism that provides flow water at 116°F to 135°F via a dry contact closure from the zone relay box. There's no reason for me to believe that Bosch (and others) can create a modulating boiler that works efficiently from just a dry contact closure input from the house (plus a flow temp sensor, a return temp sensor, an outdoor temp sensor, and a programmed reset curve in the heating unit), but that a heat pump would be unable to do the same.

      The boiler can modulate up and down based on the delta-T between return and supply and the target supply temp from the outdoor reset. A heat pump could do exactly the same thing (with an inverter drive, it can do it with even more granularity than a multi-stage gas valve affords).

      - **dtgriscom** · [2023-03-14 02:23 UTC](https://news.ycombinator.com/item?id=35146539)
        Ah, clarification: you're OK with using a proprietary (and intelligently proportional) thermostat, as long as there's a backup dry contact option if the factory thermostat fails and is irreplaceable. ^c35146539

        - **sokoloff** · [2023-03-14 02:39 UTC](https://news.ycombinator.com/item?id=35146677)
          Yes, that’s true; I’m ok to use a proprietary thermostat if I think it will save me money in 2 years max. (I’m using Sensi wifi thermostats that will become non-programmable if they stop supporting their phone app. It’s ok, as they were around \$40 each after incentives and I’ll save most of that just this heating season. Its interface to the boiler is just power, common, and call-for-heat.) ^c35146677

          At least in a hydronic (air-to-water or gas-fired) application, an intelligent stat is not mandatory to get decent efficiency (from variable control). You still have building heat transfer rate and outdoor temp sensing available inside the unit even with just a contact closure.

- **quirkot** · [2023-03-14 03:21 UTC](https://news.ycombinator.com/item?id=35146984)
  I've seen other construction related businesses try to go direct and it is *extremely* difficult. By going direct to the homeowner you are targeting the venn diagram union of "people who are willing & able to do the work themselves" and "people who will pay more" ^c35146984

  How are you going to build your service network? You say you will "connect them with a contractor to do the actual install." But contractors make their money on equipment sales, not on labor. I bought my residential HVAC system direct from a friend and it took me 3 weeks calling around to find a contractor that would do the install and THAT was only because of the same friend connection.

  Who are the decision makers in your target market exactly? Wil Joe Homeowner be deciding? Will you pursue developers who install and build? Are you pursuing multi-family complexes and engineers will be specifying the equipment? Each of these will require you to provide value above and beyond what they are receiving now and it's not clear what your value proposition is.

  \>\> "contractors struggle with installs because of the difficulty of properly sizing the system, and understanding if your duct work is compatible with a heat pump"

  What? How could duct work possibly be incompatible with a heat pump? Any forced air system is already ready for hot or cold air. Additionally if you are banking on contractor unfamiliarity or incompetence as part of your business plan, you are in for a rude surprise.

  One other headwind is that you're VC funded. No one wants to buy a HVAC unit from a company with a 5-7yr liquidation event timeline. If you do go into *any* other channel than direct to home owner, no one wants to SELL a unit that may not exist in 7 years. How will support work? What about parts? A well built machine could be in working for 15 years (or longer) and the question everyone has is: will you?

  - **cmui** · [2023-03-14 03:53 UTC](https://news.ycombinator.com/item?id=35147239)
    \> By going direct to the homeowner you are targeting the venn diagram union of "people who are willing & able to do the work themselves" ^c35147239

    This is meant to be installed by a professional contractor, not the homeowner.

    \> How are you going to build your service network?

    Compensate the contractors fairly and act as lead gen.

    \> Who are the decision makers in your target market exactly?

    Homeowners. Not targeting multiunit residential or new builds, they care less about efficiency because they don't bear the cost of ownership.

    \> What? How could duct work possibly be incompatible with a heat pump?

    A natural gas furnace requires \~150cfm airflow per 10kbtu heat produced, while a heat pump requires 330cfm per 10kbtu. This large mismatch in required airflow means that if you replace a natural gas furnace with a like sized heat pump, you've likely exceeded the ability of the air handler blower. Luckily most natural gas furnaces are grossly oversized for homes. The way you find the right size unit is with our software.

    - **borland** · [2023-03-14 10:29 UTC](https://news.ycombinator.com/item?id=35149458)
      \> \> How are you going to build your service network?
      \> Compensate the contractors fairly and act as lead gen. ^c35149458

      I used to work at a company which makes security and access control systems (swipe cards, electronic locks, etc).

      They created a consumer-level system (as opposed to the big Enterprise ones they were known for) and tried to create a distribution model which appears to be how you're thinking about it. The idea was they'd build a network of contractors ("Installers"). Customers would buy direct from the company, who would then forward a request to your local installer (lead gen). The company would cut the installers in for some percentage of the ongoing subscription revenue cost, plus whatever margin they added at install time.

      This *failed miserably*. The company learned within the space of a couple of years, that all the good installers want to build a relationship with (and critically, to bill) the customer, they don't want to be a behind-the-scenes referral on someone else's website. 
      Few signed up, and the ones that did, weren't incentivized to prioritize it highly. They put it lower down on their job lists, which led to customers having to wait a long time and experiencing poor service in some cases. Not great.
      The company also struggled tremendously to drum up interest. Because security systems (like HVAC) come with maintenance/repairs/etc, the market had evolved into one centered around companies/individuals looking around at their local providers first, picking the "best" one, and then choosing a product based on what the provider was offering or what they recommended, much like you would with a Plumber or Electrician.

      Maybe the HVAC industry is sufficiently different from Security and this model might work for you? From what I saw though, there's a lot of overlap there and I'm not optimistic.

      After a year or two, the company pivoted to a model where they formed partnerships with contractors/installers and moved away from the direct-to-consumer model. At the time I left, this was proving much more successful of a model. The partnership model involved more revenue share, training, and a bunch of other stuff I wasn't involved in, but critically, it meant that when an end-customer went to their local security system provider and asked them what was good, they'd be highly likely to recommend my ex-company's product. That was the clincher.

      I hope that's of some use @cmui

      - **r3trohack3r** · [2023-03-14 14:15 UTC](https://news.ycombinator.com/item?id=35151871)
        A flip-side from the consumer perspective. ^c35151871

        The company who installed the windows in our house operated this way. They have a network of contractors for installs.

        The contractor that showed up was accompanied by their general contractor who managed the relationship with the window company and customer.

        The general contractor came with business cards, was friendly, and kicked off a 15 minute conversation where we walked around the house and made a list of everything they could help with later down the road.

        The lead for them wasn’t the window install, it was follow up business once they built a relationship. The window install was an ad for them.

    - **KennyBlanken** · [2023-03-14 07:23 UTC](https://news.ycombinator.com/item?id=35148329)
      \> This is meant to be installed by a professional contractor, not the homeowner. ^c35148329

      And where are you going to get the contractors? Nobody is going to want to contract with you. HVAC companies go with 1, maybe 2 companies. How are you going to pull them away from Carrier, Lenox, etc who can offer volume discounts or just dump their products into the market and bleed you dry without even noticing the effect on their balance sheet?

      How are you going to get the plumbing/heating distributors to supply companies to stock your units and parts? You're going to distribute them yourselves? That's going to be very expensive, slow, and unreliable.

      How are you going to guarantee you'll still be around for the lifespan of the unit, to provide parts and technicians who know how to service the units?

      *Puts envelope with your business plan to forehead*

      You're going to:

      \-lock down the protocol between the components so nobody can use standard thermostats

      \-lock down access to the controller for diagnostics, forcing people to go with you for service

      \-charge a fee for remote "smart" thermostat features

      \-justify all this with some hand-wavy nonsense about using ML/AI to maximize energy efficiency or predict when the unit needs service

      How close am I?

    - **judge2020** · [2023-03-14 05:55 UTC](https://news.ycombinator.com/item?id=35147888)
      \> This is meant to be installed by a professional contractor, not the homeowner. ^c35147888

      This quote was obviously to emphasize that HVAC contractors make money from margin on equipment sales and not labor, which (according to OP) means you end up targeting people who either can do it themselves or purchase this before finding out how hard it is to find a certified technician willing to basically waste their time on installing a HVAC system for little profit.

      The only way I can see this working is if perhaps Electric Air pays a hefty commission to their HVAC techs as a way to ensure they still profit from their time, which is what I assume OP was trying to find out.

    - **chwzr** · [2023-03-14 06:53 UTC](https://news.ycombinator.com/item?id=35148181)
      \> This is meant to be installed by a professional contractor, not the homeowner. ^c35148181

      But I would want to install that myself. I do everything in my house myself.
      Could I order a device from you and at the same time save the compensation that otherwise gets the installer?

    - **friendzis** · [2023-03-14 09:34 UTC](https://news.ycombinator.com/item?id=35149099)
      \> A natural gas furnace requires \~150cfm airflow per 10kbtu heat produced, while a heat pump requires 330cfm per 10kbtu. ^c35149099

      How do you arrive at these figures? First, you are stating flow numbers at total energy which does not make sense. Second, airflow requirements at certain *power* (not energy you cite) come from heat exchanger size and temperature gradient. What are operational parameters of the reference natgas heater?

      Let's assume that you mean 10kbtu/h instead of 10kbtu. That is \~3kW. For reference Nibe F730 produces \~5kW at 250M\^3/h, i.e. 150 cfm.

      - **ovi256** · [2023-03-14 10:51 UTC](https://news.ycombinator.com/item?id=35149576)
        Heat pump output temp is lower than a furnace's. Thus, it needs to move more air to inject the same heating power. ^c35149576

        In Europe, where the traditional working fluid is usually water in water radiators, this has been a big issue in popularizing heat pumps. Radiators sized right for hot water from electric or gas furnaces were undersized for heat pumps and their lower output temp. This required expensive replacing of the water network and radiators.

        Heat pumps in new builds are popular for heated floors, which are great.

    - **Vrondi** · [2023-03-14 15:40 UTC](https://news.ycombinator.com/item?id=35153301)
      If I still have to hire a contractor, then why on Earth would I direct buy from you? The only reason I'm even interested in reading this post is the idea of installing myself with no contractor involved. I can't imagine why anyone not interested in self install would ever want to direct buy. Too much hassle to still have to go find a contractor willing to do it. ^c35153301

    - **quirkot** · [2023-03-14 20:05 UTC](https://news.ycombinator.com/item?id=35157588)
      \>\> How are you going to build your service network? ^c35157588

      \> Compensate the contractors fairly and act as lead gen

      This will be tough. At least in my geography every decent contractor is busy all the time. Additionally, you'll need to provide enough business to your partners that it's worth the time to deal with. I don't know if that's 1/x install per week or enough to basically have a whole dedicated person. I've tried to outsource something similar (equipment start-up, not install), but my volume was only \~20/year and my guy eventually said it wasn't worth the hassle unless the price was outrageous.

      I see a bunch of people dogpiling. I'm skeptical of the distribution approach, but there is space for more heat pump players. Good luck. See you at AHR in Chicago

    - **unknown** · [2023-03-14 13:00 UTC](https://news.ycombinator.com/item?id=35150750)
      [deleted] ^c35150750

    - **uoaei** · [2023-03-14 06:16 UTC](https://news.ycombinator.com/item?id=35147991)
      [flagged] ^c35147991

      \[flagged\]

  - **alangibson** · [2023-03-14 10:00 UTC](https://news.ycombinator.com/item?id=35149296)
    \> But contractors make their money on equipment sales, not on labor. ^c35149296

    This. No competent contractor will install a unit you bought off some website.

    That will lead to two possibilities: 
    1) Homeowners try to install it themselves and screw it up
    2) Incompetent contractors install it and screw it up

    The result of both is bad word of mouth/press and reputational damage to the brand.

    - **galfarragem** · [2023-03-14 13:14 UTC](https://news.ycombinator.com/item?id=35150908)
      That is exactly what most people fail to acknowledge: (nowadays) every competent contractor in trades has more work than he can handle. You need him more than he needs you. ^c35150908

  - **hef19898** · [2023-03-14 13:37 UTC](https://news.ycombinator.com/item?id=35151258)
    Basically the same business model Solar City, and a whole bunch of other PV start-ups, tried and failed with. In this model, you take the capital requiremts, someone has to fund the equipment, and the resource requirements, selling once every twenty year purchases to consumers requires loads of people, combine them together and hope all the hot VC money will allow you to squeeze enough existing companies out to create a comfortable nieche for yourself by the time VC money isn't there anymore... ^c35151258

  - **avip** · [2023-03-14 07:54 UTC](https://news.ycombinator.com/item?id=35148506)
    (intersection) ^c35148506

    - **quirkot** · [2023-03-14 19:56 UTC](https://news.ycombinator.com/item?id=35157416)
      Doh! ^c35157416

  - **KennyBlanken** · [2023-03-14 06:48 UTC](https://news.ycombinator.com/item?id=35148154)
    [flagged] ^c35148154

    \[flagged\]

- **mdasen** · [2023-03-13 17:37 UTC](https://news.ycombinator.com/item?id=35139323)
  I guess I'm wondering what this offers over calling an HVAC company and having them install a heat pump system. The system seems expensive at \$14,000 for a 48k BTU 18 SEER system. It looks like I can get that for \$4,000. Is the sleek software and design of your units worth the extra \$10,000, especially when I'm not really going to see my air handler frequently? ^c35139323

  I do like that it monitors CO2 and offers humidification, but presumably that means that it needs a hookup to a water line for humidification (not that easy since my air handler is in my attic) and a source of fresh air (so presumably a hole in the roof or something to accommodate that).

  I'm also curious if the mini-split system on your site would also handle fresh air and humidification. Wouldn't that require each air handler to have access to fresh air and water?

  I'm also curious why 18 SEER? Are there diminishing returns above that? I'm in a pretty cold climate so I've been thinking it would be better to get a 20 SEER unit.

  My suggestion for your company: Add stoves and hot water heaters to your offering. I'm not going to switch to a heat pump and continue to have natural gas for my stove and hot water heater. If I'm going to put in a heat pump, I'd want to get natural gas out of my place. I don't want to have to get a heat pump from you, then call someone else to deal with my water heater and another person to deal with my stove.

  I'm certainly not an expert on this so maybe you'll just say that you're using more reliable equipment than the stuff I've seen, but it seems like something I'm more inclined to go with a local HVAC company than a startup.

  - **dmarlow** · [2023-03-13 19:29 UTC](https://news.ycombinator.com/item?id=35141151)
    Same thought as well. I recently self installed an 18k BTU unit. The lines came pre-charged, but I wanted it to be run exactly to length. For someone to come and do just that part (cut, flare and vacuum/charge the lines) cost me just \$150. I got the unit (a pioneer) for under \$900. The rest of the world has heat pumps figured out, no need for a tesla-ish version charging a premium. Cost will be the biggest factor for adoption for ElectricAir, imo. ^c35141151

    If anything, a sweaty startup offering just the install for a nominal fee would do really well here.

    - **antisthenes** · [2023-03-13 20:39 UTC](https://news.ycombinator.com/item?id=35142200)
      \> The rest of the world has heat pumps figured out, no need for a tesla-ish version charging a premium. ^c35142200

      USA has heat pumps (the technology) figured out as well.

      What the USA does NOT have figured out is how to accomplish trades like HVAC and construction without massive grift.

      - **c\_o\_n\_v\_e\_x** · [2023-03-14 02:20 UTC](https://news.ycombinator.com/item?id=35146509)
        \>What the USA does NOT have figured out is how to accomplish trades like HVAC and construction without massive grift. ^c35146509

        The US has professional licensing schemes which increase costs.  I had to work 5 years in the field doing HVAC work before even being eligible to get a license.  Licensing limits the supply of labor while (in theory) establishing better quality.  I've lived in countries with zero professional licensing and the quality of work is atrocious.

        - **freeopinion** · [2023-03-14 05:30 UTC](https://news.ycombinator.com/item?id=35147758)
          I live in the USA and have seen plenty of atrocious work. I currently have the best HVAC expert in the world. YMMV. ^c35147758

          - **c\_o\_n\_v\_e\_x** · [2023-03-14 06:45 UTC](https://news.ycombinator.com/item?id=35148137)
            Was said work performed by a licensed individual? ^c35148137

            Fun fact - In some states, contracts with unlicensed contractors are unenforceable.

            - **aidenn0** · [2023-03-14 15:48 UTC](https://news.ycombinator.com/item?id=35153455)
              I have had incredibly atrocious work done by licensed individuals of all stripes.  In one case they took out a mechanics lien on the house when I refused to pay for unfinished and shoddy work and then one of their workers assaulted my wife. ^c35153455

              \- Horizontal exhaust run from a furnace that was 25x longer than specified by the manufacturer

              \- Putting registers in very wrong places (like 2 in one room and 0 in another instead of one in each)

              \- (For Electrical) Rather than using junction boxes, just wire-nut together some Romex in random places in the attic.

              - **acjohnson55** · [2023-03-15 04:08 UTC](https://news.ycombinator.com/item?id=35163747)
                Geez, sorry you dealt with that. In my town, this would never pass inspection, which certainly costs something in taxes, permits, and labor cost, but I think it would be difficult to end up saddled with bad work. ^c35163747

                - **aidenn0** · [2023-03-15 21:24 UTC](https://news.ycombinator.com/item?id=35174935)
                  All the contractors around here push really hard to do the work without permits.  It takes at least twice as long to finish with permits since there needs to be an inspection after each step that will get covered up by something else (and since much work is done unpermitted, many contractors forget to do this and have to redo work). ^c35174935

                  I always pull permits these days because of stupid stuff contractors have done; the horizontal duct run that was way out of spec was found by an inspector and I had to call 4 HVAC contractors before finding one that would do a quote that included permits...

              - **c\_o\_n\_v\_e\_x** · [2023-03-15 00:42 UTC](https://news.ycombinator.com/item?id=35162009)
                What a nightmare! I hope you filed a complaint ^c35162009

        - **KingMob** · [2023-03-14 05:39 UTC](https://news.ycombinator.com/item?id=35147816)
          So, what I'm hearing is software engineers should be licensed. ^c35147816

          - **oriolid** · [2023-03-14 15:35 UTC](https://news.ycombinator.com/item?id=35153219)
            Do you have the knowledge or time to conduct whiteboard interviews for every contractor? ^c35153219

    - **adventured** · [2023-03-13 20:54 UTC](https://news.ycombinator.com/item?id=35142415)
      \> The rest of the world has heat pumps figured out ^c35142415

      A single digit percentage of homes globally are using heat pumps, most of the world does not have it figured out. That's specifically why Electric Air exists, they're chasing what is going to be a gigantic market (if it were already such a figured out market they couldn't get funding without a revolutionary 10x approach, YC would have little interest).

      - **veb** · [2023-03-13 22:54 UTC](https://news.ycombinator.com/item?id=35144296)
        I'd say in New Zealand we definitely have them figured out. Every rental needs a heat-pump if there's no fireplace. Landlords will prefer the heat-pumps primarily because it's less maintenance. Apparently 25\% of all households in NZ have one: [https://www.genesisenergy.co.nz/tips-and-tricks/articles/use...](<https://www.genesisenergy.co.nz/tips-and-tricks/articles/use-your-heat-pump-efficiently-this-winter>)) you may also be interested in: [https://figure.nz/chart/HkvN4YjwyylwL2A4](<https://figure.nz/chart/HkvN4YjwyylwL2A4>) ^c35144296

        Ours are exactly the same sort of units that I saw in Singapore - they're A/C systems, but can do cold or hot. I remember when I saw the 'heat-pumps' in Singapore, I was like "Wow, why does everyone have a heat-pump" and everyone looked at me and went "What's a heat-pump?" as they always called them A/C units - doubt they ever got above 16 degrees or something.

        - **socks** · [2023-03-14 12:21 UTC](https://news.ycombinator.com/item?id=35150308)
          You just helped me realise (as an Aussie living in Europe) that when some people are saying "air-to-air heat pump" what they mean is what an Aussie or Kiwi would call "reverse cycle air conditioner" - which are *extremely* common and affordable.
          The heat pumps I have seen personally in Europe are geothermal, very big, and very expensive. ^c35150308

          - **bkor** · [2023-03-14 15:16 UTC](https://news.ycombinator.com/item?id=35152852)
            \> The heat pumps I have seen personally in Europe are geothermal, very big, and very expensive. ^c35152852

            In NL I saw loads of water/water heat pumps (so using geothermal) in plans for new buildings. The latest plans now seem to prefer air/water. The air/water is cheaper and the units nowadays are much quieter than they used to be. This is just my observations, I could be way off.

          - **ianleighton** · [2023-03-14 13:05 UTC](https://news.ycombinator.com/item?id=35150805)
            I think your reverse cycle ac would be an air-to-air heat pump. Air-to-water is more like your heat pump water heater, with the hot water then going through radiators. ^c35150805

        - **avastmick** · [2023-03-14 04:43 UTC](https://news.ycombinator.com/item?id=35147543)
          Aligns with our experience in China for the four years before the pandemic. Apart from a couple of apartments we visited in Harbin that had gas boiler radiators, everwhere else we found apartments heated and cooled by heat pumps. It makes total sense in countries that have hot summers and cold winters. ^c35147543

      - **yurishimo** · [2023-03-13 21:54 UTC](https://news.ycombinator.com/item?id=35143464)
        Europe as a whole has been utilizing heat pumps for residential heavily over the past decade. With global temperatures rising, heat pump installs in OECD countries are skyrocketing as the climate becomes uncomfortable for larger and larger groups of people. ^c35143464

        In the Netherlands, I can purchase a minisplit with installation for under €4k. It could get cheaper if I wanted something less powerful.

        While your point about "single digit percentage\[s\]" is accurate, it's not helpful when discussing the merits of this product, or the wider industry as a whole in most of western world.

        - **adventured** · [2023-03-13 22:10 UTC](https://news.ycombinator.com/item?id=35143704)
          \> it's not helpful when discussing the merits of this product ^c35143704

          Of course it is. How would global market size, present and future, not be helpful as a discussion topic? The parent I replied to was referencing that very issue, directly or indirectly. It indicates heat pumps are still a relatively small market, and the OP company is betting it's going to get a lot larger, meaning there is a landgrab going on right now and they're aiming for capturing a segment of that future market.

          You contradict your claim that it's not a helpful discussion point in pointing out how usage is skyrocketing (ie the market is getting bigger fast) and having to reference the larger established use in some parts of Europe to try to make your point. You proved it is a pertinent discussion point in trying to claim that it's not.

        - **spockz** · [2023-03-14 05:33 UTC](https://news.ycombinator.com/item?id=35147775)
          Where are you looking for \<€4K  installs? Most around here start at 4. But that is using daikin. ^c35147775

          I’m a bit concerned about what happens when it freezes. Can the outdoor unit still I operate?

          - **sparsely** · [2023-03-14 09:15 UTC](https://news.ycombinator.com/item?id=35148958)
            \> I’m a bit concerned about what happens when it freezes. Can the outdoor unit still I operate? ^c35148958

            Yes as long as the parts where chosen by someone with a bare minimum of competence. The efficiency will be lower than ideal but still better than electric radiators. Norway has very high heat-pump installation rates.

          - **lb1lf** · [2023-03-14 12:33 UTC](https://news.ycombinator.com/item?id=35150431)
            I am using a Panasonic unit a little south of the Arctic circle. Even at -20C outside it works fine. ^c35150431

          - **yurishimo** · [2023-03-14 10:29 UTC](https://news.ycombinator.com/item?id=35149460)
            I live in Brabant, so that likely explains the discrepancy in pricing. ^c35149460

      - **fomine3** · [2023-03-14 00:46 UTC](https://news.ycombinator.com/item?id=35145648)
        \$500 + \$150 (install) mini split works fine in Japan and it should be fine for other worlds where central heating isn't a thing. US is one of the richest country and rest of the world spend less. ^c35145648

    - **hcrisp** · [2023-03-13 20:12 UTC](https://news.ycombinator.com/item?id=35141809)
      I agree, in fact a couple things in the pitch don't add up. ^c35141809

      *\> ... where the 80M single family homes in the US replace their furnaces with heat pumps.*

      Where did they get this statistic?  I already have a heat pump and know many that do too.  Are we included in this 80M estimate?  What about those in the northern half of the US that also need back-up heat for when it is very cold?  They aren't going to replace their furnaces with a heat pump.  They might add one to their setup but replace, no.

      *\> In addition the process of getting a heat pump is painful, including finding a trustworthy contractor, sorting out financing, and wading through rebates. And finally contractors struggle with installs because of the difficulty of properly sizing the system, and understanding if your duct work is compatible with a heat pump*

      I don't know the contractors they are talking about, but I literally had to say the words "heat pump" to my local Carrier installer and they did all the rest.

      - **snark42** · [2023-03-13 23:53 UTC](https://news.ycombinator.com/item?id=35145062)
        \> What about those in the northern half of the US that also need back-up heat for when it is very cold? ^c35145062

        This heat pump is supposed to work to -15F and includes back-up resistive heat.  Theoretically it can replace a heater and air conditioner anywhere.  I know people north of Chicago that use a similar heat pump and resistive backup system and it's been fine to -30F keeping the house at 69F.

        \> I don't know the contractors they are talking about, but I literally had to say the words "heat pump" to my local Carrier installer and they did all the rest.

        There's definitely a bias against them when natural gas is available.  Until probably the past 3-4 years very few HVAC contractors in the midwest were familiar with heat pumps or had bad experiences 5-15 years back and recommended against them as it's "too cold" for them to work here.

        - **andrewem** · [2023-03-14 04:29 UTC](https://news.ycombinator.com/item?id=35147464)
          My gas-powered water heater failed in my northern US location. I asked a friend who’s a plumbing engineer (!) who said to get a heat pump. I called the HVAC company which had installed the gas water heater and gas furnace some years before and asked for a heat pump water hearer, and they said oh yeah we sell one of those and people love it. I get the feeling that as you say 5-15 years ago it would have been a different story but now it’s routine. ^c35147464

          - **cmui** · [2023-03-14 04:55 UTC](https://news.ycombinator.com/item?id=35147604)
            Heat pump water heaters are great, also a much simpler install than an HVAC system. ^c35147604

        - **shjake** · [2023-03-14 07:17 UTC](https://news.ycombinator.com/item?id=35148298)
          Resistive heating is very extremely inefficient compared to gas though ^c35148298

          - **m\_d\_** · [2023-03-14 15:31 UTC](https://news.ycombinator.com/item?id=35153136)
            Clarification: resistive heating is very near 100\% efficient, meaning that all of the energy you pull ends up in the air or water it is meant for. Gas water heating is at the very best \~90-95\% efficient (e.g., top-end condensing tankless water heaters), but often as low as 60\%: plenty of heat going out the exhaust. You think resistive heating is inefficient because policy has made electricity much more expensive per kwh than gas/oil. ^c35153136

      - **cmui** · [2023-03-14 04:53 UTC](https://news.ycombinator.com/item?id=35147596)
        Only 17\% of homes have heat pumps at the moment. 80M (though I believe its closer to 88M) homes in the US are single family detached homes. ^c35147596

        What region are you in? Local contractor knowledge around heat pumps is quite regional.

        - **malfist** · [2023-03-14 17:01 UTC](https://news.ycombinator.com/item?id=35154617)
          \>  Only 17\% of homes have heat pumps at the moment. 80M (though I believe its closer to 88M) homes in the US are single family detached homes. ^c35154617

          \> ... where the 80M single family homes in the US replace their furnaces with heat pumps.

          Why would 13.6M homes with heat pumps need to replace their heat pump with a heat pump?

          What percentage of that 80M single family homes have a climate that can run on heat pumps?

    - **turtlebits** · [2023-03-13 23:43 UTC](https://news.ycombinator.com/item?id=35144965)
      The problem with trying to charge a nominal/flat fee is the same for all contractors. ^c35144965

      Not all houses are alike, and you'll never know what is inside a wall/attic where a customer wants to install it, or what kind of electrical work will be needed. (might have to run a new 240v line).  Dirt work may be required for the exterior condenser.

      - **dmarlow** · [2023-03-14 00:34 UTC](https://news.ycombinator.com/item?id=35145511)
        Totally get it. If you're into it for a few k to install, that's one thing. To me, the total costs for this seem a bit high. Who knows, maybe with scale things get cheaper. I'm definitely not their target customer, despite wanting to be. ^c35145511

  - **0xffff2** · [2023-03-13 17:47 UTC](https://news.ycombinator.com/item?id=35139502)
    I mean, they estimate \$10k for installation, so you *are* calling an HVAC company and having them install a heat pump system. It's not clear to me from the website if the idea is that they are actually integrating installation in-house or if they will contract out the work, in which case it's likely the exact same installers as if you ordered a system from somewhere like Home Depot. ^c35139502

    - **yencabulator** · [2023-03-13 21:50 UTC](https://news.ycombinator.com/item?id=35143384)
      Well, at least the ones that agree to work with it. For example, the most reputable HVAC company I can find locally has picked their favorite 1-2 brands and largely only installs those, so they know what they're bound to be repairing later. ^c35143384

      - **cstejerean** · [2023-03-13 23:23 UTC](https://news.ycombinator.com/item?id=35144691)
        They also tend to only install units that you can't buy directly and only quote for total cost not parts and labor so you cannot easily tell just how much they are charging for the labor. ^c35144691

        - **PaulDavisThe1st** · [2023-03-13 23:51 UTC](https://news.ycombinator.com/item?id=35145049)
          What difference would the breakdown on parts and labor make to you as a prospective client, given that you cannot buy the units directly? ^c35145049

          - **cstejerean** · [2023-03-14 00:50 UTC](https://news.ycombinator.com/item?id=35145699)
            It must make a difference otherwise they'd provide the breakdown when asked. ^c35145699

            I suspect most consumers don't know how much the appliance should cost, it is a complex piece of machinery. But the labor part is easier to reason about.

            So seeing \$12k all in to install a heat pump might seem reasonable, people will shrug and say heatpumps must be expensive, but if they see that's \$5k for the heat pump and \$7k for the labor then it doesn't seem so reasonable.

            And there are alternatives. You can buy comparable units from other manufacturers directly and shop for labor only (harder to find but not impossible). And there are sealed DIY units you can install yourself.

          - **briHass** · [2023-03-14 00:51 UTC](https://news.ycombinator.com/item?id=35145710)
            The answer to this, assuming the breakdown was actually honest, is exactly why they don't typically provide a breakdown. You would see an hourly labor rate that would make a lawyer blush. There's just something unpalatable to most people about seeing a \$200-300+/hr labor rate, especially considering that the average person paying that rate probably make closer to \$20-40/hr. ^c35145710

          - **hattmall** · [2023-03-14 01:01 UTC](https://news.ycombinator.com/item?id=35145829)
            You could buy an equivalent system, they just use special contractor only models so you cant easily see the price online. ^c35145829

  - **ryantgtg** · [2023-03-14 03:08 UTC](https://news.ycombinator.com/item?id=35146892)
    From your comment, it sounds like managed to find a price for this unit. I’m on my phone, and the preorder page says nothing more than a \$100 deposit. Why would anyone order this without the full price bring front and center? Is this a mistake or are these people hiding this info? ^c35146892

- **opendomain** · [2023-03-14 00:44 UTC](https://news.ycombinator.com/item?id=35145624)
  I love startups, but the value proposition is not here.  I just had a heat pump installed and it was a much better price and higher efficiency.  What is the benefit of direct to consumers is you are going to charge more?  What makes your heat pumps better? Hepa filtering? Smart controls? They all have that. ^c35145624

  Is the market niche esthetics? They do look nice - maybe this company is trying to be the Apple of heat pumps? Charge more because of looks?

  This is a serious question - where is the innovation?

  - **donkeyd** · [2023-03-14 05:56 UTC](https://news.ycombinator.com/item?id=35147891)
    \> What is the benefit of direct to consumers is you are going to charge more? ^c35147891

    I'm going to guess there's a very specific target market for this, 'lazy' people with a lot of money who don't really do a lot of research before they buy stuff. They are aware of climate change and the need to reduce emissions and have heard of heat pumps as a solution. They've already installed solar panels through a similar service that made the process seamless. They don't want to spend hours calling contractors, getting estimates and selecting someone who is trustworthy. They've bought the same brand car from the same dealership for the last 40 years or so because it's familiar and has worked every time.

    There's a massive group of people in the 50-70 age range who are like this. But there are also plenty young people who are like this. Heck, I almost paid quite a lot more for my bathroom than necessary, because of the convenience of the store also installing the bathroom. This meant no need to find a decent contractor (there are many awful ones over here).

    - **newaccount74** · [2023-03-14 09:47 UTC](https://news.ycombinator.com/item?id=35149195)
      I think that the vast majority of people do not like calling contractors for quotes. You have to spend time on the phone, wait for someone to show up at your house, wait two weeks, call them a bunch of times to ask when they will have time to send a quote, only to find out the cost is about 3 times what you expected, and the quote doesn't include a few things you specifically asked for. ^c35149195

      If a company has a website where I can see an estimated price before I call, that's a huge advantage.

    - **Cthulhu\_** · [2023-03-14 08:37 UTC](https://news.ycombinator.com/item?id=35148751)
      \> But there are also plenty young people who are like this. ^c35148751

      I think there's a subcategory of people who would go for this one specifically because it's a SF company, "one of us" kinda thinking. And unawareness of the market and competition where heat pumps are normalized, routine, and don't need the sleek marketing page / YC funding.

    - **lbriner** · [2023-03-14 11:00 UTC](https://news.ycombinator.com/item?id=35149630)
      A couple of companies like boxt did it in the UK with gas boilers. The appeal is a fixed price quote online, next day installation by a qualified plumber and not having to spin the roulette wheel of trying to call plumbers, negotiate a "fair" price and not have the customer support if things go wrong. ^c35149630

      Can you get a cheaper install with another plumber? Not necessarily! boxt have massive volume discounts with boiler manufacturers and presumably keep the installation charge reasonable but the plumber gets steady work and doesn't have to manage their client list so it does work pretty well.

  - **cmui** · [2023-03-14 00:50 UTC](https://news.ycombinator.com/item?id=35145694)
    Mind sharing some details of your install - equipment model/size, controls, and cost of install? ^c35145694

    - **saenns** · [2023-03-14 01:32 UTC](https://news.ycombinator.com/item?id=35146112)
      I'm looking at this 36,000 BTU/h unit for \$3,750.  Pre-charged line sets make it accessible to homeowners ^c35146112

      [https://www.amazon.com/dp/B08FGLMZB8?\_encoding\=UTF8&aaxitk\=e...](<https://www.amazon.com/dp/B08FGLMZB8?_encoding=UTF8&aaxitk=ed3fa3131928ea09935bb813d3402e6f&hsa_cr_id=8690585940001&pd_rd_plhdr=t&pd_rd_r=c1aaa7f5-5c94-497f-825e-c6176906545d&pd_rd_w=TYrzG&pd_rd_wg=NL4Kn&linkCode=sl1&tag=riste00-20&linkId=8de9d42098df28b22f9c9e5af0fe9da9&language=en_US&ref_=as_li_ss_tl&th=1>)

      - **ireflect** · [2023-03-14 03:19 UTC](https://news.ycombinator.com/item?id=35146969)
        I installed a MrCool mini split a few years ago and it's still running great in both summer and winter. ^c35146969

        Installing one of these is a pretty advanced project for a typical home owner though. You have one chance to get those pre-charged linesets connected perfectly, and if you screw it up, good luck finding an HVAC contractor that will come and help you recover your botched installation of an off-brand heat pump.

        That said, there are certainly homeowners who are experienced enough to pull it off, and I'm glad these DIY products exist. I could see potential for further innovation from ElectricAir to make this sort of thing accessible to more people (at a higher cost, obviously, to pay for that sweet sweet design)

      - **cmui** · [2023-03-14 04:30 UTC](https://news.ycombinator.com/item?id=35147469)
        The size ratings are confusing. This is really a \~19kbtu unit at 5F. Most homeowners do not want a DIY solution, they want it professionally installed. And this system lacks air quality features (HEPA, fresh air intake, humidifier) and the thermostat. ^c35147469

      - **nixonpjoshua1** · [2023-03-14 05:49 UTC](https://news.ycombinator.com/item?id=35147864)
        That really isn't the same product, as I understand this is an HRV combined with heat pump system where they are software integrated to PID controls that optimize the level of fresh air and weather aware energy utilization, with a system like this and a startup I'm sure optimizations like this [https://youtu.be/0f9GpMWdvWI?t\=432](<https://youtu.be/0f9GpMWdvWI?t=432>) should be possible - this is like Dropbox, can't expect people to roll their own - and you need a fully integrated system to really make this work well without comfort, even simpler if cooling/heating is more efficient via bringing in fresh air this system could choose to do that vs running the heat pump at all! ^c35147864

      - **ricardobayes** · [2023-03-14 09:51 UTC](https://news.ycombinator.com/item?id=35149226)
        Looking at these US prices with envy. Heat pumps are just becoming a thing in Europe and currently installers are looking to earn a quick buck. I've not seen an install under 20k in the UK lately, bolting on to existing radiators. Also Europe seems to be heavily into air-to-water systems. ^c35149226

        - **stevekemp** · [2023-03-14 10:10 UTC](https://news.ycombinator.com/item?id=35149354)
          My wife paid 4000 euros for a heatpump in Finland, last year.  Mostly to be used for cooling during the summer, rather than for heating in the winters (since there is "district heating" available for that). ^c35149354

          Seemed pretty cheap, and the installation only took a day.

          - **oriolid** · [2023-03-14 15:32 UTC](https://news.ycombinator.com/item?id=35153145)
            Air-to-air is much cheaper than connecting to water flow radiator system. Radiators aren't that great for cooling anyway. ^c35153145

        - **sokoloff** · [2023-03-14 10:02 UTC](https://news.ycombinator.com/item?id=35149312)
          US (attempted) buyers of air-to-water look with envy to the Nordics, Northern EU, and the UK. My quote in the US was almost double that figure (for an installed system). The parts prices you’re looking at are indeed cheap. The labor is moderate. The profit margins are high. ^c35149312

        - **fnomnom** · [2023-03-14 10:26 UTC](https://news.ycombinator.com/item?id=35149441)
          \>are just becoming a thing ^c35149441

          where do you life? in germany they are available for years already. friends built new homes with them 5-6 years ago and back then it was already established

          in all differen varities. air or with geothermal pipes in your yard (either surface or drilled)

      - **bluGill** · [2023-03-14 02:14 UTC](https://news.ycombinator.com/item?id=35146455)
        Often you can get EPA certification and all the tools for less. But that system does get good reviews. ^c35146455

    - **divbzero** · [2023-03-14 01:03 UTC](https://news.ycombinator.com/item?id=35145849)
      Is there a straightforward way to estimate whether a small (24 kbtu), medium (36 kbtu), or large (48 kbtu) unit would be most appropriate for a given home? ^c35145849

      - **ta1243** · [2023-03-14 02:05 UTC](https://news.ycombinator.com/item?id=35146386)
        For reference for international users, 24 kbtu is 7kW, 36 is 10kW and 48 is 14kW ^c35146386

        I'm not a heatpump export, but if that's continuous output, with an SCOP of say 3.8 (what I had quoted in the UK for an airsource -\> water -- UK heating is typically hot water run from a boiler through radiators in each room rather than pumping hot (or cool) air direct to the romm via ducted which seems common in the US, perhaps because of the historical desire/need for aircon)

        That would require 1.8/2.6/3.7kW of electricity to run. In the UK at 35p/kWh that would mean 91p to generate 10kWh of heat. For reference my oil boiler at 95\% efficency and current prices is about 6p/kWh, but we have had insanely high electricity charges this year. Back in September my oil heating approached 10p/kWh -- about £1 a litre.

        - **ricardobayes** · [2023-03-14 09:53 UTC](https://news.ycombinator.com/item?id=35149245)
          I hear a lot of horror stories from the UK about this, that people pay upwards of £500 and still cold in their homes. There are a lot of cowboy installers going around but even those who are qualified can't be reached for aftercare/handoff etc. Fiddling with settings at 50p/kWh is not a great experience.
          On that note I think biopropane will be the solution for Europe. ^c35149245

          - **bkor** · [2023-03-14 15:08 UTC](https://news.ycombinator.com/item?id=35152710)
            \> I hear a lot of horror stories from the UK about this, that people pay upwards of £500 ^c35152710

            £500 for what? Total cost for a month? A year? The monthly average of a full year of costs. The monthly average cost thing is common in NL; people often have no clue other than knowing the monthly average cost. And it's often estimated beforehand by the energy company. It's assumed to be correct.

            Anyway, people need to check the SCOP instead of figuring out if it is efficient (COP) at a certain temperature.

            \> On that note I think biopropane will be the solution for Europe.

            Oh please no.

            On UK, I was in Scotland. I thought the homes in NL are often terrible quality. Scotland was another level. Pretty much no insulation, terrible windows. Really drafty. Yet the media (as a result the public as well) hates the "Insulate Britain" movement.

            - **ricardobayes** · [2023-03-17 19:15 UTC](https://news.ycombinator.com/item?id=35201572)
              Why no? Biopropane is fully renewable from biomass but on the other hand people think heating with electricity is somehow cleaner than other methods. Well, electricity production in Europe is not very clean at the moment and not will be (and can't be) renewable-based unless wind and solar conditions change drastically. Large-scale geothermal production is a pipe dream within our lifetimes.
              So while most homes in Europe are already connected to a pipeline we are demolishing that and figuring out from scratch how to heat drafty homes with heat pumps. I'm just saying maybe, we shouldn't throw out 50+ years of boiler knowledge just like that. ^c35201572

            - **ta1243** · [2023-03-15 13:54 UTC](https://news.ycombinator.com/item?id=35168369)
              A great deal of the problem is the inability to understand basic maths. This whole nonsense about a £2000 a year cap or whatever, rather than something nice and simple like a 35p/kWh electric cap, or a 7p/kWh gas cap, is both a symptom and the cause. ^c35168369

              The number of homes that could have improvements in insulation for tiny costs is astounding, but somehow insulating a home is some lefty woke thing.

      - **pkaye** · [2023-03-14 01:29 UTC](https://news.ycombinator.com/item?id=35146084)
        I think the proper method used by HVAC companies is called the manual J method. I found a simplified version below but the real thing involved a whole book. ^c35146084

        [https://www.indeed.com/career-advice/career-development/manu...](<https://www.indeed.com/career-advice/career-development/manual-j-calculation>)

        - **secabeen** · [2023-03-14 03:53 UTC](https://news.ycombinator.com/item?id=35147235)
          This page does the full Manual J, but it is challenging to do and understand.  I used it to confirm the estimates that my installer did without a full J workup, and it was helpful. ^c35147235

          [https://loadcalc.net/](<https://loadcalc.net/>)

      - **camel\_gopher** · [2023-03-14 03:14 UTC](https://news.ycombinator.com/item?id=35146942)
        If you have a Nest thermostat, some of the newer models give a usage display of how many minutes per hour they are running. This will tell you how much of your furnace's capacity is running at. For example, if I have a 40kbtu furnace, and I see a maximum of 15 minutes per hour usage on the furnace during a heating season, that means my usage maxes out at roughly 10kbtu. I might choose my heat pump based on that capacity; if I got a 10kbtu heat pump, I would expect it to be running continuously during the maximum usage time. ^c35146942

      - **cmui** · [2023-03-14 01:22 UTC](https://news.ycombinator.com/item?id=35146025)
        Not at the moment, working on a tool like this for the preorder site! There are btu/sq.ft. rules of thumbs that are not appropriate for heat pumps (you can easily oversize by 100\%). ^c35146025

      - **friendzis** · [2023-03-14 09:59 UTC](https://news.ycombinator.com/item?id=35149283)
        10-20 W/m2 is modern warm house, 30-40 - modernish house or well insulated old house, 60 - barely insulated, 100 - no insulation. Roughly. ^c35149283

        Assuming they mean kbtu/h continuous and not kbtu, 12kbtu/h is \~3.5kW. So, 7, 10, 14 KW units.

  - **petrusnonius** · [2023-03-17 10:08 UTC](https://news.ycombinator.com/item?id=35195127)
    Yeah and these can be bought on eBay already. ^c35195127

  - **hackernewds** · [2023-03-14 01:07 UTC](https://news.ycombinator.com/item?id=35145888)
    which heat pump did you install? mind sharing? ^c35145888

  - **derefr** · [2023-03-14 02:29 UTC](https://news.ycombinator.com/item?id=35146600)
    IIRC: heat pumps aren’t even available for sale in many markets, because distributors don’t see enough interest to stock them. ^c35146600

    See also: water beds.

    - **bkor** · [2023-03-14 15:10 UTC](https://news.ycombinator.com/item?id=35152751)
      \> IIRC: heat pumps aren’t even available for sale in many markets ^c35152751

      If you've installed an airconditioning system which can cool and heat up your home you've installed a heat pump (air/air). They're hardly magic.

- **spaceguillotine** · [2023-03-13 20:17 UTC](https://news.ycombinator.com/item?id=35141874)
  How will you compete with Goodman/Daikin and needing lineset runs with usually high voltage work and panel upgrades that sometimes come with converting to a heat pump. ^c35141874

  If you don't use 24V AC controls i don't think it would take off with any installers and you seriously limit and then hinder yourself needing way more customer support.

  What refrigerants are you considering as there is more environmental stuff coming out killing 410A.

  You will be competing against installers that can offer 10 year warranties (Bosch, Mitsubishi) without any of the backing of a large company saying parts will still be available and that is a big worry with start ups, at least when nest got bought you can still run systems without the cloud or could swap to any 24V controls system.

  I used to be an installer but am out of the trades now and I think you'd kind of off the mark with your shortcomings to the current experience, the biggest issue you're gonna find is duct leakage and contractors skipping out on the testing and then the old vac n run and the new construction builders literally will want whatever is cheapest and gets them through the build fastest (80\% gas single stage with a empty coil box is hella common)

  I hope you have seen the variety of retro installs that will need to be done as there are still lots of oil burners out there.

  Honestly i've almost talked myself into the idea that I should be working on this project. LMAO.

  Please tell me you aren't going to rely on internet and at least use local RTD sensors at least.

  - **Panino** · [2023-03-13 21:29 UTC](https://news.ycombinator.com/item?id=35143065)
    \> What refrigerants are you considering as there is more environmental stuff coming out killing 410A. ^c35143065

    I'm also interested in this. Specifically, I'm interested in R-744 (CO2) as it has a GWP (global warming potential) of only 1.  R-32 (Difluoromethane) has a GWP of 675 while R-410A has a GWP of 2088. Japan has had R-744 heat pumps for years now.

    Drawdown lists refrigeration improvements as the single most effective method (we need to do all of them) for combatting climate change.

    [https://www.drawdown.org/the-book](<https://www.drawdown.org/the-book>)

    - **cmui** · [2023-03-13 23:30 UTC](https://news.ycombinator.com/item?id=35144786)
      Some background on CO2 systems. On the one hand, great, because CO2 has a GWP of 1 as you point out. On the other, the operating pressures are much higher than other conventional refrigerants (80+bar vs 20bar). Because of this high pressure the components are more expensive, and you don't see any field installs of refrigerant lines like in a mini-split setup. Instead the CO2 systems typically come as factory sealed air-water systems. ^c35144786

  - **cmui** · [2023-03-13 23:21 UTC](https://news.ycombinator.com/item?id=35144661)
    24V controls: Any inverter heat pump will run best with a communicating thermostat. We can make efficiency sacrifices to run the system on 24V controls, but it would not be my recommended setup. ^c35144661

    Refrigerants: this is largely dictated by compressor availability. At this point it looks like R454B is the winner (GWP 467)

    You're right about new construction builders wanting whatever is cheapest. They don't bear the cost of ownership, so there's very little incentive to go for efficient equipment. Doing replacements on oil is great! The monthly savings when moving from electric resistance, propane and fuel oil are huge.

    Connectivity - system runs fine standalone without any internet connection.

    If you decide to get in the heat pump game come say hi at the next AHR expo!

    - **runnerup** · [2023-03-14 02:32 UTC](https://news.ycombinator.com/item?id=35146621)
      Can you open the communication API so that FLOSS licensed software/hardware can run the unit instead of replacing/repairing your interface? ^c35146621

      - **enriquto** · [2023-03-14 08:23 UTC](https://news.ycombinator.com/item?id=35148661)
        He will reply with a pile of word salad again and again, never addressing the crucial API issue. ^c35148661

- **turtlebits** · [2023-03-13 16:58 UTC](https://news.ycombinator.com/item?id=35138582)
  Existing established companies offer centrally ducted heat pumps. You can purchase them direct, and are even sold by your big box home improvement stores. (search for "ducted heat pump) ^c35138582

  They are generally contractor only as homeowners generally can't DIY the 240v electrical and lineset hookup.  What exactly is being improved upon by your startup?

  - **cmui** · [2023-03-13 17:24 UTC](https://news.ycombinator.com/item?id=35139068)
    A few major improvements - (1) Purchasing experience, we'll connect you with a local contractor, arrange financing and help with rebates. (2) HEPA filtration, fresh air intake and humidity control fully integrated into the system, actuated off PM2.5 and CO2 sensors in the thermostat. (3) A smart thermostat that is optimized for operation with a variable speed heat pump, and reduces your monthly bills. (4) Help for the contractors in the form of a web app to do load disaggregation for heat pump sizing and figure out if the existing ducts can be used for the install. This is something a lot of contractors need an effective tool for. ^c35139068

    - **lancesells** · [2023-03-13 18:11 UTC](https://news.ycombinator.com/item?id=35139916)
      I'm really not sure how any of this is worth the extra \~\$8k in price difference. Not saying there aren't people out there willing to buy but it's not for me. ^c35139916

      1 - I already have a local contractor and financing shouldn't be a reason it costs more.
      2 - This is \~\$500 and I already own a air purifier.
      3 - This is \~\$200 and I already own a thermostat.
      4 - I can't speak to the value in this but in my case I don't have central ducts.

    - **portpecos** · [2023-03-13 18:23 UTC](https://news.ycombinator.com/item?id=35140119)
      Are you considering following in the footsteps of Project Solar? I've received 20 quotes from other solar companies like Solar Run as well as local solar companies, and they're quoting me around \$3-\$6/watt. This price includes their sales commission. Project Solar, on the other hand, eliminates the middleman, allowing us to purchase their system for just \$2.2/watt. Those \$3-\$6/watt quotes didn’t make long-term sense to us. Project Solar made financial sense to us. ^c35140119

      As a VC-backed startup, it's worth checking out their business model.

      This is a big deal because if you can beat the rates of your competitors and guarantee a quality workmanship, then that takes away the 100+ hours we spend on sourcing quotes and negotiating better prices.

      Here’s a story about what happens when you DON’T spend 100+ hours sourcing multiple quotes. You end up with a \$36,000 heater + air conditioning unit where the installer caused a leak to occur on on the second floor. We were so desperate for cold air that we didn’t have time to get 20 quotes, but the 5 other quotes we did get ranged from \$48k to \$64k.

      If you can save us that 100+ hours of time and give us a cheaper deal while guaranteeing workmanship, then I’m sold.

      We’re getting really really really tired of overly inflated prices and the negotiation process.

    - **tjmc** · [2023-03-14 01:38 UTC](https://news.ycombinator.com/item?id=35146167)
      HVAC engineer here - this looks great Chris. How are you doing the humidity control out of interest? I've done a few datacentres that won't touch ultrasonic humidifiers because they generate dust in areas with hard water. Less of an issue in resi but perhaps something to consider. Also, are you doing energy recovery for your fresh air intake? If you're ducting both intake and exhaust/spill, is there any opportunity to direct the exhaust/spill air back through the external condenser on the way out to get some extra efficiency? ^c35146167

    - **runako** · [2023-03-13 18:23 UTC](https://news.ycombinator.com/item?id=35140131)
      First -- good luck with this! ^c35140131

      \> Purchasing experience, we'll connect you with a local contractor, arrange financing and help with rebates.

      Hopefully constructive feedback: I replaced 2 of our residential furnaces within the last few years, in two separate transactions with two different vendors. I can say that this pitch doesn't resonate as an improvement because vendors already make this turnkey.

      You call a furnace/air conditioning company, they come out and recommend a unit. You sign their financing thing, they come out the next day and install. I interacted with a single primary person (on-site) at each company. Cost aside, it's actually one of the more pleasant buying experiences of any major home improvement.

      Finally, I can tell you who installed the (\$\$\$\$\$) units but I definitely could not tell you who made them. Branding might be tough unless you do the installs yourself.

      - **cmui** · [2023-03-13 18:31 UTC](https://news.ycombinator.com/item?id=35140253)
        Thanks for the feedback. If you feel comfortable saying, what region are you in? I think where you might start running into friction is if you want a heat pump vs a furnace. There's a lot of variation between local markets in terms of heat pump install competence. ^c35140253

        - **jdmichal** · [2023-03-14 15:06 UTC](https://news.ycombinator.com/item?id=35152681)
          I agree with runako.  I suspect that you are going to have a hard time targeting areas where heat pumps are already common for cooling. ^c35152681

          I'm in Florida.  We got our A/C replaced a few years ago.  Got quotes from three companies with varying ranges and the one we chose knocked it out in a (long) day.  Including various "side-jobs" such as running a new electric line with a larger gauge, installing a hurricane pad, removing the loopback with the water heater, and lifting the air handler into the attic.

          Total cost was under \$8k.  None of the quotes, including for name-brand units, were above \$12k.  \$18k for an unknown name seems just right out to me.

        - **runako** · [2023-03-13 19:36 UTC](https://news.ycombinator.com/item?id=35141244)
          I’m in the southeastern US, USDA Zone 8. ^c35141244

  - **potatolicious** · [2023-03-13 17:30 UTC](https://news.ycombinator.com/item?id=35139194)
    In addition to the *software* concerns above, I would have severe reservations about the ongoing maintenance of the system. ^c35139194

    How would maintenance be handled? There are a large number of contractors in my area that can service the major brands. Would maintenance come from the company itself, or via third party partners? If third parties, what if they prove unreliable? Will there be enough diversity in providers to give me choice?

    More importantly, what happens if the startup is acquired or shuts down? This is an expensive kit that, depending on system sizing, costs as much as a car. I need this type of system to work for years, with high availability of parts and labor, and replacement as-required.

    Going with a new company in this space seems *deeply* risky. And yeah, the existing manufacturers don't play super nicely with smarthomes and cloud-based control and whatnot, but it's far from enough of a pain to offset the risk IMO.

  - **mjhay** · [2023-03-13 20:48 UTC](https://news.ycombinator.com/item?id=35142326)
    Those established companies don't have units with smart thermostats that get bricked if the company goes out of business. ^c35142326

- **WaitWaitWha** · [2023-03-13 18:48 UTC](https://news.ycombinator.com/item?id=35140494)
  Please consider on-boarding to Home Assistant. ^c35140494

  Avoid proprietary protocols to communicate between sub-systems as much as possible.

  The system should be self contained *from the start* and must be able to function without a local network & internet.

  Do not require internet connectivity, a hub, or some intermediary solution if a third party system (such as Home Assistant) wants to communicate to the system.

  My biggest fear is attempt to lock me into an ecosystem that charges me a monthly fee to just exist, while selling data about me.  *No promise* will make this fear go away, as consumers mistreated many many times in the past. Show it through your open design.

  Good luck.

  \> What issues have you had with your existing heat and cooling, and do you have any interesting stories around a heat pump install or use? I would love to hear your ideas, experiences, and feedback on any and all of the above!

  Fan motor on compressor broken, company insist everything needs changed.  Another similar incident was with a capacitor.  Such rip-offs create a disdain in consumer.

  In some very cold nights, the heat pump fails to keep the heat and emergency/aux heat kicks in.

  - **cmui** · [2023-03-13 21:52 UTC](https://news.ycombinator.com/item?id=35143433)
    I hear your concerns! Just want to reiterate (since this is one of the top comments) no internet connectivity is required to operate the system. We will have integrations that also allow you to change the setpoint with your home system of choice. We're not interested in holding people hostage, we want to make the best way to heat and cool your home, and make it easy to get. If you're willing to turn on wifi, you can ingest demand response, weather and rate plan signals to optimize energy, and remotely operate the system. ^c35143433

    - **alangibson** · [2023-03-14 09:33 UTC](https://news.ycombinator.com/item?id=35149091)
      \> We're not interested in holding people hostage ^c35149091

      This one isn't your fault, but many people aren't going to believe you. What they will hear is "We're not interested in holding people hostage (until we need some of that sweet subscription revenue)". And they'll know that features can be paywalled with a simple firmware update.

      - **TheCoelacanth** · [2023-03-15 02:01 UTC](https://news.ycombinator.com/item?id=35162742)
        Or "We're not interested in holding people hostage (but the people that acquire us will be)". ^c35162742

  - **ilamont** · [2023-03-13 19:53 UTC](https://news.ycombinator.com/item?id=35141512)
    \> The system should be self contained from the start and must be able to function without a local network & internet. ^c35141512

    Rural users often have limited or no access to Internet service, yet need technology like this to heat and cool their homes.

    - **mydriasis** · [2023-03-14 00:53 UTC](https://news.ycombinator.com/item?id=35145731)
      Hey, that's me! We wound up getting a pellet stove, super cheap to operate and very efficient so far, but I'd also be open to a heat pump at the right price range. We're some of the few with high quality Internet.
      Lots of my neighbors have wood burning stoves or pellet burners, because they're so cheap to operate compared to the next possibility, which is propane, a very expensive fossil fuel. ^c35145731

      Pellets being renewable is great, but if the heat pump does just as well, or at least assists, they might get lots of rural bites. I'm excited to see where this goes.

      - **bozertron** · [2023-03-14 14:59 UTC](https://news.ycombinator.com/item?id=35152541)
        Me too! ^c35152541

        Rural and temperate? Great. Rural and cold? Not great.

        I have a heat pump that's rated to -30C. The energy benefits fall off a cliff when it gets cold.

        Can use as primary in the summer and parts of the shoulder seasons. Useless in the winter from a cost perspective.

        I think the direction of the industry is great. Needs some R&D cycles to become a primary for all.

        - **mydriasis** · [2023-03-14 16:18 UTC](https://news.ycombinator.com/item?id=35153911)
          Aw, bummer. Yeah, we're up in Ohio -- not the coldest, but wintery enough. Here's hope for the future! Like you said, perhaps with enough R&D... ^c35153911

    - **WaitWaitWha** · [2023-03-13 20:01 UTC](https://news.ycombinator.com/item?id=35141652)
      Yes, the internet is not as ubiquitous as some might presume, and not just in rural areas.  Some newly developed suburbs of large cities do not have internet connectivity, not even Starlink yet.  I have learned about this in Ohio, Delaware, Texas, and most recently in Florida.  Some where just too isolated & not big enough for the carriers, some were blocked by politicking, and some I have no idea why. ^c35141652

  - **scwoodal** · [2023-03-13 23:02 UTC](https://news.ycombinator.com/item?id=35144403)
    \> Fan motor on compressor broken, company insist everything needs changed. ^c35144403

    Ugh, this happened to me recently.

    “It’s an old system and the replacement parts can’t be found. Have to replace the whole thing. \$12k”

    After they leave I found a replacement on Amazon and replaced it myself 2 days later in under an hour.

- **sabareesh** · [2023-03-13 17:07 UTC](https://news.ycombinator.com/item?id=35138754)
  Typical medium unit at market place is only around 3K compared to your offering at 12k. Why is it so expensive [https://www.homedepot.com/p/Pioneer-36-000-BTU-3-Ton-18-SEER...](<https://www.homedepot.com/p/Pioneer-36-000-BTU-3-Ton-18-SEER-Ducted-Central-Split-Air-Conditioner-Heat-Pump-System-DYR3036GMFI18R/314800196>) ^c35138754

  - **cmui** · [2023-03-13 17:19 UTC](https://news.ycombinator.com/item?id=35138964)
    Fair point, I should do a better job of communicating the unit sizes. Heat pump capacity varies as a function of outdoor temps. A standard unit is rated at 47F but the sizes I'm showing are at 5F (cold climate conditions). Also for this price you get the air quality module which does HEPA, fresh air intake and humidification and a smart thermostat that's designed to fully optimize this heat pump system. ^c35138964

    - **danielmarkbruce** · [2023-03-13 18:50 UTC](https://news.ycombinator.com/item?id=35140533)
      First - this thing is awesome so nice going. ^c35140533

      Second - yes, significantly better communication on the website is going to help. Some economic analysis (the section of savings is ambiguous) with specifics, specifics on how it would look with financing, for different house sizes etc would get a lot of people across the hump. It's quite unclear to me if this thing makes sense financially.

      Third - nice going, this really is awesome.

    - **turtlebits** · [2023-03-13 17:30 UTC](https://news.ycombinator.com/item?id=35139180)
      If you want to control air quality, you do this with a separate fresh air intake, not with a ducted furnace.  Many older homes have furnaces taking air from sub-optimal spaces such as garages or crawl spaces. ^c35139180

      - **cmui** · [2023-03-13 18:49 UTC](https://news.ycombinator.com/item?id=35140513)
        Great point. You don't source from the same spot you source combustion air - you run a separate fresh air intake. This system has HEPA, fresh air intake and humidity control packaged/integrated together well. The fresh air wouldn't come from a garage or crawl space, but from the outdoors via a dedicated (small) duct. ^c35140513

      - **heatpumpfan** · [2023-03-13 17:37 UTC](https://news.ycombinator.com/item?id=35139335)
        [flagged] ^c35139335

        \[dead\]

    - **sosodev** · [2023-03-13 17:53 UTC](https://news.ycombinator.com/item?id=35139624)
      When you say it's rated at 47F do you mean its efficiency is measured at 47F? If so, does that matter much? ^c35139624

      The unit linked in the post you're replying to states that it can operate as low as -13F.

      - **cmui** · [2023-03-13 19:57 UTC](https://news.ycombinator.com/item?id=35141569)
        Talking about capacity for heat pumps is tricky, their available heating power changes continuously as a function of outdoor temperature. The convention is to refer to the available capacity at 47F for 'normal' heat pump and the capacity at 5F for a cold climate heat pump. ^c35141569

        - **sosodev** · [2023-03-13 21:09 UTC](https://news.ycombinator.com/item?id=35142697)
          Makes sense. How much does their capacity typically change over their operating temperature range? ^c35142697

          - **malfist** · [2023-03-14 15:21 UTC](https://news.ycombinator.com/item?id=35152938)
            Heat pumps extract heat, either from the house, or from the outside air. ^c35152938

            When heating, it pulls it from the outside air. As it gets colder, there is less heat to pull out. Typically heat pumps will still keep pulling heat at \>100\% efficiency nearly into the negatives, but the amount they're extracting isn't enough to keep up with the heat loss of the house.

            Heat lost of the house is a factor of insulation, surface area and heat gradient. It's a lot harder to keep a house at 68F when it's 5F outside than it is when it is 50F.

            So when it's cold out, you need more heat generation, and there's less heat to pull from the air. That's why heat pumps have backup auxiliary heat.

    - **sabareesh** · [2023-03-13 17:46 UTC](https://news.ycombinator.com/item?id=35139484)
      Do you have product specification sheet like this [https://images.thdstatic.com/catalog/pdfImages/96/96c34548-a...](<https://images.thdstatic.com/catalog/pdfImages/96/96c34548-a354-49c1-8e73-6661e493ada3.pdf>) ^c35139484

      You say 5f but I dont see any reference to that on your site.

    - **cosmosisjones** · [2023-03-13 17:27 UTC](https://news.ycombinator.com/item?id=35139125)
      so what about places like Duluth, MN where it can be  -20F ambient, then -40F to -50F with a windchill for several weeks of the year? ^c35139125

      - **elil17** · [2023-03-13 18:02 UTC](https://news.ycombinator.com/item?id=35139770)
        Windchill doesn't effect, and you can handle small dips below -15 F (like for a couple hours at night) because the house has some thermal mass. However, Duluth, MN is right at the edge of being too cold for this heat pump (99th percentile cold temperature in the coldest month is -15.16 F). If I was in Duluth and was considering a heat pump, I'd want to make sure I had an electric furnace or some space heaters as a backup. However, it would still be worth it to get the heat pump because you'd be able to heat your home much more efficiently/cheaply \>99\% of the time. ^c35139770

        - **hedora** · [2023-03-13 22:12 UTC](https://news.ycombinator.com/item?id=35143727)
          Even in coastal California, most ducted heat pumps have a built in electric or gas furnace. ^c35143727

          I imagine anything sold in areas where it actually gets cold will as well.

          - **PaulDavisThe1st** · [2023-03-13 23:59 UTC](https://news.ycombinator.com/item?id=35145144)
            Here at 7000' near Santa Fe, I know dozens of homes, many new construction, that are heat pump only to all effects and purposes (i.e. they may also have fireplaces but these are not part of the normal heating systems nor part of any plan for the 0F-5F winter nights we can get. ^c35145144

            Heat pumps can handle things by themselves down to around -10F to -15F, if correctly sized and installed.

            - **hedora** · [2023-03-14 02:12 UTC](https://news.ycombinator.com/item?id=35146439)
              What brand? ^c35146439

              Most of the low temperature ones I’ve seen include resistive heating.  At some point the COP of the heat pump approaches 1.

              Also, having heat to -15, then switching to no heat isn’t ideal.

              - **PaulDavisThe1st** · [2023-03-14 05:46 UTC](https://news.ycombinator.com/item?id=35147854)
                Mitsubishi. Their "extreme" models do not switch to resistive heating, but deal with the critical problem at very low temps: partial freezing of the refridgerant. They divert some of the heat into fully melting the refridgerant. This reduces the COP but keeps them functioning. ^c35147854

      - **mikeyouse** · [2023-03-13 17:30 UTC](https://news.ycombinator.com/item?id=35139198)
        It's not designed for those areas.  The world is plenty large, they don't need to accommodate every single address in the country to have a viable or useful product. ^c35139198

      - **GauntletWizard** · [2023-03-13 17:44 UTC](https://news.ycombinator.com/item?id=35139462)
        I would be very interested in stats on the gradient of home energy use by average outdoor temperature. I imagine that "Places where it gets too cold for heat pumps" represent a large percentage of heat usage; That is, there's (made up numbers) 10\% of the population living in those areas, but they represent 90\% of heating energy use. ^c35139462

        If every home that could use your heat pumps year-round installed one and used it exclusively, what's the upper bound on energy saved? If every home across the country installed one and used it primarily (whenever it was warm enough outside), what would be the energy savings? Not to disparage, I'm certain it's still significant, but I'm curious to quantify it.

        - **mikeyouse** · [2023-03-13 20:11 UTC](https://news.ycombinator.com/item?id=35141787)
          This is quantified by "heating degree days" and I don't think your intuition is correct here. ^c35141787

          [https://upload.wikimedia.org/wikipedia/commons/d/da/United\_S...](<https://upload.wikimedia.org/wikipedia/commons/d/da/United_States_Heating_Degree_Day_map%2C_1961-1990.jpg>)

          The difference between "Can use a heat pump" and "can't" is only maybe 10º or 15º. The coldest places are only \~20\% colder than much more populated areas with millions of more residents.

          Metro Boston has around 5 million people -- that's more than 3x as many as who live in North Dakota and South Dakota combined.  Their climate is cold and they get around 6,000 HDD every winter compared to the frigid upper plains who average something like 8,000 or 8,500. So 1.3x more heat requirement per person but spread out across 1/3 as many people.

          Not to mention all of e.g. Chicago, Denver, Des Moines, Cleveland, Detroit, New York, the rest of New England, etc. etc. where heat pumps do just fine.

      - **throitallaway** · [2023-03-13 18:11 UTC](https://news.ycombinator.com/item?id=35139926)
        Windchill is irrelevant here, it only indicates what the temperature feels like to warm blooded mammals. ^c35139926

        - **nkurz** · [2023-03-14 02:01 UTC](https://news.ycombinator.com/item?id=35146355)
          I was tempted to give a similar answer, but I'm not so sure it's irrelevant.  Yes, the windchill won't affect the energy efficiency of the heatpump.  But it will affect the rate at which the house loses heat, and thus the BTU's the system needs to provide to maintain a temperature.  If the heatpump has been exactly sized to maintain a house temperature of (say) 70F at the expected winter low, adding a strong wind on the exterior of the house seems like it might make for a chilly morning.  The effect isn't as strong as it is for bare skin at body temp, and hence the exact numbers will be off, but it's still there, right? ^c35146355

        - **doctoboggan** · [2023-03-13 18:22 UTC](https://news.ycombinator.com/item?id=35140105)
          windchill as a concept can be applied to all evaporative cooling systems. ^c35140105

          - **16bytes** · [2023-03-13 19:32 UTC](https://news.ycombinator.com/item?id=35141189)
            Heat pumps are not an evaporative system. ^c35141189

            You can't lower the temperature across a gradient lower than the fluid temperature, no matter how fast that fluid is moving.  You can cool things down faster, but you can't go lower.

            So if it's 10F, a 5F heat pump will work equally well at 0mph wind and 30mph.

            - **cmui** · [2023-03-13 20:01 UTC](https://news.ycombinator.com/item?id=35141651)
              You got it. A brief technical aside, heat pump performance is hurt by frosting, which happens at intermediate outdoor temps (\~35-50F). Basically the outdoor coil is both below freezing, and below the dewpoint of the air. The frost forms a thermal insulating layer around the coil, and intermittently you have to run a defrost cycle to melt off the ice. This is a small hit to system efficiency. ^c35141651

            - **doctoboggan** · [2023-03-13 20:10 UTC](https://news.ycombinator.com/item?id=35141782)
              Yes, I never claimed they were. I was responding to the idea that only warm-blooded mammals have the concept of wind-chill. Any system that takes advantage of evaporative cooling will have the concept of wind chill. A "swamp cooler" is one example. ^c35141782

      - **ROTMetro** · [2023-03-13 18:07 UTC](https://news.ycombinator.com/item?id=35139869)
        Custom ground source heat pump my friend :) side benefit (energy cost) free hot water. ^c35139869

        - **cmui** · [2023-03-13 18:28 UTC](https://news.ycombinator.com/item?id=35140208)
          Ground source is great! (if you can afford the install). ^c35140208

      - **unknown** · [2023-03-13 18:58 UTC](https://news.ycombinator.com/item?id=35140690)
        [deleted] ^c35140690

      - **triceratops** · [2023-03-13 21:59 UTC](https://news.ycombinator.com/item?id=35143559)
        Not every product is for everyone. ^c35143559

- **Animats** · [2023-03-13 17:24 UTC](https://news.ycombinator.com/item?id=35139067)
  "Preorder". "Shipping Winter 2024". ^c35139067

  "While we don't have any physical prototypes at the moment, we have the industrial design and also largely understand how this will be built."

  No. You have to build it before you can sell it.

  - **leviathant** · [2023-03-13 19:01 UTC](https://news.ycombinator.com/item?id=35140746)
    Reminds me of Noria (later Kapsul), a somewhat early Kickstarter darling that promised to have revolutionized window air conditioners. Theirs would be quiet and light, and inexpensive (\$250!), and would ship within a year, all they needed to do was raise \$250,000! ^c35140746

    The timeline graphic is still up here: [https://www.kickstarter.com/projects/kurt/noria-cool-redefin...](<https://www.kickstarter.com/projects/kurt/noria-cool-redefined>)

    They raised nearly \$1.5MM, because as it turns out, people will throw money at a solution that sounds amazing, regardless of their understanding of manufacturing and physics. They finally started delivering some five years later, and what they delivered amounted to a repackaged traditional window air conditioning unit. Still noisy, still heavy, and the build quality wasn't great. Cf. [https://www.phillymag.com/news/2021/06/23/kapsul-air-conditi...](<https://www.phillymag.com/news/2021/06/23/kapsul-air-conditioner-noria-kickstarter/>)

    Johnson Controls does \$20-\$30 billion in annual revenue. They've swallowed up all kinds of other HVAC companies over the decades. Turns out, there's not a whole lot of innovation to be had in the HVAC world, because of the limitations of physics.

    Nest, on the other hand, did some wildly overdue disruption on the control side of things, doing a little bit of math on historic local data to help figure out how to cycle radiators more efficiently, but for the most part, the cost savings tended to be from Nest suggesting that it's silly to be running your AC at 68 degrees F on a 98 degree day.

    I appreciate there's an attempt to be transparent at the cost here, but "shipping winter 2024 even though we don't have a physical prototype" for an HVAC system is as big a red flag as there is, to me.

    - **SamBam** · [2023-03-14 02:48 UTC](https://news.ycombinator.com/item?id=35146738)
      I was reminded of Noria/Kapsul as well. I paid the \$1 for the chance to opt in later, so I was still getting their apologetic emails to customers as of last year, six years after backing. ^c35146738

      The last email (May 2022) said they had delivered to \~700 backers, and had "a long way to go."

      No further news since then.

  - **cmui** · [2023-03-13 17:46 UTC](https://news.ycombinator.com/item?id=35139489)
    I get where you're coming from. There's a lot of scope to this though, and not a lot of technical risk. I think in this case it makes sense to sell units, and also generate feedback about the product as early as possible. We're not selling fusion or self driving cars. ^c35139489

    - **joezydeco** · [2023-03-13 19:45 UTC](https://news.ycombinator.com/item?id=35141373)
      *Where* will you be building these? ^c35141373

      *I think in this case it makes sense to sell units, and also generate feedback about the product as early as possible*

      So you're going to use end customers as your test base? That's pretty gutsy. Especially when they're shelling out \$10K and ripping out their existing (and *working*) HVAC system to do this. Don't use the car analogy here, there's no backup if it doesn't work.

      Unless you predict 100\% flawless execution and satisfaction on that aspect, you're going to get screwed. Your customers, more so. A few fucked up installations, or performance below expectations, and it's over.

      - **cmui** · [2023-03-13 20:10 UTC](https://news.ycombinator.com/item?id=35141779)
        Definitely agree that a good customer experience is key here. We're not shipping half baked hardware to end customers. That's what engineering development (alpha build, design validation build, production validation build, home pilot) is for. After all that happens, then customers can an install (and one that's well designed and tested). ^c35141779

        - **joezydeco** · [2023-03-13 22:20 UTC](https://news.ycombinator.com/item?id=35143847)
          I guess your definition of "feedback" is different than mine. Maybe that's a Tesla thing. ^c35143847

        - **freedude** · [2023-03-15 17:09 UTC](https://news.ycombinator.com/item?id=35171432)
          "We're not shipping half baked hardware to end customers. That's what engineering development (alpha build, design validation build, production validation build, home pilot) is for." ^c35171432

          I can appreciate that. I am sure you will also agree a single part of a complex system can render it inoperable. When I consider the consequences, at 15° F (which is about the yearly low in my part of the US), of a failed part then I consider what that means to my wife and children and the value of the experimental but proven design becomes much less.

    - **simonebrunozzi** · [2023-03-13 21:30 UTC](https://news.ycombinator.com/item?id=35143067)
      In this particular case, and given your background, I am not worried about your ability to build it. Yes, a bit easier than fusion energy :) ^c35143067

      I am wondering, though... Why don't you make a prototype, and attach a webcam in front of it, with a few sensors, etc?

      - **lancepioch** · [2023-03-14 20:38 UTC](https://news.ycombinator.com/item?id=35158125)
        For their cheapest model, they want to sell it at \$10k which includes profit, but they can't build a single working one before that? Several thousand to build a single functional prototype is a drop in the bucket comparatively. This instills absolutely zero confidence that they could build anything... because well they've apparently built nothing except a preorder website full of mockups. ^c35158125

- **z3ugma** · [2023-03-13 16:57 UTC](https://news.ycombinator.com/item?id=35138564)
  Chris, one of my biggest worries is that your startup will get acquired or go out of business and then the firmware will leave me with a \$14,000 brick. ^c35138564

  What if I want to keep using the cloud-based thermostat when your servers get shut off or moved to another system, or if something like Google Nest closing down their API happens after you've exited?

  This is an expensive system with an expected long life, and I'd want some guarantees that I can control it entirely myself.

  - **cmui** · [2023-03-13 17:09 UTC](https://news.ycombinator.com/item?id=35138796)
    I totally get this concern. Any good piece of critical home infrastructure should be able to operate without the cloud or an internet connection. Following this logic the thermostat + heat pump combination can operate fine without the cloud. You leave some optimized behavior on the table like demand response and weather response, but everything else will work (you'd have to manually enter your TOU rate plan to get that energy optimization). ^c35138796

    - **daredoes** · [2023-03-13 17:23 UTC](https://news.ycombinator.com/item?id=35139058)
      Would your company be willing to provide an open-source local-first websocket-based integration with [https://www.home-assistant.io/](<https://www.home-assistant.io/>) or use the new Matter + Thread standard to provide it for everyone? ^c35139058

      If that's available, this would be my top choice as I'm actively shopping for all-electric heat pumps

      - **cmui** · [2023-03-13 17:29 UTC](https://news.ycombinator.com/item?id=35139170)
        It's something we'd definitely consider. Is the desire to have thermostat control via any third party? ^c35139170

        edit - The current plan has been Matter/thread Homekit + Google Home integration. We can expose at least temperature control via this to everyone.

        - **xxpor** · [2023-03-13 17:46 UTC](https://news.ycombinator.com/item?id=35139485)
          (not OP, but I also use HA) ^c35139485

          The important bit is to have an open API that can be connected to from the local network (or via Matter + Thread, etc), and via a cloud. Then anyone can develop a client. This also has benefits in UX: the latency to update is much lower than cloud based polling, since that's almost always rate limited.

          The closer anything is to the bottom of the chart here, the better. When buying something as expensive as a heat pump, I wouldn't even consider something that isn't at least local polling:

          [https://www.home-assistant.io/blog/2016/02/12/classifying-th...](<https://www.home-assistant.io/blog/2016/02/12/classifying-the-internet-of-things/>)

          That being said, I'm not opposed to *value add* things via cloud services. Want to get the weather via a cloud service, even if that changes the schedule? Totally fine! But ultimate *control* must be local.

          - **snuxoll** · [2023-03-13 21:44 UTC](https://news.ycombinator.com/item?id=35143282)
            Agreed, this isn't a \$100 thermostat that I can just pull off the wall and replace - we're talking an expensive investment with a 10+ year lifespan. That said, even for my thermostat not being bound to the cloud was an important reason I went with Emerson/Sensi (the only value-add I lose if their cloud goes down is usage reporting, everything else I can do with the native Homekit support). ^c35143282

        - **mabbo** · [2023-03-13 17:43 UTC](https://news.ycombinator.com/item?id=35139426)
          Consider it is as a competitive advantage. ^c35139426

          An API that is public, well-documented, and easy for other systems to securely integrate with would mean that customers get the integration they want. If someone builds a better way to utilize your system, then you just got value-add on your product at basically zero cost.

          Amazon can hook Alexa into it. Google can hook their Home thing into it. And whatever comes next, whatever doesn't even exist today, should have an easy time integrating, continuing to add value.

          - **RicDan** · [2023-03-13 18:09 UTC](https://news.ycombinator.com/item?id=35139894)
            Completely agree on this point. I've worked over half a decade with smart home systems, and it's just so much easier (and cheaper!) to integrate well documented, open APIs (and please make them secure, I have nightmares of all the open, unencrypted UDP based alarm systems) that is purely local. This means we would highly recommend these products even tho we made zero money off them, and customers would actually prefer them as well - it's well beyond the time of people naively buying this stuff, and they know that clouds can just "go offline". ^c35139894

            What also can't be underestimated is the tinker community. Many people in the smart home business are tinkerers themselfs; create a great product for them and they will inevitably try to use it at their job. But this really isn't only applicable to integrators, really.

        - **tedivm** · [2023-03-13 23:26 UTC](https://news.ycombinator.com/item?id=35144726)
          If you support home assistant then I am far, far more likely to purchase this. My wife and I are buying a house sometime over the next year and one of my higher priorities is getting a heat pump. At the same time though I also refuse to use cloud based services and instead prefer to run my own home assistant installation. ^c35144726

          You should consider this a huge marketing opportunity- the home assistant people are obsessed with perfecting HVAC (half of these people have their own weather stations) and are also the kind of geeky first adopter who will push useful tech on all their friends. It's also not a small community, as the subreddit alone has over 222k people on it.

          [https://old.reddit.com/r/homeassistant/](<https://old.reddit.com/r/homeassistant/>)

          - **mox1** · [2023-03-14 00:16 UTC](https://news.ycombinator.com/item?id=35145325)
            I just preordered and I will echo this. ^c35145325

            On track to replace my gas furnace in the next few years, this sounds awesome, but HA integration would be very highly desired.

        - **simonebrunozzi** · [2023-03-13 20:55 UTC](https://news.ycombinator.com/item?id=35142436)
          Chris, I think there's a lot more here to uncover. Most of your competition has no sensitivity, and almost no openness, about these aspects. I think this could become a really important part of your go-to market, but also a differentiator vs other products. ^c35142436

          I'm a VC since recently, but have been a tech guy for a long time. Feel free to ping me if you'd like to discuss it further. \$HN\_username at gmail.

        - **ukd1** · [2023-03-13 18:00 UTC](https://news.ycombinator.com/item?id=35139739)
          HA user here as well, having a non-locked down API at minimum (i.e. not actively trying to stop folks using it), through to an open and documented api (would be great), through to open firmware (would be best) and or releasing your own integration for HA would likely get you those kinda customers. ^c35139739

          - **cmui** · [2023-03-13 18:14 UTC](https://news.ycombinator.com/item?id=35139964)
            If people have a preferred way of integrating their devices, like home assistant, I'd want to make that possible for people to do with Electric Air. ^c35139964

            Re the sizing question - this is a part of the site that needs improvement. 12kbtu is 1 ton. The 48kbtu system is a 4ton system, but rated at 5F, if you're in a more temperate climate, two of these will likely have plenty of capacity for you. It's also likely that your current system is oversized.

            - **StrangeATractor** · [2023-03-13 20:27 UTC](https://news.ycombinator.com/item?id=35142020)
              As someone about to be in the market for something like this, propriety lockout is a complete deal breaker for me. ^c35142020

              /2¢

            - **pkulak** · [2023-03-13 21:09 UTC](https://news.ycombinator.com/item?id=35142704)
              The good news, at least, is that almost anything will work. You don't need full Matter support for Home Assistant folks to be happy. The bare-minimum, local REST api built on a Monday by an intern will do it. Someone will write the Python code to fully integrate it. I get that there would be some security concerns there, but you get my drift. ^c35142704

              - **briHass** · [2023-03-14 01:12 UTC](https://news.ycombinator.com/item?id=35145935)
                If worried about security concerns, just provide a common port interface (RJ-45/RJ-11) on the unit with a simple, well-documented, serial-based protocol on RS485/RS232. You can sell an add-on device to bridge that to Ethernet/simple API, and easily replace/recall that inexpensive module if there are issues. ^c35145935

                The hackers will do what they want to anyway, and they'll implement cool interfaces/HA plugins/controllers on RPis or ESP32s for free. Someone will get enterprising and package a pre-built/programmed ESP32 unit that makes it plug-and-play for nerdy, but less capable users, and your company can avoid any liability from users using an 'unsupported' add-on.

          - **ukd1** · [2023-03-13 18:05 UTC](https://news.ycombinator.com/item?id=35139822)
            Also, I'm in the market for a new AC/heater - so have been looking. ^c35139822

            Your specs are in kbtu, but at least for cooling I'm used to tons; I have 2x4.5ton units, and I think that's \~120kbtu, so I wouldn't be able to get just two of your biggest units?

            - **sgc** · [2023-03-14 00:42 UTC](https://news.ycombinator.com/item?id=35145596)
              That would be 108kbtu, but you are likely oversized. With proper duct configuration including ACCA Manual D calcs and air sealing, you will most likely be more than fine with 96kbtu. Most systems (even in very nice houses) are just sort of thrown in rather than actually calculated, and then they are installed sloppily with a lot of leakage and only roughly resembling the design in at least a few locations. I do these calculations for a living, and would recommend presuming that will be the case until proven otherwise. Obviously get hard numbers before full commitment. ^c35145596

        - **clbrmbr** · [2023-03-13 20:14 UTC](https://news.ycombinator.com/item?id=35141833)
          My company took GP’s suggested strategy and got an incredible community response. Really resonates with the high-end residential market, both DIY and DIFM (pros / CEDIA). ^c35141833

        - **JshWright** · [2023-03-13 17:38 UTC](https://news.ycombinator.com/item?id=35139346)
          I think the desire would be a locally accessible API so that anyone could build an integration to it. ^c35139346

        - **ultrarunner** · [2023-03-13 17:47 UTC](https://news.ycombinator.com/item?id=35139504)
          My desire would be to have the possibility of thermostat control (entirely) via first party, me. Odds are I would never even touch it, but the fact that I *couldn't* would be a dealbreaker for something like this. ^c35139504

        - **RetpolineDrama** · [2023-03-13 18:15 UTC](https://news.ycombinator.com/item?id=35139980)
          For me the goal is 100\% local control. I found out the other day that I couldn't turn my 8sleep mattress on because a guy down the street struck a fiber line. My bed was basically a \$4k brick as soon as the internet went down. ^c35139980

          Look at it this way, it saves you money in server costs and performs much better.

          - **keithah** · [2023-03-13 19:16 UTC](https://news.ycombinator.com/item?id=35140968)
            Hey, that happened to me too this weekend! Do you also live in Ingleside in SF? ^c35140968

          - **voidee** · [2023-03-13 18:51 UTC](https://news.ycombinator.com/item?id=35140570)
            WOW. ^c35140570

        - **pkulak** · [2023-03-13 20:58 UTC](https://news.ycombinator.com/item?id=35142491)
          For me, it's just peace of mind. I need to know that if cloud servers go down, or even my internet goes down, my house still works. My Nest thermostats are currently cloud-only (the only parts of my house left that are), and I had to write a script to never update them exactly on the hour. That's when their API is very likely to 500; I'm guessing because most people have automations trigger on the hour. ^c35142491

          I guess I can sum it up like this: I only want to deal with my own problems in my free time in my own home.

        - **stingraycharles** · [2023-03-13 19:00 UTC](https://news.ycombinator.com/item?id=35140730)
          The point is to not have your company as a single point of failure for the thermostat. So yes, integrate into a wider (open) ecosystem, and that problem is addressed. ^c35140730

        - **AYBABTME** · [2023-03-13 17:44 UTC](https://news.ycombinator.com/item?id=35139460)
          Yes, and particularly in a local/LAN/no internet manner. Local push or local pull. ^c35139460

        - **X-Istence** · [2023-03-13 18:11 UTC](https://news.ycombinator.com/item?id=35139923)
          I would like to be able to add it to HomeKit without it ever phoning home once. Matter + Thread help make that a possibility. ^c35139923

        - **8ytecoder** · [2023-03-13 17:54 UTC](https://news.ycombinator.com/item?id=35139636)
          I consider Matter support to be vital for any product that’s “connected”. You can keep all the specialised features limited to your app but basic controls should be exposed via a standard protocol like Matter so I can use any Matter controller to set the temperatures and such. ^c35139636

        - **doctoboggan** · [2023-03-13 18:13 UTC](https://news.ycombinator.com/item?id=35139955)
          I think going with Matter would give you the best bang for your buck as you would get virtually every major smart home hub system. ^c35139955

          You would still be able to do more with your own app as matter will probably mainly support the lowest common denominator across your category.

        - **daredoes** · [2023-03-13 19:00 UTC](https://news.ycombinator.com/item?id=35140717)
          The desire is to have any control/knowledge you'd want to have as the creator/developer. I want to be my own mechanic, and if I'm not that mechanic I want to be able to have anyone be that mechanic. ^c35140717

          Do you want to know what the active airflow rate is? I want to know what the active airflow rate is. Do you want to know power consumption? I want to know power consumption. Do you have a way to write unique schedules/programs that get executed on the heat pump? I want a way to write unique schedules/programs that get executed on the heat pump.

          Context: Full-Stack Software Engineer (worked at a few start ups including Bird Rides). Active Home Assistant user and community-run integration creator (Linked Lovelace)

          The incredible part about a company like yours is the ability to do hardware at scale. There's no reality in which I'm safely and cost-effectively building my own Electric Heat Pump, or television, or \[cool product here\].

          Companies that make it easier for me to do my own things stand out.

          If you don't want that for the standard customer, fine. Provide some way to open up the device and trigger dev mode, or manually upload firmware, or OTA update firmware.

          Side notes:

          \- a failed kickstarter I joined shipped out their original product with bad firmware and no way to do a physical firmware update without destroying the product, so they tanked instantly despite having a great hardware setup. Despite their failure, I and a few others opened up our products and manually flashed custom firmware onto it to make use of the product we bought

          \- I exclusively buy LG Televisions now due to their usage of Web OS (has a local-first \[HA Integration\]([https://www.home-assistant.io/integrations/webostv/](<https://www.home-assistant.io/integrations/webostv/>))) which used to be hackable with [https://rootmy.tv](<https://rootmy.tv>). With that, my TV runs custom Linux software that controls lights just like \[Phillips Hue Sync\]([https://www.philips-hue.com/en-us/explore-hue/propositions/e...](<https://www.philips-hue.com/en-us/explore-hue/propositions/entertainment/sync-with-home-theater>)) but free/open-source and no additional hardware.  Compare that to Samsung which is like 40\% ads now?

          \- I don't mind using a voice assistant, steal my ideas Tim Apple. I hate the part where the request goes (phone -\> router -\> cloud server -\> router -\> local server -\>  light bulb) instead of (phone -\> router -\> local server -\> light bulb) or worse (phone -\> router -\> local server -\> router -\> cloud server -\> router -\> local server -\> light bulb).

          EDIT: my markdown is showing, I should stick to lurking

          - **liminalsunset** · [2023-03-13 22:47 UTC](https://news.ycombinator.com/item?id=35144214)
            Speaking of heat pumps and granular control, I recently figured out that some Midea heat pumps (usually sold rebranded to various brands) contain two interfaces to get and set detailed information: ^c35144214

            1) Detailed diagnostics i.e. RPMs, feeds, speeds, currents, temps etc can be read from the high voltage signal line between the indoor and outdoor unit - there is an official tool (search "Dr. Smart Midea" on YouTube) that does this. If you look in the right places, there is a PowerPoint with a schematic of the PHY that you need to interface with this using a LV isolated controller

            2) The outdoor unit can be driven manually using the same tool using an i2c port that is on the PCB on the outdoor unit

            I have the new generation of their Dr. Smart tool, which I haven't had the time to thoroughly test or document. If there is interest I will likely try to reverse engineer and document these protocols properly.

            \> "I want to be my own mechanic, and if I'm not that mechanic I want to be able to have anyone be that mechanic."

            \> "Do you want to know what the active airflow rate is? I want to know what the active airflow rate is. Do you want to know power consumption? I want to know power consumption. Do you have a way to write unique schedules/programs that get executed on the heat pump? I want a way to write unique schedules/programs that get executed on the heat pump."

            There's one feature of this diagnostic interface that I really really like.
            It allows you to "drive" the hardware of the unit manually, like Program Auto mode on a camera. You can manually set the frequency of the compressor and fan, and the control board will continue to enforce safeties.

            I haven't tried yet, but something I really want to try to implement myself is "frequency lockout". This is a common feature on commercial variable frequency drives. I noticed that under some operating conditions, the unit vibrations resonate with the building and create unpleasant sounds - I'd like to program it to never dwell on that frequency and skip over it.

            \> The desire is to have any control/knowledge you'd want to have as the creator/developer.

            While I was exploring this, I had this in mind constantly. I definitely had this diag interface in mind when I was selecting a unit.

            - **briHass** · [2023-03-14 01:22 UTC](https://news.ycombinator.com/item?id=35146030)
              Can you provide any more details on the I2C interface on Midea units? ^c35146030

              I found some sparse documentation on Midea's (and rebadged units) Modbus-esque protocol over RS485 (aka XYE connectors), and I control it via an ESP32 on HA. From the indoor unit, the diagnostic data I could reverse engineer is limited to temp sensors (intake, indoor coil, outdoor ambient) and basic running modes. I believe the outdoor unit also has a modbus/485 that has more info, and obviously the signal wire passes some comms between the two, but Midea doesn't make this stuff public.

      - **0xbadcafebee** · [2023-03-13 18:31 UTC](https://news.ycombinator.com/item?id=35140251)
        If I'm gonna invest in a heat pump for the long term, I don't want it committed to any software technology that may be obsolete in 10 years. I want it to use something so dead stupid simple that anything in 50 years can still operate it without a lot of work. ^c35140251

        The simplest example I can think of is MIME ([https://en.wikipedia.org/wiki/MIME](<https://en.wikipedia.org/wiki/MIME>)). It can be embedded in basically any transport type. It can encode anything you want (binary, UTF8, etc). It is very old, stable and well-tested. It is fairly trivial to implement a limited instruction set of.

        Transport security, authentication, authorization, etc, are nice, but not nearly as important to me as a future-proof interface to my heat pump. Give me the option to enable an admin port and just run a single unsecured connection with a basic dumb text protocol, and I can hack together a client in 30 minutes in any programming language. It's not fancy but it will work forever.

        - **dminor** · [2023-03-13 20:04 UTC](https://news.ycombinator.com/item?id=35141695)
          I agree on the point of not wanting to end up with a brick due to obsolete software. Note though that heat pumps typically last 10-20 years. ^c35141695

          - **blincoln** · [2023-03-13 23:42 UTC](https://news.ycombinator.com/item?id=35144951)
            This is extremely disappointing, given their price point. ^c35144951

            I've seen an oil furnace still running after 50 years with just basic maintenance. Did it cost 2-5 times as much in inflation-adjusted dollars as a heat pump does now? No.

            - **oblio** · [2023-03-14 14:14 UTC](https://news.ycombinator.com/item?id=35151853)
              [https://www.evergreenenergy.co.uk/heat-pump-guides/how-long-...](<https://www.evergreenenergy.co.uk/heat-pump-guides/how-long-do-heat-pumps-last/>) ^c35151853

              I don't see why a heat pump wouldn't run for a long time. I imagine many people want to replace old heat pumps because newer ones are more efficient.

              But otherwise this is quite old and widely available tech, it should be possible to replace individual components that break down.

          - **oblio** · [2023-03-13 23:09 UTC](https://news.ycombinator.com/item?id=35144506)
            What happens to them after 20 years? ^c35144506

      - **seiferteric** · [2023-03-13 22:00 UTC](https://news.ycombinator.com/item?id=35143570)
        IMO I would prefer a Bluetooth thermostat that once paired, you don't have to login again. One thing that really annoys me about home "smart" devices is arbitrarily being logged out and having to remember passwords etc. and I don't see a reason I need to be "logged in" to control my thermostat. Also I don't want it to stop working when your servers are down... (had this happen the other day with my garage door opener sigh...) If you want internet connectivity, it should connect to some hub to bridge the Bluetooth to the web account. ^c35143570

      - **stevenpetryk** · [2023-03-13 17:28 UTC](https://news.ycombinator.com/item?id=35139159)
        Or the company could at least leave it easy to hack :) ^c35139159

        - **walterbell** · [2023-03-13 17:33 UTC](https://news.ycombinator.com/item?id=35139256)
          Implement with a swappable compute module? ^c35139256

          - **samstave** · [2023-03-13 19:40 UTC](https://news.ycombinator.com/item?id=35141303)
            We need an entire industry of 'appliance based Rpi's to be able to act as modules in a standardly compute plug-in-form factor (just like blades) with a unit preloaded with a config and just swap out inter connects - ich that we have an appliance hub, the solar/whatever input pushes power and the distributor determines where to push or halt the power - with a selector that tells me the input costs, and output draws, such that it can have a system to auto switch to best performance. ^c35141303

            Honywell missed the mark on the importance of thermostats on the economy.

          - **whstl** · [2023-03-14 00:07 UTC](https://news.ycombinator.com/item?id=35145228)
            My dream is something equivalent to a Dumb TV + Chromecast. ^c35145228

      - **jacquesm** · [2023-03-13 18:26 UTC](https://news.ycombinator.com/item?id=35140182)
        Seconded. ^c35140182

    - **itake** · [2023-03-13 17:30 UTC](https://news.ycombinator.com/item?id=35139199)
      I also would appreciate a local-only user experience. ^c35139199

      I'd also be concerned about dealing with "cannot find server" alerts popping up every time I use it.

    - **nickparker** · [2023-03-13 18:58 UTC](https://news.ycombinator.com/item?id=35140693)
      Please also be careful about selling to incumbents without a strong guarantee (ie contractual penalties) your product will stay in market for many years. ^c35140693

      I know smoke detectors and a couple other crappy home goods have been fixed by scrappy upstarts, sold to the losers for \<100M, and then shuttered to avoid pivoting the existing business. Heartbreaking lost progress every time it happens.

    - **dawnerd** · [2023-03-13 17:11 UTC](https://news.ycombinator.com/item?id=35138840)
      that's good to hear, I'd make sure it's mentioned in the FAQ at the bottom. ^c35138840

    - **mlfreeman** · [2023-03-13 19:03 UTC](https://news.ycombinator.com/item?id=35140774)
      1\. There's a plugin for WeeWX that will happily fling readings from a weather station to my RainMachine sprinkler timer, so perhaps you could still support weather response as long as the user ran their own weather station. ^c35140774

      2\. The thermostat should support at least as much local control as the REST-ish API on the Venstar ColorTouch series.

    - **samstave** · [2023-03-13 19:59 UTC](https://news.ycombinator.com/item?id=35141610)
      Crazy idea: ^c35141610

      Pressure plates in the streets which are pressed when cars drive over them - pushing fluids through your coils, but connected to multiple units on either side.

      Harvest the kinetic energy of cars passing through the streets to apply pressure to pumps that feed fluids through the system, capturing that energy in a dynamo way?

      Put these plates in every high trafficked area. Piping the pumping action from parking garages to freeway exits and shipping ports which roll off weight from water to street and pump a f-ton of fluid based on vehicle traffick and weight.

      Make smaller installations... make an adapter interface to railway. heavy as cars on trains constantly hitting the pump valves. (yes we still need to deal with the bureau assholes in that industry... Im talking engineering)

      - **cmui** · [2023-03-13 20:45 UTC](https://news.ycombinator.com/item?id=35142281)
        I like the out of the box thinking! Unfortunately I think this one doesn't quite pass first principles. Any pumping action from the vehicles would be extra work they have to perform, so you just shuffle the energy expenditure from your local heat pumps, to a fleet of vehicles. ^c35142281

        - **lazyasciiart** · [2023-03-13 22:44 UTC](https://news.ycombinator.com/item?id=35144182)
          Aren’t the cars already performing that work, just letting the energy dissipate into the road surface instead of going somewhere? ^c35144182

          - **sfink** · [2023-03-13 23:30 UTC](https://news.ycombinator.com/item?id=35144781)
            No. The cars would be doing a little extra work. Imagine if you did it with half-filled hoses of water going in a loop. The car tires would be pushing the water through the hose, adding drag. The energy cost would come from the gas or electricity of the car. ^c35144781

            It's like the usual analogy I used to use for content mills or adtech: it's like setting up wind farms along the interstates. The wind from the trucks creates free energy! Awesome, right? Except that those trucks are no longer drafting off each other quite as much...

            (And I say "used to use" because it used to be a small tax, a bit of an extra nuisance here and there, and people largely felt like it didn't really cost anyone anything. Now it's more obviously expensive, like making the entire roadbed out of little rolling wheels that charge generators, so you have to "drive" 80mph in order to progress at 50mph...)

          - **faefox** · [2023-03-13 23:24 UTC](https://news.ycombinator.com/item?id=35144699)
            It takes more energy to drive a car through mud than on pavement. The same principle would apply here. ^c35144699

      - **Arch-TK** · [2023-03-13 20:47 UTC](https://news.ycombinator.com/item?id=35142310)
        For a similar reason why riding a bike through sand is more difficult than on flat tarmac, this will require additional energy and you will pay for it in locally burned petrol. Moreover, it will be less efficient than if you just burned that fuel in a power station. ^c35142310

      - **brooksbp** · [2023-03-14 00:27 UTC](https://news.ycombinator.com/item?id=35145443)
        I can already see the "Avoid bumpy roads" option right next to the "Avoid tolls", "Avoid ferries", ... ^c35145443

    - **nullbyte808** · [2023-03-13 21:45 UTC](https://news.ycombinator.com/item?id=35143295)
      I agree with this. I would rather have it automated without cloud functionality. I think people on HN just like hacking lol. But when it comes to appliances and cars I would rather not mess with their code and break them. ^c35143295

    - **Psype** · [2023-03-14 01:32 UTC](https://news.ycombinator.com/item?id=35146108)
      You can either go using open source protocols at first or at least guarantee open-sourcing most of it in case of leadership change. For reuse. ^c35146108

      I'd go starting with it and let a community build by itself around it, tho.

    - **soheil** · [2023-03-13 17:29 UTC](https://news.ycombinator.com/item?id=35139173)
      I'd be careful catering to everyone asking for everything but the kitchen sink. Creating a non-cloud capable system is dumb. ^c35139173

      If you have customers like commenter above maybe put in a clause in the contract that says they will receive a partial refund if/when there is an acquisition event during the warranty period and bump up their price by 20\%.

      - **robertlagrant** · [2023-03-13 17:35 UTC](https://news.ycombinator.com/item?id=35139302)
        \> Creating a non-cloud capable system is dumb ^c35139302

        No, you haven't understood. It will be cloud-capable. They're asking that it's not cloud-only.

        - **soheil** · [2023-03-13 21:23 UTC](https://news.ycombinator.com/item?id=35142948)
          No, you don't understand. Making it non-cloud-capable incurs a cost. ^c35142948

          And there is no they, the commenter is a single individual.

          - **robertlagrant** · [2023-03-13 21:45 UTC](https://news.ycombinator.com/item?id=35143302)
            "As someone about to be in the market for something like this, propriety lockout is a complete deal breaker for me." - StrangeATractor ^c35143302

            "Would your company be willing to provide an open-source local-first websocket-based integration with [https://www.home-assistant.io/](<https://www.home-assistant.io/>) or use the new Matter + Thread standard to provide it for everyone?" - daredoes

            "Most of your competition has no sensitivity, and almost no openness, about these aspects. I think this could become a really important part of your go-to market, but also a differentiator vs other products." - simonebrunozzi

            "I would like to be able to add it to HomeKit without it ever phoning home once. Matter + Thread help make that a possibility." - X-Istence

            They.

            - **soheil** · [2023-03-13 22:07 UTC](https://news.ycombinator.com/item?id=35143667)
              Yes this is HN what do you expect, of course everyone and their grandma here is gonna want a fully unlocked, open source and free as in freedom fries product. ^c35143667

              - **robertlagrant** · [2023-03-13 22:11 UTC](https://news.ycombinator.com/item?id=35143714)
                I expect to be able to refer to those people as "they". ^c35143714

      - **Arch-TK** · [2023-03-13 20:56 UTC](https://news.ycombinator.com/item?id=35142457)
        I mean, aside from the fact that you misunderstood the whole point, nobody ever paid 20\% extra for a heating system which didn't have cloud connectivity. In fact, the whole idea that there's something wrong with a heating system which doesn't require an internet connection is so incredibly bizarre that I can only wonder if you're someone who came out of a time machine. ^c35142457

        Lastly, a partial refund does fuck all to compensate for the fact that you have a multi-tonne brick in your house that has perfectly functioning hardware but broken software (because the server it used to talk to is gone). It also doesn't compensate for the wasted resources.

      - **UncleEntity** · [2023-03-13 17:43 UTC](https://news.ycombinator.com/item?id=35139425)
        \> Creating a non-cloud capable system is dumb. ^c35139425

        For a system that absolutely doesn’t need a “cloud” to operate?

        But this is my second concern.

        First is availability of replacement parts after the get bought out and they shut off the servers.

      - **unknown** · [2023-03-13 18:55 UTC](https://news.ycombinator.com/item?id=35140644)
        [deleted] ^c35140644

  - **dawnerd** · [2023-03-13 17:00 UTC](https://news.ycombinator.com/item?id=35138627)
    My thoughts too. Local heating/cooling should not be tied to the cloud period. If it doesn't use the normal wiring people already have it's a hard pass from me. ^c35138627

    - **toss1** · [2023-03-13 17:23 UTC](https://news.ycombinator.com/item?id=35139061)
      Exactly.  I will not even buy a \$100 remote-internet-controlled thermostat that relies on a cloud service \[0\], and I've looked for both my home and my shop. ^c35139061

      I would not even consider buying the hardware that keeps my pipes from freezing if it depends on an internet connection.

      I'm happy if there are non-critical *OPTIONS* available that use the internet (e.g., as another poster mentioned, available optimizations based on real-time elec rates, etc.), but if there is *any* key function that'll fail without an internet connection, that's immediate disqualification, hard nope, not looking anymore.  Period, full stop, even if it is "free" as in beer.

      OTOH, if OP can deliver a true stand-alone system and guarantees that it will *never* require a connection for any core function (as above, optional ok), then he'll have a large market.

      \[0\] any remote-via-internet control function should be able to directly access my IP, static or transient.  Not only are non-static home IPs actually quite durable in my experience, there are a variety of easy solutions to keep track of the home IP.   Yes, some of those are cloud services, but they are not tied to any hardware.

      Edit:  That said, I'm ok with requiring wiring beyond the normal thermostat-HVAC wiring.

    - **paxys** · [2023-03-13 21:55 UTC](https://news.ycombinator.com/item?id=35143474)
      Disagree. There are a lot of advantages in being able to coordinate heating/cooling and general home electricity use based on stuff like weather forecasts, your electric company's rate tiers (including working around peak hours), when you are home or about to come home etc. Of course there should be a fallback mode where the system can work 100\% offline, but being connected is definitely worth it. ^c35143474

    - **vladgur** · [2023-03-13 18:35 UTC](https://news.ycombinator.com/item?id=35140320)
      I agree. 
      Use standardized wiring and let me control it from a \$100 smart thermostat that i can replace if it becomes obsolete. ^c35140320

      If i want HomeAssistant integration, ill buy an HA-compatible thermostat.

      I dont want an expensive HVAC system to be in a walled garden of its own.

      - **coryrc** · [2023-03-13 20:16 UTC](https://news.ycombinator.com/item?id=35141868)
        You lose about 30\% efficiency using "standardized wiring" with an inverter heat pump instead of a communicating thermostat, because running a heat pump at 33\% power continuously instead of 100\% power 20 minutes of every hour results in a COP about 30\% higher. ^c35141868

        - **raisedbyninjas** · [2023-03-13 21:08 UTC](https://news.ycombinator.com/item?id=35142680)
          Why do inverter heat pump need proprietary wiring? Everything I've seen indicates inverter and dual stage heat pumps can use standard wiring. ^c35142680

          - **coryrc** · [2023-03-13 23:51 UTC](https://news.ycombinator.com/item?id=35145043)
            They don't *need* it, they just don't get all their rated efficiency, which is much higher than single-speed systems. Single-speed systems commonly have cooling efficiencies around 10-14 SEER, the Gree Sapphire is 38 SEER. If you ran it at only full power, it'd probably only be 30 SEER. ^c35145043

    - **thehappypm** · [2023-03-13 17:47 UTC](https://news.ycombinator.com/item?id=35139506)
      Counterpoint — I have an app for my Mitsubishi heat pump and use it all the time. It’s way more convenient and lets me hyper optimize my house. I actually don’t even use the physical ones at all anymore ^c35139506

      - **itake** · [2023-03-13 19:21 UTC](https://news.ycombinator.com/item?id=35141045)
        What is your plan if Mitsubishi cuts off access in 20 years or updates in a way that you're not comfortable with (like add advertisements to the panels)? ^c35141045

        - **surfmike** · [2023-03-13 21:15 UTC](https://news.ycombinator.com/item?id=35142793)
          You can replace the thermostats with dumb versions. ^c35142793

      - **epanchin** · [2023-03-13 17:49 UTC](https://news.ycombinator.com/item?id=35139545)
        Are you tied to the app? ^c35139545

        - **aintgonnatakeit** · [2023-03-13 18:17 UTC](https://news.ycombinator.com/item?id=35140019)
          Yes s/he is. Mitsubishi force you to use their Kumo Cloud controls, which are 1) expensive (a few kk) and 2) require cloud. Supposedly Mitsubishi is replacing Kumo with something else, but that just makes the problem worse. ^c35140019

          - **burntsushi** · [2023-03-13 21:59 UTC](https://news.ycombinator.com/item?id=35143553)
            Wat. First of all, I have Kumo Cloud and it did not cost thousands of dollars. It was a few hundred for the adapter, and then I paid an HVAC tech to install it. That's it. ^c35143553

            Second of all, you aren't forced to use Kumo Cloud. Even though I have it, I still have a remote that operates the Split. No network or cloud required.

          - **spaceguillotine** · [2023-03-13 20:04 UTC](https://news.ycombinator.com/item?id=35141696)
            you can get a converter to get Mitsu to work with any 24v AC controls
            PAC-US444CN-1, ive installed a few of them so the customer could use their existing Nest and Ecobee thermostats. ^c35141696

            I'm a former diamond certified Mitsubishi installer

            - **drusenko** · [2023-03-13 20:48 UTC](https://news.ycombinator.com/item?id=35142320)
              I've used the PAC-US444CN-1 (at our house) and fully native Mitsubishi thermostat/controls (at our in-laws). The converter is better than a simple 2-stage set up but is still not as good, in my experience, as the fully native one. ^c35142320

              It has to translate a 2-stage signal into a fully modulating output, and it still seems to do a lot more on & off with high fan speeds than I would like or would be most efficient (as an aside, yes I have verified that the dip switches are in the correct position on the converters).

              On the other hand, the unit at my in-laws tends to blow gently but consistently which is both more comfortable and more efficient.

            - **JeremyPOsborne** · [2023-03-16 09:40 UTC](https://news.ycombinator.com/item?id=35179902)
              spaceguillotine I'd love to hear about your experience as a former installer! Any chance for a DM? ^c35179902

        - **SamBam** · [2023-03-13 18:16 UTC](https://news.ycombinator.com/item?id=35140007)
          Mitsubishi heat pumps has a local thermostat that operates by remote, no cloud access needed, so if the app's servers go down it will still function. ^c35140007

        - **thehappypm** · [2023-03-13 18:11 UTC](https://news.ycombinator.com/item?id=35139922)
          No, my phone is wireless ^c35139922

          - **vosper** · [2023-03-13 18:16 UTC](https://news.ycombinator.com/item?id=35140009)
            Pretty sure they were asking if you could still access all the functionality currently provided by the app if it were to go away for some reason (who can see the future? It's not impossible Mitsubishi goes out of business or the app gets cancelled/pulled after some number of years) ^c35140009

          - **shagie** · [2023-03-13 18:17 UTC](https://news.ycombinator.com/item?id=35140026)
            If you lost your phone, would you still be able to manage the heat pump through other interfaces? ^c35140026

            If the app wasn't updated for \${latest phone OS}, would you be be unable to upgrade the phone OS?

    - **s\_tec** · [2023-03-13 17:10 UTC](https://news.ycombinator.com/item?id=35138819)
      Normal wiring is terrible, though, since it only supports turning the equipment on & off. If you have a variable-speed fan and variable-speed pumps, it would be nice for the thermostat to throttle those based on the load, but it can't. ^c35138819

      If this company has a solution for variable-speed equipment, the best thing they can do is publish an open standard. Suppose the thermostat talks to the equipment over CAN bus, for instance, using a well-documented protocol. If they go out of business, anybody can hack together a compatible aftermarket thermostat.

      A lot of solar equipment is already going this way, with batteries talking to inverters over open CAN bus protocols. As one of the biggest energy loads, the HVAC equipment should get in the game too.

      - **SketchySeaBeast** · [2023-03-13 17:21 UTC](https://news.ycombinator.com/item?id=35139007)
        What do you mean?  There are variable speed furnaces that can be controlled via a normal thermostat and a 4-wire thermostat setup. Like you said, though, there's no open standard so that can be an issue, but it's standard wiring. ^c35139007

        [https://www.pickhvac.com/thermostat/](<https://www.pickhvac.com/thermostat/>) (halfway down - "Communicating HVAC System")

        [https://www.pickhvac.com/central-air-conditioner/extras/comm...](<https://www.pickhvac.com/central-air-conditioner/extras/communicating-vs-non-communicating/>) (deeper dive into Communicating vs Non-Communicating HVAC systems)

        - **s\_tec** · [2023-03-13 17:43 UTC](https://news.ycombinator.com/item?id=35139428)
          Well, that just makes it worse! OP strongly implies that there is no good variable-speed solution, but if the industry already has an assortment of products, what exactly are they even selling?! ^c35139428

          - **notJim** · [2023-03-13 18:48 UTC](https://news.ycombinator.com/item?id=35140507)
            I think you're misreading the OP slightly. There's no cross-compatible system for variable equipment, which is why the OP says you can't use variable speed equipment with Nest. Nest is basically a really fancy switch only. To use variable speed equipment, you have to use your manufacturer's proprietary system. I'm not positive this is right, but I'm pretty sure it's backed up by [https://www.pickhvac.com/central-air-conditioner/extras/comm...](<https://www.pickhvac.com/central-air-conditioner/extras/communicating-vs-non-communicating/>) ^c35140507

            So basically, the premise of this product is that the proprietary system they design will be nicer than the proprietary systems HVAC manufacturer's design. That's probably true, but as an owner of a Carrier proprietary system, it's totally fine.

            - **drusenko** · [2023-03-13 20:51 UTC](https://news.ycombinator.com/item?id=35142380)
              The issue isn't that an open standard for fully variable speed isn't possible, the issue is that nearly all of the manufacturers to date have considered this proprietary (as they want to own the entire ecosystem from controls \> equipment) and a purposefully boxing Nest, Ecobee, etc, out of being able to control it in order to sell more thermostats and trying to capture more value. ^c35142380

              Only problem, their thermostats and apps really suck.

          - **necovek** · [2023-03-14 06:41 UTC](https://news.ycombinator.com/item?id=35148116)
            Heat pumps are basically ACs with inverters allowing them to work at partial load (i.e. 10\% pr 20\% or 70\%). Otherwise, they are as efficient as ACs at full load. ^c35148116

            There are few off the shelf AC thermostats that work with most heatpumps: they are usually the on/off variety.

            Remotes coming with heatpumps would do the right thing, though, and there are IR blasters that can replicate those signals and integrate into your home automation system.

          - **aintgonnatakeit** · [2023-03-13 18:19 UTC](https://news.ycombinator.com/item?id=35140064)
            I think you have to go thru a licensed HVAC installer to get an inverter system. These guys are DTC. ^c35140064

      - **SamBam** · [2023-03-13 18:18 UTC](https://news.ycombinator.com/item?id=35140044)
        Mitsubishi heat pumps, and most others I assume, have local thermostats that communicate by remote (I assume radio waves), but do not require the cloud. This is a fine solution, as stable as wires but not tied to the cloud. ^c35140044

        - **whafro** · [2023-03-13 18:50 UTC](https://news.ycombinator.com/item?id=35140525)
          Unfortunately, they (or at least mine) communicate by IR, which is not as stable as wires – two of my rooms have very intermittent response to my IR pucks. ^c35140525

      - **ROTMetro** · [2023-03-13 18:02 UTC](https://news.ycombinator.com/item?id=35139768)
        Huh? My Lennox basic middle America furnace already does this if I am understanding your comment correctly. ^c35139768

    - **RetpolineDrama** · [2023-03-13 18:16 UTC](https://news.ycombinator.com/item?id=35140012)
      \>If it doesn't use the normal wiring people already have it's a hard pass from me. ^c35140012

      Why? a real smart thermostat can just use the existing wiring for power and then use IP over Wifi or Matter/Thread to communicate. Way better than the crappy wiring in most people's houses for thermostat control.

      - **dawnerd** · [2023-03-13 19:17 UTC](https://news.ycombinator.com/item?id=35140972)
        Because HVAC in theory should outlive most other standards that have come and gone. Its totally fine to built on top of it, but using basic hard wiring to turn on/off is essential - even if just as a fallback. in 20 years the hvac should still be working, but will the wifi spec it shipped with? What about matter/thread? ^c35140972

        - **Melatonic** · [2023-03-13 23:40 UTC](https://news.ycombinator.com/item?id=35144922)
          Theres certainly a middleground between "must use existing old ass 2 wire setups" and "requires fancy always on cloud subscription" ^c35144922

          Surely we could come up with a device that might require an electrician to run a few extra wires (or maybe even larger wires or something) and still run perfectly fine offline, for as long as the hardware functions, with some type of integrated manual controller. And of course this device could also have an internet option and an app and wifi for all of the fancy stuff.

    - **soheil** · [2023-03-13 17:31 UTC](https://news.ycombinator.com/item?id=35139209)
      It's hard pass for you because you know what a cloud is. Many don't and you don't know what many know. ^c35139209

    - **startupsfail** · [2023-03-13 17:08 UTC](https://news.ycombinator.com/item?id=35138778)
      Maybe Europe market is ready for this. ^c35138778

      Considering how unstable the residential electrical and internet grid is in the US (instead of being dug in, into the ground all the cables are hanging between the trees and there are constant failures), relying on that AND on the cloud for an essential service is a no-go.

      - **pridkett** · [2023-03-13 17:54 UTC](https://news.ycombinator.com/item?id=35139632)
        I live in a rural part of New England with an electricity company that everyone dislikes because it's super expensive and sometimes things go bad. Since 2010 we've had the following major outages: ^c35139632

        \* October 2011 Snow Storm - Lost power for 4 days, didn't end up being that cold

        \* October 2019 Thunderstorms - Lost power for 3 days, thankfully generator kept the house going

        \* August 2020 Tropical Storm Isaias - Caused widespread grid damage, but only lost power for 18 hours. Internet was out for 36 hours.

        \* August 2021 Hurricane Henri - Widespread grid damage, lost power for about 6 hours. By this point I had powerwalls. I didn't even turn down the air conditioner.

        That's it - every other outage has been a few hours. And that's living in a rural area that is heavily wooded with most of the power lines above ground and often long runs close to trees. If I lived in a suburb or city those times would be even less.

        The grid in the United States, despite some widespread and documented regional failures (2021 Texas, 2003 NE Blackout), is remarkably resilient.

        - **drusenko** · [2023-03-13 20:57 UTC](https://news.ycombinator.com/item?id=35142470)
          I would say it depends on where you live. The grid in CA has (in some parts) not been reliable for 5+ years. To Chris' point below though, it's not really relevant because gas furnaces need electricity to operate, too. ^c35142470

      - **cmui** · [2023-03-13 18:18 UTC](https://news.ycombinator.com/item?id=35140042)
        A common misconception is that you can use your forced air furnace when the power is out - you can't because the blower relies on electricity to move air around. Your point on the cloud service is a good one, which is why cloud services are value-add but unnecessary for core system functionality, ie your system works if there's no internet. ^c35140042

        - **startupsfail** · [2023-03-13 21:58 UTC](https://news.ycombinator.com/item?id=35143531)
          In California power outages are very frequent (PG&E is now cutting off the residential power upfront, to avoid fires and associated liability). ^c35143531

          I’ve experienced 4-5 outages last year, a couple were local, a couple were widespread.  One lasted 2 days.

          Fortunately I do have a small  3.2kWh battery backup power, so I can keep the refrigerator from defrosting. I do think that this is sufficient to power the air furnace as well, but I haven’t tried.

          The residential internet outages also are pretty frequent, but we don’t notice these as much as power outages.

      - **eldaisfish** · [2023-03-13 17:45 UTC](https://news.ycombinator.com/item?id=35139471)
        the US power grid is not in any way unreliable. US residents enjoy some of the highest grid availability figures for anywhere in the world. Sure, sometimes things go horribly wrong but their system is not unreliable by design as this comment insinuates. ^c35139471

  - **aaomidi** · [2023-03-13 17:08 UTC](https://news.ycombinator.com/item?id=35138781)
    I will not buy this without a fully unlocked everything. ^c35138781

    This company is going to wait a few years and then charge you a shit ton for subscription to keep using your device.

    No thanks, and honestly whoever goes with this is going to regret it if they don't make changes to their software.

    Pick one:

    \- Sell the device

    \- Sell the software

    If you do both, you're going to alienate your customers and get regulatory wrath on you. Don't emulate Apple. They're going to get their ass handed to them in the near future.

    Take it even a step further and make the code AGPL. That way you know you're protected if a company decides to steal from you.

    - **cmui** · [2023-03-13 17:15 UTC](https://news.ycombinator.com/item?id=35138892)
      I understand the concern around lock in. There is a technical hurdle to optimized thermostat \<--\> variable speed heat pump interop. You have to turn the temperature error between setpoint and actual temperature into a compressor speed command and also factor in behavior such as defrost, compressor cycling limits, etc. So you have to have a communicating thermostat to fully utilize the efficiency of these variable speed heat pump systems, not just a collection of analog on/off wires. ^c35138892

      - **oceanplexian** · [2023-03-13 18:16 UTC](https://news.ycombinator.com/item?id=35140006)
        This is not strictly true. ^c35140006

        Mr. Cool has a 2-Ton heat pump (Designed to work with existing ducting) that can operate off of a normal non-communicating thermostat. It still hits 19 SEER and does a lot of that optimization on the controller side. And when it comes to mini splits there are lots of them that will work with a normal thermostat.

        I know this, well, because I’ve spent many countless hours trying to find something that will work with Z-Wave and not a proprietary communicating system. Granted it might be less efficient but efficiency is way less important than having the ability to do that. The only exception I would consider is if the communicating thermostat was fully open and had a decent API that worked without Internet access.

      - **amluto** · [2023-03-13 19:37 UTC](https://news.ycombinator.com/item?id=35141253)
        This doesn't seem at all worthy of anything proprietary, though -- a simple RS-485 or 10BASE-T1L protocol and a page of docs would do the trick. ^c35141253

        And if you build this, you can also sell the same hardware plus a BacNET or MODBUS gateway for a bunch of money to the commercial building management types :)

        Or you could support existing commercial 0-10V thermostats.

        - **phasetransition** · [2023-03-13 20:46 UTC](https://news.ycombinator.com/item?id=35142291)
          Upvoted, ^c35142291

          BACnet already exists as an ISO standard:
          [https://www.iso.org/standard/37298.html](<https://www.iso.org/standard/37298.html>)
          [https://bacnetinternational.org/](<https://bacnetinternational.org/>)

          The example application in the Ethernet Alliance one-pager on single pair Ethernet is HVAC:
          [https://ethernetalliance.org/wp-content/uploads/2020/10/EA\_T...](<https://ethernetalliance.org/wp-content/uploads/2020/10/EA_TechBrief-10SPE-DT_final.pdf>)

          - **amluto** · [2023-03-13 21:52 UTC](https://news.ycombinator.com/item?id=35143425)
            FWIW, if this were my startup, I would probably use 10BASE-T1L.  The programming model is simple, and cloud or other “smart” integration is natural if the system already uses IP.  For that matter, one ought to be able to support wired 10BASE-T1L and wireless Matter/Thread thermostats without much duplicate effort. ^c35143425

            This could be prototyped on a BeaglePlay :)

            - **phasetransition** · [2023-03-14 02:20 UTC](https://news.ycombinator.com/item?id=35146511)
              FWIW, ^c35146511

              BACnet allows multiple PHY implementations, including 802.3

              I suspect that 802.3.cg is also kosher, but haven't looked in detail. It's been 5 years since I looked seriously at whether BACnet was the correct solution for a product family.

              Single pair Ethernet is indeed cool tech.

      - **toss1** · [2023-03-13 17:34 UTC](https://news.ycombinator.com/item?id=35139283)
        Yes, that MAY be required for full optimization ^c35139283

        Wonderful option to have: "Subscribe, and we'll improve your efficiency by 10\%++"

        OPTION

        Another option would be "we'll send you a download with the latest weightings for our optimizing AI firmware for \$14.95, or every month for a subscription of \$49/year"  whatever.

        I, and most other sharp people will happily ignore you and buy a system that is 50\% less efficient and twice the cost to avoid your lock-in.

        I'll also happily buy and subscribe to your *reasonably-priced* optimization service as long as it is *OPTIONAL*.

        Just look at the nearly violent reaction that BMW got when they suggested that their heated seats would be a subscription option.

        If you want your company to die before it even gets started, keep making excuses for why you need to lock us in.

        If you want a growth giant, architect it from scratch so someone can happily use it where Starlink doesn't even service, and offer extra-efficiency OPTIONS that OPTIONALLY use internet service.

        And yes, open-sourcing the code would be a huge step in giving people confidence that you are serious, and that their investment has a future that is not a brick.

        - **oceanplexian** · [2023-03-13 18:25 UTC](https://news.ycombinator.com/item?id=35140155)
          Yeah I wish these companies would “get it” but they never do. ^c35140155

          Provide an open API with the option to use a cloud service. Some cloud services are great, and have way better UIs than the self hosted stuff which I would gladly pay for. But take away the option to go self hosted and I lose all interest. If a device can’t be controlled locally you don’t really “own” it, you’re just renting it from someone else.

          - **fourseventy** · [2023-03-13 19:02 UTC](https://news.ycombinator.com/item?id=35140748)
            98\% of consumers who would buy a heat pump have no idea what an API is. ^c35140748

            - **toss1** · [2023-03-14 00:09 UTC](https://news.ycombinator.com/item?id=35145248)
              That's quite generous to estimate that 2\% of the population knows what is an API ! ^c35145248

              My first guess would be more like 99.98\% don't know about APIs

              But yes, that 2\% or whatever is an important set of leaders

      - **sokoloff** · [2023-03-13 17:18 UTC](https://news.ycombinator.com/item?id=35138952)
        That's totally fair and reasonable. I still will demand that it be able to function in a bang-bang mode using dry contacts, especially from a new entrant to the market, because there's a fair risk that the unit will be in my house longer than your company is in business. ^c35138952

        - **cmui** · [2023-03-13 17:32 UTC](https://news.ycombinator.com/item?id=35139230)
          This behavior is how current variable speed heat pumps operate with Ecobee and Nest. You leave efficiency on the table, but I get it provides some future proofing assurance for homeowners. Definitely something we can integrate into the board. ^c35139230

          - **joelfried** · [2023-03-13 18:47 UTC](https://news.ycombinator.com/item?id=35140487)
            \> I get it provides some future proofing assurance ^c35140487

            I don't think you're getting it, and a lot of us around here want you to.  If I were actively researching heat pumps (a thing most homeowners do before dropping 4-5 figures on ANY hardware), if you are locking me into your ecosystem -- or even have the appearance of locking me into your ecosystem -- your product is not getting onto any short list from me or likely anyone else around here.

            All of us -- every tech person who has ever gotten into home automation in a real way -- has thrown out some hardware rendered useless by a company.  We've already seen this play out.  You're an unknown and so are the riskiest kind of company to buy into.

            You need to get this -- deeply -- if you want to sell to this market.  The pull quote above makes me want to run for the hills.

            - **mbreese** · [2023-03-13 23:56 UTC](https://news.ycombinator.com/item?id=35145092)
              This all especially true given the expected time frame a heat pump is supposed to have. No one wants to spend \$14,000 for a paper weight. Whether that’s because the software disappears, spare parts can’t be found, or it’s impossible to service. Any of the above are real risks that need to be considered seriously and addressed. HVAC can also become an issue when trying to sell a house, so it’s not like trying to sell to traditional early adopters. The majority of this market is going to be very conservative. ^c35145092

              I’d honestly just try to market to heat pump believers first who actively are looking for what they are selling. First, it’s an easier sales pitch. Second, they will be more forgiving of growing pains. Go through the 1-3 years trying to get the manufacturing, maintenance, and installation locked in before trying to sell in bulk to a larger market.

              As it is, it’s just too risky for many to buy. (And for my house, it would be impossible to install).

            - **alex\_dev** · [2023-03-13 22:13 UTC](https://news.ycombinator.com/item?id=35143756)
              Agreed. As someone in the market for a good heat pump, I'm already turned off by this offering. I don't want more features (air quality module) that are more points of failure and complexity. I just want an efficient heat pump that'll work reliably for a long time, integrate well with HA, and won't cost a kidney to install. ^c35143756

    - **risyachka** · [2023-03-13 17:56 UTC](https://news.ycombinator.com/item?id=35139666)
      That's just not true. ^c35139666

      1\. 99.99999\% will never care about code, open sourcing it etc. All consumers need is to have a guarantee it will work in case company is out of business or there is no internet. It doesn't matter how that guarantee will look like.

      2\. Sell device OR software is the exact reason most tech is so bad. Doing one of two is 10x easier than doing both, and results are 10x worse. If you do both you actually have a chance to do something nice.

  - **londons\_explore** · [2023-03-13 17:13 UTC](https://news.ycombinator.com/item?id=35138865)
    I'd want to see a guarantee of "We will either keep running the servers forever, maintaining all current features, or we will opensource all the server side code, so you or someone else can keep running it". ^c35138865

    I'd want the code handed over to a third party to guarantee this (so the company can't walk back on their promise).

    - **mtrpcic** · [2023-03-13 17:22 UTC](https://news.ycombinator.com/item?id=35139035)
      If the server code is too complex, at least give me an OpenAPI spec (or equivalent) that the server must adhere to, so I can spin something simple up on a Raspberry PI to solve the problem myself. ^c35139035

    - **mrits** · [2023-03-13 17:21 UTC](https://news.ycombinator.com/item?id=35139014)
      Statically there is a great chance the people that would guarantee will be replaced upon failure or success in an early state startup. ^c35139014

    - **pagutierrezn** · [2023-03-13 18:08 UTC](https://news.ycombinator.com/item?id=35139877)
      This went by the name: Source Code Scrow [https://en.m.wikipedia.org/wiki/Source\_code\_escrow](<https://en.m.wikipedia.org/wiki/Source_code_escrow>) ^c35139877

  - **masterj** · [2023-03-13 18:01 UTC](https://news.ycombinator.com/item?id=35139754)
    The software is certainly a concern, but I would also heavily emphasize the ability to get spare parts and service quickly. If your heat goes out in the middle of winter you don't want to wait weeks for spare parts, or be unable to get them at all if the company goes out of business. ^c35139754

    - **cmui** · [2023-03-13 18:21 UTC](https://news.ycombinator.com/item?id=35140097)
      Yes, making spare parts and service work is super important. We'll likely set up regional distribution points for spare parts so anything critical can be easily sent next day. ^c35140097

      - **potatolicious** · [2023-03-13 20:25 UTC](https://news.ycombinator.com/item?id=35141992)
        What about labor? I'm pretty handy but there are definitely parts of my HVAC system where I'd be unable/unwilling to DIY it. I currently have a local HVAC contractor on-retainer for same-day emergency appointments - and honestly I don't think I'd be willing to consider anything less since my current heat pump is my exclusive source of heating in this house. ^c35141992

        I'm in a temperate climate so there's little actual danger, but the idea of freezing/roasting my butt off for multiple days to wait for parts/labor is deeply unattractive.

        - **cmui** · [2023-03-13 20:49 UTC](https://news.ycombinator.com/item?id=35142332)
          Yeah, good question. The system is not meant to be DIY. The same contractor that does install also offers service. Logistics for replacement parts is important we will have quick, easy access for contractors. ^c35142332

          - **bumby** · [2023-03-13 22:13 UTC](https://news.ycombinator.com/item?id=35143745)
            Have you worked on creating a network of qualified contractors? In my region, there are lots of contractors who are little more than unreliable DIYers, especially in the mechanical space. ^c35143745

            My hesitancy is in the ongoing service. I’ve looked into geo-coupled heat pumps but the lack of qualified contractors locally deterred me.

      - **hd95489** · [2023-03-13 21:56 UTC](https://news.ycombinator.com/item?id=35143493)
        How would you ensure that spares are available in the event a model is discontinued or the company shuts down? It’s likely there will be few parts or trained techs in that case. ^c35143493

  - **jtagen** · [2023-03-13 20:42 UTC](https://news.ycombinator.com/item?id=35142244)
    Wait, is this not going to have the usual "pair of wires you short to turn it on" feature of every furnace made so far? That's the ultimate control for when all the cloud features disappear and would be a deal-breaker for me. ^c35142244

  - **ajross** · [2023-03-13 23:57 UTC](https://news.ycombinator.com/item?id=35145106)
    FWIW: the "cloud based" part is the flexible bit, it's the fixed equipment that you're stuck with for two decades.  I see the problem as exactly the opposite: I could in principle switch from a Carrier to a Lennox to a Nest to an EcoBee in probably 10 minutes, *but I can't*, because all the equipment manufacturers are shipping their own garbage with closed protocols. ^c35145106

    So I had to fight with a contractor to get them to install our fancy new heat pump in "traditional dumb thermostat" mode, and then handed them the Nest box (which doesn't speak Carrier-ese) and put it in the contract that it had to work.  It took them *several hours extra* to do things the "portable" way.  They were absolutely not prepared even though the manufacturer claims this works just fine.

    So... I think there's absolutely a spot in the market for an Electric Air that can make this work cleanly.  The existing HVAC players are really, really bad at this.

  - **pshirshov** · [2023-03-13 18:55 UTC](https://news.ycombinator.com/item?id=35140648)
    Just buy an LG heat pump. They have cloud capabilities, though you have to install a separate module for that. ^c35140648

  - **soheil** · [2023-03-13 17:24 UTC](https://news.ycombinator.com/item?id=35139073)
    It'd be super helpful to mention the total cost will be close to \$14k on the \$100 pre-order page or at least somewhere near the top of the homepage. Also probably one of the implicit reasons this comment got upvoted. ^c35139073

    - **cmui** · [2023-03-13 18:38 UTC](https://news.ycombinator.com/item?id=35140360)
      Yeah, not a bad idea to place pricing (or a link to it) on the preorder page, in addition to main page. ^c35140360

    - **unknown** · [2023-03-14 03:19 UTC](https://news.ycombinator.com/item?id=35146973)
      [deleted] ^c35146973

  - **1970-01-01** · [2023-03-13 20:36 UTC](https://news.ycombinator.com/item?id=35142166)
    I have the same question, but on the hardware side. Since HVAC is critical infrastructure for a home, where will replacement parts be in a decade? ^c35142166

- **phaedrus** · [2023-03-14 16:51 UTC](https://news.ycombinator.com/item?id=35154459)
  As a serious DIYer with engineering knowledge and a bit of HVAC understanding, I find the sleek/modern design in the pictures of this product to be the opposite of reassuring.  (Maybe I'm not the target customer.)  It's for the same reason that after initially being interested integrated solar generators, in the end I went with a solar system that, while sold as a kit, consisted of independent components.  With a solar generator if the electronics go bad the whole thing (including expensive batteries) is potentially a write-off and not easily fixable.  I fear the same thing with this. ^c35154459

  I'm also looking askance at the picture or rendering (next to "Installation Process") showing the PVC drain pipe going \_up\_ before it goes horizontally.  How does that drain?  I realize a graphic designer was probably just trying to make it aesthetic without understanding how it really works, but you yourself do understand as you detail in your post.

  I resonate with the idea of your mission and your description of current market deficiencies.  I just wish the product were more like the solar kit I bought as separate components or the PC water cooling loop I pieced together from a web store that specializes in that.  Maybe that's an unrealistic hope.  But I don't have to like the over-integrated alternative.

  (I realize heat pumps and air conditioners have a requirement that the components have to be appropriately sized to each other to work as a system.  But that could be overcome with software that advises the consumer what parts work together.  We currently spend equivalent effort on using software to lock the consumer out instead of helping them make informed choices.)

- **heatpumpfan** · [2023-03-13 17:04 UTC](https://news.ycombinator.com/item?id=35138709)
  I recently purchased and installed a 3 ton MrCool Universal (Gree Flexx, I believe) with lineset for \~\$4K shipped: [https://hvacdirect.com/mrcool-universal-36-000-btu-heat-pump...](<https://hvacdirect.com/mrcool-universal-36-000-btu-heat-pump-mdu18036.html>) Worked just fine during the Christmas arctic blast. We will see about longevity but at 1/3 of the price of your proposed units, I'm not worried about slapping a new one at any time. I am essentially on my own for service as no contractors will work on it but it seems your units would present the same problem. ^c35138709

  - **cmui** · [2023-03-13 17:41 UTC](https://news.ycombinator.com/item?id=35139413)
    My hats off to you for doing a DIY install. This is not a bad route to go if you enjoy/feel comfortable doing the work and don't care about air quality, smart thermostat integration, etc. Re contractors, we will have local contractor partners do the install and handle servicing, so you won't be left with an unserviceable system. ^c35139413

    - **heatpumpfan** · [2023-03-13 17:51 UTC](https://news.ycombinator.com/item?id=35139591)
      Are you able to say more about that? "We will have local contractors" sounds great but in my area I don't think you will be able to find anyone to work with you. The local contractors and supply houses have closed ranks to fend off internet sales. I can't even buy sheet metal from the local supply houses without presenting an HVAC license. These folks are seeing their livelihoods threatened by a looming shift toward the "appliance" model (which I for one surely welcome) so they would see partnering to service a model like this as slitting their own throats. ^c35139591

      - **briHass** · [2023-03-13 19:29 UTC](https://news.ycombinator.com/item?id=35141147)
        Agree 100\% (I have my EPA cert and do my own installs) ^c35141147

        Trying to bust into the HVAC company cartel will be the death of this idea. Most HVAC companies are highly local and have built their business around partnerships with supply houses and the US big-boy manufacturers (e.g. Carrier, Trane, Lennox). The Asian brands (Mitsubishi, Midea, Gree) have taken years to start penetrating the US market, and even then, many have done so through partnerships with the above US brands.

        No reputable HVAC company is going to install a 'no name' dotcom branded unit that they won't be able to service with parts from their local supply house. They, and their suppliers, won't be getting the typical kickbacks or be able to mark up the unit costs and they likely won't offer any kind of warranty (at least on labor). To them, this is no different from Joe Homeowner ordering his MrCool/Goodman unit online and expecting them to install and service it for a low hourly fee. It's not worth their time or potential risk when the customer raises a stink a year later when that company reminds them they have zero warranty and parts aren't readily available.

      - **cmui** · [2023-03-13 19:23 UTC](https://news.ycombinator.com/item?id=35141069)
        There are ways of working with local HVAC contractors that provides value to them and doesn't just undercut their current way of business. Electric Air can provide lead gen, tools to support install, improved payment terms on jobs. ^c35141069

    - **nerdface** · [2023-03-13 19:16 UTC](https://news.ycombinator.com/item?id=35140965)
      \> This is not a bad route to go if you enjoy/feel comfortable doing the work and don't care about air quality, smart thermostat integration, etc ^c35140965

      You're insinuating that doing the work yourself means you'll have poor air quality, poor thermostat integration etc. That's not true at all. If you've gone to the trouble to do a DIY install then you're now already experienced enough to install a heat-recovery ventilator to get fresh air into your home via an independent system. I installed my own ecobee thermostat with my heat pump and electric furnace and it works with HomeKit so is integrated with my entire ecosystem.

      - **sokoloff** · [2023-03-13 23:24 UTC](https://news.ycombinator.com/item?id=35144705)
        Reading their comment slightly overly charitably vs what was written (but almost surely in-line with what was intended), they were contrasting their unit that has a HEPA filter bundled as part of their unit and that is not part of the Mr Cool unit. ^c35144705

        - **cmui** · [2023-03-14 00:25 UTC](https://news.ycombinator.com/item?id=35145418)
          Exactly. There's lots of stuff you can stitch together yourself, and if you're a DIY person, its more fun/rewarding to do it that way. I think the majority of homeowners will want something that doesn't require doing the install themselves, or having to worry about overall system integration. ^c35145418

    - **simplyaccont** · [2023-03-13 18:09 UTC](https://news.ycombinator.com/item?id=35139886)
      mr. cool has it's own smart thermostats/apps. you can use it also with nest/ecobee.
      with regards to air quality, usually this kind of stuff better managed by dedicated systems. ^c35139886

- **roamerz** · [2023-03-13 17:23 UTC](https://news.ycombinator.com/item?id=35139054)
  How do you compete with the likes of Mr Cool? Me and my father replaced his 15yr old heat pump/air handler in his house a few months ago. Took us a weekend and about \$4500. That was a 3 ton unit. ^c35139054

  Similarly we installed a 1.8 ton split unit in a new house. About \$2500 for that one.

  Both were complete kits including thermostat and required no refrigerant install as everything was pre charged. The 3 ton was even 21 seer if I remember correctly.

  These Mr Cool units sell locally at Home Depot and other places.

  - **telcal** · [2023-03-14 01:55 UTC](https://news.ycombinator.com/item?id=35146316)
    We also installed a Mr Cool DIY system in our house about 3 years ago. We also did it ourselves. It works well, no complaints, and has an app that you can control it anywhere with. 36k BTU 21.5 SEER Multi-Zone all for about \$3700. ^c35146316

- **Max-q** · [2023-03-13 22:11 UTC](https://news.ycombinator.com/item?id=35143716)
  In Norway most homes have one or more heat pumps. We are living in a cold climate and the pumps are being used like 9-10 months a year. ^c35143716

  The most common brands are Japanese: Toshiba, Mitsubishi and Panasonic.

  I will not agree that the user experience is bad at all. They are very good products. Stand alone they work well and with integration they work together with the power company to optimize the energy consumption vs energy price during the day.

  Be careful to just think the existing products are bad because you want them to be. It’s an existing, competitive, multi billion market with very good products.

  - **ttul** · [2023-03-13 22:15 UTC](https://news.ycombinator.com/item?id=35143785)
    They are UGLY though... ^c35143785

    - **ianlevesque** · [2023-03-13 23:16 UTC](https://news.ycombinator.com/item?id=35144602)
      It really depends. Old hot water radiators were ugly in their own way. Even with modern forced air HVAC I find the soffits and boxes to accommodate ductwork unsightly. ^c35144602

      Some brands make units that interface with existing radiant baseboards, or individual heat pump heads that recess entirely into the ceiling leaving just a vent visible, like [https://mylinkdrive.com/USA/M\_Series/R410A\_Systems-1/One\_Way...](<https://mylinkdrive.com/USA/M_Series/R410A_Systems-1/One_Way_Ceiling_cassette>)

    - **elif** · [2023-03-14 00:09 UTC](https://news.ycombinator.com/item?id=35145250)
      this is why I went with LG ceiling mounted cassettes. IMO it's even better than floor vents (they stay cleaner, floors are easier to clean) or ducted ceiling vents (each cassette can target the air movement direction actively toward humans). ^c35145250

      and all the electronic bits are in the attic so the noise is a little better.

    - **SamBam** · [2023-03-14 02:44 UTC](https://news.ycombinator.com/item?id=35146715)
      Who sees the indoor unit in a ducted system? ^c35146715

- **criddell** · [2023-03-13 17:49 UTC](https://news.ycombinator.com/item?id=35139550)
  My HVAC is 14 years old so we’re actually planning on replacing it sometime in the next 24 months. ^c35139550

  I’ve talked to a couple of HVAC companies already because I want more cooling power. When it’s above 100F (which it is for 3+ months of the year) my current system struggles to hold 80F. If we use the oven on a hot day, we may not get the temperature back down for days. Our winters are relatively mild (we don’t get much below 25F). We’re in central Texas.

  The HVAC companies I’ve spoken to won’t sell me an oversized system. They’ve never really said why, but from my research I think it has to do with mold problems resulting from cooling air with too much moisture in it. It doesn’t seem like a big ask for the thermostat to include humidity in its decision on how hard to run the AC, but apparently that doesn’t exist.

  Would one of your systems solve any of these problems? I’m not a DIY person, so I don’t really want to buy direct. Do you have installation partners in the Austin, TX area?

  - **adanto6840** · [2023-03-13 18:54 UTC](https://news.ycombinator.com/item?id=35140616)
    Sounds like you may have had a whole-home energy audit done already -- including a blower door test?  If not, I'd highly recommend it; I paid \~\$500 for one a few years back which included thermal imaging, blower door tests, airflow measurements & calcs, current/draw measurements for all energy-consuming devices, thermal load calcs, etc.  You may find better pricing even -- ours included a detached structure/office, and house is relatively large, multiple HVAC units/solar/pool/servers/etc... ^c35140616

    In my case, I didn't end up with any *super* directly-actionable insights -- but it was still very well worth the money IMO.  Even just to confirm that we weren't losing/"leaking" energy egregiously.  The reality was, our household simply uses a lot of energy - hah.

    I mention this all because, at the time, we were just about to replace our HVAC units & we had just installed solar + storage.

    I'm located in Las Vegas -- summers are HOT (!) -- but our units (2x 5-ton Bosch heat pumps) can near-trivially keep us at 70F (or cooler), even on the hottest of days.  I *try* to "push" the thermostats up a bit (we leverage a ToU energy plan), but there are days when the battle isn't worth having & the wife needs it at 69F -- and, even on the hottest Vegas days, we're able to hit it (can be expensive to do so, depending on time of day -- but is totally doable).

    Edit to add --  Oversizing a system can very easily lead to issues;  short-cycling, humidity control, etc.  The ideal system will run nearly non-stop on "design" temperature days. 
     See if you can find any highly-rated Bosch installers locally; they'd likely be willing to "oversize" a system since the Bosch units are "variable capacity" (inverter-driven), which means you're less susceptible to hitting some of the common issues/concerns when oversizing traditional systems.  Alternatively, the high-end variable-speed options from major brands are generally well-regarded though they can be extremely expensive (the price segmentation, and resultant value propositions, are bordering on dubious IMO).

    - **criddell** · [2023-03-13 21:55 UTC](https://news.ycombinator.com/item?id=35143475)
      Thanks for the Bosch recommendation. Your system is *much* larger than ours, but you likely have a lot more square footage (we are \~2100 sq ft). I don’t recall the exact number, but I think we are 2.5 or 3.5 ton. ^c35143475

      Our system is old enough that it’s just time to replace. It’s the one the builder installed 14 or 15 years ago and it’s fairly low end.

      What you’ve accomplished in your home is exactly what my installer tells me they can’t do. He told me no matter how large of a system I buy, the system will never be able to pul the indoor temperature down more than about 20F (internet searches for “max ac cooling” seem to back that up). He says a bigger system will get me down to the 20F floor faster, but that’s it.

      I don’t believe it though because of stories like yours and because commercial spaces around here are very cold on hot days.

      - **adanto6840** · [2023-03-13 23:54 UTC](https://news.ycombinator.com/item?id=35145068)
        I'd probably suggest checking out Reddit (r/hvac for pros, and r/hvacadvice for homeowners) -- you'll generally get really good advice, often from professionals, if you provide good inputs/context. ^c35145068

        If you have 2+ floors, you probably need (or have) zones, and it may be worth paying a professional to engineer a solution that meet your requirements.  I recall finding some small businesses online that do exactly this for a nominal fee (\<\$500 IIRC).

        You might also consider looking for residential HVAC companies that also do commercial refrigeration;  the conceptual physics for commercial refrigeration aren't much different from residential HVAC, just specialized refrigerants & components that are tailored to those use-cases (ie labs often require extra-cold freezers, etc).

        FWIW, my gut is you'd be happy with most variable-speed offerings, if sized appropriately. Low humidity here makes it easier, but I'm sure you can do what you want, but it may not be cheap.

  - **brudgers** · [2023-03-13 18:51 UTC](https://news.ycombinator.com/item?id=35140562)
    You don't want an over-sized system. ^c35140562

    They short cycle.

    An over-sized system can quickly cool to the thermostat setting, but leave the latent heat in the water vapor in the air.

    So you experience the "feels like" temperature...it's not the heat, as they say.

    A properly sized system runs long enough to condense water vapor and with it remove the latent heat from the air.

    - **criddell** · [2023-03-13 21:50 UTC](https://news.ycombinator.com/item?id=35143388)
      The short cycle argument only really applies to older and low end systems that are not variable speed. ^c35143388

      A variable speed system integrated with a humidifier should be able to slowly bring the temperature down, making sure that the cooling does not get ahead of the dehumidifying.

      I want an “oversized” system that can do \> 20F temperature drops. I know they exist because a lot of commercial spaces have them.

      - **unknown** · [2023-03-13 22:30 UTC](https://news.ycombinator.com/item?id=35143975)
        [deleted] ^c35143975

      - **brudgers** · [2023-03-13 23:38 UTC](https://news.ycombinator.com/item?id=35144890)
        Short cycling is thermodynamics, not an argument. ^c35144890

        - **criddell** · [2023-03-14 00:53 UTC](https://news.ycombinator.com/item?id=35145727)
          As I understand it, short cycling is a problem with air conditioners that cycle on and off. You can get staged compressors, multi-speed compressors, and truly variable speed compressors. A truly variable speed compressor runs continuously and so won’t short cycle. ^c35145727

  - **tutorialmanager** · [2023-03-13 18:11 UTC](https://news.ycombinator.com/item?id=35139930)
    How about just adding a small minisplit with heat. Warm day \= use the minisplit. Hot day \= existing central air. Very hot\= use them both. If one goes down you still have something while you wait for repair. The mini split could also provide some heating when its mildly cold. ^c35139930

    - **criddell** · [2023-03-13 18:16 UTC](https://news.ycombinator.com/item?id=35140015)
      We had a mini split installed into our garage (a Daikin that’s been great). I’m not sure how we would do that for the house. It’s a forced air system with outlets and return air in every room. I’m not sure how feasible it would be to pipe the output from a split system into that ductwork. ^c35140015

      - **turtlebits** · [2023-03-13 18:24 UTC](https://news.ycombinator.com/item?id=35140140)
        Mini splits aren't ducted (generally the air handler is mounted high up on a wall).  They are great for spot heating. ^c35140140

        - **sokoloff** · [2023-03-13 23:29 UTC](https://news.ycombinator.com/item?id=35144777)
          *Ductless mini-splits* aren't ducted. (These are the type most are familiar with, the ones with a large air handler up on the wall or in a ceiling cassette.) However, mini-split just means that the condenser and evaporator units are separate ("split") and are smaller capacity ("mini") than a traditional central air system (which are also "split"). ^c35144777

          There are ducted mini-splits in addition to ductless mini-splits.

  - **buttersbrian** · [2023-03-13 18:03 UTC](https://news.ycombinator.com/item?id=35139773)
    Have you considered assessing your home's insulation? ^c35139773

    - **criddell** · [2023-03-13 18:13 UTC](https://news.ycombinator.com/item?id=35139949)
      We did. We had more insulation blown into our attic (it gets crazy hot up there) and we are now looking for new windows. ^c35139949

      - **tguvot** · [2023-03-13 22:39 UTC](https://news.ycombinator.com/item?id=35144112)
        actually i'll advise you to take a look at temperature of your walls. both inside and outside. they have a bunch of thermal mass. during the summer they effectively heat the air inside the house. unless you manage to cool walls somewhat (lets say during night), hvac will have to really fight to keep temperature down. I live in bay area and I installed whole house fan which is typically runs through the night at summer. For most of the cooling season it sufficiently cools air and walls in order to require only a couple hours of hvac a day. ^c35144112

        additional point, you wrote that you have current system installed 15 years ago. back than design temperatures (i.e. how hvac sized based on outdoor temperature) were different. recent updates sometime bring those temperatures up by 10F or so, what can result in extra half a ton - ton of hvac.

        you could retain company to make a proper hvac sizing (called manual j calculation). hvac contracts from my expirience won't do it.

        - **criddell** · [2023-03-13 23:11 UTC](https://news.ycombinator.com/item?id=35144526)
          Our walls are good but our windows are a weak point. ^c35144526

          During summer, the night temperature drops to the low 90’s here. It’s A/C all day, every day, for at least 3 months.

          Any idea why the HVAC guy and just about every source online insists that A/C can only give you a temperature delta of 20F? I know it can’t be true, but that claim is everywhere.

          - **sokoloff** · [2023-03-13 23:35 UTC](https://news.ycombinator.com/item?id=35144849)
            There's a lot of poor engineering fundamentals among some HVAC salespeople and some websites as well as some sloppy writing. ^c35144849

            The delta-T that is correctly cited as being "around a max of 20°F" is the delta in temperature *across the evaporator* (IOW between the return duct and the supply duct \[aka the goes-inta and the goes-outta\]). It's not the delta-T between the *outside air and inside air*.

            With good enough insulation and/or enough cooling, you can get whatever delta-T you want as is obviously the case with refrigerators and freezers.

            - **tguvot** · [2023-03-14 00:05 UTC](https://news.ycombinator.com/item?id=35145206)
              \>The delta-T that is correctly cited as being "around a max of 20°F" is the delta in temperature across the evaporator (IOW between the return duct and the supply duct \[aka the goes-inta and the goes-outta\]). ^c35145206

              well said. i have temp sensor on supply and return and I graph them and delta, to make sure that hvac works within proper parameters. otherwise during heat waves you start thinking that hvac maybe out of shape

            - **criddell** · [2023-03-14 00:42 UTC](https://news.ycombinator.com/item?id=35145608)
              So in places like Arizona where the outside temperature can reach 120F and the inside temperature has to be 82F (what landlords are required to provide to tenants), are they just using bigger units than they would in some place where the temperature rarely breaks 95? The refrigerants are the same? ^c35145608

              - **sokoloff** · [2023-03-14 00:48 UTC](https://news.ycombinator.com/item?id=35145673)
                Same refrigerants work. Getting a large decrease in temp vs outside is a matter of insulation, air sealing, roof/wall color, and sizing of units/ducts. ^c35145673

                - **criddell** · [2023-03-14 00:55 UTC](https://news.ycombinator.com/item?id=35145763)
                  Thanks for the information. ^c35145763

                  One more question- what about commercial spaces where they will have a door open and be flooding the store with ice cold air. It sure feels like more than a 20 degree difference.

                  - **sokoloff** · [2023-03-14 01:06 UTC](https://news.ycombinator.com/item?id=35145875)
                    It's still just a 20°F difference from the vent that the AC sucks air from to the supply the AC blows out of. ^c35145875

                    That has (essentially) nothing to with the relationship between the indoor and outdoor temp.

                    For simplicity, imagine a balmy 110°F outside temp, an 80°F inside temp. That's 30°F from inside to outside \[and will feel refreshing\], but probably results from a supply temp \[the coldest air coming right out of the vent\] at 68°F, a return temp \[the air being drawn into the AC duct\] of 88°F.

                    The key 20°F delta-T is the measure between the 88°F and the 68°F (both temperatures inside the conditioned \[in other words, "indoor"\] space). All of the other temperatures can be all over the place. Even if the outside temp was 120°F, provided the unit was sized large enough or the insulation good enough, the indoor air might average 80°F and keep the same 88°F/68°F \[20°F delta-T\].

                    As a more extreme example, your freezer probably works on a delta-T of \~10°F. That's the difference between the air going into the evap coil area and the outlet. If your indoor kitchen temperature is 80°F, your freezer still keeps things frozen even though its delta-T is only 10°F. You don't take the 10°F from the 80°F. You take the 10° from the 30-ish°F and get a warm temp of 30°F and a cold temp of 20°F in the freezer.

          - **tguvot** · [2023-03-13 23:23 UTC](https://news.ycombinator.com/item?id=35144694)
            \>Our walls are good but our windows are a weak point. ^c35144694

            are you sure ? at summer I have walls that are 170F outside (at 2pm) and 80-90F inside. Also, window will pass through heat only during the day. Wall will keep heating your inside air through the night as well. Get some cheap thermal camera - it's very educational.

            You should also check your ductwork/registers. To see if there are any tears/openings/etc. Also, in case you are using flex duct, if it's not tensioned properly, sagging, etc - there will be a lot of air velocity losses that reduce overall cooling experience.

            \>Any idea why the HVAC guy and just about every source online insists that A/C can only give you a temperature delta of 20F? I know it can’t be true, but that claim is everywhere.

            Something around refrigerant properties, mechanics and physics, etc. I also spent some time in this rabbit hole

- **Nition** · [2023-03-13 18:46 UTC](https://news.ycombinator.com/item?id=35140479)
  It's strange seeing this post describe heat pumps as if they're a new thing, and everyone commenting as if they are. ^c35140479

  I live in New Zealand and heat pumps have been standard in new builds for just about 20 years now. They're great. If you want to add one to your home you can call up various companies to do it for reasonable prices (not sure how this stacks up against US prices, but I recently had a small 2.5kW cool/3.2kW heat mini split heat pump installed in my office room for \$1,200USD including labour). It helps that we have relatively mild seasons, with it getting just a little too cold in winter and a little too hot in summer - pretty much the ideal environment for a heat pump.

  I have never seen a residential home in NZ with a furnace or a pure air conditioner (that can't also heat). The standard installed system before heat pumps was a wood fire or sometimes gas heaters. In summer you just put up with being hot.

  Re smart thermostats, I've been in many homes with heat pumps and never seen one. Everyone just uses the controls in the heat pump remote. They all have the option to cool to a certain temp, heat to a certain temp, stay at a certain temp, and set a start/stop time. Basic but generally good enough.

  Re ducted systems, my experience is they never seem quite as efficient or effective as just installing two totally separate mini split systems. Which is also usually cheaper and has the added bonus that you can only run one if you're not in the other part of the house.

  Looking at your wall unit, it looks really nice, but can that front face tilt to blow air either up or down?

  - **thaeli** · [2023-03-13 19:00 UTC](https://news.ycombinator.com/item?id=35140723)
    I'm in the US and have had a heat pump for 15 years. It was a fairly small cost add from a straight cool. I get this depends on region, especially for the older units, but I never understood why they were such a hard sell even in mild heating climates. ^c35140723

    Ironically, I bought this system because at the time natural gas looked like it would be becoming more expensive more quickly than electricity in my area. Since the cost delta was small, and I don't think it made my total monthly utility bills any higher, no big deal, but I might not have even bothered with a heat pump if I'd known about the fracking boom at the time. (I'm also fortunate enough to live in a state with powerful utility regulators, so electricity prices never spiralled like they did in "deregulation" areas.)

    - **kevstev** · [2023-03-13 20:14 UTC](https://news.ycombinator.com/item?id=35141839)
      Interestingly, I am in the middle of replacing my HVAC which died last fall. I was dead set on getting a heat pump. I didn't really care about the increased upfront cost, so long as I was getting increased comfort and there would be a reduction in costs after install. ^c35141839

      When I really looked at the numbers though, my cost of electricity is so high, and my natural gas is so cheap, that I would need a COP of over 5 or an HSPF of around 20 on the heat pump to just break even on heating- I pay about 16.5 cents per KWH for electricity all in, and \$1.05/therm for natural gas in NJ just outside of NYC. Efficiencies that high don't exist on central units. It would cost me easily an extra \$100/month to heat my home, and the additional upfront cost was \$7-10k. In cooling mode they are slightly less efficient than the best AC units as well, not by a significant amount- but its not like it will make up for it on the  cooling side of things.

      I really wanted to go this route, but this would be an extra upfront as well as ongoing cost. I really have no option but to replace with a conventional system and in 10-15 years re-evaluate. I will likely eventually get solar, but my roof is currently close to, but not yet at its end of life, and I have a townhome with limited roof space and a historic district to contend with, its not going to solve the electricity cost problem.

  - **AnonMO** · [2023-03-13 20:31 UTC](https://news.ycombinator.com/item?id=35142086)
    I don’t think he ever sold it ad new tech its more of a Silicon Valley spin on old tech. And heat pump are in the US but many are hesitant because of the climate in the states can be extreme and as you said NZ has a milder climate compared to the US. for example in my state just last month we hit lows that aren’t supported by any heat pump on the market for days on end but my furnace kept me warm and on the other side of the country temperatures break world record highs every year. Everything op said fits the US market very well heat pump demand is on the rise, alot of people have smart thermostats they’re even provided by some utility companies, the product is a very compelling. ^c35142086

  - **dang** · [2023-03-13 19:37 UTC](https://news.ycombinator.com/item?id=35141255)
    Heat pump passion is kind of a thing for some reason! ^c35141255

    *200-year old heat pump technology is back* \- [https://news.ycombinator.com/item?id\=34846762](<https://news.ycombinator.com/item?id=34846762>) \- Feb 2023 (205 comments)

    *How a heat pump works* \- [https://news.ycombinator.com/item?id\=34739375](<https://news.ycombinator.com/item?id=34739375>) \- Feb 2023 (324 comments)

    *Heat pumps are defying Maine’s winters and oil industry pushback* \- [https://news.ycombinator.com/item?id\=34708161](<https://news.ycombinator.com/item?id=34708161>) \- Feb 2023 (174 comments)

    *Heat pumps of the 1800s are becoming the technology of the future* \- [https://news.ycombinator.com/item?id\=34397715](<https://news.ycombinator.com/item?id=34397715>) \- Jan 2023 (477 comments)

    *Do heat pumps work in cold climates?* \- [https://news.ycombinator.com/item?id\=34352309](<https://news.ycombinator.com/item?id=34352309>) \- Jan 2023 (326 comments)

    *French startup unveils new residential thermo-acoustic heat pump* \- [https://news.ycombinator.com/item?id\=34233719](<https://news.ycombinator.com/item?id=34233719>) \- Jan 2023 (219 comments)

    *US companies are producing heat pumps that work below -20F* \- [https://news.ycombinator.com/item?id\=34160672](<https://news.ycombinator.com/item?id=34160672>) \- Dec 2022 (330 comments)

    *Heat pumps are now mandatory in new homes in Washington State* \- [https://news.ycombinator.com/item?id\=33589627](<https://news.ycombinator.com/item?id=33589627>) \- Nov 2022 (48 comments)

    *WA building council votes to require heat pumps in new homes and apartments* \- [https://news.ycombinator.com/item?id\=33526419](<https://news.ycombinator.com/item?id=33526419>) \- Nov 2022 (14 comments)

    *Homemade Heat Pump Manifesto (2009)* \- [https://news.ycombinator.com/item?id\=32959850](<https://news.ycombinator.com/item?id=32959850>) \- Sept 2022 (247 comments)

    *Show HN: Heat Pumps, Hooray – A heat pump calculator for your home* \- [https://news.ycombinator.com/item?id\=32838748](<https://news.ycombinator.com/item?id=32838748>) \- Sept 2022 (56 comments)

    *Interest in heat pumps has increased dramatically in recent years* \- [https://news.ycombinator.com/item?id\=32712140](<https://news.ycombinator.com/item?id=32712140>) \- Sept 2022 (257 comments)

    *Heat pumps: what they do and why they’re hot now* \- [https://news.ycombinator.com/item?id\=32431077](<https://news.ycombinator.com/item?id=32431077>) \- Aug 2022 (23 comments)

    *Heat pumps are efficient and eco-friendly. So why are they so rarely used?* \- [https://news.ycombinator.com/item?id\=32182699](<https://news.ycombinator.com/item?id=32182699>) \- July 2022 (34 comments)

    *Värtan Ropsten – The largest sea water heat pump facility worldwide (2017) \[pdf\]* \- [https://news.ycombinator.com/item?id\=31985467](<https://news.ycombinator.com/item?id=31985467>) \- July 2022 (19 comments)

    *DOE announces breakthrough in residential cold climate heat pump technology* \- [https://news.ycombinator.com/item?id\=31791444](<https://news.ycombinator.com/item?id=31791444>) \- June 2022 (398 comments)

    *We must ban boilers to force public to switch to £10k heat pumps'* \- [https://news.ycombinator.com/item?id\=31086020](<https://news.ycombinator.com/item?id=31086020>) \- April 2022 (26 comments)

    *Why Heat Pumps Are Immensely Important* \- [https://news.ycombinator.com/item?id\=30814536](<https://news.ycombinator.com/item?id=30814536>) \- March 2022 (23 comments)

    *You and the planet need a heat pump* \- [https://news.ycombinator.com/item?id\=30746081](<https://news.ycombinator.com/item?id=30746081>) \- March 2022 (139 comments)

    *Warmth from the earth and air: could heat pumps replace our gas boilers?* \- [https://news.ycombinator.com/item?id\=28258855](<https://news.ycombinator.com/item?id=28258855>) \- Aug 2021 (13 comments)

    *Heat Pump Water Heaters* \- [https://news.ycombinator.com/item?id\=23000192](<https://news.ycombinator.com/item?id=23000192>) \- April 2020 (214 comments)

    *Heat Pumps Work Miracles* \- [https://news.ycombinator.com/item?id\=19271162](<https://news.ycombinator.com/item?id=19271162>) \- Feb 2019 (243 comments)

    - **robomartin** · [2023-03-13 20:15 UTC](https://news.ycombinator.com/item?id=35141852)
      \> Heat pump passion is kind of a thing for some reason! ^c35141852

      Because they are throwing money at it.  Billions.  All policy driven, not science-driven.

      If every home in the US switched to electric powered HVAC heat-pump systems we'd have huge blackouts in every city.  Our power grid and power generation systems are not ready for this at all.  Add electric cars to the mix and the scenario gets much darker (no pun intended, lights will go out!).

      This is a case of placing the cart ahead of the horse.  We are in desperate need of a non-trivial 25 year program to *double* out reliable power generation and delivery infrastructure.

      - **cmui** · [2023-03-13 20:20 UTC](https://news.ycombinator.com/item?id=35141917)
        You're right about switching everything over all at once. That would be a big step change in grid load! But large scale heat pump adoption is going to take a decade or more, and in the meantime we can work to build out the grid, and also on technologies that make load shifting more feasible. ^c35141917

        - **robomartin** · [2023-03-13 21:23 UTC](https://news.ycombinator.com/item?id=35142960)
          Of course.  My issue is that there seems to be no serious acceptance of this reality and, therefore, a strong political push to address it.  All we talk about are the wonders of electric-everything, as if power will magically appear from somewhere. ^c35142960

          Gradual adoption is conceptually easy to understand, except that in certain places it will not take much for gradual adoption to reach a threshold that will lead to a painful reality.  Speaking in terms of Southern California, it doesn't take much for a city like Los Angeles to create a power availability/grid crisis.  We've already been there multiple times.

          The issue with *reliable* (strong emphasis on that term) power generation is that, in the US, it takes decades and much red tape to address it.  In other words, cart before the horse:  We can't afford to materially increase demand without a solid preexisting plan to also materially increase supply ahead of demand.  The two need to be out of phase, with power generation build-up happening first.

      - **PaulDavisThe1st** · [2023-03-14 00:08 UTC](https://news.ycombinator.com/item?id=35145239)
        Let's suppose that you want to switch over, say, Chicago, to be fully electric heat pump driven. Let's further suppose you want to do this over 25 years. ^c35145239

        There are just over 1M households in Chicago. If we assume (wrongly) that nobody has heat pumps today, that conversion needs to take place in 123 households every day of every year for the next 25 years. If the contractors don't work weekends, it's 153 households a day.

        And all this while the same thing has to take place in Houston, NYC, LA and cities and towns of every size *at the same time*.

        That's a huge task even spread out over 25 years. It seems very unlikely we will meet that goal, so your hand wringing over heat-pump induced blackouts seems misplaced.

        - **robomartin** · [2023-03-14 06:42 UTC](https://news.ycombinator.com/item?id=35148123)
          \> your hand wringing over heat-pump induced blackouts seems misplaced. ^c35148123

          I would very much appreciate it if we could keep to a mutually-respectful conversation rather than resorting to insults.  We only learn if we respect each other's positions.  I have no problem being wrong.  Show me how and will forever be grateful.

          I have no problem with anyone challenging anything I say.  Thanks for questioning my claim.

          I can't get into numbers for Chicago without doing much research.  Not sure that data exists.  This is what I was able to find quickly though:

          [https://www.statista.com/statistics/220357/manufactured-ship...](<https://www.statista.com/statistics/220357/manufactured-shipments-of-unitary-air-conditioners/>)

          According to this information over six million HVAC systems were sold per year in 2021.  I think it is fair to assume these systems were installed.  They don't provide information on the geographic distribution, kind or type of installation (residential, commercial or industrial).

          What it says for me is that there's a great deal of installation capacity.  This page gives us a sense of the concentration of contractors per state:

          [https://www.statista.com/statistics/1243016/plumbing-and-hva...](<https://www.statista.com/statistics/1243016/plumbing-and-hvac-contractors-by-state-usa/>)

          This association link gives us an idea of how many HVAC contractors exist in the US:

          [https://www.ibisworld.com/industry-statistics/number-of-busi...](<https://www.ibisworld.com/industry-statistics/number-of-businesses/heating-air-conditioning-contractors-united-states>)

          Their number is 145K.

          The first link says Illinois has about 4100 contractors, or 2.8\% of the national number.

          I am just trying to get a sense of proportion here with some quick math.  I do realize these numbers come from different years.

          If I take the 6 million annual HVAC system sales rate for the US and calculate 2.8\% of that, we get 168K units per year.  Per this metric, installing a million units would require just 6 years.

          If the million units, on average \[0\], require 3 kW of power, we are adding a power requirement of 504 MW per year.  I am trying to keep it simple.  In terms of power demand, the average is meaningless \[0\], what matters are outliers on the high side of the distribution curve.  Keeping it simple...

          By this metric we would need to build half a nuclear power plant \[1\] per year in Illinois, for a total of three brand-new nuclear power plants in six years.

          I think these numbers more than support my thinking that power problems might be severe.  If we understand that, once again, averages are a horrible metric \[0\], the numbers are likely much higher than this.

          Over that period of time electric ground transportation would experience significant growth, further exacerbating the problem.

          BTW, I have not addressed the issues we will have with the grid itself --power transmission lines, substations, transformers, etc.-- not being able to handle the increased load.

          The current estimate is that a full transition to electric vehicles will roughly require a doubling of the entire US power generation and transmission infrastructure \[3\].  This means the equivalent of 1200 brand new nuclear power plants.  By this I do not mean we have to build that many, I am using them as a unit of measure for a sense of proportion \[1\].  Electric heat pumps will add significant demand on top of this.

          As I said in another post, this, I feel, is a cart before the horse situation.  There's nothing wrong with electrification.  What's wrong is that we need to put the horse (power generation) ahead of the cart.  As far as I can tell, we are not doing that, at all, anywhere.  Solar and wind are not enough.  We need a non-trivial program to boost energy generation and transmission capacity.  This, in my opinion, must include nuclear power.

          Notes:

          \[0\] I truly hate using averages because it is a horrible figure that has no merit when applied to the entire population.

          [https://en.wikipedia.org/wiki/Tyranny\_of\_averages](<https://en.wikipedia.org/wiki/Tyranny_of_averages>)

          [https://en.wikipedia.org/wiki/Anscombe\%27s\_quartet](<https://en.wikipedia.org/wiki/Anscombe%27s_quartet>)

          \[1\] I like to use nuclear power plants for a sense of proportion because the typical plant is rated at 1 GW and people can understand the severity of needing new nuclear power plants.

          \[3\] [https://www.youtube.com/watch?v\=TcI6FaaDp8g&t\=3510s](<https://www.youtube.com/watch?v=TcI6FaaDp8g&t=3510s>)

          - **PaulDavisThe1st** · [2023-03-14 17:59 UTC](https://news.ycombinator.com/item?id=35155671)
            There's a major study out of Princeton from a year or two ago that fully covers what is needed for full electrification with only renewables, and with mostly renewables. It covers all this much better than I could, especially here on HN: ^c35155671

            [https://netzeroamerica.princeton.edu/the-report](<https://netzeroamerica.princeton.edu/the-report>)

            My take on that report is "yep, this would/will be a major effort, as large as anything we've ever done, but not much more than an order of magnitude beyond anything we've ever done".

            - **robomartin** · [2023-03-14 22:10 UTC](https://news.ycombinator.com/item?id=35159716)
              Yeah, from my perspective, the fact that it is large isn't the problem.  The issues is that we can't seem to get anything done.  Politicians --of all denominations-- stopped working for us and towards solid long term objectives for the benefit of society a long time ago, decades.  Their focus is firmly aimed at winning elections and opposing the other side.  We, the people, well, we don't really matter, all they want is our votes.  Stupid us. ^c35159716

              A prime example of this is the "high speed" train here in California.  They said the bill was ten billion.  We are in for over a hundred billion.  What had been built isn't finished and it isn't even high speed (I think it tops out at around 50 mph).  The whole thing is a disgusting example of just how dysfunctional we have become as a nation.

              And so, I look at the idea of having to, say, double, our power generation and distribution infrastructure and the only equation that balances out in my head says: Good luck.  It will never happen.

              I hope I am wrong.  A sign of this would be for these people (politicians) to finally get their heads out of their behinds, work together and put forth a solid 25 year plan to materially expand our power generation and distribution.  A plan that is executable, not some hand-wavy thing that will never happen.

              Anyhow, I don't want to be a pessimist, yet, I can't see any evidence of anything that might lead me to believe this nation is capable of the great things we accomplished in the past.  The Hoover Damn could not be built today.  We could say that about almost every large scale project going back a century or more.  Can you imagine proposing to build the Panama Canal today?  Right.

              In this context, we are waving our hands and talking about 300 million electric cars and 100 million all-electric homes.  Part of me things "C'mon.  Get serious".

              - **PaulDavisThe1st** · [2023-03-14 22:33 UTC](https://news.ycombinator.com/item?id=35160061)
                I would recommend listening to the Ezra Klein show interview with one of the main authors of the NetZero Princeton report. It is not recklessly optimistic, but I was surprised to finish it and have a sense "hell, maybe we might actually pull this off". ^c35160061

                [https://www.nytimes.com/2022/09/20/opinion/ezra-klein-podcas...](<https://www.nytimes.com/2022/09/20/opinion/ezra-klein-podcast-jesse-jenkins.html>)

                The title is a bit click-baity, so ignore that.

                - **robomartin** · [2023-03-15 00:38 UTC](https://news.ycombinator.com/item?id=35161961)
                  I'll read the report and watch this interview over the next few days. This looks really interesting.  I hope it serves to realign some of my thinking.  Thanks for posting this. ^c35161961

                  - **PaulDavisThe1st** · [2023-03-15 00:51 UTC](https://news.ycombinator.com/item?id=35162096)
                    Note also that Ezra is currently *really* into his "why can't we do stuff any more phase" and has had a couple of good shows and a couple of NYT op-eds about it, plus a whole book on the topic. He's particularly oriented now, as a multi-year CA resident, on how this cannot be blamed on partisan stuff, since even (or especially) in "blue" states where Democrats hold all the power, stuff still does not happen. ^c35162096

                    I don't like his conclusions, but it is hard to argue with them (at least for me).

                    - **robomartin** · [2023-03-15 11:05 UTC](https://news.ycombinator.com/item?id=35166386)
                      You reminded me of a funny segment in a famous George Carlin joke about religion.  My apologies if you are a believer, please just take this as what it is: comedy. ^c35166386

                      "Something is wrong here. War, disease, death, destruction, hunger, filth, poverty, torture, crime, corruption, and the Ice Capades. Something is definitely wrong. This is not good work. If this is the best God can do, I am not impressed. Results like these do not belong on the résumé of a Supreme Being. This is the kind of shit you’d expect from an office temp with a bad attitude. And just between you and me, in any decently-run universe, this guy would’ve been out on his all-powerful ass a long time ago."

                      This is the kind of thing I think about when I watch reality happen and compare it to the fantasies people construct about what we can actually accomplish these days.  You are right, this has nothing to do with political party; each having its own maddening twists and turns.

                      We just can't get things done.  Not just when it comes to a large scale.  I have two personal examples.

                      First, our street, which is 25 years old (I've been here since the neighborhood was built) was repaved twice and, I am told, will be repaved again next year.

                      Why?  Was it in bad shape?

                      Not even close.  You could almost play pool on this street.  It is, for most intents and purposes, perfect.  There was no need to touch it.

                      The same is true of our sidewalks.  Again, 25 years old.  They were fine.  They came through, jack-hammered about 50\% of it (non-contiguos, of course) and re-poured it all.  It looks horrible now, because, of course, they used a different color concrete and the work itself looks like shit (not the same quality and care, they patterned it a bit different, etc).

                      Why?  To keep the union guys busy.  That's the only reason I can find.  I don't understand why they didn't send them to neighborhoods where this was actually needed.  We have plenty of those in Southern California.

                      I was just in Singapore on business for a couple of weeks.  The streets and highways on this tiny nation  (\~ 12 x 30 miles) make the crap we drive on in SoCal every day truly look like third-world worthy roads.  And the taxes we pay for road maintenance are some of the highest in the nation.  The roads in Florida are luxurious compared to our pot-hole ridden streets and highways.

                      The other story has to do with our schools.  Years ago, when my kids were in middle school, they had a science teacher that was anything but that.  He is a Chiropractor who works as a science teacher.  This guy is clueless and verbally abusive.  For example, he told the kids that the moon does not spin about its axis.  If anyone questioned him, he would get angry.  And that's just one example of many.  Yes, he is still there.  We could not get him fired or reassigned to basket-weaving class.  There are kids coming out of that school who do not have parents with scientific training who come out believing all sorts of nonsense.

                      Why does this happen?  Is it incompetence?  Is it that our culture has devolved into something we should be ashamed of?  I really don't know.  What I do know is that countries like China are placing one foot in front of the other while, in the US, we can't do anything at scale, we waste time and money rebuilding streets and sidewalks that are just fine and we are causing our kids serious mental damage by teaching them absolute bullshit at every level.

                      Don't get me started about 20-somethings.  I was just at the SxSW conference in Austin.  I had a few very interesting conversations with 20-somethings who, in this case, actually had it together.  A couple of the US.  Most of the rest from other countries.  The kids from the US gave me a perspective on what their peers are being taught and how they think that I honestly wish I did not have.  To parrot George Carlin...

                      Something is definitely wrong. This is not good work. If this is the best the US can do, I am not impressed. Results like these do not belong on the résumé of an advanced nation. This is the kind of shit you’d expect from a dictator with a bad attitude running a banana republic.

                      I am trying very hard not to be a pessimist when it comes to our future.  I have to admit the results in front of me make it difficult to switch to a half-full view of the US.  Frankly, in this environment, one can almost understand and justify the need for someone like Donald Trump.  You actually need someone with enough power and an I-don't-give-a-fuck attitude to come in, rip this putrid system apart to the studs and rebuild it into something that actually works.

                      So, here we are, talking about installing billions of solar panels (made in China) and billions of batteries (made in China) and billions of inverters, cables, electrical components, etc. (all made in China) when we can't maintain our roads and stop teaching our kids bullshit.

                      This will represent the largest-ever transfer of wealth from one nation to another in the history of humanity.  We will forever be dependent on China for almost everything if we continue down this path.  These massive installations will require parts and materials, all coming from China.  If the Chinese were smart --and they are, very much so-- they would carefully come up with a way to implement what I am going to call "sensible" failure rate on the products they sell us.  This will guarantee millions of units per year in sales for replacement components in support of our wonderful power generation and distribution system...forever.  It's like selling drugs to a drug addict.

                      This is one of the reasons for which I think of nuclear and wind as potential alternatives to solar (and I do like solar).  I think the supply chains for these forms of energy can be constrained to the US, Europe and countries outside of China.  I could be wrong, of course.  I just think it is beyond stupid to send everything to China and not think strategically at all.

                      It reminds me of "Fire one million":

                      [https://www.youtube.com/watch?v\=r0mO6UY6uTg](<https://www.youtube.com/watch?v=r0mO6UY6uTg>)

                      (sorry, that was a bit of a rant)

                - **robomartin** · [2023-03-16 08:46 UTC](https://news.ycombinator.com/item?id=35179630)
                  \> [https://www.nytimes.com/2022/09/20/opinion/ezra-klein-podcas...](<https://www.nytimes.com/2022/09/20/opinion/ezra-klein-podcast-jesse-jenkins.html>) ^c35179630

                  Their short (7 minutes) summary of findings is good.  It might compel some to dig deeper.

                  [https://www.youtube.com/watch?v\=REDKd3wT220](<https://www.youtube.com/watch?v=REDKd3wT220>)

                  Listening to the long interview now.  They are hitting on points that I have been talking about for years.  Points that earned me countless, and sometimes vicious, attacks here on HN and relentless down-voting.  This is an audience that is supposed to be analytical.  Sadly, I have discovered the hard way that the loud-mouths, the bullies, are nothing of the sort.  As is always the case, the moderate thinking majorities tend to not get involved, and the bullies win.

                  The part you did not know is that I wrote a simulation model some five years ago to try and help me understand all of this.  It would be fair to call it a Monte Carlo Simulation.  It created millions of behavioral avatars with randomized patterns of electrical vehicle usage (driving, charging, etc.).  It also distributed these across all six time zones in the US.  It then calculated peak charging requirements per region and cranked out a range in the aggregate.  The result was an estimate between 900 GW and 1400 GW.

                  I was not able to confirm this until last year, when someone asked Elon Musk about this and he said we need to more than double our power generation capacity.  That's why I became so confident in my estimate.

                  I am also going through the entire research report.  This will likely take a few weeks (I only have weekends available for something like this).

                  I did discover I am wrong about something I've been claiming.

                  I've been saying we need approximately 1200 GW of new power.

                  That's not correct.

                  We need 2400 GW.

                  Why?

                  Silly mistake on my part.  I forgot that part of the objective is to *replace* our "dirty" power generators with clean energy.  If the objective was to support electric vehicles, the answer is somewhere around 1200 GW.  However, this report made me realize I had skipped over the obvious part:  We want our entire power system to be clean.

                  This means we need 1200 GW of brand-new clean energy to replace the dirty power we have right now.  And then, we need another 1200 GW to power electric cars.  My guess is likely much more than that once we account for electric heat pumps and stoves in every home.

                  So, yeah, I was wrong.  My estimate made the problem far simpler than what it actually is.

                  We have to rip-up our entire power generation infrastructure, replace it with a new one and then more than double it.  All by 2050.  Good luck.

                  I can't even imagine the degree of verbal violence I will be subjected to on HN when I say we need 2400 GW and the "true believers" blow a fuse.

                  Fantastic study.  Thanks for posting it.  Much to learn and think about.  I am glad that I hear them talk about things a hundred years away as options rather than being all-in on getting there in 20 years or some of other seriously flawed claim.

  - **nfriedly** · [2023-03-13 19:58 UTC](https://news.ycombinator.com/item?id=35141588)
    In the US, heat pumps are not unheard of, but they are fairly rare. (Not counting air conditioning, which no one here thinks of as a "heat pump" even tough it essentially is.) ^c35141588

    Trying to get a HVAC company to install a heat pump can be very difficult and/or expensive in may parts of the US.

    - **PaulDavisThe1st** · [2023-03-14 00:04 UTC](https://news.ycombinator.com/item?id=35145197)
      More or less every HVAC contractor in the Santa Fe/ABQ area pushed heat pumps on us when we wanted a solution for our home 3 years ago. That doesn't mean it's not hard in some places, but we're a (very) small population low density state, so if you can get it done here ... ^c35145197

    - **mayli** · [2023-03-13 23:30 UTC](https://news.ycombinator.com/item?id=35144790)
      Isn't AC just a heat pump that pumps heat to outside, and a heater if you install it reversely? ^c35144790

      - **nfriedly** · [2023-03-13 23:40 UTC](https://news.ycombinator.com/item?id=35144920)
        Yes, the only real difference between an  air conditioner and a heat pump is that air conditioning only works one way, whereas a heat pump has some valves and solenoids and whatnot that allow it to switch directions. ^c35144920

        It's kind of bonkers that we so frequently install air conditioners but not the tiny bit of extra parts to make it into a proper heat pump. I hope this will change in the near future.

- **pokot0** · [2023-03-14 11:03 UTC](https://news.ycombinator.com/item?id=35149651)
  I always wondered why the A/C units installed in the US do not make heat as well. In europe I have seen a push for this kind of units for at least 20 years now, to the point that I don't think anyone has bought anything else for the past 10. ^c35149651

  It seems your challenge is more about changing a status quo market then introducing a technology disruption that it's already been there for a long time now.

  - **lsaferite** · [2023-03-14 12:39 UTC](https://news.ycombinator.com/item?id=35150503)
    In the South-East US we've used Heat Pumps for at least 35-40+ years. Probably longer, I'm just lowering the number because I was a kid and don't know when they became the norm exactly. We don't have strong winters here so even the older heat pumps were fine with keeping houses warm. And we had/have resistive electric heating to supplement if the temp dropped too fast or too low. ^c35150503

    - **cmui** · [2023-03-15 02:11 UTC](https://news.ycombinator.com/item?id=35162820)
      You're right, heat pumps have been around for a while, but they're only at 15\% market share across the whole US. The Southeast, for a few different reasons, has the highest market share. (1) It doesn't get that cold, and magnitude of heating/cooling loads are close enough that single stage equipment provides an OK experience. (2) There's very little natural gas infrastructure. ^c35162820

      Cold weather heat pumps have recently become popular and enable increased adoption in the northeast, and the fact they're so efficient means they're competitive even in areas with a lot of natural gas infrastructure.

  - **STM32F030R8** · [2023-03-14 11:54 UTC](https://news.ycombinator.com/item?id=35150062)
    Heat pumps are very common in the US. That part isn’t really a challenge. ^c35150062

    - **malfist** · [2023-03-14 15:16 UTC](https://news.ycombinator.com/item?id=35152858)
      Heat pumps are super common, in the southern US I would be willing to bet you can't build a house without one, even geothermal is a heat pump. ^c35152858

      I don't get what this startup is offering. Heat pumps are common and readily accessible, I can walk into lowes and buy one today and they can arrange a contractor to do the install. It'll be a lot less expensive this this setup.

      If your business plan starts with "X is rare and hard to find" and X is actually extremely common, you're not going to be successful.

- **euph0ria** · [2023-03-13 17:05 UTC](https://news.ycombinator.com/item?id=35138723)
  I would only buy it if it has an API that I can access like NIBE does. It should have WiFI and also be able to run completely without internet connection. No functionality should be limited if internet is down except for functions that rely on external data such as live electricity prices etc. ^c35138723

  Also, it should be modular so it is easy to repair. Nibe sucks from this aspect and I would love a different heat pump that has better parts prices and was repairable.

  As a final must have: Silence. The NIBE is way too noisy and we have it placed next to a bedroom which causes a lot of frustration. When the compressor starts it travels through the walls. I'm currently building extra walls to isolate it and reduce the noise.

  - **konigschnell** · [2023-03-13 20:30 UTC](https://news.ycombinator.com/item?id=35142078)
    Professional installer for NIBE products here. Your experience doesn't align well with what I hear from my customers. Out of curiosity, what product do you have? ^c35142078

    - **euph0ria** · [2023-03-14 11:27 UTC](https://news.ycombinator.com/item?id=35149841)
      I have the F370. It has noise levels of about 60db when compressor is running. Exchanging the compressor costs \$3000 from quotes from installers in my city. ^c35149841

- **freeopinion** · [2023-03-14 03:05 UTC](https://news.ycombinator.com/item?id=35146871)
  I am clearly not your target audience. (Around here we measure AC/heat pumps in tons, not BTU and mount them outside the home.) But I'm willing to provide (fairly obvious) feedback. ^c35146871

  Price: yikes!
  Other: I stopped at price. Clearly you were expecting this because you hid the price underneath 10 pages of stuff I didn't read while I scrolled to find the price.

  Even people who would spend that kind of money are going to see a Juicero logo on your product. I may be wrong, but you will really need to elevate your sales pitch to survive long term. Do you have a \$2000 toy model that people can use for their garage or basement/attic apartment before they gamble bigger money?

- **IgorPartola** · [2023-03-14 03:56 UTC](https://news.ycombinator.com/item?id=35147256)
  I think you are going about this the wrong way. ^c35147256

  If you want to build a better experience with converting fossil fuel or electric resistance systems to heat pumps then you want to put together a network of installers and standardize on widely available equipment from existing manufacturers.

  If you want to design the next generation of heat pumps, then don’t sell directly to the consumer.

  Your price so far is pretty outrageous, a Mr Cool unit is an order of magnitude cheaper for the same BTU. No it won’t monitor CO2 and air quality, etc. But at the prices you are asking it’s a major investment into a startup and these systems require support more than technology.

  Lastly, your sales pitch is off. There are loads of heat pumps or there, from DIY installed units to multi ton full systems. If your main value proposition is the integration of air quality and humidity then explain why a whole house humidifier and a HEPA filter won’t be enough. Just explaining what a heat pump is isn’t going to cut it.

- **fintechjock** · [2023-03-13 16:59 UTC](https://news.ycombinator.com/item?id=35138620)
  Really cool and interesting. I definitely think the market is there for this. ^c35138620

  I'm betting that your biggest hurdle will be post-purchase. If I remember correctly, Tony Fadell talks about how hard it was to disrupt the contractor model when building Nest. People often just bought whatever thermostat their contractor recommended, and those contractors were incentivized to push them towards specific brands. They beat this by just making the product super easy to install by the consumer and cutting out the contractor all together (something I doubt is feasible with a heat pump).

  Maybe that won't be a problem with the DTC model considering the contractor is only brought in post-purchase, but I wonder if this really takes hold if competitors start trying to corner local installers. Good luck!

  - **foobarian** · [2023-03-13 17:23 UTC](https://news.ycombinator.com/item?id=35139048)
    \> They beat this by just making the product super easy to install by the consumer ^c35139048

    I think it was more than that, I cannot possibly overstate how stupidly better the design/UX was compared to alternatives.  In my home I spent years looking for a replacement for the ancient, round thermostat with a mercury switch.  That thermostat is a marvel: you spin the dial with instant visual feedback, and there is an off/heat/ac switch.  That's it!  The Nest just added networking.

- **AYBABTME** · [2023-03-13 17:06 UTC](https://news.ycombinator.com/item?id=35138747)
  My gas furnace sits next to my gas water heater. I want a central air heat pump that dumps the heat into my water heater when I'm cooling the house. ^c35138747

  - **cmui** · [2023-03-13 17:38 UTC](https://news.ycombinator.com/item?id=35139354)
    There are some combined space heating + water heating heat pump options out there. A few points to watch out for (1) install of an extra hydronic loop for the air handler can be expensive (2) your air handler + heatpump combination will not run as efficiently because of the losses associated with a secondary loop (3) there's a bit of a trick to getting the heat pump properly sized for cold weather + domestic hot water operation (4) if the demand temperatures for domestic hot water and space heating are far apart, the whole system will run at the lowest efficiency dictated by the highest demand temperature. ^c35139354

  - **js2** · [2023-03-13 17:24 UTC](https://news.ycombinator.com/item?id=35139084)
    In the meantime there are heat pump water heaters that can absorb the heat in your furnace room. ^c35139084

  - **jahewson** · [2023-03-13 17:33 UTC](https://news.ycombinator.com/item?id=35139258)
    We have a heat pump water heater, it pumps out cold air. In theory we could duct it into the house (at least in the summer) though it cools the garage for free, so that’s nice. ^c35139258

- **Brystephor** · [2023-03-13 22:04 UTC](https://news.ycombinator.com/item?id=35143628)
  I have family that works as HVAC techs for both residential and commercial. I also used to work at the shop but did other stuff primarily. ^c35143628

  Here's my question though: it states as a direct to consumer sales route. However the pricing includes installation. I don't know of any contractors that would be willing to do a customer supplied part installation for something like a heat pump. I also know that if they did do it, they would provide no warranties around it. So then from the consumers point of view, you've paid \$10k to have something installed and if it breaks, you're out of luck and it's time to pay up again.

  I'm interested in hearing more about this product and seeing how it works. Would love to chat more about it.

  - **cmui** · [2023-03-14 00:42 UTC](https://news.ycombinator.com/item?id=35145601)
    I understand the confusion around the install. The process for homeowners won't be fend for yourself and twist a contractor's arm to do an install, Electric Air will have local contractors that we connect you with. ^c35145601

    - **Brystephor** · [2023-03-14 01:43 UTC](https://news.ycombinator.com/item?id=35146207)
      What's the direct to consumer part then? ^c35146207

      The place I used to work had inventory on hand and so they could do your service now. Most people dont fix something that isn't broken. Meaning, if their existing system works, they won't replace it just because. So what this also means is that speed and time of delivery is very important. If your heat or cooling has broken and it's necessary, and you want to replace it, you're going to want to do it asap. So it needs to be on hand for contractors to have ready to go. Furnaces don't break in the summer when they're not being used.

      If you have contractor deals, you're going to have to provide some incentive for them to use these things. Because contractors are inclined to charge the most amount of money for the thing that's easiest for them to install.

      I am biased because I worked at a shop whose selling point was "we'll do it now when everyone else will book you two weeks out" and when you're talking about things like water, heat, and to an extent sewage, the value of time increases significantly.

- **danans** · [2023-03-14 00:09 UTC](https://news.ycombinator.com/item?id=35145243)
  It's great to see more heat pump options being developed, free from the assumptions of traditional manufacturers. ^c35145243

  Combining air quality and ventilation with the same appliance is great (most houses lack systems for either of those).   I don't see it addressed whether or not their fresh air systems will do heat-recovery.  This is also a big energy saver when fresh air is being introduced, and would eliminate the need for a separate HRV/ERV system.   So it's better to think of this as 3 systems in one:  Heating, Ventilation and A/C (hence HVAC).  Most houses have at best H and AC.

  It will be very interesting to see how their heat pump sizing tools work.   Right now, there is an epidemic of HVAC contractors installing massively over-sized heat pumps in a house by naively using the same rules of thumb they use for gas furnaces.

  This often results in short cycling, higher-than-necessary electricity use, and ultimately discomfort.  This is even worse when the heat pump air handlers and duct-work are installed in unconditioned spaces (common in temperate climates).  In places with high energy prices (i.e. California) this results in huge energy bills.

  The elephant in the room is of course the poor quality and leaky building envelopes that are commonplace across the country.  This equipment can't solve that problem.

  - **cmui** · [2023-03-14 00:19 UTC](https://news.ycombinator.com/item?id=35145356)
    Wholeheartedly agree with the comment about oversized heat pumps - this also has the side effect of lots of homes in the Northeast being told they can't use their duct work without a major upgrade, or an unnecessary electrical panel upgrade. ^c35145356

- **briHass** · [2023-03-13 19:13 UTC](https://news.ycombinator.com/item?id=35140915)
  Would've loved to see a different approach to the typical refrigerant-split units. I'm EPA certified, and do my own heat pump work, but something that could really blow up the heat pump space would be a closed-loop refrigerant system that uses water lines to the indoor coil/air handler. This would make the system a true DIY self-install, since you'd never be messing with refrigerant loops. ^c35140915

  The indoor coil/AH could be made as lightweight and small as possible (or multiple configurations) so it could easily be installed by a DIYer or a handyman for extremely low cost using insulated PEX lines for the water with basic tools. The outdoor unit would be heavy and require an electrical circuit, but would otherwise be as easy as swapping a window-unit AC.

  Just like with solar, the biggest problem with adoption of heat pumps is labor cost to install. The units themselves are shockingly cheap (and continuously getting cheaper), but labor adds 3-4X the cost of the unit itself. The certification, tools, and knowledge to handle the refrigerant is the 'secret sauce' used by HVAC companies to keep prices high. Imagine how few people would have window AC units or refrigerators if they needed to be installed by an HVAC company that wanted to make \$300/hr to install.

  - **danans** · [2023-03-13 22:04 UTC](https://news.ycombinator.com/item?id=35143625)
    \> something that could really blow up the heat pump space would be a closed-loop refrigerant system that uses water lines to the indoor coil/air handler. ^c35143625

    Add in hot water heating and storage, and that's basically what Harvest Thermal is doing:

    [https://www.harvest-thermal.com/product](<https://www.harvest-thermal.com/product>)

    They even use an off-the-shelf heat pump compressor (SanCO2) that as the name implies, uses CO2 as a refrigerant.   It's a pricey compressor though.

    - **briHass** · [2023-03-14 00:40 UTC](https://news.ycombinator.com/item?id=35145581)
      Thanks for the link; I hadn't heard of them before. I can absolutely see a system similar to this being the future. With an additional water loop, when running in 'AC/cooling mode', the waste heat could be captured for the domestic hot water tank as well. ^c35145581

      As with solar, energy/heat storage is likely to be an important component of the solution. Even without TOU rates, areas like mine (Mid-Atlantic) can hit temps at night that start to tax heat pumps (low teens F). However, the next day will often be above freezing and sunny. The HP could 'bank' available heat during the day to handle the late-night chill.

  - **cmui** · [2023-03-13 22:12 UTC](https://news.ycombinator.com/item?id=35143724)
    It's a different but valid approach. You still need a pump station and someone comfortable with hydronic loop install/fittings. Some areas also ban PEX. Northeast is definitely the place to do this, as there is way more hydronic knowledge than other parts of the US. System efficiency takes a hit because the secondary water loop adds more lift to the heat pump. ^c35143724

  - **earleybird** · [2023-03-13 19:40 UTC](https://news.ycombinator.com/item?id=35141299)
    Absolutely this. 3-4x?  Sibling of mine just had a minisplit installed where the unit was probably \$4-\$5k and the total was north of \$24k. ^c35141299

    A sealed water loop where any plumber and most DIYers could manage would be miles ahead in both reliability and accessibility.

    - **briHass** · [2023-03-13 19:53 UTC](https://news.ycombinator.com/item?id=35141504)
      Good point; I forgot to mention the reliability/environmental aspect as well. Most DIY, and even pro installs, of mini splits fail due to leaking flare connections, which must be made in the field. Modern refrigerants operate at very high (400+ PSI) pressures, and getting a perfect seal is critical. Having the entire refidgerant loop sealed and tested at the factory significantly decrease the common issues and prevents dumping climate-harmful gasses into the atmosphere. ^c35141504

      Even with more reliable brazed connections, modern heat pumps are very sensitive to contamination of the refrigerant lines. Brazing must be done with utmost care not to overheat the copper, and nitrogen gas needs to flow through the pipe at specific volumes to prevent carbon deposits that can decrease the longevity of the system. Any damage caused by improper brazing is largely invisible (inside the pipe) and the process is time consuming and precise; in exact opposition to the incentives an HVAC installer to get it done quickly.

      - **cmui** · [2023-03-13 22:13 UTC](https://news.ycombinator.com/item?id=35143755)
        Though somewhat controversial, ZoomLock also seems promising. Agreed though, there are obvious benefits to having a fully factory sealed refrigerant loop. ^c35143755

        - **briHass** · [2023-03-14 00:28 UTC](https://news.ycombinator.com/item?id=35145448)
          I'll wait for more reliability data on ZoomLock, but it could easily prove to be the optimal solution. Unfortunately, it doesn't help the DIYer, because the crimping tools are outrageously expensive, and clearly aimed at a pro doing enough installs to make the time-savings worth it. ^c35145448

      - **simplyaccont** · [2023-03-13 20:15 UTC](https://news.ycombinator.com/item?id=35141841)
        there are diy systems with threaded connectors, pre-vacuumed units and linesets filled with refrigerants. ^c35141841

        - **briHass** · [2023-03-14 00:20 UTC](https://news.ycombinator.com/item?id=35145362)
          True, but those linesets introduce other downsides. They can't be cut to length, so you often have to have unsightly loops of extra line set somewhere, and the loops can potentially trap the oils that mix with the refrigerant to lubricate the compressor. They're also much more expensive, and anecdotally, I've heard of leaks from over/under tightening the threaded connections. ^c35145362

          Not to mention, installing them without an EPA 608 certification is technically illegal. MrCool and others that use them are relying on the EPA being understaffed and unlikely to pursue homeowners, but their stance on it is perfectly clear:

          "Is technician certification required to install an R-410A mini-split?

          Yes. Adding or removing refrigerant from a mini-split as part of installation, and/or connecting or disconnecting hoses or pre-charged lines requires a section 608 technician certification. Activities reasonably expected to violate the integrity of the refrigerant circuit include but are not limited to: Attaching or detaching hoses and gauges to and from the appliance; adding or removing refrigerant; adding or removing components; and cutting the refrigerant line."

          [https://www.epa.gov/section608/epas-refrigerant-management-p...](<https://www.epa.gov/section608/epas-refrigerant-management-program-questions-and-answers-section-608-certified>)

          - **simplyaccont** · [2023-03-14 02:14 UTC](https://news.ycombinator.com/item?id=35146460)
            \>True, but those linesets introduce other downsides. They can't be cut to length, so you often have to have unsightly loops of extra line set somewhere, and the loops can potentially trap the oils that mix with the refrigerant to lubricate the compressor. ^c35146460

            well, i run my through crawlspace. had only a small extra loop. in crawlspace.

            \>They're also much more expensive,

            per unit - yes. but... if you doing to diy mini-split not with precharged lineste, you need vacuum, refrigerant and probably license to buy it. it raises cost and make it viable if you plant to install multiple units (have coworkers that did it).
            if you want to get it professionally install, than in addition to \~\$1.4k for 2ton unit you look into \$6k-\$8k for labor. Those were prices year ago for install in garage with 240v line connected to 40amp breaker available at install location.

            \>Not to mention, installing them without an EPA 608 certification is technically illegal.

            technically, i guess much of the work done by home owners must be done by certified professionals and get approvals and inspections.

  - **gandalfian** · [2023-03-14 00:56 UTC](https://news.ycombinator.com/item?id=35145769)
    *a closed-loop refrigerant system that uses water lines to the indoor coil/air handler* ^c35145769

    Sounds like an air to water monoblock heat pump. Common in Europe. But you can only get the water up to about 50C efficiently. Not as good as refrigerant. So you need a large radiator to get the heat out into the room. Using wet underfloor heating as a giant emmitter works well. But otherwise it makes them tricky.

    Some people are trying for minisplits with propane in the lines which is not a greenhouse gas so they hope anyone will be able to install it without a licence.

- **jhallenworld** · [2023-03-13 19:12 UTC](https://news.ycombinator.com/item?id=35140896)
  I had a recent experience with replacing the main blower motor on my American Standard gas furnace: the variable speed motor has firmware, so can you guess what they did? The motor has to be programmed by the distributor or it will not work in your furnace.  You have to provide the furnace's serial number for the programming.  Worse, the local distributor would not sell it to me!  They will only sell it to an installer.  "Qualification" for an installer is load of nonsense- they just want your EPA refrigerant certification- which is nothing compared to a real license, like plumbers or electricians. ^c35140896

  So please:

  No serialized parts.

  I should be able to buy replacement parts from you or common online suppliers without hassle- like amazon.com or supplyhouse.com.

  I should be able to install it myself, at least in theory: so unit comes pre-charged, and various lengths of linesets are available so I don't have to do any brazing.

  There is a company making a window unit heat pump: this one [https://www.gradientcomfort.com/](<https://www.gradientcomfort.com/>)

  You should make something like this..  basically a zero-installation work version of your product.  This will be a big hit in places with insane labor costs- like New York City.

  - **cmui** · [2023-03-13 19:51 UTC](https://news.ycombinator.com/item?id=35141472)
    Gradient is a great product, uses 120V, great for small spaces, like apartments in NYC. [https://www.protocol.com/climate/gradient-nycha-heat-pumps-q...](<https://www.protocol.com/climate/gradient-nycha-heat-pumps-queens>). Electric Air is really targeted at replacing natural gas furnaces in single family homes. ^c35141472

- **aloukissas** · [2023-03-13 21:26 UTC](https://news.ycombinator.com/item?id=35142997)
  This is great to see. I have a question around the "a delightfully uniform temperature in each room". I live in a 3-story townhome, which has largely non-uniform temperature across floors (since warm air travels up). So, cold lower floors in the winter and hot upper floors in the summer. AFAICT, this is pretty common with central duct systems and the usual fix is to switch to split-unit systems. How does your product handle this? ^c35142997

  - **cmui** · [2023-03-13 22:04 UTC](https://news.ycombinator.com/item?id=35143634)
    Good question. The uniform temp is really within a room, what you're describing is the not uncommon experience of having unbalanced duct work. A few options for you (1) DIY or pro duct balancing. You change the position of dampers and vents, might have to modify duct work (2) actuated zone dampers, these live in the duct work and install is expensive (3) a smart vent that you can DIY, battery life is surprisingly good [https://flair.co/](<https://flair.co/>) (4) mini-split system, every major room gets a wall unit connected to an outdoor unit (condenser), and you can control the temperature of each room the mini-split is in. Electric Air offers wall units for this if you're not able to make a ducted install work. (5) hybrid setup, you use a centrally ducted furnace for most of the house, heat pump or otherwise, and use a mini-split in the upstairs rooms that are not reaching the desired temperature. ^c35143634

    - **aloukissas** · [2023-03-13 22:42 UTC](https://news.ycombinator.com/item?id=35144155)
      Thanks for the pointers! Coming from Europe, I really love ductless split systems, so that's probably my preference. ^c35144155

- **izolate** · [2023-03-13 17:53 UTC](https://news.ycombinator.com/item?id=35139627)
  I live in Buffalo NY, and from the recent record-breaking snowstorms, I've concluded that the push for electrification of home appliances may not be the best solution. Although gas furnaces still require electricity, they can operate for a more extended period on a generator, and gas stoves are a crucial backup option for staying warm during a power outage. Until our electricity grid becomes more reliable, I would hesitate to switch to an all-electric setup. ^c35139627

  While I think your product looks excellent and applaud your launch, I regret that it's not something I'd purchase anytime soon, given my concerns about relying solely on electricity during power outages.

  - **nemo44x** · [2023-03-13 19:05 UTC](https://news.ycombinator.com/item?id=35140797)
    Also so many of our electric lines are above ground. I wouldn't feel comfortable 100\% relying on that. Snow and ice take these things out in the winter and summer storms have their way too. And then the unreliable grid. How many brownouts have been occurring in part of the USA over the last few years? ^c35140797

    I actually have a heatpump but I also have 2 furnaces/ACs as well for 3 systems total for my home. I don't plan on moving to electric for stovetop anytime soon.

  - **hunter2\_** · [2023-03-13 19:49 UTC](https://news.ycombinator.com/item?id=35141436)
    \> gas stoves are a crucial backup option for staying warm during a power outage ^c35141436

    Isn't CO (and other combustion byproducts) an issue? When cooking a meal the duration is short enough to not matter much, but at extended durations to provide heat I would think this is a bad idea, unless you monitor air quality enough to run a vented range hood at the optimization point between unhealthy and wasting most of the heat you're generating.

    - **izolate** · [2023-03-13 21:12 UTC](https://news.ycombinator.com/item?id=35142758)
      I agree that these byproducts can be an issue. However, in the context of a life-threatening situation like a power blackout in a blizzard, where the alternative is death from exposure to the cold, running a gas stove for a long duration may be an acceptable risk. ^c35142758

- **gumptionary** · [2023-03-13 17:28 UTC](https://news.ycombinator.com/item?id=35139155)
  Love what you're trying to do. I recently moved most of the way off oil-based hydronic baseboard heating in my 1800's New England farmhouse through installing 3 ductless mini-splits with Mitsubishi Hyper Heat condensors. Just to help with your user research, my biggest decision points: ^c35139155

  1\. Cold weather operation. I get you're saying the units are good down to -15f, but there's nothing like the fact that I can talk to plenty of other people who have good experiences with Hyperheat at -15f to ensure that they'll actually work. Given I'm using these primarily for heat (the AC is a bonus), if they didn't heat well and efficiently at 0f then it was all pointless. 
  2\. Repairability. Again, given I'm trying to use these as my primary heat, I need to know I'll have someone who will service the unit who can be here in a matter of hours. This is why I went away from the DIY route. Most installers around here (semi-rural New England) are super brand aligned and won't service the stuff they don't install.

  Would be happy to help with user research if you're looking for folks to talk to.

  - **harterrt** · [2023-03-13 17:38 UTC](https://news.ycombinator.com/item?id=35139341)
    \+1 to servicability. It's hard to get someone who knows how to clean my minisplits. This looks really cool, but I'd need to be confident that I could maintain my units myself. ^c35139341

  - **sokoloff** · [2023-03-13 23:39 UTC](https://news.ycombinator.com/item?id=35144904)
    \> if they didn't heat well and efficiently at 0f then it was all pointless. ^c35144904

    As long as they heat well (capacity-wise) at those temps, I wouldn't really care if the CoP was 1.5-ish (which it likely will be). You'll still get plenty of 3.5-5.0 CoP time in the (much, much longer) shoulder seasons that getting 3-5 days of sub-2.0 isn't that big of a deal \[again, provided the capacity is there\].

  - **cmui** · [2023-03-13 17:34 UTC](https://news.ycombinator.com/item?id=35139268)
    Thanks for the feedback! I'll send you a note. ^c35139268

- **hectormalot** · [2023-03-13 18:54 UTC](https://news.ycombinator.com/item?id=35140623)
  This is a really important consumer problem to solve. We retrofitted a heatpump into our home about a 18 months ago and it wasn’t a great experience. Ranging from contractors not even replying (retrofit being harder than new homes), wildly different quotes and setups, lack of (API) integration, uncharitable on planning and timelines, Etc. Note: This was before the energy prices spike because of the Russian invasion into Ukraine, it’s gotten worse since then. ^c35140623

  We’ve seen two similar start-ups (direct to consumer heat pumps) in the Dutch market. Might be interesting to have a look:

  \- [https://www.quatt.io/](<https://www.quatt.io/>) (4 or 8kW at \$5500- and \$6500. After which you get about \$3000 subsidy.)

  \- [https://www.dewarmte.nl/product-pompao](<https://www.dewarmte.nl/product-pompao>) (2-8kW modulating at \$6500, or \$3500 with the subsidy)

  Both marketed as hybrid pumps because they don’t provide hot tap water and that’s typically still done with gas. Electric boilers being uncommon here.

  - **cmui** · [2023-03-13 19:12 UTC](https://news.ycombinator.com/item?id=35140900)
    Thanks for the feedback! I'll take a look at those two products. ^c35140900

- **londons\_explore** · [2023-03-13 17:21 UTC](https://news.ycombinator.com/item?id=35139017)
  I'd like a furnace company that has a financial incentive to keep my house warm and efficient. ^c35139017

  Todays furnace/heat pump makers test their kit in a lab under perfect conditions, and then when it is installed it often costs double or more to run compared to what the datasheet says.\[1\]

  I would like the company to say "we will keep your house at 70F, year round, for \$3000/yr.   We will pay any electric/gas use to achieve that, and pay for and install maintain and upgrade the hardware".

  Then, the company has a direct incentive to keep costs down.  The company can optimize maintenance schedules, energy contracts, algorithms to control fans and pumps, etc.    Doing this, they should be able to keep total costs lower for the homeowner (who isn't an expert on any of those things)

  \[1\]: [https://www.sciencedirect.com/science/article/pii/S136403212...](<https://www.sciencedirect.com/science/article/pii/S1364032120305621>)

  - **potatolicious** · [2023-03-13 17:38 UTC](https://news.ycombinator.com/item?id=35139352)
    \> *"and pay for and install maintain and upgrade the hardware"* ^c35139352

    The problem is that the cost of running the kit has much less to do with the actual HVAC equipment itself and has to do with your house - which no sane HVAC company wants to make guarantees on.

    \- What kind of insulation is in the walls? What's the R-value? The vast majority of home owners do not know this, and *many* homes have old and deeply substandard insulation.

    \- What kind of windows do you have? Expecting an HVAC company to guarantee the thermal properties of your windows seems unrealistic.

    \- *How many* windows do you have? Do you keep them open a lot? How many doors? Are the doors well-sealed?

    \- What is the attic situation? What's the insulation in the attic like?

    The list goes on. I can *potentially* see a company willing to entertain such a guarantee for a brand new home that they knew the specs of, but for an existing home it feels totally unrealistic.

    - **londons\_explore** · [2023-03-13 17:41 UTC](https://news.ycombinator.com/item?id=35139412)
      They could make an estimate based on the age and size of the house.  Build in a profit margin. ^c35139412

      - **potatolicious** · [2023-03-13 18:53 UTC](https://news.ycombinator.com/item?id=35140597)
        Sure, the profit margin would have to be wide enough to account for a lot of variance. ^c35140597

        Seriously, the insulation effects on your heating bills cannot be underestimated. Two houses that look superficially the same on the curb can have a margin of error that is a *multiple* of your heating bill, and that largely comes down to what the insulation is in the house.

        Like we're not talking about "variances up to 30\%" territory, we're talking "variances up to 300\%" territory. No one is willing to make that guarantee without pulling off your drywall and examining the state of your insulation, not to mention the various behavioral issues others have brought up that vastly alter your bills.

      - **eldaisfish** · [2023-03-13 17:49 UTC](https://news.ycombinator.com/item?id=35139553)
        This is wishful thinking. the ability of a structure to retain heat depends on SO MANY factors that guaranteeing a temperature is a fool’s errand. ^c35139553

        - **zamnos** · [2023-03-13 17:55 UTC](https://news.ycombinator.com/item?id=35139660)
          An *estimate*, not a guarantee, and just bring in a FLIR/thermal camera to see where the heats getting lost and how much. They're cheap enough for professional use these days. ^c35139660

  - **lotsofpulp** · [2023-03-13 17:32 UTC](https://news.ycombinator.com/item?id=35139233)
    Would the company also have control of the doors and windows, or at least perfect knowledge of how long they are open?  And number of bodies in the house, or amount of cooking being done? ^c35139233

    - **londons\_explore** · [2023-03-13 17:37 UTC](https://news.ycombinator.com/item?id=35139325)
      No, just like a taxi doesn't charge extra if you're too fat, even though it costs him more in fuel. ^c35139325

      Obviously they can send reminders to keep the doors closed...   Or have sensors on the windows and have it not heat when a window is open...

      Or they could just not renew the service for customers who leave the window open all year.

  - **dolmen** · [2023-03-13 17:43 UTC](https://news.ycombinator.com/item?id=35139431)
    \+1 ^c35139431

    THAT would be disruptive to the market.

- **dolmen** · [2023-03-13 17:30 UTC](https://news.ycombinator.com/item?id=35139182)
  I bought a house with two air heat pumps. I live in France. ^c35139182

  One day it stopped working. I tried to find a contractor to repair it. It was hard. Too long to wait in the winter. I immediately bought electric heaters to replace the heat pump as wiring was already in place (the heat pumps were already v2 of the house heating).

  I finally got one contractor to come for the heat pump. It happened that he came to my home the only day the last 3 years that temperature was below -5 °C. The issue was apparently a gas leak, but because of the low temperature he couldn't do anything. Despites my calls, he never came back. And I haven't been able to get someone else to fix the thing. The only other contractor I found was only asking 250 EUR to decommission the thing.

  So I still have a non working air heat pump in my living room.

- **abakker** · [2023-03-13 17:06 UTC](https://news.ycombinator.com/item?id=35138739)
  If you ever want to chat with a technical homeowner, who is mid-process in reevaluating HVAC retrofit in a house that would be a great candidate for this, contact me at the email account in my profile. I'd love to talk about this. ^c35138739

  I've installed a few mini splits, understand load calcs (basically) and have plenty of experience with ducting systems and electrical and control systems.

- **codingdave** · [2023-03-13 18:46 UTC](https://news.ycombinator.com/item?id=35140472)
  I'm all for this effort, but this is not yet a compelling story. I've never had a problem getting a heat pump installed in prior homes. So if the market value is avoiding pain in hiring contractors... I simply have not felt that pain. Asking me to pre-order something that already exists when you have no physical prototypes feels like you are jumping the gun. ^c35140472

  I do hope you succeed - I love heat pumps and want more of them to exist in this world. But not having a prototype yet and asking people what their ideas and experiences are feels like you are just starting market research, not that you are in a place to be taking orders.

  - **cmui** · [2023-03-13 19:24 UTC](https://news.ycombinator.com/item?id=35141085)
    What regions have you done those heat pump installs in? There's a lot of regional variability. Thanks for the feedback! ^c35141085

    - **eep\_social** · [2023-03-14 01:32 UTC](https://news.ycombinator.com/item?id=35146109)
      \+1 to gp ^c35146109

      Reading the original post, I knew immediately that you were not familiar with what’s going on in the southwest, or Arizona at least. We’ve been doing heat pumps for a long time out here. Most people talk about them like they’re AC but as far as I am aware they’re all heat pumps because it does get chilly overnight in deserts in the winter.

    - **codingdave** · [2023-03-13 19:34 UTC](https://news.ycombinator.com/item?id=35141205)
      My experiences were in the Southwestern USA. ^c35141205

- **rcme** · [2023-03-13 17:00 UTC](https://news.ycombinator.com/item?id=35138638)
  Those are beautiful looking units. It's a cool idea to focus on giving something very pedestrian and utilitarian a nice cosmetic overhaul. ^c35138638

  I just replaced radiators with a heat pump install. I had a few questions about your units: What are "backup heating strips?" They're mentioned in passing when talking about cold weather, but I imagine there is some meat here. Also, even though many heat pumps work in cold weather, their efficiency drops. Where is the break even point? Also, what is the sound level of the condenser unit? It looks like you only list sound levels for the air handler.

  - **signaturefish** · [2023-03-13 17:07 UTC](https://news.ycombinator.com/item?id=35138752)
    In the context of heat pumps, a "backup heating strip" is a resistive heating element - electricity goes in, heat comes out just like an old electric heater. They're generally used during defrost cycles for the external air handler in cold weather, or to provide a temporary thermal boost when the heat pump is having performance trouble e.g. when the exterior temperature is near the bottom of the heat pump's operating range. ^c35138752

    More detail at [https://carolinacomfortsc.com/hvac/what-are-heat-strips/](<https://carolinacomfortsc.com/hvac/what-are-heat-strips/>) (no affiliation, they were the first authoritative return from my web search).

    - **rcme** · [2023-03-13 17:13 UTC](https://news.ycombinator.com/item?id=35138871)
      Whole-house heating with resistive electric heating is going to get expensive, quickly. If they're serious about installing these in cold weather climates, they should have more information about the cut over temperature and the efficiency of the heat pumps at those temperatures. ^c35138871

      Just for context, my heat pumps cut over around 40-45 degrees to gas-based heat.

      - **tgtweak** · [2023-03-13 21:17 UTC](https://news.ycombinator.com/item?id=35142822)
        High efficiency heat pumps with built-in defrosters (or "heating strips") can often provide full heating capacity (ie: 48,000btu for a 4 ton unit) down to -12f, with reduced output at even lower temps.  The COP efficiency drops quite a bit though and it will eventually get to a point where it is essentially as energy efficient as a resistive heater.  Whether it's more efficient than using gas or not is a difficult calculation based on your gas price, heat pump COP temperature curve and electricity price.  If you expect to see \<-20f temperatures regularly, you'll want/need a backup heat source anyway. ^c35142822

      - **signaturefish** · [2023-03-13 18:13 UTC](https://news.ycombinator.com/item?id=35139951)
        Yeah, I'd like to see those figures too, and I think they might surprise you (and me). I don't have figures or references to hand here, but as I understand it modern heat pumps should be good down at least a little way below freezing.  They're widely used and popular in Norway, for example, and the Norwegians aren't exactly new to cold weather. ^c35139951

      - **heatpumpfan** · [2023-03-13 17:44 UTC](https://news.ycombinator.com/item?id=35139455)
        You have an older system. New systems can provide 100\% rated capacity well below freezing. Mine is -5F and not specifically a "cold climate" unit. The unit in OP seems to offer 100\% nameplate capacity at 5F. ^c35139455

        - **rcme** · [2023-03-13 19:15 UTC](https://news.ycombinator.com/item?id=35140940)
          These are brand new heat pumps. I don’t think it’s possible to have high efficiency at cold temps because of the need for a defrost cycle. I just check and mine are around 2 COP at 8F and 5 COP at 40F. ^c35140940

          - **heatpumpfan** · [2023-03-14 02:35 UTC](https://news.ycombinator.com/item?id=35146648)
            It is not clear why your heat pump cuts over at 40 degrees if it still has COP of 2 at 8 degrees. Presumably a cost-effectiveness calculation if gas is cheap in your area. If you had heat strips instead of gas, the "cut over" temperature would be much lower. If your unit is capable of operating at full capacity below 8F, it would likely only use resistive heating below 5F. For most climate zones, that is fine and your unit does not sound like one specifically deemed a "cold climate" heat pump, the which now regularly achieve full rated output down to -15F. Of course, it's only rarely that cold even in "cold climate" zones so operating down at a COP of 1 for these short durations is not a real problem. The impetus for systems designed for lower temperature operation is not really aimed at those with cheap gas but at those living where heat pumps were previously only feasible for heating if using much more expensive ground source systems. Achieving year-round heat with only the heat pump eliminates the need for a furnace so you have to include this missing gear and installation cost in your analysis. ^c35146648

  - **heatpumpfan** · [2023-03-13 17:06 UTC](https://news.ycombinator.com/item?id=35138737)
    \>"backup heating strips" ^c35138737

    Big resistive elements sitting in the air handler. Think big toaster oven coils that are used when the outdoor temperature drops too low for the heat pump to handle the load.

  - **NickM** · [2023-03-13 17:43 UTC](https://news.ycombinator.com/item?id=35139427)
    How did you replace your radiators? Did you have to install ducts, or did you find a cost-effective way to have a heat pump heat the water for your radiator system? ^c35139427

    Good ways to upgrade homes that use radiators to use heat pump heating seems like a big gap in the market right now (though, not sure if this is just a market problem or a gap in the technology, since my understanding is that radiators need higher temperatures than forced air systems).

    - **rcme** · [2023-03-13 20:01 UTC](https://news.ycombinator.com/item?id=35141659)
      I installed ducts. For me, personally, I think it was worth it. I live in an old home, but someone 50 years ago replaced all of the radiators with baseboard radiators (why???). So ducts over baseboard radiators is a huge upgrade. ^c35141659

- **amluto** · [2023-03-13 19:39 UTC](https://news.ycombinator.com/item?id=35141281)
  Some questions: ^c35141281

  What is the HEPA for?  Is it on the fresh air intake or are you actually HEPA-filtering the recirculated air?  If the latter, why not MERV 16?  HEPA media is probably more expensive, and it definitely has much higher pressure loss, and there is no actual need for it outside of healthcare.

  How are you humidifying?

  Can you control the coil temperature in cooling mode and thus control the sensible/latent cooling ratio?  (i.e. can the amount of *de*humidification be adjusted on the fly as needed?)

  Can you integrate with some kind of HRV or ERV?

  - **cmui** · [2023-03-13 20:29 UTC](https://news.ycombinator.com/item?id=35142052)
    Good questions. ^c35142052

    We have a way of running HEPA with not unreasonable pressure loss,  and then dialing back the amount of filtration when PM2.5 levels are reasonable. Separately a homeowner can request a high filtration mode.

    Humidifying is though a system similar to a whole home humidifier - a small bypass from the supply side of the furnace evaporates water off a media.

    Yes, through a combination of reheat and coil temperature control we can change the sensible/latent cooling ratio.

    HRV/ERV only makes sense in certain applications. We're looking at making one integral in the system, but it will come down to minimizing total cost for homeowners. Comfort metrics will be unaffected.

    - **amluto** · [2023-03-13 21:03 UTC](https://news.ycombinator.com/item?id=35142589)
      Do you have a diagram of the system (with water connections, duct connections, fresh air connections, exhaust, etc)? ^c35142589

  - **Beached** · [2023-03-13 19:48 UTC](https://news.ycombinator.com/item?id=35141411)
    I would like a standard air filter to be used. a lot of individuals don't require HEPA, but I do. I would like to be able to source my own filters from anywhere, and put them in. just like my current furnace. let people pick their level of air filtration they are comfortable with ^c35141411

    - **amluto** · [2023-03-13 20:01 UTC](https://news.ycombinator.com/item?id=35141654)
      How standard?  The hardware store products are fundamentally pretty poor because they’re at most 2” deep.  But Aprilaire, Lennox and some others have nice 4” filters at reasonable prices. ^c35141654

      - **tguvot** · [2023-03-13 22:51 UTC](https://news.ycombinator.com/item?id=35144269)
        4" is standard. plenty on amazon and other places.  hardware stores don't usually carry it because people probably don't understand that 4" is better from one side, and from the other not all filter boxes/supplies can accommodate \> 1" ^c35144269

- **zainhoda** · [2023-03-13 17:09 UTC](https://news.ycombinator.com/item?id=35138804)
  I installed a Mr. Cool DIY mini split in my home for 2 rooms and so far it’s been great. That initial foray was a bit of an experiment. I’d like to just replace my central air now with a ducted heat pump but I haven’t found a good solution that doesn’t cost a ridiculous amount for a professional to install. ^c35138804

  I think you have a big problem with selling direct to homeowners. Most HVAC companies will not touch a homeowner-purchased system. So if you’re selling direct, then you’re going to need DIY quick connect line sets like Mr. Cool.

  - **hi\_hello** · [2023-03-13 19:27 UTC](https://news.ycombinator.com/item?id=35141125)
    Your point on HVAC companies not servicing homeowner-purchased systems is worth underlining. ^c35141125

    In our case, we need some duct work to fit a 2-ton Mr. Cool system to our existing ducts. Every licensed HVAC contractor/company we've contacted has refused to touch any part of consumer purchased system, citing liability issues (context: Bay Area, CA).

    - **simplyaccont** · [2023-03-13 20:16 UTC](https://news.ycombinator.com/item?id=35141861)
      i am thinking to replace one of the hvacs with ducted mr.cool. just curious, what was the needed duct work ? ^c35141861

  - **tguvot** · [2023-03-13 17:20 UTC](https://news.ycombinator.com/item?id=35138990)
    same mrcool has ducted diy heatpumps ^c35138990

    - **heatpumpfan** · [2023-03-13 17:22 UTC](https://news.ycombinator.com/item?id=35139030)
      [flagged] ^c35139030

      \[dead\]

- **borland** · [2023-03-14 10:12 UTC](https://news.ycombinator.com/item?id=35149361)
  Speaking here from New Zealand, where central heating/thermostats are basically unheard of, outside of offices and schools. Heatpumps are *very* common in homes, usually high-wall mounted ones like this: ^c35149361

  [https://www.mitsubishi-electric.co.nz/heatpump/i/69337B/stan...](<https://www.mitsubishi-electric.co.nz/heatpump/i/69337B/standard-gs-60-high-wall-heat-pump>)

  We have the approx 12 year old variant of the above heatpump in our current house, and in our previous house paid to install a similar thing.

  The hardware cost for one of those is \$2900 NZD, plus another few for install, leading to a total cost of around \$5000-6000 NZD (\$3000 - \$3700) USD approx. While that is still a fair chunk of change, it's less than a quarter of the cost of the \$14,000 USD that Electric Air is launching with.

  It's not ideal, you end up with a single climate controlled part of your house, and the rest relies on leaving the doors open. The fully ducted electric air system (which I assume lets you heat/cool individual rooms) would certainly be a lot nicer, but the *massive* price differential means that only the really super rich elite level houses would ever install one. The other 99\% of the market is happy with the "good enough" solution of a wall-mounted heatpump.

  One other thing - Water drainage from a heatpump in cooling mode is a common problem. Installers need to run pipes out through walls to drain away condensed water, and while they ideally can use gravity, sometimes install location means a water pump is required. We have one of those; some years ago the pump failed leading to a lot of soaked carpet in our living room. Hopefully electric air has a good reliable solution there!

  Finally: When installing heatpumps, this requires the indoor unit (source of cold/hot air) to be connected via heatpipe to the outdoor unit. This almost always involves drilling holes through interior and exterior walls (often brick). Because of the potential for things to go wrong, I'd never recommend a DIY / home contractor to install such a thing. You want a reputable company that warranties their work, has something at stake, and that you can have recourse against, if they screw it up.

  Good luck!

  - **borland** · [2023-03-14 10:16 UTC](https://news.ycombinator.com/item?id=35149379)
    Oh BTW, a small bit more feedback ^c35149379

    \> Better air quality is achieved through a thermostat with PM2.5 and CO2 sensors, as well as an air quality module on the air handler that controls HEPA filtration, fresh air intake and modification of the home’s humidity

    This is very nice, but in the grand scheme of things nobody cares about these. They just want a warm house in winter and a cool one in summer.
    If air quality/filtering were a free/cheap addon that'd be great, but not if it means the unit costs significantly more.

    OTOH, that gives you a very nice market segmentation mechanic. Provide a lower-cost unit without things like CO2 sensors and HEPA filters, and charge a fat margin to upgrade to the fancy one for those richer people who have the luxury of such things.

- **rkagerer** · [2023-03-14 09:50 UTC](https://news.ycombinator.com/item?id=35149214)
  "*While we don't have any physical prototypes at the moment... working on building traction via preorders... start building hardware once fundraising is complete*" ^c35149214

  Sorry mate, I stopped reading at this point.

  It sounds like you might be trying to tackle too much at once.  Unless you have very deep pockets (which I'm guessing isn't the case since you haven't secured funding yet) you might be better served finding a route that gets you there via smaller steps with discrete wins along the way.  If there are companies out there as you've described who are good at one piece, consider starting with a product that works well with the portion of the puzzle they already solved - perhaps with an eye to eventual acquisition (them of you, or possibly you of them once you've built up a reputation for execution and growth in this space that will attract sufficient capital).

  It's along the same lines of reason aircraft companies don't generally build a new engine and airframe at the same time. Even Apple started off with a simple music player before they grew a whole iOS ecosystem.

  It sounds like you have a clear vision and your past experience will serve you well.  I'd really love to see innovation in this space and wish you luck.

  One other gut feeling from reading this that I have to share, which may be painful for you to hear... the timing of your post and its similarities to a Kickstarter come across like this is really more of a pitch to drum up attention and VC funding.

- **jkravitz61** · [2023-03-14 06:13 UTC](https://news.ycombinator.com/item?id=35147977)
  Seems like a lot is being promised here for a 7 month old startup with one employee- SW, multiple different HW components, high end thermal mechanics delivering all of this by EOY 2024. Best of luck, I am legitimately rooting for this to be a winner (I love the concept of design meets efficient heat pumps and believe there is a substantial market here)... but how can outsiders trust to give you their money for a deposit when it's clear there is very high risk that this ever reaches market? ^c35147977

  - **cmui** · [2023-03-14 06:40 UTC](https://news.ycombinator.com/item?id=35148114)
    You're right - hardware is tough, and the scope is large. But this is an important area to build better products, there are a lot of people passionate about this/want to work on this and the hardware doesn't have to be designed from scratch. As for trust, the deposit is pretty low stakes, \$100, fully refundable, reserves your place in line for a system. For those of you that placed a deposit, thank you, it means a lot! ^c35148114

- **neilalexander** · [2023-03-13 16:52 UTC](https://news.ycombinator.com/item?id=35138479)
  This is interesting but many systems like it fall at the first hurdle in countries like Britain where forced air is not the norm. How are products like this supposed to work in a house that is currently optimised for radiators and combi-boilers and with no existing air ducts? ^c35138479

  - **cmui** · [2023-03-13 16:55 UTC](https://news.ycombinator.com/item?id=35138528)
    That's a great point. Our initial market will be North America where this makes the most sense. For people with radiators, you could also do an install with our wall unit. If you have a radiator + boiler system there are also a lot of air-to-water heat pump options for you today. It's an area worth exploring for future Electric Air products. ^c35138528

  - **Vvector** · [2023-03-13 16:56 UTC](https://news.ycombinator.com/item?id=35138541)
    It's not designed to work in those houses.  It's specifically designed for homes with ducts. ^c35138541

    "The most common heating system in the US is a natural gas furnace connected to ductwork, with the hot air ultimately coming out of vents in each room. This heat pump is a great replacement for the furnace and air conditioner in these ducted systems."

  - **shagie** · [2023-03-13 16:57 UTC](https://news.ycombinator.com/item?id=35138571)
    You can either move the air (via ductwork) or the coolant with a small insulated pipe. ^c35138571

    The question is where do you have the exchange.  The central / forced air tends to be a furnace in the basement.  But its also viable to have a ductless mini-split heat pump ( [https://www.energy.gov/energysaver/ductless-mini-split-heat-...](<https://www.energy.gov/energysaver/ductless-mini-split-heat-pumps>) ) that just moves the heat carrying fluid to a room and then have that room with an exchange.

    \> Ductless, mini-split-system heat pumps (mini-splits) make good retrofit add-ons to houses with "non-ducted" heating systems, such as hydronic (hot water heat), radiant panels, and space heaters (wood, kerosene, propane). They can also be a good choice for room additions where extending or installing distribution ductwork is not feasible, and for very efficient new homes that require only a small space conditioning system. Be sure to choose an ENERGY STAR® compliant unit and hire an installer familiar with the product and its installation.

    \> Like standard air-source heat pumps, mini-splits have two main components -- an outdoor compressor/condenser and an indoor air-handling unit. A conduit, which houses the power cable, refrigerant tubing, suction tubing, and a condensate drain, links the outdoor and indoor units.

    \> The main advantages of mini-splits are their small size and flexibility for zoning or heating and cooling individual rooms. Many models can have as many as four indoor air-handling units (for four zones or rooms) connected to one outdoor unit. The number depends on how much heating or cooling is required for the building or each zone. This can be affected by how well the building is insulated and air sealed). Each of the zones has its own thermostat, so you only need to condition occupied spaces, which can save energy and money.

  - **iknowstuff** · [2023-03-13 17:01 UTC](https://news.ycombinator.com/item?id=35138644)
    Yeah you would either get an air-to-water heat pump, or better yet a minisplit system where a single condenser has multiple runs of small tubes carrying refrigerant to heat exchangers in different rooms. ^c35138644

  - **masterj** · [2023-03-13 17:01 UTC](https://news.ycombinator.com/item?id=35138642)
    They're not. Instead you can use air-to-water heat pumps to swap out those systems. ^c35138642

  - **bodhi\_mind** · [2023-03-13 16:56 UTC](https://news.ycombinator.com/item?id=35138545)
    From their website homepage: ^c35138545

    \> An optional wall unit heats and cools homes without ducts. Replace your expensive baseboard heaters and radiators with an efficient, ductless unit that blends into your home.

  - **tony\_cannistra** · [2023-03-13 16:56 UTC](https://news.ycombinator.com/item?id=35138542)
    not OP. My understanding is that situations like these really require installation of the (IMO, ugly) wall units ("mini-splits"). ^c35138542

    Current air-source heat pumps can't produce hot water at temperatures necessary to drive radiators.

    - **skrause** · [2023-03-13 17:08 UTC](https://news.ycombinator.com/item?id=35138787)
      It depends on your radiators and insulation. As a rule of thumb modern air-to-water heat pumps have a good efficiency up to a water temperature of 55 C. That can be enough if you have radiators with a large enough surface and no terrible insulation. ^c35138787

    - **oceanplexian** · [2023-03-13 18:49 UTC](https://news.ycombinator.com/item?id=35140519)
      They don’t have to be ugly! You can get mini splits in a cassette format that just looks like an air vent. ^c35140519

      I’m not against ducted systems or anything (Most houses in the US have them). But the laws of physics pretty much guarantee that a mini split will always be more efficient. Air ducts are harder to insulate and not that good at moving heat energy compared to sending refrigerant right to where you need it.

    - **abakker** · [2023-03-13 17:11 UTC](https://news.ycombinator.com/item?id=35138826)
      I think they can produce water at temps to support both radiators and radiant floor heat, but they can't produce the capacity/volume needed ^c35138826

- **jdlshore** · [2023-03-13 19:53 UTC](https://news.ycombinator.com/item?id=35141518)
  Hi Chris, good luck with your startup. I'm in the market for a natural gas --\> heat pump remodel and expect to be signing a contractor's proposal today. I'm looking to put in a 4 ton Mitsubishi hyper heat system with an air handler to replace the gas furnace and four minisplits for the cold spots in the house. I live in the PNW. ^c35141518

  The Mitsubishi remotes and thermostats do indeed look like they're going to be terrible, and their cloud-based offering is a joke whose website has been offline every time I looked at it. I still won't be considering your startup's offering. In the interest of providing constructive feedback, here's why:

  1\. Timing. My existing air conditioner is defunct and I need a replacement before summer.

  2\. No track record. This is by far the biggest issue after timing. I'm not comfortable making such a big purchase, which I expect to maintain for decades, with a company without at *least* a five year history and the opportunity to work out the bugs.

  3\. Multi-port system. My house has serious problems with hot and cold spots that can't be resolved with the existing ducting. Minisplits are necessary. I like that the Mitsubishi system runs the central air and minisplits off a single compressor.

  4\. Contractor. This is a big install and I'm not going to do it myself. I contacted several contractors. Each has their preferred vendor, and the one I liked the best prefers Mitsubishi.

  I hope this is helpful. Again, best of luck to you. Competition in this space can only be a good thing.

  - **amluto** · [2023-03-13 19:56 UTC](https://news.ycombinator.com/item?id=35141554)
    The Mitsubishi thermostats aren’t *that* bad. And you can buy a locally-controllable system from Cool Automation for an egregious price to control them, too. ^c35141554

  - **cmui** · [2023-03-13 20:15 UTC](https://news.ycombinator.com/item?id=35141854)
    Thanks for the feedback! If you feel ok saying, how much was the quote for this install? Do you place any value in indoor air quality? ^c35141854

    - **jdlshore** · [2023-03-14 00:44 UTC](https://news.ycombinator.com/item?id=35145635)
      You're welcome! I'm not comfortable sharing the quote, but you can probably imagine—24k air handler, 4 basic minisplits ranging from 6k to 12k, 48k condenser, five port branch box, installation and replacement of existing A/C and gas furnace. ^c35145635

      Indoor air quality wasn't a factor, no.

- **unixfg** · [2023-03-13 16:59 UTC](https://news.ycombinator.com/item?id=35138618)
  I see an “App” section, but it’s pretty light on details. ^c35138618

  Is the plan for it to be cloud driven (both app and thermostat connect to a remote server) or will there be a local network API? Zigbee/Thread?

  I can see some real value in a system that is fully accessible to a home automation platform.

- **kumarski** · [2023-03-14 06:19 UTC](https://news.ycombinator.com/item?id=35148012)
  HVAC distro is a racket that was mobbed up along with the financing. ^c35148012

  There seems to be no marketing distribution conspiracy to find the 2M of 120M homes per year that need to be replaced.

  Massive problem for cos like watsco.

  The marketing costs for installers are insane and finding the 2M homes is a needle in a haystack biz.

  Heat pumps are only kosher for mild winters.

  Demographics shifting stateside might make this a bad business as people are depopulating everything west of San Antonio b/c of aquifer shortages etc... on a 20 year basis.

  - **cmui** · [2023-03-14 06:31 UTC](https://news.ycombinator.com/item?id=35148069)
    More than 2M per year - this article implies 8M combined natural gas and heat pump installs in US: [https://www.canarymedia.com/articles/heat-pumps/chart-americ...](<https://www.canarymedia.com/articles/heat-pumps/chart-americans-bought-more-heat-pumps-than-gas-furnaces-last-year>) ^c35148069

- **coupdejarnac** · [2023-03-14 09:34 UTC](https://news.ycombinator.com/item?id=35149094)
  I used to be an engineer at Lennox.. HVAC is a mature and boring industry, so I can understand how it doesn't usually generate much interest among people who are attracted to startups. However, just because the industry is very mature doesn't mean the incumbents aren't innovating. I haven't been at Lennox for several years now. I just searched their heatpump offerings, and they look comprehensive. ^c35149094

  I'm not sure what to tell you, but good luck.

- **efields** · [2023-03-13 17:39 UTC](https://news.ycombinator.com/item?id=35139360)
  All-electric house owner here. 2x Carrier heat pumps, ducted air handlers. One of the carrier units is 13 years old and going great. Electrostatic filters on the air handlers. The house was built in the 50s and renovated in 2010, doubling the square footage. That's when they put in the oldest unit. ^c35139360

  Idk if it has to do with the mid-Atlantic temperature swings on the marginal seasons, but this time of year the house will get weirdly cold around 6/7pm, so we bump up the heat a couple degrees. It resets to schedule after two hours. The system has a hard time keeping up if it stays below 20 for an extended period of time, but that just means it holds somewhere around 65ºF instead of 68ºF.

  We're not near seasonal wildfires so air quality is never an issue for us. In fact I notice when we leave the house for the day and come back several hours later, the air in the house has a reassuring "neutral" smell (sealed house cycling old air uninterrupted).

  We also have a whole-house fan, a relic from the original build, which is incredible when you want to cycle in fresh air periodically. More homes should have these.

  Anyway, high seer home-scale heat pumps are just pricy things, but they do work well and efficiently in their existing form. The thermostat we use is also by carrier and is \_fine\_. I don't see anything here that's a significant improvement from our own setup, but they do look nice.

  We have a big house. If we wanted to be more energy efficient at this point, we'd need similar setup in a smaller house. I don't think nice looking residential mechanicals are going to help the transition to cleaner energy sources any faster. Sorry.

  - **cmui** · [2023-03-13 19:39 UTC](https://news.ycombinator.com/item?id=35141292)
    Thanks for the feedback! What was install like for you, any issues there? Do you have any comfort issues that you'd like to address, say a room to hot or cold? ^c35141292

- **adanto6840** · [2023-03-13 18:34 UTC](https://news.ycombinator.com/item?id=35140313)
  Wish you had been around a few years ago, before I took the plunge on two 5-ton Bosch "BOVA 2.0" heat pump units -- I'd have seriously considered your product. ^c35140313

  The Bosch units are inverter driven and contain some interesting tech; we've had some issues with them, unfortunately I'm not sure that the HVAC industry is ready for such tech, but I do generally think it's the future.

  I continually wish (and search Github bi-annually for) there was a way to see what frequency ("capacity") my BOVA units are running at -- aside from just being able to see the "staging" (purely controlled by temperature delta via Ecobee).  There's a USB port on the board, but I can't find any info/data on it & obviously I don't want to take chances on \>\$15k -worth of HVAC units.  But it'd sure be nice to see, at the very least, what the capacity/frequency is -- without having to physically take screws out to remove the panel covering the board.

  Alas, maybe some day -- perhaps once my units are out of warranty I'll be daring enough to try and get something from that (very tantalizing) USB port.

  - **cmui** · [2023-03-13 18:57 UTC](https://news.ycombinator.com/item?id=35140666)
    I'm sure there's some contractor unit that lets you see the live readout of compressor speed. As for Electric Air - we want to give visibility into system operation, what's the input electrical power, what's the output thermal power, how much have you spent on heating so far, and what's your average COP for a given time period (ratio of heating out/electrical in). ^c35140666

    - **adanto6840** · [2023-03-13 20:37 UTC](https://news.ycombinator.com/item?id=35142179)
      If you remove the service panel there's a screen that displays what capacity they're running at.  My installer had some issues initially, and Bosch actually had 2 regional reps (corporate) visit the site themselves.  I'm sure the protocol exists somewhere, but the guys they sent wouldn't have known and I don't believe they connected anything to the board -- the Bosch reps couldn't even correctly explain to me how/what logic controls the speed of the interior blower fan (two speed). ^c35142179

      I actually never really did get an answer to that question -- what/when will the interior fan go to it's "second speed" (when only sending 1 cooling signal & letting the Bosch board have 100\% control over capacity), so we ended up wiring my units to be "remote" controlled, like a 2-stage system - though it's then critical to enable an extra setting ("Reverse Staging" on Ecobee), otherwise you'll just end up with short-cycling when stage2 cooling calls are made.  If you search the topic you'll probably stumble on my Reddit thread which has quite a bit of detail on the topic.  \=D

      I wish you luck;  I do think it's the future.  FWIW I think your product's ideal audience/target market is probably not here/us, but I think a relatively large addressable market does exist.  How you can best reach & tap into that market, at a price point that make sense & while providing a (sales) UX that actually converts -- I think those are the main challenges you'll have to solve.

      - **cmui** · [2023-03-13 22:37 UTC](https://news.ycombinator.com/item?id=35144086)
        Wow, sorry you had to go through that setup hassle. I would also say you are probably in the 1\% of motivated homeowners trying to get those details right. A lot of this difficulty seems like it stemmed from trying to get the Ecobee to play nice with the Bosch. With Electric Air I hope to avoid setup issues like this, the thermostat is specifically designed to work well with the other equipment. ^c35144086

- **acjohnson55** · [2023-03-15 03:58 UTC](https://news.ycombinator.com/item?id=35163664)
  I really admire what you all are doing. ^c35163664

  I am building a house and I just spent countless hours obsessing over the best way to approach HVAC. It's a bewildering topic, thick on opinion, heuristic, and wisdom that's of questionable recency.

  What I want is almost exactly what you describe. A system that holistically optimizes for upfront cost, operating cost, sustainability, temperature, humidity, room-to-room preference/utilization patterns, exhaust of indoor pollution, filtration of outdoor pollution, and ease of maintenance. In the process, I realized that:

  \- Most professionals pick equipment that operates on these things independently, and hope for the best, based on experience.

  \- The ability to comparison shop or get definitive answers on things is very limited.

  \- All the tax incentives don't seem to offset the upfront cost of the machinery that qualifies for incentives.

  \- A lot of professionals are not up to date on their knowledge. I love my general contractor dearly...but he's old school and I had to teach him what an HRV was.

  After all of that research, I ended up opting for a very conventional ducted gas furnace + A/C, with an HRV.

  So you're really speaking my language with what you are describing. Some of the objections people have raised are things I've come across in my own research. But it sounds like you're trying to build something that attacks the whole problem at once, probably understanding that piecemeal solutions will get you stuck having to work within confines of the status quo.

  But, if you succeed, you might stake out a novel model, like Tesla or direct-to-consumer insurance. Sounds very risky, but I wish you all the best.

- **hd95489** · [2023-03-13 19:44 UTC](https://news.ycombinator.com/item?id=35141363)
  Your install costs are super low. Is there some sort of innovation that would drastically reduce install costs? We just got quoted for a conventional heat pump install in Seattle 2/3 of the cost is installation.  The unit costs like 6-8k but to get an installer to install its 18-22k. That’s with 5 quotes so I don’t think it’s abnormal. How do you plan to keep install costs so low at 6k ^c35141363

  - **cmui** · [2023-03-13 19:47 UTC](https://news.ycombinator.com/item?id=35141402)
    How much ductwork are you having upgraded, also any electrical panel upgrades? There can be extra scope that drives up install cost. ^c35141402

    - **hd95489** · [2023-03-13 21:47 UTC](https://news.ycombinator.com/item?id=35143336)
      They don’t itemize that out but the existing electrical line has to be retrofitted to current code and some duct work needs modified to fit a new unit. Nothing crazy though, going from one heat pump to a new one. A drop in replacement was 4k unit and 8k costs so 6k listed here seems super low ^c35143336

- **garfieldnate** · [2023-03-14 12:25 UTC](https://news.ycombinator.com/item?id=35150358)
  I'm confused by the price on the website. It's only \$100? Or is this a deposit to allow me to pay whatever the real price is? Hard to know whether this is worth it without knowing the price. ^c35150358

  - **ahofmann** · [2023-03-14 12:35 UTC](https://news.ycombinator.com/item?id=35150476)
    If you stay on the starting page, you can scroll down and see the prices (from 10k to 14k per unit + installation costs). ^c35150476

    - **malfist** · [2023-03-14 15:32 UTC](https://news.ycombinator.com/item?id=35153159)
      Which is bonkers. ^c35153159

      Daikin's DZ20VC0241 is a 2 ton, 20 Seer heat pump available everywhere. Price including install is 5000-8200 (not counting tax credit).

      Their offering is a 2 ton, 18 seer and costs 16k (not counting tax credit). Double the price at the high end of Daikin's install costs, triple at the low end.

      Plus you get all sorts of vendor lock in with this startup

- **agmetcalf** · [2023-03-14 06:20 UTC](https://news.ycombinator.com/item?id=35148015)
  I think well-controlled fresh air intake is the most uniquely appealing part of this offering. I built a few prototypes to provide CO2 based fresh air intake in our house and it has made our bedrooms *much* more comfortable ([https://www.instagram.com/p/CUYBYm\_v0IV/?igshid\=YmMyMTA2M2Y\=](<https://www.instagram.com/p/CUYBYm_v0IV/?igshid=YmMyMTA2M2Y=>)). I think it’s hard to appreciate until you sleep with it for a week! ^c35148015

  I’m currently working on specifying the HVAC for our next house. I think we’ll go with an air-to-water heat pump feeding in-floor hydronics with a separate fresh air intake and filtration system. I’d be happy to talk about what led us to those choices and the compromises if that’d be helpful.

  Good luck with Electric Air—I think there’s real value in what you’re offering if you can convince people of it.

  - **cmui** · [2023-03-14 07:16 UTC](https://news.ycombinator.com/item?id=35148292)
    Very cool prototype. Fresh air is a bigger deal than people realize. Shoot me a note at the email in my bio, I'd love to connect. ^c35148292

  - **elevenoh** · [2023-03-14 07:46 UTC](https://news.ycombinator.com/item?id=35148460)
    [flagged] ^c35148460

    \[dead\]

- **Dnguyen** · [2023-03-13 16:59 UTC](https://news.ycombinator.com/item?id=35138607)
  So the difference in cost between natural gas and ElectricAir is \~ 400/yr.  And it costs \$14,000 to install the ElectricAir system. It will take a very long time to break even.
  It will be very difficult to convince people with current working natural gas system to switch over. ^c35138607

  - **imhoguy** · [2023-03-13 17:00 UTC](https://news.ycombinator.com/item?id=35138636)
    Unless the ruling changes and one won't be able to install fossil fuel based heating, like in EU soon. ^c35138636

    - **garduque** · [2023-03-13 17:34 UTC](https://news.ycombinator.com/item?id=35139272)
      Sure but his target market is North America, where I don't think there is too much danger of dropping fossil fuel heating anytime soon. ^c35139272

- **nemo44x** · [2023-03-13 19:18 UTC](https://news.ycombinator.com/item?id=35140999)
  Who is going to install these? I am close to a lot of contractors and they aren't going to install equipment from a company they don't have a relationship with. Who gets called back when there's a problem? They also aren't going to install something the end user provides. They make money on reselling equipment, etc. ^c35140999

  Seriously, sourcing the labor side of it is a really difficult problem. Labor has to be licensed, etc. No one is installing this themselves.

  And although the designs look cool, if it costs so much as a cent more to build then no one will buy it. No one looks at their HVAC appliances before they buy them.

  I guess my point is - why would I buy this rather than just call my local HVAC companies and get some estimates?

- **vladgur** · [2023-03-13 18:43 UTC](https://news.ycombinator.com/item?id=35140446)
  The costs to install/replace an existing gas furnace-based system are ridiculous and are not likely to offer any cost benefits over long period of time, especially if you live somewhere with pricey electricity and (relatively) cheap natural gas. ^c35140446

- **verelo** · [2023-03-13 22:30 UTC](https://news.ycombinator.com/item?id=35143974)
  Chris, great and i love that you're working on this. We need more heatpumps in this world! ^c35143974

  Any chance there's a solution coming for people with hydronic systems? We have a house in rural Ontario that has in-floor hydronic in the basement and hydronic radiators upstairs too. We'd love to get off propane, but there are virtually zero options without us installing ducts (which due to the German wood-frame design is very difficult to achieve without a lot of unfavourable cosmetic alterations)

  - **sokoloff** · [2023-03-13 23:44 UTC](https://news.ycombinator.com/item?id=35144980)
    There are air-to-water heat pumps, provided your emitters are sized such that you can heat your home with flow temps at/under 135°F. (I was able to test the prior winter and turning my aquastat way down and see when the house was no longer able to maintain the desired setpoint. For me, that was at about 9°F and it fell by about 1°F inside for every 2°F outside below that over a single night.) ^c35144980

    If you can get by with 135°F (or ideally 130°F) flow, Google for "air to water heat pump" and there's likely a vendor that will sell into Ontario. (Ultimately, I decided against it for economic reasons, mostly because of a monopoly supplier in my area giving me a monopoly quote while not accepting Monopoly money.)

    - **verelo** · [2023-03-14 12:17 UTC](https://news.ycombinator.com/item?id=35150272)
      Interesting! I think upstairs we would struggle but the basement slab runs cooler, I’m pretty sure it would handle this pretty fine. I’ll check it out, thanks!! ^c35150272

  - **kruipen** · [2023-03-13 23:11 UTC](https://news.ycombinator.com/item?id=35144528)
    [https://www.spacepak.com/](<https://www.spacepak.com/>) ^c35144528

- **gregmac** · [2023-03-13 19:00 UTC](https://news.ycombinator.com/item?id=35140728)
  I have been an Ecobee user for years, and one of the main things that sold me on that is the room sensors. ^c35140728

  In my house, there's large south-facing windows that let in a lot of sun, and for a lot of the year the north side of the house will be several degrees cooler than the south. I was constantly battling how to set the thermostat, especially to keep the upstairs a decent temperature at night.

  The Ecobee 100\% solved that: at night the upstairs room sensors control temp, while during the day mostly the main floor does. No guessing: it just works regardless of how sunny it was that day. It would be hard to give that feature up.

  Another handy feature which I didn't realize until owning it is the "min fan runtime per hour". Even set to 20 mins, this helped drastically with evening out the temperatures throughout the house.

  There's already a thread about an open, local API, and I'd mirror that here. The Ecobee isn't open+local, but if they were to go under (or do something stupid like block HomeAssistant), it's \$\$\$ to rip it out and switch to something else. When we're talking about a \$\$,\$\$\$ system I wouldn't even consider it without a company committed to providing a proper local API -- including that it won't disappear in an over-the-air firmware update.

- **kayson** · [2023-03-13 17:20 UTC](https://news.ycombinator.com/item?id=35138983)
  Ducted systems are horribly inefficient. Why heat/cool the entire house if you're only in one room? ^c35138983

  We paid \$11k to have a 4-unit 42kbtu mini-split system installed in our condo. We love it. We turn the two units on in the living areas during the day, and just the two units in the bedroom at night. Each unit comes with its own remote and can be programmed individually. No need for an app-enabled/iot multi-zone thermostat. But if you want it, there were addons available to enable it.

  The only downside in my mind is limited filtration, since the heat exchangers aren't very big, but we have some nice quiet hepa filters running that keep the air quality quite good.

  This does leave CO2 as a potential problem, since its just recirculating inside air, but you'd have the same issue with a ducted system if the intake is inside, which most are.

  You can always get an energy-recovering ventilation system, but that does require ducting. Interestingly, electric air mentions bringing fresh outside air in, but doesn't have any details about energy recovery. In fact the details are pretty sparse all around. I couldn't even find dimensions of the units!

  All that being said, I hope this succeeds because heat pumps are way better than furnaces, and adding competition to this market will be great.

  - **mdeeks** · [2023-03-13 17:30 UTC](https://news.ycombinator.com/item?id=35139187)
    My main problem with mini-splits is that they are just ugly. I can't get past it. Neither can my wife nor others I've talked to. My engineer brain loves the idea, but I just don't want them on my walls nor do I want five different remotes laying around. I suspect thats a problem for many others too. ^c35139187

    - **synctheship** · [2023-03-13 18:50 UTC](https://news.ycombinator.com/item?id=35140548)
      Have you looked at cassette style mini-splits? Nothing on the wall's you'd just replace the vent in your ceiling. They are quite a bit larger than your standard vent though. ^c35140548

      As far as remotes, there are a bunch of universal remote control options and smart (wifi/bluetooth) based controllers.

    - **kayson** · [2023-03-13 18:48 UTC](https://news.ycombinator.com/item?id=35140506)
      My wife (who invested heavily in the aesthetics and interior design of our home) shared the same concern. We decided to do it anyways, and though they're certainly a little ugly, they blend in and just sort of go away. It helps that they're fairly close to the ceiling. ^c35140506

      The remotes aren't lying around. They all have wall mounts that we placed near the light switches and ceiling fan remotes. With the units being programmed, though, you don't often have to mess around with them anyways. Unless you're the sort who likes fiddling with the temperature and fan speed.

    - **skellington** · [2023-03-13 18:55 UTC](https://news.ycombinator.com/item?id=35140637)
      You can get mini-splits that don't have protruding wall units, but the real downside of mini-splits is indoor air quality. ^c35140637

      They don't have good filters and they basically recirculate the air in the same room.

      For a very tightly built house, you need to bring outside air in continuously, ideally through an energy recovering ventilator (ERV), and then you want to filter that air with a MERV 13 filter (or whatever target you want), plus you want to move and filter all the house air in general, plus you often want to control whole house humidity.

      Mini-splits can't do any of the above.

    - **turtlebits** · [2023-03-13 18:31 UTC](https://news.ycombinator.com/item?id=35140259)
      You can get ceiling cassettes as well as radiator style floor mounted air handlers.  They just cost more. ^c35140259

  - **chewmieser** · [2023-03-13 17:24 UTC](https://news.ycombinator.com/item?id=35139076)
    You could always use smart vents (e.g. [https://flair.co/](<https://flair.co/>)) to eliminate some of the inefficiencies you mentioned with ducted systems. ^c35139076

    - **kayson** · [2023-03-13 18:51 UTC](https://news.ycombinator.com/item?id=35140557)
      Yes! This is what I wanted to do first but we only had an aging furnace and no AC. I've read that you can run into problems with back pressure if you close too many vents, though. ^c35140557

  - **simplyaccont** · [2023-03-13 18:20 UTC](https://news.ycombinator.com/item?id=35140071)
    it's possible to use zone system with ducted hvac. extra layer of fun. ^c35140071

- **dmitrygr** · [2023-03-13 17:08 UTC](https://news.ycombinator.com/item?id=35138784)
  Cloud tie in. Maybe acceptable for a \$30 gadget. Not acceptable for a home appliance. Hard pass! ^c35138784

- **mrDmrTmrJ** · [2023-03-14 03:20 UTC](https://news.ycombinator.com/item?id=35146981)
  Do you combine an ERV or and HRV into your air quality module? ^c35146981

  My parents live have oil heat (water radiators) and a classic ducted A/C unit in Installation Climate zone 5A (Moist - New England) and I'd love to get them to a product like yours. ERV/HRV functionality for air quality would really help and would set this product apart from current offerings in the market.

  I don't really know how to do proper ventilation/humidity control in that climate without an ERV.

- **zol** · [2023-03-14 03:39 UTC](https://news.ycombinator.com/item?id=35147150)
  I’ve been wondering lately how small one of the indoor inverter heads could be scaled down to. Specifically, whether it could approach the footprint of a ducted heating outlet (with most of it under the floor). It seems like it would be more efficient to run coolant lines to the heads rather than blowing all that air through ducts as well as making it easier to have separate temp zones in the house. Does anyone know what the physical limitations are? ^c35147150

- **unknown** · [2023-03-14 00:49 UTC](https://news.ycombinator.com/item?id=35145679)
  [deleted] ^c35145679

- **the\_third\_wave** · [2023-03-13 20:46 UTC](https://news.ycombinator.com/item?id=35142294)
  Those prices... out of this world? Can you explain to me how it is possible to get a 7kW air/air heat pump installed for a total cost of \~17.000 \[1\] Swedish kronor (\~\$1600 at current rate) for a fraction of the price of these things? These devices all come with networked remote control, most of them can be integrated into 'home automation' systems without problems, they tend to work down to around -30°C (-21°F) albeit with lower efficiency (as will these devices). All that is 'missing' is the 'air quality' claim - although several of these heat pump manufacturers make claims about their devices filtering the air, using ionizers to 'increase air quality' and such. What remains is the Apple/Nest-like design and the claim of better integration with thermostats. To me this does not explain the factor 10 price difference, especially given that the Swedish prices include the high Swedish value added tax (25\%) as well as the installation costs. What am I missing? ^c35142294

  \[1\] [https://www.polarpumpen.se/varmepumpar/luftvarmepump/](<https://www.polarpumpen.se/varmepumpar/luftvarmepump/>)

- **daviross** · [2023-03-13 21:06 UTC](https://news.ycombinator.com/item?id=35142657)
  This looks/sounds neat, I'll be happy to keep an ear out on how you're doing.
  The thing keeping me from anything more yet though: What's the ductless option like? ^c35142657

  I don't have any ducts, just hydronic+baseboard heating currently (and a dual-hose portable AC unit for cooling). I'm looking at a mini-split setup, but that's a fairly daunting prospect for the issues you note with the existing market.

- **fwlr** · [2023-03-14 11:03 UTC](https://news.ycombinator.com/item?id=35149647)
  Why direct-to-homeowner? Your product requires installation by a licensed professional, it doesn’t make sense to sell it without the installation. And I don’t see any major benefits to you, the customer, or the contractor by doing it this way. ^c35149647

  Supply HVAC contractors like the furnace companies do, work with contractors so that booking an installation is part of the sale process, or train your own installation team in each area.

- **will\_walker** · [2023-03-13 23:06 UTC](https://news.ycombinator.com/item?id=35144458)
  I'm currently sitting on a home with a basement open with no heater, and trying to find a contractor to install an all-electric heat pump. I'd love to be your customer but I worked in hardware and just don't see you hitting delivery times, and I can't wait that long. ^c35144458

  For those of us who can't wait, If you were to buy a ducted heat pump today, which brand would you go with? Who is the best of the worst?

  - **cmui** · [2023-03-13 23:07 UTC](https://news.ycombinator.com/item?id=35144481)
    If you need something today, Mitsubishi or Daikin, and for ducted specifically, Mitsubishi. ^c35144481

- **avaku** · [2023-03-14 10:11 UTC](https://news.ycombinator.com/item?id=35149359)
  Great idea. I've read some people's comments. There are a lot of companies in the UK that sell their equipment, and use contractors to install them (Worcester Bosch for boilers, even Tesla uses external contractors to install the chargers). I think you can do it. There was a heat pump company with similar approach in the UK that went bust recently, so maybe research what they did wrong. ^c35149359

- **simonbarker87** · [2023-03-13 16:56 UTC](https://news.ycombinator.com/item?id=35138551)
  If the Vapor aspect works well then this might make air source heat pumps tenable in cold countries. The current crop here in the UK are costing home owners a fortune as the 3-4 kw multiplier drops to 1 below 0degC or so and hearing becomes horrifically expensive. I know a chap who was paying £1,200 a month to hear is home at the worst of this winters cold and the energy price jumps we have here. ^c35138551

  - **pappn** · [2023-03-13 17:02 UTC](https://news.ycombinator.com/item?id=35138673)
    FYI, air-to-air heat pumps are very popular in Norway. There are models that have \>2 COP in -15 C, for instance Toshiba Daiseikai 9S at 2.35 at -15C, and \>5 at +7C. ^c35138673

  - **heatpumpfan** · [2023-03-13 17:09 UTC](https://news.ycombinator.com/item?id=35138802)
    "Cold climate" air source pumps have been available for years. Even my cheap MrCool Universal has 100\% output down to -5F and it is not even really a "cold climate" heat pump. ^c35138802

  - **IanCal** · [2023-03-13 17:03 UTC](https://news.ycombinator.com/item?id=35138686)
    That doesn't sound right. They should be above 1 for much lower temperatures. ^c35138686

- **alkonaut** · [2023-03-14 10:56 UTC](https://news.ycombinator.com/item?id=35149605)
  It's really interesting how the task of heating a home (and providing hot water) is solved so radically differently in different parts of the world. Some areas seem to use only wall-mounted air-air pumps, and gas burning boilers for hot water, some times even without hot water storage i.e. direct burning (Something I have never seen in North Europe). I use a combined heat pump with hot water heater/tank. The whole thing is about the size of a regular closet and the heat pump has no outside unit. It uses only the heat in the return air leaving the house. So basically it handles ventilation, and cools the air being vented out, re-using it for heat. These cost \$5-10k and last 15-20years. This to me is a pretty reasonable cost given they do all ventilation, space heating and hot water production in one. And there are no pressurized lines anywhere because it's a single self-contained unit without an outside part. ^c35149605

- **lukepighetti** · [2023-03-13 17:44 UTC](https://news.ycombinator.com/item?id=35139442)
  All I'm looking for is a heat pump that can maintain a COP of 3.0 or higher down to -20f, can be easily controlled via MQTT on my home network OR via standard 3 wire thermostat, does not use the cloud for any of it's core functionality, and does not require an HVAC license to buy parts and see technical manuals. ^c35139442

  If you've nailed that down, awesome!

- **5amdotis** · [2023-03-13 16:55 UTC](https://news.ycombinator.com/item?id=35138518)
  Can someone install and use it without the app? ^c35138518

  - **cmui** · [2023-03-13 16:58 UTC](https://news.ycombinator.com/item?id=35138594)
    We will have standard home integrations (Google Home, Apple Homekit, likely implemented via Matter standard). Using those you can set temperature easily, however to have deeper insight into system state, energy use, air quality, you'd have to use the app. We could also set up the thermostat so it can be used standalone - no app integration. ^c35138594

- **trollied** · [2023-03-13 18:40 UTC](https://news.ycombinator.com/item?id=35140385)
  This: [https://ecorenovator.org/forum/showthread.php?t\=484](<https://ecorenovator.org/forum/showthread.php?t=484>) is a homemade heat pump setup, documented over 10+ years of forum posts. A great read if you have a few hours to spare. 2 million views! ^c35140385

- **tguvot** · [2023-03-13 17:11 UTC](https://news.ycombinator.com/item?id=35138841)
  Putting aside fact that homeowners can buy HVACs online and get it shipped, how it differs from mrcool ducted heatpump that, for example can be bought for under 4k for 3ton model and have DIY install (no vacuuming needed), besides nicer of external unit and prettier app ? as opposed to 12k for yours + 8k install ? ^c35138841

  - **cmui** · [2023-03-14 06:00 UTC](https://news.ycombinator.com/item?id=35147911)
    Yeah, its a good question. I think 'direct to homeowners' has generated some confusion that this is a DIY product. After a purchase we have one of our contractor partners perform the install, they also bring the unit with them, we don't ship the unit to you and expect you to find your own installer or DIY. ^c35147911

    - **tguvot** · [2023-03-14 16:32 UTC](https://news.ycombinator.com/item?id=35154156)
      no confusion here. i was asking why it's triple the price for same functionality (before installation) ?
      with regards to total price including install: it pretty much same price as any central ducted heatpump that offered by lenox/trane/etc. what's the innovation here ? ^c35154156

- **el\_don\_almighty** · [2023-03-13 19:14 UTC](https://news.ycombinator.com/item?id=35140925)
  Parts & Service documentation means more than software ^c35140925

  The nerds can always reverse engineer practical controls.  As a systems integrator, your job is providing access to comprehensive service information and long-term, easy access to parts.  This is harder than it seems because of the necessary infrastructure and product management control.  (Engineers are always tweaking something)

  Of course, then you have to withstand the inevitable liability risk and lawsuits from idiots improperly installing capital goods in their homes.  Let's be honest, there are people out there struggling to fasten their airplane lap belt...

  The technology is NOT the hard part, it's all in the distribution and support

  I would make sure your systems focus more on self-diagnostics, data logging, and anything else that makes troubleshooting faster and easier

- **chime** · [2023-03-13 16:55 UTC](https://news.ycombinator.com/item?id=35138532)
  I would love to upgrade once my existing unit dies, especially if you can get a test unit reviewed by [https://www.youtube.com/@TechnologyConnections/search?query\=...](<https://www.youtube.com/@TechnologyConnections/search?query=heat%20pump>) ^c35138532

- **richwater** · [2023-03-13 17:06 UTC](https://news.ycombinator.com/item?id=35138740)
  I was raised on the belief that Heat Pumps could not be used in climates that really got "cold". I see the website lists -15 degrees as the operating temperature. What has changed in the past years to enable this? It seems like this would cover most of the contintental US now. ^c35138740

  - **Scoundreller** · [2023-03-13 17:13 UTC](https://news.ycombinator.com/item?id=35138861)
    Probably better/more efficient defrost cycles. And maybe refrigerant choices. ^c35138861

    - **heatpumpfan** · [2023-03-13 17:15 UTC](https://news.ycombinator.com/item?id=35138903)
      Refrigerant, pressure, vapor injection, and a highly "managed" vapor compression cycle. ^c35138903

      - **HEPA\_As\_Service** · [2023-03-13 18:32 UTC](https://news.ycombinator.com/item?id=35140276)
        Regulation has helped a lot!  Government can act as the unifier of buyer's not that long ago central systems scored 6 now this lowballs at 18. ^c35140276

        If you increase the time of operation you can earn greater return on the costs invested. Commercial water heating is storing heat cheaply now to avoid storing water warm that will be used as that causes biofilms and disease.

        Healthy sleep in room you want to work in upon rising creates a challenge for live pumping of heat.  A sudden heat is best and that means storing from day before.  We thrive sleeping in cold being woken by warmth.

        \$20,000 on a four ton heating load is compromised by this design tragically.

- **gcheong** · [2023-03-13 18:31 UTC](https://news.ycombinator.com/item?id=35140264)
  How far away can the condenser be located from the air handler? Does it have to be outside or can it work in a garage? Also, how do I determine the size of system I need? Biggest problem with our current nat gas furnace, which isn't a fuel problem per se, is that it isn't zoned  (which I can alleviate somewhat with the ecobee and its remote temp sensors) so I am considering installing mini-splits in the bedrooms and downstairs room and having the main furnace for heating the living room and other areas as needed but I'd also like to move the main furnace off nat gas as well at some point if possible but I don't want a big condenser taking up space in the rear patio which is potentially where I could see your unit come in. ^c35140264

  - **cmui** · [2023-03-13 19:02 UTC](https://news.ycombinator.com/item?id=35140760)
    Condenser can be typically \~25ft from the air handler. It would have to be outside, otherwise it would act as a refrigerator for the garage, and tank the efficiency of the system. System size - we're working on an online tool to get you close to the right size. In the current flow you preorder and a contractor will prepare the final quote and system sizing (we give them a web app to turn a utility bill into a heat pump size). ^c35140760

  - **brudgers** · [2023-03-13 18:40 UTC](https://news.ycombinator.com/item?id=35140389)
    If not part of a major remodel, a mini-split would by my recommendation for retrofit. ^c35140389

    Horizontal runs usually aren't a problem with HVAC lines. Vertical runs can be.

    But read the manual for limitations and when the lines need to be upsized.

- **notwhatyouthink** · [2023-03-13 16:58 UTC](https://news.ycombinator.com/item?id=35138588)
  Who are you partnering with to design/manufacture your air handler and condenser units? ^c35138588

- **NathanielBaking** · [2023-03-14 11:42 UTC](https://news.ycombinator.com/item?id=35149972)
  I have had two heat pumps in the last 20(ish) years.  The first one worked ok for heating. Warm air I can only describe as tepid blew out of the registers.  The second heat pump is amazing.  We live in Madison, WI, so very cold. This heat pump blows out air that feels just like the gas furnace air and is able to heat our house down to around 5 degrees Fahrenheit.  It consumes quite a bit more energy at that temp and cost wise gas is better. ^c35149972

  I would second @quirkot in all of his points.  I consider myself a good home re modeler.  I have done plumbing, electrical including replacing all the wiring up to the pigtail at the top of the roof.  I will not touch HVAC or gas.

  - **mabbo** · [2023-03-14 11:45 UTC](https://news.ycombinator.com/item?id=35149993)
    The technology has really improved in the last decade ^c35149993

- **mattcantstop** · [2023-03-13 19:26 UTC](https://news.ycombinator.com/item?id=35141109)
  I have had a lot of issues with my mini-splits. I am a firm believer in the technology, but my Pioneer units have had a lot of issues. I am glad some innovative companies are getting into this industry. I built a passive house that has triple-framed walls. We don't need much heating/cooling, so mini-splits seemed the obvious answer. Hopefully we get them squared away soon as we have been in the home for 1.5 years and have learned that in the Denver area (zone 5b) they don't perform well when it gets into freezing temperatures. I am interested in the technology you have described (the injection) to keep it heating during really cold days. ^c35141109

- **jacquesm** · [2023-03-13 18:26 UTC](https://news.ycombinator.com/item?id=35140176)
  I've been electrifying the heating of our house bit by bit and I'm probably in the target market for your product. The big killer for direct-to-consumer here is that the refrigerants used are environmentally hazardous and most of them are greenhouse gas producers. Making it so that you don't need a licensed professional (who will charge you an arm and a leg for something that should be simple and end-user safe) would go a long way to drive adoption. ^c35140176

  What refrigerant are you using?

  Will your device require internet access? (if so it is a non-starter for me, I don't want any of my appliances connected to the internet and to have some stupid service grafted on).

- **fauigerzigerk** · [2023-03-13 17:19 UTC](https://news.ycombinator.com/item?id=35138965)
  I keep reading lots of horror stories about heat pumps. People are complaining about all of the following: ^c35138965

  \- Enormous energy bills because under some conditions (cold weather?) heat pumps use a lot more energy than expected.

  \- Heat pump equipment and radiators taking too much space in small homes.

  \- Cold homes and/or a requirement to keep windows shut because heat pumps just don't generate enough heat.

  \- Only suitable for very well insulated homes.

  Am I only reading this because people are more willing to speak up when something bad happens to them than when everything works as expected?

  I worry that heat pumps are only viable under perfect conditions, installed by exceptionally competent engineers that hardly exist anywhere.

  Please tell me it is not so! :)

  - **toast0** · [2023-03-13 17:41 UTC](https://news.ycombinator.com/item?id=35139411)
    You probably don't hear much from people who are happy with their heat pumps, because it's boring when it just works. ^c35139411

    But, the competence required for heat pump sizing depends on the local climate. If you need more heat than the outside unit can gather, you're stuck with fallback heat, which is usually resistance strips, which is expensive. Some thermostats will call for the fallback heat anytime the requested temperature is 2-3 degrees F above the measured indoor temperature; if you've got a thermostat like that, you've got to be careful how you adjust it, and HVAC installers don't always explain that in ways that the users understand. Lots of people want it a few degrees colder when they're sleeping, but setting that up in the most straightforward way leads to resistance heating in the morning.

    You're going to tend to want to windows of conditioned spaces closed, otherwise you're sending your heating budget out of the windows. Heat pumps are usually setup so you can directly regulate the temperature as desired, rather than boilers where it gets so hot that you need to open the windows to balance. If you want to run it with the windows open, you'd need more capacity, and you'd really need to convince your HVAC person. It probably makes more sense to look into a heat recovery ventilation system, which gets fresh air in without losing as much of the heat (or gaining as much heat if you're cooling). This is probably a norms thing.

    Insulation helps reduce heating / cooling costs for sure, but if your home is less insulated than the norm, you *just* need a larger capacity system. That's another place where installer competence comes in. Actually measuring airflow and calculating requirements is unfortunately not very standard, there's a lot of rules of thumb or replacing with similar size units or the neighbor has X so use that. Again, this is workable in mild climates, but if you've got outside temperatures much below freezing, you need a competent installer, as capacity goes down quite a bit as the temperatures go down, and that's also when you need it the most. And, just insulating the heck out of an old home that was built to be drafty can cause issues with retained moisture and mold; it needs to be done carefully and appropriately.

    - **fauigerzigerk** · [2023-03-13 17:56 UTC](https://news.ycombinator.com/item?id=35139664)
      So the fallback heat issue seems fixable by learning how to operate the equipment properly. That's good to know. ^c35139664

      Unfortunately, the requirement to keep windows shut and install a ventilation system instead rules out every single place I have ever lived in.

      - **toast0** · [2023-03-13 18:05 UTC](https://news.ycombinator.com/item?id=35139818)
        Yeah, if you're accustomed to keeping windows open during the heating season, I think you're going to have a bad time unless you live with a mild climate. Sounds like you're probably on a boiler / radiator system; which probably means you're not in a very mild climate. ^c35139818

        You could ask an HVAC company what it would take to be on a heat pump with the windows open, but it's probably going to cost a lot of electricity, and if you build the system for that, when you eventually do decide to close the windows, the system is going to be too big and you'll have comfort issues from that.

        Do you have air conditioning? Do you leave the windows open during the cooling season?

        - **fauigerzigerk** · [2023-03-13 18:16 UTC](https://news.ycombinator.com/item?id=35140014)
          Understood, thanks! ^c35140014

          I'm in London using a gas boiler like almost everybody here. Our windows are always open in the summer and also during much of spring and autumn to keep the mold at bay and the air fresh.

  - **londons\_explore** · [2023-03-13 17:32 UTC](https://news.ycombinator.com/item?id=35139241)
    Heat pumps are trying to compete against very inefficient, yet very powerful, forms of heating. ^c35139241

    A 100 year old house might have 12 fireplaces, each of which, when loaded full of wood or coal, can output 10 kilowatts.   Thats 120 kilowatts of heat - 500k btu/h.

    If upgraded to a gas boiler, that same house might be fitted with a 30 kilowatt system - 100k btu/h

    The same house outfitted with a heat pump might expect to get a 10 kilowatt system - 34k btu/hr.

    See how we are fitting smaller and smaller heating systems to our houses?   Thats because a heat pump's cost scales with capacity, so we don't want to oversize.    In fact, a typical house wouldn't even have enough electricity for a heat pump as powerful as those fireplaces!!  Whereas a fireplace doesn't really cost any more to make it a tad bigger.

    The less powerful heat sources need to run all the time, and will take many days to bring the house up to temperature after being turned off.   Even then, they need to be paired with extra insulation to reduce losses.

    - **Ekaros** · [2023-03-13 19:14 UTC](https://news.ycombinator.com/item?id=35140937)
      12 fire places? Is that a mansion or something? Or just poorly designed and not insulated in any way? ^c35140937

      - **londons\_explore** · [2023-03-13 19:52 UTC](https://news.ycombinator.com/item?id=35141491)
        A typical WW1 'workers house' would have \~5 bedrooms, 10 foot ceilings, \~6 other rooms, and one or two fireplaces in each room. ^c35141491

        With no heat circulation system, you would want a fireplace in each room for comfort.   Typically windows wouldn't really seal, so you needed the radiant heat.

  - **cmui** · [2023-03-13 17:56 UTC](https://news.ycombinator.com/item?id=35139665)
    Other replies have great points. A few of my own (1) Proper install is really important, we're building a software tool to make sizing heat pumps and qualifying ducts easier (2) Having a dedicated smart thermostat means that back up heat strip operation is much better than the normal control logic (3) A well installed heat pump system provides a better thermal environment than a furnace because it precisely matches the load of your home instead of cycling on and off. This lets the surfaces in your home soak to a more uniform radiant temp, and radiative exchange is \~50\% of your perceived thermal environment at room temperatures. ^c35139665

  - **olyjohn** · [2023-03-13 17:37 UTC](https://news.ycombinator.com/item?id=35139321)
    I replaced my electric furnace with a heat pump. It takes up the same space as the old furnace, so you're not wasting any space inside the house. There is an outside unit, but we just put it on the side of the house where we don't see or hear it. They are noisy outside, that's one thing they don't always tell you. ^c35139321

    When the temps are too cold out, there are still electric elements inside the unit in the house. Sure, that's probably not saving me any power when it's running, but most of the time it's not. It pretty much only kicks in when there's a big temp differential between desired temp and current temp. It's basically like having the best of both worlds. Plus, as a bonus, I got A/C for the summer to offset all my winter savings.

    - **fauigerzigerk** · [2023-03-13 17:58 UTC](https://news.ycombinator.com/item?id=35139711)
      *\>It takes up the same space as the old furnace* ^c35139711

      Is that a size similar to a gas boiler?

  - **ezrast** · [2023-03-13 17:47 UTC](https://news.ycombinator.com/item?id=35139510)
    I've no horse in this race (not a homeowner), but Technology Connections has made a series of videos advocating heat pumps, most recently this one: [https://www.youtube.com/watch?v\=CVLLNjSLJTQ](<https://www.youtube.com/watch?v=CVLLNjSLJTQ>) ^c35139510

    The gist is that heat pump technology is continuously getting better at working in cold conditions, so if the horror stories are more than 5-10 years old they may not reflect the current state of things, and in extreme situations resistive heating can always be used as a backup.

    Heat pumps are "just" air conditioners that point the other way, and AC is extremely common in the USA, so I'd doubt that the competency required is exceptional.

  - **hd95489** · [2023-03-13 22:21 UTC](https://news.ycombinator.com/item?id=35143859)
    They aren’t a drop in replacement. Heat pumps need large ducts or you won’t have enough flow because the air in the ducts is not that much hotter than outside air. Delta t is low ^c35143859

- **unknown** · [2023-03-13 17:31 UTC](https://news.ycombinator.com/item?id=35139220)
  [deleted] ^c35139220

- **alsaaro** · [2023-03-14 05:24 UTC](https://news.ycombinator.com/item?id=35147729)
  Not to be too big picky, but why are the first few photos showing the heat pump with a perspective that implies a small dimensions, as if it were some portable boombox. Also, why do the photos look indoors? ^c35147729

  What do you think of thermoacoustic heat pumps?

  - **cmui** · [2023-03-14 05:56 UTC](https://news.ycombinator.com/item?id=35147893)
    In the future we'll likely show the condenser more in context, a backyard or something similar. ^c35147893

    I don't know that much about thermoacoustic heat pumps. I do suspect they're less efficient than a standard vapor compression heat pumps, otherwise that would be their main selling point in the commercialization project underway: [https://www.blueheartenergy.com/ourtechnology](<https://www.blueheartenergy.com/ourtechnology>).

- **boringg** · [2023-03-14 12:43 UTC](https://news.ycombinator.com/item?id=35150563)
  Conceptually this sounds compelling.  How do you get around having to use heat pump manufacturers or are you beholden to them to build your product? ^c35150563

  From a mini split perspective - where we have our heat pumps situated is for AC and when we would use them for electricity (winter) those floors are already to hot.  Ie take heat away in the summer on third floor, not add heat in the winter on third floor.  They are the best on the market but are completely trash interface for managing temperature - all individually controlled remotes.  I could do the work to integrate them but ive heard its cumbersome and doesnt work well.(to your points).

  Good luck

- **AkhSha** · [2023-03-13 20:33 UTC](https://news.ycombinator.com/item?id=35142129)
  Why are heat pumps suddenly getting so much attention? Here in Australia they have been common for at least the last 20 years. Most new houses have been fitted with heat pumps, or as we know them, reverse cycle air conditioning. ^c35142129

  - **hummus\_bae** · [2023-03-13 20:51 UTC](https://news.ycombinator.com/item?id=35142373)
    Not to start trash talk, but I believe that most of the ones here are scams. ^c35142373

    They are effectively electricity generators, using electricity to heat and generate more electricity. In typical Australian winter even slightly below average outside temperature means they are generating more than they are consuming.

    They definitely have a place, but they are not as good as they are marketed to be.

- **steren** · [2023-03-13 21:26 UTC](https://news.ycombinator.com/item?id=35143009)
  As someone who recently picked a contractor to install a heat pumpt I need to see: ^c35143009

  \- confirmation that it does both heating and cooling
  \- the price
  \- a list of approved contractors who can install it in my area
  \- the expected installation costs

- **unknown** · [2023-03-13 17:55 UTC](https://news.ycombinator.com/item?id=35139653)
  [deleted] ^c35139653

- **antisthenes** · [2023-03-13 20:35 UTC](https://news.ycombinator.com/item?id=35142156)
  When you advertise as something being sold direct, it usually implies some kind of cost savings due to cutting out the middleman. ^c35142156

  Instead, what we're seeing here is about a 2x cost of what an HVAC company would charge you for installing the heat pump.

  So you've cut out the middleman, but inserted your startup here and decided to upcharge the end user double. Justify the cost to me, as a homeowner. Why should I not opt for an HVAC-company installed heat pump from a known-brand like Mitsubishi or Hitachi?

  What do I get for the extra \$6-7k you seem to be upcharging? Is it efficiency? PM 2.5 sensors? Longer expected system lifetime?

- **elif** · [2023-03-13 23:57 UTC](https://news.ycombinator.com/item?id=35145117)
  For comparison on pricing, their lowest tier unit is 24kbtu and costs \$10k. ^c35145117

  I bought an LG split with 4 ceiling-mounted heat exchangers, one of them 18K BTU, and 3 of them 9K BTU, all of the plumbing and distribution box to connect them, and the outside 48K BTU exchanger, and the total shipped price including sales tax was \$7,200.

  The advantage of having 4 independent indoor units is the key, as you don't have to heat the entire house 24/7 and can save energy by only heating/cooling the appropriate zones. I don't see even any option or pricing for them to use 4 indoor units on their website.

  - **cmui** · [2023-03-14 00:08 UTC](https://news.ycombinator.com/item?id=35145234)
    Definitely hearing the feedback that we need better communication on pricing and sizing! A 24kbtu at 5F heat pump is much bigger than a 24kbtu heat pump at 47F so its not an apples to apples comparison. You're right about ductless offering more opportunity for zoning, but I think most homeowners with ducts would like a drop-in replacement for their furnace, not a bunch of extra hardware in each room. ^c35145234

- **papertokyo** · [2023-03-13 20:18 UTC](https://news.ycombinator.com/item?id=35141885)
  Small suggestion for your preorder buttons: the gray/white combo doesn't have great contrast and might be perceived as being in a disabled state. I'd recommend black/white on light backgrounds and white/black on dark backgrounds to make them fit with the (very nice) industrial design theme. ^c35141885

  Our building (Western Canada) has a heat pump system and it's very capable of keeping the apartment comfortable in all seasons as long as your definition of summer cooling isn't "like being inside a fridge". Great to see the tech being developed for mass adoption.

  - **cmui** · [2023-03-13 22:30 UTC](https://news.ycombinator.com/item?id=35143986)
    Thanks for the suggestions! ^c35143986

- **Dave3of5** · [2023-03-14 23:07 UTC](https://news.ycombinator.com/item?id=35160626)
  I don't know what the comparable price is given this is priced in dollars and in the US but compared to a gas boiler in the UK (I know this does cooling as well). The price jump is insane £20k installed is about 10 times the price of a gas boiler. ^c35160626

  My parents neighbors got a heat pump installed at about that same price so I think it makes sense. Even at 50\% the cost of a natural gas boiler it would be at least a decade before it was paid off which I'm not sure how long these things last.

  Also for the founder there are a lot of companies in Europe selling this type of thing at a similar price.

- **alanh** · [2023-03-14 16:31 UTC](https://news.ycombinator.com/item?id=35154152)
  I hope you consider HomeKit compatibility :) Most new tech i would buy for my home would need to integrate into my smart home system which is currently powered by HomeKit (although I am slightly wary of lock-in) ^c35154152

- **tryqa** · [2023-03-14 11:28 UTC](https://news.ycombinator.com/item?id=35149853)
  \> The thermostat algorithm combines demand-response with weather and time-of-use rate plans to reduce monthly utility bills through pre-cooling and pre-heating. ^c35149853

  In addition to this, have you considered also offering a simple model? I have very bad experience with heating systems lecturing me about the outside temperature. It is always a game of coercion to get them to do what I want.

  I want no outside thermostat, no connection to the Internet. I want a single knob to set the room temperature. If I set it to 25°C after a long walk in winter, I want it to be 25°C within half an hour.

- **samstave** · [2023-03-13 19:49 UTC](https://news.ycombinator.com/item?id=35141440)
  Can you have a system, such as a "Solyndra-type-rod"(s) which placed down a deep well and a solar pump to flow water intor a unit that sits within the ground-well water level and use that as a coolant supply and the solar to provide a small amount of elec to a downward pump to push water through the closed system, and then have a solar powered UV light strip to kill bacteria on the upward flow... then pipe that to a rooftop black-ulta-paint pased piping module to allow solar heating for the water.... in addition to your system? ^c35141440

  - **cmui** · [2023-03-13 22:51 UTC](https://news.ycombinator.com/item?id=35144266)
    That feature ships Winter 2034. ^c35144266

- **j928734** · [2023-03-14 16:38 UTC](https://news.ycombinator.com/item?id=35154262)
  If you're looking for ways to differentiate a heat pump product ... I have a 55k btu heat pump (bosch bova60) and it is loud (my neighbor, who is \~15-20ft away is complaining that it wakes him up at night) - as a result, I've been using too much backup heat (at temperatures when the heat pump would be perfectly sufficient). I would happily pay for a super-quiet outdoor unit. ^c35154262

  the thermostat integration wasn't hard. and the bosch unit has a blower, so the "can it go into a central ducted system?" question was also easy.

- **pjsg** · [2023-03-13 19:00 UTC](https://news.ycombinator.com/item?id=35140720)
  I want to know how to prevent my house from freezing (I'm in New England) in the middle of winter during a multiday power outage. Today, I run a 7kW generator that can keep the oil furnace running and the fans to circulate the air through the heat-exchangers (it is a multi-zone system). ^c35140720

  It seems that I need soft-start compressors *and* coordination between the different units so that they don't all try to start at once.

  I don't care if the house gets down to 40F during this period. I just don't want the interior water pipes to freeze.

- **rappjo** · [2023-03-13 22:06 UTC](https://news.ycombinator.com/item?id=35143648)
  I have many of the issues you've hit upon - I currently have an older heating and no cooling, and I wanted to upgrade to a newer system. I signed a contract with a vendor that had previously worked in our HOA, but they reneged and cancelled our contract, so now we've been left in the lurch with the existing system we had without a good way to proceed. Would love to have a new system that plays well with my smart home, is efficient, and cost effective (both in terms of installation and ongoing operational cost). ^c35143648

- **jakedata** · [2023-03-13 20:29 UTC](https://news.ycombinator.com/item?id=35142044)
  You should give some thought to offering an AC-DC power supply. Being able to dedicate several solar panels directly to heating or cooling might get people out of a regulatory bind with crazy interconnect fees and local regulations. ^c35142044

  The trick would be to supply supplemental DC solar power in a manner that would not be considered grid-tied. That would eliminate a whole level of installation costs, permitting fees and time consuming approvals. Plus you could run the system at some capacity during a grid outage which could be a lifesaver.

  - **tgtweak** · [2023-03-13 21:12 UTC](https://news.ycombinator.com/item?id=35142743)
    Most ultra high efficiency heat pumps are already using DC inverter technology which allows the compressor, fans and pumps to run on fully variable speed.  If Electric Air is planning on using DC components for their heat pumps, they could make it DC powered as well.  The issue is that it would increase cost substantially for people who don't necessarily need it since a 5KW class DC controller (to run the aforementioned off of solar) would add a good chunk to the bill of materials.  It would also add a lot of complexity to the system.  Lastly, it is only really practical in hotter summer climates for cooling where your cooling demand and sunshine line up nicely. In heating applications, you need the most power when it is cold out (in the middle of the night) and so the demand and generation is almost fully inverted. ^c35142743

    One feature that would be great (and universally practical) is using the heat pump to heat water with the waste heat from air conditioning in the summer (or when any time the house doesn't need the air heated).  Add to this the fact that heat-pump water heaters are in the \$2000 range, and eligible for many credits - it could be a great add-on.

    - **jakedata** · [2023-03-13 21:52 UTC](https://news.ycombinator.com/item?id=35143415)
      I wouldn't try to over complicate things. A 5KW DC solar controller does not need to be included in every product. The system could allow for DC power input in a manner controlled by software that could offset power delivery from the AC stage. ^c35143415

      Individual panel optimizers can already tune output voltage and current, it is just a matter of telling them what you want. If you are really clever you can set operational parameters to cap power consumption based on available solar power, but that's all for later.

- **RetpolineDrama** · [2023-03-13 18:12 UTC](https://news.ycombinator.com/item?id=35139941)
  This looks absolutely amazing, and I think you guys are going to win big here. ^c35139941

  My only concern is why the low SEER2? For a state of the art system like this I was expecting 22+

  I am hovering over the pre-order button regardless...

- **john\_cheapsms** · [2023-03-14 07:17 UTC](https://news.ycombinator.com/item?id=35148299)
  1\. App needs to be very responsive, probably should have some port exposed to communicate with it directly without cloud if needed. Using Samsung Air - Air solution, the app is just annoyingly slow.
  2\. Provide some basic API to start, stop the device, set the desired temperature.
  3\. Add some integration with weather forecast for the area - I would prefer to wait for couple hours for better efficiency.
  4\. You should not feel moving air.
  5\. By current solutions humidity is removed from air - try to address that. ^c35148299

- **disordinary** · [2023-03-14 06:21 UTC](https://news.ycombinator.com/item?id=35148026)
  I mean, they look better than your standard Mitsubishi or Panasonic heatpump, but other than cosmetics, what difference does this have from the normal sort of heatpumps that most homes have? ^c35148026

- **deedubaya** · [2023-03-13 21:41 UTC](https://news.ycombinator.com/item?id=35143226)
  I'm in the market for a heat pump in my home to replace electric forced air which is in a cold climate. It seems like this heat pump would work great for me, and being able to see pricing up front and self-order sounds awesome! ^c35143226

  I'm gonna be a no on purchasing tho. I don't want a smart thermostat that is not system agnostic. High risk of it bricking the system or not being upgradable, minimal reward when compared to all the other smart thermostat options.

  A heat pump manufacture that's trying to be a tech company? Nah.

- **zhyder** · [2023-03-13 20:19 UTC](https://news.ycombinator.com/item?id=35141902)
  You mentioned CO2 so I hope you're integrating active ventilation through an HRV or ERV. Integrated energy-efficient heating+cooling+filtration+ventilation is the holy grail for me. ^c35141902

- **tonyarkles** · [2023-03-13 18:03 UTC](https://news.ycombinator.com/item?id=35139784)
  Super interesting product! I've been chewing on this idea and market for a while (as a potential customer, primarily) but with a slight twist. Conventional heat pumps tend to fall back to resistive heating as things get colder; where I'm at in Canada, we routinely hit -40C/F in the winter and unfortunately this means that the efficiency is the worst when we need it the most. Your approach with the improved condenser is great but... any thoughts on how it would handle -40F? ^c35139784

- **mheat2** · [2023-03-14 20:42 UTC](https://news.ycombinator.com/item?id=35158198)
  Just bought a 2 head 28,000 BTU/hr mini split from Senville, a 2005 startup here in Quebec. Direct from company. They manufacture them in China. Rated for -22F. Factory direct, including installation kit and comprehensive install manual. Very responsive customer service. I'm a heating guy (wood burning masonry heaters), and my shop guy and I did the install ourselves. There's Quebec subsidies, etc., if you use a licensed installer, but doesn't matter to me. ^c35158198

- **mixdup** · [2023-03-13 17:36 UTC](https://news.ycombinator.com/item?id=35139315)
  The site is kind of sparse with specifics, this seems like a marketing ploy to people who don't know heat pumps exist or have existed for decades. Mostly marketed to people who think a gas furnace is the only option ^c35139315

  What do I get out of this \$10k, 24k btu system that I don't get in a \$4,695/36k BTU Mr Cool mini-split, or \$4,528/5 ton (\~60kbtu) ducted Goodman heat pump system?

  If you're going to be charging 2.5x per btu, you're probably going to need to explain why

- **drewm1980** · [2023-03-14 09:37 UTC](https://news.ycombinator.com/item?id=35149122)
  As a homeowner in the EU just starting an ecological home renovation, the biggest obstacle to heat pump adoption BY FAR is that you have to rip up your floors and install in-floor heating to deal with the lower warm-side operating temperature of heat pumps. At least that's what homeowners are being told here by tradesmen. Your two choices are to stay on natural gas or embark on a renovation that may end up costing as much as your entire house. ^c35149122

- **sleton38234234** · [2023-03-13 21:03 UTC](https://news.ycombinator.com/item?id=35142576)
  I already got a heat pump water heater and I love it!   I'm totally in the market for a heat pump heater to replace our Heater/AC.  the primary concern are three things: up front cost, and electricity costs for heating and 3) performance.  the last quote I got was about 11K, so that's pretty steep.  and on top of that heat pumps don't perform well for heating: it has to be on most of the time and will struggle to increase temps. ^c35142576

- **dgoodell** · [2023-03-13 23:24 UTC](https://news.ycombinator.com/item?id=35144707)
  Having industrial design and a nice webpage complete before there is any hardware at all seems like a major red flag to me. Who is actually going to manufacture this? ^c35144707

  - **cmui** · [2023-03-13 23:49 UTC](https://news.ycombinator.com/item?id=35145021)
    I would agree with you if there was major technical risk, but this is a system integration problem. Re manufacturing, there are millions of heat pumps made every year, and an ecosystem of contract manufacturers and thermal parts suppliers. ^c35145021

- **owlbite** · [2023-03-13 17:38 UTC](https://news.ycombinator.com/item?id=35139347)
  I'd love to upgrade to an electric heat pump, however being out in the urban-wild land interface of California, we're subject to occasionally multi-day power outages, for which having propane-based heating is a god-send in a winter storm.
  Offer an option to have propane-based backup heating element for such times would be a killer feature for us, as running electric-based heating probably kills our Tesla power walls in short order. ^c35139347

- **garyfirestorm** · [2023-03-13 17:29 UTC](https://news.ycombinator.com/item?id=35139176)
  The website lists 3 different sizes, but it doesn't say which one is recommended for a home of \$SqFt. Do I need a small or medium if my house is \~1100 sqft? ^c35139176

- **HPMOR** · [2023-03-13 18:19 UTC](https://news.ycombinator.com/item?id=35140060)
  Hi Chris, I’m an investor in Carrier Global the largest manufacturer of HVAC equipment. Curious on how you see your product differentiating yourself from their heat pumps, I.e superior specs? Also, I believe Carrier sells residential heat pumps directly to consumers through their service centers and also through large commercial deals, so not sure if your business model is strictly different than theirs. ^c35140060

- **odysseus** · [2023-03-13 19:59 UTC](https://news.ycombinator.com/item?id=35141618)
  I have a heat pump.  It works well, especially for air conditioning.  I only have 3 complaints: ^c35141618

  \* Fan is noisy (but at least that noise is confined to the outside)

  \* During ice storms, it ices up and I have to jam a stick through the grate to knock off the ice around the components inside.  (or the fan doesn't spin)

  \* Natural gas furnace backup (that comes when temps dip below freezing) heats the house considerably faster than the heat pump

- **throwway120385** · [2023-03-13 22:25 UTC](https://news.ycombinator.com/item?id=35143917)
  Let me know when I can buy one to install under my house in the crawl space. My house was built in the 30s before forced air was available and the ductwork is a retrofit because the crawl is almost big enough that I can stand up in it. We currently have a giant Rheem gas furnace and I'd love to replace it with an electric since they're no longer up to code as of this year. ^c35143917

- **soheil** · [2023-03-13 17:21 UTC](https://news.ycombinator.com/item?id=35139020)
  \> we have the industrial design and also largely understand how this will be built. The core technology risk is quite low, it's really about executing the scope well and also finding the right product that homeowners find compelling ^c35139020

  How many HN readers are going to read this and think why not give it a try myself? Is this really a deposit collector campaign or more of a competitor generator.

  - **UncleEntity** · [2023-03-13 18:24 UTC](https://news.ycombinator.com/item?id=35140144)
    \> How many HN readers are going to read this and think why not give it a try myself? ^c35140144

    I did but then saw what it cost — from the comments and not the website.

    I really want to get a heat pump for the “free” AC, lived in Phoenix too long I guess. The problem is (aside from not making Silicon Valley wages) justifying spending those prices on a house I got for \$15k.

    Well, and I’ve seen too many SV startups do a very bad job looking outside the bubble they live in and go away as soon as products end up in the hands of real people.

  - **cmui** · [2023-03-13 18:08 UTC](https://news.ycombinator.com/item?id=35139870)
    Heat pumps are really important for reducing fossil fuel use in homes, and we need better products. Scaling this sort of company has unique challenges, but it would be a net positive if more people build good products/services in this space. ^c35139870

    - **HEPA\_As\_Service** · [2023-03-13 18:23 UTC](https://news.ycombinator.com/item?id=35140128)
      The net positive is disrupting the space for emerging markets with the incent-er's rather clearly being focused AGAINST THAT. ^c35140128

      You are targeted away from INDIA etc. markets that are mainly cooling.  But I support your wanting to improve the thermostat for variable speed and also provide design room for the buyer into higher efficiency by oversizing and controlling accordingly.

      What bothers me is your premise that outdoor air can address indoor pollution.  You need to offer other filter case options and be drop in for new or existing construction leasing it to incent cost engineering pollution elimination in the lived in envelope.

      Also you should offer body climate control not just "air".  One company takes this seriously, for uncontrolled worker neck contact, and only leases!  Fujitsu does not even lease in Most english speaking or even European etc.  Handful of countries.

- **faromanc** · [2023-03-14 07:26 UTC](https://news.ycombinator.com/item?id=35148341)
  Awesome! How would this work for homes that require intense dehumidification? Where we live it reaches 99\% relative humidity every day of the year and you need multiple dehumidifiers around the house or a central dehumidifier connected to the furnace. Would a separate dehumidifier be able to connect to this system? Or would it be able to handle the dehumidification on its own? ^c35148341

  - **cmui** · [2023-03-14 07:44 UTC](https://news.ycombinator.com/item?id=35148441)
    The Electric Air system can provide a lot of dehumidification. For your specific situation dedicated dehumidifiers are probably the right solution, unless you need a fair amount of cooling in addition to the dehumidification. This is because for purely dehumidification you need some reheat after chilling the air to condenser water out. With a dedicated dehumidifier you get this for free from the condenser on the other side of your refrigeration cycle. In the Electric Air system the backup strip heaters provide the reheat in the air handler, but using them a lot is expensive. ^c35148441

- **kiddz** · [2023-03-13 19:14 UTC](https://news.ycombinator.com/item?id=35140935)
  Hey Chris. .  . given the novel nature of your product (it looks very sleek btw) and you're looking to gather feedback, maybe we can talk using askhumans.io to gather feedback at scale?  also, many years ago, I worked on compressed air energy storage on the demand side and we looked at co-generation opportunities to drive the caes turbines.  anyways, would love to connect. ^c35140935

- **seltzered\_** · [2023-03-14 03:28 UTC](https://news.ycombinator.com/item?id=35147038)
  I appreciate those trying to start in the HVAC space, while holding the many criticisms brought up in the other comments. ^c35147038

  I have a different take - what would it take to make a heat pump system as rebuildable and easily maintainable to last more than the 10year expected lifetime? You could price in options for a longer warranty akin what 'Speed Queen' does with their clothes washers.

- **alangibson** · [2023-03-14 09:50 UTC](https://news.ycombinator.com/item?id=35149219)
  I'd love to hear the VC case for this startup. I see a very late entrant, bringing no real product innovation, into a market with big established players. The only thing new I see is going D2C. But many others have commented how going D2C with this product makes no sense. ^c35149219

  And if D2C is the play, it would make far more sense to just rebadge an existing high-quality unit and sell that.

- **jcuenod** · [2023-03-13 17:05 UTC](https://news.ycombinator.com/item?id=35138724)
  Heat pumps were quite the rage in South Africa. Family members replaced their water heater ("geyser") with one, but I have not been impressed by the ability to heat water for baths and showers. ^c35138724

  @Chris, I guess that you would say that heat pumps vary in quality and ability. What sort of metrics should I use to assess the quality of the pump that I am buying to avoid buying a dud?

  - **Scoundreller** · [2023-03-13 17:10 UTC](https://news.ycombinator.com/item?id=35138810)
    There are even (somewhat weak at recovery) domestic water heaters that run off 120V for those replacing a gas water heater in North America and want to avoid the cost of new wiring/breaker/panels. ^c35138810

- **steviedotboston** · [2023-03-13 17:22 UTC](https://news.ycombinator.com/item?id=35139041)
  \> For homeowners switching from natural gas, the savings are usually 0-30\%, varying based on the local cost of electricity and natural gas. ^c35139041

  Yeah, that's gonna be a hard sell for lots of people. The majority of people with forced air (which is the target market) have natural gas. So the savings are potentially nothing, with a huge upfront cost for a new, untested startup product.

- **pgporada** · [2023-03-15 04:46 UTC](https://news.ycombinator.com/item?id=35164001)
  How does your heat pump system work with ERVs and HRVs that bring fresh air into the home directly for the blower in the furnace? How well do heat pumps work to remove humidity from spray foamed houses (rim joists, walls, attic) vs a regular AC unit? I suffer from high humidity after spray foaming my house and wish I could go back and undo it. ^c35164001

  Will this work in a 2550sqft house?

- **tgtweak** · [2023-03-13 21:20 UTC](https://news.ycombinator.com/item?id=35142909)
  Difficult market to jump into with Tesla openly saying they want to disrupt the heat pump/heating space with their established manufacturing and dealer/installer network.  They also have some significant IP in the heat pump space with their octovalve heat pump design which is being battle-tested and proven in one of the most hostile environments. ^c35142909

- **itissid** · [2023-03-13 19:57 UTC](https://news.ycombinator.com/item?id=35141578)
  Chris, I live in a high rise in a US city with only PTAC units\[1\]. The same unit provide both heating and cooling. Can this replace them? ^c35141578

  \[1\] [https://www.trane.com/Commercial/Uploads/Pdf/1129/ptac-svx01...](<https://www.trane.com/Commercial/Uploads/Pdf/1129/ptac-svx01c-en.pdf>)

  - **cmui** · [2023-03-13 20:38 UTC](https://news.ycombinator.com/item?id=35142187)
    A few options for you, if you have a viable mounting situation for the condenser (big if), you can use an Electric Air unit with wall unit. Otherwise you're best off with a drop in heat pump PTAC, or a heat pump window unit like Gradient. ^c35142187

- **unknown** · [2023-03-13 19:27 UTC](https://news.ycombinator.com/item?id=35141116)
  [deleted] ^c35141116

- **time4tea** · [2023-03-13 22:46 UTC](https://news.ycombinator.com/item?id=35144203)
  Seems expensive. I just got a \~13kW / \~45kbtu Mitsubishi Ecodan air/water plus new hot water tank etc for £10k (plus £5k government grant) ^c35144203

  No details on refrigerant and therefore GWP / F-gas that I could find.

  On the plus side (for you!), mitsubishi data/api/app sucks so bad, I can only imagine it is powered by EJB - there is so much potential upside there.

- **immy** · [2023-03-13 17:22 UTC](https://news.ycombinator.com/item?id=35139045)
  Doing some good work. Hope you find some investment or partnership with some trusted appliance names. Sounds like you'll be subbing out installation, I wish you luck building and protecting your brand reputation. ^c35139045

  I'm an edge case in Bay Area, don't have ducts, so looking at ceiling cassettes. I'll go learn about vapor injection compressors now.

  - **cmui** · [2023-03-13 17:59 UTC](https://news.ycombinator.com/item?id=35139716)
    Thanks for the support! Vapor injection is cool - if that's interesting look at some other novel architectures like cascade cycles, hot gas bypass, and internal heat exchangers. ^c35139716

- **barbazoo** · [2023-03-13 17:57 UTC](https://news.ycombinator.com/item?id=35139695)
  I really appreciate the transparent pricing. There is so much secrecy in the industry where I live (non-US) it seems, I get the feeling I'm supposed to be lured in before someone will actually tell me what it costs, even just the price of differently sized heat pumps, I'm not even talking about the variable cost of installation. ^c35139695

- **zorrobyte** · [2023-03-13 19:50 UTC](https://news.ycombinator.com/item?id=35141448)
  I installed my own Heat Pump (Pioneer) setup in my RV. I evacuated my system using a vacuum pump myself, total cost was around 3k. Got Home Assistant working through a hacked Local Tuya script. ^c35141448

  This unit is 22 SEER.

  \+1 for a LOCAL API that doesn't require the cloud and +1 for a self install. I can buy two whole higher efficiency Pioneer units for your \$6k install fee

- **SkyPuncher** · [2023-03-14 04:40 UTC](https://news.ycombinator.com/item?id=35147522)
  \> In addition the process of getting a heat pump is painful, including finding a trustworthy contractor, sorting out financing, and wading through rebates. ^c35147522

  Have you actually validated this?

  I got quotes a few years back for mini-split install. All heat-pump, from a large, reputable brand and the best installer in the area. Very close to the price you're asking.

  - **cmui** · [2023-03-14 04:48 UTC](https://news.ycombinator.com/item?id=35147569)
    It can be very regional, most of my specific discussions have been in the Northeast and the SF Bay Area. What area did you do this in? ^c35147569

- **bartislartfast** · [2023-03-13 18:04 UTC](https://news.ycombinator.com/item?id=35139806)
  \$14,000 is competitive with quotes I've seen for heatpumps. I've been quoted up to  €18,000 for a small retrofit. ^c35139806

  I would have expected the cost of heatpumps to have fallen as adoption goes up, like solar, but instead the opposite seems to have happened and they're far more expensive now than five years ago.

  Any insights into why this is?

  - **turtlebits** · [2023-03-13 18:29 UTC](https://news.ycombinator.com/item?id=35140230)
    Labor is extremely expensive.   The costs of heat pumps has fallen greatly.  I put in a 12k mini split in my house last year which cost \$850.  (The tools to DIY cost around \~\$150, but I've done 2 installs so far). ^c35140230

    - **bartislartfast** · [2023-03-20 14:33 UTC](https://news.ycombinator.com/item?id=35232056)
      is it difficult to DIY? ^c35232056

- **tony\_cannistra** · [2023-03-13 16:54 UTC](https://news.ycombinator.com/item?id=35138516)
  The holistic approach is nice to see. ^c35138516

  There are obviously already several major players in the industry (notably, Mitsubishi, but also more "DIY"-focused brands like "Mr. Cool") offering heat pump systems with air handlers, such as this.

  But this approach seems to be much more integrated in ways that actually might make a difference.

  - **cmui** · [2023-03-13 17:01 UTC](https://news.ycombinator.com/item?id=35138652)
    What I've observed is that getting a heat pump turns into a real science fair project for homeowners, and forget trying to integrate air quality in a good way. The proprietary communicating thermostats that come with heat pumps are really bad, and you can force an Ecobee or Nest to work with the heat pumps, but it hurts system efficiency by turning your variable speed equipment into less efficient fixed stage equipment. Lots of integration problems to be solved! ^c35138652

- **bythreads** · [2023-03-13 21:03 UTC](https://news.ycombinator.com/item?id=35142595)
  From a country where these are super normal:
  The air inside gets bone dry due to the hx and humidity of outdoors vs indoors. ^c35142595

  Its super unhealthy, but a good design avoids this by using either an entalpic(moisture permeable) hx or a rotor hx (humidity is controllable)

  If you really want to be different do this, not just a fancy cover and an api...

- **uoaei** · [2023-03-14 01:45 UTC](https://news.ycombinator.com/item?id=35146222)
  Remarkable reading through this comments section absolutely excoriating this business proposition. ^c35146222

  Really makes you question the authority that YCombinator carries in the startup space.

  I gotta say, most of the Launch HNs I witness do not seem to be addressing meaningful, valuable gaps in the market, except perhaps in the spreadsheet view...

- **gwbas1c** · [2023-03-13 19:05 UTC](https://news.ycombinator.com/item?id=35140790)
  What's the COP? ^c35140790

  There's just a vague 3-5x more efficient claim on your web site. More efficient than what?

  I currently have a 5-year-old 2.8ish COP whole house system that won't last forever. I get a monster bill in January and February, so when it's time to replace it, I'd like to go with something a bit more modern.

  - **cmui** · [2023-03-13 19:11 UTC](https://news.ycombinator.com/item?id=35140877)
    Good questions. A heat pump is 3-5 more efficient than any fossil fuel furnace. Fossil fuel furnace is 70-96\% efficient, heat pump is typically between 300-500\% 'efficient'. COP varies depending on the outdoor conditions, but you can infer COP at various temperatures by looking at the HSPF2 (heating season performance factor) which is the weighted average of the btu output/watt input at various outdoor/indoor conditions. ^c35140877

- **LastTrain** · [2023-03-13 21:29 UTC](https://news.ycombinator.com/item?id=35143043)
  How long will I own this before you start trying to squeeze more revenue out of me by locking up basic functionality? I mean, this isn't just Sonos, you could literally freeze people out! ^c35143043

  Seriously though, how is your system better than the heat pump that has been installed in my parents house since the mid eighties?

- **chociej** · [2023-03-14 05:08 UTC](https://news.ycombinator.com/item?id=35147650)
  I gather I'm the weirdo here, but I really \_don't\_ want a ducted heat pump, even though my conventionally-built 1950s home is currently full of ductwork for the two forced-air furnaces. I daydream frequently about tearing out all that sheet metal. Is a split system not wildly better somehow? ^c35147650

- **EngManagerIsMe** · [2023-03-13 23:17 UTC](https://news.ycombinator.com/item?id=35144619)
  I live in Seattle, which has *strict* noise requirements for heat pump units, and will absolutely ensure you are compliant. The electric air website mentions a db measurement, but it's not clear if that's the external or internal unit's noise level. Might be worth clarifying that. ^c35144619

  - **cmui** · [2023-03-14 00:58 UTC](https://news.ycombinator.com/item?id=35145782)
    The listed noise is for the outside unit. ^c35145782

- **beefman** · [2023-03-13 17:43 UTC](https://news.ycombinator.com/item?id=35139432)
  I have a 5400sqft house with 3 thermostats driving 3 natural gas furnaces and 2 air conditioners. System is loud, works poorly, and is expensive to operate. Outdoor temps from 30 - 110 degF. Can you help? ^c35139432

  I do not want the system connected to the internet.

  Currently paying \$0.36/kWh for electricity and \$2.80/therm for natgas.

- **quickthrower2** · [2023-03-13 21:33 UTC](https://news.ycombinator.com/item?id=35143117)
  \$22000 with install seems high. Got a ducted a reverse cycle air conditioner and an additional split reverse cycle air conditioner supply and install for about \$8k aud (us\$5k) 10 years ago so say us\$10k with inflation. Is this a competitive price. I don’t know btu but in total about 4kwh input. ^c35143117

- **yafbum** · [2023-03-14 04:21 UTC](https://news.ycombinator.com/item?id=35147417)
  Dumb question perhaps - I'm going to be shopping for an HVAC system for an area that needs heating in the winter and AC in the summer. Any chance that heat pumps can serve both cases? I mean, we're just compressing gas at one end and letting it expand at the other, right :-) ^c35147417

  - **cmui** · [2023-03-14 04:38 UTC](https://news.ycombinator.com/item?id=35147508)
    Not a dumb question, you've hit on one of the best features of these systems. They act as a heater in the winter and as AC in the summer. Same system. ^c35147508

- **uptown** · [2023-03-14 04:35 UTC](https://news.ycombinator.com/item?id=35147489)
  I wish some company would make more aesthetically pleasing ceiling cassette units suitable for residential use instead of the wall mounted mini-splits. Most cassettes are 24x24 which is great for commercial applications but a nonstarter for residential ceiling joist widths. ^c35147489

  - **kbuck** · [2023-03-14 16:40 UTC](https://news.ycombinator.com/item?id=35154291)
    MrCool has a DIY cassette that is designed to fit between residential joists: [https://mrcool.com/diy-ceiling-cassette/](<https://mrcool.com/diy-ceiling-cassette/>) ^c35154291

    No idea if it's any good though, and I don't really like the big logo and big black IR receiver.

  - **cmui** · [2023-03-14 04:44 UTC](https://news.ycombinator.com/item?id=35147549)
    Its an interesting idea. Install would be more expensive because you have to fit it nicely into the ceiling drywall and also snake refrigerant lines through the ceiling. Wall units typically have a hole drilled straight through the wall for condensate tubing and refrigerant line access. There's a wall unit on the Electric Air preorder site, thoughts on the aesthetics of that? ^c35147549

- **acyou** · [2023-03-14 04:30 UTC](https://news.ycombinator.com/item?id=35147467)
  Heat pumps are a mature and well adopted technology. Their efficiency and value will not be significantly improved. I have some ideas on how heat pumps could be turned into a more compelling offering. Improving the appearance and UI of the heat pump isn't on my list. ^c35147467

  - **cmui** · [2023-03-14 04:36 UTC](https://news.ycombinator.com/item?id=35147500)
    Thanks for your perspective. What do you think is needed to move the needle on heat pump adoption/ make them a more compelling product? ^c35147500

- **borski** · [2023-03-14 06:10 UTC](https://news.ycombinator.com/item?id=35147957)
  Here’s my big question: physical size of the pump. I have limited space for condensers outside due to the layout of the home, and the reason I haven’t put in a heat pump is due to none being physically sized small enough to replace our ACs (48k btu and 24k btu). ^c35147957

  Any word on dimensions?

  - **cmui** · [2023-03-14 07:19 UTC](https://news.ycombinator.com/item?id=35148307)
    My main worry for you would be clearance in front of the condenser. These are side discharging units and require 4ft clearance in front for the air exhaust stream. Rough foot print of the condenser - 36" x 15". ^c35148307

    - **borski** · [2023-03-14 07:41 UTC](https://news.ycombinator.com/item?id=35148420)
      That clearance may actually work, at least for one of them. The other one I could make work easily too. I’ll check the footprint. ^c35148420

- **cde-v** · [2023-03-14 02:45 UTC](https://news.ycombinator.com/item?id=35146723)
  This reminds me of the lady who tried selling ice melt she bought from China on Dragons Den (British Shark Tank). ^c35146723

  [https://www.youtube.com/watch?v\=Zns00EBWrWU](<https://www.youtube.com/watch?v=Zns00EBWrWU>)

  You seems like an unnecessary middleman with no value add.

- **friendzis** · [2023-03-14 08:03 UTC](https://news.ycombinator.com/item?id=35148547)
  \> I would love to hear your ideas, experiences, and feedback on any and all of the above! ^c35148547

  1\. Why would direct sale be regarded as a plus? I \*need\* a certified contractor to do the install for the warranty anyway, so instead of buying heat pump install I now have to buy heat pump and search for contractor separately?
  Even if this is somehow totally DIY-able device, I still need a contractor to do yearly service anyway. At the same time you would be targeting a population of DIYers with fully integrated product. Those are not really compatible. Whoever is doing product-market fit at your company should really reconsider their bubble.

  2\. Regarding thermostat, WTF. Per room thermostats are only useful if you can control individual circuits. I have never seen a residential ductwork with circuit control. You tune diffusers and forget. Now, even if you could control per circuit energy flow (which is usually a property of floor heating), in any modern house you would be looking at something like 2 degree difference between zero and max rooms at something like -15C outside. Look at offerings from e.g. Danfoss.

  3\. Claimed temperature gradients are weird. Are we talking about air source pumps? Modern R32 pumps barely handle -25C outside at MAYBE 1.0 CoP, but manage to heat DHW up to 50-60.

  4\. Brand. As far as I can understand you are considering building your own units? Do you have proven track record of intimate understanding of metallurgy and design behind modern scroll compressors? Your track record of working at Tesla does not inspire confidence. And even if it did, why would I buy your compressor instead of buying a product from trusted Daikin/Panasonic/Nibe? Not only I know that they make good (performant and reliable) products, but I can trust them more to exist when I need spare parts.

  5\. \> While we don't have any physical prototypes at the moment, we have the industrial design and also largely understand how this will be built. The core technology risk is quite low.

  Well... You do not have neither proven prototype nor proven process. And yet you already take preorders. This definitely does not inspire confidence that you intend to ship the best product possible. Sorry if that sounds harsh. Show me your pump achieving at least 1.0 CoP at -25 outside, at least +30 supply at minimum 70\% of nominal power.

  6\. Your value proposition seems to be better integration between heating unit, thermostats and HRV. What are your plans to support wider ecosystem? This sounds like a major lock-in requirement for the whole HVAC system.

- **schiffern** · [2023-03-13 22:47 UTC](https://news.ycombinator.com/item?id=35144217)
  Based on the location of the filter, it looks like the air return is supposed to come in... from the *bottom*? ^c35144217

  In most home unit I've seen, the return air duct connects on the *side*. Do you plan to offer anything in that configuration? Thanks!

- **obituary\_latte** · [2023-03-13 17:23 UTC](https://news.ycombinator.com/item?id=35139064)
  Does it explain somewhere that I missed how the different size units translate to sq. ft.? I would think that would be a great way to convey which size might work for people, but I might be missing some other factor that doesn't allow for that conversion? ^c35139064

  - **heatpumpfan** · [2023-03-13 17:31 UTC](https://news.ycombinator.com/item?id=35139218)
    Sizing heat pumps by the sq. ft. is hairy reasoning. Load calculations take into account climate zone, insulation, building materials, orientation, ceiling height, etc. Any recommendation based on 2D area is sketchy. For replacement of existing professionally installed systems, going by the capacity of the installed unit is a better shortcut. ^c35139218

    - **simplyaccont** · [2023-03-13 19:11 UTC](https://news.ycombinator.com/item?id=35140879)
      There is actually good reason to bump up capacity by half a ton to ton, unless currently installed unit was sized recently. The reason for this it's that design temperatures jumped up, sometime in a big way in a recent ashray published design conditions (and many companies don't even know that this is the case and use those from 10 years ago or more).
      And even the published  numbers tend to be off and they usually use one specific weather station in a region that may or may not have same weather as you. ^c35140879

      When I replaced hvac a couple of years ago, I retained company to make manual j calcuation as none of hvac contractors were willing to do it. I provided it with design temperatures that I calculated after scrapping data from a bunch of private weather stations in few miles radius

  - **cmui** · [2023-03-13 18:01 UTC](https://news.ycombinator.com/item?id=35139748)
    In the process of building out a tool that allows you to do just that on the website. You need some basic info about the home + a recent energy bill to do this. You can also go more bottoms up where you have all the geometric/thermal + air leakage properties of the home and the local weather, this is more involved. ^c35139748

    - **obituary\_latte** · [2023-03-13 20:02 UTC](https://news.ycombinator.com/item?id=35141669)
      Ah, very cool (LOL). Even if it's not totally accurate, getting a ballpark sense of what the costs might be would be huge. Thanks! ^c35141669

  - **simplyaccont** · [2023-03-13 18:25 UTC](https://news.ycombinator.com/item?id=35140166)
    it doesn't translate. there is a thing called "manual j" calculation, that take into consideration size of house, orientation, insulation, number of rooms. windows in each room, type of windows, appliances, a bunch of other parameters and then how many people live in house. topped of with required temperature inside during winter/summer and outside temperature during winter/summer.
    after this you get unit sizing ^c35140166

- **ddalex** · [2023-03-13 20:09 UTC](https://news.ycombinator.com/item?id=35141766)
  I have been thinking for a while on heat pumps, and I think your proposition here is golden ! It is an obvious sale to me if you put up the savings upfront, esp. for new builds. I live in a house warmed by heat pumps, and the magic of utility bills is great! ^c35141766

- **importantbrian** · [2023-03-14 14:07 UTC](https://news.ycombinator.com/item?id=35151756)
  I've seen a lot of heat pump hype lately but it's usually around heating your home, but I live in Florida. Is there any benefit to this for people in warm climates? My understanding is that the cooling part of an AC unit is already a heat pump. ^c35151756

- **solived** · [2023-03-13 22:14 UTC](https://news.ycombinator.com/item?id=35143768)
  Good on ya! This is a huge challenge, but sorely needed in the industry. How are you going about designing these systems? Do you have ducted options? HEPA filtration is not an end-all to indoor air quality, is there any consideration for ventilation? ^c35143768

  - **cmui** · [2023-03-13 22:27 UTC](https://news.ycombinator.com/item?id=35143950)
    We are primarily targeting ducted options. For us, air quality means manage particulate (PM2.5), CO2 with fresh air intake, and humidity in the home. ^c35143950

- **unknown** · [2023-03-18 18:36 UTC](https://news.ycombinator.com/item?id=35211837)
  [deleted] ^c35211837

- **lukepighetti** · [2023-03-13 17:46 UTC](https://news.ycombinator.com/item?id=35139496)
  I'm sniffing an air of "California syndrome" when it comes to HVAC products. The literature says 3-5x more efficient than my existing furnace. I believe that may be true in SF climate. But is it true where I live, in Northern Maine? ^c35139496

  - **shagie** · [2023-03-13 17:57 UTC](https://news.ycombinator.com/item?id=35139694)
    They're viable in Maine too. ^c35139694

    Heat pumps are defying Maine’s winters and oil industry pushback [https://wapo.st/3YK0hbC](<https://wapo.st/3YK0hbC>)

    From an (opinionated) Youtube channel out of the midwest (Chicago area which isn't known for being warm) - Why Heat Pumps are Immensely Important Right Now  [https://youtu.be/MFEHFsO-XSI](<https://youtu.be/MFEHFsO-XSI>)

    - **lukepighetti** · [2023-03-13 19:15 UTC](https://news.ycombinator.com/item?id=35140945)
      I'm not questioning if they are viable, I'm questioning the blanket claims and the direct comparison. What kind of furnace? Natural gas? Oil? A heat pump in Maine is not going to be 3-5x more cost effective than a natural gas furnace in Maine. In fact, it's currently more expensive than natural gas, and at parity with oil furnaces. [https://www.maine.gov/energy/heating-fuel-prices](<https://www.maine.gov/energy/heating-fuel-prices>) ^c35140945

      - **shagie** · [2023-03-13 19:48 UTC](https://news.ycombinator.com/item?id=35141423)
        [https://www.efficiencymaine.com/at-home/heating-cost-compari...](<https://www.efficiencymaine.com/at-home/heating-cost-comparison/>) ^c35141423

        And you can update the values there.  There are some approaches that are even more cost effective.

        I will also note on the url that you provided:

        \> Heat Pump Water Heater (HPWH) and Air Source Heat Pump (ASHP): Final fuel prices (i.e., far right column) reflect the increased efficiency of HPWHs and ASHPs. According to Efficiency Maine Trust and when compared to electric resistance heating, HPWHs are 2.98 times more efficient and ASHPs are 2.93 times more efficient. To obtain a theoretical and relative fuel price per unit, divide the price per kWh by 2.98 or 2.93 depending on your technology (e.g., \$0.2099 for an ASHP is like paying \$0.0716 for electric resistance heating).

        The numbers in the heating cost comparison roughly match the ones that you have.  A natural gas furnace can be as cost effective.  The point with the heat pump in part isn't the cost effective nature for the residential user - even if in parity, but that in addition to being similarly priced it is more environmentally sound to use a heat pump than to burn hydrocarbons for heat.

        The comparison that we're making above is also natural gas vs heat pump.  When you get the rural locations, natural gas isn't always an option and so then you need to change to the propane and heating oil versions.

        From the WaPo article:

        \> “Oh, hell no,” Casagranda said, when asked recently if she missed her propane furnace. As part of the experiment, the agency promised residents they could have their fossil-fuel-burning systems back if they didn’t like the results. So far, none of the homeowners have wanted to go back, according to agency officials, and Casagranda said she is more than satisfied.

        \> ...

        \> But oil’s market share is falling. Whereas 74 percent of the state’s homes relied on oil to keep warm in the winter of 2010, according to the Census Bureau’s American Community Survey, that figure had fallen to 60 percent by 2021.

        \> ...

        \> Despite the bitter cold, a drive up U.S. Route 1 reveals a quiet transformation underway with major implications for climate change. Mainers who have heated their homes, diners, libraries and churches with oil and propane for decades are turning to an alternative source of warmth.

        - **lukepighetti** · [2023-03-13 23:36 UTC](https://news.ycombinator.com/item?id=35144870)
          You may be educating others on this topic, but you're not educating me. No one runs resistive electric heaters in Maine. Is that common in California? Is that why the startup above is comfortable saying "it's 3-5 times more efficient than \[my\] current furnace?" ^c35144870

          Air source heat pumps are very popular here. We have two. They are great technology, but they are not a panacea. The majority of the electricity we generate comes from natural gas in New England because we don't have access to amazing renewables like is available in California. Also, they are a point heating source, so many folks who retrofit end up buying 3-4 of them to get full coverage in old poorly insulated homes. If the product above is \$12k, we're getting into \$36k-\$48k which is almost double the cost of installing a ground source heat pump which is vastly more efficient during the winter compared to an air source.

          This further proves my point: the startup above is clearly looking at this problem from a California context. They should get that under control immediately because the realities in the rest of the country will be shocking to them once they have to take customer calls outside their mediterranean climate.

- **kasdi** · [2023-03-18 18:37 UTC](https://news.ycombinator.com/item?id=35211852)
  I believe Elon repeatedly said that Tesla wanted to do heatpumps at some point too. ^c35211852

  As you were working at Tesla before, I'd be interested as to why you chose to go at it alone and what it would mean if Tesla entered the space as a competitor?

- **Empact** · [2023-03-14 04:51 UTC](https://news.ycombinator.com/item?id=35147584)
  I recommend getting connected with The BUILD Show\[1\] and/or the related BS\[2\] and Beer meetups, where you can reach forward-thinking builders. ^c35147584

  \[1\][https://youtube.com/@buildshow](<https://youtube.com/@buildshow>)

  \[2\]Building Science

- **anovikov** · [2023-03-13 18:24 UTC](https://news.ycombinator.com/item?id=35140145)
  3-5x is an exaggeration. Recent EU study put it at 1x-3x depending on the temperature outside, with \<1x or even inability to work at all at coldest temps (under -15C or so). Maybe 2x is a good average in practical use. Not 4x. ^c35140145

- **zhoujianfu** · [2023-03-13 17:58 UTC](https://news.ycombinator.com/item?id=35139713)
  I didn’t read everything you posted, but I’ve always also wanted “central humidity”… is that possible/feasible/does it already exist? ^c35139713

  I would like a fully electric central HVAC(H) system that keeps my house at 72F AND 50\% humidity.

  - **cmui** · [2023-03-14 01:32 UTC](https://news.ycombinator.com/item?id=35146113)
    Yep, definitely possible and done in this system. Depending on the details of your house + climate you will be limited on how high on humidity you can go in the winter. This is to prevent condensation in the structure. ^c35146113

- **londons\_explore** · [2023-03-13 18:00 UTC](https://news.ycombinator.com/item?id=35139744)
  Have you considered doing double-vapor injection? ^c35139744

  Ie. have a 2nd injection port on the compressor, and another valve and heat exchanger after the first?

  Software could then decide to use none, one, or two, depending on the desired heat output vs efficiency.

  - **cmui** · [2023-03-14 01:34 UTC](https://news.ycombinator.com/item?id=35146129)
    Haven't looked at that. Dictating compressor design requires some massive scale as a business, or taking on the design and manufacture yourself, which I wouldn't recommend to startups. Also, I suspect that increased vapor injection ports has diminishing returns (but I haven't done the calcs on it). ^c35146129

- **nightski** · [2023-03-13 21:13 UTC](https://news.ycombinator.com/item?id=35142761)
  This  is cool, but we just bought a very nice high end gas furnace and electric AC which was about \$8k installed in total.  I'd love a heat pump, but \$22k even after federal rebates?  That's kind of crazy. ^c35142761

- **carom** · [2023-03-14 08:54 UTC](https://news.ycombinator.com/item?id=35148855)
  I am really interested in HRV/ERV systems as well. Managing CO2 levels in the house has greatly improved my quality of life. Main issue is bringing in cold air in the winter when trying to control levels. ^c35148855

- **arein3** · [2023-03-14 15:44 UTC](https://news.ycombinator.com/item?id=35153376)
  If you want to do this right, use open protocols and open source the software. There is no reason not to (the software here is basic, the main product is the unit), except malicious intent from the seller. ^c35153376

- **yencabulator** · [2023-03-13 21:34 UTC](https://news.ycombinator.com/item?id=35143123)
  \> The system operates at all temperatures. Thanks to vapor injection technology the condenser is rated to -15F, and the backup heating strips can operate at all outdoor temperatures. ^c35143123

  I call bullshit. Demonstrate a unit at the south pole if you disagree.

  The heating strip can operate at all outdoor temperatures perhaps -- it's just a heating strip! -- but that doesn't necessarily make the rest of the system work. Your -15F figure is warmer than what existing products claim, so you're underperforming competition there, yet trying to boast about being superior.

  Similarly, the cooling part can only work when you still can dump heat outside.

  Established manufacturers state ranges like -22..86F/-25..30C for heating and -22F..122F/-30..50C for cooling. You trying to say "all" is just a lie.

- **karmicthreat** · [2023-03-13 19:39 UTC](https://news.ycombinator.com/item?id=35141279)
  This product doesn't really have much oomph without integrating with other appliances. If this was combined with other equipment like a water heater and heat recovery it would be a much better value. ^c35141279

- **ericzawo** · [2023-03-14 04:40 UTC](https://news.ycombinator.com/item?id=35147527)
  Just chiming in to say your company's website is really well done. ^c35147527

  - **cmui** · [2023-03-14 04:45 UTC](https://news.ycombinator.com/item?id=35147550)
    Thanks! ^c35147550

- **swayvil** · [2023-03-13 17:52 UTC](https://news.ycombinator.com/item?id=35139604)
  My first thought is, "how often will it break"? I don't even care if there's a warranty. I just want it to do its job for 10 years straight without a blip. ^c35139604

- **mderazon** · [2023-03-13 23:24 UTC](https://news.ycombinator.com/item?id=35144696)
  Sou these heat pumps are for ducted systems... What about homes that have water wall radiators or underfloor heading? Are these systems considered air to water heat pumps? ^c35144696

  - **cmui** · [2023-03-13 23:38 UTC](https://news.ycombinator.com/item?id=35144895)
    Great question, for that type of system, you can either do a mini-split install which Electric Air could support, or an air to water heat pump which would still utilize your existing wall radiators or radiant (underfloor) heating. ^c35144895

- **egillie** · [2023-03-13 16:47 UTC](https://news.ycombinator.com/item?id=35138359)
  This is fantastic timing with natural gas prices skyrocketing! ^c35138359

- **jaequery** · [2023-03-14 02:14 UTC](https://news.ycombinator.com/item?id=35146457)
  Does this do air conditioning too or just heating ? ^c35146457

  And would this be allowed for condominiums? HOA recently rejected our attempt to go all electric because the equipment wouldn’t fit.

- **ccamrobertson** · [2023-03-13 21:06 UTC](https://news.ycombinator.com/item?id=35142656)
  Congratulations on the launch! ^c35142656

  Would it be possible to combine both a ducted system with a mini-split style head unit? Our ducting is old, undersized and with poorly located returns.

  - **cmui** · [2023-03-14 01:27 UTC](https://news.ycombinator.com/item?id=35146072)
    Yep, this should be possible. ^c35146072

- **kazinator** · [2023-03-13 18:12 UTC](https://news.ycombinator.com/item?id=35139931)
  Of course you sell to homeowners; otherwise you'd have to get a distributor (e.g. Home Depot) to carry the product. ^c35139931

  This is not a feature; it's just how you have to hustle.

- **ARandomerDude** · [2023-03-14 03:13 UTC](https://news.ycombinator.com/item?id=35146933)
  Heat pumps are extremely common in the south. Those prices are outrageously high though. I think I’ll just call the local HVAC guy next time I need a new system. ^c35146933

- **sizzle** · [2023-03-14 02:54 UTC](https://news.ycombinator.com/item?id=35146784)
  My crappy coil keeps leaking every odd year and the refrigerant cost so much to replace. I hate the thin coils being created nowadays, not built to last at all. ^c35146784

  - **cmui** · [2023-03-14 03:00 UTC](https://news.ycombinator.com/item?id=35146829)
    Indoor or outdoor coil, copper tube-and-fin or aluminum microchannel? ^c35146829

    - **sizzle** · [2023-03-15 05:32 UTC](https://news.ycombinator.com/item?id=35164307)
      Indoor copper in the attic, the typical warrantied coils but they don’t cover recharging refrigerant ^c35164307

- **vinaypai** · [2023-03-14 01:41 UTC](https://news.ycombinator.com/item?id=35146194)
  I don't see how this is different from any number of heat pump systems out there except that your product doesn't exist yet, and your competitors do. ^c35146194

- **stevelacy** · [2023-03-13 17:39 UTC](https://news.ycombinator.com/item?id=35139358)
  Is this designed for new home builds or remodel/retrofits? There would be a major cost difference between demo/prepping a retrofit over a new build. ^c35139358

  - **cmui** · [2023-03-13 17:44 UTC](https://news.ycombinator.com/item?id=35139443)
    We're primarily targeting remodel/retrofits as a market, but you could certainly use this in a new build. ^c35139443

- **mrexroad** · [2023-03-13 20:06 UTC](https://news.ycombinator.com/item?id=35141722)
  Request: Allow homeowners to self install without voiding warranty. Some of us here can sweat/flare copper, vac test and flush lines just fine. ^c35141722

- **debacle** · [2023-03-13 19:47 UTC](https://news.ycombinator.com/item?id=35141400)
  I saw a comment about demand response below. ^c35141400

  You don't opt your residential hvac into demand response unless you want to freeze. Juice is not worth the squeeze.

  - **cmui** · [2023-03-14 01:35 UTC](https://news.ycombinator.com/item?id=35146135)
    Up to homeowners to decide how much energy optimization they want. You can easily enable/disable DR as a homeowner. ^c35146135

- **swyx** · [2023-03-13 23:40 UTC](https://news.ycombinator.com/item?id=35144926)
  just commenting to say HECK YES to YC startups actually doing literally anything other than building B2B SAAS. congrats on being truly contrarian. ^c35144926

  - **cmui** · [2023-03-13 23:42 UTC](https://news.ycombinator.com/item?id=35144952)
    Thanks for the support! ^c35144952

- **soheil** · [2023-03-13 17:15 UTC](https://news.ycombinator.com/item?id=35138894)
  I very much get the vibe of a Kickstarter campaign. Is YC advising its startups to go that route more and more now that the VC money has dried up? ^c35138894

- **vl** · [2023-03-13 23:29 UTC](https://news.ycombinator.com/item?id=35144772)
  Looks like first direct-to-consumer ad of this kind on HN! ^c35144772

  It's interesting how much HN community goodwill can be stretched to bend for Y Combinator.

  - **cmui** · [2023-03-13 23:31 UTC](https://news.ycombinator.com/item?id=35144798)
    What do you think of the product? ^c35144798

    - **vl** · [2023-03-13 23:54 UTC](https://news.ycombinator.com/item?id=35145071)
      I generally like the product as described, but definitely there are tricky challenges for you, and no-product launch at HN is perhaps a bit premature. (You can't do a launch like this on HN, you need to hype it up in the media and then to it a-la Tesla). ^c35145071

      As specifically for the product:

      All-electric is no-go in many locations. I live in the (outside) Seattle suburb, electricity goes out few times in the winter. In this case I can still heat from the gas running controls from the generator. I.e. back-up furnace is an important add-on.

      It's unclear what is your production strategy: if you repackage existing devices with better software and integrations, then it's a viable option since repairs can be reasonably done (i.e. I had control board on the AC unit replaced in a day and failed water heater replaced in 3 days). If you produce new hardware, then it's hard to justify: when it fails in the winter, what exactly is the repair plan?

      In addition to that ducted heat pump with smart controls is not exactly a new concept, I can buy one right now. It looks like yours is going to be integrated with better sensors, humidifier and ERV? Are they part of the system? Are they separate install?

- **tikkun** · [2023-03-13 18:03 UTC](https://news.ycombinator.com/item?id=35139790)
  Related: [https://calv.info/heat-pumps](<https://calv.info/heat-pumps>) ^c35139790

- **sirtimbly** · [2023-03-14 02:01 UTC](https://news.ycombinator.com/item?id=35146352)
  Yes yes! One million times yes! Shut up and take my money. ^c35146352

  \$4K lower than a quote from a local contractor for a less capable system.

- **m1sta\_** · [2023-03-14 00:35 UTC](https://news.ycombinator.com/item?id=35145523)
  Q. What issues have you had with your existing heat and cooling? ^c35145523

  A1. Installation cost and complexity

  A2. Physical size of installed components

  A3. Noise

  A4. Aesthetics if non-ducted

  - **cmui** · [2023-03-14 00:39 UTC](https://news.ycombinator.com/item?id=35145571)
    Thanks for the feedback! What type of system do you have today, and if you're ok sharing, what part of the world are you in? ^c35145571

- **caeril** · [2023-03-13 21:19 UTC](https://news.ycombinator.com/item?id=35142863)
  Very confused about this. How is it any different from any other high-SEER heat pump currently on the market? ^c35142863

- **sidcool** · [2023-03-14 00:11 UTC](https://news.ycombinator.com/item?id=35145265)
  I am not a target customer for the product.  Just came here to congratulate you on launching. And good luck! ^c35145265

  - **cmui** · [2023-03-14 00:13 UTC](https://news.ycombinator.com/item?id=35145292)
    Thanks for your support! What do you use for heating and cooling today? ^c35145292

- **Eumenes** · [2023-03-13 18:49 UTC](https://news.ycombinator.com/item?id=35140518)
  i'm glad to have a wood stove, electrical rates keep rising, and wood is pretty consistent (plus I source some on my own, tons of free firewood if you know where to look) ... unfortuantely it doesnt solve my hot water problem, but one 200 gallon tank of oil lasts me over 1.5 years ^c35140518

  - **cmui** · [2023-03-14 00:03 UTC](https://news.ycombinator.com/item?id=35145186)
    Have you looked at the relative cost of wood + fuel oil vs a heat pump. I think you'd be surprised how quickly it pays off. ^c35145186

    - **Eumenes** · [2023-03-14 13:09 UTC](https://news.ycombinator.com/item?id=35150850)
      If anything I'd get a heat pump to supplement my wood stove, but I'd like to have solar first, because the electrical rates are very high and have friends who have installed heat pumps to only trade expensive oil bills for \$400-500/month electric bills. I do like the dual purpose with air conditioning. Your product is attractive, way more than the ones I've seen out there, and I think that'll be a good selling point. Best of luck! ^c35150850

- **jasonmarks\_** · [2023-03-13 20:52 UTC](https://news.ycombinator.com/item?id=35142389)
  UV lights as an extra disinfectant inside the furnace around the filter would look heckin' smart ^c35142389

  - **cmui** · [2023-03-14 01:44 UTC](https://news.ycombinator.com/item?id=35146211)
    Yeah, definitely aware of this tech, and its often found in commercial applications. Probably overkill for residential stuff though, HEPA is already very good. ^c35146211

- **cultureulterior** · [2023-03-14 04:05 UTC](https://news.ycombinator.com/item?id=35147314)
  I'm interested, but not ready to preorder. Please add a mailing list that I can sign up to? ^c35147314

- **fridder** · [2023-03-13 19:06 UTC](https://news.ycombinator.com/item?id=35140814)
  I have a very tightly insulated house so I have an ERV. Does your system integrate with ERVs? ^c35140814

- **timzaman** · [2023-03-14 03:21 UTC](https://news.ycombinator.com/item?id=35146982)
  Pretty sure you need a mechanical permit for this in SF. So easier to get that installer. ^c35146982

- **michpoch** · [2023-03-13 22:48 UTC](https://news.ycombinator.com/item?id=35144228)
  It is not really clear / mentioned anywhere - are the sales limited just to the USA? ^c35144228

  - **cmui** · [2023-03-13 23:05 UTC](https://news.ycombinator.com/item?id=35144447)
    Great call out, USA sales only for now. ^c35144447

- **Denzel** · [2023-03-13 18:52 UTC](https://news.ycombinator.com/item?id=35140583)
  The value prop on this is unbelievable. I've been trying to get an affordable whole home heat pump system for over a year now. ^c35140583

  You've explained the problem space, the solution, and why your background is relevant, extremely well. Kudos. I put a preorder in.

  Minor nit: the grey on white on your preorder page is practically unreadable for my eyes.

  - **cmui** · [2023-03-14 01:48 UTC](https://news.ycombinator.com/item?id=35146249)
    Thank you for pointing that out - just fixed it! ^c35146249

- **politician** · [2023-03-13 18:03 UTC](https://news.ycombinator.com/item?id=35139776)
  How do you envision the installation working in the direct-to-consumer sales model? ^c35139776

  - **cmui** · [2023-03-13 18:42 UTC](https://news.ycombinator.com/item?id=35140422)
    Similar to solar. We connect you with a contractor to do a site visit, provide final quote and ultimately do the install. ^c35140422

- **geor9e** · [2023-03-14 00:20 UTC](https://news.ycombinator.com/item?id=35145365)
  \>wall unit heats and cools homes without ducts. ^c35145365

  In my house we follow the laws of thermodynamics.

- **davidmurdoch** · [2023-03-14 01:45 UTC](https://news.ycombinator.com/item?id=35146220)
  \> a delightfully uniform temperature in each room. ^c35146220

  You'd need programmable vents for that.

  - **cmui** · [2023-03-14 01:52 UTC](https://news.ycombinator.com/item?id=35146283)
    We could be more clear on that claim. Temp variation within a room - ducted variable speed equipment solves this well. Temp variation between rooms - either need zoned dampers, programmable vents like Flair, or ductless units controlling each zone. ^c35146283

- **m1sta\_** · [2023-03-14 00:39 UTC](https://news.ycombinator.com/item?id=35145567)
  Can the wall unit be installed vertically, under a bed, or behind a headboard? ^c35145567

  - **cmui** · [2023-03-14 00:40 UTC](https://news.ycombinator.com/item?id=35145586)
    Vertically, no, would mess up condensate return path. Not recommended under a bed or behind a headboard either, you ideally want it high up on a wall so it has the best chance of mixing its supply air with the rest of the room. ^c35145586

- **larsiusprime** · [2023-03-14 04:29 UTC](https://news.ycombinator.com/item?id=35147463)
  Please make it so that I don't have to use an app to interface with it. ^c35147463

- **spennino** · [2023-03-13 17:07 UTC](https://news.ycombinator.com/item?id=35138768)
  great to see someone take a holistic approach here. heat pumps are imperative to moving off fossil fuels and it's crazy how difficult it is to get these devices installed in homes right now. ^c35138768

- **TruthWillHurt** · [2023-03-14 10:25 UTC](https://news.ycombinator.com/item?id=35149432)
  Sooo... it's an airconditioner.  
  Welcome to the 20th century YC! ^c35149432

- **Melatonic** · [2023-03-13 23:36 UTC](https://news.ycombinator.com/item?id=35144864)
  Does this REQUIRE the use of a smartphone and the app? Or can it be controlled from the unit itself? ^c35144864

  Generally I hard pass on any device that does not have at least some basic manual controls itegrated into the unit itself (or an offline dedicated controller perhaps that wires to it). A phone app is great for controlling things away from home or setting up more advanced features like schedules and alarms but especially for a home appliance that is meant to last a long time (with installation costs) the last thing I want is reliance on a mobile device.

  My ideal version of this in order of most important to least important:

  1\. Oldschool hardware thermostat / control knob (rotary knobs are cool and very reliable long term!) built into the thermostat itself or a port on the unit itself to wire up one of these also sold by the same company. If the unit requires a bit of intelligence to run the heat pump properly from a simple thermostat and control knob then that would be needed to be integrated into the firmware itself of the unit (or the hardware thermostat / knob).

  2\. Modern support for WiFi or Ethernet and fancy features through an app that communicates directly with the unit while on the home network or through the Cloud while away (Cloud could have additional features). API access is always cool for the nerds + easy GUI with visual programmable features for the power users that are not programmers.

  3\. Included instructions that any competent electrician can follow if any additional electrical wiring is needed (say if wires need to be a thicker guage or there needs to be more than 2 or if certain aftermarket thermostats need special wiring)

  4\. Easily replaceable filter by the end user + physical reset button built into the unit itself (in case some kind of protection is tripped). And ideally also a few easily user accessible parts (say like replacing a fuse or relay). The more standardized parts the better (such as filter sizes).

  5\. Guarantee certain number of years of updates (and phone version compatiblities) and also try to guarantee backwards compatiblity (in some way) with older devices (to some extent).

  6\. When the app / software finally does cease to be updated release either source code or some way for third parties to continue work customizing / updating the system for old or newer devices or niche systems.

  7\. Dedicated smart device or remote made specifically to work with this that provides all of the functions the phone app does but in a very simple to use, reliable way. This could be a stripped down android device (could be a very cheap model) or something more like an oldschool remote control with physical buttons and a simple black and white tiny OLED.

  - **cmui** · [2023-03-13 23:41 UTC](https://news.ycombinator.com/item?id=35144943)
    No problem if you don't want to use an app, just use the thermostat. The system runs fine without internet connectivity. What you get with a wifi connection is the thermostat can access signals that increase system efficiency (demand response, weather, TOU rates) and you get remote commands from your smartphone. ^c35144943

- **hdhdjdjd** · [2023-03-14 00:30 UTC](https://news.ycombinator.com/item?id=35145468)
  All good, but preorder page only lists \$100 and not a full cost. ^c35145468

  - **cmui** · [2023-03-14 00:32 UTC](https://news.ycombinator.com/item?id=35145497)
    Pricing on the main product page. In the future I'll link to pricing from the preorder page as well. Been answering comments all day so no time to change yet! ^c35145497

- **brianjoseff** · [2023-03-13 17:53 UTC](https://news.ycombinator.com/item?id=35139622)
  looks very cool. consider putting estimated savings in the pricing area too. similar to solar where big upfront cost but amortization prob makes it relatively cheap! ^c35139622

- **rad\_gruchalski** · [2023-03-13 19:18 UTC](https://news.ycombinator.com/item?id=35140994)
  Interesting, you accept preorders from anywhere in the world? ^c35140994

- **surfmike** · [2023-03-13 21:13 UTC](https://news.ycombinator.com/item?id=35142766)
  Why not also have a way to integrate with Nest, ecobee, etc? ^c35142766

- **camillomiller** · [2023-03-14 10:43 UTC](https://news.ycombinator.com/item?id=35149527)
  Hey, what's your take on Thermo-Acoustic heat pumps? ^c35149527

- **steponlego** · [2023-03-13 23:15 UTC](https://news.ycombinator.com/item?id=35144582)
  Where's your product made? Is it a US built product? ^c35144582

- **muhammadusman** · [2023-03-13 21:12 UTC](https://news.ycombinator.com/item?id=35142756)
  Does this include an integration with Matter or Thread? ^c35142756

- **unknown** · [2023-03-13 23:03 UTC](https://news.ycombinator.com/item?id=35144413)
  [deleted] ^c35144413

- **antoineMoPa** · [2023-03-13 18:51 UTC](https://news.ycombinator.com/item?id=35140568)
  The design looks pretty good! The Apple of heat pumps? ^c35140568

- **tomcam** · [2023-03-13 19:35 UTC](https://news.ycombinator.com/item?id=35141235)
  \> There’s a big push to end fossil fuel use in US homes by electrifying all end-uses ^c35141235

  If all end uses are electrified, where does  that electricity come from if not fossil fuel in large part?

  - **afterburner** · [2023-03-13 19:39 UTC](https://news.ycombinator.com/item?id=35141278)
    Solar and wind prices are extremely low and still dropping. They are already cheaper than other newly built options. Coal plants have been shutting down, natural gas is now way more expensive, nuclear can't build soon enough or cheap enough. ^c35141278

    The transition in generation is happening too.

    - **tomcam** · [2023-03-13 20:06 UTC](https://news.ycombinator.com/item?id=35141708)
      Solar and wind do not come close to handling peak loads right, especially when the weather doesn't cooperate. ^c35141708

      - **afterburner** · [2023-03-14 01:20 UTC](https://news.ycombinator.com/item?id=35146005)
        Batteries and dams can be used to store energy. It doesn't have to be sunny and/or windy all the time. Excess generation capacity takes care of the issue. ^c35146005

        Regardless, burning natural gas for heat is burning 100\% fossil fuels for heat, while electricity is not generally generated 100\% by fossil fuels. Using electricity is still a huge improvement even now. And if you're using baseboard heating (electric), heat pumps are way more efficient.

        - **tomcam** · [2023-03-14 03:34 UTC](https://news.ycombinator.com/item?id=35147100)
          If batteries and dams are so effective, why were Germany and Texas caught off guard during the last few years? ^c35147100

          - **afterburner** · [2023-03-14 08:28 UTC](https://news.ycombinator.com/item?id=35148693)
            Wow, this says everything I need to know about you. You are arguing in incredibly bad faith. ^c35148693

            Germany? What the natural gas thing? They heavily relied on it through building up gas heating and then they had to embargo Russia due to their invasion of Ukraine. You can't replace all German homes with heat pumps overnight, and they hadn't even started until the war started.

            Texas? They refuse to winterize their energy grid against winter weather and have repeatedly suffered failures over the last couple decades when they get an bad winter storm. Note that the biggest parts of the grid that failed were natural gas power generation. They are also not connected to the rest of the US grids which could have helped, because they don't want to be federally regulated, because they don't want to spend money to winterize their grid.

            Now, what does that have to do with dams and batteries? Absolutely nothing. It's just fossil fuel generation failing thanks to regressive policy. You realize you have to build the new power generation before you can blame it right?

            Nice try.

            Don't worry, I don't have to convince you. Solar and wind will get so cheap even stubborn regressives will want to build it. Only the fossil fuel companies will resist. I guess maybe you work for one?

            - **tomcam** · [2023-03-14 09:21 UTC](https://news.ycombinator.com/item?id=35148998)
              Didn’t mean to trigger you. Sorry. The point I’m making is that no matter how cheap solar and wind are, with electric cars increasing in popularity, usage is getting more and more lopsided. The network just cannot deal with peak loads, especially in places with harsh winters. Solar and wind are pretty useless at night or when there’s no wind, which is a lot of the time. And thanks for the detailed answer! ^c35148998

              - **afterburner** · [2023-03-14 21:34 UTC](https://news.ycombinator.com/item?id=35159144)
                "The network just cannot deal with peak loads" ^c35159144

                It can if it gets upgraded. Which is happening.

                "Solar and wind are pretty useless at night or when there’s no wind"

                Did you forget about the batteries already? And are you forgetting that power grids operate on a continental level? Your power doesn't have to come from next door.

  - **exicer** · [2023-03-13 19:45 UTC](https://news.ycombinator.com/item?id=35141381)
    Yeah this is only necessary, not sufficient! What a dumb idea. ^c35141381

- **abakker** · [2023-03-13 17:24 UTC](https://news.ycombinator.com/item?id=35139082)
  Also - is this going to be R410a, or R32? ^c35139082

  - **cmui** · [2023-03-13 18:05 UTC](https://news.ycombinator.com/item?id=35139816)
    Great question - this will be R454B (GWP 467) vs R410A (GWP 2000) and R32 (GWP 675). GWP is global warming potential, the relative emission factor of a substance relative to CO2. ^c35139816

- **RomanPushkin** · [2023-03-14 04:21 UTC](https://news.ycombinator.com/item?id=35147419)
  Heat control with a touch screen? Never. ^c35147419

  - **cmui** · [2023-03-14 06:01 UTC](https://news.ycombinator.com/item?id=35147916)
    What's your preferred thermostat? ^c35147916

    - **RomanPushkin** · [2023-03-14 20:19 UTC](https://news.ycombinator.com/item?id=35157801)
      With physical buttons [https://www.amazon.com/HoneyWell-T498B1512-Electric-Voltage-...](<https://www.amazon.com/HoneyWell-T498B1512-Electric-Voltage-Thermostat/dp/B000LDFSV2/>) ^c35157801

- **thegrizzlyking** · [2023-03-14 05:10 UTC](https://news.ycombinator.com/item?id=35147661)
  Whats the monthly subscription on this? ^c35147661

- **benben613** · [2023-03-13 16:57 UTC](https://news.ycombinator.com/item?id=35138566)
  Any idea what the pricing will be like? ^c35138566

  - **tony\_cannistra** · [2023-03-13 16:58 UTC](https://news.ycombinator.com/item?id=35138589)
    There is a pricing section on the website. ^c35138589

- **dirtyoldmick** · [2023-03-14 00:51 UTC](https://news.ycombinator.com/item?id=35145711)
  I'll stick to natural gas. ^c35145711

- **sabujp** · [2023-03-14 04:07 UTC](https://news.ycombinator.com/item?id=35147328)
  this is too expensive, i'm not paying more than \$5k for a new hvac unit ^c35147328

- **globalnode** · [2023-03-14 09:58 UTC](https://news.ycombinator.com/item?id=35149277)
  this has been at the top of hn all day :( ^c35149277

- **jpease** · [2023-03-14 01:36 UTC](https://news.ycombinator.com/item?id=35146142)
  \$20k… lol. No. ^c35146142

- **princeharry86** · [2023-03-13 23:06 UTC](https://news.ycombinator.com/item?id=35144462)
  What are the chances that TESLA will enter the market as Elon Musk has previously mentioned deep interests in Home heating/cooling before ^c35144462

- **mikebreac** · [2023-03-14 06:25 UTC](https://news.ycombinator.com/item?id=35148050)
  Google.com ^c35148050

- **robomartin** · [2023-03-13 20:10 UTC](https://news.ycombinator.com/item?id=35141784)
  A lot to unpack here. ^c35141784

  First, I tend to react badly to the usual SCV "We are going to disrupt \<XYZ\>" when there's nothing wrong with \<XYZ\>.

  The current policy-driven push for heat pump systems is, at best, nonsensical.

  Why?

  Just speaking of the US (and guessing it might be the same in other regions) the power grid and power generation capacity are already stressed to the point where, in places like CA, power outages and having the governor ask electric vehicle owners not to charge their cars are a thing.

  Now we want to push 80 million homes to ADD, not remove, electrical demand to the tune of kilowatts per home, in the name of efficiency?

  This is deeply misguided.  We need to get serious about upgrading our power generation and distribution systems before adding non-trivial demand.

  Current estimates are that we need to double our power generation and transmission capacity to be able to support electric cars.  Going with an electric heat-pump based system for cooling and heating means having the potential to add somewhere in the range of 3 kW to 6 kW or more of nearly steady-state load for 6 to 12 hours to tens of millions of homes.

  While it is never a good idea to apply averages to this kind of analysis, if I were to do the math for the endpoints, we are talking about 240 GW to 480 GW of new power demand for 80 million homes going electric.  That is nothing even close to trivial.

  For context, a nuclear power plant is typically rated at 1 GW.  This means we might need somewhere between 240 and 480 new nuclear power plants to support full electrification of our heating and cooling systems.  And we are not even talking about large commercial buildings, hotels, etc.

  Add that to the 1200 GW deficit for full electrification of ground transportation and we quickly approach a requirement for over 1500 new 1GW nuclear power plants.

  No.  You cannot do this with solar.  You cannot do this with solar and wind combined.  These technologies are not reliable.  Under the best of conditions they might be able to reach 80\% reliability.  Another way to say it is that towns and cities will go dark 20\% of the time without having 100\% backup systems.

  In other words, the energy story on this (not the startup, but rather the idea of placing all of our eggs on the magical electric-power-will-save-the-world basket) isn't good at all.

  As far as the startup itself.  I know there are first adopters out there who might jump on something like this.  I am a first adopter of many technologies.  I have spent a thousand dollars on 3D printers that turned out to be crap.  Not a big deal.  When it comes to my home, no, sorry.  Not going to happen.

  First of all, your company is a YC funded startup with no manufacturing history or infrastructure whatsoever.  Sorry, this isn't like making smart watches.  What you are going to do is come-up with a design, go to a company in China and make something.  A unicorn.  Your design will change based on what that company already makes.  It will be, for the most part, not much different internally than what Carrier and other companies make.

  The difference is that companies like Carrier have been around forever.  They can stand behind their product and I can be assured they --and the extended support infrastructure that knows their product-- will be around for decades.  You are one bank failure or investor decision away from being out of business.

  Others may think differently, of course.  In my case, there is no way I am going to spend tens of thousands of dollars on a unicorn that nobody will want to touch of maintain.  I saw a post from someone in France who cannot get their heat-pump system serviced.  That's a reality in the US if one installs something your local service infrastructure has never seen or isn't interested in dealing with.

  Another consideration: Installing a no-name system in a home can have negative consequences when it comes time to sell it.

  HEPA, air quality, smart thermostat, API's, cloud, etc.  Yeah, no, not interested.  As someone else said, a contact closure is all you need and want.  No air conditioning maintenance guy is going to show up with a laptop to connect with your A/C unit via SSH.

  Air filtering is easy and cheap.  Depending on how you want to do it, it can, quite literally, cost less than \$100 to have excellent filtering.  I recently experimented with building a couple of these:

  [https://en.wikipedia.org/wiki/Corsi\%E2\%80\%93Rosenthal\_Box](<https://en.wikipedia.org/wiki/Corsi%E2%80%93Rosenthal_Box>)

  I used 20 x 30 inch tall filters, which don't cost much more than 20 x 20's.  The result was super-cheap high-performance filtration with measurable results and very low power consumption.

  I do wish you the best.  I am not a potential customer.  In fact, I am surprised YC funded you.  My guess is they are jumping on top of the billions that will be available in this segment.  The investors will do well.  I don't see anything in your product and company history to lead me to believe you will be able to produce anything "disruptive" at scale.  The Carrier's of this world will get the bulk of that business, and rightly so.

  Here's something you could do that would be disruptive.  It has nothing to do with heat pumps but could easily be integrated into one:

  Rather than build a single large system (say, 5 ton cooling capacity equivalent), create a single high efficiency "box" that effectively houses multiple smaller systems.  For sake of a discussion, imagine a system that is five 1 ton units in one box.

  Why?

  Everyone wants zone controls.  If you own a two level home, and you don't have a zone system, you hate your life.  Upstairs is always ridiculously hot when heating and downstairs is freezing when cooling.

  Come-up with a truly innovative way to create a zone system with room-scale granularity.  Make it super easy to install without having to have ugly heat exchangers mounted on the wall.  Easy enough that, when done, the home will not look materially different.

  Do this and you will --if they trust you-- have lots of customers.  Or, more likely than that, one of the large HVAC companies will acquire your company for the technology.

  That's the real energy efficiency story.  Room-scale granularity in HVAC at a price not materially different from a centralized single-zone system.  I want thermostats (or sensors) in every room.  There is no need to cool or heat the bathroom all day.  There is no need to cool or heat the bedrooms when nobody is in there until the end of the day.  A lot of homes would be just fine if one room was actively cooled/heated while the rest of the rooms were "off" and a couple (kitchen and one bathroom) were programmed to be at the JNC threshold (Just Nominally Comfortable --my term).

  That, to me, would be innovative and disruptive.  Not an easy task.  You would have to come up with a way to build such a system in such a way that you did not have to penetrate the home with a million refrigerant hoses (a pair per room?) and work with the standard installation to the extent possible.

  There's a lot more to something like this.  Just making a heat pump that looks good and has wiz-bang controls, from my perspective, isn't disruptive at all.  There are lower cost solutions in the market today that can be financed, people trust, contractors can install and support.

  Your opportunity for disruption, in my opinion, is in delivering a material and non-trivial improvement to best-in-class performance of products available today.  That, to me, means a granular zone system.

  Personal context:  I have decades of thermal management and clean-room design and operation experience as well as life-support level experience in aerospace applications.  Some of the technology we helped engineer orbits the planet and, in time, will go to the moon.

  - **cmui** · [2023-03-13 23:00 UTC](https://news.ycombinator.com/item?id=35144371)
    Thanks for your perspective! ^c35144371

    Regarding the overall energy story, do you think decarbonizing the economy should be a national priority, and if so, what is the proper approach to take?

    - **robomartin** · [2023-03-14 05:09 UTC](https://news.ycombinator.com/item?id=35147657)
      \> do you think decarbonizing the economy should be a national priority ^c35147657

      Yes, absolutely.  Global, really.

      \> what is the proper approach to take?

      I am glad you asked this question because my follow-up to the above was going to be: Judiciously.

      One of my pet peeves when it comes to all things related to the set of subjects orbiting the general idea of cleaning our collective act is that the popular narrative has lost most connections, if not all, with reality.

      The story has to begin with data.  We have lots of it.  Here's the source for the last 800K years of atmospheric CO2 concentration:

      [https://cdiac.ess-dive.lbl.gov/trends/co2/ice\_core\_co2.html](<https://cdiac.ess-dive.lbl.gov/trends/co2/ice_core_co2.html>)

      This graph, in particular, is very interesting:

      [https://cdiac.ess-dive.lbl.gov/images/air\_bubbles\_historical...](<https://cdiac.ess-dive.lbl.gov/images/air_bubbles_historical.jpg>)

      If we draw a few lines on it and take rough measurements...

      [https://i.imgur.com/37AKa8L.png](<https://i.imgur.com/37AKa8L.png>)

      we might observe that, historically speaking, a 100 ppm increase in atmospheric CO2 took in the range of 25K years and a 100 ppm decrease 50K to 75K years.

      What is interesting about this data and charts is that it gives us a baseline that is, in my opinion, important to keep in mind if we are to be intellectually honest about this subject:


      ```
          Baseline: If humanity left the planet tomorrow, the rate of change
          for the natural reduction of CO2 is approximately 100 ppm in 75K years.
      ```

      
      Let's call that 1 ppm in 1000 years for short (it's just a thinking tool, not a precise calculation).

      As a "solution", I can't think of anything more extreme than humanity evaporating from this planet tomorrow.  And, if we did, it would take somewhere around 100K years for atmospheric CO2 to come down from the current 400 ppm range to, say the historical peak of around 300 ppm.

      I also think this perspective also informs us about the scale of the problem.  Any solution that purports to be able to take the natural rate of change from 1 ppm/ 1000 years to anything in the scale of a human lifetime has to provide proof as extraordinary as the claim being made. For example, a claim of being able to drop atmospheric CO2 concentration by 100 ppm in 30 years would represent a rate of change over 3000x faster than the no-humans-on-earth baseline rate.  That is an exceptional claim that requires even more exceptional proof.

      In understanding certain topics I feel it is important to achieve what I like to refer to as a "tangible sense of proportion" about things.  Once you understand what it takes to send a satellite into orbit you know it can't be done with 1/10th. the energy.  For me, the no-humans-on-earth knowledge provides this baseline that cannot be explained away with the usual hand-wavy argument that seem to permeate this domain.

      Another interesting look is the CO2 contributions of various countries or regions.  Here's a look at that:

      Here's a picture of that answers that question:

      [https://i.imgur.com/wbHptnf.png](<https://i.imgur.com/wbHptnf.png>)

      Looking at this it is clear we have a very serious challenge in our hands.  To repeat myself, if *all* of humanity was beamed into space by Captain Pickard, it would take a thousand years for a 1 ppm drop in CO2.

      Clearly, looking at this graph, completely erasing a number of these countries off the face of this planet would not be equivalent to all of humanity disappearing into space.  Which mean, by simple deduction, that the rate of reduction of CO2 --if any-- would be much slower than 1 ppm per 1000 years.

      Erasing the entire US from the planet would have no effect whatsoever.  The US and China?  Same problem.  Erase 3/4 of these planets and the problem remains: The rate of change will never be better than 1 ppm per 1000 years.

      Well, then, does this mean efforts to reduce CO2 emissions are pointless, futile, nonsensical?

      No, of course not.  I do think that we are pushing a massive lie by claiming to be able to materially affect matters of planetary scale in just a few tens or dozens of years.  It just makes no sense at all.  In fact, it is my opinion that such talk is truly counterproductive and should be treated as comedy or, at best, opportunism aimed at making money given the current drive to promote such matters.

      There are, of course, lots of reasons to decarbonize to the extent possible.  I think most of them boil down to living in healthier environments, healthier cities, homes and buildings.

      Most people don't understand the environment they live in on a daily basis.  These are two images from my office.  The first is with windows open for an hour or so.  The second could be any other day of the week, with windows closed all day.

      [https://i.imgur.com/k9qufys.png](<https://i.imgur.com/k9qufys.png>)

      [https://i.imgur.com/DQL2Kr2.png](<https://i.imgur.com/DQL2Kr2.png>)

      Just looking at CO2, that's a 1000 ppm delta.  This is why I urge people to spend a few dollars and get an air quality meter.  You'll learn things about where you live and what you do every day you could not imagine.  For example, driving in a car for a couple of hours per day means you are in a 1400+ ppm environment for the duration of your travel.


      ```
          Product Idea for Your Startup
          -----------------------------
          Provide for an easy way to inject clean air into an environment.  
          It could be as simple as a 1 inch tube that makes it into the air
          handler through a HEPA filter and injects fresh air into the system.
          Almost anything is better than recirculating bad air.
          Today most homes don't have a sensible way to accomplish this.
      ```

      
      These things, to me, would be truly disruptive (like the easy-to-install zone system).  Otherwise you are competing with the same product against established companies with products that are not materially different in a way that matters.

      Going back to your question:  What would be the proper approach?

      Almost impossible to answer.  It's like going back 50 years and asking someone from the 1970's what the world might be like in 2023.  No clue.

      I would say we need to continue pushing for everything we do to be as clean and environmentally friendly as possible.  Not due to a delusion about being able to save the planet or reverse climate change.  I am not sure I have seen any evidence of this being realistically attainable.  No, we do it because it will make for healthier living and health is crucially important.

      We can justify full electrification and migration away from burning fuels in the long run based on this premise, that of creating a healthier future for everyone on the planet.  That, to me, would be a sensible narrative everyone could get behind.  The problem with pushing a questionable narrative is that the entire planet will eventually see the "emperor has no clothes" effect.  The backlash would not be trivial at all.  It is better, in my opinion, to talk about healthy living than claiming to be able to affect rapid change of a planetary scale.

      I'll leave you with this link to a paper published some time ago by Google Research.  I admire the guts of the researchers who dared publish such a conclusion at a time when this could be career-ending.  Their conclusion still holds.  And, yes, pushing for us to get cleaner at all levels still has significant value.

      [https://storage.googleapis.com/pub-tools-public-publication-...](<https://storage.googleapis.com/pub-tools-public-publication-data/pdf/43326.pdf>)

- **csense** · [2023-03-13 19:42 UTC](https://news.ycombinator.com/item?id=35141333)
  My main experience with heat pumps is a heat pump installed in the northern US in the mid 1990's. ^c35141333

  As a user, the main problem is it's fine in spring and fall, but:

  \- (1) In winter (when the temperature is below freezing) it can't keep up, and needs to switch the gas furnace on

  \- (2) It often needs to be manually switched at the thermostat, you should be able to interface an outside thermometer and say "below X degrees use the gas furnace"

  \- (3) The homeowner told me that they'd never have bought a heat pump if they'd known it would only work for like 25\% of the year.  Decades have passed, so presumably you have better tech.  But you need marketing and customer education to explain that it's better, and assure your customers that past bad experiences aren't indicative of future results if they buy your system.   For me, that means performance metrics (e.g. curves for various house sizes showing the duty cycle needed to maintain a given indoor temperature as a function of the outdoor temperature) and testimonials from customers in states that border Canada.

  Also, you stress fighting climate change a lot.  My sense is that, if you emphasize climate change, you'll potentially alienate the half of the country who thinks climate change is fake news.  (As a group, homeowners who buy heat pumps are probably older and more conservative.)  You have a bigger market if you stay apolitical and sell a practical product.  Features and cost savings appeal to everyone; fighting climate change does not.

  Your pitch is fine for HN.  But for a general audience I'd either (a) leave out the references to climate change, (b) move them pretty far down (not at the end but maybe 2/3 of the way down), and/or (c) emphasize "the government wants to fight climate change and is making the following assistance available..." informing customers those financing options exist without yourself taking a position on the issue.

  Also, I agree with other commenters:  It's important your product will keep functioning if you go out of business or the customer stops paying a subscription fee.

  For me personally it would be great to have a wifi and Ethernet enabled thermostat with an HTTP JSON-RPC endpoint that gives raw data of when the heater turns on, indoor / outdoor temperatures, and be able to change the set-point or turn the system on/off via LAN (protected by some auth mechanism).  An interface to existing FOSS home automation solutions would be nice to have but not essential.  The main thing for me is that your interface is open and can be run without any subscription fees or access to the cloud.

  It would be a real plus if everything's open source and off-the-shelf components.  Ideally if a voltage spike sets the computer on fire, I can unplug the cables, slide the board out, buy a Raspberry Pi, Arduino or similar, re-cable everything, download the software onto an SD card, and bring it back up.

  - **cmui** · [2023-03-13 22:50 UTC](https://news.ycombinator.com/item?id=35144245)
    Thanks for sharing your perspective! Cold weather and general performance has come a long ways thanks to variable speed equipment and vapor injection. Re climate change messaging, I think you're right. The product page doesn't have any climate change messaging on it, and I'm interested in making a product that homeowners find compelling outside of its climate motivations. ^c35144245

- **KirillPanov** · [2023-03-13 18:54 UTC](https://news.ycombinator.com/item?id=35140629)
  Permits. ^c35140629

- **rkg9800** · [2023-03-14 10:55 UTC](https://news.ycombinator.com/item?id=35149600)
  amazing ^c35149600

- **mikebreac** · [2023-03-14 06:25 UTC](https://news.ycombinator.com/item?id=35148048)
  google.com ^c35148048

- **throwawayacc5** · [2023-03-13 17:42 UTC](https://news.ycombinator.com/item?id=35139416)
  Why would I go with you versus a Mitsubishi heat pump system that has years worth of supply chain, installers, trained techs, etc. behind them? ^c35139416

  Is there a term for releasing products that are decades old in Asia/Europe in the US as new, cool, hip, etc.? Maybe "technology arbitrage"?

  - **cmui** · [2023-03-13 23:04 UTC](https://news.ycombinator.com/item?id=35144438)
    Nothing wrong with heat pumps being hip and cool! ^c35144438

    Electric Air gives you (1) easy purchase, financing install (2) built in air quality sensors and controls (3) a thermostat that's actually good, and fully utilizes the efficiency of your inverter heat pump and uses demand response, weather, and TOU rate plans to lower your bills.

- **dang** · [2023-03-13 17:07 UTC](https://news.ycombinator.com/item?id=35138758)
  Offtopic but for those wondering: there are two Launch HNs on the front page today because we're getting close to Demo Day for YC's W23 batch, so it's launch season. When we do pair them, I'm trying to select two startups that are uncorrelated with each other. Also, I thought it might be good to start the week with two launches that have nothing to do with LLMs. ^c35138758

  - **UncleEntity** · [2023-03-13 18:27 UTC](https://news.ycombinator.com/item?id=35140193)
    I vote for a whole month of no LLMs. ^c35140193

    - **dang** · [2023-03-14 00:55 UTC](https://news.ycombinator.com/item?id=35145764)
      Sorry, no can do. You're going to get one tomorrow and two on Thursday I think. I'm trying to pace them! ^c35145764

- **litiholofan** · [2023-03-14 02:30 UTC](https://news.ycombinator.com/item?id=35146602)
  \>The thermostat algorithm combines demand-response with weather and time-of-use rate plans ^c35146602

  Any chance of a dumb version of this without the internet connected bloat?

  - **cmui** · [2023-03-14 02:45 UTC](https://news.ycombinator.com/item?id=35146720)
    Thermostat operates as a standalone device, no internet connectivity required. If you connect it to wifi it receives demand response, weather and TOU signals to reduce your utility bill. ^c35146720

- **ar9av** · [2023-03-14 03:27 UTC](https://news.ycombinator.com/item?id=35147027)
  Hey, so I've been having some issues with my heating and cooling system at home. It's been causing me some headaches, from high energy bills to frequent breakdowns, poor air quality, uneven heating and cooling, and loud operation. I'm tired of dealing with all these problems, and I'm thinking about upgrading to a more modern and efficient solution like a heat pump. ^c35147027

  I was reading up on the benefits and I think it could really make a difference. But to be honest, I'm not really sure where to start or what type of heat pump would be best for my home.

- **grift\_economy** · [2023-03-13 19:27 UTC](https://news.ycombinator.com/item?id=35141127)
  [flagged] ^c35141127

  \[dead\]

- **mfreeman451** · [2023-03-13 17:14 UTC](https://news.ycombinator.com/item?id=35138884)
  [flagged] ^c35138884

  \[dead\]

- **maisie123** · [2023-03-14 01:03 UTC](https://news.ycombinator.com/item?id=35145839)
  [flagged] ^c35145839

  \[dead\]

- **braingenious** · [2023-03-13 18:55 UTC](https://news.ycombinator.com/item?id=35140647)
  This sounds pretty coo— ^c35140647

  \> *combined with a smart thermostat*

  —nevermind. You lost me.

