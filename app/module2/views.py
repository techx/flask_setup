from flask import Blueprint, request, jsonify
from app import db
from app.models import Item

module2_bp = Blueprint("mod2", __name__, url_prefix='/mod2')

@module2_bp.route("/", methods=['GET'])
def hello_world():
    return "Hello World from module 2!"

@module2_bp.route("/get_all_users", methods=["GET"])
def get_all_users():
    items = db.session.query(Item).all()
    return jsonify([x.serialize() for x in items]), 200

@module2_bp.route("/get_active_users", methods=["GET"])
def get_active_users():
    items = Item.query.filter_by(active=True).all()
    return jsonify([x.serialize() for x in items]), 200

