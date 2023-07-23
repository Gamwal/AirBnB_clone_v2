#!/usr/bin/python3
# Flask Application

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello HBNH!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
