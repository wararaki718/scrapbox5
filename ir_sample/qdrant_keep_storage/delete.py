from client import SearchClient


def main():
    collection_name = "sample"
    client = SearchClient()

    _ = client.delete_index(collection_name)
    print(f"index deleted: {collection_name}")

    print("DONE")


if __name__ == "__main__":
    main()
