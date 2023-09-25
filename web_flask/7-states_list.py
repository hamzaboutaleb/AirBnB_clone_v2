#!/usr/bin/python3
"""Web application"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home_route():
    """home page controller"""
    return "Hello HBNB!"

@app.route("/states_list", strict_slashes=False)
def states_list_page():
  states = storage.all(State).values()
  states = sorted(states, key=lambda state: state.name)
  return render_template("7-states_list.html", states = states)

@app.teardown_appcontext
def teardown(e):
  storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)