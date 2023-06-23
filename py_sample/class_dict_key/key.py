from dataclasses import dataclass


@dataclass
class CustomKey:
    name: str
    value: int

    def __hash__(self):
        return hash((self.name, self.value))
    
    def __eq__(self, other: "CustomKey") -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.name == other.name and self.value == other.value

    def __str__(self) -> str:
        return f"{self.name}={self.value}"
