import enum
from dataclasses_json import dataclass_json

@dataclass_json
class RuleType(enum.Enum):
    INCLUDE = 'INCLUDE'
    EXCLUDE = 'EXCLUDE'