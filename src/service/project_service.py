from typing import List

from src.model.project.project import Project
from src.service.base_service import BaseService
from src.repository.project_repository import ProjectRepository
from src.dto.project.create_project_dto import CreateProjectRequest
from src.dto.project.update_project_dto import UpdateProjectRequest
from src.exception import RecordNotFoundException, EntitySaveException, EntityUpdateException


class ProjectService(BaseService):

    def __init__(self, project_repository: ProjectRepository) -> None:
        super().__init__()
        self.project_repository = project_repository

    def find_by_id(self, id: str) -> Project:
        find_by_id_response = self.project_repository.fetch_by_id(id)

        if find_by_id_response.data:
            project_response = find_by_id_response.data[0]
            return Project.from_dict(project_response)

        raise RecordNotFoundException('Project not found with id: ' + id)

    def find_all(self) -> List[Project]:
        find_all_response = self.project_repository.fetch_all()
        return Project.schema().load(find_all_response.data, many=True)

    def save(self, create_project_request: CreateProjectRequest) -> Project:
        create_project_json = CreateProjectRequest.to_json(create_project_request)
        save_response = self.project_repository.insert(create_project_json)

        if save_response.data:
            return Project.from_dict(save_response.data[0])

        raise EntitySaveException('Project saving failed' + str(save_response))

    def update(self, update_project_request: UpdateProjectRequest) -> Project:
        update_project_json = UpdateProjectRequest.to_json(update_project_request)
        update_response = self.project_repository.update_by_id(update_project_request.id, update_project_json)

        if update_response.data:
            return Project.from_dict(update_response.data[0])

        raise EntityUpdateException('Project updating failed' + str(update_response))

    def delete(self, id: str) -> Project:
        delete_response = self.project_repository.delete_by_id(id)

        if delete_response.data:
            return Project.from_dict(delete_response.data[0])

        raise RecordNotFoundException('Project not found to be deleted: ' + id)
