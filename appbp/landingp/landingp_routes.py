
from flask import request, render_template
from pymongo import MongoClient 

from . import landingp 

#mongoclient 

client= MongoClient(port=27017)

#db name

db = client.contact_datamp




@landingp.route('/', methods=['GET'])
def home():
    return render_template('landingp_index.html')

@landingp.route('/cafe', methods=['GET'])
def reg1():
    return render_template('s01a01.html')

@landingp.route('/s01a02', methods=['GET'])
def reg2():
    return render_template('s01a02.html')

@landingp.route('/s01a03', methods=['GET'])
def reg3():
    return render_template('s01a03.html')

@landingp.route('/s01a04', methods=['GET'])
def reg4():
    return render_template('s01a04.html')

@landingp.route('/s01a05', methods=['GET'])
def reg5():
    return render_template('s01a05.html')


@landingp.route( '/contactr', methods=['POST'])

def data(): 
    data = {}
    if request.method == "POST": 
        data['Name'] = request.form ['name']
        data['Email']= request.form ['email']
        data['Message'] = request.form ['message']
        db.contactData.insert_one(data) 
        return render_template('landingp_index.html')







