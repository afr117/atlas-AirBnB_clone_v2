#!/usr/bin/python3
"""
This module starts a Flask web application that listens on 0.0.0.0, port 5000.
Routes:
/: display "Hello HBNB!"
/hbnb: display "HBNB"
/c/<text>: display "C " followed by the value of the text variable (replace underscore _ symbols with a space)
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display a simple message."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display a simple message."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display "C " followed by the value of the text variable."""
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
