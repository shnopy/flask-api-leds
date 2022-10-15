from LedControl import SetLEDColour, defaultColour
from time import sleep
from random import randint, uniform

from GetArguments import GetArgumentAsRGB, GetArgumentAsNumber

shouldLoop = True


def Run(args):
  global shouldLoop
  shouldLoop = True

  colour = GetArgumentAsRGB(args, "colour", defaultColour)
  fadeTime = GetArgumentAsNumber(args, "fade_time", 0.01)

  while True:
    if shouldLoop:
      SetLEDColour(colour, "true", fadeTime, "true")

      sleep(fadeTime)

      SetLEDColour([0, 0, 0], "true", fadeTime, "true")

      sleep(fadeTime)
    else:
      break


# Don't touch this function

def Stop():
  global shouldLoop
  shouldLoop = False


help = {
    "arguments": {
        "colour": {"type": "text"},
        "fade_time": {"type": "number", "min": 0, "max": 0.1},
    },
    "description": "A breathing effect",
}
