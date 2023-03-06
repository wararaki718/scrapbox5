import pandas as pd
import pytest

from project_template.batch.vectorizer.components import EmbarkedVectorizer


@pytest.fixture
def vectorizer() -> EmbarkedVectorizer:
    return EmbarkedVectorizer()


def test_vectorize_embarked(vectorizer: EmbarkedVectorizer, embarkeds: pd.Series):
    result = vectorizer.fit_transform(embarkeds)
    assert result.shape[0] == 3
    assert result.shape[1] == 3
