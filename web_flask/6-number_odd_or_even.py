#!/usr/bin/python3

"""
Hello World! script that has routing for the following:
    '/',
    '/hbnb'
    '/c/<usertext>'
    '/python/<usertext>'
    '/number_template/<n>'
    '/number_odd_or_even/<n>'
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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Renders image based on 'n' parity
    """
    return render_template('6-number_odd_or_even.html',
                           n=n,
                           parity='odd' if n % 2 else 'even')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
