from flask import request, Blueprint
from flask.json import jsonify
from dependency_injector.wiring import Provide, inject

from src.containers import Container
from src.model.data_source.data_source_model import DataSourceModel
from src.service.training_service import TrainingService

training_bp = Blueprint('training_blueprint', __name__)


@training_bp.route('/upload-files', methods=['POST'])
@inject
def upload_files(training_service: TrainingService = Provide[Container.training_service]):
    files = request.files.getlist('files')

    output = training_service.train_files_data(files)

    return jsonify({'result': output})


@training_bp.route('/scrape-website', methods=['POST'])
@inject
def scrape_website(training_service: TrainingService = Provide[Container.training_service]):
    data_source_request = DataSourceModel.from_dict(request.get_json())

    status = training_service.train_website_data(data_source_request)

    return jsonify({'status': status})
