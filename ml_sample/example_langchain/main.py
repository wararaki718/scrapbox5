from langchain.llms import OpenAI


def main():
    # use llm
    llm = OpenAI(temperature=0.9)
    text = "犬の名前を5つ挙げてください。"

    response = llm(text)
    #print(type(response))
    print(f"Q: {text}")
    print("A:")
    print(response.strip())
    print()

    print("DONE")


if __name__ == "__main__":
    main()
