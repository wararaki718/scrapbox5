from loader import LTRLoader


def main():
    filename = "MQ2008/S1.txt"
    loader = LTRLoader()

    df = loader.load(filename)
    print(df.shape)
    print("DONE")


if __name__ == "__main__":
    main()
