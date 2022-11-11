
from flask import render_template
from . import loginp

@loginp.route( '/loginp', methods=['GET'])

def home(): 
    return  render_template('loginp.html')