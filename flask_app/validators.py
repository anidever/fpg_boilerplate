from marshmallow import fields, validate, ValidationError
from flask_app import models, marshmallow


class MockSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = models.MockModel


class UserSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = models.User

    username = fields.Str(required=True)
    email = fields.Str(required=True, validate=validate.Email(error="Not a valid email address"))
