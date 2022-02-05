import threading

from WebServer import app
from flask import jsonify, request
from LedControl import SetEffect
from GetEffects import GetEffects


@app.post("/setEffect/")
def setEffect():
  if not request.args.get("effect"):
    return jsonify(response="Please provide a valid effect")
  else:
    requestedEffect = request.args.get("effect")
    otherArguments = request.args.to_dict()

    del otherArguments[list(otherArguments)[0]]

    effects = GetEffects()

    if requestedEffect in effects:
      threading.Thread(
          target=SetEffect, args=(requestedEffect, otherArguments)
      ).start()

      return jsonify(
          response="Attempting to set effect",
          arguments={
              "requestedEffect": requestedEffect,
              "otherArguments": otherArguments,
          },
      )
    else:
      return jsonify(response="Please provide a valid effect")
