# WrymBattle

**Drakes of Dusk and Dawn** (formerly Ember Wyrm): a 16-bit style charge-time battle game in the spirit of the classic 16-bit console RPGs, built as an installable Progressive Web App.

Play: https://woodenbehere.github.io/WrymBattle/

## The fight

Five heroes take on a dragon in two phases:

| Hero | Class | Special | Fury |
|---|---|---|---|
| Garrick | Fighter | Rage Strike, Guard | Meteor Cleave |
| Vesh | Thief | Steal, Plunder | Shadow Flurry |
| Ilse | Cleric | Mend, Mend All, Bulwark, Revive | Seraph's Grace |
| Morrow | Sorcerer | Flame, Frost, Thunder | Nova |
| Senna | Summoner | Undine, Sylph, Golem | Thalassa |

- **turn**: each hero's gauge fills by speed; when it is full, their command menu opens. Wait mode pauses gauges while you choose; Active mode does not.
- **Rows**: the back row halves physical damage dealt and taken. Magic ignores rows.
- **Fury**: the pink gauge fills as a hero takes damage (and when an ally falls).
- **World map**: beat the Ember Dragon and a top-down world map in classic 16-bit style opens, with animated water and surf, forests, mountains and deserts. Walk with the arrow keys or WASD, or press and hold on the map. Visit Ember Peak, Thornwick and Castle Valemont.
- **Random encounters**: Thornhares and Bog Slimes in the grasslands, Grave Wolves in the forest, Sand Rays in the desert, Stone Imps in the hills. Each has its own weaknesses, steals and drops. **Run** escapes most fights, and encounters can be turned off from the map menu.
- **Camp**: rest anywhere on the map to restore all HP and MP and revive fallen heroes. Party HP, MP and items carry over between battles.
- **Walkable towns**: Valemont Village and Thornwick are explorable on foot, with wandering townsfolk to talk to. Walk into a shop door to shop: weapons, armor, items, magic, and the inn.
- **Adventurers’ Guild**: in Valemont Village. Guildmaster Orla and the quest board offer bounties (Goblin Trouble, Wolf Pack, Ogre Bounty and more) that track your kills and pay gold, EXP and gear. Guild rank rises from Copper to Gold and unlocks bigger bounties. Check progress anywhere from the Quests menu.
- **Equipment**: five slots per hero (Weapon, Shield, Head, Body, Accessory) with class restrictions, stat comparisons in the shop, and an Optimize button on the Party screen.
- **Progression**: monsters give EXP and Gold. Heroes start at Lv 10 and grow with class-specific stats up to Lv 60. The magic shop teaches new spells (Greater Mend, Radiance, Blaze, Hailstorm, Thunderbolt, and the Glacia and Raijin summons).
- **Saving**: progress saves automatically in your browser once the Ember Dragon falls. Start over from the ? panel.
- **Group battles**: fights against up to four enemies, each with its own turn gauge and health bar. Pick a target from the menu (a cursor marks it on screen); summons hit every enemy.
- **Bestiary**: Thornhare, Goblin, Bog Slime, Grave Wolf, Mandrake, Dusk Bat, Sand Ray, Dune Scorpion, Stone Imp, Ash Salamander, the Hill Ogre, and the Vault Sentinel with its Ward Orbs.
- **Frostfang Peak**: a cave in the great mountain range leads into a three-floor dungeon (Frostfang Trail, Icy Ledges, Frozen Summit) with its own monsters: Frost Harpy, Crag Lizard, Snow Wisp, Rime Golem, Mountain Yeti and the Yeti Chieftain. At the top waits Frostfang, the Rime Dragon: an ice dragon weak to fire that absorbs ice and unleashes a telegraphed Blizzard.
- **The hidden valley**: deep in the island's great mountain range, ringed by peaks so only the airship can land, lie **Castle Arcanum**, home of the magi, and the village of **Highmere**. New spells (Grand Mend, Rebirth, Sunburst, Skyfall, and the summons Valgard and Emberwing), new items (Grand Potion, Greater Tonic, Grand Elixir) and crystal-tier gear.
- **The Isle of Aether**: speak with King Corvin and the magi gather in the Circle of Magi to raise a lost island in the northwest. A wall of storm clouds, rain and lightning surrounds it: fly the airship into the storm and it is hurled back. Only a ship of the sea can cross, so King Aldous's shipwrights build the **Eastern Port**: a pier running out over the water just east of Castle Valemont, with a sailing ship tied at the end. Walk out along the pier to board. On the main island the ship can only tie up at that pier; on the isle it can land on any beach.
- **Tower of Aether**: a hundred generated floors in five tiers (Cloud, Storm, Thunder, Star and Void) with tougher monsters as you climb, Colossus guardians on floors 25, 50 and 75, rare gear every twentieth floor, waystones every tenth floor (tap one three times until it blazes purple to return to the first floor), and **Zephyrion, the Sky Dragon** at the top.
- **Day and night**: a day passes in about six minutes, with dusk, a deep blue night and dawn on the world map and in towns. The time shows in the menu. Inns, tents and beds wake the party at 6:00.
- **Sky and weather**: the top-left icon shows the sun by day and the moon by night, with a 15-day cycle of moon phases; a weather icon sits beside it (tap for the time, weather, moon phase and day). Weather drifts between clear, cloudy, rain and storms: cloud shadows sweep across the ground, rain falls, storms flash with lightning, and battles out in the field show the rain and the dark.
- **Monsters by time and weather**: rain brings Rain Toads and slimes; storms bring Thunderbirds; cloudy days bring out bats. Encounters are a little more frequent at night and in storms.
- **Night monsters**: after dark every area's monsters give way to night forms, about twice as tough (double HP and damage, two and a half times the EXP and gil): Night Goblins, Moonfang Wolves, Vampire Bats, Gloom Imps, Night Ogres, Ghost Wisps and so on, up to the far isles' Night Basilisks and Elder Nightmares. Thornhares sleep. New classes roam only at night: **Night Wraiths**, **Night Gargoyles**, **Moon Moths** and the **big cats**: Shadow Panther (forest), Night Tiger (grass and forest), Dusk Lion (grass, sand and desert), Moon Lynx (hills and shore), Sabertooth (hills) and Cinder Jaguar (the ash fields). On the far isles they're Tide cats (Coralhaven's isle) and Storm cats (the Storm Isles). Night monsters have **MP** (a blue bar under their HP) and cast basic spells: Flame, Frost, Thunder, Torrent, Drain, Poison, Confuse and Cure on a hurt ally. When their MP runs out, they only fight; Mana Siphon drains it. Blood Moon nights on the main isle still belong to the dead.
- **Blood Moon**: every other full moon (day 9, then every 30 days, about every 3 hours of play) rises red. Zombies, Ghouls and Zombie Knights (weak to fire and holy) swarm the open land at two and a half times the usual rate. Valemont’s portcullis drops and Thornwick bars its gates until dawn (you can still leave), with the dead shambling outside. The magi of Castle Arcanum stand on the peaks around their valley casting Radiance, and their golden barrier, visible on the world map, keeps the valley free of the dead. The sky icon counts down the last week.
- **The Blood Moon Hunt**: in the week before a Blood Moon, King Aldous, King Durgan or King Corvin offers the hunt. Report to any king after dawn: 5 dead earns 3,000 G and 2 Elixirs, 15 earns 8,000 G and 2 Grand Elixirs, 30 earns 20,000 G and the Sunlit Charm, 50 earns 40,000 G and Dawnbringer (a 100-attack sword for the fighter). Repeat hunts pay extra gold in place of gear you already have.
- **Vesh's night work**: sleep at an inn after dark and Vesh can slip out alone. He can't leave town, and must be back by dawn. Houses are locked (a lockpicking minigame: tap when the pick is in the gold) and their owners asleep: walking near them wakes them, so learn to **Sneak**. Guards with lanterns patrol the streets; get too close and Vesh drops his loot and runs. Stolen goods sell to the fence. Whenever Vesh steps out onto the street (from the inn, a house or the guild), any guard close by moves off to the far end of their beat, and the guards can't spot him for a couple of seconds while he gets his bearings.
- **Thieves' guilds**: a hidden trapdoor in Valemont Village, Thornwick, Ironhold and Highmere appears only at night. Each guild master (Silk, Old Mags, Grubb Ironfingers and Whisper) gives a quest; ranks go Footpad, Cutpurse, Shadow, Ninja. The trainer Rook teaches Backstab, Pickpocket, Shuriken and Shadowbind, and the last quest makes Vesh a **Ninja** with Katon, Suiton and Raiton and the Kotetsu blade.
- **Fishing**: while sailing, schools of fish ripple on the water. Sail up to one and choose **Fish** to switch to an underwater side view with Vesh at the rail. Tap the water to cast, hold **Reel** (or hold the screen) to work the lure, keep still while a fish nibbles, then tap **HOOK!** when it bites. Landing it is a tug of war: reel while it rests, ease off while it thrashes, or the line snaps. Twelve kinds of fish, from Silver Sardines to the legendary Aether Sea Serpent near the isle; bigger fish fight harder. Snag chests on the seabed for gold, items, and magic armor found nowhere else (Tidecaller Robe, Pearl Crown, Siren’s Pendant).
- **Old Gill and the Fish Book**: Old Gill at the Adventurers’ Guild buys your catch and rewards new kinds with a Sturdy Line, a Master Reel, Grand Elixirs and the Kingfisher Ring. The Fish Book (in the menu once you have a ship) logs every kind with its count, largest size and the date it was caught.
- **Status ailments**: monsters can poison (HP drains over time), petrify (the hero is out of the fight until cured; if the whole party turns to stone, the battle is lost) and confuse (the hero attacks at random, sometimes an ally). Antidotes, Stonebalm and Remedies cure them, as do the Heal spell and the monk's Purification. Confusion wears off when a battle ends; poison (which also drains HP as you walk) and stone last until cured, or until you rest at an inn or camp. The Warding Sash accessory blocks them all.
- **Magic and items outside battle**: open **Party** on the map or in towns and dungeons to cast healing magic (Mend, Greater Mend, Grand Mend, Mend All, Heal, Revive, Rebirth, Sylph, Emberwing), cast Exit inside any dungeon, castle or town, and use potions, ethers, feathers, elixirs and status cures.
- **New magic**: Heal and Exit (warps the party out of any dungeon, castle or town to the world map; tap Exit twice to confirm) at Valemont's magic shop. Ironhold's Rune Hall adds Blight, Firestorm, Glacier, Stormcall, and the summons Pyralis, Gaian and Drakonis.
- **Knightly arts and thief tricks**: Ironhold's Training Hall teaches the Fighter Inner Focus, Shield Bash (heavy hit that knocks the enemy's turn back), Smite (holy light on one enemy, full power from the back row), Consecration (holy damage to every enemy), Purification and Martyr's Grace (revive an ally at the cost of 15% of his own HP) and the Thief Smoke Bomb, Twin Strike, Venom Edge and Assassinate. Auto battle and habits use all of them.
- **Deepdelve Mine**: sealed by royal order until you finish King Aldous's Hill Ogre quest and defeat Frostfang. Then a mine shaft on the northernmost cape drops five levels (Deepdelve Mine, Crystal Galleries, the Old Sky Road, Fungal Hollow, the Magma Depths) to **Ironhold**, the dwarf city. New monsters: Deep Crawler, Burrow Mole, Crystal Spider, Gloom Shade and Magma Slug. At the bottom of the fifth level coils **Gravemaw, the Earth Dragon**, which has walled the dwarves in: a full dragon fight with Rockfall, a petrifying glare and a telegraphed Landslide. It is weak to water and ice and absorbs earth (Gaian). Rescue Hilde the crystal-cutter, and read the Sky Folk's tablets along the Old Sky Road.
- **Ironhold**: freed once Gravemaw falls. The **Royal Hall** holds the throne room of King Durgan and Queen Sigrun, the royal bedchamber and a treasury. In gratitude, the King and Queen reveal the secret of the airship. Also in the city: the dwarven forge and armory (Dwarven Axe, Shadow Edge, Runic Staff, Magma Rod, Dragonbone Whip, Adamant gear), an item shop, an inn, murals, and Elder Thrain's tale of the lost airship. Lifts connect the city to the mine entrance.
- **The airship Aurora**: after the royal audience, Forgemaster Brannoc blasts the old Sky Road open with powder ground from Gravemaw's Earthheart. The Aurora rises to the surface beside the mine. Walk aboard to fly anywhere on the world map, over sea and mountains, with no random battles; choose **Land** to set down on open ground.
- **Resting**: inns, guest beds, tents and the Aurora's bunks offer sleep until morning or until nightfall. Nobody can sleep under a Blood Moon.
- **Town hours**: shops close at dusk (19:00) and reopen at dawn (6:00); the townsfolk of Valemont, Thornwick, Ironhold and Highmere head home, leaving only the guards. The thieves' trainer and the Aurora's stores keep night hours.
- **Night work**: while Vesh is out alone at night, the minimap is hidden. He has to learn the streets by eye.
- **The thieves' sign**: the first time Vesh finds a guild, the doorman shows him a three-gesture sign. Every visit after, he must make it in order at the door, or he's thrown back out through the trapdoor.
- **Sky window**: the top-left window shows the sun rising and setting across the sky, and at night the moon crossing it in its current phase (red under a Blood Moon). Tap it for the time, weather and moon.
- **Sea battles**: sailing the ship brings random encounters (Encounters toggle applies; none near land or the whirlpool), fought on the ship's deck over open water. By day: Sea Serpents, Giant Crabs, Storm Harpies and Reefkin Chiefs; by night, under a dark sky: Krakens, Ghost Pirates, Abyssal Anglers and Sirens. Difficulty rises with distance from the Eastern Port pier: within 10 leagues they're at 40% strength, out to 24 leagues at 70%, and beyond that at full strength (up to 28,000 HP and 1,350-damage hits), with EXP and gold scaling to match. Most absorb water and fear thunder.
- **Fishing weather**: the fishing scene shows night, stars and the moon, clouds, rain and storms. Schools are bigger and more frequent, and fish chase the lure more eagerly, in the rain and in the nights around the full moon.
- **The far isles**: two new islands, reached by ship (which can land on any of their beaches) or by airship.
  - **Coralhaven** on the Coral Reach (southwest) and **Stormhaven** on the Storm Isles (northeast). Coralhaven sits on its island's east shore beside its own pier, the **Coralhaven Docks**: steer the ship into the pier to tie up, and a boardwalk leads to the town gate. Each town has weapon, armor, item and magic shops with new endgame gear (Coral Blade, Coral Kris, Tide Staff, Coral Mail, Nautilus Helm; Storm Edge, Storm Rod, Gale Whip, Thunder Shield, Storm Crown, Gale Cape), an inn, a guild hall with the quest board, two houses, and a hidden thieves' guild. Their masters, Madame Brine and The Gale, give a Ninja the Shadowfang and the Night Veil.
  - Their monsters are the deadliest in the realm: Basilisks, Krakenlings and Abyss Walkers on the Coral Reach; Wyverns, Ironclads and Nightmares on the Storm Isles.
