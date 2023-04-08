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
    train_iter = preprocessor.transform(df)
    train_iter.shape()
    del df
    gc.collect()

    # load valid
    filename = "MQ2008/Fold1/vali.txt"
    df = loader.load(filename)
    valid_iter = preprocessor.transform(df)
    valid_iter.shape()
    del df
    gc.collect()

    epochs = 2000
    model = try_gpu(MLPModel(train_iter.get_n_features(), 1, 16))
    trainer = LTRTrainer()
    model = trainer.train(model, train_iter, valid_iter, epochs=epochs)

    evaluator = LTREvaluator()
    filename = "MQ2008/Fold1/test.txt"
    df = loader.load(filename)
    test_iter = preprocessor.transform(df)
    score = evaluator.evaluate(model, test_iter)
    print(score)

    print("DONE")


if __name__ == "__main__":
    main()
