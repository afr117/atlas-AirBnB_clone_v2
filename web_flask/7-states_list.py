#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Renders HTML with sorted states
    """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """closes storage"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
