from fastapi import FastAPI

from api.evaluator import Evaluator
from api.schema.request import Item
from api.schema.response import Result


app = FastAPI()
evaluator = Evaluator()


@app.get("/ping")
def ping() -> str:
    return "pong"


@app.post("/evaluate", response_model=Result)
def evaluate(item: Item) -> Result:
    score = evaluator.evaluate(item)
    return Result(score=score)
