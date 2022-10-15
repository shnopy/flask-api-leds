from time import sleep
from WebServer import app
from flask import jsonify
from LedControl import GetLEDEffect, ResetCurrentEffect, SetLEDColour, defaultColour


@app.post("/stopEffect/")
def stopEffect():
  effect = GetLEDEffect()

  if len(effect[0]) == 0:
    return jsonify(
        response="No effect currently ongoing"
    )
  else:
    effectName = effect[0]
    importedEffect = __import__(effectName)

    if hasattr(importedEffect, "Stop"):
      importedEffect.Stop()

      sleep(1)
      SetLEDColour(defaultColour, fade="true", override="true")
      ResetCurrentEffect()

      return jsonify(
          response=f"Successfully stopped '{effectName} effect"
      )
    else:
      return jsonify(
          response=f"Error! Effect '{effectName}' does not have a stop function!"
      )
