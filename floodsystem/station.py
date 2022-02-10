# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range, 
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None



    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        # Function has the input of a station and will check if it has inconsistent typical ranges ie if there is no range or high range< low range
        # Returns false if the data is inconsistent, True if the data is consistent
        if type(self.typical_range) != tuple:
            #checking if the type is unexpected 
            return False
        elif len(self.typical_range) != 2:
            # checking if the length is unexpected
            return False    
        elif self.typical_range[0]>self.typical_range[1]:
            #checking if high range < low range 
            return False
        else:
            # typical range has passed tests and so is returned as consistent
            return True


def inconsistent_typical_range_stations(stations):
    #given a list of MonitoringStation objects it will return a list of which of these stations has inconsistent data 
    InconsistentStations = []
    for station in stations:
        # looping through list to check each station in given list
        if MonitoringStation.typical_range_consistent(station) == False:
            # Uses method in monitoring station class to check if station has inconsistent data and if so adds it to the list
            InconsistentStations.append(station)
    # returns list of inconsistent stations
    return InconsistentStations

