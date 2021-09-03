import json
import os
import shutil

from parse_name import parse_name


# Open loot file
with open('data/loot.json', 'r') as loot_file:
    data = json.load(loot_file)


def get_loot(loot_name):
    return [
        bag[list(bag.keys())[0]][loot_name]
        for bag in data
    ]


# Get all weapon loot names
weapon_loot = get_loot("weapon")

# Get all chest loot names
chest_loot = get_loot("chest")

# Get all head loot names
head_loot = get_loot("head")

# Get all waist loot names
waist_loot = get_loot("waist")

# Get all foot loot names
foot_loot = get_loot("foot")

# Get all hand loot names
hand_loot = get_loot("hand")

# Get all neck loot names
neck_loot = get_loot("neck")

# Get all ring loot names
ring_loot = get_loot("ring")


# We will populate this mapping file
mapping = {
    "VERSION": "0.0.1"
}


# A little gross, but whatever
def add_loot_to_mapping(name, items):
    # Dirs
    top_dir = f"{name}/"
    main_dir = f"{top_dir}name/"
    prefix_dir = f"{top_dir}prefix/"
    suffix_dir = f"{top_dir}suffix/"
    plus_one_dir = f"{top_dir}plus_one/"

    mapping[name] = {
        "prefix": f"{prefix_dir}prefix.png",
        "suffix": {},
        "plus_one": f"{plus_one_dir}plus_one.png",
        "name": {},
    }
    
    for item_name in items:
        parsed = parse_name(item_name)
    
        # Name
        parsed_name = parsed["name"]
        png_name = parsed_name.replace("'", "").replace(" ", "_").lower() + ".png"
        mapping[name]["name"][parsed_name] = f"{main_dir}{png_name}"
    
        # Suffix
        if parsed_name not in mapping[name]["suffix"]:
            mapping[name]["suffix"][parsed_name] = {}
        parsed_suffix = parsed["suffix"]
        if parsed_suffix:
            png_suffix = png_name.replace(".png", "") + "_" + parsed_suffix.replace(" ", "_").lower() + ".png"
            mapping[name]["suffix"][parsed_name][parsed_suffix] = f"{suffix_dir}{png_suffix}"


add_loot_to_mapping("weapon", weapon_loot)
add_loot_to_mapping("chest", chest_loot)
add_loot_to_mapping("head", head_loot)
add_loot_to_mapping("waist", waist_loot)
add_loot_to_mapping("foot", foot_loot)
add_loot_to_mapping("hand", hand_loot)
add_loot_to_mapping("neck", neck_loot)
add_loot_to_mapping("ring", ring_loot)


# Write the mapping
with open('./build/mapping.json', 'w') as mapping_file:
    mapping_file.write(json.dumps(mapping, indent=4))


blank_png_path = "./img/blank.png"
character_img_path = ('./build/character_imgs/')

# Check if an image directory already exists. If so, delete
if os.path.isdir(character_img_path):
    shutil.rmtree(character_img_path)

# Create the image directory
os.mkdir(character_img_path)

# Remove the version metadata
del(mapping["VERSION"])

# Traverse the dict and write all paths
for item in mapping:
    item_path = f"{character_img_path}{item}/"
    os.mkdir(item_path)
    for item_attr in mapping[item].keys():
        if item_attr == "prefix":
            prefix_path = f"{item_path}prefix/"
            os.mkdir(prefix_path)
            png_path = f"{prefix_path}prefix.png"
            shutil.copy(blank_png_path, png_path)
        if item_attr == "plus_one":
            plus_one_path = f"{item_path}plus_one/"
            os.mkdir(plus_one_path)
            png_path = f"{plus_one_path}plus_one.png"
            shutil.copy(blank_png_path, png_path)
        if item_attr == "name":
            name_path =  f"{item_path}name/"
            os.mkdir(name_path)
            for item_name in mapping[item][item_attr].keys():
                png_path = f"{character_img_path}{mapping[item][item_attr][item_name]}"
                shutil.copy(blank_png_path, png_path)
        if item_attr == "suffix":
            suffix_path =  f"{item_path}suffix/"
            os.mkdir(suffix_path)
            for item_name in mapping[item][item_attr].keys():
                for suffix in mapping[item][item_attr][item_name].keys():
                    png_path = f"{character_img_path}{mapping[item][item_attr][item_name][suffix]}"
                    shutil.copy(blank_png_path, png_path)


# Add fg/bg img
shutil.copy(blank_png_path, f"{character_img_path}bg.png")
shutil.copy(blank_png_path, f"{character_img_path}fg.png")


# Create the layering json obj
layer_order = [
  "bg", "fg",
  "weaponName", "weaponPrefix", "weaponSuffix", "weaponPlusOne",
  "chestName", "chestPrefix", "chestSuffix", "chestPlusOne",
  "headName", "headPrefix", "headSuffix", "headPlusOne",
  "waistName", "waistPrefix", "waistSuffix", "waistPlusOne",
  "footName", "footPrefix", "footSuffix", "footPlusOne",
  "handName", "handPrefix", "handSuffix", "handPlusOne",
  "neckName", "neckPrefix", "neckSuffix", "neckPlusOne",
  "ringName", "ringPrefix", "ringSuffix", "ringPlusOne",
]

with open('./build/layers.json', 'w') as layer_file:
    layer_file.write(json.dumps(layer_order, indent=4))
