from typing import List

from string2string.alignment import NeedlemanWunsch


def alignment(s1: List[str], s2: List[str]):
    nw = NeedlemanWunsch()
    
    a1, a2 = nw.get_alignment(s1, s2)
    print(type(a1))
    print(type(a2))

    print("s1:")
    print(f" before: {s1}")
    print(f" after : {a1}")
    print("s2:")
    print(f" before: {s2}")
    print(f" after : {a2}")
    print()


def main():
    seq1 = ['X', 'ATT', 'GC', 'GC', 'A', 'A', 'G']
    seq2 = ['ATT', 'G', 'GC', 'GC', 'A', 'C', 'G']
    alignment(seq1, seq2)
    print("DONE")


if __name__ == "__main__":
    main()
