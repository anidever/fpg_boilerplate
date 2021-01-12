from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app


def init_db(app):
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    return db, migrate


app = create_app()
db, migrate = init_db(app)
