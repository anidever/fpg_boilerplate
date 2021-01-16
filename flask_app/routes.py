from flask import jsonify, request
from http import HTTPStatus
from flask_app import app, db
from flask_app.models import MockModel, User
from flask_app.validators import MockSchema, UserSchema


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(hello="world")


@app.route("/register", methods=['POST'])
def register():
    body = request.get_json()
    data = UserSchema().load(body)
    user = User(username=data["username"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify('GREAT SUCCESS'), HTTPStatus.CREATED
