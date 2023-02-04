
from flask import request, render_template , jsonify
from pymongo import MongoClient
from . import productos


#mongoclient 

client= MongoClient(port=27017)


#db name

db = client.pagosdata
 
@productos.route('/cafe', methods=['GET'])

def data():
         return render_template('s01a01.html')



@productos.route('/confirm.pago', methods=['POST'])

def pagos(): 
        pagos = {}
        if request.method == "POST": 
            pagos = request.get_json()['pagos']
            
            db.pagosdata.insert_one(pagos) 
            return render_template('confirmpago.html')

    