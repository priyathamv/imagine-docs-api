from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json

from src.dto.rule import Rule


@dataclass_json
@dataclass
class WebsiteTrainingRequest():
    application_id: str
    url: str
    is_auth_enabled: bool
    is_recursive: bool
    rules: List[Rule]
