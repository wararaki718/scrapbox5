from unittest.mock import MagicMock

import pytest



@pytest.fixture
def model() -> MagicMock:
    dummy = MagicMock()
    dummy._model = b"dummy"
    return dummy


@pytest.fixture
def vectorizer() -> MagicMock:
    dummy = MagicMock()
    dummy._embarked_vectorizer = MagicMock()
    dummy._embarked_vectorizer._vectorizer = b"dummy"
    return dummy
