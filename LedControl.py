# Imports
from re import match
from time import sleep
from rpi_ws281x import Color, PixelStrip, ws

#
# https://github.com/rpi-ws281x/rpi-ws281x-python/blob/f35d40a56c3a3ae854a6a601fecc9fa8bc92f5dc/examples/SK6812_strandtest.py#L47
#

# Variables
defaultColour = [0,75,255]

isOn = False
currentColour = {
  "red": defaultColour[0],
  "green": defaultColour[1],
  "blue": defaultColour[2]
}
currentEffect = ""
currentEffectArguments = {}
currentEffectHelp = {}
strip = None



# LED Variables
LED_COUNT = 30  # Number of LED pixels.
LED_PIN = 12  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# Private
def __FindLargest(numbers):
  largest = 0
  for i in range(len(numbers)):
    if largest == 0 or numbers[i] > largest:
      largest = numbers[i]

  return largest


def __ValidateRGB(toCheck):
  if isOn:
    RGBArray = {}

    if len(toCheck) < 3:
      return "RGB array does not include all three values!"
    else:
      for index,value in enumerate(toCheck):
        if match(r"-?\d",str(value)) is not None:
          valueAsInt = int(value)

          if valueAsInt > 255:
            RGBArray[index] = 255
          elif valueAsInt < 0:
            RGBArray[index] = 0
          else:
            RGBArray[index] = valueAsInt
        else:
          return f"Given value {value} is not a valid number!"

      rgb = {
        "red": RGBArray[0],
        "green": RGBArray[1],
        "blue": RGBArray[2]
      }

      return rgb
  else:
    return "LEDs are not currently on!"



def __FadeColour(r,g,b,fadeTime=0.01):

  print(f"FADING TO: {r,g,b}")

  largest = 0
  largestNumber = __FindLargest([r,g,b])
  largestCurrent = __FindLargest(list(currentColour.values()))

  if largestCurrent > largestNumber:
    largest = largestCurrent
  else:
    largest = largestNumber

  print(largest,fadeTime)

  initial = GetLEDColour() 
  internalR = initial["red"]
  internalG = initial["green"]
  internalB = initial["blue"]

  for i in range(largest):
    if r > initial["red"] and internalR < r:
      internalR+=1
    if r < initial["red"] and internalR > r:
      internalR-=1

    if g > initial["green"] and internalG < g:
      internalG+=1
    if g < initial["green"] and internalG > g:
      internalG-=1

    if b > initial["blue"] and internalB < b:
      internalB+=1
    if b < initial["blue"] and internalB > b:
      internalB-=1


    for x in range(strip.numPixels()): 
      strip.setPixelColor(x,Color(internalR,internalG,internalB))

    sleep(fadeTime)
    strip.show()
  
  ##
  currentColour["red"] = r
  currentColour["green"] = g
  currentColour["blue"]= b

def __SetColour(r,g,b):
  
  print(f"SETTING COLOUR TO: {r,g,b}")

  currentColour["red"] = r
  currentColour["green"] = g
  currentColour["blue"]= b

  for i in range(strip.numPixels()):
    strip.setPixelColor(i,Color(r,g,b))
        
  strip.show()


# Public

def SetLEDColour(colour,fade=False,fadeTime=0.01):
  RGB = __ValidateRGB(toCheck=colour)
  fade = str(fade).lower()  
  
  if len(RGB) == 3:
    if fade == "true":
      __FadeColour(RGB["red"],RGB["green"],RGB["blue"],fadeTime)
    else:
      __SetColour(RGB["red"],RGB["green"],RGB["blue"])

    return RGB
  else:
    return "LEDs are not currently on or an invalid RGB value was provided!"


def DisableLEDs():
  global isOn
  print("TURNING ALL LEDS OFF")
  __FadeColour(0,0,0,0.001)
  isOn = False


def EnableLEDs():
  global isOn
  print("TURNING ALL LEDS ON ⚡")
  __FadeColour(defaultColour[0],defaultColour[1],defaultColour[2])
  isOn = True


def SetEffect(effect,otherArguments):
  global currentEffect,currentEffectArguments,currentEffectHelp

  if isOn:
    effectModule = __import__(effect,otherArguments)

    if hasattr(effectModule, "Run"):
      __SetColour(0,0,0)

      currentEffect = effect
      currentEffectArguments = otherArguments

      if hasattr(effectModule,"help"):
        currentEffectHelp = effectModule.help
      else:
        currentEffectHelp = "No help provided for effect"

      effectModule.Run(otherArguments)

      sleep(0.75)
      currentEffect = ""
      currentEffectArguments = {}
      currentEffectHelp = {}
      
      __FadeColour(defaultColour[0],defaultColour[1],defaultColour[2])

      return f"Effect {effect} completed successfully!"
    else:
      return f"Effect {effect} doesn't have a Run function!"
  else:
    return "LEDs are not currently on!"


def GetLEDStatus():
  return isOn


def GetLEDColour():
  return currentColour


def GetLEDEffect():
  return [currentEffect,currentEffectArguments,currentEffectHelp]