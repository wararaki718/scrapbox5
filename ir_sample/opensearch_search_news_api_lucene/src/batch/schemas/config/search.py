from dataclasses import dataclass, asdict


@dataclass
class SearchConfig:
    index_name: str = "sample-knn-index"

    @classmethod
    def load(cls) -> "SearchConfig":
        return cls()

    def dict(self) -> dict:
        return asdict(self)
