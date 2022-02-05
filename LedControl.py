# Imports
from re import match
from time import sleep
from rpi_ws281x import Color, PixelStrip, ws
from copy import copy

#
# https://github.com/rpi-ws281x/rpi-ws281x-python/blob/f35d40a56c3a3ae854a6a601fecc9fa8bc92f5dc/examples/SK6812_strandtest.py#L47
#

# Variables
defaultColour = [255, 50, 100]

isOn = False
currentColour = {
    "red": defaultColour[0],
    "green": defaultColour[1],
    "blue": defaultColour[2],
}
currentEffect = ""
currentEffectArguments = {}
currentEffectHelp = {}
strip = None


# LED Variables
LED_COUNT = 30  # Number of LED pixels.
LED_PIN = 13  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_CHANNEL = 1

strip = PixelStrip(
    LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL
)
strip.begin()

# Private


def __FindLargest(numbers):
  largest = 0
  for i in range(len(numbers)):
    if largest == 0 or numbers[i] > largest:
      largest = numbers[i]

  return largest


def __StripSpaces(value):
  return value.strip()


def __ValidateRGB(toCheck):
  if isOn:
    RGBArray = {}
    toCheck = list(map(__StripSpaces, toCheck))

    if len(toCheck) < 3:
      return "RGB array does not include all three values!"
    else:
      for index, value in enumerate(toCheck):
        if match(r"-?\d", str(value)) is not None:
          valueAsInt = int(value)

          if valueAsInt > 255:
            RGBArray[index] = 255
          elif valueAsInt < 0:
            RGBArray[index] = 0
          else:
            RGBArray[index] = valueAsInt
        else:
          return f"Given value {value} is not a valid number!"

      rgb = {"red": RGBArray[0], "green": RGBArray[1], "blue": RGBArray[2]}

      return rgb
  else:
    return "LEDs are not currently on!"


def __FadeColour(r, g, b, fadeTime=0.01):
  largest = 0
  largestNumber = __FindLargest([r, g, b])
  largestCurrent = __FindLargest(list(currentColour.values()))

  initial = GetLEDColour()
  internalR = initial["red"]
  internalG = initial["green"]
  internalB = initial["blue"]

  if largestCurrent > largestNumber:
    largest = largestCurrent
  else:
    largest = largestNumber

  currentColour["red"] = r
  currentColour["green"] = g
  currentColour["blue"] = b

  for i in range(largest):
    # print(g < initial["green"],g,initial["green"])
    if r > initial["red"] and internalR < r:
      internalR += 1
    if r < initial["red"] and internalR > r:
      internalR -= 1

    if g > initial["green"] and internalG < g:
      internalG += 1
    if g < initial["green"] and internalG > g:
      internalG -= 1

    if b > initial["blue"] and internalB < b:
      internalB += 1
    if b < initial["blue"] and internalB > b:
      internalB -= 1

    for x in range(strip.numPixels()):
      strip.setPixelColor(x, Color(internalR, internalG, internalB))

    sleep(fadeTime)
    strip.show()


def __SetColour(r, g, b):

  print(f"SETTING COLOUR TO: {r,g,b}")

  currentColour["red"] = r
  currentColour["green"] = g
  currentColour["blue"] = b

  for i in range(strip.numPixels()):
    strip.setPixelColor(i, Color(r, g, b))

  strip.show()


# Public


def SetLEDColour(colour, fade="false", fadeTime=0.01, override="false"):
  if currentEffect == "" or override.lower() == "true":
    RGB = __ValidateRGB(toCheck=colour)

    if len(RGB) == 3:
      if fade == "true":
        __FadeColour(RGB["red"], RGB["green"], RGB["blue"], fadeTime)
      else:
        __SetColour(RGB["red"], RGB["green"], RGB["blue"])

      return RGB


def DisableLEDs():
  if currentEffect == "":
    global isOn

    isOn = False
    print("TURNING ALL LEDS OFF")
    __FadeColour(0, 0, 0, 0.001)
  else:
    print("Effect running, can not turn off LEDs")


def EnableLEDs():
  if currentEffect == "":
    global isOn
    isOn = True
    print("TURNING ALL LEDS ON")
    __FadeColour(defaultColour[0], defaultColour[1], defaultColour[2])
  else:
    print("Effect running, can not turn LEDs on")


def SetEffect(effect, otherArguments):
  global currentEffect, currentEffectArguments, currentEffectHelp
  if isOn and currentEffect == "":
    effectModule = __import__(effect, otherArguments)

    if hasattr(effectModule, "Run"):
      __SetColour(0, 0, 0)

      currentEffect = effect
      currentEffectArguments = otherArguments

      if hasattr(effectModule, "help"):
        currentEffectHelp = effectModule.help
      else:
        currentEffectHelp = "No help provided for effect"

      effectModule.Run(otherArguments)

      sleep(0.75)
      currentEffect = ""
      currentEffectArguments = {}
      currentEffectHelp = {}

      __FadeColour(defaultColour[0], defaultColour[1], defaultColour[2])

      return f"Effect {effect} completed successfully!"
    else:
      return f"Effect {effect} doesn't have a Run function!"
  else:
    return "LEDs are not currently on!"


def GetLEDStatus():
  return isOn


def GetLEDColour():
  return copy(currentColour)


def GetLEDEffect():
  return [currentEffect, currentEffectArguments, currentEffectHelp]


def ResetCurrentEffect():
  global currentEffect, currentEffectArguments, currentEffectHelp
  currentEffect = ""
  currentEffectArguments = {}
  currentEffectHelp = {}
