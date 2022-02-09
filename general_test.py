# this file is for general code for just getting used to programs and syntax 
from floodsystem.stationdata import build_station_list
#cont = [""]*10
#for i in range(len(cont)):
#    print(i)

AllStations = build_station_list()
Rivers = set()
for station in AllStations:
    Rivers.add(station.river)

print(len(Rivers))

a = [1, 2, 3, 4, 3, 2]
my_set = {x for x in a}
print(my_set)