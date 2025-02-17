#!/usr/bin/python3
""" start flask app """

from models import storage
from models.amenity import Amenity
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(e):
    """ close session then reload"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ display hbnb_filters """
    states = storage.all(State).values()
    print(states)
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000', debug=True)