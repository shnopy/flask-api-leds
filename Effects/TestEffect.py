from LedControl import strip
from rpi_ws281x import Color
from time import sleep
from random import randint

from GetArguments import GetArgumentAsNumber

def Run(args):
  iterations = GetArgumentAsNumber(args,"iterations",1)
  speed = GetArgumentAsNumber(args,"speed",0.1)

  print(f"ITERATIONS: {int(iterations)}, SPEED: {speed}")
  for _ in range(int(iterations)):
    for i in range(strip.numPixels()):
      colour = [randint(0,255),randint(0,255),randint(0,255)]
      strip.setPixelColor(i,Color(colour[0],colour[1],colour[2]))
      sleep(speed)
      strip.show()


help = {
  "arguments": {
    "speed": {
      "type": "number",
      "min": 0,
      "max": 1
    },
    "iterations": {
      "type": "number",
      "min": 1,
      "max": 50
    }
  },
  "description": "Testing effect"
}