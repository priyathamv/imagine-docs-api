import enum
from dataclasses_json import dataclass_json


@dataclass_json
class JobStatus(enum.Enum):
    NOT_INITIATED = "NOT_INITIATED"
    IN_PROGRESS = 'IN_PROGRESS'
    FAILED = 'FAILED'
    COMPLETED = 'COMPLETED'
    FILE_UPLOAD_FAILED = 'FILE_UPLOAD_FAILED'
    FILE_UPLOAD_SUCCESS = 'FILE_UPLOAD_SUCCESS'
