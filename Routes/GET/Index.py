from WebServer import app
from flask import url_for, jsonify


@app.get("/")
def index():
  routes = {
      "POST": [],
      "GET": [],
  }

  for rule in app.url_map.iter_rules():
    for method in rule.methods:
      if method in routes:
        routes[method].append(url_for(rule.endpoint))

  return jsonify(
      routes
  )
