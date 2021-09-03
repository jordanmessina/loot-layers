let parseName = (name) => {
  let parsedName = {
    hasPrefix: false,
    prefix: "",
    hasSuffix: false,
    suffix: "",
    plusOne: false,
    name: ""
  }

  let splitName;

  // Check for prefix
  if(name[0] === "\"") {
    parsedName.hasPrefix = true;
    splitName = name.split("\"");
    parsedName.prefix = splitName[1];
    name = splitName[2];  // NOTE - we modify the function arg `name`
  }

  // Check for suffix
  if(name.indexOf(" of ") >= 0) {
    parsedName.hasSuffix = true;
    splitName = name.split(" of ");
    parsedName.suffix = "of " + splitName[1];
    if(parsedName.suffix.indexOf(" +1") >= 0) {
      parsedName.plusOne = true;
      parsedName.suffix = parsedName.suffix.split(" +1")[0];
    }
    name = splitName[0];  // NOTE - we modify the function arg `name`
  }

  parsedName.name = name.trim();

  return parsedName;
}
