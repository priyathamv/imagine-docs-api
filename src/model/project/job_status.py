import enum
from dataclasses_json import dataclass_json


@dataclass_json
class JobStatus(enum.Enum):
    NOT_INITIATED = 'NOT_INITIATED'
    IN_PROGRESS = 'IN_PROGRESS'
    SUCCESSFUL = 'SUCCESSFUL'
    FAILED = 'FAILED'
