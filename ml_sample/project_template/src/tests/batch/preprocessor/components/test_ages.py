import pandas as pd
import pytest
from _pytest.fixtures import SubRequest

from project_template.batch.preprocessor.components import AgesCategorizer


@pytest.fixture
def categorizer() -> AgesCategorizer:
    return AgesCategorizer()


@pytest.fixture
def ages(request: SubRequest) -> pd.Series:
    return pd.Series([request.param])


@pytest.mark.parametrize(
    "ages,expected",
    [
        (10, 10),
        (21, 20),
        (39, 30)
    ],
    indirect=["ages"]
)
def test_categorize_ages(categorizer: AgesCategorizer, ages: pd.Series, expected: int):
    result = categorizer.transform(ages)
    assert result.shape[0] == 1
    assert result[0] == expected
