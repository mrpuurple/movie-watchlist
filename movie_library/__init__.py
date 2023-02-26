import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

from movie_library.routes import pages

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
    # generated by - python -c 'import secrets; print(secrets.token_urlsafe())'
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "980P4PhW6EnHmS71AIbHh7vpnrrysGd1Wk2aFpQ4nOI"
    )
    app.db = MongoClient(app.config["MONGODB_URI"]).get_default_database()
    app.register_blueprint(pages)

    return app