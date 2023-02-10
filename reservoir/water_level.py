"""

"""
import numpy as np


class WaterLevel:
    """
    Author: Navid
    """
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.my_data = np.loadtxt(self.csv_file, dtype=str, delimiter=',', skiprows=0)

    def max_water_alpha_lake(self):
        """

        :return:
        """
        return self.my_data[self.my_data[:, 0] == 'ZO', :][0][2]

    def min_water_alpha_lake(self):
        """

        :return:
        """
        return self.my_data[self.my_data[:, 0] == 'ZA', :][0][2]

    def bottom_outlet(self):
        """

        :return:
        """
        return self.my_data[self.my_data[:, 0] == 'ZT', :][0][2]

    # Why max_height and min_height is not used?
    def annual_storage_volume(self, max_height, min_height, pump_volume):
        """

        :param max_height:
        :param min_height:
        :param pump_volume:
        :return:
        """
        volume_max_height = self.my_data[self.my_data[:, 0] == 'ZO', :][0][3]
        volume_min_height = self.my_data[self.my_data[:, 0] == 'ZA', :][0][3]
        return int(volume_max_height) - int(volume_min_height) - int(pump_volume)
