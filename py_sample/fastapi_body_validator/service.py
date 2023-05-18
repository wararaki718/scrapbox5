class CalculatorService:
    @classmethod
    def calculate(cls, a: int, b: int, mode: str = "add") -> int:
        if mode == "add":
            return a + b
        
        if mode == "sub":
            return a - b
        
        if mode == "mul":
            return a * b
        
        return int(a / b)
