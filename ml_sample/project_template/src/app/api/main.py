from pathlib import Path

from fastapi import FastAPI

from .predictor import SurvivePredictor
from .schema.config import APIConfig
from .schema.request import Passenger
from .schema.response import Result


app = FastAPI()
config = APIConfig.load(Path("app/api/config.yml"))
predictor = SurvivePredictor(config.predictor_config)


@app.get("/ping")
def ping() -> str:
    return "pong"


@app.post("/predict", response_model=Result)
def predict(passenger: Passenger) -> Result:
    result = predictor.predict(passenger)
    return Result(survived=result)
