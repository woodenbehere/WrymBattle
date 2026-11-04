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
- **Auto battle**: the Auto button hands any heroes you choose to the AI, using one of four strategies (All-Out Attack, Balanced, Protect Allies, Save MP).
- **Phase 2**: the Ember Wyrm becomes the Molten Wyrm. Its elemental weaknesses change and it gains row-targeting attacks.

## Install

Open the play link on a phone or in Chrome/Edge, then use **Add to Home Screen** (iOS Safari: Share → Add to Home Screen). After the first load, it works offline.

## Files

- `index.html`: the whole game (canvas renderer, battle logic, UI)
- `manifest.webmanifest`: PWA metadata
- `sw.js`: service worker for offline play. Bump `VERSION` (and the footer version in `index.html`) when you change files so installed copies update.
- `icons/`: app icons

To run locally, serve the folder over HTTP (for example `python3 -m http.server`) and open `http://localhost:8000`. Service workers don't run from `file://`.
