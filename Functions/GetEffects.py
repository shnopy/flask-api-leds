from os import listdir


def GetEffects():
  effects = {}

  for file in listdir("./Effects"):
    if len(file.split(".")) == 2 and file.split(".")[1] == "py":
      effectImport = __import__(file.split(".")[0])
      if hasattr(effectImport, "help"):
        effects[file.split(".")[0]] = effectImport.help
      else:
        effects[file.split(".")[0]] = "No help provided"

  return effects
