from suggester import BinarySearchSuggester, BruteForceSuggester, EdgeNGramSuggester, NGramSuggester, TrieTreeSuggester


def main():
    suggestions = [
        "banana",
        "baloon",
        "baby",
        "bad",
        "bag",
        "byte",
        "bat",
        "but",
        "bug",
        "ban",
        "bound",
        "bowl",
        "boss",
        "bottom",
        "boom",
        "both"
    ]

    suggesters = {
        "binary_search": BinarySearchSuggester(),
        "brute_force": BruteForceSuggester(),
        "edge_ngram": EdgeNGramSuggester(),
        "ngram": NGramSuggester(),
        "trie_tree": TrieTreeSuggester()
    }
    
    for name, suggester in suggesters.items():
        print(f"[{name} suggester]")
        suggester.index(suggestions)
        for prefix in ["bo", "ba"]:
            print(f"prefix: {prefix}")
            for result in suggester.search(prefix):
                print(f" - {result}")
            print()

    print("DONE")


if __name__ == "__main__":
    main()
