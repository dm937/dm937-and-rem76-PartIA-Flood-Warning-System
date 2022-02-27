
import numpy as py

from floodsystem.station import MonitoringStation



#def stations_highest_rel_level(stations, N):
#    range_ratios = [i, i.typical_range for i in stations]
#    sorted_range_ratios = range_ratios.sorted()


def stations_level_over_threshold(stations, tol):
    '''
    returns a list of tuples, where each tuple holds (i) a station (object) 
    at which the latest relative water level is over tol 
    and (ii) the relative water level at the station. 
    '''
    Stations_over_tol = []
    # loops through the stations
    for station in stations:
        # checks if relative water level is over that of the tolerance
        if MonitoringStation.relative_water_level(station) == None:
            pass
        elif MonitoringStation.relative_water_level(station) > tol:
            # adds the staion and relative water level tuple to the list
            Stations_over_tol.append((station, MonitoringStation.relative_water_level(station)))
    # sorts the list in descending order by the relative water level
    Stations_over_tol = sorted(Stations_over_tol, key=lambda tup: tup[1], reverse=True)
    return Stations_over_tol

def stations_highest_rel_level(stations, N):
    station = stations[1]
    print(station.relative_water_level())
    # returns station objects with the highest water level relative to typical
    valid_stations = [i for i in stations if i.relative_water_level() != None and i.typical_range_consistent() == True]
    station_levels = [(i, i.relative_water_level()) for i in valid_stations]
    sorted_station_levels = sorted(station_levels, key = lambda tup:tup[1], reverse=True)
    sorted_stations = [i[0] for i in sorted_station_levels]
    return sorted_stations[:N]