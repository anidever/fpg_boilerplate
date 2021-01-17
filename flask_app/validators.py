from marshmallow import fields, validate, ValidationError
from flask_app import models, marshmallow


class MockSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = models.MockModel
