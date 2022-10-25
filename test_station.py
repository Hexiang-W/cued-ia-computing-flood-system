# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
# from floodsystem.flood import stations_highest_rel_level


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent():
    """ Test this function written for Task 1F using arbitrary stations p, q and r"""

    # Create first test station
    s_id = "test1-s-id"
    m_id = "test1-m-id"
    label = "first test station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    p = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create second test station
    s_id = "test2-s-id"
    m_id = "test2-m-id"
    label = "second test station"
    coord = (-2.0, 4.0)
    trange = (4.11, -1.04)
    river = "River X"
    town = "My Town"
    q = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create third test station
    s_id = "test3-s-id"
    m_id = "test3-m-id"
    label = "third test station"
    coord = (-2.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    r = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert MonitoringStation.typical_range_consistent(p) is True
    assert MonitoringStation.typical_range_consistent(q) is False
    assert MonitoringStation.typical_range_consistent(r) is False


# Test not wokring, because cannot manually assign latest level to arbitrary stations
# def test_relative_water_level():
#    """Test this function written for Task 2B using arbitrary stations p, q, r, s and t"""
#
#    # Create first test station
#    s_id = "test1-s-id"
#    m_id = "test1-m-id"
#    label = "first test station"
#    coord = (0.0, 0.0)
#    trange = None
#    river = "River X"
#    town = "My Town"
#    latest_level = 3.0
#    p = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)

    # Create second test station
#    s_id = "test2-s-id"
#    m_id = "test2-m-id"
#    label = "second test station"
#    coord = (0.0, 0.0)
#    trange = (5.0, 2.0)
#    river = "River X"
#    town = "My Town"
#    latest_level = 3.0
#    q = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)

    # Create third test station
#    s_id = "test3-s-id"
#    m_id = "test3-m-id"
#    label = "third test station"
#    coord = (0.0, 0.0)
#    trange = (2.0, 5.0)
#    river = "River X"
#    town = "My Town"
#    latest_level = -1.0
#    r = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)

    # Create fourth test station
#    s_id = "test4-s-id"
#    m_id = "test4-m-id"
#    label = "fourth test station"
#    coord = (0.0, 0.0)
#    trange = (2.0, 5.0)
#    river = "River X"
#    town = "My Town"
#    latest_level = 3.5
#    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)

    # Create fifth test station
#    s_id = "test5-s-id"
#    m_id = "test5-m-id"
#    label = "fifth test station"
#    coord = (0.0, 0.0)
#    trange = (2.0, 5.0)
#    river = "River X"
#    town = "My Town"
#    latest_level = 8.0
#    t = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)

#    assert MonitoringStation.relative_water_level(p) is None
#    assert MonitoringStation.relative_water_level(q) is None
#    assert MonitoringStation.relative_water_level(r) == -1.0
#    assert MonitoringStation.relative_water_level(s) == 1.5
#    assert MonitoringStation.relative_water_level(t) == 2.0"""

# def test_stations_highest_rel_level():

#    """Test this function written for Task 2C using arbitrary stations p, q, r, s and t"""
    # Create first test station
#    s_id = "test1-s-id"
#    m_id = "test1-m-id"
#    label = "first test station"
#    coord = (0.0, 0.0)
#   trange = None
#    river = "River X"
#    town = "My Town"
#    latest_level = 3.0
#    p = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)

    # Create second test station
#    s_id = "test2-s-id"
#    m_id = "test2-m-id"
#    label = "second test station"
#    coord = (0.0, 0.0)
#    trange = (5.0, 2.0)
#    river = "River X"
#    town = "My Town"
#    latest_level = 3.0
#    q = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)

    # Create third test station
#    s_id = "test3-s-id"
#    m_id = "test3-m-id"
#    label = "third test station"
#    coord = (0.0, 0.0)
#    trange = (2.0, 5.0)
#    river = "River X"
#    town = "My Town"
#    latest_level = -1.0
#    r = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)

    # Create fourth test station
#    s_id = "test4-s-id"
#    m_id = "test4-m-id"
#    label = "fourth test station"
#    coord = (0.0, 0.0)
#    trange = (2.0, 5.0)
#    river = "River X"
#    town = "My Town"
#    latest_level = 3.5
#    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)

    # Create fifth test station
#    s_id = "test5-s-id"
#    m_id = "test5-m-id"
#    label = "fifth test station"
#    coord = (0.0, 0.0)
#    trange = (2.0, 5.0)
#    river = "River X"
#    town = "My Town"
#    latest_level = 8.0
#    t = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)

#    stations = [p, q, r, s, t]

#    assert stations_highest_rel_level(stations, 2) == [("fifth test station", 2), ("fourth test station", 0.5)]
