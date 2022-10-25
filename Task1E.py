# Task1E: rivers by number of stations

from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1E"""

    # Set arguments for demonstrations
    N = 9
    stations = build_station_list()
    demonstration_1E = rivers_by_station_number(stations, N)

    # Print top 9 rivers with greatest number of stations
    print("The top 9 rivers with greatest number of stations are:{}".format(demonstration_1E))


if __name__ == "__main__":
    print("***Task1D Demonstration: Rivers with at least one monitoring station***")
    run()
