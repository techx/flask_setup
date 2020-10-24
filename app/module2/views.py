from flask import Blueprint, request, jsonify

module2_bp = Blueprint("mod2", __name__, url_prefix='/mod2')

@module2_bp.route("/", methods=['GET'])
def hello_world():
    return "Hello World from module 2!"
