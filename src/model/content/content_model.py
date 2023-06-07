from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json, Undefined


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ContentModel:
    data_source_id: str
    content: str
    token_count: int
    embedding: List[float]
