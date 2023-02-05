
from flask import request, render_template , jsonify
from flask_pymongo import pymongo

from . import productos


#mongoclient 
CONNECTION_STRING = "mongodb+srv://iwvuser:iwvuser1@pruebas.nabbcu0.mongodb.net/?retryWrites=true&w=majority"
client= pymongo.MongoClient( CONNECTION_STRING)


#db name

db = client.pagosdata
 
@productos.route('/cafe', methods=['GET'])

def data():
         return render_template('s01a01.html')



@productos.route('/confirm.pago', methods=['POST'])

def pagos(): 
    data = {}
    if request.method == "POST": 
        data['Name'] = request.form ['name']
        data['Email']= request.form ['email']
        data['Message'] = request.form ['message']
        
        db.pagosData.insert_one(data) 
        
        return render_template('confirmpago.html')

    