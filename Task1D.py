from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def extract_names(Stations):
    Name_list = []
    for station in Stations:
        Name_list.append(station.name)
    Name_list.sort()
    return Name_list


def run():
    river_atleast_1station = rivers_with_station(build_station_list())
    print(len(river_atleast_1station), " stations. The first 10 are : " , river_atleast_1station[0:10])
    Stations_with_river_dict = stations_by_river(build_station_list())
    print(extract_names(Stations_with_river_dict["River Aire"]))
    print(extract_names(Stations_with_river_dict["River Cam"]))
    print(extract_names(Stations_with_river_dict["River Thames"]))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()