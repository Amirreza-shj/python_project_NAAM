from reservoir.pump_storage import PumpStorage
from reservoir.water_level import WaterLevel
from config import CSV_PATH


if __name__ == '__main__':
    ps_obj = PumpStorage(csv_file=CSV_PATH['reservoir'])
    wl_obj = WaterLevel(csv_file=CSV_PATH['water_level'])
    print(f"volume of pool Beta is: {ps_obj.maxVolume() - ps_obj.min_volume()}")
    ps_obj.plotVolume()
    ps_obj.findPeaks()
    print(f"pump storage volume in lake is {ps_obj.maxVolume() - ps_obj.min_volume()}")
    print(f"maximum operational water level in reservoir is {wl_obj.maxWaterAlphaLake()}")
    print(f"bottom outlet is located at {wl_obj.bottomOutlet()}")
    print(
        f"annual storage volume of reservoir is volume of reservoir without dead volume and pump storage so in this case ---> {wl_obj.annualStorageVolume(maxheight=wl_obj.maxWaterAlphaLake(), minheight=wl_obj.minWaterAlphaLake(), pumpvolume=ps_obj.maxVolume() - ps_obj.min_volume())}")
