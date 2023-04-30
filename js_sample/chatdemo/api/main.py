from fastapi import FastAPI, WebSocket


app = FastAPI()

@app.get("/ping")
def ping() -> str:
    return "pong"

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"server receive: {data}")
