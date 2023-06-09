import logging
from flask import request, Blueprint
from flask.json import jsonify
from dependency_injector.wiring import Provide, inject

from src.containers import Container
from src.dto.project.project_dto import ProjectDTO
from src.model.project.project_model import ProjectModel
from src.service.project import ProjectService

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
    project_details = project_service.get_project_by_id(id)
    # project_details = project_service.get_project_details(id)

    return jsonify(project_details)


@project_bp.route('/', methods=['POST'])
@inject
def save_project(project_service: ProjectService = Provide[Container.project_service]):
    create_project_request = ProjectModel.from_dict(request.get_json())

    saved_project = project_service.save_project(create_project_request)

    return jsonify(saved_project)


@project_bp.route('/', methods=['PUT'])
@inject
def update_project(project_service: ProjectService = Provide[Container.project_service]):
    update_project_request = ProjectDTO.from_dict(request.get_json())

    updated_project = project_service.update_project(update_project_request)

    return jsonify(updated_project)


@project_bp.route('/<id>', methods=['DELETE'])
@inject
def delete_project(id: str, project_service: ProjectService = Provide[Container.project_service]):
    deleted_project = project_service.delete_project(id)

    return jsonify(deleted_project)
