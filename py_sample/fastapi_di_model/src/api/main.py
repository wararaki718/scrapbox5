from functools import partial
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Depends

from .config import Config
from .model import Classifier
from .schema import Result


app = FastAPI()
config = Config.load(Path("api/config.yml"))


@app.get("/{value}", response_model=Result)
def predict(value: int, model: Optional[Classifier] = Depends(partial(Classifier.get_model, config))):
    if model is None:
        return Result(value=-1)
    result = model.predict(value)
    return Result(value=result)
