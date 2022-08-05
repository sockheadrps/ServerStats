from fastapi.testclient import TestClient
from main import app, generate_id
from httpx import AsyncClient
import pytest


client = TestClient(app, backend_options={"use_uvloop": True})


@pytest.mark.anyio
async def test_html_client():
    """
    Assertion 1: Tests the successful delivery of the /stats endpoint
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/stats")
    assert response.status_code == 200


def test_generate_id():
    """
    Assertion 1: Test to ensure generate_id() actually returns unique ID's
    """
    assert generate_id() != generate_id()


def test_websocket():
    """
    There is no need to test for stats data validity here, data is validated in the test_stats.
    Assertion 1: Ensures initial websocket connection event
    Assertion 2: Ensures the delivery of the expected datatype from DATAREQUEST
    """
    ws_client = TestClient(app)
    with ws_client.websocket_connect("/ws/stats") as websocket:
        # Initial WS connection
        data = websocket.receive_json()
        print(f"client {data}")
        assert data == {"event": "CONNECT"}
        # Stats request
        websocket.send_json({"event": "DATAREQUEST"})
        data = websocket.receive_json()
        print(f"client {data}")
        assert isinstance(data, dict)
