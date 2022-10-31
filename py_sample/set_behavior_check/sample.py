class Base:
    def __init__(self, x: int):
        self.x = x
    
    def __str__(self) -> str:
        return f"{self.x}"

class Sample(Base):
    def __eq__(self, other: "Sample") -> bool:
        return self.x == other.x
    
    def __hash__(self) -> int:
        return hash(self.x)
