#!/usr/bin/python3
"""
This module starts a Flask web application that listens on 0.0.0.0, port 5000.
Routes:
/: display "Hello HBNB!"
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display a simple message."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
