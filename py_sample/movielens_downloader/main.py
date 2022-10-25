from pathlib import Path

import pandas as pd

from movielens import get_movielens


def show(df: pd.DataFrame):
    print(df.shape)
    print(df.columns)
    print(df.head(3))
    print()


def main():
    download_dir = Path("./data")
    movies, ratings, tags, links = get_movielens(download_dir)
    show(movies)
    show(ratings)
    show(tags)
    show(links)

    print("DONE")


if __name__ == "__main__":
    main()
