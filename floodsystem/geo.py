# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from math import cos, asin, sqrt
from cmath import pi
from .utils import sorted_by_key


def stations_by_distance(stations, p):
    # this program returns a list
    #creates empty list 
    StationsDistance = []
    # appends (name, town, distance) tuple for every station in stations
    for station in stations:
        Current_tuple = (station.name, station.town) + (distance_between_points(station.coord, p),)
        StationsDistance.append(Current_tuple)
    # final line sorts the list by distance (distance is the 2nd index in each tuple)
    return sorted_by_key(StationsDistance, 2)

def distance_between_points(coord1, coord2):
    '''
    gives the distance between 2 coordinates (coords in longtitude and latitude)
    '''
    lat1, lon1, lat2, lon2 = coord1[0], coord1[1], coord2[0], coord2[1]
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))

def stations_within_radius(stations, centre, r):
    # Task 1 C, returns a list of stations from the inputted list "stations" within a radius "r" of a coordinate tuple "centre"
    return [i for i in stations if(distance_between_points(i.coord,centre)<r)]
 
    
def rivers_by_station_number(stations, N):
    #returns the N rivers with the greatest number of stataions with the number of stations on each river
    rivers = [i.river for i in stations]
    rivers_count = []
    #produces a list of tuples of rivers and their number of stations
    for i in rivers:
        n= rivers.count(i)
        rivers_count.append((i,n))
        rivers = [x for x in rivers if x != i]
    #sorts the list in decending order of station number
    rivers_ordered = sorted(rivers_count, key = lambda i: i[1], reverse= True)
    #Takes the N with the largest number of stations, allowing additional repeats of the final value
    top_N = rivers_ordered[:N-1] + [i for i in rivers_ordered if i[1] == rivers_ordered[N][1]]
    return top_N


def rivers_with_station(stations):
    # This functions creates a container with the rivers monitoring a list of stations - the rivers in this list are all unique 
    # use of a set as the container will ensure that no duplicate rivers can be added to the container
    # length of this container will be number of rivers with a monitoring station
    Rivers = set()
    for station in stations:
        # as Rivers is a set it will only add non dupliccate entries 
        Rivers.add(station.river)
    # sorted command then changes the set into an ascending ordered list - usefull for indexing/slicing
    return sorted(Rivers)

def stations_by_river(stations):
    # creates empty dictionary 
    station_river_dict = {}
    #uses previous function to get list of rivers monitoring the inputed list of stations
    Rivers = rivers_with_station(stations)
    # looping through all rivers the user want to create keys for
    for river in Rivers:
        # creates empty list for stations with that river to be stored in
        Connections = []
        for station in stations:
            # adds all stations with that river to a list
            if station.river == river:
                Connections.append(station)
        # the river then becomes the key for this list of stations
        station_river_dict[river] = Connections
    return station_river_dict