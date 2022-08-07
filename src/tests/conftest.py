import pytest


@pytest.fixture(scope="module")
def test_client():
    from fastapi.testclient import TestClient
    from server_stats import app
    return TestClient(app)