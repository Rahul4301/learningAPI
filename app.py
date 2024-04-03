from flask import Flask, request, jsonify
import json

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


from bson.json_util import dumps
from bson import json_util

uri = "mongodb+srv://UCRBNH_user1:MOPnuymgggUHUKby@cluster0.lvfogdm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# client = MongoClient(uri, server_api=ServerApi('1'))
# db = client["UCRBNH"]
# collection = db["wantedcars"]


# Initialize the Flask app
app = Flask(__name__)

data = ()

@app.route('/', methods=['GET'])
def home():
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['UCRBNH']  # Replace 'mydatabase' with your actual database name
    collection = db['wantedcars']  # Replace 'mycollection' with your actual collection name
    cursor = collection.find({})


    # for document in cursor:
   # data.append(json.dumps(document))
    data = [doc for doc in cursor]
    json_data = json.dumps(data, sort_keys=True, indent=4, default=json_util.default)

    #return jsonify(json_data)
    return json_data


@app.route('/lisenceplate/<lisenceplate>', methods=['GET'])
def findbylisenceplate(lisenceplate):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['UCRBNH']  # Replace 'mydatabase' with your actual database name
    collection = db['wantedcars']
    cars = list(collection.find({"lisenceplate": lisenceplate}))

    data = [car for car in cars]
    json_data = json.dumps(data, sort_keys=True, indent=4, default=json_util.default)

    #return jsonify(json_data)
    return json_data

    '''
    for car in cars:
        car['_id'] = str(car['_id'])

    if cars:
        return jsonify(cars), 200
    else:
        return jsonify({"message": "Not Found"}), 404
    '''


@app.route('/vehicletype/<vehicletype>', methods=['GET'])
def findvevicletype(vehicletype):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['UCRBNH']  # Replace 'mydatabase' with your actual database name
    collection = db['wantedcars']
    cars = list(collection.find({"vehicletype": vehicletype}))

    for car in cars:
        car['_id'] = str(car['_id'])

    if cars:
        return jsonify(cars), 200
    else:
        return jsonify({"message": "Not Found"}), 404


@app.route('/color/<color>', methods=['GET'])
def findcolor(color):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['UCRBNH']  # Replace 'mydatabase' with your actual database name
    collection = db['wantedcars']
    cars = list(collection.find({"color": color}))

    for car in cars:
        car['_id'] = str(car['_id'])

    if cars:
        return jsonify(cars), 200
    else:
        return jsonify({"message": "Not Found"}), 404
    
    
@app.route('/lastlocation/<lastlocation>', methods=['GET'])
def findlastlocation(lastlocation):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['UCRBNH']  # Replace 'mydatabase' with your actual database name
    collection = db['wantedcars']
    cars = list(collection.find({"lastlocation": lastlocation}))
    
    for car in cars:
        car['_id'] = str(car['_id'])

    if cars:
        return jsonify(cars), 200
    else:
        return jsonify({"message": "Not Found"}), 404
    

if __name__ == '__main__':
    app.run(debug=True)

