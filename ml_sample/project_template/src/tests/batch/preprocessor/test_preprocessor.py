import pandas as pd
import pytest
from _pytest.fixtures import FixtureRequest

from project_template.batch.preprocessor import TitanicPreprocessor


@pytest.fixture
def preprocessor() -> TitanicPreprocessor:
    return TitanicPreprocessor()


def test_remove_unused_columns(preprocessor: TitanicPreprocessor, full_columns_data: pd.DataFrame):
    result = preprocessor.transform(full_columns_data)
    keep_columns = set(["Pclass", "Age", "Embarked"])
    assert result[0].shape[0] == 1
    assert len(set(result[0].columns) & keep_columns) == len(keep_columns)
    assert result[1].shape[0] == 1


@pytest.mark.parametrize(
    "fixturename,expected",
    [
        ("full_columns_data", 1),
        ("missing_pclass_cell_data", 1),
        ("missing_age_cell_data", 1),
        ("missing_embarked_cell_data", 1)
    ]
)
def test_remove_rows_missing_cells(preprocessor: TitanicPreprocessor, fixturename: str, expected: int, request: FixtureRequest):
    data: pd.DataFrame = request.getfixturevalue(fixturename)
    result = preprocessor.transform(data)
    assert result[0].shape[0] == expected
