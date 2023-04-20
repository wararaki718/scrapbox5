from pathlib import Path

import numpy as np
import pandas as pd


def load_group(filepath: Path) -> np.ndarray:
    df = pd.read_csv(filepath, header=None)
    group = df.values.flatten()
    return group
