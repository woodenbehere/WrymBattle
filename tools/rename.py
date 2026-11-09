#!/usr/bin/env python3
"""v3.48: scrub Final Fantasy names from player-facing text (display names only; save keys stay the same).
RULES is also imported by tools/changelog.py so old changelog lines use the new names."""
import re, sys
RULES = [
 # spells
 (r"\bCure All\b", "Mend All"), (r"\bCuraga\b", "Grand Mend"), (r"\bCura\b", "Greater Mend"), (r"\bCure\b(?! [a-z])", "Mend"),
 (r"\bFiraga\b", "Firestorm"), (r"\bFira\b", "Blaze"), (r"\bBlizzaga\b", "Glacier"), (r"\bBlizzara\b", "Hailstorm"),
 (r"\bThundaga\b", "Stormcall"), (r"\bThundara\b", "Thunderbolt"),
 (r"\bHoly\b(?! [A-Za-z])", "Radiance"), (r"\bFlare\b", "Sunburst"), (r"\bUltima\b", "Oblivion"), (r"\bMeteor\b(?! Cleave)", "Skyfall"),
 (r"\bBio\b", "Blight"), (r"\bQuake\b", "Tremor"), (r"\bOsmose\b", "Mana Siphon"), (r"\bArise\b", "Rebirth"), (r"\bRegen\b", "Renew"),
 (r"\bProtect\b(?! Allies)", "Bulwark"), (r"\bShell\b", "Spellguard"),
 # summons
 (r"\bMegaflare\b", "Sovereign Flame"), (r"\bBahamut\b", "Drakonis"), (r"\bHellfire\b", "Cinderstorm"), (r"\bIfrit\b", "Pyralis"),
 (r"\bZantetsuken\b", "Severing Stroke"), (r"\bOdin\b", "Valgard"), (r"\bDivine Judgment\b", "Final Verdict"), (r"\bAlexander\b", "Bastion"),
 (r"\bLeviathan\b", "Thalassa"), (r"Gaia’s Wrath", "Worldbreaker"), (r"\bTitan\b", "Gaian"), (r"\bRebirth Flame\b", "Ashen Dawn"),
 (r"\bPhoenix Feather\b", "Life Feather"), (r"\bPhoenix Palm\b", "Rising Palm"), (r"\bPhoenix\b", "Emberwing"), (r"\bEidolon\b", "Spirit"),
 # items and gear
 (r"\bHi-Potion", "Greater Potion"), (r"\bX-Potion", "Grand Potion"), (r"\bHi-Ether", "Greater Tonic"), (r"\bEthers\b", "Mana Tonics"), (r"\bEther\b", "Mana Tonic"),
 (r"\bMegalixir", "Grand Elixir"), (r"\bGold Needles?\b", "Stonebalm"), (r"\bRibbon\b", "Warding Sash"), (r"\bEconomizer rings\b", "Thrift Rings"), (r"\bEconomizers\b", "Thrift Rings"), (r"\bEconomizer\b", "Thrift Ring"),
 (r"\bMythril\b", "Silversteel"), (r"\bGenji Helm\b", "Ronin Helm"), (r"\bSahagin\b", "Reefkin"),
 # abilities, systems, money
 (r"\bMug\b", "Plunder"), (r"\bChakra\b", "Inner Focus"), (r"\bLimit breaks?\b", "Fury"), (r"\blimit breaks?\b", "fury"), (r"\bLimit\b", "Fury"),
 (r"\bATB\b", "turn"), (r"\bActive Time Battle\b", "charge-time battle"),
 (r"\bGil\b", "Gold"), (r"(?<=[\w,!.] )gil(?=[ ,.!'’\]<])", "gold"),
 # classes
 (r"\bWhite Mage\b", "Cleric"), (r"\bWhite Wizards\b", "High Clerics"), (r"\bWhite Wizard\b", "High Cleric"), (r"\bBlack Mage\b", "Sorcerer"),
 (r"\bBlack Wizard:", "Sorcerer:"), (r"\bBlack Wizard\b", "Archmage"), (r"\bblack wizards\b", "sorcerers"), (r"\bblack wizard\b", "sorcerer"),
 # v3.50: wyrms are dragons
 (r"\bWyrmscale\b", "Dragonscale"), (r"\bWyrmbone\b", "Dragonbone"), (r"\bWyrms\b", "Dragons"), (r"\bWyrm\b", "Dragon"),
 (r"(?<![\w'.\-/`$])wyrms\b", "dragons"), (r"(?<![\w'.\-/`$])wyrm\b(?![\w'(=:\-.\[])", "dragon"),
 # night-monster spells added in v3.47 (FSPELL names)
 (r"name:'Fire',mp:5", "name:'Flame',mp:5"), (r"name:'Blizzard',mp:5", "name:'Frost',mp:5"), (r"name:'Aqua',mp:5", "name:'Torrent',mp:5"),
 (r"cast basic spells: Fire, Blizzard, Thunder, Aqua", "cast basic spells: Flame, Frost, Thunder, Torrent"),
 (r"spells like Fire, Blizzard, Drain", "spells like Flame, Frost, Drain"),
]
def scrub(text, counts=None):
    for pat, rep in RULES:
        text, n = re.subn(pat, rep, text)
        if counts is not None: counts[pat] = counts.get(pat, 0) + n
    return text
if __name__ == '__main__':
    for path in sys.argv[1:]:
        c = {}; s = open(path).read(); s2 = scrub(s, c); open(path, 'w').write(s2)
        print(path, sum(c.values()), 'changes'); print('  ', {k: v for k, v in c.items() if v})
