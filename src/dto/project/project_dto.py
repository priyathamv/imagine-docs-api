from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined

from src.model.project.project_model import ProjectModel


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ProjectDTO(ProjectModel):
    id: str
    created_at: str
    updated_at: str