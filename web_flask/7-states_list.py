#!/usr/bin/python3
"""
starts a Flask web application. Listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list/', strict_slashes=False)
def states_list():
    """fetching State data from the storage engine"""
    state_dict = storage.all('State').values()
    return render_template('7-states_list.html', state_dict=state_dict)


@app.teardown_appcontext
def teardown_app(err):
    """remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
