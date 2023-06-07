from flask import request, Blueprint
from flask.json import jsonify
from dependency_injector.wiring import Provide, inject

from src.containers import Container
from src.service.training_service import TrainingService
from src.dto.core.website_training_request import WebsiteTrainingRequest

training_bp = Blueprint('training_blueprint', __name__)


@training_bp.route('/upload-files/<bucket_name>', methods=['POST'])
@inject
def upload_files(bucket_name, training_service: TrainingService = Provide[Container.training_service]):
    files = request.files.getlist('files')

    if not bucket_name or bucket_name.isspace():
        raise Exception("bucket name can not be empty")

    output = training_service.train_files_data(files, bucket_name)

    return jsonify({'result': output})


@training_bp.route('/scrape-website', methods=['POST'])
@inject
def scrape_website(training_service: TrainingService = Provide[Container.training_service]):
    website_training_request = WebsiteTrainingRequest.from_dict(request.get_json())

    output = training_service.train_website_data(website_training_request)

    return jsonify({'result': output})
