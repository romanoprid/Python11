from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import json
import copy

from ua.lviv.iot.python.model.good import Good

with open('secret.json') as f:
    SECRET = json.load(f)
    DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
        user=SECRET["user"],
        host=SECRET["host"],
        password=SECRET["password"],
        port=SECRET["port"],
        db=SECRET["db"]
    )
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    ma = Marshmallow(app)


class IceSkates(Good, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    price_in_ukrainian_hryvnas = db.Column(db.String(64), unique=False)
    producer = db.Column(db.String(32), unique=False)
    producing_country = db.Column(db.String(64), unique=False)
    material = db.Column(db.String(64), unique=False)
    amount = db.Column(db.Float, unique=False)
    purpose = db.Column(db.String(64), unique=False)
    foot_size = db.Column(db.Float, unique=False)

    def __init__(self, name="N/A", price_in_ukrainian_hryvnas=0.0, producer="N/A", producing_country="N/A",
                 material="N/A", amount=0.0, purpose="N/A", foot_size=0.0):
        super().__init__(name, price_in_ukrainian_hryvnas, producer, producing_country, material, amount, purpose)
        self.foot_size = foot_size


class IceSkatesSchema(ma.Schema):
    class Meta:
        fields = ('name', 'price_in_ukrainian_hryvnas', 'producer',
                  'producing_country', 'material', 'amount', 'purpose', 'foot_size')


ice_skates_schema = IceSkatesSchema()
ice_skates_schemas = IceSkatesSchema(many=True)


@app.route("/ice_skates", methods=["POST"])
def add_ice_skates():
    name = request.json['name']
    price_in_ukrainian_hryvnas = request.json['price_in_ukrainian_hryvnas']
    producer = request.json['producer']
    producing_country = request.json['producing_country']
    material = request.json['material']
    amount = request.json['amount']
    purpose = request.json['purpose']
    foot_size = request.json['foot_size']
    ice_skates = IceSkates(name, price_in_ukrainian_hryvnas, producer, producing_country, material, amount, purpose,
                           foot_size)
    db.session.add(ice_skates)
    db.session.commit()
    return ice_skates_schema.jsonify(ice_skates)


@app.route("/ice_skates", methods=["GET"])
def get_ice_skates():
    all_ice_skates = IceSkates.query.all()
    result = ice_skates_schema.dump(all_ice_skates)
    return jsonify({'ice_skates': result})


@app.route("/ice_skates/<id>", methods=["GET"])
def ice_skates_detail(id):
    ice_skates = IceSkates.query.get(id)
    if not ice_skates:
        abort(404)
    return ice_skates_schema.jsonify(ice_skates)


@app.route("/ice_skates/<id>", methods=["PUT"])
def ice_skates_update(id):
    ice_skates = IceSkates.query.get(id)
    if not ice_skates:
        abort(404)
    old_ice_skates = copy.deepcopy(ice_skates)
    ice_skates.name = request.json['name']
    ice_skates.price_in_ukrainian_hryvnas = request.json['price_in_ukrainian_hryvnas']
    ice_skates.producer = request.json['producer']
    ice_skates.producing_country = request.json['producing_country']
    ice_skates.material = request.json['material']
    ice_skates.amount = request.json['amount']
    ice_skates.purpose = request.json['purpose']
    ice_skates.foot_size = request.json['foot_size']
    db.session.commit()
    return ice_skates_schema.jsonify(old_ice_skates)


@app.route("/ice_skates/<id>", methods=["DELETE"])
def ice_skates_delete(id):
    ice_skates = IceSkates.query.get(id)
    if not ice_skates:
        abort(404)
    db.session.delete(ice_skates)
    db.session.commit()
    return ice_skates_schema.jsonify(ice_skates)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
