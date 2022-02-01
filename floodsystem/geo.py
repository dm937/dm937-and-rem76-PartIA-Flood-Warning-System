# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    StationsDistance = [""]*len(stations)
    i = 0
    for station in stations:
        StationsDistance[i] = (station, int(haversine(station.coord, p)))
        i += 1
    StationsDistance = sorted_by_key(StationsDistance, 1)
    return StationsDistance
    