from WebServer import app
from flask import jsonify
from LedControl import EnableLEDs

@app.post("/on/")
def TurnOnLEDs():
  EnableLEDs()

  return jsonify(
    response="LEDs on"
  )