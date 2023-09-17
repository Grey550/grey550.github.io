#!/usr/bin/python3
"""Flask app to generate complete html page containing location/amenity
dropdown menus and rental listings"""
from flask import Flask, render_template
from models import storage
app = Flask('__name__')
app.url_map.strict_slashes = False


@app.route('/')
def display_hbnb():
    """Generate page with popdown menu of states/cities"""
    states = storage.all('State')
    activities = storage.all('Activity')
    return render_template('index.html',
                           states=states,
                           activities=activities)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close database or file storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)