# Task1D: rivers with a station(s)

from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""

    # Set up demonstrations
    stations = build_station_list()
    demonstration_1D_part_one = rivers_with_station(stations)
    demonstration_1D_part_two = stations_by_river(stations)

    # Print the first 10 rivers in alphabetical order
    print("The first 10 rivers in alphabetical order are:{}".format(demonstration_1D_part_one[:10]))

    # Print all stations for River Aire, River Cam and River Thames
    # Check existence of key in demonstration_1D_part_two dictionary
    print("River Aire" in demonstration_1D_part_two)
    print("River Cam" in demonstration_1D_part_two)
    print("River Thames" in demonstration_1D_part_two)

    # Add stations into lists
    river_aire = demonstration_1D_part_two["River Aire"]
    river_cam = demonstration_1D_part_two["River Cam"]
    river_thames = demonstration_1D_part_two["River Thames"]

    # Print rivers and their corresponding stations
    print("The monitoring stations on River Aire are: {}".format(river_aire))
    print("The monitoring stations on River Cam are: {}".format(river_cam))
    print("The monitoring stations on River Thames are: {}".format(river_thames))


if __name__ == "__main__":
    print("***Task1D Demonstration: Rivers with at least one monitoring station***")
    run()
