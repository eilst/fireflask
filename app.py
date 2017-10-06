#!flask/bin/python
import os
import json
import pyrebase
from flask import Flask, make_response, request, abort

app = Flask(__name__)

config = {
    "apiKey": os.environ['API_KEY'],
    "authDomain": os.environ['AUTHDOMAIN'],
    "databaseURL": os.environ['DBUTL'],
    "storageBucket": os.environ['SBUCKET']
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


def putCat(name):
    db.child(name).set("")


def putArea(cat,name):
    """if exists, area will be overwritten"""
    db.child(cat).update(name).set("")


def putItem(cat,area,item):
    db.child(cat).child(area).set({item : item})


def delete(catalogo,area,item):
    if catalogo != "" and area == "" and item == "":
        return db.child(catalogo).remove()
    elif catalogo != "" and area != "" and item == "":
        return db.child(catalogo).child(area).remove()
    elif catalogo != "" and area != "" and item != "":
        return db.child(catalogo).child(area).child(item).remove()


def get(catalogo = "", area = "", item = ""):
    if catalogo == "" and area == "" and item == "":
        data = db.get()
        return json.dumps(data.val())
    elif catalogo != "" and area == "" and item == "":
        data = db.child(catalogo).get()
        return json.dumps(data.val())
    elif catalogo != "" and area != "" and item == "":
        data = db.child(catalogo).child(area).get()
        return json.dumps(data.val())
    elif catalogo != "" and area != "" and item != "":
        data = db.child(catalogo).child(area).child(item).get()
        return json.dumps(data.val())


def put(catalogo , area = "", item = ""):
    if catalogo != "" and area == "" and item == "":
        return db.child(catalogo).set("")
    elif catalogo != "" and area != "" and item == "":
        return db.child(catalogo).child(area).set("")
    elif catalogo != "" and area != "" and item != "":
        return db.child(catalogo).child(area).update({item : item})

def puton(catalogo = "", area = "", item = "", new =""):
    
    if catalogo != "" and area == "" and item == "":
        curr = get(catalogo)
        obj = json.loads(curr)
        if obj is None:
            return False
        delete(catalogo)
        for key in obj.keys():
            for value in obj.values():
                for k in value:
                    put(new,key,k)

    if catalogo != "" and area != "" and item == "":
        curr = get(catalogo,area)
        obj = json.loads(curr)
        if obj is None:
            return False
        delete(catalogo,area)
        for key in obj.keys():
            for value in obj.values():
                    put(catalogo, new, value)

    if catalogo != "" and area != "" and item != "":
        curr = get(catalogo,area,item)
        obj = json.loads(curr)
        if obj is None:
            return False
        delete(catalogo,area,item)
        put(catalogo,area,new)

"""GET"""

@app.route('/api/v1.0/catalogos', methods=['GET'])
def get_catalogos():
    response = get()
    if response != "null":
        return response
    else:
        return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1.0/catalogos/<string:catalogo>', methods=['GET'])
def get_catalogo(catalogo):
    response = get(catalogo)
    if response != "null":
        return response
    else:
        return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1.0/catalogos/<string:catalogo>/<string:area>', methods=['GET'])
def get_area(catalogo,area):
    response = get(catalogo,area)
    if response != "null":
        return response
    else:
        return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1.0/catalogos/<string:catalogo>/<string:area>/<string:item>', methods=['GET'])
def get_item(catalogo,area,item):
    response = get(catalogo, area,item)
    if response != "null":
        return response
    else:
        return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(404)
def not_found(error):
    return make_response(json.dumps({'error': 'Not found'}), 404)

"""POST"""

@app.route('/api/v1.0/catalogos', methods=['POST'])
def create_catalogo():
    if not request.json or not 'catalogo' in request.json:
        abort(400)
    putCat(request.json['catalogo'])
    return jsonify({'catalogo': request.json['catalogo']}), 201


@app.route('/api/v1.0/catalogos/<string:catalogo>', methods=['POST'])
def create_area(catalogo):
    if not request.json or not 'area' in request.json:
        abort(400)
    putArea(catalogo,request.json['area'])
    return jsonify({'area': request.json['area']}), 201


@app.route('/api/v1.0/catalogos/<string:catalogo>/<string:area>', methods=['POST'])
def create_item(catalogo,area):
    if not request.json or not 'item' in request.json:
        abort(400)
    putItem(catalogo,area,request.json['item'])
    return jsonify({'area': request.json['item']}), 201


"""PUT"""

"""json request as { "catalogo" : "nameofcatalogo" }"""
@app.route('/api/v1.0/catalogos/<string:catalogo>', methods=['PUT'])
def update_catalogo(catalogo):
    if len(catalogo) == 0:
        abort(404)
    if not request.json:
        abort(400)
    puton(catalogo,"","",request.json.get('catalogo'))
    return  jsonify({'result': True})

@app.route('/api/v1.0/catalogos/<string:catalogo>/<string:area>', methods=['PUT'])
def update_area(catalogo,area):
    if len(area) == 0 or len(catalogo) == 0:
        abort(404)
    if not request.json:
        abort(400)
    puton(catalogo,area,"",request.json.get('area'))
    return  jsonify({'result': True})

@app.route('/api/v1.0/catalogos/<string:catalogo>/<string:area>/<string:item>', methods=['PUT'])
def update_item(catalogo,area,item):
    if len(area) == 0 or len(catalogo) == 0 or len(item) == 0 :
        abort(404)
    if not request.json:
        abort(400)
    puton(catalogo,area,item,request.json.get('item'))
    return  jsonify({'result': True})

"""DELETE"""
@app.route('/api/v1.0/catalogos/<string:catalogo>', methods=['DELETE'])
def delete_catalogo(catalogo):
    if len(catalogo) == 0:
        abort(404)
    else:
        delete(catalogo)
        return jsonify({'result': True})


@app.route('/api/v1.0/catalogos/<string:catalogo>/<string:area>', methods=['DELETE'])
def delete_area(catalogo,area):
    if len(catalogo) == 0 or len(area) == 0:
        abort(404)
    else:
        delete(catalogo,area)
        return jsonify({'result': True})


@app.route('/api/v1.0/catalogos/<string:catalogo>/<string:area>', methods=['DELETE'])
def delete_item(catalogo,area,item):
    if len(catalogo) == 0 or len(area) == 0 or len(item) == 0:
        abort(404)
    else:
        delete(catalogo,area,item)
        return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
