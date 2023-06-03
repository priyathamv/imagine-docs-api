from flask import request, Blueprint
from flask.json import jsonify
from dependency_injector.wiring import Provide, inject

from src.containers import Container
from src.service.training_service import TrainingService
from src.dto.core.website_training_request import WebsiteTrainingRequest

gpt_bp = Blueprint('gpt_blueprint', __name__)


@gpt_bp.route('/upload-files', methods=['POST'])
@inject
def upload_files(training_service: TrainingService = Provide[Container.training_service]):
    files = request.files.getlist('files')

    output = training_service.train_files_data(files)

    return jsonify({'result': output})


@gpt_bp.route('/scrape-website', methods=['POST'])
@inject
def scrape_website(training_service: TrainingService = Provide[Container.training_service]):
    website_training_request = WebsiteTrainingRequest.from_dict(request.get_json())

    output = training_service.train_website_data(website_training_request)

    return jsonify({'result': output})
