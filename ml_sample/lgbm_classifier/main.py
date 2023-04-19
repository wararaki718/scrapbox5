from lightgbm import LGBMClassifier
from sklearn.datasets import load_iris


def main():
    iris = load_iris()
    X = iris.data
    y = iris.target

    print(X.shape)
    print(y.shape)

    model = LGBMClassifier()
    model.fit(X, y)
    
    print(model.score(X, y))
    print("DONE")


if __name__ == "__main__":
    main()
