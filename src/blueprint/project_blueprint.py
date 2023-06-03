import logging
from flask import request, Blueprint
from flask.json import jsonify
from dependency_injector.wiring import Provide, inject

from src.containers import Container
from src.exception import InvalidRequestException
from src.service.project_service import ProjectService
from src.dto.project.create_project_dto import CreateProjectDTO
from src.dto.project.update_project_dto import UpdateProjectDTO

log = logging.getLogger(__name__)

project_bp = Blueprint('project_blueprint', __name__)


@project_bp.route('/', methods=['GET'])
@inject
def find_all_projects(project_service: ProjectService = Provide[Container.project_service]):
    projects = project_service.find_all()

    return jsonify(projects)


@project_bp.route('/<id>', methods=['GET'])
@inject
def find_project_by_id(id, project_service: ProjectService = Provide[Container.project_service]):
    project = project_service.find_by_id(id)

    return jsonify(project)


@project_bp.route('/', methods=['POST'])
@inject
def save_project(project_service: ProjectService = Provide[Container.project_service]):
    create_project_request = CreateProjectDTO.from_dict(request.get_json())

    saved_project = project_service.save(create_project_request)

    return jsonify(saved_project)


@project_bp.route('/', methods=['PUT'])
@inject
def update_project(project_service: ProjectService = Provide[Container.project_service]):
    update_project_request = UpdateProjectDTO.from_dict(request.get_json())

    updated_project = project_service.update(update_project_request)

    return jsonify(updated_project)


@project_bp.route('/<id>', methods=['DELETE'])
@inject
def delete_project(id: str, project_service: ProjectService = Provide[Container.project_service]):
    deleted_project = project_service.delete(id)

    return jsonify(deleted_project)
