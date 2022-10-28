from pathlib import Path

import pandas as pd
import scipy.sparse as sps

from movielens import get_movielens
from train_test_split import train_test_split

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

    user_ids = ratings.userId.unique()
    movie_ids = ratings.movieId.unique()
    user_id2index = {user_id: i for i, user_id in enumerate(user_ids)}
    movie_id2index = {movie_id: i for i, movie_id in enumerate(movie_ids)}

    X = sps.csr_matrix((
        ratings.rating,
        (
            ratings.userId.map(user_id2index),
            ratings.movieId.map(movie_id2index)
        )
    ))

    X_train, X_test = train_test_split(X)
    print(X_train.shape)
    print(X_test.shape)

    print("DONE")


if __name__ == "__main__":
    main()
