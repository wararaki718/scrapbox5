import yaml
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def get_custom_openapi() -> dict:
    if app.openapi_schema:
        return app.openapi_schema

    with open("custom_openapi.yaml") as f:
        schema = yaml.safe_load(f)
    print("yaml loaded!")
    app.openapi_schema = schema
    return app.openapi_schema


app = FastAPI()
app.openapi = get_custom_openapi


@app.get("/ping")
def ping() -> str:
    return "pong"


@app.get("/hello")
def hello() -> str:
    return "world"


if __name__ == "__main__":
    openapi_schema = get_openapi(
        title="title",
        version="1.0.0",
        routes=app.routes
    )

    with open("openapi.yaml", "wt") as f:
        yaml.safe_dump(openapi_schema, f)
    print("DONE")
