#!/usr/bin/python3
""" This script that starts a Flask web application
listening on 0.0.0.0, port 5000 """
from flask import Flask
from models import storage
from models.state import State
from flask import render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """ method to remove the current SQLAlchemy session """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_cities():
    """ display html page with states and cities """
    list_state = storage.all(State)
    return render_template('8-cities_by_states.html', list_state=list_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
