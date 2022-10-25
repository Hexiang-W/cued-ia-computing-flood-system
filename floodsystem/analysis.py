""" This modules provides functinality for computing a least-squares fit of
a polynomial of degree p to water level data"""

import matplotlib
import numpy as np


def polyfit(dates, levels, p):
    """Returns best-fit polynomial of a plot"""

    # Convert dates as a function argument to floats
    float_dates = matplotlib.dates.date2num(dates)

    # Using shifted x values, find coefficient of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(float_dates - float_dates[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    return poly
