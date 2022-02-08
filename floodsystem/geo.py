# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from haversine import haversine, Unit
import maths


def stations_by_distance(stations, p):
    StationsDistance = [""]*len(stations)
    i = 0
    for station in stations:
        StationsDistance[i] = (station, int(haversine(station.coord, p)))
        i += 1
    StationsDistance = sorted_by_key(StationsDistance, 1)
    return StationsDistance


def stations_within_radius(stations, centre, r):
    # Task 1 C, returns a list of stations within a radius
    [i if (haversine(i, centre) > r) for i in stations]


