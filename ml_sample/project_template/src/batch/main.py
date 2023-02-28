from pathlib import Path

import typer

from loaders import TitanicLoader
from preprocessor import TitanicPreprocessor
from schema.config import BatchConfig
from vectorizer import TitanicVectorizer


def main(config_path: str = typer.Argument("batch/config.yml")):
    config = BatchConfig.load(Path(config_path))

    titanic_loader = TitanicLoader()
    df = titanic_loader.load(config.titanic_path)
    print(df.shape)
    
    titanic_preprocessor = TitanicPreprocessor()
    df = titanic_preprocessor.transform(df)
    print(df.shape)

    titanic_vectorizer = TitanicVectorizer()
    x = titanic_vectorizer.fit_transform(df)
    print(x.shape)

    

    print("DONE")


if __name__ == "__main__":
    typer.run(main)
