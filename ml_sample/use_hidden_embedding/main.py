from pathlib import Path

from loader import DataLoader
from preprocessor import TextPreprocessor
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

    ## TODO: model definition
    ## TODO: get embedding

    print("DONE")


if __name__ == "__main__":
    main()