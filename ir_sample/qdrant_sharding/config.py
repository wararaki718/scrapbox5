from dataclasses import dataclass, asdict


@dataclass
class ModelConfig:
    name: str = "line-corporation/line-distilbert-base-japanese"
    truncation: bool = True
    add_special_tokens: bool = True
    max_length: int = 128
    padding: str = "max_length"
    return_tensors: str = "pt"

    @classmethod
    def load(cls) -> "ModelConfig":
        return cls()
    
    def dict(self) -> dict:
        return asdict(self)

    def params(self) -> dict:
        params = asdict(self)
        del params["name"]
        return params
