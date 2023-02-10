"""

"""
from reservoir.pump_storage import PumpStorage, MonthVolume
from reservoir.water_level import WaterLevel
from config import CSV_PATH, CONSTANT

if __name__ == '__main__':
    # Write some info
    pump_storage = PumpStorage(CSV_PATH['reservoir'])
    water_level = WaterLevel(CSV_PATH['water_level'])
    month_volume = MonthVolume(CSV_PATH['inflow_alpha_creek'])

    # Write some info
    pump_volume = pump_storage.max_volume() - pump_storage.min_volume()
    print(f"*** Solution 1 ***\nvolume of pool Beta is: {pump_volume} Mio.m³")

    # Write some info
    print(f"\n*** Solution 2 ***\ntime of pumping and turbining in UHPP & plot volumes")
    pump_storage.plot_volume()
    pump_storage.find_peaks()

    # Write some info
    print(f"\n*** Solution 3 ***\ninflow/outflow of Pool Beta")
    pump_storage.plot_slope()

    # Write some info
    pump_storage_volume_lake = pump_volume
    print(f"\n*** Solution 4 ***\npump storage volume in lake is {pump_storage_volume_lake} Mio.m³")

    # Write some info
    max_height = water_level.max_water_alpha_lake()
    print(f"\n*** Solution 5 ***\nmaximum operational water level in reservoir is {max_height} m.a.s.l")

    # Write some info
    water_level_outlet = water_level.bottom_outlet()
    print(f"\n*** Solution 6 ***\nbottom outlet is located at {water_level_outlet} m.a.s.l")

    # Write some info
    msg_annual_storage_volume = 'annual storage volume of reservoir is volume of reservoir without ' \
                                'dead volume and pump storage: '
    min_height = water_level.min_water_alpha_lake()
    volume_annual_alpha = water_level.annual_storage_volume(max_height, min_height, pump_volume)
    print(f"\n*** Solution 7 ***\n{msg_annual_storage_volume} {volume_annual_alpha} Mio.m³")

    # Write some info
    msg_uhpp_electricity_power_plant = 'Maximum Fall Head for UHPP happens when Upper Reservoir in its maximum ' \
                                       'level AND Lake Alpha in its minimum level. This happens at the end of August'
    start_time_max = pump_storage.max_water_level()['start_time']
    end_time_max = pump_storage.max_water_level()['end_time']
    print(f"\n*** Solution 8 ***\n{msg_uhpp_electricity_power_plant}, {start_time_max} - {end_time_max} o`clock")

    # Write some info
    msg_delta_h = 'Delta h:'
    max_level = float(pump_storage.max_water_level()['max_level'])
    print(f"{msg_delta_h} {max_level - int(min_height)} m")

    # Write some info
    msg_max_height_upper_alpha = 'Minimum Fall Head for UHPP happens when Upper Reservoir in its minimum level AND ' \
                                 'Lake Alpha in its maximum level. This happens at the end of April,'
    end_time_min = pump_storage.min_water_level()[-1]
    print(f"{msg_max_height_upper_alpha} {end_time_min} o´clock")

    # Write some info
    min_level = float(pump_storage.min_water_level()[0])
    print(f"{msg_delta_h} {min_level - int(max_height)} m")

    # Write some info
    inflow_volume_alpha_lack_may_till_aug = round(
        (month_volume.volume_in_month('May') +
         month_volume.volume_in_month('Jun') +
         month_volume.volume_in_month('Jul') +
         month_volume.volume_in_month('Aug')
         ) / 1000000, 1
    )
    outflow_volume_alpha_lack_may_till_aug = inflow_volume_alpha_lack_may_till_aug + volume_annual_alpha
    q_out_alpha_may_aug = round((outflow_volume_alpha_lack_may_till_aug / (4 * 30 * 24 * 3600) * 1000000), 1)
    q_lhpp_electricity_power_plant = round(q_out_alpha_may_aug - (CONSTANT['flow_in_tropical_creek'] / 1000), 1)
    msg_lhpp_electricity_power_plant = 'Between the start of May and the end of August, Lake Alpha Volume goes from ' \
                                       'Maximum Operational Volume to Minimum Operational Volume,And since there ' \
                                       'are 2 outflow (to LHPP and to Alphabeta Creek), we can say turbine discharge ' \
                                       'in the LHPP has'
    print(f"\n*** Solution 9 ***\n{msg_lhpp_electricity_power_plant} {q_lhpp_electricity_power_plant} m³/s")
