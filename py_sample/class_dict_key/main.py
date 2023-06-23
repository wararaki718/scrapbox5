from collections import Counter

from key import CustomKey


def main() -> None:
    k1 = CustomKey("k1", 1)
    k2 = CustomKey("k2", 2)
    k3 = CustomKey("k3", 3)
    k4 = CustomKey("k1", 1)
    d = {k1: "v1", k2: "v2", k3: "v3"}

    for key, value in d.items():
        print(key, value)
    print()

    a = [k1, k2, k3, k4]
    counter = Counter(a)
    print(counter)
    for key, value in counter.items():
        print(key, value)

    print("DONE")


if __name__ == "__main__":
    main()
