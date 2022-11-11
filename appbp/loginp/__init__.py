
from flask import Blueprint

loginp = Blueprint ('loginp',__name__, template_folder= 'templates' )

from . import loginp_routes