import numpy as np
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta
from floodsystem.station import MonitoringStation


def polyfit(dates, levels, p):
    w_dates = matplotlib.dates.date2num(dates)
    shift = w_dates[0]
    w_dates -= shift     
    coefficients = np.polyfit(w_dates,levels, p)
    return np.poly1d(coefficients), shift



def flood_risk_assessment(station, dates, levels):
    '''
    used to assess the risk of flooding and returns one of 4 strings
    severe - average level over the past specified days is at a relative level of >3
    high - average level over the past specified days is at a relative level of 3> relative level>1
    moderate - average level over the past specified days is at a relative level of 1>relative level>0.8
    low - average level over the past specified days is at a relative level of <0.8
    '''
    # checks that data is compatible
    if not station.typical_range_consistent:
        return None
    if dates == [] or levels ==[] or type(dates) == None or type(levels) == None:
        return None
    level_array = np.array(levels)
    # uses np arrays to reduce computation time
    average_level = np.dot(level_array, np.ones(len(level_array)))
    # finds the average water level 
    relative_level_ot = average_level/(station.typical_range[1]*len(level_array))
    # returns which threat level the station is 
    if relative_level_ot >= 3:
        return 'severe'
    elif 3 > relative_level_ot >=1:
        return 'high'
    elif 1> relative_level_ot >= 0.5:
        return 'moderate'
    else:
        return 'low'
