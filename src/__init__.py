from flask import Flask
from flask_cors import CORS

from src.blueprint import register_blueprints
from src.containers import Container
from src.exception import global_exception_handler

import nltk

nltk.set_proxy('***')
nltk.download('punkt')


# Application Factory
def create_app():
    app = Flask(__name__)

    # Enabling CORS for all routes
    CORS(app, resources={r'/*': {'origins': '*'}})

    # Fetching configuration from config.py
    # config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    # app.config.from_object(config_type)

    # Dependency injection container
    container = Container()
    app.container = container

    # Register Blueprints
    register_blueprints(app)

    # Register error handlers
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def error_handler(error):
        return global_exception_handler(error)
