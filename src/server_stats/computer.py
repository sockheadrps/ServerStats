from typing import Dict

import psutil

from .constants import BYTES_IN_GB

"""
These helper functions are not intended to be called in any other place other than the provided class. 
The functions themselves arent even really necessary, but I thought it looked cleaner to do the data conversion
in some functions rather than inline in the class itself, and just decided to write functions for each
class variable.
"""

# REVIEW: These methods were purely in service of the Computer class so they belong within the class. You hitting this ambiguity is understandable
# as other languages use private vs public methods/properties to distinguish between functionality that is exposed externally versus
# functionality that is not. Since python does not use this people can be tempted to keep functions outside of the class in some cases but
# usually they should be kept within the class.
class Computer:
    """
    This class is used to easily evaluate the status of the computer. It returns a dictionary with the results
    of querying the status os the available computer components via psutils
    """

    def get_stats_dict(self) -> dict:
        stats_dict = {
            "cpu_count": self.cpu_count,
            "cpu_usage": self.cpu_percent,
            "cpu_frequency": self.cpu_frequency,
            "core_temperatures": self.temperatures,
            "ram_total": self.total_ram,
            "ram_available": self.available_ram,
            "ram_percentage": self.percentage_used_ram,
            "disk_total": self.total_disk_space,
            "disk_free": self.total_disk_free,
            "disk_used": self.total_disk_used,
            "disk_percentage": self.disk_percentage_used,
        }
        return stats_dict

    # REVIEW: since you only need a "getter" method it makes more sense to use a property instead of a method
    @property
    def cpu_count(self) -> int:
        return psutil.cpu_count(logical=False)

    @property
    def cpu_percent(self) -> float:
        return psutil.cpu_percent(interval=1, percpu=False)

    @property
    def cpu_frequency(self) -> Dict[str, float]:
        current = psutil.cpu_freq()[0]
        max_frequency = float(psutil.cpu_freq()[2])
        cpu_freq_dict = {
            "current_frequency": current / 1000,
            "max_frequency": max_frequency,
        }
        return cpu_freq_dict

    @property
    def total_ram(self) -> float:
        mem = psutil.virtual_memory()
        # REVIEW: conversions should be preserved as a constant
        return round((mem.total / BYTES_IN_GB), 2)

    @property
    def available_ram(self) -> float:
        mem = psutil.virtual_memory()
        return round((mem.available / BYTES_IN_GB), 2)

    @property
    def percentage_used_ram(self) -> float:
        mem = psutil.virtual_memory()
        return round(mem.percent, 2)

    @property
    def total_disk_space(self) -> float:
        disk = psutil.disk_usage("/")
        return round((disk.total / BYTES_IN_GB), 2)

    @property
    def total_disk_free(self) -> float:
        disk = psutil.disk_usage("/")
        return round((disk.free / BYTES_IN_GB), 2)

    @property
    def total_disk_used(self) -> float:
        disk = psutil.disk_usage("/")
        return round((disk.total - disk.free) / BYTES_IN_GB, 2)

    @property
    def disk_percentage_used(self) -> float:
        disk = psutil.disk_usage("/")
        return disk.percent

    @property
    def temperatures(self) -> dict:
        # Core temperature only available on linux machine
        """
        Get core temperature(s)
        :return: Dict of core temperatures if running on Linux. If other OS, returns and empty dictionary.
        """
        try:
            core_temp_list = psutil.sensors_temperatures(fahrenheit=True)["coretemp"]
            core_temp_dict = {}
            for core in core_temp_list:
                core_temp_dict[core.label] = core.current
            return core_temp_dict
        except AttributeError:
            core_temp_dict = {}
            return core_temp_dict
