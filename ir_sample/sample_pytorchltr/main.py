from pytorchltr.datasets import Example3

from evaluate import Evaluator
from model import NNModel
from train import Trainer


def main():
    train = Example3(split="train")
    test = Example3(split="test")

    model = NNModel(train[0].features.shape[1], 1)
    trainer = Trainer()
    model = trainer.train(model, train)

    evaluator = Evaluator()
    score = evaluator.evaluate(model, test)

    print(f"ndcg@10: {score}")

    print("DONE")


if __name__ == "__main__":
    main()
