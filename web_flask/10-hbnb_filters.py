#!/usr/bin/python3
"""
Starts a Flask web application with filters
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session after each request"""
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display HTML page with filters"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    cities = sorted(storage.all(City).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

