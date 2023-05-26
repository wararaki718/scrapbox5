from datasets import load_dataset
from datasets.arrow_dataset import Dataset


def main():
    # data = load_dataset("ms_marco", "v2.1")
    data: Dataset = load_dataset("ms_marco", "v1.1")
    print(type(data))
    print(data.shape)
    print(data["test"])
    print(type(data["test"]))
    test: Dataset = data["test"]
    for column in test.features:
        print(f"[{column}]:")
        print(test[column][0])
        print()
        
    print("DONE")


if __name__ == "__main__":
    main()
