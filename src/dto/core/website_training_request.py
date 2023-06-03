from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json, Undefined

from src.dto.core.rule import Rule


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class WebsiteTrainingRequest:
    application_id: str
    url: str
    is_auth_enabled: bool
    is_recursive: bool
    rules: List[Rule]
