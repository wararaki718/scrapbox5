from datasets import load_dataset


def main():
    data = load_dataset("ms_marco", "v2.1")
    print(type(data))
    print("DONE")


if __name__ == "__main__":
    main()
