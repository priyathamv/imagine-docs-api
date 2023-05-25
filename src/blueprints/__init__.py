from flask import Flask

from .health_blueprint import health_bp
from .gpt_blueprint import gpt_bp


def register_blueprints(app: Flask):
    app.register_blueprint(health_bp, url_prefix='/health')
    app.register_blueprint(gpt_bp, url_prefix='/api/v1/gpt')
