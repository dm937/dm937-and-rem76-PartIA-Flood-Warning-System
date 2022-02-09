# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from haversine import haversine


def stations_by_distance(stations, p):
    #creates empty list 
    StationsDistance = []
    # appends (name, town, distance) tuple for every station in stations
    for station in stations:
        Current_tuple = (station.name, station.town) + (haversine(station.coord, p),)
        StationsDistance.append(Current_tuple)
    # final line sorts the list by distance (distance is the 2nd index in each tuple)
    return sorted_by_key(StationsDistance, 2)


def stations_within_radius(stations, centre, r):
    # Task 1 C, returns a list of stations within a radius
    print("Test")
    print(haversine(stations[1],centre))
    """[i if (haversine(i, centre) > r) for i in stations]"""


def rivers_with_station(stations):
    # use of a set as the container will ensure that no duplicate rivers can be added to the container
    # length of this container will be number of rivers with a monitoring station
    
    return set(stations.river)