from unittest.mock import MagicMock

import pytest



@pytest.fixture
def model() -> MagicMock:
    dummy = MagicMock()
    dummy._model = b"dummy"
    return dummy
