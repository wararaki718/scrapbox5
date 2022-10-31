from sample import Base, Sample


def main():
    a = set()
    a.add(Sample(1))
    a.add(Sample(2))
    a.add(Sample(1))
    for i in a:
        print(i)
    print("DONE")


if __name__ == "__main__":
    main()
