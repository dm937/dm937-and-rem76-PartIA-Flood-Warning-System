# this file is for general code for just getting used to programs and syntax 
from floodsystem.stationdata import build_station_list
import floodsystem.geo

AllStations = build_station_list()
#Rivers = set()
#for station in AllStations:
#    Rivers.add(station.river)
#Rivers_list = list(Rivers)
#Rivers_list.sort()
#print(sorted(Rivers))

#a = [1, 2, 3, 4, 3, 2]
#my_set = {x for x in a}
#print(my_set)

river_station_dict = floodsystem.geo.stations_by_river(AllStations)
print (river_station_dict["River Aire"])