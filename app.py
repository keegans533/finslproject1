from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from objects import *
import os
port = int(os.getenv('PORT', 8000))
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
