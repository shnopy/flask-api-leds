from re import search

def GetArgumentAsString(arguments,key,default):
  if key not in arguments:
    return default
  elif key in arguments and len(arguments[key]) > 0:
    return arguments[key]
  else:
    return default

def GetArgumentAsNumber(arguments,key,default):
  if key not in arguments:
    return default
  elif key in arguments and search(r"\d[.]?",arguments[key]) is not None:
    return float(arguments[key])
  else:
    return default
