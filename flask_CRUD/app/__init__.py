from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config
from app.routes.user_routes import user_bp
from app.extensions import mongo

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    mongo.init_app(app)

    app.register_blueprint(user_bp, url_prefix="/users")

    return app