#!/usr/bin/python3
"""Web application"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)

@app.teardown_appcontext
def teardown(e):
  storage.close()

@app.route("/states_list", strict_slashes=False)
def states_list_page():
  states = storage.all(State).values()
  states = sorted(states, key=lambda state: state.name)
  return render_template("8-cities_by_states.html", states = states)



if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)