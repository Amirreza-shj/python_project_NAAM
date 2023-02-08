import pandas as pd
import matplotlib.pyplot as plt


class PumpStorage:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        columns = ["hours", "volumes", "water_level"]
        df = pd.read_csv(self.csv_file,
                         names=columns,
                         header=0,
                         sep=",",
                         encoding="latin1")
        self.df_new = df  # df.mask((df["hours"] > 3) & (df["hours"] < 5))
        self.df_new['min'] = self.df_new.hours[(self.df_new.volumes.shift(1) >= self.df_new.volumes) & (
                    self.df_new.volumes.shift(-1) > self.df_new.volumes)]
        self.df_new['max'] = self.df_new.hours[(self.df_new.volumes.shift(1) <= self.df_new.volumes) & (
                    self.df_new.volumes.shift(-1) < self.df_new.volumes)]

    def min_volume(self):
        sorted_data = self.df_new.sort_values(["volumes"])
        min_volume = sorted_data["volumes"].min()
        return int(min_volume)

    def maxVolume(self):
        sorted_data = self.df_new.sort_values(["volumes"])
        max_volume = sorted_data["volumes"].max()
        return int(max_volume)

    def plotVolume(self):
        ax = plt.gca()
        self.df_new.plot(x="hours", y="volumes")
        plt.show()

    def findPeaks(self):
        if self.df_new["max"][self.df_new["max"].notnull()].iloc[0] < \
                self.df_new["min"][self.df_new["min"].notnull()].iloc[0]:
            for i in range(self.df_new['max'].count()):
                if i == range(self.df_new['max'].count())[-1] and self.df_new["min"][self.df_new["min"].notnull()].iloc[-1] > self.df_new["max"][self.df_new["max"].notnull()].iloc[-1]:
                    print(
                        f'time of pumping: {self.df_new["min"][self.df_new["min"].notnull()].iloc[-1]} untill {self.df_new["hours"].iloc[-1]}')
                else:
                    print(
                        f'time of pumping: {self.df_new["min"][self.df_new["min"].notnull()].iloc[i]} untill {self.df_new["max"][self.df_new["max"].notnull()].iloc[i + 1]}')
            for i in range(self.df_new['min'].count()):
                print(
                    f'time of turbining: {self.df_new["max"][self.df_new["max"].notnull()].iloc[i]} untill {self.df_new["min"][self.df_new["min"].notnull()].iloc[i]}')
                if i == range(self.df_new['min'].count())[-1] and self.df_new["max"][self.df_new["max"].notnull()].iloc[
                    -1] > self.df_new["min"][self.df_new["min"].notnull()].iloc[i]:
                    print(
                        f'time of turbining: {self.df_new["max"][self.df_new["max"].notnull()].iloc[-1]} untill {self.df_new["hours"].iloc[-1]}')
        else:
            for i in range(self.df_new['max'].count()):
                if i == range(self.df_new['max'].count())[-1] and self.df_new["min"][self.df_new["min"].notnull()].iloc[-1] > self.df_new["max"][self.df_new["max"].notnull()].iloc[-1]:
                    print(f'time of pumping: {self.df_new["min"][self.df_new["min"].notnull()].iloc[-1]} untill {self.df_new["hours"].iloc[-1]}')
                else:
                    print(f'time of pumping: {self.df_new["min"][self.df_new["min"].notnull()].iloc[i]} untill {self.df_new["max"][self.df_new["max"].notnull()].iloc[i]}')
            for i in range(self.df_new['min'].count()):
                print(f'time of turbining: {self.df_new["max"][self.df_new["max"].notnull()].iloc[i]} untill {self.df_new["min"][self.df_new["min"].notnull()].iloc[i]}')
                if i == range(self.df_new['min'].count())[-1] and self.df_new["max"][self.df_new["max"].notnull()].iloc[-1] > self.df_new["min"][self.df_new["min"].notnull()].iloc[i]:
                    print(f'time of turbining: {self.df_new["max"][self.df_new["max"].notnull()].iloc[-1]} untill {self.df_new["hours"].iloc[-1]}')
