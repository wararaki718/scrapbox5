import pytest

from app.mul import Multiplier

@pytest.fixture
def calculator() -> Multiplier:
    return Multiplier()


def test_calc(calculator: Multiplier) -> None:
    a = 1
    b = 2

    result = calculator.calc(a, b)
    
    assert result == 2
