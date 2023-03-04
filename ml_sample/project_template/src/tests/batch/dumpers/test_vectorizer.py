from pathlib import Path
from py._path.local import LocalPath
from unittest.mock import MagicMock

import pytest

from project_template.batch.dumpers import VectorizerDumper


@pytest.fixture
def dumper() -> VectorizerDumper:
    return VectorizerDumper()


def test_vectorizer_dump(tmp_path: LocalPath, vectorizer: MagicMock, dumper: VectorizerDumper):
    vectorizer_path = Path(tmp_path) / "vectorizer.pkl"
    dumper.dump(vectorizer, vectorizer_path)
    assert vectorizer_path.exists()
