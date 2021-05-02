#!/usr/bin/python3
"""
starts a Flask web application. Listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states/', strict_slashes=False)
def states_list():
    """fetching State data from the storage engine"""
    state_dict = storage.all('State').values()
    return render_template('7-states_list.html', state_dict=state_dict)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """fetching State data from the storage engine"""
    list_states = storage.all('State')
    state_id = 'State.{}'.format(id)
    if state_id in list_states:
        list_states = list_states[state_id]
    else:
        list_states = None
    return render_template('9-states.html', list_states=list_states)


@app.teardown_appcontext
def teardown_app(err):
    """remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
