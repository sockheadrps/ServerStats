import psutil

# This is just a helper class to poll data from the hardware. The functions are just to help build the class, and the class is intended to
# only be used in main.py

def get_cpu_count():
    return psutil.cpu_count(logical=False)


def get_cpu_usage():
    return psutil.cpu_percent(interval=1, percpu=False)


def get_cpu_frequency():
    current = psutil.cpu_freq()[0]
    max_frequency = psutil.cpu_freq()[2]
    cpu_freq_dict = {
        "current_frequency": current / 1000,
        "max_frequency": max_frequency
    }
    return cpu_freq_dict


def get_total_ram():
    mem = psutil.virtual_memory()
    return round((mem.total / 1073741824), 2)


def get_available_ram():
    mem = psutil.virtual_memory()
    return round((mem.available / 1073741824), 2)


def get_percentage_used_ram():
    mem = psutil.virtual_memory()
    return round(mem.percent, 2)


def get_total_disk_space():
    disk = psutil.disk_usage('/')
    return round((disk.total / 1073741824), 2)


def get_total_disk_free():
    disk = psutil.disk_usage('/')
    return round((disk.free / 1073741824), 2)


def get_total_disk_used():
    disk = psutil.disk_usage('/')
    return round((disk.total - disk.free) / 1073741824, 2)


def get_disk_percentage_used():
    disk = psutil.disk_usage('/')
    return disk.percent


def get_temperatures():
    try:
        core_temp_list = psutil.sensors_temperatures(fahrenheit=True)['coretemp']
        core_temp_dict = {}
        for core in core_temp_list:
            core_temp_dict[core.label] = core.current
        return core_temp_dict
    except AttributeError:
        core_temp_dict = {}
        return core_temp_dict


class Computer:
    """
    This class is used to easily evaluate the status of the computer. It returns a dictionary with the results
    of querying the status os the available computer components via psutils
    """

    @staticmethod
    def get_stats_dict() -> dict:
        stats_dict = {
            "cpu_count": get_cpu_count(),
            "cpu_usage": get_cpu_usage(),
            "cpu_frequency": get_cpu_frequency(),
            "core_temperatures": get_temperatures(),
            "ram_total": get_total_ram(),
            "ram_available": get_available_ram(),
            "ram_percentage": get_percentage_used_ram(),
            "disk_total": get_total_disk_space(),
            "disk_free": get_total_disk_free(),
            "disk_used": get_total_disk_used(),
            "disk_percentage": get_disk_percentage_used()

        }
        return stats_dict
