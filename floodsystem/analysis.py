import numpy as np
import matplotlib

from floodsystem.station import MonitoringStation

def polyfit(dates, levels, p):
    w_dates = matplotlib.dates.date2num(dates)
    shift = w_dates[0]
    w_dates -= shift     
    coefficients = np.polyfit(w_dates,levels, p)
    return np.poly1d(coefficients), shift

