from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles

from .manager import ConnectionManager

manager = ConnectionManager()

app = FastAPI()

app.mount("/chat", StaticFiles(directory="static/chat", html=True), name="chat")

@app.get("/ping")
def ping() -> str:
    return "pong"

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: int):
    await manager.connect(websocket, room_id)
    while True:
        text = await websocket.receive_text()
        await manager.broadcast(text, room_id)
