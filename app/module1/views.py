from flask import Blueprint, request, jsonify, render_template

module1_bp = Blueprint("mod1", __name__, url_prefix='/mod1')


@module1_bp.route("/")
def index():
    msg = request.args.get("msg", "rippo")
    return render_template("index.html", message=msg)

@module1_bp.route("/hello_world")
def hello_world():
    return "Hello World"

@module1_bp.route("/requests", methods=['GET', 'POST'])
def requests():
    if request.method == 'GET':
        args = request.args
        return f"This is a GET request!\nArgs:\n{args}"
    if request.method == "POST":
        body = request.get_json() if request.is_json() else "[NOT JSON!]"
        return f"This is a POST request!\nPOST body:\n{body}"

@module1_bp.route("/send_json")
def send_json():
    return jsonify(request.args)


@module1_bp.route("/status_codes/<int:status>")
def status_codes(status):
    return "check console for status code", int(status)
