from WebServer import app
from flask import jsonify
from GetEffects import GetEffects

@app.get("/effects/")
def getEffects():
  _effects = GetEffects()

  return jsonify(
    effects = _effects
  )
