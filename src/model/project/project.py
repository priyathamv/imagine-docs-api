from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Project:
    id: str
    name: str
    owner_id: str
    created_at: str
    updated_at: str
