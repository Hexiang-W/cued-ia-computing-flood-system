# Task1C: stations within radius

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1C"""

    # Set arguments for demonstrations
    stations = build_station_list()
    cambridge_centre = (52.2053, 0.1218)
    radius = 10
    demonstration_1C = stations_within_radius(stations, cambridge_centre, radius)

    # Print stations within 10km radius of Cambridge City Centre
    print(demonstration_1C)


if __name__ == "__main__":
    print("***Task1C Demonstration: Stations within 10km radius of Cambridge City Centre***")
    run()
