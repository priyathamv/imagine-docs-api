import logging
from typing import List

from src.dto.content.content_dto import ContentDTO
from src.exception import EntitySaveException
from src.model.content.content_model import ContentModel
from src.repository.content_repository import ContentRepository
from src.service.base_service import BaseService

log = logging.getLogger(__name__)


class ContentService(BaseService):

    def __init__(self, content_repository: ContentRepository) -> None:
        super().__init__()
        self.content_repository = content_repository

    def find_by_data_source_id(self, data_source_id) -> List[ContentDTO]:
        content_response = self.content_repository.fetch_by_data_source_id(data_source_id)

        return ContentDTO.schema().load(content_response.data, many=True)

    def save_all(self, content_list: List[ContentModel]) -> bool:
        content_dict_list = list(map(ContentModel.to_dict, content_list))

        save_all_response = self.content_repository.insert(content_dict_list)

        if save_all_response.data:
            log.info('Saved all the contents')
            return len(content_list) == len(save_all_response.data)

        raise EntitySaveException('Content list saving failed' + str(save_all_response))
