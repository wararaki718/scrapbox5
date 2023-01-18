from typing import Generator
from unittest.mock import patch

import pytest

from app.calculator import Calculator


@pytest.fixture
def mul_calculator() -> Calculator:
    return Calculator()


@pytest.fixture
def add_calculator() -> Generator[Calculator, None, None]:
    def add_func(a: int, b: int) -> int:
        return a + b
    
    with patch("app.calculator.calculator.mul_func", add_func):
        yield Calculator()


def test_multiply(mul_calculator: Calculator):
    result = mul_calculator.calc(3, 3)
    assert result == 9


def test_add(add_calculator: Calculator):
    result = add_calculator.calc(3, 3)
    assert result == 6
