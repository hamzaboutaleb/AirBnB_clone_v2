#!/usr/bin/python3
"""Web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list_page():
  # states = storage.all("State").values()
  # states = sorted(states, key=lambda state: state.name)
  states = [
    {'id': '421a55f4-7d82-47d9-b51c-a76916479545', 'name': 'stateA'},
    {'id': '421a55f4-7d82-47d9-b51c-a76916479546', 'name': 'stateB'},
    {'id': '421a55f4-7d82-47d9-b52c-a76916479547', 'name': 'stateC'},
    {'id': '421a55f4-7d82-47d9-b53c-a76916479548', 'name': 'stateD'},
    {'id': '421a55f4-7d82-47d9-b57c-a76916479549', 'name': 'stateE'}
]
  return render_template("7-states_list.html", states = states)

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)