from WebServer import app
from flask import jsonify,request

@app.errorhandler(404)
def _404(error):
  return jsonify(
    shortError=f"Route '{request.path}' does not exist!",
    longError=str(error)
  )