import pytest

from project_template.api.preprocessor.components import AgesCategorizer


@pytest.fixture
def categorizer() -> AgesCategorizer:
    return AgesCategorizer()


@pytest.mark.parametrize(
    "age,expected",
    [
        (10, 10),
        (11, 10),
        (19, 10),
        (20, 20)
    ]
)
def test_transform(categorizer: AgesCategorizer, age: int, expected: int):
    result = categorizer.transform(age)
    assert result == expected
