from typing import Dict, List

from dataclasses import dataclass


@dataclass
class TableConfig:
    key_schema: List[Dict[str, str]]
    attribute_definitions: List[Dict[str, str]]
    provisioned_throughput: Dict[str, int]
