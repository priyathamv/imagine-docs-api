from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined

from src.model.content.content_model import ContentModel


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class SimilarContent:
    link: str
    content: str
    token_count: int
    similarity: float
