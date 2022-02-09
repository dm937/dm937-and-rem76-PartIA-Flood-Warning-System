import floodsystem.geo
from floodsystem.stationdata import build_station_list


def test_call_stations_by_distance():
    x = floodsystem.geo.stations_by_distance(build_station_list(), (52.2053, 0.1218))

def test_correct_lengths_stations_by_distance():
     assert len(build_station_list()) == len(floodsystem.geo.stations_by_distance(build_station_list(), (52.2053, 0.1218)))
     # checking special values don't affect the program
     assert len(build_station_list()) == len(floodsystem.geo.stations_by_distance(build_station_list(), (0, 0)))
     assert len(build_station_list()) == len(floodsystem.geo.stations_by_distance(build_station_list(), (-90, 90)))
     assert len(build_station_list()) == len(floodsystem.geo.stations_by_distance(build_station_list(), (90, -90)))
     assert floodsystem.geo.stations_by_distance(build_station_list(), (52.2053, 0.1218))[]