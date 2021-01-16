from marshmallow import fields, validate, ValidationError
from flask_app import marshmallow
from flask_app import models


class MockSchema(marshmallow.SQLAlchemySchema):
    pass


class UserSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = models.User

    username = fields.Str(required=True)
    email = fields.Str(required=True, validate=validate.Email(error="Not a valid email address"))
