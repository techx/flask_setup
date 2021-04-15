from flask import Blueprint, request, jsonify, render_template

module1_bp = Blueprint("mod1", __name__, url_prefix='/mod1')


@module1_bp.route("/")
def index():
    msg = request.args.get("msg", "rippo")
    return render_template("index.html", message=msg)

@module1_bp.route("/hello_world")
def hello_world():
    return "Hello World"
