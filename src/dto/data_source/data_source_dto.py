from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined

from src.model.data_source.data_source_model import DataSourceModel


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class DataSourceDTO(DataSourceModel):
    id: str
    created_at: str
    updated_at: str
