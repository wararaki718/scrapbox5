from functools import partial
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Depends

from .config import Config
from .model import Classifier
from .schema import Result


app = FastAPI()
config = Config.load(Path("api/config.yml"))
get_model = partial(Classifier.get_model, config)

@app.get("/{value}", response_model=Result)
def predict(value: int, model: Optional[Classifier] = Depends(get_model)):
    if model is None:
        return Result(value=-1)
    print(value)
    result = model.predict(value)
    print(model._threshold)
    print(app.dependency_overrides.keys())
    return Result(value=result)
