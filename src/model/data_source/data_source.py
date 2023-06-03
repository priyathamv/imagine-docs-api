from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime
from typing import List

from src.dto.core.rule import Rule
from src.model.project.project_status import JobStatus
from src.model.data_source.source_type import SourceType


@dataclass_json
@dataclass
class DataSource:
    id: int
    project_id: int
    source_type: SourceType
    source_link: str
    content: str
    status: JobStatus
    is_auth_enabled: bool
    is_recursive: bool
    rules: List[Rule]
    created_at: datetime
    updated_at: datetime
