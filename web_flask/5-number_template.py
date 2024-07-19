#!/usr/bin/python3

"""
Hello World! script that has routing for the following:
    '/',
    '/hbnb'
    '/c/<usertext>'
    '/python/<usertext>'
"""

from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Hello, HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    C {}
    """
    return "C {}".format(escape(text.replace("_", " ")))


@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
    'Python {}' (has default)
    """
    return "Python {}".format(escape(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n=0):
    """
    '{n} is a number'
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    'Number: {}'
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
