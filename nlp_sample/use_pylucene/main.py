from analyzer import TextAnalyzer


def main():
    analyzer = TextAnalyzer()
    text = "私は東京でご飯を食べます。"
    tokens = analyzer.analyze(text)
    print(text)
    print(" ".join(tokens))
    print()
    print("DONE")


if __name__ == "__main__":
    main()
