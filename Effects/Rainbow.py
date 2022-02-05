from LedControl import SetLEDColour
from time import sleep
from random import randint

from GetArguments import GetArgumentAsNumber

shouldLoop = True


def Run(args):
  global shouldLoop
  shouldLoop = True

  iterations = GetArgumentAsNumber(args, "iterations", 1)
  fadeTime = GetArgumentAsNumber(args, "fade_time", 0.01)

  for _ in range(int(iterations)):
    print(f"Should loop: {shouldLoop}")
    if shouldLoop:
      colour = [randint(0, 255), randint(0, 255), randint(0, 255)]
      SetLEDColour(colour, "true", fadeTime, "true")
      print(f"Fadetime: {fadeTime}")
      sleep(fadeTime)
    else:
      break

# Don't touch this function
def Stop():
  global shouldLoop
  shouldLoop = False


help = {
    "arguments": {
        "iterations": {"type": "number", "min": 1, "max": 100},
        "fade_time": {"type": "number", "min": 0, "max": 0.1},
    },
    "description": "Rainbow fade effect",
}
