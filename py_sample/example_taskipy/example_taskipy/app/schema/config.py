from dataclasses import dataclass


@dataclass
class CalculatorConfig:
    mode: str = "add"
