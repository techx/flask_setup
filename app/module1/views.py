from flask import Blueprint, request, jsonify, render_template
from app import db
from app.models import Item
import random

module1_bp = Blueprint("mod1", __name__, url_prefix='/mod1')


@module1_bp.route("/")
def index():
    msg = request.args.get("msg", "rippo")
    return render_template("index.html", message=msg)

@module1_bp.route("/hello_world")
def hello_world():
    return "Hello World"


## More cool database stuff:

alphabet = [chr(x) for x in range(ord('a'), ord('z'))]
@module1_bp.route("/populate_data")
def populate_data():
	for _ in range(50):
		new_item = Item(name = ''.join(random.choices(alphabet, k=5)), active=random.choice((True, False)))
		db.session.add(new_item)

	db.session.commit()
	return "done!"

@module1_bp.route("/view")
def view():
	filt = request.args.get('active', None)
	page = int(request.args.get('page', 1))
	if filt is None:
		data = Item.query.all()
	else:
		data = Item.query.filter(Item.active==bool(filt))

	return '<br>'.join(str((item.name, item.active)) for item in data.order_by(Item.name).paginate(page, 5).items)


@module1_bp.route("/delete_all")
def delete_all():
	num = Item.query.delete()
	db.session.commit()
	return str(num)


# this part is for part 2
# @module1_bp.route("/requests", methods=['GET', 'POST'])
# def requests():
#     if request.method == 'GET':
#         args = request.args
#         return f"This is a GET request!\nArgs:\n{args}"
#     if request.method == "POST":
#         body = request.get_json() if request.is_json() else "[NOT JSON!]"
#         return f"This is a POST request!\nPOST body:\n{body}"

# @module1_bp.route("/send_json")
# def send_json():
#     return jsonify(request.args)


# @module1_bp.route("/status_codes/<int:status>")
# def status_codes(status):
#     return "check console for status code", int(status)
