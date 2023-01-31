import warnings


def main():
    print("copy")
    with warnings.catch_warnings():
        import pandas as pd

    df = pd.DataFrame([
        [1, 11],
        [2, 22],
        [3, 33]
    ], columns=["A", "B"], index=['a', 'b', 'c'])

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        df[df['B']==11]['A'] = 1

    ## output warning.
    df[df['B']==11]['A'] = 1

    print("DONE")


if __name__ == "__main__":
    main()
