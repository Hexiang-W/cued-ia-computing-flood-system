"""This module provides functionality for sorting stations according to relative water level"""

from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """Returns all stations within a given list of stations which has a relative_water_level of over the set tol"""

    # Create an empty list
    stations_threshold = []

    # Add each station with relative_water_level above tol into the list
    for station in stations:
        ratio = MonitoringStation.relative_water_level(station)
        if ratio is None:
            continue
        elif ratio > tol:
            stations_threshold.append((station.name, ratio))

    # Sort the list of tuples
    sorted_stations_over_threshold = sorted_by_key(stations_threshold, 1, True)

    return sorted_stations_over_threshold


def stations_highest_rel_level(stations, N):
    """Returns N stations where the water level, relative to typical range, is the highest in decending order"""

    # Create an empty list
    risky_stations = []

    # loop each station with highest relative water level
    for station in stations:
        ratio = MonitoringStation.relative_water_level(station)
        if ratio is None:
            continue
        risky_stations.append((station.name, ratio))

    # Sort the list of tuples
    sorted_risky_stations = sorted_by_key(risky_stations, 1, True)

    # Create an list of N most risky stations
    most_risky_stations = sorted_risky_stations[:N]

    return most_risky_stations
