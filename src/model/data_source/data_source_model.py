from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, Undefined, config
from typing import List, Optional

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
    text: Optional[str]
    title: Optional[str]
    job_status: JobStatus = field(metadata=config(encoder=lambda x: x.value, decoder=JobStatus))

    @classmethod
    def from_file_request(cls, project_id: str):
        return cls(project_id, SourceType.FILE, '', False, False, [], None, None, JobStatus.NOT_INITIATED)

    @classmethod
    def from_website_request(cls, request_json):
        return cls(request_json['project_id'], SourceType.WEBSITE, request_json['source_link'],
                   request_json['is_auth_enabled'], request_json['is_recursive'], request_json['rules'],
                   None, None, JobStatus.NOT_INITIATED)

    @classmethod
    def from_text_request(cls, request_json):
        return cls(request_json['project_id'], SourceType.PLAIN_TEXT, '', False, False, [], request_json['text'],
                   request_json['title'], JobStatus.NOT_INITIATED)
