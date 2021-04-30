#!/usr/bin/python3
""" This script starts a web application. It takes requests
    and generates a web page
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_1(id=None):
    """Returns a rendered html template:
    if id is given, list the cities of that State
    else, list all States
    """
    states = storage.all('State')
    if id:
        key = '{}.{}'.format('State', id)
        if key in states:
            states = states[key]
        else:
            states = None
    else:
        states = storage.all('State').values()
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def close_session(self):
    """ This function closes a session
    with the storage.close() method
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
