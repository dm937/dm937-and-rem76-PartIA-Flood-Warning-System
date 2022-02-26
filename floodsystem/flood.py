
import numpy as py
from floodsystem.station import MonitoringStation


def stations_highest_rel_level(stations, N):
    range_ratios = [(i, i.typical_range) for i in stations]
    sorted_range_ratios = range_ratios.sorted()