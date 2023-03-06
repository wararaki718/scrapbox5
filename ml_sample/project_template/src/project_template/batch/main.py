from pathlib import Path

from .dumpers import ModelDumper, VectorizerDumper
from .estimator import SurviverClassifier
from .loaders import TitanicLoader
from .preprocessor import TitanicPreprocessor
from .schema.config import BatchConfig
from .vectorizer import TitanicVectorizer


# TODO: use typer
def main(config_path: str = "project_template/batch/config.yml"):
    config = BatchConfig.load(Path(config_path))

    titanic_loader = TitanicLoader()
    df = titanic_loader.load(config.titanic_path)
    print(df.shape)
    
    titanic_preprocessor = TitanicPreprocessor()
    df, y = titanic_preprocessor.transform(df)
    print(df.shape)

    titanic_vectorizer = TitanicVectorizer()
    x = titanic_vectorizer.fit_transform(df)
    print(x.shape)

    classifier = SurviverClassifier()
    classifier.fit(x, y)
    print("model trained")

    # TODO: evaluator

    vectorizer_dumper = VectorizerDumper()
    vectorizer_dumper.dump(titanic_vectorizer, config.vectorizer_path)
    
    model_dumper = ModelDumper()
    model_dumper.dump(classifier, config.model_path)

    print("save models.")
    print("DONE")
