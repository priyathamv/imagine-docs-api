import logging
from flask import request, Blueprint
from flask.json import jsonify
from dependency_injector.wiring import Provide, inject

from src.containers import Container
from src.dto.data_source.data_source_dto import DataSourceDTO
from src.model.data_source.data_source_model import DataSourceModel
from src.service.data_source import DataSourceService

log = logging.getLogger(__name__)

data_source_bp = Blueprint('data_source_blueprint', __name__)


@data_source_bp.route('/file/<project_id>', methods=['POST'])
@inject
def save_file_data_source(project_id: str, data_source_service: DataSourceService = Provide[Container.data_source_service]):
    file = request.files['file']
    create_file_data_source_request = DataSourceModel.from_file_request(project_id)

    saved_data_source = data_source_service.save_data_source(create_file_data_source_request, file)

    return jsonify(saved_data_source)


@data_source_bp.route('/website', methods=['POST'])
@inject
def save_website_data_source(data_source_service: DataSourceService = Provide[Container.data_source_service]):
    create_data_source_request = DataSourceModel.from_website_request(request.get_json())

    saved_data_source = data_source_service.save_data_source(create_data_source_request)

    return jsonify(saved_data_source)


@data_source_bp.route('/text', methods=['POST'])
@inject
def save_text_data_source(data_source_service: DataSourceService = Provide[Container.data_source_service]):
    create_data_source_request = DataSourceModel.from_text_request(request.get_json())

    saved_data_source = data_source_service.save_data_source(create_data_source_request)

    return jsonify(saved_data_source)


@data_source_bp.route('/', methods=['PUT'])
@inject
def update_data_source(data_source_service: DataSourceService = Provide[Container.data_source_service]):
    update_data_source_request = DataSourceDTO.from_website_request(request.get_json())

    updated_data_source = data_source_service.update_data_source(update_data_source_request)

    return jsonify(updated_data_source)


@data_source_bp.route('/<id>', methods=['DELETE'])
@inject
def delete_data_source(id: str, data_source_service: DataSourceService = Provide[Container.data_source_service]):
    delete_status = data_source_service.delete_data_source(id)

    return jsonify({'status': delete_status})
