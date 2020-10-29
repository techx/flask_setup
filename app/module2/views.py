from flask import Blueprint, request, jsonify, render_template
import requests
module2_bp = Blueprint("mod2", __name__, url_prefix='/mod2')

@module2_bp.route("/", methods=['GET'])
def hello_world():
	return "Hello World from module 2!"


## API call:

@module2_bp.route("/mbta", methods=['GET'])
def mbta():
	line = request.args.get("line", None)
	line_data = requests.get(f"https://api-v3.mbta.com/routes/{line}")
	color = line_data.json()['data']['attributes']['color']
	stop_data = requests.get(f"https://api-v3.mbta.com/stops?filter&route={line}")
	stops = stop_data.json()['data']
	return render_template('stops.html', line=line, color=f'#{color}', stop_data=[stop['attributes']['name'] for stop in stops])


