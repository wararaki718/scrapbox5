from pathlib import Path
from typing import Generator
from unittest.mock import patch, MagicMock

import numpy as np
import pytest

from project_template.api.predictor import SurvivePredictor


@pytest.fixture
def predictor() -> Generator[SurvivePredictor, None, None]:
    config = MagicMock()
    config.vectorizer_config = MagicMock()
    config.vectorizer_config.vectorizer_path = Path("dummy")
    config.estimator_config = MagicMock()
    config.estimator_config.model_path = Path("dummy")

    vectorizer = MagicMock()
    vectorizer.transform = MagicMock(return_value=np.array([[1, 1, 1, 1]]))

    model = MagicMock()
    model.estimate = MagicMock(return_value=np.array([1]))

    with patch("project_template.api.predictor.PassengerVectorizer", return_value=vectorizer):
        with patch("project_template.api.predictor.SurviveEstimator", return_value=model):
            yield SurvivePredictor(config)


@pytest.fixture
def passenger() -> MagicMock:
    passenger = MagicMock()
    passenger.Pclass = 1
    passenger.Age = 11
    passenger.Embarked = "C"
    return passenger


def test_predict(predictor: SurvivePredictor, passenger: MagicMock):
    result = predictor.predict(passenger)
    assert result == 1
