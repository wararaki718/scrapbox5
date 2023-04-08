import gc

from evaluator import LTREvaluator
from loader import LTRLoader
from model import MLPModel
from preprocessor import LTRPreprocessor
from trainer import LTRTrainer
from utils import try_gpu


def main():
    filename = "MQ2008/Fold1/train.txt"
    # filename = "MQ2008/S1.txt"
    loader = LTRLoader()

    df = loader.load(filename)
    print(df.shape)

    preprocessor = LTRPreprocessor()
    batch_iter = preprocessor.transform(df)
    batch_iter.shape()
    del df
    gc.collect()

    epochs = 2000
    model = try_gpu(MLPModel(batch_iter.get_n_features(), 1, 16))
    trainer = LTRTrainer()
    model = trainer.train(model, batch_iter, epochs=epochs)

    filename = "MQ2008/Fold1/test.txt"
    df = loader.load(filename)
    batch_iter = preprocessor.transform(df)
    evaluator = LTREvaluator()
    score = evaluator.evaluate(model, batch_iter)
    print(score)

    print("DONE")


if __name__ == "__main__":
    main()
