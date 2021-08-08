from WebServer import app
from flask import jsonify,request

@app.errorhandler(405)
def _405(error):
  return jsonify(
    shortError=f"'{request.path}'' does not support the method '{request.method}'",
    longError=str(error)
  )