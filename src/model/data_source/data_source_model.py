from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, Undefined, config
from typing import List

from src.dto.core.rule import Rule
from src.model.project.job_status import JobStatus
from src.model.data_source.source_type import SourceType


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class DataSourceModel:
    project_id: str
    source_type: SourceType = field(metadata=config(encoder=lambda x: x.value, decoder=SourceType))
    source_link: str
    is_auth_enabled: bool  # Need to revisit how to handle authenticated websites
    is_recursive: bool
    rules: List[Rule]
    job_status: JobStatus = field(metadata=config(encoder=lambda x: x.value, decoder=JobStatus))

    def set_job_status(self, job_status: JobStatus):
        self.job_status = job_status
