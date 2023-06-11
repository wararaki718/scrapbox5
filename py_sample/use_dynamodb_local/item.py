from dataclasses import dataclass, asdict


@dataclass
class Item:
    username: str
    first_name: str
    last_name: str
    age: int
    account_type: str

    def to_dict(self) -> dict:
        return asdict(self)
