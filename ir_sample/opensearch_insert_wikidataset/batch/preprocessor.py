import pandas as pd

from text import TextParser

class Preprocessor:
    def __init__(self):
        self._text_parser = TextParser()

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.applymap(lambda x: x.decode())
        df["text"] = df.text.apply(self._text_parser.parse)
        return df
