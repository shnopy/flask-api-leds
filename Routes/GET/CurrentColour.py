from WebServer import app
from flask import jsonify
from LedControl import GetLEDColour

@app.get("/currentColour/")
def CurrentColour():
  currentColour = GetLEDColour()

  return jsonify(
    currentColour,
  )