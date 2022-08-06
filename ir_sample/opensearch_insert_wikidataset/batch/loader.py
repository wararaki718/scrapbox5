import pandas as pd
import tensorflow_datasets as tfds


def load_wiki() -> pd.DataFrame:
    wiki = tfds.load("wiki40b/ja", split=["test"], data_dir=".data")
    return tfds.as_dataframe(wiki[0])
