import numpy as np
import pytest

from project_template.survive.postprocessor import ResultPostprocessor


@pytest.fixture
def postprocessor() -> ResultPostprocessor:
    return ResultPostprocessor()


def test_transform(postprocessor: ResultPostprocessor):
    y = np.array([0])
    result: int = postprocessor.transform(y)
    assert result == 0
