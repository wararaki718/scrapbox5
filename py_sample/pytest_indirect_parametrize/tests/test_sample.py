import pytest
from _pytest.fixtures import SubRequest

from app.sample import add, minus


@pytest.fixture
def to_str(request: SubRequest) -> str:
    return str(request.param)


@pytest.fixture
def to_set(request: SubRequest) -> set:
    return set(request.param)


@pytest.mark.parametrize(
    "to_str,y",
    [
        (1, "2")
    ],
    indirect=["to_str"]
)
def test_add(to_str: str, y: str):
    result = add(to_str, y)
    assert result == "12"


@pytest.mark.parametrize(
    "to_set,y,expected",
    [
        ([1, 2, 3], {2 ,3}, {1}),
        ([2, 3, 4], {3, 4}, {2}),
        ([3, 4, 5], {5}, {3, 4})
    ],
    indirect=["to_set"]
)
def test_minus(to_set: set, y: set, expected: set):
    result = minus(to_set, y)
    assert result == expected
