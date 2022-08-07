import pytest

# REVIEW: Use the conftest.py file to build the fixtures needed for running tests.
# This prevents the issue you noticed where you needed a test client and had to
# intialize in the test script itself.

# It would be a good idea to read up on fixtures as they are core to the usage of pytest.
# https://docs.pytest.org/en/6.2.x/fixture.html. Long story short these fixtures load
# into a particular scope when called by a test method.


@pytest.fixture(scope="module")
def test_client():
    pass


@pytest.fixture(scope="module")
def test_computer():
    # REVIEW: Any imports in tests should be done only in the context they are needed
    from server_stats.computer import Computer

    return Computer()
