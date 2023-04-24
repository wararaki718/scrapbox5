import pytest

from app.add import Adder

@pytest.fixture
def calculator() -> Adder:
    return Adder()


def test_calc(calculator: Adder) -> None:
    a = 3
    b = 2

    result = calculator.calc(a, b)
    
    assert result == 5
