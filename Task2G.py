# Task 2G: issuing flood warnings for towns

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation


def run():
    """Requirements for Task 2G"""
    # Assessment of risk of flooding
    # Severe when relative water level > 2.0
    # High when relative water level > 1.6 and <2.0
    # Moderate when relative water level > 1.2 and < 1.6
    # Low when relative water level > 0.8 and < 1.2

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Create empty sets for towns exposed to different risk of flood
    severe_towns = set()
    high_towns = set()
    moderate_towns = set()
    low_towns = set()

    # Apply function to find all stations with relative_water_level above determined threshold
    for station in stations:
        ratio = MonitoringStation.relative_water_level(station)
        if ratio is None:
            continue
        elif ratio > 2.0:
            if station.town is not None:
                severe_towns.add(station.town)
        elif ratio > 1.6:
            if station.town is not None:
                high_towns.add(station.town)
        elif ratio > 1.2:
            if station.town is not None:
                moderate_towns.add(station.town)
        elif ratio > 0.8:
            if station.town is not None:
                low_towns.add(station.town)

    # Print results
    print("Towns with severe risk of flooding are: {}".format(severe_towns))
    print("Towns with high risk of flooding are: {}".format(high_towns))
    print("Towns with moderate risk of flooding are: {}".format(moderate_towns))
    print("Towns with low risk of flooding are: {}".format(low_towns))


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
