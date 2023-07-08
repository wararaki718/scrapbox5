import requests
from fastapi import FastAPI


app = FastAPI()


@app.get("/ping")
def ping() -> str:
    return "ping"

@app.get("/back")
def back() -> str:
    response = requests.get("http://localhost:3000")
    return f"{response.text} via front\n"
