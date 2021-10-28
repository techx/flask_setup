from flask import Blueprint, request

counter_bp = Blueprint("counter", __name__, url_prefix='/count')

counts = {}

from math import sqrt
from itertools import count, islice
def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))

@counter_bp.route("/the/super/secret/endpoint/only/ani/knows/about/lol/this/is/so/scuffed", methods=['GET'])
def secret():
    res = "These are the current counts!<br>"
    lis = sorted([ (count if is_prime(count) else -1, name) for name,count in counts.items()], reverse=True)

    for count, person in lis:
        res += person + ": " + str(count) + "<br>"
    return res, 200

@counter_bp.route("/add/<user>", methods=["GET"])
def add_user(user):
    if user in counts:
        counts[user]+=1
    else:
        counts[user]=1    
    return "Done!", 200

# @counter_bp.route("/get/<user>", methods=["GET"])
# def get_user(user):
#     if user in counts:
#         return str(counts[user]), 200
#     else:
#         return "Not found :(", 404
