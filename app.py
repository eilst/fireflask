#!flask/bin/python
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


def putItem(cat,area,item,new):
    db.child(cat).child(area).set({new : new})


def delItem(cat,area,item):
    """if there is only one item in area, area will also be removed"""
    db.child(cat).child(area).child(item).remove()


def delArea(cat,area):
    """delete with all its items"""
    db.child(cat).child(area).remove()


def delCat(cat):
    db.child(cat).remove()


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

"""GET"""

@app.route('/api/v1.0/catalogos', methods=['GET'])
def get_catalogos():
    response = get()
    if response != "null":
        return response
    else:
        return make_response(json.dumps({'error': 'Not found'}), 404)


@app.route('/api/v1.0/catalogos/<string:catalogo>', methods=['GET'])
def get_catalogo(catalogo):
    response = get(catalogo)
    if response != "null":
        return response
    else:
        return make_response(json.dumps({'error': 'Not found'}), 404)


@app.route('/api/v1.0/catalogos/<string:catalogo>/<string:area>', methods=['GET'])
def get_area(catalogo,area):
    response = get(catalogo,area)
    if response != "null":
        return response
    else:
        return make_response(json.dumps({'error': 'Not found'}), 404)


@app.route('/api/v1.0/catalogos/<string:catalogo>/<string:area>/<string:item>', methods=['GET'])
def get_item(catalogo,area,item):
    response = get(catalogo, area,item)
    if response != "null":
        return response
    else:
        return make_response(json.dumps({'error': 'Not found'}), 404)


@app.errorhandler(404)
def not_found(error):
    return make_response(json.dumps({'error': 'Not found'}), 404)

"""POST"""

@app.route('/api/v1.0/catalogos', methods=['POST'])
def create_catalogo():
    if not request.json or not 'catalogo' in request.json:
        abort(400)
    putCat(request.json['catalogo'])
    return json.dumps({'catalogo': request.json['catalogo']}), 201


@app.route('/api/v1.0/catalogos/<string:catalogo>', methods=['POST'])
def create_area(catalogo):
    if not request.json or not 'area' in request.json:
        abort(400)
    putArea(catalogo,request.json['area'])
    return json.dumps({'area': request.json['area']}), 201


@app.route('/api/v1.0/catalogos/<string:catalogo>/<string:area>', methods=['POST'])
def create_item(catalogo,area):
    if not request.json or not 'item' in request.json:
        abort(400)
    putItem(catalogo,area,request.json['item'])
    return json.dumps({'area': request.json['item']}), 201


"""PUT"""

"""DELETE"""


if __name__ == '__main__':
    app.run(debug=True)
