# Task2B: assess flood risk by level

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Apply function to find all stations with relative_water_level above 0.8
    stations_with_higher_tol = stations_level_over_threshold(stations, 0.8)

    # Print each tuple in new lines
    for i in range(len(stations_with_higher_tol)):
        print(stations_with_higher_tol[i][0], stations_with_higher_tol[i][1])


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
