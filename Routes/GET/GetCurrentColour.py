from WebServer import app
from flask import jsonify
from LedControl import GetLEDColour

@app.get("/getCurrentColour/")
def GetCurrentColour():
  currentColour = GetLEDColour()

  return jsonify(
    currentColour,
  )