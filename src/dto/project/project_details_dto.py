from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json, Undefined

from src.dto.data_source.data_source_dto import DataSourceDTO
from src.dto.project.project_dto import ProjectDTO


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ProjectDetailsDTO(ProjectDTO):
    id: str
    created_at: str
    updated_at: str
    data_sources: List[DataSourceDTO]