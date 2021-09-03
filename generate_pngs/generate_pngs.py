import json
import os
import shutil

from PIL import Image

from parse_name import parse_name


with open('./data/loot.json', 'r') as loot_file:
    loot_bags = json.load(loot_file)

with open('./data/mapping.json', 'r') as mapping_file:
    mapping = json.load(mapping_file)

with open('./data/layers.json', 'r') as layers_file:
    layers = json.load(layers_file)


LAYERS = {
    "fg": None,
    "bg": None,
    "weaponName": None,
    "weaponPrefix": None,
    "weaponSuffix": None,
    "weaponPlusOne": None,
    "chestName": None,
    "chestPrefix": None,
    "chestSuffix": None,
    "chestPlusOne": None,
    "headName": None,
    "headPrefix": None,
    "headSuffix": None,
    "headPlusOne": None,
    "waistName": None,
    "waistPrefix": None,
    "waistSuffix": None,
    "waistPlusOne": None,
    "footName": None,
    "footPrefix": None,
    "footSuffix": None,
    "footPlusOne": None,
    "handName": None,
    "handPrefix": None,
    "handSuffix": None,
    "handPlusOne": None,
    "neckName": None,
    "neckPrefix": None,
    "neckSuffix": None,
    "neckPlusOne": None,
    "ringName": None,
    "ringPrefix": None,
    "ringSuffix": None,
    "ringPlusOne": None,
}

IMG_DIR = "./data/character_imgs"
BUILD_DIR = "./build/imgs"

# Check if an image directory already exists. If so, delete
if os.path.isdir(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)

os.mkdir(BUILD_DIR)


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


# Yuck
def reset_layers():
    for key in LAYERS:
        LAYERS[key] = None


for index, loot_bag in enumerate(loot_bags):
    loot = loot_bag[str(index+1)]
    update_layers("weapon", loot["weapon"])
    update_layers("chest", loot["chest"])
    update_layers("head", loot["head"])
    update_layers("waist", loot["waist"])
    update_layers("foot", loot["foot"])
    update_layers("hand", loot["hand"])
    update_layers("neck", loot["neck"])
    update_layers("ring", loot["ring"])

    LAYERS["bg"] = f"{IMG_DIR}/bg.png"
    LAYERS["fg"] = f"{IMG_DIR}/fg.png"

    filename = str(index+1).zfill(4)
    image = Image.open(LAYERS[layers[0]])
    for layer in layers[1:]:
        if LAYERS[layer]:
            layer_image = Image.open(LAYERS[layer])
            image.paste(layer_image, (0,0), layer_image)
    image.save(f"{BUILD_DIR}/{filename}.png", "PNG")
    reset_layers()
