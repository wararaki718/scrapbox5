from fastapi import FastAPI

from .schemas.config import ClientConfig, ModelConfig, SearchConfig
from .schemas.request import Query
from .schemas.response import SearchResults
from .search import VectorSearch


app = FastAPI()


client_config = ClientConfig.load()
model_config = ModelConfig.load()
search_config = SearchConfig.load()

vector_search = VectorSearch(
    client_config,
    model_config,
    search_config
)

@app.get("/ping")
def ping() -> str:
    return "ping"


@app.post("/search", response_model=SearchResults)
def search(query: Query) -> SearchResults:
    results = vector_search.search(query.context)
    return SearchResults(results=results)