- **Maelstrom, the Water Dragon**: sleeps in a great whirlpool in the far southeast sea. Sail close and the current drags the ship into its eye. It absorbs water, fears thunder, and heals itself with the tide. Until Maelstrom falls, a wall of seawater seals the Tower of Aether. Saves that had already entered the tower are not locked out. Victory brings the Maelstrom Ring, 3 Grand Elixirs, 15,000 EXP and 30,000 G.
- **Seasons**: every three moons (45 days) the season turns, starting in Fall: Fall, Winter, Spring, Summer, then a new year. Fall has drifting leaves and an amber cast, Winter whitens the land and brings snow and blizzards instead of rain, Spring has blossom petals, Summer a warm glow. The sky window, Journal and Homestead all show the season.
- **The Homestead**: a farmhouse a few leagues north of Castle Valemont. Old Hob greets you and sells seed.
  - **Fields**: 24 plots to start (48 and 72 with land clearing). Stand on a plot to **Till**, **Plant**, **Water**, **Harvest** or **Clear** it, or use Till all, Plant all tilled, Water all and Harvest all.
  - **Growing**: crops grow one day for each day they're watered (rain counts). Each has a season, and planted crops wither when the season turns. Crows eat a crop now and then unless you build a scarecrow.
  - **Crops**: Spring turnip, potato and strawberry; Summer tomato, corn and melon; Fall carrot, wheat and pumpkin; Winter snowroot and frostberry.
  - **Animals**: a Chicken Coop houses up to 6 chickens (eggs daily); a Barn houses up to 4 cows (milk daily) or sheep (wool every other day). Their goods appear in your crates each morning. Old Hob buys animals back for 60% of their price from the Animals tab.
  - **Buildings**: Coop, Barn, Well (sits just below the field and waters every planted plot each morning, and anything you plant, automatically), Scarecrow, two rounds of land clearing, a **Greenhouse** and a **Greenhouse Well**.
  - **The greenhouse** is a real indoor growing room: walk through its door to a glass hall of 288 beds (four times the fully cleared field). Till, plant, water and harvest there exactly as outside. Any seed grows in any season and nothing withers, and Old Hob sells every seed once it stands (out-of-season seeds can only be planted inside). Rain doesn't reach the beds, so water them by hand or buy the **Greenhouse Well** (5,000 G), a pump well inside that waters every bed each morning. The outdoor field always follows the seasons.
  - **The farmhouse**: walk in through the front door. Inside are a bed (a free rest), a hearth, and a side table with the latest **Valemont Home Goods Catalog**.
  - **Mail order**: browse the catalog inside or at the red **mailbox** outside, mark what you want (+ and −), then mail the order from the mailbox. It arrives the next morning as **boxes stacked by the farmhouse**; walk into them to carry everything inside.
  - **Decorating**: face an open spot on the floor and choose **Place furniture**; face a piece (or stand on a rug) and choose **Pick up** to move it. Pieces include an oak table, rocking chair, bookshelf, potted fern, sunflower, brass lamp, dresser, grandfather clock (tells the time), fish tank, armor stand, piano, a carved dragon trophy, and three rugs you can walk on.
  - **Auto-arrange**: inside the farmhouse, Auto-arrange lays out every piece (placed or in storage): trophy, piano, shelves, dresser, clock, tank and armor along the walls, tables with their chairs in a dining corner, plants and lamps in the corners, rugs under the tables and in the open, and a clear aisle from the door to the hearth.
  - **Journal: Homestead tab**: the season and days left in it, a **harvest schedule** grouping every planted crop by kind and place (field or greenhouse) with the day it will be ready, plots needing water today, and a warning for field crops that will wither before they ripen; field and greenhouse space, seeds in storage, animals and their daily income, goods waiting in the crates, total homestead earnings, crops harvested, buildings, and farmhouse furniture.
  - **Selling**: drop goods in the shipping bin, or use the Sell tab of the Homestead menu. The farmhouse bed is a free rest.
