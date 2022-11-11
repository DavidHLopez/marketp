
from flask import Blueprint

landingp = Blueprint ('landingp',__name__, template_folder= 'templates' )

from . import landingp_routes