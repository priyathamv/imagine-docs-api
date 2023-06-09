from typing import List

from src.dto.project.project_details_dto import ProjectDetailsDTO
from src.dto.project.project_dto import ProjectDTO
from src.model.project.project_model import ProjectModel
from src.service.base_service import BaseService
from src.repository.project_repository import ProjectRepository
from src.exception import RecordNotFoundException, EntitySaveException, EntityUpdateException


class ProjectService(BaseService):

    def __init__(self, project_repository: ProjectRepository) -> None:
        super().__init__()
        self.project_repository = project_repository

    def get_project_by_id(self, id: str) -> ProjectDTO:
        find_by_id_response = self.project_repository.fetch_by_id(id)

        if find_by_id_response.data:
            project_response = find_by_id_response.data[0]
            return ProjectDTO.from_dict(project_response)

        raise RecordNotFoundException('Project not found with id: ' + id)

    def get_project_details(self, id: str):
        project_details_response = self.project_repository.fetch_project_details(id)

        if project_details_response.data:
            x = ProjectDetailsDTO.from_dict(project_details_response.data[0])
            return x

        raise RecordNotFoundException('Project not found with id: ' + id)

    def find_all(self) -> List[ProjectDTO]:
        find_all_response = self.project_repository.fetch_all()
        return ProjectDTO.schema().load(find_all_response.data, many=True)

    def save_project(self, create_project_request: ProjectModel) -> ProjectDTO:
        create_project_dict = ProjectModel.to_dict(create_project_request)
        save_response = self.project_repository.insert(create_project_dict)

        if save_response.data:
            return ProjectDTO.from_dict(save_response.data[0])

        raise EntitySaveException('Project saving failed' + str(save_response))

    def update_project(self, update_project_request: ProjectDTO) -> ProjectDTO:
        update_project_dict = ProjectDTO.to_dict(update_project_request)
        update_response = self.project_repository.update_by_id(update_project_request.id, update_project_dict)

        if update_response.data:
            return ProjectDTO.from_dict(update_response.data[0])

        raise EntityUpdateException('Project updating failed' + str(update_response))

    def delete_project(self, id: str) -> ProjectDTO:
        delete_response = self.project_repository.delete_by_id(id)

        if delete_response.data:
            return ProjectDTO.from_dict(delete_response.data[0])

        raise RecordNotFoundException('Project not found to be deleted: ' + id)
