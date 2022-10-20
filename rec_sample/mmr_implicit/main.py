from typing import List

from implicit.datasets.movielens import get_movielens

from mmr import mmr
from recommender import UserRecommender


def show(ids: List[int],  scores: List[float]):
    for id, score in zip(ids, scores):
        print(f"{id}: {score}")
    print()


def show2(before_ids: List[int], after_ids: List[int]):
    for i, (before_id, after_id) in enumerate(zip(before_ids, after_ids), start=1):
        print(f"{i}: before={before_id} -> after={after_id}")
    print()


def main():
    _, ratings = get_movielens("100k")
    recommender = UserRecommender(factors=32)
    recommender.fit(ratings)

    user_id = 12
    ids, scores = recommender.recommend(user_id, ratings[user_id], n=10)
    fixed_ids, fixed_scores = mmr(
        ratings[user_id].toarray(),
        ratings[ids].toarray(),
        ids,
        lambda_=0.5
    )
    print("before -> after:")
    show2(ids, fixed_ids)

    # show(ids, scores)
    # show(fixed_ids, fixed_scores)
    
    print("DONE")


if __name__ == "__main__":
    main()
