import pytest


from fastapi.testclient import TestClient
from fastapi import WebSocket, WebSocketDisconnect

from server_stats.__main__ import app

from server_stats.connection_manager import ConnectionManager

"""
This feels like a hacky-way to test this context manager, but I cant think of any other way to do it. The test will
fail if for any reason an uncaught exception is raised in the TestClient endpoint in this test(stats_websocket)
"""

# TODO: a lot of this should be in conftest.py
client = TestClient(app, backend_options={"use_uvloop": True})
connection_manager = ConnectionManager()


@app.websocket("/ws/test/stats")
async def stats_websocket(client_websocket: WebSocket):
    try:
        await connection_manager.connect(client_websocket)
        await client_websocket.send_json({"event": "connected"})
        data = await client_websocket.receive_json()
        if data["event"] == "disconnect":
            await client_websocket.send_json({"event": "disconnected"})
            await connection_manager.disconnect_websocket(client_websocket)
    except WebSocketDisconnect:
        print("Disconnected")
        pass


@pytest.mark.asyncio
async def test_websocket():
    with client.websocket_connect("/ws/test/stats") as websocket:
        connection = websocket.receive_json()
        assert connection["event"] == "connected"
        websocket.send_json({"event": "disconnect"})
        disconnection = websocket.receive_json()
        assert disconnection["event"] == "disconnected"
