from LedControl import SetLEDColour
from time import sleep
from random import randint

from GetArguments import GetArgumentAsBool


shouldLoop = True


def Run(args):
  global shouldLoop
  shouldLoop = True

  while True:
    if shouldLoop:
      colour = [randint(0, 255), randint(0, 255), randint(0, 255)]
      fadeTime = 0.001

      SetLEDColour(colour, "true", fadeTime, "true")

      sleep(fadeTime)
    else:
      break


# Don't touch this function

def Stop():
  global shouldLoop
  shouldLoop = False


help = {
    "arguments": {

    },
    "description": "Infinite fade effect with random colours and fade times",
}
