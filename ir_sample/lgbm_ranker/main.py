import gc

from pytorchltr.datasets import MSLR10K

# from evaluate import Evaluator
from lightgbm import LGBMRanker
# from model import NNModel
# from train import Trainer

from utils import create_dataset

def main():
    train = MSLR10K(split="train")
    test = MSLR10K(split="test")

    # print(train.collate_fn())

    # model = NNModel(train[0].features.shape[1], 1)
    # model = LGBMRanker()
    # trainer = Trainer()
    # model = trainer.train(model, train)

    X_train, y_train, group = create_dataset(train)
    print()
    

    model = LGBMRanker()
    model.fit(X_train, y_train, group=group)
    del X_train, y_train, group
    gc.collect()

    print("test")
    X_test, y_test, group = create_dataset(test)

    # evaluator = Evaluator()
    # score = evaluator.evaluate(model, test)
    score = 1

    print(f"ndcg@10: {score}")
    print("DONE")


if __name__ == "__main__":
    main()
