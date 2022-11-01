from spearman import spearman
from utils import get_two_ranks


def main():
    n = 10
    rank_a, rank_b = get_two_ranks(n)
    
    result = spearman(rank_a, rank_b)
    print(f"rank_a={rank_a}")
    print(f"rank_b={rank_b}")
    print(f"spearman(rank_a, rank_b)={result}")
    print("DONE")


if __name__ == "__main__":
    main()
