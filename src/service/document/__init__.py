import logging
from typing import List

from src.dto.document.document_dto import DocumentDTO
from src.exception import EntitySaveException
from src.model.document.document_model import DocumentModel
from src.repository.document_repository import DocumentRepository
from src.service.base_service import BaseService

log = logging.getLogger(__name__)


class DocumentService(BaseService):

    def __init__(self, document_repository: DocumentRepository) -> None:
        super().__init__()
        self.document_repository = document_repository

    def find_by_data_source_id(self, data_source_id) -> List[DocumentDTO]:
        document_response = self.document_repository.fetch_by_data_source_id(data_source_id)

        return DocumentDTO.schema().load(document_response.data, many=True)

    def save_all(self, document_list: List[DocumentModel]) -> bool:
        document_dict_list = list(map(DocumentModel.to_dict, document_list))

        save_all_response = self.document_repository.insert(document_dict_list)

        if save_all_response.data:
            log.info('Saved all the documents')
            return len(document_list) == len(save_all_response.data)

        raise EntitySaveException('Document list saving failed' + str(save_all_response))
