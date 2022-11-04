from dataclasses import dataclass


@dataclass
class Character:
    base_index: int
    fixed_char: str  # character

    def is_empty(self) -> bool:
        return self.fixed_char == ""

    def __eq__(self, other: "Character") -> bool:
        return self.fixed_char == other.fixed_char

    def __str__(self) -> str:
        if self.fixed_char == "EOF":
            return ""
        return self.fixed_char
