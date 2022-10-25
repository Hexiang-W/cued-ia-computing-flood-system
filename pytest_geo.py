"""Unit test for the geo module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number


def test_stations_by_distance():
    """Test this function written for Task 1B"""

    k = (0.0, 0.0)

    # Create first test station
    s_id = "test1-s-id"
    m_id = "test1-m-id"
    label = "first test station"
    coord = (1.0, 1.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town 1"
    p = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create second test station
    s_id = "test2-s-id"
    m_id = "test2-m-id"
    label = "second test station"
    coord = (2.0, 2.0)
    trange = (4.11, -1.04)
    river = "River X"
    town = "My Town 2"
    q = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create third test station
    s_id = "test3-s-id"
    m_id = "test3-m-id"
    label = "third test station"
    coord = (-2.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town 3"
    r = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    station_list_1 = [p, q, r]
    expected_one = ("first test station", "My Town 1", 157.2495984740402)
    expected_two = ("second test station", "My Town 2", 314.47523947196964)
    expected_three = ("third test station", "My Town 3", 497.19868760742435)
    expected_results = [expected_one, expected_two, expected_three]
    assert stations_by_distance(station_list_1, k) == expected_results


def test_stations_within_radius():
    """Test this function written for Task 1C by checking number of stations when r=0, r=440 and r=468"""

    # Set arguments for test
    stations = build_station_list()
    cambridge_centre = (52.2053, 0.1218)

    # Find stations within 0km radius, which should return none
    test_radius_one = 0

    # Find stations within 440km radius, which should return all stations except the furthest ten stations
    test_radius_two = 440

    # Find stations within 468km radius, which should return all stations
    test_radius_three = 468

    # Find number of stations within 0km, 440km and 468km respectively
    demonstration_1C_test_one = len(stations_within_radius(stations, cambridge_centre, test_radius_one))
    demonstration_1C_test_two = len(stations_within_radius(stations, cambridge_centre, test_radius_two))
    demonstration_1C_test_three = len(stations_within_radius(stations, cambridge_centre, test_radius_three))

    # Number of stations within 0km should be zero
    assert demonstration_1C_test_one == 0

    # Number of stations within 440km should be 2094
    assert demonstration_1C_test_two == 2094

    # Number of stations within 468km should be 2104
    assert demonstration_1C_test_three == 2104


def test_rivers_with_station():
    """Test this function written for Task 1D using arbitrary stations p, q, r, s and t"""

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
    river = "River Y"
    town = "My Town"
    q = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create third test station
    s_id = "test3-s-id"
    m_id = "test3-m-id"
    label = "third test station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River Z"
    town = "My Town"
    r = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create fourth test station
    s_id = "test4-s-id"
    m_id = "test4-m-id"
    label = "fourth test station"
    coord = (-2.0, 4.0)
    trange = (4.11, -1.04)
    river = "River Y"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create fifth test station
    s_id = "test5-s-id"
    m_id = "test5-m-id"
    label = "fifth test station"
    coord = (-2.0, 4.0)
    trange = (4.11, -1.04)
    river = "River X"
    town = "My Town"
    t = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Returns all rivers in a list
    stations = [p, q, r, s, t]
    rivers = rivers_with_station(stations)

    # Add expected result into a list
    expected_rivers = ["River X", "River Y", "River Z"]

    # Compare returned and expected results
    assert rivers == expected_rivers


def test_stations_by_river():
    """Test this function written for Task 1D using arbitrary stations p, q, r, s and t"""

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
    river = "River Y"
    town = "My Town"
    q = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create third test station
    s_id = "test3-s-id"
    m_id = "test3-m-id"
    label = "third test station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River Z"
    town = "My Town"
    r = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create fourth test station
    s_id = "test4-s-id"
    m_id = "test4-m-id"
    label = "fourth test station"
    coord = (-2.0, 4.0)
    trange = (4.11, -1.04)
    river = "River Y"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create fifth test station
    s_id = "test5-s-id"
    m_id = "test5-m-id"
    label = "fifth test station"
    coord = (-2.0, 4.0)
    trange = (4.11, -1.04)
    river = "River X"
    town = "My Town"
    t = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Returns all stations on each river in a list
    stations = [p, q, r, s, t]
    rivers_and_stations = stations_by_river(stations)
    river_x = rivers_and_stations["River X"]
    river_y = rivers_and_stations["River Y"]
    river_z = rivers_and_stations["River Z"]

    # Add expected result into a list
    expected_river_x = ["first test station", "fifth test station"]
    expected_river_y = ["second test station", "fourth test station"]
    expected_river_z = ["third test station"]

    # Compare returned and expected results
    assert river_x == expected_river_x
    assert river_y == expected_river_y
    assert river_z == expected_river_z


def test_rivers_by_station_number():
    """Test this function written for Task 1E"""

    N = 1

    # Create first test station
    s_id = "test1-s-id"
    m_id = "test1-m-id"
    label = "first test station"
    coord = (1.0, 1.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    p = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create second test station
    s_id = "test2-s-id"
    m_id = "test2-m-id"
    label = "second test station"
    coord = (2.0, 2.0)
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

    # Create fourth test station
    s_id = "test4-s-id"
    m_id = "test4-m-id"
    label = "fourth test station"
    coord = (-2.0, -4.0)
    trange = (4.11, -1.04)
    river = "River Y"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    station_list = [p, q, r, s]
    assert rivers_by_station_number(station_list, N) == [("River X", 3)]
