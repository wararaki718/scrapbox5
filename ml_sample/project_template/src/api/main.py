from fastapi import FastAPI


app = FastAPI()


@app.get("/ping")
def ping() -> str:
    return "pong"
