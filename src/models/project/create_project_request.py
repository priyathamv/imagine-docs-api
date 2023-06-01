from dataclasses import dataclass

@dataclass
class CreateProjectRequest():
    name: str
    owner_id: str
