# Task1F: typical low/high range consistency

from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1F"""

    # Set up demonstrations
    stations = build_station_list()
    demonstration_1F = inconsistent_typical_range_stations(stations)

    # Print all the stations with inconsistent typical low/high range
    print("The stations with inconsistent typical low/high range are:{}".format(demonstration_1F))


if __name__ == "__main__":
    print("***Task1F Demonstration: Stations with inconsistent typical low/high range***")
    run()
