#!/usr/bin/python3
""" This script that starts a Flask web application
listening on 0.0.0.0, port 5000 """
from flask import Flask
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """ method to remove the current SQLAlchemy session """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ display a html page already done in
    web static project"""
    list_states = storage.all(State)
    list_amenities = storage.all(Amenity)
    return render_template(
        "10-hbnb_filters.html",
        list_states=list_states,
        list_amenities=list_amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
