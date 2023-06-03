from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json

from .rule_type import RuleType


@dataclass_json
@dataclass
class Rule():
    rule_type: RuleType
    exact_match_list: List[str]
    starts_with_list: List[str]
    contains_list: List[str]
