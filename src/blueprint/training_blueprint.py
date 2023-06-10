from flask import request, Blueprint
from flask.json import jsonify
from dependency_injector.wiring import Provide, inject

from src.containers import Container
from src.exception import InvalidRequestException
from src.model.data_source.data_source_model import DataSourceModel
from src.service.gpt_stream_service import GPTStreamService
from src.service.training_service import TrainingService

training_bp = Blueprint('training_blueprint', __name__)


@training_bp.route('/upload-files/<project_id>', methods=['POST'])
@inject
def upload_files(project_id, training_service: TrainingService = Provide[Container.training_service]):
    files = request.files.getlist('files')

    if not project_id or project_id.isspace():
        raise InvalidRequestException("Invalid project_id: " + project_id)

    output = training_service.train_files_data(files, project_id)

    return jsonify({'result': output})


@training_bp.route('/scrape-website', methods=['POST'])
@inject
def scrape_website(training_service: TrainingService = Provide[Container.training_service]):
    data_source_request = DataSourceModel.from_dict(request.get_json())

    status = training_service.train_website_data(data_source_request)

    return jsonify({'status': status})


# TODO: the maximum context length is 8191 tokens
@training_bp.route('/', methods=['GET'])
@inject
def response_stream(gpt_stream_service: GPTStreamService = Provide[Container.gpt_stream_service]):
    stream = gpt_stream_service.get_response_stream()

    return jsonify({'stream': True})
