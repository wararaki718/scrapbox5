from typing import Generator
from unittest.mock import patch

import pytest

from app.calculator import Calculator


@pytest.fixture
def add_calculator() -> Calculator:
    return Calculator()


@pytest.fixture
def minus_calculator() -> Generator[Calculator, None, None]:
    def minus(self, a: int, b: int) -> int:
        return a - b

    with patch("app.calculator.Calculator.calc", minus):
        yield Calculator()


def test_add(add_calculator: Calculator):
    result = add_calculator.calc(1, 1)
    assert result == 2


def test_minus(minus_calculator: Calculator):
    result = minus_calculator.calc(1, 1)
    assert result == 0
