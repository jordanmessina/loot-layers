# Loot Layers

An opinionated layering pattern for building visuals from your [Loot](https://www.lootproject.com/).

Inspired by `dom` and this conversation in Discord: [https://discord.com/channels/880899217973968917/881141224776531998/882052146646900827](https://discord.com/channels/880899217973968917/881141224776531998/882052146646900827)

## About

The goal of this project is to allow an artist to quickly and easily create a Layer Pack for generatign visuals of [Loots](https://www.lootproject.com/).

A Layer Pack consists of 3 main parts:

### `mapping.json`

Provides a mapping from attributes of a Loot's name to a relative file path pointing to a png. The structure looks like:
```
{
    "VERSION": "0.0.1",
    "weapon": {
        "prefix": "weapon/prefix/prefix.png",
        "suffix": {
            "Grave Wand": {
                "of Skill": "weapon/suffix/grave_wand_of_skill.png",
                "of Protection": "weapon/suffix/grave_wand_of_protection.png",
                "of Brilliance": "weapon/suffix/grave_wand_of_brilliance.png",
                "of Giants": "weapon/suffix/grave_wand_of_giants.png",
                "of Vitriol": "weapon/suffix/grave_wand_of_vitriol.png",
                "of Detection": "weapon/suffix/grave_wand_of_detection.png",
                "of the Twins": "weapon/suffix/grave_wand_of_the_twins.png",
                "of Rage": "weapon/suffix/grave_wand_of_rage.png"
            },
            "Bone Wand": {
                "of Perfection": "weapon/suffix/bone_wand_of_perfection.png",
                "of Reflection": "weapon/suffix/bone_wand_of_reflection.png",
                "of Anger": "weapon/suffix/bone_wand_of_anger.png",
                "of Power": "weapon/suffix/bone_wand_of_power.png",
                "of Titans": "weapon/suffix/bone_wand_of_titans.png",
                "of the Fox": "weapon/suffix/bone_wand_of_the_fox.png",
                "of Enlightenment": "weapon/suffix/bone_wand_of_enlightenment.png",
                "of Fury": "weapon/suffix/bone_wand_of_fury.png"
            },
            "Katana": {
                "of Rage": "weapon/suffix/katana_of_rage.png",
                "of Protection": "weapon/suffix/katana_of_protection.png",
                "of Skill": "weapon/suffix/katana_of_skill.png",
                "of Brilliance": "weapon/suffix/katana_of_brilliance.png",
                "of the Twins": "weapon/suffix/katana_of_the_twins.png",
                "of Detection": "weapon/suffix/katana_of_detection.png",
                etc.
            etc.
        },
        "plus_one": "weapon/plus_one/plus_one.png",
        "name": {
            "Grave Wand": "weapon/name/grave_wand.png",
            "Bone Wand": "weapon/name/bone_wand.png",
            "Katana": "weapon/name/katana.png",
            "Scimitar": "weapon/name/scimitar.png",
            "Maul": "weapon/name/maul.png",
            "Long Sword": "weapon/name/long_sword.png",
            "Ghost Wand": "weapon/name/ghost_wand.png",
            "Short Sword": "weapon/name/short_sword.png",
            "Warhammer": "weapon/name/warhammer.png",
            "Chronicle": "weapon/name/chronicle.png",
            "Book": "weapon/name/book.png",
            "Tome": "weapon/name/tome.png",
            "Quarterstaff": "weapon/name/quarterstaff.png",
            "Grimoire": "weapon/name/grimoire.png",
            "Falchion": "weapon/name/falchion.png",
            "Mace": "weapon/name/mace.png",
            "Club": "weapon/name/club.png",
            "Wand": "weapon/name/wand.png"
        }
    },
    "chest": {
        "prefix": "chest/prefix/prefix.png",
        "suffix": {
            "Hard Leather Armor": {
                "of Skill": "chest/suffix/hard_leather_armor_of_skill.png",
                "of Giants": "chest/suffix/hard_leather_armor_of_giants.png",
                "of Protection": "chest/suffix/hard_leather_armor_of_protection.png",
                "of Rage": "chest/suffix/hard_leather_armor_of_rage.png",
                etc.
            etc.
       etc.
    }
}
```

If necessary, an artist can change the relative path for any Loot attribute.

### `layers.json`

The ordering of the layers:
```
[
    "bg",
    "fg",
    "weaponName",
    "weaponPrefix",
    "weaponSuffix",
    "weaponPlusOne",
    "chestName",
    "chestPrefix",
    "chestSuffix",
    "chestPlusOne",
    "headName",
    "headPrefix",
    "headSuffix",
    "headPlusOne",
    "waistName",
    "waistPrefix",
    "waistSuffix",
    "waistPlusOne",
    "footName",
    "footPrefix",
    "footSuffix",
    "footPlusOne",
    "handName",
    "handPrefix",
    "handSuffix",
    "handPlusOne",
    "neckName",
    "neckPrefix",
    "neckSuffix",
    "neckPlusOne",
    "ringName",
    "ringPrefix",
    "ringSuffix",
    "ringPlusOne"
]
```


### Images

Where the magic happens. The structure of this is broken down by item:
```
├── bg.png
├── fg.png
├── chest
│   ├── name
│   │   ├── chain_mail.png
│   │   ├── demon_husk.png
│   │   ├── divine_robe.png
│   │   ├── dragonskin_armor.png
│   │   ├── hard_leather_armor.png
│   │   ├── holy_chestplate.png
│   │   ├── leather_armor.png
│   │   ├── linen_robe.png
│   │   ├── ornate_chestplate.png
│   │   ├── plate_mail.png
│   │   ├── ring_mail.png
│   │   ├── robe.png
│   │   ├── shirt.png
│   │   ├── silk_robe.png
│   │   └── studded_leather_armor.png
│   ├── plus_one
│   │   └── plus_one.png
│   ├── prefix
│   │   └── prefix.png
│   └── suffix
│       ├── chain_mail_of_anger.png
│       ├── chain_mail_of_brilliance.png
│       ├── chain_mail_of_detection.png
│       ├── studded_leather_armor_of_titans.png
│       └── etc.
├── foot
│   ├── name
│   │   ├── chain_boots.png
│   │   ├── demonhide_boots.png
│   │   ├── divine_slippers.png
│   │   ├── dragonskin_boots.png
│   │   ├── greaves.png
│   │   ├── hard_leather_boots.png
│   │   ├── heavy_boots.png
│   │   ├── holy_greaves.png
│   │   ├── leather_boots.png
│   │   ├── linen_shoes.png
│   │   ├── ornate_greaves.png
│   │   ├── shoes.png
│   │   ├── silk_slippers.png
│   │   ├── studded_leather_boots.png
│   │   └── wool_shoes.png
│   ├── plus_one
│   │   └── plus_one.png
│   ├── prefix
│   │   └── prefix.png
│   └── suffix
│       ├── chain_boots_of_anger.png
│       ├── chain_boots_of_brilliance.png
│       ├── demonhide_boots_of_skill.png
│       ├── demonhide_boots_of_the_fox.png
│       └── etc.
├── hand
│   └── etc.
├── head
│   └── etc.
├── neck
│   └── etc.
├── ring
│   └── etc.
├── waist
│   └── etc.
└── weapon
    └── etc.
```

NOTE - we didn't break down the prefixes, so there's only a single png for when an item has prefix.


