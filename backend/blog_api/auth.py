from flask import request, Blueprint
from flask import jsonify
from flask_jwt_extended import create_access_token

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # TODO later use db to store admin username and password
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password", "code": -1})

    access_token = create_access_token(identity=username)
    return jsonify({
        "code": 0,
        "msg": "ok",
        "data": {"access_token": access_token}
    })
