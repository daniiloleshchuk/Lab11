from flask import Flask, request, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from flask_marshmallow import Marshmallow
import json
import copy

with open("secret.json") as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Flower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_of_product = db.Column(db.String(35), unique=False)
    color = db.Column(db.String(35), unique=False)
    height_in_sm = db.Column(db.Integer, unique=False)
    type_of_flower = db.Column(db.String(35), unique=False)
    price_in_uah = db.Column(db.Integer, unique=False)

    def __init__(self, type_of_product=None, color=None, height_in_sm=0, type_of_flower=None, price_in_uah=0):
        self.type_of_product = type_of_product
        self.color = color
        self.height_in_sm = height_in_sm
        self.type_of_flower = type_of_flower
        self.price_in_uah = price_in_uah

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


db.create_all()


class FlowerSchema(ma.Schema):
    class Meta:
        model = Flower
        sql_session = db.session

    id = fields.Integer(dump_only=True)
    type_of_product = fields.String(required=True)
    color = fields.String(required=True)
    height_in_sm = fields.Integer(required=True)
    price_in_uah = fields.Integer(required=True)
    type_of_flower = fields.String(required=True)


flower_schema = FlowerSchema()
many_flower_schemas = FlowerSchema(many=True)


@app.route("/flowers", methods=["GET"])
def get_all_flowers():
    flowers = Flower.query.all()
    if not flowers:
        abort(404)
    flowers = many_flower_schemas.dump(flowers)
    return make_response(jsonify({"flowers": flowers}), 200)


@app.route("/flowers/<id>", methods=["GET"])
def get_flower_by_id(id):
    get_flower = Flower.query.get(id)
    if not get_flower:
        abort(404)
    flower = flower_schema.dump(get_flower)
    return make_response(jsonify({"flower": flower}), 200)


@app.route("/flowers", methods=["POST"])
def add_flower():
    color = request.json['color']
    height_in_sm = request.json['height_in_sm']
    type_of_product = request.json['type_of_product']
    type_of_flower = request.json['type_of_flower']
    price_in_uah = request.json['price_in_uah']
    flower = Flower(color=color, height_in_sm=height_in_sm, type_of_product=type_of_product,
                    type_of_flower=type_of_flower, price_in_uah=price_in_uah)
    db.session.add(flower)
    db.session.commit()
    return flower_schema.jsonify(flower)


@app.route("/flowers/<id>", methods=["PUT"])
def update_flower_by_id(id):
    data = request.get_json()
    get_flower = Flower.query.get(id)

    old_flower = copy.deepcopy(get_flower)
    if data.get("type_of_product"):
        get_flower.type_of_product = data["type_of_product"]
    if data.get("color"):
        get_flower.color = data["color"]
    if data.get("height_in_sm"):
        get_flower.height_in_sm = data["height_in_sm"]
    if data.get("type_of_flower"):
        get_flower.type_of_flower = data["type_of_flower"]
    if data.get("price_in_uah"):
        get_flower.price_in_uah = data["price_in_uah"]

    db.session.add(get_flower)
    db.session.commit()
    return flower_schema.jsonify(old_flower)


@app.route("/flowers/<id>", methods=["DELETE"])
def delete_flower_by_id(id):
    get_flower = Flower.query.get(id)
    if not get_flower:
        abort(404)
    db.session.delete(get_flower)
    db.session.commit()
    return make_response("", 200)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host="127.0.0.1", port="8080")
