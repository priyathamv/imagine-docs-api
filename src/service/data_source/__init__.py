from typing import List

from src.dto.data_source.data_source_dto import DataSourceDTO
from src.exception import EntitySaveException, RecordNotFoundException, EntityUpdateException
from src.model.data_source.data_source_model import DataSourceModel
from src.model.project.job_status import JobStatus
from src.repository.data_source_repository import DataSourceRepository
from src.service.base_service import BaseService
from src.service.file_service import FileService


class DataSourceService(BaseService):

    def __init__(self, data_source_repository: DataSourceRepository, file_service: FileService) -> None:
        super().__init__()
        self.data_source_repository = data_source_repository
        self.file_service = file_service

    def find_by_project_id(self, project_id: str) -> List[DataSourceDTO]:
        data_sources_response = self.data_source_repository.fetch_by_project_id(project_id)

        return DataSourceDTO.schema().load(data_sources_response.data, many=True)

    def save_data_source(self, data_source: DataSourceModel, file=None):
        if file is not None:
            data_source.source_link = self.file_service.upload_file('test', file)  # data_source.project_id, file)

        data_source_dict = DataSourceModel.to_dict(data_source)

        save_response = self.data_source_repository.insert(data_source_dict)

        if save_response.data:
            return save_response.data[0]

        raise EntitySaveException('DataSource saving failed' + str(save_response))

    def update_data_source(self, update_data_source_request: DataSourceDTO):
        update_data_source_dict = DataSourceDTO.to_dict(update_data_source_request)
        update_response = self.data_source_repository.update_by_id(update_data_source_request.id,
                                                                   update_data_source_dict)

        if update_response.data:
            return update_response.data[0]

        raise EntityUpdateException('DataSource updating failed' + str(update_response))

    def update_data_source_status(self, id: str, job_status: JobStatus) -> bool:
        update_response = self.data_source_repository.update_status(id, job_status)

        return len(update_response.data) == 1

    def delete_data_source(self, id: str) -> bool:
        delete_response = self.data_source_repository.delete_by_id(id)

        if delete_response.data:
            return len(delete_response.data[0]) == 1

        raise RecordNotFoundException('DataSource not found to be deleted: ' + id)
