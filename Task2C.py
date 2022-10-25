# Task2C: most at risk stations

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Returns 10 stations where the water level, relative to typical range
    most_risky_stations = stations_highest_rel_level(stations, 10)

    # Print each tuple in new lines
    for i in range(len(most_risky_stations)):
        print(most_risky_stations[i][0], most_risky_stations[i][1])


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
