from pathlib import Path
from typing import List

import yaml
from pydantic import BaseModel, parse_obj_as


class User(BaseModel):
    uid: int
    name: str
    age: int

    @classmethod
    def load(cls, filepath: Path) -> List["User"]:
        with open(filepath) as f:
            config = yaml.safe_load(f)
        return parse_obj_as(List[User], config["config"])
