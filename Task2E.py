# Task2E: plot water level

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime
from floodsystem.datafetcher import fetch_measure_levels


def run():
    """Requirements for Task 2E"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # 5 stations to plot
    stations_plot = []
    for i in stations_highest_rel_level(stations, 5):
        stations_plot.append(i[0])

    # create a list of stations with all information required
    final_plot = []

    for i in stations_plot:
        for station in stations:
            if i == station.name:
                final_plot.append(station)

    # plot the graph for past 10 days
    dt = 10
    for station in final_plot:
        station = station
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
