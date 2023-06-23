from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class SimilarContent:
    source_link: str
    content: str
    token_count: int
    similarity: float
