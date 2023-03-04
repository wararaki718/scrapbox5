from pathlib import Path
from py._path.local import LocalPath
from unittest.mock import MagicMock

import pytest

from project_template.batch.dumpers import ModelDumper



@pytest.fixture
def dumper() -> ModelDumper:
    return ModelDumper()


def test_model_dump(tmp_path: LocalPath, model: MagicMock, dumper: ModelDumper):
    model_path = Path(tmp_path) / "model.pkl"
    dumper.dump(model, model_path)
    assert model_path.exists()
