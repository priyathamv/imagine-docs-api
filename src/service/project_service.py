from src.service.base_service import BaseService
from src.repository.project_repository import ProjectRepository


class ProjectService(BaseService):

    def __init__(self, project_repository: ProjectRepository) -> None:
        super().__init__()
        self.project_repository = project_repository

    def find_by_id(self, id: str):
        return self.project_repository.fetch_by_id(id)

    def find_all(self):
        return self.project_repository.fetch_all()

    def save(self, create_project_request):
        save_response = self.project_repository.insert(create_project_request)
        return save_response.data

    def update(self, update_project_request):
        update_response = self.project_repository.update_by_id(update_project_request['id'], update_project_request)
        return update_response.data

    def delete(self, id: str):
        delete_response = self.project_repository.delete_by_id(id)
        return delete_response.data
