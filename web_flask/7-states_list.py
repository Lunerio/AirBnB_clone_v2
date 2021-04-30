#!/usr/bin/python3
""" This script starts a web application. It takes requests
    and generates a web page
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ This function loads the list of states
    and creates the web page
    """
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session():
    """ This function closes a session
    with the storage.close() method
    """
    storage.close()
