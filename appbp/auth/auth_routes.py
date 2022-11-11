

import flask

from appbp import auth


@auth.route('/login', methods=['GET']) 
def forms_hello():
    return flask.jsonify({"message": " pagina validacion usuario"})
    