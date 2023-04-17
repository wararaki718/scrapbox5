from pytorchltr.datasets import Example3

from evaluate import Evaluator
from lightgbm import LGBMRanker
# from model import NNModel
# from train import Trainer

from utils import create_dataset

def main():
    train = Example3(split="train")
    test = Example3(split="test")

    print(train.collate_fn())

    # model = NNModel(train[0].features.shape[1], 1)
    # model = LGBMRanker()
    # trainer = Trainer()
    # model = trainer.train(model, train)

    X_train, y_train, group = create_dataset(train)
    print()

    test_dataset = create_dataset(test)

    model = LGBMRanker()
    model.fit(X_train, y_train, group=group)


    # evaluator = Evaluator()
    # score = evaluator.evaluate(model, test)
    score = 1

    print(f"ndcg@10: {score}")
    print("DONE")


if __name__ == "__main__":
    main()
