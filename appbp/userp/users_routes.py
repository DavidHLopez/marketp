

import flask

users = flask.Blueprint('users', __name__)

@users.route('/users', methods=['GET']) 
def users_hello():
    return flask.jsonify({"message": "Vista de usuario listado de forms y acceso a bdhcue"})
