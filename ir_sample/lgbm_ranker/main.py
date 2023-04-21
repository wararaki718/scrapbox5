import gc

from pytorchltr.datasets import MSLR10K

# from evaluate import Evaluator
from lightgbm import LGBMRanker
# from model import NNModel
# from train import Trainer

from utils import create_dataset

def main():
    train = MSLR10K(split="train")
    X_train, y_train, group = create_dataset(train, n_sample=5)
    del train
    gc.collect()
    
    print(X_train)
    print()
    print(y_train)
    print()
    print(group)

    model = LGBMRanker(n_estimators=50, boosting_type="gbdt", num_leaves=41, learning_rate=0.01, n_jobs=-1, random_state=42)
    model.fit(X_train, y_train, group=group, verbose=True)
    del X_train, y_train, group
    gc.collect()

    print("test")
    test = MSLR10K(split="test")
    X_test, y_test, group = create_dataset(test)

    # evaluator = Evaluator()
    # score = evaluator.evaluate(model, test)
    score = 1

    print(f"ndcg@10: {score}")
    print("DONE")


if __name__ == "__main__":
    main()
