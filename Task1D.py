from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station

def run():
    river_atleast_1station = rivers_with_station(build_station_list())
    print(len(river_atleast_1station), " stations. The first 10 are : " , river_atleast_1station[0:10])

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()