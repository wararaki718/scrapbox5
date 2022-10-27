from pathlib import Path
from typing import List

import pandas as pd
import scipy.sparse as sps

from mmr import mmr
from movielens import get_movielens
from recommender import ItemRecommender


def show(df: pd.DataFrame):
    print(df.shape)
    print(df.columns)
    print(df.head(3))
    print()


def show2(before_ids: List[int], after_ids: List[int]):
    for i, (before_id, after_id) in enumerate(zip(before_ids, after_ids), start=1):
        print(f"{i}: before={before_id} -> after={after_id}")
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
    movie_index2id = {i: movie_id for i, movie_id in enumerate(movie_ids)}

    X = sps.csr_matrix((
        ratings.rating,
        (
            ratings.userId.map(user_id2index),
            ratings.movieId.map(movie_id2index)
        )
    ))
    recommender = ItemRecommender(factors=32)
    recommender.fit(X)

    movie_id = 12
    movie_ids, scores = recommender.recommend(movie_id, n=10)
    fixed_ids, fixed_scores = mmr(
        X.T[movie_id].toarray(),
        X.T[movie_ids].toarray(),
        movie_ids,
        lambda_=0.5
    )

    print()
    print(f"search movie_id: {movie_index2id[movie_id]}")
    print("before -> after:")
    item_results = [movie_index2id[movie_id] for movie_id in movie_ids]
    fixed_results = [movie_index2id[movie_id] for movie_id in fixed_ids]
    show2(item_results, fixed_results)

    print("DONE")


if __name__ == "__main__":
    main()
