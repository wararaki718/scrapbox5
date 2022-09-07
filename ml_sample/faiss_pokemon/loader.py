from pathlib import Path

import pandas as pd


def load_pokemon(filepath: Path) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    df = pd.concat([
        df,
        pd.get_dummies(df["Type 1"]),
        pd.get_dummies(df["Type 2"])
    ], axis=1)
    df.drop(["#", "Type 1", "Type 2"], axis=1, inplace=True)
    df["Legendary"] = df["Legendary"].astype(int)
    return df
