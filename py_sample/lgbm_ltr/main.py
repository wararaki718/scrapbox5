from lightgbm import LGBMRanker

from evaluate import ndcg
from loader import DataLoader


def main():
    loader = DataLoader()
    X_train, y_train, q_train = loader.load("rank.train")
    X_test, y_test, q_test = loader.load("rank.test")
    print("data loaded.")

    params = {
        "objective": "lambdarank",
        "metric": "ndcg",
        "n_estimators": 40,
        "boosting_type": "gbdt"
    }

    model = LGBMRanker(**params)
    model.fit(X_train, y_train, group=q_train)
    print("model fitted")

    y_preds = model.predict(X_test)
    score = ndcg(y_test, y_preds, q_test)
    print(f"ndcg: {score}")

    print("DONE")


if __name__ == "__main__":
    main()
