#!/usr/bin/python3
""" This module contains a Flask instance
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def first_task():
    """ This function returns a string
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def second_task():
    """ This function returns a string
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def third_task(text):
    """ This function returns a string.
    It also takes a variable
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def fourth_task(text):
    """ This function returns a string.
    It also takes a variable
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def fifth_task(n):
    """ This function returns a string.
    It also takes a variable
    """
    return '%i is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def sixth_task(n):
    """ This function returns a rendered web
    if n is an int.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """ This function returns a rendered web
    if n is an int.
    Tells if n is odd or even
    """
    if n % 2 == 0:
        type = "even"
    else:
        type = "odd"
    return render_template('6-number_odd_or_even.html', n=n, type=type)


if __name__ == '__main__':
    app.run(host='0.0.0.0')