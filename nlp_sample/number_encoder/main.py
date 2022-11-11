from converter import NumberConverter


def main():
    converter = NumberConverter()
    texts = [
        "二〇〇五年",
        "一二三四五六七八九",
        "千円",
        "これは二万七千円です。",
        "1億9千万人"
        "四千二百万",
        "10,000万円",
        "１億円",
        "FF10,10人月で開発しました。",
        "FF10,十人月で開発しました。",
        "10.6億円",
        "0.6人月"
    ]
    for text in texts:
        result = converter.convert(text)
        print(f"before: {text}")
        print(f"after : {result}")
        print()
    print("DONE")


if __name__ == "__main__":
    main()
