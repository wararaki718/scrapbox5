from pathlib import Path

import lightgbm
from lightgbm import LGBMRanker, Dataset
from scipy.stats import spearmanr
from sklearn.datasets import load_svmlight_files

from loader import load_group


def main():
    test_path = "data/rank.test"
    train_path = "data/rank.train"
    query_path = Path("data/rank.train.query")

    X_train, y_train, X_test, y_test = load_svmlight_files(
        [train_path, test_path]
    )
    train_group = load_group(query_path)
    print(X_train.shape)
    print(y_train.shape)
    print(X_test.shape)
    print(y_test.shape)
    print(train_group.shape)
    print(sum(train_group))

    model = LGBMRanker(
        num_leaves=50,
        n_estimators=200,
        random_state=42
    )
    model.fit(X_train, y_train, group=train_group)
    preds = model.predict(X_test)
    print(spearmanr(y_test, preds))
    print()

    data = Dataset(X_train, label=y_train, group=train_group) 
    params = {
        "objective": "lambdarank",
        "boosting_type": "gbdt",
        "random_state": 42,
        "force_row_wise": True
    }
    ranker = lightgbm.train(params=params, train_set=data)
    preds = ranker.predict(X_test)
    print(spearmanr(y_test, preds))

    print("DONE")


if __name__ == "__main__":
    main()
