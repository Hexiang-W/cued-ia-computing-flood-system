# Task 2F: function fitting

import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level


def run():
    """Requirements for Task 2F"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Returns 5 stations where the water level, relative to typical range
    most_risky_stations = stations_highest_rel_level(stations, 5)

    # Add names of risky station to a list
    names_of_risky_stations = []
    for station in most_risky_stations:
        names_of_risky_stations.append(station[0])

    # Find and add the risky stations into a list with all its relevant info
    # (which is not included in the results of the function most_risky_stations)
    risky_stations = []
    for name in names_of_risky_stations:
        for station in stations:
            if station.name == name:
                risky_stations.append(station)

    # Fetch data over past 2 days
    dt = 2
    for station in risky_stations:
        station = station
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
