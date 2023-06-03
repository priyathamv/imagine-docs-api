from dataclasses import dataclass
from datetime import datetime

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Project:
    id: int
    name: str
    owner_id: str
    created_at: datetime
    updated_at: datetime
