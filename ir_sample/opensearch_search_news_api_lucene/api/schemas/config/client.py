from dataclasses import dataclass, field, asdict


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
    
    def dict(self) -> dict:
        return asdict(self)
