from py._path.local import LocalPath
from pathlib import Path

import pytest


@pytest.fixture
def config_path(tmp_path: LocalPath) -> Path:
    csv_path = Path(tmp_path) / "config.yaml"
    csv_path.write_text("titanic_path: titanic.csv\nmodel_path: model.pkl\nvectorizer_path: vectorizer.pkl")
    return csv_path
