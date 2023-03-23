from loader import LTRLoader
from preprocessor import LTRPreprocessor


def main():
    #filename = "MQ2008/Fold1/train.txt"
    filename = "MQ2008/S1.txt"
    loader = LTRLoader()

    df = loader.load(filename)
    print(df.shape)

    preprocessor = LTRPreprocessor()
    X, y, df = preprocessor.transform(df)
    print(X.shape)
    print(y.shape)
    print(df.shape)

    print("DONE")


if __name__ == "__main__":
    main()
