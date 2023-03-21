import pandas as pd

from .parser import LineParser


class LTRLoader:
    def __init__(self):
        self._parser = LineParser()

    def load(self, filename: str) -> pd.DataFrame:
        features = []
        with open(filename) as f:
            for line in f:
                feature = self._parser.parse(line)
                features.append(feature)
        
        return pd.DataFrame(features)
