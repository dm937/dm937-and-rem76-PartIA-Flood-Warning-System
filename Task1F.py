from floodsystem.stationdata import build_station_list
from Task1D import extract_names
from floodsystem.station import inconsistent_typical_range_stations
from test_geo import AllStations

def run():
    Inconsistent_Stations_list = inconsistent_typical_range_stations(build_station_list())
    Inconsistent_names_list = extract_names(Inconsistent_Stations_list)
    Inconsistent_names_list.sort()
    print(Inconsistent_names_list)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()