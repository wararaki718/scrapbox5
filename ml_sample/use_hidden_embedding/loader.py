from pathlib import Path

import pandas as pd


class DataLoader:
    def __init__(self):
        pass

    def load(self, filepath: Path) -> pd.DataFrame:
        df = pd.read_csv(filepath, sep="\t")
        return df
