from LedControl import strip,SetLEDColour
from rpi_ws281x import Color
from time import sleep
from random import randint

from GetArguments import GetArgumentAsNumber

def Run(args):
  iterations = GetArgumentAsNumber(args,"iterations",1)
  fadeTime = GetArgumentAsNumber(args,"fade_time",0.01)

  for _ in range(int(iterations)):
    colour = [randint(0,255),randint(0,255),randint(0,255)]
    SetLEDColour(colour,True,fadeTime)


help = {
  "arguments": {
    "iterations": {
      "type": "number",
      "min": 1,
      "max": 100
    },
    "fade_time": {
      "type": "number",
      "min": 0,
      "max": 0.5
    }
  },
  "description": "Rainbow fade effect"
}