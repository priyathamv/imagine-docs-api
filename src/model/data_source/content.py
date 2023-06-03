from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Content:
    data_source_id: int
    content: str
    token_count: int
    embedding: List[float]