- **Mine lift**: every level of Deepdelve Mine, and Ironhold, has a lift cage near its entrance. Walk into it to ride to any level you've already reached (Ironhold once Gravemaw is slain).
- **Ironhold homes**: an Upper Ward of four houses flanks the airship bay, and another home sits on the south lane, all open to Vesh's night work.
- **Class advancement**: each hero has a second class with a new look, stronger stats and a signature skill.
  - **Paladin** (Garrick): reach level 20 and slay the Hill Ogre, then speak to King Aldous to take the **Oath of Light** against the Black Knight. +10 strength, +1 speed, +10 defense, +8 magic defense, 48 MP, white-and-gold plate, **Holy Blade** (a holy sword stroke at full power from either row) and **Lay on Hands** (16 MP: restore half an ally's HP and cure ailments, in battle or on the field).
  - **Ninja** (Vesh): via the thieves' guilds as before; now he wears a ninja outfit.
  - **Master Summoner** (Senna, Drakonis, level 20): once the isle is raised, Queen Elowen of Castle Arcanum holds the **Rite of Mastery** against the Spirit Warden. More magic and +60 MP, new robes, and **Bastion** (holy judgment on every enemy).
  - **High Cleric** (Ilse): Coralhaven, on the southwest isle, now has a church, the **Chapel of the Tide**, with a steeple, a rose window and stained glass. Inside, a gold tabernacle stands against the back wall directly behind the altar, with a red sanctuary lamp burning beside it. A confessional stands at the back, with a line of townsfolk waiting in the back pew by day, and the **holy water font** just inside the door, on the left, fully restores the party's HP and MP and cures every ailment. Outside, a rose garden with a small statue of Mary sits to the right of the church door. Once Ilse knows Grand Mend and is level 20, stay a night at the Coralhaven inn: she wakes alone in the chapel, where the **Seraph of the Tide** explains a High Cleric's duties (mend what is broken, shelter the weak, speak the truth) and puts her through five questions of conscience: mercy, need, honesty, humility and grief. Answer every one as a true healer would and she becomes a High Cleric (more magic, magic defense and +60 MP, new robes, and **Benediction**: fully heal and cleanse the party, also usable from the Party screen). Miss one and she wakes at the inn; she can try again any night. By day, Sister Marisol tends the chapel.
  - **Archmage** (Morrow): won in **Gloamhollow**, below. Gives more magic and +60 MP, a new robe and **Oblivion** (raw magic on every enemy).
- **Gloamhollow**: a chasm on the Storm Isles, a short walk from Stormhaven. Only the airship can go down: fly directly over it and choose **Descend**. The Aurora lands in an underground city where everyone is a sorcerer and every house is an A-frame shaped like a wizard's hat. There is no thieves' guild. Talk to the Aurora to take off again.
  - **Shops**: wood weapons (Witchwood Rod, Ebony Staff, Gnarled Wand), cloth armor (Nightweave Robe, Pointed Hat, Shadow Sash), an item shop heavy on Mana Tonics, and the Hall of Whispers, where any magic user can learn **Mana Siphon** (drain MP from an enemy; level 30) and **Wall** (each ally reflects the next three spells back at the caster; level 35). Auto battle casts Wall when enemies use magic and Mana Siphon when MP runs low. Shops never close.
  - **The Depths**: the Gatekeeper lets only magic users through, and only with no metal armor (crowns, helms, mail and shields). Garrick and Vesh wait in town and rejoin when you come back up. Twenty floors, each harder than the last; rune circles on floors 5, 10, 15 and 20 return you to town, and the Gatekeeper can send you back to the deepest one you've reached.
  - **Thrift Ring**: three rings lie in chests on floors 6, 12 and 18. While one is equipped, every spell costs 1 MP.
  - **King Nocturne**: the King of Gloamhollow waits on floor 20. He has 240,000 HP and casts Doomfire, Abyssal Sunburst and Night Oblivion; almost everything he throws is a spell, so Wall turns his power back on him. He is weak to holy. Beat him and Morrow becomes a Archmage, and you win the Night King's Hat and 40,000 gold.
  - Trials are like the Aurora's simulator: no EXP or gold, and the party is restored whether you win or lose, so you can retry as often as you like.
- **Party menu**: laid out like a classic 16-bit RPG menu: each hero's portrait, name, class, LV, HP and MP down the left; Item, Skills, Equip, Status, Journal, Quests, Save and Close down the right, with boxes for time played, steps and gold. Tap a hero, then a command.
  - **Item**: Use / Arrange (by type, A–Z or most held) / Gear tabs, a description box with the count, and a two-column list. Tap an item to read it, tap again (or Use) to pick who it's for. A **Tent** is used from here to camp: on the world map (not while aboard a ship) or at a dungeon save circle.
  - **Skills**: description box with the MP cost, the hero's portrait and LV/HP/MP, and the skill list (bright skills work outside battle). Tap to read, tap again or Cast to use.
  - **Equip**: Equip / Optimum / Remove / Empty; the slots with the hero beside them; tap a slot, then a piece to see every stat change (green up, red down), and tap it again to equip.
  - **Status**: portrait, LV/HP/MP, EXP and EXP to the next level, condition, battle commands, all stats in two columns, and equipment.
  - ◀ ▶ switch heroes on every screen, and Back returns to the party menu.
  - **Journal**: the page fills the left side and its sections (Stats, Homestead, Bestiary, Items, Fish Book, Notes) are picked from the list on the right.
- **Journal** (from the menu): **Stats** (time played, days passed, steps on foot, leagues sailed and flown, battles won, lost and fled, monsters slain, gold on hand, earned and spent, chests opened, fish caught, Blood Moon Hunt best, thieves' rank and sign, party levels), a **Bestiary** of everything slain (with HP and weaknesses) and seen, **Items** collected and used or sold plus gear collected, the **Fish Book**, and **Notes** you can type that are kept with the save. Counting starts with this version, so older saves begin their tallies from zero.
- **Save slots**: three save files. Save to any slot (overwriting another game takes a second tap), load any slot, or start a new game in an empty one. Each slot shows level, day, time played, gold and when it was saved. The game keeps autosaving to the slot you're playing, and existing saves become slot 1.
- **Minimap**: in dungeons (the mountain trail, Deepdelve Mine and the Tower of Aether) the minimap starts dark and fills in as you explore, and each floor remembers what you've seen. Tap × on the minimap to close it and see more of the screen; a round **M** button brings it back.
- **Full view**: on the world map, choose Full view to hide the menus and zoom the map out, so you see far more of the world (twice as far by default; tap **View** to switch between 2×, 3× and 1.5×) while walking, sailing or flying. Tap ✕ Menu or press Esc to bring them back. Battles always play at normal size: full view steps aside when a fight starts and returns when you're back on the map.
- **Aboard the Aurora**: while flying, choose **Explore the ship** to walk her decks. The **top deck** has the helm, masts, cargo and crew; a hatch leads **below deck** to the crew quarters (rest in a bunk to restore all HP and MP and cure ailments), Quartermaster Hilde's stores (potions through Grand Potions, ethers, remedies, feathers and tents), and the **training room**. There, the **Battle Simulator** crystal conjures any creature the party has fought, one to three at a time. Simulations give no EXP, gold, items or bounty kills, and the party can't truly fall: when the bout ends, won, lost or fled, everyone is restored to exactly how they started, items included. Walk into the wheel or choose **Take the helm** to fly on.
- **Save circles**: glowing safe spots in the dungeon that save your progress, allow Tent camping, and are where you wake if the party falls.
- **Mountain side quests**: return Brom the miner's lucky pickaxe, rescue the climber Kessa from behind the Yeti Chieftain, and gather three Frost Lilies for Hermit Oswin's Frost Ward (halves ice damage).
- **Castle grounds**: a stone wall surrounds Castle Valemont and Valemont Village. A clear road runs from the south gate straight to the castle, with the village on both sides.
- **Mini-map**: a map of the world (or the castle, when inside) sits in the top-right corner. Tap it to enlarge.
- **Castle Valemont**: walk inside to meet King Aldous and Queen Mirelle in the throne room, rest in the guest rooms, loot the armory, and earn the Royal Key by slaying the Hill Ogre. The vault is locked, guarded by Captain Brann, and protected by an ancient sentinel.
- **Auto battle**: the Auto button hands any heroes you choose to the AI, using one of four strategies (All-Out Attack, Balanced, Protect Allies, Save MP). Each hero can also get a habit, such as Thief: Always Plunder, that overrides the strategy whenever it can.
- **Phase 2**: the Ember Dragon becomes the Molten Dragon. Its elemental weaknesses change and it gains row-targeting attacks.

## Install

Open the play link on a phone or in Chrome/Edge, then use **Add to Home Screen** (iOS Safari: Share → Add to Home Screen). After the first load, it works offline. To force the newest version, tap the version number in the footer twice.

## Files

- `index.html`: the whole game (canvas renderer, battle logic, UI)
- `manifest.webmanifest`: PWA metadata
- `sw.js`: service worker for offline play. When you change files, bump `VERSION` here and `APP_VERSION` (plus the footer button text) in `index.html`.
- `icons/`: app icons

To run locally, serve the folder over HTTP (for example `python3 -m http.server`) and open `http://localhost:8000`. Service workers don't run from `file://`.

## Rows

Open the main menu and double-tap a hero to move them between the front row and the back row. Back-row heroes' portraits shift to the right and say "Back row". Back-row heroes take and deal half physical damage. During a battle, use the Row command instead.

## Touch view

The game starts in a full-screen touch view made for phones (turn the phone sideways for the biggest picture). The menus and party list are hidden. Switch to the classic layout under Options → Display, or with **Classic view** in the action ring; your choice is remembered.

- **Walking:** hold anywhere on the left half of the screen and drag. A faint thumb stick appears under your thumb.
- **Actions:** tap the right half for a ring of actions: Party, Journal and whatever applies where you are (Leave, Camp, Fish, Land and so on), plus Full screen, Help and **Classic view** to switch back. Menus open as usual and closing them returns to the touch view.
- **Battles:** when a hero's turn comes, they step out to the front and center of the party and a full ring of commands opens around them; they walk back into line once they act. To simply attack, skip the ring and tap an enemy: that hero uses Fight on it. Magic, Skill and Item lists open as a second ring around the hero (an inner and outer loop when long, with More › to page; spells you can't afford are dimmed, and items you have none of are left out). To choose who an attack, spell or item is for, tap that enemy or hero. With a single-target attack spell (Flame, Frost, Thunder, Blight and the like), triple-tap empty space instead to spread it across every enemy; the damage is split evenly between them. Tap another glowing hero to switch who acts; Wait/Active and Auto are in the top-right corner.
- **Zoom:** on the world map, a magnifying glass sits under the mini map. Tap it to cycle the view through 1×, 1.5×, 2× and 3× zoomed out; your choice is remembered and towns, dungeons and battles stay at normal size.
- **Battle corner:** in the top-right of every battle, the **Auto** button sits on top: tap it to switch between auto (it shows how many heroes are on auto) and **Manual**, or press and hold it to open the auto-battle settings. Below it, a **Wait** button: tap it to switch to **Active** (gauges keep filling while you choose) and back.
- **Bars:** trailing off the lower right of each hero, HP (green, turning yellow and red), MP (blue), Fury (pink, pulsing when ready) and the turn gauge (gold).

## Options

Open the menu (Party) and choose **Options**:

- **Battle:** Manual or Auto control, the auto strategy (All-out Attack, Balanced, Protect Allies, Save MP), which heroes fight on auto and each one's habit, and Wait or Active mode. These are remembered between visits.
- **Gameplay:** random encounters on or off, and show or hide the mini map.
- **Display:** Classic or Touch interface, and full screen where the browser supports it.
- **Text size** (under Display): Small, Medium, Large or Extra large, set all at once or separately for battle and command menus, battle info (spell names, targeting prompts, Victory and Defeat cards), speech, pop-up messages, and menu screens. Remembered on this device.
- **About:** the version (tap it twice to update), How to play, Parden Web Apps, and email and donate links.

## Title screen

The game opens on a title screen: two dragons face each other above the name on a black background, with **Start** and **Continue** below, Parden Web Apps 2026 at the bottom, and the version under that (tap it twice to update).

- **Start** begins a new game in the first empty save slot. If all three slots are full, tap it twice; the slot you were playing is replaced once you beat the wyrm.
- **Continue** loads your most recently saved game and shows its slot, level and location. It is greyed out until you have a save.

## Clearing a save

In **Save & Load**, each saved slot has a **Clear** button. To make sure it never happens by accident, it takes three taps: the first warns you, the second asks once more, and the third deletes the slot. Waiting four seconds or tapping anything else cancels. Clearing the slot you are playing returns you to the title screen.

## Summon entrances

When Senna summons, the screen darkens and the summon itself appears before its attack: Undine rises from a whirlpool, Sylph flutters in, Golem drops from the sky, Glacia forms out of snow, Raijin arrives in a lightning flash, Pyralis bursts from flame, Gaian breaks out of the ground, Valgard gallops in, Emberwing and Drakonis swoop down, Bastion rises over the horizon, and Thalassa (Senna's Fury) breaches from the waves. Attack summons appear over the enemies; Sylph, Golem and Emberwing appear on the party's side. The full entrance (about 1.5 seconds) plays the first time each summon is called in a battle, then a quick flash after that. Tap to skip.

## Inkwell

Inkwell, a little scribe in a navy robe with an ink-pot hat, round spectacles and a quill, stands near the entrance of every town during the day (he heads home at dusk with the townsfolk, 7 PM, and is back at 6 AM): Valemont Village, the port town, Ironhold, Highmere, Coralhaven, Stormhaven and Gloamhollow. Talk to him to rename any hero (up to 8 letters, numbers, spaces, hyphens or apostrophes). Tap a hero's original name to restore it. New names are kept in that save slot and are used everywhere: battle, menus, the party list, and all story dialogue, messages and help text. Two heroes can't share a name, and a hero can't take another hero's original name.

## Sylph

Senna's Sylph casts four spells on the whole party: **Mend** (heals HP), **Haste** (turn gauges fill 50% faster for 30 seconds), **Spellguard** (magic damage taken is cut by 40% for 30 seconds) and **Renew** (restores 4% of max HP every 2 seconds for 30 seconds). They show as HASTE, SHELL and REGEN tags in the party list and end if a hero is knocked out.

Ilse can also learn **Spellguard** (16 MP, one ally; from Lv 12, 1,500 G) and **Renew** (22 MP, one ally; from Lv 18, 2,600 G). Spellguard is sold at Ironhold's Rune Hall, Highmere's Spellhouse, Coralhaven's Reef Library and Stormhaven's Thunder Spire; Renew at the last three.

## Enemy bars

Each enemy's name and HP bar sit right under it in battle. The big dragon bosses keep their bar in the top-left corner.


## Camping
Pitching a Tent (on the world map or at a dungeon save circle) plays a 5½-second campfire scene, one of five picked at random:
- **Supper**: the party gathers around the campfire while Garrick turns a boar on a spit over a cooking fire with Vesh waiting nearby, and Morrow launches magical fireworks.
- **Stargazing**: the party lies back to watch falling stars while Senna traces a constellation.
- **Song**: Vesh strums a lute by the fire, with notes drifting up and fireflies around.
- **Night watch**: the others sleep in bedrolls while Garrick walks the camp with a lantern and an owl watches.
- **Sparring**: Garrick and Vesh spar by the firelight; Ilse cheers, Morrow reads a glowing tome and Senna's wisps circle her.

In touch view, the world map's action ring has a **Camp** button showing how many Tents you carry (it's hidden while aboard a ship or airship). In dungeons it appears while you stand on a save circle.

## Change log
Options › About › **Change log** lists every version, newest first, with the date and time and a short description. The list is built from the git history: before each release run `python3 tools/changelog.py vX.Y.Z "what changed"` to rebuild it with the new entry.

## Original names (v3.48)
To make the game its own, every spell, summon, item, class and the currency now has an original name (save files keep working; only the names shown changed). Mend / Greater Mend / Grand Mend; Blaze and Firestorm; Hailstorm and Glacier; Thunderbolt and Stormcall; Radiance, Sunburst, Skyfall, Oblivion, Blight, Rebirth, Renew, Bulwark, Spellguard, Mana Siphon; the summons Pyralis, Gaian, Drakonis, Valgard, Emberwing, Bastion and Thalassa; Greater and Grand Potions, Mana Tonics, Grand Elixirs, Life Feathers, Stonebalm, the Warding Sash, Thrift Rings and Silversteel gear; the Cleric and High Cleric, the Sorcerer and Archmage; the Fury gauge; and gold. `tools/rename.py` holds the full list.

## Save backup
Saves live in the phone's browser storage, so uninstalling the app or clearing its data erases them. **Options › Gameplay › Save backup** writes every save slot and setting to a small file (`ember-wyrm-backup-YYYY-MM-DD.json`): **Share…** sends it straight to Google Drive, Gmail or Messages (where the phone supports it), **Download** puts it in Downloads. **Restore from backup** loads a file and replaces the saves on the device after you confirm. On a fresh install the title screen shows **Restore a saved-game backup** under Start and Continue. If you haven't backed up in two weeks, the game reminds you once every few days when you continue.


## The name (v3.50)
The game is now **Drakes of Dusk and Dawn**, and the five wyrms are dragons: the Ember Dragon (Molten Dragon), Frostfang the Rime Dragon, Gravemaw the Earth Dragon, Maelstrom the Water Dragon and Zephyrion the Sky Dragon. Save files, the web address and the repo name are unchanged.

## The opening (v3.51)
Starting a new game plays the chronicle of **Orren Vael**, archivist of Castle Arcanum: eleven parchment-toned scenes with typed narration. The Dawn Ballad says Sir Kael and the Knights of the Dawn slew the five dragons and ended the Long Dusk; Orren sets down what really happened (the Sky Folk fleet, the dragons waking, the five forgotten heroes) and the last scene fades into color at the foot of Ember Peak before the Ember Dragon fight. Tap to advance (it also advances on its own), or Skip. Watch it again from Options › About › The opening.

## Auto battle: spread spells (v3.54)
The auto-battle settings have **Cast attack spells on all enemies**: Never, 3 or more enemies, or 2 or more enemies. When it applies, a hero on auto casts single-target attack spells (Flame, Blaze, Thunder and the like) on every enemy at once with the damage split between them, the same as triple-tapping empty space by hand. Healing and support spells are unaffected. The choice is saved with your other auto settings.

## Quest tracker (v3.55)
On the world map, a **Quests** panel sits under the sun/moon icon. Tap the **−/+** to collapse or expand it (the game remembers). It lists the main-story goal (from the Ember Dragon to Zephyrion) and every active guild bounty with its count, like "Goblin Trouble 3/5", or a green **Turn in** once it's done. Tap a bounty to open the Quests list. It hides in battles, menus, towns and while camping.

## Spell groups (v3.56, touch view)
In battle, Ilse's and Morrow's magic opens in two steps. Tapping White Magic shows a ring of **Healing** (Mend, Mend All, Revive, Renew, Rebirth…), **Attack** (Radiance, Mana Siphon) and **Status** (Bulwark, Spellguard, Heal, Wall); Morrow's Black Magic shows **Fire**, **Ice**, **Lightning** and **Arcane** (Blight, Sunburst, Skyfall, Oblivion, Mana Siphon, Wall). Each group shows how many spells it holds; tap one for its spells, or ‹ Back to return to the groups. Groups with no spells yet don't appear, and if a hero knows spells from only one group the step is skipped.

## Throw a stone (v3.57)
On Vesh's solo nights, **Throw stone** (in the night menu and the touch action ring) tosses a stone a few tiles the way he last moved. Every guard within about nine tiles of where it lands walks over to check the sound (a yellow **?** floats over their heads), looks around for a few seconds, then walks back to their beat. Use it to pull guards away from a door before slipping in. A stone that lands near a house can stir light sleepers, and Vesh needs a couple of seconds to find another.

The Equip screen's hero card no longer overlaps the gear names: when long names or large menu text leave no room beside the list, the card moves below it.

## Dungeon camps (v3.58)
A Tent pitched on a dungeon's save circle plays a camp scene built for that place: an ice cave with icicles and frosty breath on Frostfang Trail and the Icy Ledges; a windblown summit at the top; timber supports, a swaying lantern and an ore cart in Deepdelve; glowing crystal clusters in the Crystal Galleries; glowing Sky Folk carvings and a carved airship on the Old Sky Road; giant glowing mushrooms and drifting spores in the Fungal Hollow; a lava river and rising embers in the Magma Depths; the Tower of Aether's open arches showing its tier (clouds, storm, thunder, stars, the void); and violet flames among pointed roofs in Gloamhollow's Depths. A line about the place appears with the "Rested and ready" message afterward.

## Warp (v3.59)
Morrow can buy **Warp** (2,500 G, 30 MP) at the Valemont magic shop. Cast it from Party › Magic on the world map or inside a town: pick any town the party has visited (Valemont Village, Thornwick, Highmere, Coralhaven, Stormhaven or the Homestead) and the party arrives there in a swirl of blue light. Walking out of the town puts you beside it on the world map. It can't be cast aboard a ship or the airship, in dungeons (that's Ilse's Exit), or on Vesh's solo nights. Your ship stays where you left it, so warp back to it when you need it. Valemont Village counts as visited from the start; other towns are added the first time you enter them after this update.

## Mine battles (v3.60)
Battles inside Deepdelve now look like the level you're fighting on: timber supports, a hanging lantern, rails and broken ore carts on the first level; walls of glowing cyan and violet crystals (and a cart full of them) in the Crystal Galleries; glowing Sky Folk carvings over the rails on the Old Sky Road; giant glowing mushrooms and a cart of spores in the Fungal Hollow; and a lava river, glowing cracks and a scorched cart in the Magma Depths. Crystals, lanterns and mushrooms softly pulse with light, and crystal tips glint. Gravemaw keeps his own arena.

## Ironhold's guild hall (v3.62)
A guild hall now stands in Ironhold's southeast corner (gold-brown roof, crossed-swords sign). Guildmaster Torva posts a deep-tunnel board of nine tougher, better-paying bounties: Tunnel Crawlers, Undermined (Burrow Moles), Crystal Thieves (Crystal Spiders, Bronze), Shades on the Sky Road (Bronze), Yeti Hunt (Bronze, Frost Ward), Molten Menace (Magma Slugs, Silver, Magus Ring), Rogue Golems (Silver, Giant's Belt), Night Prowlers (Shadow Panthers at night, Silver) and The Dusk Lions (Gold: 9,000 G, two Grand Elixirs and the Hero's Ring). Ironhold bounties are accepted only at Ironhold's board and surface ones only in Valemont; finished bounties can be claimed at either hall, and all of them count toward guild rank. Master Bryn now stands beside the Training Hall door.

## Choosing what the tracker shows (v3.63)
In Quests › Active, every bounty in progress (and the main story goal at the top) has a **Track** button. Tracked ones (✓ Tracked, in blue) appear in the map and dungeon tracker; untrack any you don't want cluttering the screen. New bounties are tracked automatically, and the choices are saved with your game.

## Equip item descriptions (v3.64.0)
On the Equip screen, a description box sits between the top command bar and the slot list. It shows the selected piece (or the piece already in the chosen slot): its name, slot, a short line on what it does, its stat bonuses, any special effect (blocks ailments, halves an element, 1-MP spells) and who can wear it. Text comes from `gearDesc(id)`; notable items have hand-written lines in `GEAR_FLAVOR`.

## Info text away from the hero (v3.65.0)
In towns, castles and dungeons, info text (`say`) and NPC dialog boxes move to the top of the screen when the hero is in the lower half, and back to the bottom when the hero is in the upper half (with a little dead zone so they don't flicker). `msgSide()` runs each castle frame and toggles `.msgTop` on the stage. On the world map the hero sits just below center, so both always show at the top there. If an area-name banner is showing, the info text drops just below it.

## Bigger farmhouse and family meals (v3.66.0)
The farmhouse is now 24×16 with four rooms: a **Bedroom** (big bed that rests the party, fireplace), a **Kitchen** (icebox, counters, iron stove, sink, kitchen island), a **Living Room** (two couches facing a low table, the catalog stand) and a **Dining Room** (table for six). Doorways and the front door approach are kept clear of placed furniture (`HOME_CLEAR`); anything from the old layout that lands in a wall goes back to storage.

**Family meal**: use the stove, the dining table or chairs, or *Cook a family meal* in the house menu. It costs 6 farm goods from the crates (or 500 G of groceries when short). A ~10 s cut scene plays (cooking → serving → toast → eating) with the whole party and Old Hob, then everyone is **Well Fed** for 7 game days: +10% Attack, Magic, Defense, Magic def. and Max HP, plus HP/MP restored. A new meal restarts the week. The status screen shows the days left. Code: `familyMeal()`, `mealScene()`, `wellFed()`, and a `recalc` wrapper.

## Isle of Aether rising cut scene (v3.67.0)
When the Circle of Magi raises the isle, `isleCine()` plays a ~13.5 s letterboxed scene in five beats: the sea churns (whirlpool rings, a swelling dome, the golden spire tip), the white tower bursts up with water sheeting off it, the island heaves out of the ocean with waterfalls pouring off its cliffs, storm clouds spin in over the peak with rain and lightning, and a see-through wall of water rises to ring the island. The screen shakes while things rise, and captions run along the bottom (`.stage.cutfx`). This replaces the old world-map splash.

## Stop fishing button (v3.68.0)
The fishing scene now has an on-screen **✕ Stop fishing** button in the top-left corner (`#fishX`). Touch view hides the command list, so before this there was no way out of fishing on a phone. Esc still works on a keyboard.

## Raijin bolts stay on the enemy side (v3.69.0)
Raijin's Storm Drum still throws its barrage of lightning, but the bolts now only land between the left edge and just short of the front hero (`min(hero.x) - 18`), so none strike the party.

## Hero's Diners (v3.70.0)
A cottage in each town (Valemont, Thornwick, Highmere, Coralhaven, Stormhaven and Ironhold) is now an empty eatery with a plate-and-cutlery sign. Lease it for 2,500 G from the landlord inside to open a **Hero's Diner**.

- **Ingredients**:
  - **Monster cuts** drop in battle (`CUTS`): Hare Haunch, Wolf Flank, Harpy Wing, Lizard Tail, Scorpion Tail, Toad Legs, Ray Fin, Slime Jelly, Mole Cutlet, Spider Leg, Yeti Shank, Crab Claw, Kraken Tentacle, Serpent Fillet, Panther Loin (all the big cats) and the rare Drake Tail. Night forms drop more.
  - **Fish** in the basket count as carried food.
  - **Crops, eggs and milk** sit in the farm crates. Pack them at the **Larder** (the farmhouse icebox, or *Larder* in the house menu), which also stores food for runners.
- **Each diner keeps its own stock.** Carry food in on the Stock tab ("Stock everything the menu uses" does it in one tap).
- **Menu**: 22 recipes (`RECIPES`). Four are known at the start; learn the rest with gold, and some need more stars. You get 3 slots at first, up to 5. Each town favors certain kinds of food (`DINER_TOWNS[t].taste`): those dishes sell more often and for 20% more.
- **Staff**: hire a cook (required; skill raises prices) and a server (brings in more customers). Each has a trait (Generous, Gourmet, Speedy, Showman or Thrifty) and a daily wage paid from the till. New applicants come each week.
- **Each morning** (`dinerDay`): customers come based on reputation and the server, order by local taste, and switch to another dish if theirs is out of stock. Sales fill the till and wages come out of it. Reputation (0–100) gives 1–5 stars, which unlock recipes and upgrades. The Overview tab keeps a 7-day ledger.
- **Upgrades**: extra menu slots; runners (6 or 12 ingredients a day carried from the larder for the menu); a road sentry post (raid chance drops from 25% to 8%); and the sky skiff (20 a day, can't be raided).
- **Raids**: when runners are ambushed, the shipment is lost and they won't go out again. Talk to the runner at the diner (or tap *Clear the road*) to fight the area's monsters. Winning keeps the road safe for 7 days.

## Status screen fit (v3.71.0)
The hero card and the command list on the Status screen now sit in a wrapping row (`.ffs-strow`). When big text or a narrow screen leaves too little room, the command list drops below the card and lays out in columns instead of squeezing the card. Numbers like EXP no longer run over the box border.

## Check the latest version (v3.72.0)
Options › About has a **Latest version** row under the installed version. **Check** fetches the live `index.html` with `cache: 'no-store'` and a cache-busting query, so the service worker can't answer from its cache. It reads the footer version and the embedded changelog, then shows the installed and latest versions side by side, with a list of the updates you don't have yet. Nothing is installed until you tap the version twice.

## Summons on top (v3.73.0)
While a summon plays, the enemy name tags, HP bars and boss bar fade out (`.stage.summoning`), so the summoned creature isn't covered. They fade back in as soon as the summon's action ends.

## Warp ring and quest tracker shortcut (v3.74.0)
- **Warp in the touch ring**: once Morrow knows Warp, the world-map and town command ring has a **Warp** chip. Tapping it opens a second ring of visited towns, with a hint showing the MP cost and Morrow's MP, plus **‹ Back** to the command ring. Picking a town casts Warp straight away (`castWarp(h, dest)`).
- **Quest tracker**: tapping the *Quests* header, or any quest in the list, opens the Quests menu. The **−/+** box still collapses and expands the tracker.

## Every monster drops food, and a Food page in the Journal (v3.75.0)
- Every defeated monster now always drops one food ingredient, or two for night forms half the time. The cuts table gained non-meat foods:
  - **Vegetables**: Mandrake Root, Grave Mushroom (undead), Reef Kelp (sea folk), Shadow Truffle (shades, wraiths, gargoyles).
  - **Spices**: Rock Salt (golems, orbs, ironclads), Fire Pepper (imps, slugs).
  - **Sweets**: Wisp Honey (wisps, moths), Mana Sugar (grimoires).
  - **Bread**: Trail Bread (goblins, acolytes, ghost pirates).
  - **Dairy**: Ogre Cheese, Wild Egg, Fresh Cream.
  - **Meats**: Bat Wing, Grub Steak, Nightmare Rump, Mutton, Angler Fillet, Wyvern Wing.
  - Bosses have their own drops (tower guardians and the Black Wyrm King give Drake Tail). Anything without a match drops Monster Jerky.
- Six new recipes use them: Monster Jerky Plate (known from the start), Ogre Cheese Toastie, Salt-Crusted Fish, Wisp Honey Cake, Fire Pepper Steak and Shadow Truffle Risotto. Recipes can now ask for any bread, any egg or dairy, any spice or any sweet, and wheat counts as bread.
- **Journal › Food** lists every ingredient by group, with how many you've gathered all-time (`S.flags.foodLog`: battle drops, fish caught, crops harvested) and where it is now: your pack, home (larder and crates) or stocked in your diners.

## Standing behind counters (v3.76.0)
In the diners and the farmhouse, furniture just below the hero (counters, stoves, sink, icebox, kitchen island, tables, couches, the bed) is redrawn over the hero's sprite after the frame is drawn. Standing behind the counter now shows the hero half-hidden behind it instead of on top of it.

## Repaint after returning to the app (v3.77.0)
Phone browsers can quietly discard large off-screen canvases while the app is in the background, so the pre-drawn world map (`tex`, `tex2`), the minimap (`worldMini`) and the room texture (`ctex`) can come back blank. Then the island, or all the land, disappears until a reload. On `visibilitychange`, `pageshow` and `focus`, `repaintLost()` checks one pixel of each cached canvas and rebuilds any that came back empty.

## Fishing buttons under the boat (v3.78.0)
**✕ Stop fishing** now sits just under the boat, with a new **⤒ Reel in** button below it (`#fishBtns`, positioned against the canvas every 150 ms and on resize). Reel in (`fishReelIn()`) pulls the line straight back to the rod tip so you can cast again. Any fish nibbling swim off. It's greyed out while the line is already in, or while a fish or treasure is hooked.

## Diner reports (v3.79.0)
Each diner has a **Reports** tab:
- **Last 7 days**: customers served, turned away, average rating and profit.
- **Daily profit**: a bar for each of the last 14 days, green for profit and red for loss.
- **Income statement**, last 7 days and all time: sales, food cost, gross profit, wages, net profit and margin.
- **Cash flow**, all time: sales into the till, wages paid, gold you collected or paid in, the till balance, lease and upgrade spending, and net cash to you.
- **Balance sheet**, today: till cash, food in the kitchen at ingredient value, lease and upgrades at cost, wages owed, your stake (gold, food and lease put in, minus gold taken out) and retained profit. The two sides always balance.
- **Dishes**: sold, average rating, sales, profit per plate and customers turned away for each dish, plus the best seller, the customers' favorite and the dish that sells out most.
- **What customers say**: the last 8 reviews, 1–5 stars.
- **All your diners**: stars, rating, 7-day profit and till for each location.

Pricing changed with this: each plate now sells for 1.4× the value of the ingredients actually used, plus half the recipe's base price, then the cook, server and local-taste bonuses. Before, rare fish or milk could sell for less than they cost. Each served plate gets a 1–5 rating (local taste, cook skill, whether there's a server, signature dish, plus some luck), and reputation now grows from those ratings. Data: `D.life`, `D.dishes`, `D.cash`, `D.inv`, `D.reviews`, and 14 days of `D.log`.

## Journal › Diners (v3.80.0)
The Journal has a **Diners** page: totals across all diners (customers served and profit over the last 7 days, gold waiting in the tills), then one line per town with stars, 7-day sales, rating, profit and till, plus warnings (no cook, empty menu, road blocked, wages owed). **Reports** opens that diner's Overview and Reports read-only (`openDiner(t,'report',true)`). Collecting, stocking, menu and staff changes still need a visit. Closing returns to the Journal.

## Most used ingredients chart (v3.81.0)
Diner Reports now has a **Most used ingredients (last 7 days)** bar chart under Daily profit: the top 10 ingredients by amount used, colored by food group, each with the count and its value in gold. A key and a "kitchen has … left" line for the top three follow. Each day's log entry now records `used` (ingredient → amount), filled in by `cookFrom(st, R, use)`.

## Tidy spell lists with More pages (v3.82.0)
Battle skill, magic, summon and item lists in the touch view (`layList`) now form one neat curved column beside the hero instead of two crowded loops. When there are more entries than fit the screen height (up to 7 rows), the last slot becomes **More › 2/3** and opens the next page. On later pages the center **‹ Back** steps back a page, and on the first page it returns to the command ring. Command rings (`layRing`) page the same way when they hold more than 8 choices.

## Six spots per battle ring (v3.83.0)
In battle, every touch ring holds at most **six** choices. If there are more, the sixth spot becomes **More › 2/3**, which opens the next ring under the same rule. In spell, summon and item lists, the **‹ Back** button by the hero goes back one page (and to the command ring from the first page). In command rings, Back takes one of the six spots on later pages. Outside battle, rings hold up to 8.

## Command ring behind the heroes (v3.84.0)
While a touch command ring is open in battle, the heroes are drawn a second time onto a see-through canvas (`#actorCv`, which ignores taps) placed exactly over the game canvas and above the ring. The hero HP/MP bars move above the ring too. The ring now sits behind the party, and buttons still respond everywhere, even under a sprite.

## Battle commands beside the hero (v3.85.0)
The main battle command ring (Fight, Arts/Magic/Summon, Item, Defend, Row, Run) now uses the same curved column as the spell and item lists, on the enemy side of the active hero. Nothing sits over the party anymore, and it follows the same six-spot / More rule.

## Battle commands on the right (v3.86.0)
All battle command columns (main commands, spells, summons, skills and items) now sit to the **right** of the active hero. Each button is pulled in so it never runs off the screen. Buttons draw on top again: the v3.84 hero overlay is switched off, and the HP bars go back under the ring.

## ✕ on every menu (v3.87.0)
Every menu sheet (Journal, diner screens, Larder, main menu and its Status/Equip/Item screens, Options, Party, shops, the guild, Help, fishing book, saves and so on) has a small **✕** in its top-right corner. It closes every open menu, including ones that would normally reopen the main menu or the Journal, and drops you straight back to the hero in town, dungeon or on the world map. `closeAllSheets()` presses each sheet's own Close button so its usual cleanup still runs, and falls back to `closeSheet`. The title screen, intro, choice prompts and the naming screen don't get the ✕.

## Villagers walk home at dusk (v3.88.0)
When dusk falls (7 pm) while you're in Valemont, Thornwick, Highmere or Ironhold, villagers in view no longer blink out. Each one stops wandering and walks the shortest route (`exitPath`, a breadth-first search over walkable tiles) to the nearest spot outside the screen, stepping around buildings and each other, and disappears once out of sight. Villagers already off-screen simply go home. At dawn everyone is back at their usual spot. Entering a town at night still shows it empty.

## Coralhaven moved up a tile (v3.89.0)
On the world map, Coralhaven now stands one tile north of where it was, so the town no longer overlaps the boardwalk to its pier. The tile it left is grass, so you can walk from the boardwalk straight up into town.

## Inkwell strolls and walks home (v3.91.0)
Inkwell now wanders a small area around his spot in each town, like the villagers. At dusk he walks off the screen instead of vanishing, and he's back at dawn. The dusk walk also got smarter for everyone: routes step around guards, other townsfolk and the hero. In small towns where nowhere is off-screen, people head for the town gate or a house door and go inside.
