from pathlib import Path
from typing import Generator
from unittest.mock import patch, MagicMock

import numpy as np
import pytest

from project_template.api.vectorizer.components import EmbarkedVectorizer


@pytest.fixture
def vectorizer() -> Generator[EmbarkedVectorizer, None, None]:
    vectorizer = MagicMock()
    vectorizer.transform = MagicMock(return_value=np.array([[1]]))
    with patch("project_template.api.vectorizer.components.embarked.joblib.load", return_value=vectorizer):
        yield EmbarkedVectorizer(Path("dummy"))


def test_transform(vectorizer: EmbarkedVectorizer):
    x = np.array([[1]])
    result = vectorizer.transform(x)
    assert result[0][0] == 1
