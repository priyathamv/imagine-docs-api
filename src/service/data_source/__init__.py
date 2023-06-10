from src.dto.data_source.data_source_dto import DataSourceDTO
from src.exception import EntitySaveException, RecordNotFoundException, EntityUpdateException
from src.model.data_source.data_source_model import DataSourceModel
from src.model.data_source.source_type import SourceType
from src.repository.data_source_repository import DataSourceRepository
from src.service.base_service import BaseService
from src.service.file_service import FileService


class DataSourceService(BaseService):

    def __init__(self, data_source_repository: DataSourceRepository, file_service: FileService) -> None:
        super().__init__()
        self.data_source_repository = data_source_repository
        self.file_service = file_service

    def save_data_source(self, data_source: DataSourceModel, file=None):
        if file is not None:
            file_link = 'file_link_here2'  # self.file_service.upload_file(file)
            data_source.source_link = file_link

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

    def delete_data_source(self, id: str):
        delete_response = self.data_source_repository.delete_by_id(id)

        if delete_response.data:
            return delete_response.data[0]

        raise RecordNotFoundException('DataSource not found to be deleted: ' + id)
