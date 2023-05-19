import pandas as pd
from pandera.typing import DataFrame

from schema import Users


def main():
    users = DataFrame[Users]({
        "name": ["test", "sample"],
        "age": [1, 2]
    })
    print(users)
    print(users.values)
    print()

    df = pd.DataFrame({
        "name": ["test", "sample"],
        "age": [1, 2]
    })
    users2 = DataFrame[Users](df)
    print(users2)
    print()

    df = pd.read_csv("sample.csv")
    users3 = DataFrame[Users](df)
    print(users3)
    print()

    print("DONE")


if __name__ == "__main__":
    main()
