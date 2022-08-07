from fastapi import WebSocket
from typing import List, NoReturn


# REVIEW: classes should be capitalized and named the same as the file
class ConnectionManager:
    def __init__(self):
        self.connections: List[WebSocket] = []

    async def connect(self, web_socket: WebSocket) -> NoReturn:
        await web_socket.accept()
        self.connections.append(web_socket)

    async def disconnect_websocket(self, web_socket: WebSocket) -> NoReturn:
        self.connections.remove(web_socket)
