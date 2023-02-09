from unittest.mock import MagicMock

import pytest

from app.modules import Shop


@pytest.fixture
def item_mock() -> MagicMock:
    item = MagicMock()
    item.id = 1
    item.name = "fruit"
    item.price = 100
    return item


@pytest.fixture
def shop_has_item(item_mock: MagicMock) -> Shop:
    shop = Shop()
    shop.set_item(item_mock)
    return shop


def test_show_get_item(shop_has_item: Shop):
    result = shop_has_item.get_item(0)
    assert result.id == 1
    assert result.name == "fruit"
    assert result.price == 100
