from PumpStorage import PumpStorage
from WaterLevel import WaterLevel
ps_obj=PumpStorage.PumpStorage(csv_file="PumpStorage/volume and stage hydrograph of pool Beta.csv")
wl_obj=WaterLevel.WaterLevel(csv_file="WaterLevel/water_level_info.csv")
print(f"volume of pool Beta is: {ps_obj.maxVolume()-ps_obj.minVolume()}")
ps_obj.plotVolume()
ps_obj.findPeaks()
print(f"pump storage volume in lake is {ps_obj.maxVolume()-ps_obj.minVolume()}")
print(f"maximum operational water level in reservoir is {wl_obj.maxWaterAlphaLake()}")
print(f"bottom outlet is located at {wl_obj.bottomOutlet()}")
print(f"annual storage volume of reservoir is volume of reservoir without dead volume and pump storage so in this case ---> {wl_obj.annualStorageVolume(maxheight=wl_obj.maxWaterAlphaLake(),minheight=wl_obj.minWaterAlphaLake(),pumpvolume=ps_obj.maxVolume()-ps_obj.minVolume())}")