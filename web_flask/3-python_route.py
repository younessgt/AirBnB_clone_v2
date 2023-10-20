#!/usr/bin/python3
""" This script that starts a Flask web application
listening on 0.0.0.0, port 5000 """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_Hbnb():
    """ hello function """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def Hbnb():
    """ Hbnb function """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_user_text(text):
    """ adding varibale section to the url
    which is text"""
    if "_" in text:
        text = text.replace("_", " ")
    return f'C {text}'


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python(text="is cool"):
    """ setting text to "is fun" by default if no value is provided in the URL
    else displaying the user input text"""
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
