import numpy as np
import pytest

from project_template.batch.estimator import SurviverClassifier


@pytest.fixture
def classifier() -> SurviverClassifier:
    return SurviverClassifier()


def test_fit_classifier(classifier: SurviverClassifier):
    x = np.random.random(size=(20, 5))
    y = np.random.randint(0, 2, size=20)
    classifier.fit(x, y)
    assert True
