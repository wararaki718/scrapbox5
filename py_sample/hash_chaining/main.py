from typing import List

from hash import Hash


def show_table(table: Hash):
    for i, row in enumerate(table):
        print(f"{i}: {row}")


def main():
    n = 8
    a = [1, 5, 4, 2, 3, 8, 12, 15, 23]
    hash = Hash(n)
    
    for i in a:
        hash.insert(i)
    show_table(hash)
    print()

    hash.delete(a[3])
    show_table(hash)
    print()

    print("DONE")


if __name__ == "__main__":
    main()
