from flask import Flask

from .health_blueprint import health_bp
from .training_blueprint import training_bp
from .project_blueprint import project_bp


def register_blueprints(app: Flask):
    app.register_blueprint(health_bp, url_prefix='/health')
    app.register_blueprint(training_bp, url_prefix='/api/v1/gpt')
    app.register_blueprint(project_bp, url_prefix='/api/v1/project')
