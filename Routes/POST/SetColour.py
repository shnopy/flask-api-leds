from WebServer import app
from flask import jsonify,request
from LedControl import SetLEDColour

@app.post('/setColour/')
def setColour():
  colour = request.args.get("colour").split(",")
  setResponse = SetLEDColour(colour,request.args.get("fade") or False)

  return jsonify(
    response=setResponse
  )
