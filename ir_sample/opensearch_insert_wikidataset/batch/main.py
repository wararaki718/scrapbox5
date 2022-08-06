from config import ClientConfig, SearchConfig
from client import OpenSearchClient
from loader import load_wiki
from preprocessor import Preprocessor


def main():
    df = load_wiki()
    print(df.shape)

    preprocessor = Preprocessor()
    df = preprocessor.transform(df)

    client = OpenSearchClient(ClientConfig())
    config = SearchConfig()
    response = client.create_index(config.index_name, config.index_body)
    print(response)
    
    response = client.delete_index(config.index_name)
    print(response)

    print("DONE")


if __name__ == "__main__":
    main()
