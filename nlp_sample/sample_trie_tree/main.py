from trie_tree import TrieTree


def main():
    tree = TrieTree()

    vocabs = [
        "se",
        "see",
        "sea",
        "she",
        "sence",
        "seem",
        "seat",
        "self"
    ]
    for vocab in vocabs:
        tree.insert(vocab)

    print(f"vocabs: {vocabs}")
    print()
    
    keyword = "se"
    results = tree.suggest(keyword)
    print(f"prefix : {keyword}")
    print(f"suggest: {results}")
    print()

    keyword = "sea"
    results = tree.suggest(keyword)
    print(f"prefix : {keyword}")
    print(f"suggest: {results}")
    print()

    keyword = "ship"
    results = tree.suggest(keyword)
    print(f"prefix : {keyword}")
    print(f"suggest: {results}")
    print()

    print("DONE")


if __name__ == "__main__":
    main()
