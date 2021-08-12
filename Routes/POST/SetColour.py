from WebServer import app
from flask import jsonify,request
from LedControl import SetLEDColour

from GetArguments import GetArgumentAsNumber

@app.post('/setColour/')
def setColour():
  colour = request.args.get("colour").split(",")
  fadeTime = GetArgumentAsNumber(request.args,"fadeTime",0.01)
  setResponse = SetLEDColour(colour,request.args.get("fade") or False,fadeTime)

  return jsonify(
    response=setResponse
  )
