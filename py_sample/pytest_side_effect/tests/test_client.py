from typing import Dict, Generator, Optional, Union
from unittest.mock import MagicMock, patch

import pytest

from app.client import SearchClient


@pytest.fixture
def client() -> SearchClient:
    return SearchClient()


def side_effect(token: Optional[str]) -> Dict[str, Optional[Union[str, int]]]:
    if token is not None:
        return  {"id": 100, "name": "test_item", "next_token": "test"}
    
    return  {"id": 100, "name": "custom_item", "next_token": "custom"} 


def custom_dummy_client() -> MagicMock:
    custom_client = MagicMock()
    custom_client.scroll = MagicMock()
    custom_client.scroll.side_effect = side_effect
    return custom_client


@pytest.fixture
def custom_client() -> Generator[SearchClient, None, None]:
    with patch("app.client.DummyClient", custom_dummy_client):
        yield SearchClient()


def test_search_client(client: SearchClient) -> None:
    token = None
    response = client.scroll(token)

    assert response["name"] == "none_item"


def test_custom_client(custom_client: SearchClient) -> None:
    token = None
    response = custom_client.scroll(token)

    assert response["name"] == "custom_item"


def test_custom_client_with_token(custom_client: SearchClient) -> None:
    token = "custom"
    response = custom_client.scroll(token)

    assert response["name"] == "test_item"
