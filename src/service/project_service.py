from src.service.base_service import BaseService
from src.repository.project_repository import ProjectRepository
from src.dto.project.create_project_dto import CreateProjectRequest
from src.dto.project.update_project_dto import UpdateProjectRequest
from src.exception import RecordNotFoundException, EntitySaveException, EntityUpdateException


class ProjectService(BaseService):

    def __init__(self, project_repository: ProjectRepository) -> None:
        super().__init__()
        self.project_repository = project_repository

    def find_by_id(self, id: str):
        find_by_id_response = self.project_repository.fetch_by_id(id)

        if find_by_id_response.data:
            return find_by_id_response.data[0]

        raise RecordNotFoundException('Project not found with id: ' + id)

    def find_all(self):
        find_all_response = self.project_repository.fetch_all()
        return find_all_response.data

    def save(self, create_project_request: CreateProjectRequest):
        save_response = self.project_repository.insert(create_project_request)

        if save_response.data:
            return save_response.data[0]

        raise EntitySaveException('Project saving failed' + str(save_response))

    def update(self, update_project_request: UpdateProjectRequest):
        update_response = self.project_repository.update_by_id(update_project_request.id, update_project_request)

        if update_response.data:
            return update_response.data[0]

        raise EntityUpdateException('Project updating failed' + str(update_response))

    def delete(self, id: str):
        delete_response = self.project_repository.delete_by_id(id)

        if delete_response.data:
            return delete_response.data[0]

        raise RecordNotFoundException('Project not found to be deleted: ' + id)
