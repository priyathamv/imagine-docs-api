from dataclasses import dataclass

@dataclass
class UpdateProjectRequest():
    id: str
    name: str
    owner_id: str
