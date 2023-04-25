from client import SearchClient


def main():
    client = SearchClient()
    token = None
    for _ in range(3):
        response = client.scroll(token)
        print(response)
        token = response["next_token"]
    
    print("DONE")


if __name__ == "__main__":
    main()
