from pytorchltr.datasets import MSLR30K

from evaluate import Evaluator
from model import NNModel
from train import Trainer
from utils import try_gpu


def main():
    train = MSLR30K(split="train")
    test = MSLR30K(split="test")

    model = NNModel(train[0].features.shape[1], 1)
    model = try_gpu(model)

    print()
    trainer = Trainer()
    model = trainer.train(model, train)

    evaluator = Evaluator()
    score = evaluator.evaluate(model, test)

    print(f"ndcg@10: {score}")

    print("DONE")


if __name__ == "__main__":
    main()
