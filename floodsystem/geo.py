# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

"""This module contains a collection of functions related to
geographical data.
"""

from haversine import haversine
from floodsystem.utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    """Sort the stations by distances from certain location"""

    # Build an empty list of distances from p
    stations_distances = []

    for station in stations:
        distance = haversine(station.coord, p)
        # now just append the tuple into the empty list
        tuple = (station.name, station.town, distance)
        stations_distances.append(tuple)

    # Now we perform sorting
    stations_distances = sorted_by_key(stations_distances, 2)

    return stations_distances


def stations_within_radius(stations, centre, r):
    """Returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x"""

    # Build an empty list of stations within radius r of x
    stations_within_r = []

    for station in stations:
        # Find distance between station and centre
        distance = haversine(station.coord, centre)

        # Append name of station to list if distance is less than r
        if distance < r:
            stations_within_r.append(station.name)

    return stations_within_r


def rivers_with_station(stations):
    """Returns a set of rivers with at least one station"""

    # Build an empty set of river names
    rivers = set()

    # Add each new river to the set
    for station in stations:
        rivers.add(station.river)

    sorted_rivers = sorted(rivers)
    no_of_rivers = len(sorted_rivers)
    print("Number of rivers: {}".format(no_of_rivers))
    return(sorted_rivers)


def stations_by_river(stations):
    """Returns all stations on each river"""

    # Build an empty list of stations on a river
    stations_on_river = []

    # Build an empty dictionary for rivers and their monitoring stations
    stations_and_river = {}

    # Append stations into empty list and add corresponding river(key) and station(value) into dictionary
    for station in stations:
        stations_on_river.append(station.name)
        add_values_in_dict(stations_and_river, station.river, stations_on_river)
        stations_on_river = []

    return stations_and_river


# Append multiple value to a key in dictionary
def add_values_in_dict(sample_dict, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""

    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


def rivers_by_station_number(stations, N):
    """Return a list of tuples consist of N rivers with greatest no. of stations"""

    # Build an empty dict consisting of river names and no. of stations
    river_station_dict = {}

    # Add the key and value into the dict
    for station in stations:
        river_name = station.river
        if river_name in river_station_dict:
            river_station_dict[river_name] += 1
        else:
            river_station_dict[river_name] = 1

    # Convert dict data form to tuple
    river_station_num_tuples = []
    for river_name in river_station_dict:
        k = (river_name, river_station_dict[river_name])
        river_station_num_tuples.append(k)

    # Now sort the date by no. of stations on the river
    river_station_num_tuples.sort(key=lambda x: x[1], reverse=True)

    result = river_station_num_tuples[:N]

    # Check if there are rivers with same number of stations
    while river_station_num_tuples[N][1] == river_station_num_tuples[N - 1][1]:
        result.append(river_station_num_tuples[N])
        N += 1

    return result
