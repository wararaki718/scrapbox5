from unittest.mock import MagicMock

from example_taskipy.app.calculator import Calculator


def test_calculator():
    config = MagicMock()
    config.mode = "add"

    calculator = Calculator(config)
    result = calculator.compute(1, 1)
    assert result == 2
