from fastapi import WebSocket
from typing import List


class Manager:
	def __init__(self):
		self.connections: List[WebSocket] = []

	async def connect(self, web_socket: WebSocket):
		await web_socket.accept()
		self.connections.append(web_socket)

	async def disconnect_websocket(self, web_socket: WebSocket):
		self.connections.remove(web_socket)

	async def connections(self):
		return self.connections
