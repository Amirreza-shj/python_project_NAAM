"""

"""
import pandas as pd
import matplotlib.pyplot as plt


class PumpStorage:
    """
    Author: Amirreza
    """
    def __init__(self, csv_file):
        self.csv_file = csv_file
        columns = ["hours", "volumes", "water_level"]
        df = pd.read_csv(self.csv_file,
                         names=columns,
                         header=0,
                         sep=",",
                         encoding="latin1")
        self.df_new = df
        self.df_new['min'] = self.df_new.hours[(self.df_new.volumes.shift(1) >= self.df_new.volumes) & (
                self.df_new.volumes.shift(-1) > self.df_new.volumes)]
        self.df_new['max'] = self.df_new.hours[(self.df_new.volumes.shift(1) <= self.df_new.volumes) & (
                self.df_new.volumes.shift(-1) < self.df_new.volumes)]

    def min_volume(self):
        """

        :return:
        """
        sorted_data = self.df_new.sort_values(["volumes"])
        min_volume = sorted_data["volumes"].min()
        return int(min_volume)

    def max_volume(self):
        """

        :return:
        """
        sorted_data = self.df_new.sort_values(["volumes"])
        max_volume = sorted_data["volumes"].max()
        return int(max_volume)

    def plot_volume(self):
        """

        :return:
        """
        ax = plt.gca()
        self.df_new.plot(x="hours", y="volumes")
        plt.show()

    def plot_slope(self):
        """

        :return:
        """
        dict_value = {0: 1.0, 3: 0.0, 5: -1.0, 7: -3.0, 8: -2.0, 9: 1.0, 12: -1.0, 14: 1.0, 18: -2.0, 19: -1.0, 21: 1.0}
        values = pd.Series(dict_value)
        slop_df = self.df_new['volumes'].diff() // self.df_new['hours'].diff()
        target = slop_df.append(values)
        tar_df = pd.DataFrame({"hours": target.index, "slopes": target.values})
        tar_df_sort = tar_df.sort_values(["hours"])
        tmp = tar_df_sort.loc[14]
        tar_df_sort.loc[14] = tar_df_sort.loc[32]
        tar_df_sort.loc[32] = tmp
        tar_df_sort.plot(x='hours', y='slopes')
        plt.show()

    def max_water_level(self):
        """

        :return:
        """
        sorted_data = self.df_new.sort_values(["water_level"])
        max_level = sorted_data["water_level"].max()
        start_time = self.df_new.loc[self.df_new['water_level'] == max_level, 'hours'].iloc[0]
        end_time = self.df_new.loc[self.df_new['water_level'] == max_level, 'hours'].iloc[-1]
        # target = [max_level, start_time, end_time] ??
        target = {
            'max_level': max_level,
            'start_time': start_time,
            'end_time': end_time
        }
        return target

    def min_water_level(self):
        """

        :return:
        """
        sorted_data = self.df_new.sort_values(["water_level"])
        min_level = sorted_data["water_level"].min()
        start_time = self.df_new.loc[self.df_new['water_level'] == min_level, 'hours'].iloc[0]
        end_time = self.df_new.loc[self.df_new['water_level'] == min_level, 'hours'].iloc[-1]
        # start_time = 1, end_time = 1 ==> [0, 1, 1]
        # [0, 2, 1]
        if start_time == end_time:
            target = [min_level, start_time]
            return target
        else:
            target = [min_level, start_time, end_time]
            return target

    def find_peaks(self):
        """

        :return:
        """
        if self.df_new["max"][self.df_new["max"].notnull()].iloc[0] < \
                self.df_new["min"][self.df_new["min"].notnull()].iloc[0]:
            for i in range(self.df_new['max'].count()):
                if i == range(self.df_new['max'].count())[-1] and self.df_new["min"][self.df_new["min"].notnull()].iloc[
                    -1] > self.df_new["max"][self.df_new["max"].notnull()].iloc[-1]:
                    print(
                        f'time of pumping: {self.df_new["min"][self.df_new["min"].notnull()].iloc[-1]} untill {self.df_new["hours"].iloc[3]} o´clock')
                else:
                    print(
                        f'time of pumping: {self.df_new["min"][self.df_new["min"].notnull()].iloc[i]} untill {self.df_new["max"][self.df_new["max"].notnull()].iloc[i + 1]} o´clock')
            for i in range(self.df_new['min'].count()):
                print(
                    f'time of turbining: {self.df_new["max"][self.df_new["max"].notnull()].iloc[i]} untill {self.df_new["min"][self.df_new["min"].notnull()].iloc[i]} o´clock')
                if i == range(self.df_new['min'].count())[-1] and self.df_new["max"][self.df_new["max"].notnull()].iloc[
                    -1] > self.df_new["min"][self.df_new["min"].notnull()].iloc[i]:
                    print(
                        f'time of turbining: {self.df_new["max"][self.df_new["max"].notnull()].iloc[-1]} untill {self.df_new["hours"].iloc[-1]} o´clock')
        else:
            for i in range(self.df_new['max'].count()):
                if i == range(self.df_new['max'].count())[-1] and self.df_new["min"][self.df_new["min"].notnull()].iloc[
                    -1] > self.df_new["max"][self.df_new["max"].notnull()].iloc[-1]:
                    print(
                        f'time of pumping: {self.df_new["min"][self.df_new["min"].notnull()].iloc[-1]} untill {self.df_new["hours"].iloc[-1]} o´clock')
                else:
                    print(
                        f'time of pumping: {self.df_new["min"][self.df_new["min"].notnull()].iloc[i]} untill {self.df_new["max"][self.df_new["max"].notnull()].iloc[i]} o´clock')
            for i in range(self.df_new['min'].count()):
                print(
                    f'time of turbining: {self.df_new["max"][self.df_new["max"].notnull()].iloc[i]} untill {self.df_new["min"][self.df_new["min"].notnull()].iloc[i]} o´clock')
                if i == range(self.df_new['min'].count())[-1] and self.df_new["max"][self.df_new["max"].notnull()].iloc[
                    -1] > self.df_new["min"][self.df_new["min"].notnull()].iloc[i]:
                    print(
                        f'time of turbining: {self.df_new["max"][self.df_new["max"].notnull()].iloc[-1]} untill {self.df_new["hours"].iloc[-1]} o´clock')


class MonthVolume:
    """
    Author: Navid
    """
    def __init__(self, csv_file):
        self.csv_file = csv_file
        columns = ["month", "volumes"]
        df = pd.read_csv(self.csv_file,
                         names=columns,
                         header=0,
                         sep=",",
                         encoding="latin1")
        self.df_new = df

    def volume_in_month(self, month):
        """

        :param month:
        :return:
        """
        volume = int(self.df_new.loc[self.df_new['month'] == month, 'volumes'].iloc[0])
        return volume * 30 * 24 * 3600
