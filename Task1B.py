# Task 1B: sort stations by distance.

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1B"""

    # Set arguments for demonstrations
    p = (52.2053, 0.1218)
    stations = build_station_list()
    demonstration_1B = stations_by_distance(stations, p)

    # Print 10 closest stations
    print("The closest 10 stations are:{}".format(demonstration_1B[:10]))

    # Print 10 furthest stations
    print("The furthest 10 stations are:{}".format(demonstration_1B[-10:]))


if __name__ == "__main__":
    print("***Task1B Demonstration: Stations sorted by distance from Cambridge City Centre***")
    run()
