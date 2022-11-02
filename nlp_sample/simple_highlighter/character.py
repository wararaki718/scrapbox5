from dataclasses import dataclass


@dataclass
class Character:
    base_start: int
    fixed_start: int
    base_char: str   # character
    fixed_char: str  # character

    def is_empty(self) -> bool:
        return self.fixed_char == ""

    def __eq__(self, other: "Character") -> bool:
        return self.fixed_char == other.fixed_char

    def __str__(self) -> str:
        return self.fixed_char
