from key import CustomKey


def main() -> None:
    k1 = CustomKey("k1", 1)
    k2 = CustomKey("k2", 2)
    k3 = CustomKey("k3", 3)
    d = {k1: "v1", k2: "v2", k3: "v3"}

    for key, value in d.items():
        print(key, value)

    print("DONE")


if __name__ == "__main__":
    main()
