# WrymBattle

**Ember Wyrm**: a 16-bit style Active Time Battle game in the spirit of Final Fantasy VI, built as an installable Progressive Web App.

Play: https://woodenbehere.github.io/WrymBattle/

## The fight

Five heroes take on a dragon in two phases:

| Hero | Class | Special | Limit break |
|---|---|---|---|
| Garrick | Fighter | Rage Strike, Guard | Meteor Cleave |
| Vesh | Thief | Steal, Mug | Shadow Flurry |
| Ilse | White Mage | Cure, Cure All, Protect, Revive | Seraph's Grace |
| Morrow | Black Mage | Flame, Frost, Thunder | Nova |
| Senna | Summoner | Undine, Sylph, Golem | Leviathan |

- **ATB**: each hero's gauge fills by speed; when it is full, their command menu opens. Wait mode pauses gauges while you choose; Active mode does not.
- **Rows**: the back row halves physical damage dealt and taken. Magic ignores rows.
- **Limit breaks**: the pink gauge fills as a hero takes damage (and when an ally falls).
- **World map**: beat the Ember Wyrm and a top-down world map in the style of Final Fantasy II (SNES) opens, with animated water and surf, forests, mountains and deserts. Walk with the arrow keys or WASD, or press and hold on the map. Visit Ember Peak, Thornwick and Castle Valemont.
- **Random encounters**: Thornhares and Bog Slimes in the grasslands, Grave Wolves in the forest, Sand Rays in the desert, Stone Imps in the hills. Each has its own weaknesses, steals and drops. **Run** escapes most fights, and encounters can be turned off from the map menu.
- **Camp**: rest anywhere on the map to restore all HP and MP and revive fallen heroes. Party HP, MP and items carry over between battles.
- **Towns and shops**: Valemont Village beside the castle has a weapon shop, armor shop, item shop, magic shop and inn. Thornwick has an item shop and inn. Tap a building or pick it from the menu.
- **Equipment**: five slots per hero (Weapon, Shield, Head, Body, Accessory) with class restrictions, stat comparisons in the shop, and an Optimize button on the Party screen.
- **Progression**: monsters give EXP and Gil. Heroes start at Lv 10 and grow with class-specific stats up to Lv 60. The magic shop teaches new spells (Cura, Holy, Fira, Blizzara, Thundara, and the Glacia and Raijin summons).
- **Saving**: progress saves automatically in your browser once the Ember Wyrm falls. Start over from the ? panel.
- **Group battles**: fights against up to four enemies, each with its own turn gauge and health bar. Pick a target from the menu (a cursor marks it on screen); summons hit every enemy.
- **Bestiary**: Thornhare, Goblin, Bog Slime, Grave Wolf, Mandrake, Dusk Bat, Sand Ray, Dune Scorpion, Stone Imp, Ash Salamander, the Hill Ogre, and the Vault Sentinel with its Ward Orbs.
- **Castle Valemont**: walk inside to meet King Aldous and Queen Mirelle in the throne room, rest in the guest rooms, loot the armory, and earn the Royal Key by slaying the Hill Ogre. The vault is locked, guarded by Captain Brann, and protected by an ancient sentinel.
- **Auto battle**: the Auto button hands any heroes you choose to the AI, using one of four strategies (All-Out Attack, Balanced, Protect Allies, Save MP). Each hero can also get a habit, such as Thief: Always Mug, that overrides the strategy whenever it can.
- **Phase 2**: the Ember Wyrm becomes the Molten Wyrm. Its elemental weaknesses change and it gains row-targeting attacks.

## Install

Open the play link on a phone or in Chrome/Edge, then use **Add to Home Screen** (iOS Safari: Share → Add to Home Screen). After the first load, it works offline. To force the newest version, tap the version number in the footer twice.

## Files

- `index.html`: the whole game (canvas renderer, battle logic, UI)
- `manifest.webmanifest`: PWA metadata
- `sw.js`: service worker for offline play. When you change files, bump `VERSION` here and `APP_VERSION` (plus the footer button text) in `index.html`.
- `icons/`: app icons

To run locally, serve the folder over HTTP (for example `python3 -m http.server`) and open `http://localhost:8000`. Service workers don't run from `file://`.
