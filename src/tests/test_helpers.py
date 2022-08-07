def test_generate_id():
    from server_stats.helpers import generate_id

    """
    Assertion 1: Test to ensure generate_id() actually returns unique ID's
    """
    assert generate_id() != generate_id()
