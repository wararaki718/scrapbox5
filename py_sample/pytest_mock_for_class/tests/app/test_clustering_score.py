from unittest.mock import MagicMock, patch
from typing import Generator

import pytest

from app.clustering_score import ClusteringScorer


def cluster_mock() -> MagicMock:
    mock = MagicMock()
    mock.transform = MagicMock(return_value=1)
    return mock


@pytest.fixture
def scorer() -> Generator[MagicMock, None, None]:
    with patch("app.clustering_score.AgeCluster", return_value=cluster_mock()):
        with patch("app.clustering_score.TitleCluster", return_value=cluster_mock()):
            yield ClusteringScorer("filepath")


def test_score(scorer: MagicMock):
    x = [1, 2, 3]
    result = scorer.transform(x)
    assert result == 1
