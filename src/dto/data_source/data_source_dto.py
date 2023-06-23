from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined

from src.model.data_source.data_source_model import DataSourceModel
from src.model.data_source.source_type import SourceType
from src.model.project.job_status import JobStatus


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class DataSourceDTO(DataSourceModel):
    id: str
    created_at: str
    updated_at: str

    @classmethod
    def from_website_request(cls, request_json):
        return cls(request_json['project_id'],
                   SourceType.WEBSITE,
                   request_json['source_link'],
                   request_json['is_auth_enabled'],
                   request_json['is_recursive'],
                   request_json['rules'],
                   None,
                   None,
                   JobStatus(request_json['job_status']),
                   request_json['id'],
                   request_json['created_at'],
                   request_json['updated_at'])
