import os

import pytest
from _pytest.monkeypatch import MonkeyPatch


@pytest.fixture
def mock_env(monkeypatch: MonkeyPatch):
    monkeypatch.setenv("FOOD_BANANA", "YEAH!")


def test_banana_yeah(mock_env: None):
    value = os.getenv("FOOD_BANANA", "OH")
    assert value == "YEAH!"


def test_banana_oh():
    value = os.getenv("FOOD_BANANA", "OH")
    assert value == "OH"
