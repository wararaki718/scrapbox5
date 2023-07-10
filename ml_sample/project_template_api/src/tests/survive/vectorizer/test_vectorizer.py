from pathlib import Path
from typing import Generator
from unittest.mock import patch, MagicMock

import numpy as np
import pytest

from project_template.survive.vectorizer import PassengerVectorizer


@pytest.fixture
def vectorizer() -> Generator[PassengerVectorizer, None, None]:
    config = MagicMock()
    config.vectorizer_path = Path("dummy")

    embarked_vectorizer = MagicMock()
    embarked_vectorizer.transform = MagicMock(return_value=np.array([[1]]))

    with patch("project_template.survive.vectorizer.components.embarked.joblib.load", return_value=embarked_vectorizer):
        yield PassengerVectorizer(config)


@pytest.fixture
def passenger() -> MagicMock:
    passenger = MagicMock()
    passenger.Pclass = [[1]]
    passenger.Age = [[11]]
    passenger.Embarked = [["C"]]
    passenger.Ages = [[10]]
    return passenger


def test_transform(vectorizer: PassengerVectorizer, passenger: MagicMock):
    result = vectorizer.transform(passenger)
    assert result.shape[0] == 1
    assert result.shape[1] == 4
