import threading

from WebServer import app
from flask import jsonify, request
from LedControl import SetLEDColour

from GetArguments import GetArgumentAsNumber, GetArgumentAsBool


@app.post("/setColour/")
def setColour():
  colour = request.args.get("colour").split(",")

  fade = GetArgumentAsBool(request.args, "fade", "false")
  fadeTime = GetArgumentAsNumber(request.args, "fadeTime", 0.01)

  threading.Thread(target=SetLEDColour, args=(colour, fade, fadeTime)).start()

  return jsonify(
      response=f"Attempting to set LED colour",
      args={"colour": colour, "fade": fade, "fadeTime": fadeTime},
  )
