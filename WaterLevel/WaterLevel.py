import numpy as np
class WaterLevel():
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.my_data = np.loadtxt(self.csv_file,dtype=str, delimiter=',',skiprows=0)
    def maxWaterAlphaLake(self):
        return self.my_data[self.my_data[:, 0] == 'ZO', :][0][2]
    def minWaterAlphaLake(self):
        return self.my_data[self.my_data[:, 0] == 'ZA', :][0][2]
    def bottomOutlet(self):
        return self.my_data[self.my_data[:, 0] == 'ZT', :][0][2]
    def annualStorageVolume(self,maxheight,minheight,pumpvolume):
        volume_maxheight = self.my_data[self.my_data[:, 0] == 'ZO', :][0][3]
        volume_minheight = self.my_data[self.my_data[:, 0] == 'ZA', :][0][3]
        return int(volume_maxheight) - int(volume_minheight) - int(pumpvolume)
