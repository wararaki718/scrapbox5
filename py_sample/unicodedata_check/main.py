import unicodedata


def show(text: str, char: str):
    print(f"len(char): {len(char)}, [{char}], [{char.encode('utf-8')}]")
    print(f"len(text): {len(text)}, [{text}], [{text.encode('utf-8')}]")
    for i, c in enumerate(text):
        print(f"{i}: {c}")

def encode(char: str) -> str:
    print("NFC:")
    text = unicodedata.normalize("NFC", char)
    show(text, char)

    print("NFKC:")
    text = unicodedata.normalize("NFKC", char)
    show(text, char)

    print("NFD:")
    text = unicodedata.normalize("NFD", char)
    show(text, char)

    print("NFKD:")
    text = unicodedata.normalize("NFKD", char)
    show(text, char)
    print()


def main():
    char = "か゛"
    encode(char)

    char = "あﾞ"
    encode(char)

    char = "あ゙"
    encode(char)

    char = "ゔ"
    encode(char)

    char = "゛"
    encode(char)

    char = "ぱ"
    encode(char)
    
    char = "゜"
    encode(char)
    
    char = "は゜"
    encode(char)

    char = "゜"
    encode(char)

    char = "きゃ"
    encode(char)

    print("DONE")


if __name__ == "__main__":
    main()
