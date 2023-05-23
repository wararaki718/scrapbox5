from dataclasses import dataclass


@dataclass
class SearchCondition:
    key: str
    value: str
