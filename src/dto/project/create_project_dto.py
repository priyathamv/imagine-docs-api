from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined


# Order of annotations matters
@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class CreateProjectDTO:
    name: str
    owner_id: str
