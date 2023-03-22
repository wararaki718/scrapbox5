from pathlib import Path

from loader import DataLoader
from model import NNModel
from preprocessor import TextPreprocessor
from saver import EmbeddingSaver
from trainer import NNTrainer
from vectorizer import TextVectorizer


def main():
    loader = DataLoader()

    filepath = Path("data/JP_train.tsv")
    df = loader.load(filepath)
    print(df.shape)
    print(df.columns)

    preprocessor = TextPreprocessor()
    sentences, y = preprocessor.transform(df)
    print(sentences.shape)
    print(y.shape)

    vectorizer = TextVectorizer()
    X = vectorizer.fit_transform(sentences)
    print(X.shape)

    model = NNModel(n_input=X.shape[1])
    trainer = NNTrainer()
    model = trainer.train(model, X, y)
    print("model trained!")

    model_path = Path("model/model.pkl")
    saver = EmbeddingSaver()
    saver.save(model, model_path)
    print("save a embedding.")

    print("DONE")


if __name__ == "__main__":
    main()
