from example_taskipy.app.schema.config import CalculatorConfig
from .add import compute_add
from .sub import compute_sub


class Calculator:
    def __init__(self, config: CalculatorConfig) -> None:
        if config.mode == "add":
            self._compute = compute_add
        elif config.mode == "sub":
            self._compute = compute_sub
        else:
            self._compute = compute_add

    def compute(self, x: int, y: int) -> int:
        return self._compute(x, y)
