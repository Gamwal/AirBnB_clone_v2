#!/usr/bin/python3
"""Flask Application"""

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function that return Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def dhbnb():
    """Function that displays HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """Function that displays C followed by text"""
    return f"C {escape(text)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
