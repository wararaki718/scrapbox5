import pandas as pd
from sklearn.datasets import load_iris


def main():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["y"] = iris.target
    print(df.shape)

    df.to_csv("iris.csv", index=None)
    print("DONE")


if __name__ == "__main__":
    main()
