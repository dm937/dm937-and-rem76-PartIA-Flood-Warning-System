import numpy as np
import matplotlib

from floodsystem.station import MonitoringStation

def polyfit(dates, levels, p):
    w_dates = matplotlib.dates.date2num(dates)
    shift = w_dates[0]
    w_dates -= shift     
    coefficients = np.polyfit(w_dates,levels, p)
    return np.poly1d(coefficients), shift

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
import numpy as np
from datetime import timedelta


def flood_risk_assessment(station):
    '''
    used to assess the risk of flooding and returns one of 4 strings
    severe - average level over the past 3 days is at a relative level of >3
    high - average level over the past 3 days is at a relative level of 3> relative level>1
    moderate - average level over the past 3 days is at a relative level of 1>relative level>0.8
    low - average level over the past 3 days is at a relative level of <0.8
    '''
    if not station.typical_range_consistent:
        return None
    days_back = 3
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=days_back))
    if dates == [] or levels ==[]:
        return '{} station has empty levels or dates list'.format(station.name)
    level_array = np.array(levels)
    average_level = np.dot(level_array, np.ones(len(level_array)))
    relative_level_ot = average_level/station.typical_range[1]
    if relative_level_ot >= 3:
        return 'severe'
    elif 3 > relative_level_ot >=1:
        return 'high'
    elif 1> relative_level_ot >= 0.8:
        return 'moderate'
    else:
        return 'low'
