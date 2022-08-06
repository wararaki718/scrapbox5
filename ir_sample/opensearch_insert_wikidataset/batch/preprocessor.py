import pandas as pd


class Preprocessor:
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.applymap(lambda x: x.decode())
        return df
