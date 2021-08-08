from WebServer import app
from flask import jsonify
from LedControl import DisableLEDs

@app.post("/off/")
def TurnOffLEDs():
  DisableLEDs()

  return jsonify(
    response="LEDs off"
  )
