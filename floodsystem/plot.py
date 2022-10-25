"""This module provides a model for a graph ploting
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from floodsystem.analysis import polyfit


def plot_water_levels(station, dates, levels):

    # Initial settings
    t = dates
    level = levels

    # Plot the graph
    plt.plot(t, level)

    # Plot graphs of upper and lower boundaries
    plt.plot(t, np.ones(len(t)) * station.typical_range[0], color='g', label='typical low')
    plt.plot(t, np.ones(len(t)) * station.typical_range[1], color='r', label='typical high')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """Return plots of the water level data with its correspondng best-fit polynomial"""

    # Initial settings
    t = dates
    level = levels

    # Convert dates to float
    float_dates = matplotlib.dates.date2num(dates)

    # Convert float dates to equally-spaced list, suitable for plotting
    plot_dates = np.linspace(float_dates[0], float_dates[-1], len(float_dates))

    # Settings for best-fit polynomial
    polynomial = polyfit(dates, levels, p)

    # Plot the graphs of water level and best-fit polynomial
    plt.plot(plot_dates, level, color='b', label='water level data')
    plt.plot(plot_dates, polynomial(plot_dates - plot_dates[0]), color='y', label='best-fit polynomial')

    # Plot graphs of upper and lower boundaries
    plt.plot(plot_dates, np.ones(len(t)) * station.typical_range[0], color='g', label='typical low')
    plt.plot(plot_dates, np.ones(len(t)) * station.typical_range[1], color='r', label='typical high')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
