from flask import Blueprint
from flask.json import jsonify

health_bp = Blueprint('health_blueprint', __name__)


@health_bp.route('/')
def health():
    return jsonify({'status': 'Application running...'})
