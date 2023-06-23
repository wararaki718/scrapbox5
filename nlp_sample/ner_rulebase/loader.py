import json
from pathlib import Path
from typing import List

import pandas as pd

from schema import NamedEntity

class EntityLoader:
    def __init__(self) -> None:
        pass

    def load(self, filepath: Path) -> List[NamedEntity]:
        entities = []
        with open(filepath) as f:
            items = json.load(f)
            for item in items:
                entity = NamedEntity(**item)
                entities.append(entity)
        
        return entities


class CompanyLoader:
    def __init__(self) -> None:
        pass
    
    def load(self, filepath: Path) -> List[str]:
        df = pd.read_csv(filepath, header=None)
        column = df.columns[6]
        companies: List[str] = df[column].tolist()
        return companies
