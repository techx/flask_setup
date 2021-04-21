from flask import Blueprint, request, jsonify, render_template
import random
from app import db
from app.models import Item

module1_bp = Blueprint("mod1", __name__, url_prefix='/mod1')


@module1_bp.route("/")
def index():
    msg = request.args.get("msg", "rippo")
    return render_template("index.html", message=msg)

@module1_bp.route("/hello_world")
def hello_world():
    return "Hello World"

@module1_bp.route("/add_random", methods=['POST'])
def add_random():
	item = Item()
	name = str(random.random())
	active = True
	item.populate(name, active)
	db.session.add(item)
	db.session.commit()
	return "random user added using add_random", 200

# get so we can use them in browser
@module1_bp.route("/add_user/<name>", methods=['GET', 'POST'])
def add_user(name):
	item = Item()
	item.populate(name, True)
	db.session.add(item)
	db.session.commit()
	return "user added using add_user", 200

# with request body
@module1_bp.route("/add_user_json", methods=['POST'])
def add_user_json():
	'''
    Request body:
    {
        name: <string>,
        active: <bool>
    }
	'''
	req = request.get_json(force=True)
	name = req.get('name', 'default name')
	active = req.get('active', False)

	item = Item()
	item.populate(name, active)
	db.session.add(item)
	db.session.commit()
	return "user added using add_user_json", 200

# resets database
@module1_bp.route('/reset_data')
def reset_data():
	num = Item.query.delete()
	db.session.commit()
	return str(num), 200
