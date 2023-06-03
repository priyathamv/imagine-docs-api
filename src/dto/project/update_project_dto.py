from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectDTO:
    id: int
    name: str
    owner_id: str
