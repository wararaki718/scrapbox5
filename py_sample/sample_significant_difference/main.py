import pandas as pd
from scipy.stats import binom

pd.options.display.float_format = "{:.10f}".format


def main():
    k = list(range(0, 32)) # the number of appeared three of a dice
    n = 100 # the number of tests
    p = 1. / 6 # probability

    probs = binom.pmf(k, n, p)
    df = pd.DataFrame({
        "p": probs
    })
    print(df)
    print()

    print("evaluate:")
    alpha = 0.05
    n_appeared = 30
    result = alpha > probs[n_appeared]
    print(f"alpha({alpha}), prob[{n_appeared}]({probs[n_appeared]}), result: {result}")
    if result:
        print(f"null hypothesis [dismiss], alternative hypothesis [acceptance]")
    else:
        print("fnull hypothesis [not dismiss]")
    print()

    print("DONE")


if __name__ == "__main__":
    main()
