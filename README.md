# Loot Layers

An opinionated layering pattern for generating visuals from your [Loot](https://www.lootproject.com/).

Inspired by `dom` and this conversation in Discord: [https://discord.com/channels/880899217973968917/881141224776531998/882052146646900827](https://discord.com/channels/880899217973968917/881141224776531998/882052146646900827)

WARNING - At the moment, this is truly some janky code. Dive into it at your own risk.

## TLDR

If you just want to get started creating a Layer Pack, check out the [Loot Layers Playground Repo](https://github.com/jordanmessina/loot-layers-playground)

## How it works

The goal of this project is to allow an artist to quickly and easily create a Layer Pack for generatign visuals of [Loots](https://www.lootproject.com/).

An artist needs to only modify the parts of the image directory structure that they care about, while leaving the rest as empty pngs.

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

### Tying it all together

You can break down each item in a Loot bag as follows (example is for the `hand` item `"Victory Moon" Hard Leather Gloves of the Twins +1`):
```
{
    'has_prefix': True,
    'prefix': 'Victory Moon',
    'has_suffix': True,
    'suffix': 'of the Twins',
    'plus_one': True,
    'name': 'Hard Leather Gloves'
}
```

With this structure, you can determine which pngs are needed for this item. Example parsers are in the `parsers` directory. Once you determine your png path for each part of the item, you should map then to their corresponding layer name.

Example:

```
import json

from parse_name import parse_name


with open('mapping.json', 'r') as mapping_file:
    mapping = json.load(mapping_file)

with open('layers.json', 'r') as layers_file:
    layers_order = json.load(layers_file)


IMG_DIR = "./path/to/imgs/dir"

LOOT =  {
  "chest": "Hard Leather Armor",
  "foot": "\"Death Root\" Ornate Greaves of Skill",
  "hand": "Studded Leather Gloves",
  "head": "Divine Hood",
  "neck": "Necklace of Enlightenment",
  "ring": "Gold Ring",
  "waist": "Hard Leather Belt",
  "weapon": "\"Grim Shout\" Grave Wand of Skill +1"
}

LAYERS = {
    "fg": f"{IMG_DIR}/fg.png", "bg": f"{IMG_DIR}/bg.png",   # Foreground & Background are at the root
    "weaponName": None, "weaponPrefix": None, "weaponSuffix": None, "weaponPlusOne": None,
    "chestName": None, "chestPrefix": None, "chestSuffix": None, "chestPlusOne": None,
    "headName": None, "headPrefix": None, "headSuffix": None, "headPlusOne": None,
    "waistName": None, "waistPrefix": None, "waistSuffix": None, "waistPlusOne": None,
    "footName": None, "footPrefix": None, "footSuffix": None, "footPlusOne": None,
    "handName": None, "handPrefix": None, "handSuffix": None, "handPlusOne": None,
    "neckName": None, "neckPrefix": None, "neckSuffix": None, "neckPlusOne": None,
    "ringName": None, "ringPrefix": None, "ringSuffix": None, "ringPlusOne": None,
}


def update_layers(loot_name, loot):
    parsed_name = parse_name(loot)

    # Main item
    LAYERS[f"{loot_name}Name"] = f"{IMG_DIR}/{mapping[loot_name]['name'][parsed_name['name']]}"

    # Prefix
    if parsed_name["prefix"]:
        LAYERS[f"{loot_name}Prefix"] = f"{IMG_DIR}/{mapping[loot_name]['prefix']}"

    # Suffix
    if parsed_name["suffix"]:
        LAYERS[f"{loot_name}Suffix"] = f"{IMG_DIR}/{mapping[loot_name]['suffix'][parsed_name['name']][parsed_name['suffix']]}"

    # +1
    if parsed_name["plus_one"]:
        LAYERS[f"{loot_name}PlusOne"] = f"{IMG_DIR}/{mapping[loot_name]['plus_one']}"


update_layers("weapon", LOOT["weapon"])
update_layers("chest", LOOT["chest"])
update_layers("head", LOOT["head"])
update_layers("waist", LOOT["waist"])
update_layers("foot", LOOT["foot"])
update_layers("hand", LOOT["hand"])
update_layers("neck", LOOT["neck"])
update_layers("ring", LOOT["ring"])

for layer_name in layers_order:
    if LAYERS[layer_name]:
        print(LAYERS[layer_name])
```

Which would output the file paths:
```
./path/to/imgs/dir/bg.png
./path/to/imgs/dir/fg.png
./path/to/imgs/dir/weapon/name/grave_wand.png
./path/to/imgs/dir/weapon/prefix/prefix.png
./path/to/imgs/dir/weapon/suffix/grave_wand_of_skill.png
./path/to/imgs/dir/weapon/plus_one/plus_one.png
./path/to/imgs/dir/chest/name/hard_leather_armor.png
./path/to/imgs/dir/head/name/divine_hood.png
./path/to/imgs/dir/waist/name/hard_leather_belt.png
./path/to/imgs/dir/foot/name/ornate_greaves.png
./path/to/imgs/dir/foot/prefix/prefix.png
./path/to/imgs/dir/foot/suffix/ornate_greaves_of_skill.png
./path/to/imgs/dir/hand/name/studded_leather_gloves.png
./path/to/imgs/dir/neck/name/necklace.png
./path/to/imgs/dir/neck/suffix/necklace_of_enlightenment.png
./path/to/imgs/dir/ring/name/gold_ring.png
```

Now one simply needs to layer this images on top of each other.


## Tooling

### `generate_mapping`

Generates a clean Layer Pack structure with an image directory fully populated with empty pngs. If you want a different sized image, change the `blank.png` file.


### `generate_pngs`

Creates fully rendered pngs from a Layer Pack.
