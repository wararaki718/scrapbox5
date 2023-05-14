from textblob import TextBlob


def main():
    text = "I havv goood speling!"
    b = TextBlob(text)
    print(f"before: {text}")
    print(f"after : {b.correct()}")
    print("DONE")


if __name__ == "__main__":
    main()
