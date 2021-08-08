# Imports
from types import MethodType
from flask import Flask,jsonify,request,url_for
from flask_cors import CORS
from os import walk,getcwd
from sys import path

import LedControl 
import atexit

path.append("./Effects")
path.append("./Functions")

LedControl.DisableLEDs()

# Variables
app = Flask(__name__,static_folder=None)
cors = CORS(app, resources={"*": {"Access-Control-Allow-Origin": "0.0.0.0"}})

# Imports paths from paths folder

for dirPath,dirs,files in walk(f"./Routes/"):
  path.append(dirPath)

  for name in files:
    if name.endswith(".py"):
      __import__(name.split(".")[0])

