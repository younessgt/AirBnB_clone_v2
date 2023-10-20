#!/usr/bin/python3
""" This script that starts a Flask web application
listening on 0.0.0.0, port 5000 """
from flask import Flask
from flask import render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ display n only if n is integer """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """ display html page only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd_even_template(n):
    """ display html page with n is even or odd
    only if n is an integer """
    if n % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    return render_template('6-number_odd_or_even.html', n=n, even_odd=even_odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
