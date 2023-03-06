import pandas as pd
import pytest


@pytest.fixture
def embarkeds() -> pd.Series:
    return pd.Series(["A", "B", "C"])
