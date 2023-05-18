from fastapi import FastAPI

from service import CalculatorService
from schema.request import Params
from schema.response import Result


app = FastAPI()


@app.post("/calc", response_model=Result)
def calc(params: Params) -> Result:
    result = CalculatorService.calculate(params.a, params.b, params.mode)
    return Result(result=result)