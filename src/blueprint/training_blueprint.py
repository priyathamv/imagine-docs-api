from flask import request, Blueprint, Response
from flask.json import jsonify
from dependency_injector.wiring import Provide, inject

from src.containers import Container
from src.exception import InvalidRequestException
from src.service.gpt_stream_service import GPTStreamService
from src.service.training_service import TrainingService

training_bp = Blueprint('training_blueprint', __name__)


@training_bp.route('/test', methods=['GET'])
@inject
def test(training_service: TrainingService = Provide[Container.training_service]):
    output = training_service.train_file_data()

    return jsonify(output)


@training_bp.route('/upload-files/<project_id>', methods=['POST'])
@inject
def upload_files(project_id, training_service: TrainingService = Provide[Container.training_service]):
    files = request.files.getlist('files')

    if not project_id or project_id.isspace():
        raise InvalidRequestException("Invalid project_id: " + project_id)

    output = training_service.train_files_data(files, project_id)

    return jsonify({'result': output})


@training_bp.route('/train/<project_id>', methods=['POST'])
@inject
def train(project_id, training_service: TrainingService = Provide[Container.training_service]):
    status = training_service.train(project_id)

    return jsonify({'status': status})


# TODO: the maximum context length is 8191 tokens
@training_bp.route('/response', methods=['GET'])
@inject
def response_stream(gpt_stream_service: GPTStreamService = Provide[Container.gpt_stream_service]):
    project_id: str = request.args.get('project_id')
    query: str = request.args.get('query')
    response = gpt_stream_service.create_context(project_id, query)

    return jsonify({'data': response})
