#!/usr/bin/pyhton3
from flask import Flask
""" Hello route """
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home_route():
    """home page controller"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
