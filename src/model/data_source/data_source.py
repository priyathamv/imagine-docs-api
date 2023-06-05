from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

from src.dto.core.rule import Rule
from src.model.project.project_status import JobStatus
from src.model.data_source.source_type import SourceType


@dataclass_json
@dataclass
class DataSource:
    id: str
    project_id: str
    source_type: SourceType
    source_link: str
    content: str
    status: JobStatus
    is_auth_enabled: bool # Need to revisit how to handle authenticated websites
    is_recursive: bool
    rules: List[Rule]
    created_at: str
    updated_at: str
