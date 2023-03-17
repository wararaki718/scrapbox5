from pathlib import Path
from typing import List

import pandas as pd

from sentence import Sentence


class SentenceReader:
    def __init__(self):
        pass

    def read(self, filepath: Path) -> List[Sentence]:
        df = pd.read_csv(filepath, sep="\t")
        return [
            Sentence(sentence_id=i, **sentence) for i, sentence in enumerate(df.to_dict(orient="records"))
        ]
