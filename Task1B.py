#working file used to run stations-distance function addded to geo 
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from haversine import haversine, Unit


def run():
    coords_of_interest = (52.2053, 0.1218) #coords suggested in deliverables section used
    print(stations_by_distance(build_station_list(), coords_of_interest)[:10])
    print(stations_by_distance(build_station_list(), coords_of_interest)[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()