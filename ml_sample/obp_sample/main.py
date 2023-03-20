from evaluator import Evaluator
from trainer import Trainer
from utils import get_data


def main():
    n_actions = 3
    train, valid, dataset = get_data(n_actions=n_actions)
    trainer = Trainer()
    learner = trainer.train(train, dataset.n_actions)

    evaluator = Evaluator(dataset.n_actions)
    evaluator.evaluate(learner, valid, dataset)

    print("DONE")


if __name__ == "__main__":
    main()
