from pathlib import Path
from typing import Generator
from unittest.mock import patch, MagicMock

import numpy as np
import pytest

from project_template.api.estimator import SurviveEstimator


@pytest.fixture
def estimator() -> Generator[SurviveEstimator, None, None]:
    config = MagicMock()
    config.model_path = Path("dummy")

    model = MagicMock()
    model.predict = MagicMock(return_value=np.array([1]))
    with patch("project_template.api.estimator.estimator.joblib.load", return_value=model):
        yield SurviveEstimator(config)


def test_estimate(estimator: SurviveEstimator):
    x = np.array([[1, 2, 3, 4]])
    y = estimator.estimate(x)
    assert y[0] == 1
