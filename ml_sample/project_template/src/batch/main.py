from pathlib import Path

import typer

from loaders import TitanicLoader
from schema.config import BatchConfig


def main(config_path: str = typer.Argument("batch/config.yml")):
    config = BatchConfig.load(Path(config_path))
    titanic_loader = TitanicLoader()
    df = titanic_loader.load(config.titanic_path)
    print(df.shape)
    print("DONE")


if __name__ == "__main__":
    typer.run(main)
