from typing import List

from src.dto.data_source.data_source_dto import DataSourceDTO
from src.exception import EntitySaveException
from src.model.data_source.data_source_model import DataSourceModel
from src.repository.data_source_repository import DataSourceRepository
from src.service.base_service import BaseService


class DataSourceService(BaseService):

    def __init__(self, data_source_repository: DataSourceRepository) -> None:
        super().__init__()
        self.data_source_repository = data_source_repository

    def find_by_data_source_id(self, project_id) -> List[DataSourceDTO]:
        data_source_response = self.data_source_repository.fetch_by_project_id(project_id)
        return DataSourceDTO.schema().load(data_source_response.data, many=True)

    def save(self, data_source: DataSourceModel) -> DataSourceDTO:
        data_source_dict = DataSourceModel.to_dict(data_source)
        save_response = self.data_source_repository.insert(data_source_dict)

        if save_response.data:
            return DataSourceDTO.from_dict(save_response.data[0])

        raise EntitySaveException('DataSource saving failed' + str(save_response))
