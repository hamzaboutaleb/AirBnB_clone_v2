#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home_page():
    """Home controller"""
    return "Hello HBNB!"


@app.route("/", strict_slashes=False)
def hbnb_page():
    """hbnb controlelr"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_page(text):
    """c page controller"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_page(text="is_cool"):
    """C page controller"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_page(n):
    """number page controller"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_number_page(n):
    """number age controller"""
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
