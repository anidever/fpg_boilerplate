from flask import jsonify
from flask_app import app
from flask_app.models import MockModel
from flask_app.validators import MockForm


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(hello="world")
