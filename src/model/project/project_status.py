import enum
from dataclasses_json import dataclass_json


@dataclass_json
class JobStatus(enum.Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    FAILED = 'FAILED'
    COMPLETED = 'COMPLETED'
