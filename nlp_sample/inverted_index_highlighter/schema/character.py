from dataclasses import dataclass

from .link import LinkType

@dataclass
class Character:
    index: int
    value: str  # character
    link: LinkType = LinkType.NONE

    def is_empty(self) -> bool:
        return self.value == ""

    def __eq__(self, other: "Character") -> bool:
        return self.value == other.value

    def __str__(self) -> str:
        if self.value == "EOF":
            return ""
        return self.value
