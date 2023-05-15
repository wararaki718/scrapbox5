from fastapi import FastAPI

from .schema import Request, Response


app = FastAPI()


@app.get("/ping")
def ping() -> str:
    return "pong"


@app.post("/calc", response_model=Response)
def calc(request: Request) -> Response:
    result = -1
    if request.mode == "add":
        result = request.a + request.b
    elif request.mode == "sub":
        result = request.a - request.b

    return Response(result=result)
