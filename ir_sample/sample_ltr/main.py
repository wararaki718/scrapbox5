from evaluator import LTREvaluator
from loader import LTRLoader
from model import MLPModel
from preprocessor import LTRPreprocessor
from trainer import LTRTrainer


def main():
    filename = "MQ2008/Fold1/train.txt"
    # filename = "MQ2008/S1.txt"
    loader = LTRLoader()

    df = loader.load(filename)
    print(df.shape)

    preprocessor = LTRPreprocessor()
    X, y, df = preprocessor.transform(df)
    print(X.shape)
    print(y.shape)
    print(df.shape)

    epochs = 10
    model = MLPModel(X.shape[1], 1, 16)
    trainer = LTRTrainer()
    model = trainer.train(model, X, y, epochs=epochs)

    evaluator = LTREvaluator()
    score = evaluator.evaluate(model, X, y)
    print(score)

    print("DONE")


if __name__ == "__main__":
    main()
