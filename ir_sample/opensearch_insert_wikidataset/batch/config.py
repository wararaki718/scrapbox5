from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Optional


@dataclass
class ClientConfig:
    hosts: list = field(
        default_factory=lambda: [{"host": "localhost", "port": 9200}]
    )
    http_compress: bool = True
    http_auth: tuple = ("admin", "admin")
    use_ssl: bool = True
    verify_certs: bool = False
    ssl_assert_hostname: bool = False
    ssl_show_warn: bool = False

    @classmethod
    def load(cls) -> "ClientConfig":
        return cls()


@dataclass
class SearchConfig:
    index_name: str = "python-test-index"
    index_body: dict = field(
        default_factory=lambda: {"settings": {"index": {"number_of_shards": 4}}}
    )

    @classmethod
    def load(cls, index_name: Optional[str]=None, index_body_path: Optional[Path]=None) -> "SearchConfig":
        if index_name is None and index_body_path is None:
            return cls()
        
        if index_body_path is None:
            return cls(index_name=index_name)
        
        with open(index_body_path) as f:
            body = json.load(f)
        
        if index_name is None:
            return cls(index_body=body)
        
        return cls(index_name=index_name, index_body=body)


@dataclass
class TrainConfig:
    model_name: str
    model_params: dict

    @classmethod
    def load(cls, model_name: str, model_params_path: Path) -> "TrainConfig":
        with open(model_params_path) as f:
            params = json.load(f)
        
        return cls(model_name=model_name, model_params=params)
