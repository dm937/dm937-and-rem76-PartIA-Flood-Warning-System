import floodsystem.geo
from floodsystem.stationdata import build_station_list


def test_call_stations_by_distance():
    x = floodsystem.geo.stations_by_distance(build_station_list(), (52.2053, 0.1218))

def test_correct_lengths():
     