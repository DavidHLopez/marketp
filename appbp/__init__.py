#config bp-routes
from flask_login import LoginManager
from flask import Flask
import flask



from .landingp import landingp
from .loginp import loginp

from .auth import auth
from .productos import productos


app = flask.Flask(__name__)

app.config.from_pyfile('config/config.cfg')
app.register_blueprint(landingp)
app.register_blueprint(loginp)
app.register_blueprint(auth)
app.register_blueprint(productos)