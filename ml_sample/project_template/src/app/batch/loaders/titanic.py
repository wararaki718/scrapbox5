from pathlib import Path

import pandas as pd


class TitanicLoader:
    def __init__(self):
        pass

    def load(self, filepath: Path) -> pd.DataFrame:
        df = pd.read_csv(filepath)
        return df
