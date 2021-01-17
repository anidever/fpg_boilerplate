from flask import jsonify, request
from http import HTTPStatus
from flask_app import app, db
from flask_app.models import MockModel, User
from flask_app.validators import MockSchema, UserSchema


@app.route('/', methods=['GET'])
def hello_world():
    body = request.get_json()
    data = MockSchema().load(body)
    return jsonify(hello="world"), HTTPStatus.OK
