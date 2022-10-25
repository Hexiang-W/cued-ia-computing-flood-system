# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data
"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        range = self.typical_range
        if range is None:
            return False
        elif range[1] > range[0]:
            return True
        else:
            return False

    def relative_water_level(self):
        latest_level = self.latest_level
        range = self.typical_range

        if range is None:
            return None

        elif range[1] < range[0]:
            return None

        elif latest_level is None:
            return None

        elif latest_level < range[0]:
            relative_water_ratio = 0.0 - (range[0] - latest_level) / (range[1] - range[0])
            return relative_water_ratio

        elif range[0] < latest_level < range[1]:
            relative_water_ratio = 0.0 + (latest_level - range[0]) / (range[1] - range[0])
            return relative_water_ratio

        elif latest_level > range[1]:
            relative_water_ratio = 1.0 + (latest_level - range[1]) / (range[1] - range[0])
            return relative_water_ratio


def inconsistent_typical_range_stations(stations):
    """Returns a list of all stations with inconsistent typical low/high range"""

    # Build an empty list for inconsistent station(s)
    inconsistent_stations = []

    # Check consistency of each station and append inconsistent station(s) to the list
    for station in stations:
        consistency = MonitoringStation.typical_range_consistent(station)
        if consistency is False:
            inconsistent_stations.append(station.name)

    # Sort the list of inconsistent station(s) and return the list
    sorted_inconsistent_stations = sorted(inconsistent_stations)
    return sorted_inconsistent_stations
