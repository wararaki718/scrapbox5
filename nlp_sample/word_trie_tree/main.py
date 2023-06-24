from typing import List, Tuple

from trie_tree import TrieTree


def show(keywords: List[str], results: List[Tuple[str]]) -> None:
    print(f"keywords: {keywords}")
    print("suggest:")
    for result in results:
        print(result)
    print()


def main() -> None:
    tree = TrieTree()

    tokens = [
        ["hello", "world"],
        ["hello"],
        ["world"],
        ["hello", "good"],
        ["good"],
        ["hello", "good", "game"],
        ["good", "game"],
        ["good", "great"]
    ]
    for token in tokens:
        tree.insert(token)

    keywords = ["hello"]
    results = tree.suggest(keywords)
    show(keywords, results)

    keywords = ["good"]
    results = tree.suggest(keywords)
    show(keywords, results)

    keywords = ["hello", "good"]
    results = tree.suggest(keywords)
    show(keywords, results)

    keywords = ["world"]
    results = tree.suggest(keywords)
    show(keywords, results)

    print("DONE")


if __name__ == "__main__":
    main()
