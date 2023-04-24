import pytest

from app.sub import Subtractor

@pytest.fixture
def calculator() -> Subtractor:
    return Subtractor()


def test_calc(calculator: Subtractor) -> None:
    a = 3
    b = 2

    result = calculator.calc(a, b)
    
    assert result == 1
