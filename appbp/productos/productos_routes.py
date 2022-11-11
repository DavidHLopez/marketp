

from flask import request, render_template


from . import productos


@productos.route('/', methods=['GET'])

def data():
         return render_template('index.html')

    