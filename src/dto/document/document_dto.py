from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined

from src.model.document.document_model import DocumentModel


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class DocumentDTO(DocumentModel):
    id: str
