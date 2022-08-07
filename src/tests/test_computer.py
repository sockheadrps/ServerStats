import pytest


def test_get_cpu_count(test_computer):
    """
    Assertion 1: Function returns an int
    Assertion 2: Function returns a valid number of cores.
    """
    # REVIEW: is instance and boolean expressions already return a boolean, no
    # need to check "is True"
    assert isinstance(test_computer.cpu_count, int)
    assert test_computer.cpu_count > 0


def test_get_cpu_usage(test_computer):
    """
    Assertion 1: Function returns a float
    """
    assert isinstance(test_computer.cpu_percent, float)


def test_get_cpu_frequency(test_computer):
    """
    Loop Assertions: Checks the key is a string and the value is a float
    Assertion 2: Function returns a dict
    """
    cpu_frequency_dict = test_computer.cpu_frequency
    for item in cpu_frequency_dict.keys():
        assert isinstance(item, str)
        assert isinstance(cpu_frequency_dict[item], float)


# REVIEW: marking this as fail for now since I'm running windows
@pytest.mark.xfail
def test_get_core_temperatures(test_computer):
    import os

    """
    Assertion 1: Function returns a dict
    """
    assert os.name != "nt", "Temperature sensor with psutil only works with linux"
    assert isinstance(test_computer.temperatures, dict)


def test_get_ram_totals(test_computer):
    """
    Assertion 1: Function returns a float
    """
    assert isinstance(test_computer.total_ram, float)


def test_get_ram_available(test_computer):
    """
    Assertion 1: Function returns a float
    """
    assert isinstance(test_computer.available_ram, float)


def test_get_ram_percent(test_computer):
    """
    Assertion 1: Function returns a float
    """
    assert isinstance(test_computer.percentage_used_ram, float)


def test_get_disk_total(test_computer):
    """
    Assertion 1: Function returns a flaat
    """
    assert isinstance(test_computer.total_disk_space, float)


def test_get_disk_free(test_computer):
    """
    Assertion 1: Function returns a float
    """
    assert isinstance(test_computer.total_disk_free, float)


def test_get_disk_used(test_computer):
    """
    Assertion 1: Function returns a float
    """
    assert isinstance(test_computer.total_disk_used, float)


def test_get_disk_percentage_used(test_computer):
    """
    Assertion 1: Function returns a float
    """
    assert isinstance(test_computer.disk_percentage_used, float)


def test_computer_class(test_computer):
    """
    No need to test the actual data inside the returned dictionary, all of that data has been validated through
    the function tests preceding this test.
    Assertion 1: Class method returns a dictionary
    """
    assert isinstance(test_computer.get_stats_dict(), dict)
