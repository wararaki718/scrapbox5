from unittest.mock import patch, MagicMock

import pytest

from project_template.api.preprocessor import PassengerPreprocessor


@pytest.fixture
def passenger() -> MagicMock:
    passenger = MagicMock()
    passenger.Pclass = 1
    passenger.Age = 11
    passenger.Embarked = "C"
    return passenger


@pytest.fixture
def preprocessor() -> PassengerPreprocessor:
    return PassengerPreprocessor()


def test_preprocessing(preprocessor: PassengerPreprocessor, passenger: MagicMock):
    result = preprocessor.transform(passenger)
    assert result.Pclass[0][0] == 1
    assert result.Age[0][0] == 11
    assert result.Embarked[0][0] == "C"
    assert result.Ages[0][0] == 10
