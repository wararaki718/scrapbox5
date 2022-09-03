from treeset import TreeSet


def main():
    treeset = TreeSet()

    treeset.add(1)
    treeset.add([2, 3, 4, 5])
    treeset.add({4, 5, 6, 7, 8})
    treeset.remove(2)

    print(treeset)

    print("DONE")


if __name__ == "__main__":
    main()
