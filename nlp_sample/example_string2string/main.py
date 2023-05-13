from typing import List

from string2string.alignment import NeedlemanWunsch
from string2string.distance import LevenshteinEditDistance
from string2string.misc import Tokenizer


def alignment(s1: List[str], s2: List[str]):
    nw = NeedlemanWunsch()
    
    a1, a2 = nw.get_alignment(s1, s2)
    # print(type(a1))
    # print(type(a2))

    print("s1:")
    print(f" before: {s1}")
    print(f" after : {a1}")
    print("s2:")
    print(f" before: {s2}")
    print(f" after : {a2}")
    print()


def distance(s1: str, s2: str):
    levenshtein = LevenshteinEditDistance()

    score = levenshtein.compute(s1, s2)
    print(f"str levenshtein: {score}")

    tokenizer = Tokenizer()
    t1 = tokenizer.tokenize(s1)
    t2 = tokenizer.tokenize(s2)
    score = levenshtein.compute(t1, t2)
    print(f"List[str] levenshtein: {score}")
    print()


def main():
    seq1 = ['X', 'ATT', 'GC', 'GC', 'A', 'A', 'G']
    seq2 = ['ATT', 'G', 'GC', 'GC', 'A', 'C', 'G']
    alignment(seq1, seq2)

    text1 = "The quick brown fox jumps over the lazy dog"
    text2 = "The kuack brown box jumps over the lazy dog"
    distance(text1, text2)
    print("DONE")


if __name__ == "__main__":
    main()
