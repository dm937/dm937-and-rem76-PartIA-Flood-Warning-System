# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from haversine import haversine


def stations_by_distance(stations, p):
    StationsDistance = [""]*len(stations)
    i = 0
    for station in stations:
        StationsDistance[i] = (station.name, station.town) + (int(haversine(station.coord, p)),)
        i += 1
    return sorted_by_key(StationsDistance, 2)


def stations_within_radius(stations, centre, r):
    # Task 1 C, returns a list of stations within a radius
    print("Test")
    print(haversine(stations[1],centre))
    """[i if (haversine(i, centre) > r) for i in stations]"""


