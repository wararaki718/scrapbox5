from dataclasses import dataclass


@dataclass
class Position:
    start: int
    end: int

    def __hash__(self) -> int:
        return hash(f"{self.start}_{self.end}")

    def __eq__(self, other: "Position") -> bool:
        return self.start == other.start and self.end == other.end

    def __lt__(self, other: "Position") -> bool:
        if self.start < other.start:
            return True
        
        if self.start > other.start:
            return False
        
        return self.end < other.end
