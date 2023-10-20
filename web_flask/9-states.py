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


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id='all_state'):
    """ display html page with state depending on
    a given id"""
    list_state = storage.all(State)
    if id == "all_state":
        return render_template(
            '9-states.html',
            list_state=list_state,
            my_id="all_state")

    for obj in list_state.values():
        if obj.id == id:
            return render_template(
                '9-states.html',
                obj=obj,
                my_id=id)
    return render_template(
        '9-states.html',
        list_state=list_state,
        my_id="not_found")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
