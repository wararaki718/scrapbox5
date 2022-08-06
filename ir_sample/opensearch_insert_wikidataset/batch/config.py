from dataclasses import dataclass, field

import certifi


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


@dataclass
class SearchConfig:
    index_name: str = "python-test-index"
    index_body: dict = field(
        default_factory=lambda: {"settings": {"index": {"number_of_shards": 4}}}
    )
