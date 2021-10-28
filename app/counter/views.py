from flask import Blueprint, request

counter_bp = Blueprint("counter", __name__, url_prefix='/count')

counts = {}

@counter_bp.route("/", methods=['GET'])
def hello():
    res = "These are the current counts!<br>"
    for person in counts:
        res += person + ": " + str(counts[person]) + "<br>"
    return res, 200

@counter_bp.route("/add/<user>", methods=["GET"])
def add_user(user):
    if user in counts:
        counts[user]+=1
    else:
        counts[user]=1    
    return "Done!", 200

@counter_bp.route("/get/<user>", methods=["GET"])
def get_user(user):
    if user in counts:
        return str(counts[user]), 200
    else:
        return "Not found :(", 404
