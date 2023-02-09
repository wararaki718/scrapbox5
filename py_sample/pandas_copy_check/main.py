import pandas as pd


def test() -> pd.DataFrame:
    df = pd.DataFrame({"1": [1, 2, 3]})
    print(id(df))
    return df


def test2() -> pd.DataFrame:
    df = pd.DataFrame({"1": [1, 2, 3]})
    print(id(df))
    return df.reset_index(drop=True)


def test3() -> pd.DataFrame:
    df = pd.DataFrame({"1": [1, 2, 3]})
    print(id(df))
    df.reset_index(drop=True, inplace=True)
    print(id(df))
    return df


def main():
    print("test1:")
    df = test()
    print(id(df))
    print()

    print("test2:")
    df2 = test2()
    print(id(df2))
    print()

    print("test3:")
    df3 = test3()
    print(id(df3))
    print()

    print("DONE")


if __name__ == "__main__":
    main()
