from pathlib import Path
from random import randrange
from typing import List

import pandas as pd

from schema.sentence import Sentence


class SentenceReader:
    def __init__(self):
        pass

    def read(self, filepath: Path) -> List[Sentence]:
        categories = "ABCDEFGHIJKL"
        df = pd.read_csv(filepath, sep="\t")
        return [
            Sentence(
                sentence_id=i,
                category=categories[randrange(0, len(categories))],
                price=randrange(500, 5000, 100),
                sentence=sentence["sentence"],
                is_counterfactual=sentence["is_counterfactual"],
            )
            for i, sentence in enumerate(df.to_dict(orient="records"))
        ]
