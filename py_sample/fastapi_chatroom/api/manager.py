from collections import defaultdict
from typing import Dict, List
from fastapi import WebSocket


class ConnectionManager:
    def __init__(self) -> None:
        self._connections: Dict[int, List[WebSocket]] = defaultdict(list)
    
    async def connect(self, websocket: WebSocket, room_id: int) -> None:
        await websocket.accept()
        self._connections[room_id].append(websocket)
    
    async def broadcast(self, message: str, room_id: int) -> None:
        for connection in self._connections[room_id]:
            await connection.send_text(message)
