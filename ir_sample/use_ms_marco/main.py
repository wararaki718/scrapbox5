from datasets import load_dataset, DatasetDict


def main():
    # data = load_dataset("ms_marco", "v2.1")
    data: DatasetDict = load_dataset("ms_marco", "v1.1")
    print(type(data))
    print(data.shape)
    print(data["test"])
    print("DONE")


if __name__ == "__main__":
    main()
