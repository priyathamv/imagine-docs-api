import enum
from dataclasses_json import dataclass_json


@dataclass_json
class SourceType(enum.Enum):
    WEBSITE = 'WEBSITE'
    FILE = 'FILE'
    PLAIN_TEXT = 'PLAIN_TEXT'
