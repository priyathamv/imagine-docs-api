from dataclasses import dataclass
from dataclasses_json import dataclass_json

from src.model.tables.source_type import SourceType


@dataclass_json
@dataclass
class Document():
    source_link: str
    source_type: SourceType
