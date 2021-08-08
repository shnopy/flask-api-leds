from WebServer import app
from flask import jsonify
from LedControl import GetLEDStatus,GetLEDColour,GetLEDEffect

@app.get("/status/")
def GetStatus():
  LEDStatus = GetLEDStatus()
  currentColour = GetLEDColour()
  currentEffect = GetLEDEffect()

  print(currentEffect)

  return jsonify(
    colour=currentColour,
    effect={
      "effectName": currentEffect[0],
      "effectArguments": currentEffect[1],
      "effectHelp": currentEffect[2]
    },
    status=("Off","On")[LEDStatus]
  )
