from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    return app


def init_db(app):
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    return db, migrate


app = create_app()
db, migrate = init_db(app)

# importing at the end the prevent circular import
from flask_app import routes
