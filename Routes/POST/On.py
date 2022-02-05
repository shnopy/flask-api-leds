import threading

from WebServer import app
from flask import jsonify
from LedControl import EnableLEDs

@app.post("/on/")
def TurnOnLEDs():
  threading.Thread(target=EnableLEDs,args=()).start()

  return jsonify(
    response="LEDs on"
  )