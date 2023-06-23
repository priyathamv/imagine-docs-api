from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json, Undefined

from src.dto.document.metadata import Metadata


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class DocumentModel:
    data_source_id: str
    content: str
    token_count: int
    metadata: Metadata
    embedding: List[float]
