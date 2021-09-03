def parse_name(name):
    parsed_name = {
        "has_prefix": False,
        "prefix": "",
        "has_suffix": False,
        "suffix": "",
        "plus_one": False,
        "name": ""
    }

    if name[0] == '"':
        parsed_name["has_prefix"] = True
        split_name = name.split('"')
        parsed_name["prefix"] = split_name[1]
        name = split_name[2][1:]  # NOTE - We're trimming the leading whitespace. We're modifying our `name` arg

    if " of " in name:
        parsed_name["has_suffix"] = True
        split_name = name.split(" of ")
        parsed_name["suffix"] = "of " + split_name[1]
        # Check for +1
        if " +1" in parsed_name["suffix"]:
            parsed_name["plus_one"] = True
            parsed_name["suffix"] = parsed_name["suffix"].replace(" +1", "")
        name = split_name[0]  # NOTE - We're modifying our `name` arg

    parsed_name["name"] = name
    return parsed_name
