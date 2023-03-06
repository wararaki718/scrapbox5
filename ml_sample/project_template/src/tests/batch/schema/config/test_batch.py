from pathlib import Path

from project_template.batch.schema.config import BatchConfig


def test_load_config(config_path: Path):
    config = BatchConfig.load(config_path)
    assert isinstance(config.titanic_path, Path)
    assert isinstance(config.model_path, Path)
    assert isinstance(config.vectorizer_path, Path)
