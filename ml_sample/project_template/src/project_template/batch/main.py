import gc
import logging
from pathlib import Path

import typer

from .dumpers import ModelDumper, VectorizerDumper
from .estimator import SurviverClassifier
from .loaders import TitanicLoader
from .preprocessor import TitanicPreprocessor
from .schema.config import BatchConfig
from .vectorizer import TitanicVectorizer


logging.basicConfig(level=logging.INFO, format="%(asctime)s : %(levelname)s : %(name)s : %(message)s")
logger = logging.getLogger(__name__)


def app(config_path: str = typer.Argument("project_template/batch/config.yml")):
    config = BatchConfig.load(Path(config_path))

    titanic_loader = TitanicLoader()
    df = titanic_loader.load(config.titanic_path)
    logger.info(df.shape)
    
    titanic_preprocessor = TitanicPreprocessor()
    df, y = titanic_preprocessor.transform(df)
    logger.info(df.shape)

    titanic_vectorizer = TitanicVectorizer()
    x = titanic_vectorizer.fit_transform(df)
    del df
    gc.collect()
    logger.info(x.shape)

    classifier = SurviverClassifier()
    classifier.fit(x, y)
    del x
    del y
    gc.collect()
    logger.info("model trained")

    # TODO: evaluator

    vectorizer_dumper = VectorizerDumper()
    vectorizer_dumper.dump(titanic_vectorizer, config.vectorizer_path)
    
    model_dumper = ModelDumper()
    model_dumper.dump(classifier, config.model_path)

    logger.info("save models.")
    logger.info("DONE")


def main():
    typer.run(app)
