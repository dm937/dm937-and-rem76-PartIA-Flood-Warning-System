from distutils.command import build
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_by_station_number, rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list
AllStations = build_station_list()

def test_call_stations_by_distance():
    x = stations_by_distance(AllStations, (52.2053, 0.1218))

def test_correct_lengths_stations_by_distance():
     assert len(build_station_list()) == len(stations_by_distance(AllStations, (52.2053, 0.1218)))
     # checking special values don't affect the program
     assert len(AllStations) == len(stations_by_distance(AllStations, (0, 0)))
     assert len(AllStations) == len(stations_by_distance(AllStations, (-90, 90)))
     assert len(AllStations) == len(stations_by_distance(AllStations, (90, -90)))

def test_stations_within_radius():
    assert len(stations_within_radius(AllStations, (52.2053, 0.1218), 10000)) == len(AllStations)
    assert len(stations_within_radius(AllStations, (52.2053, 0.1218), 10)) > 0
    assert len(stations_within_radius(AllStations, (52.2053, 0.1218), 1)) < len(stations_within_radius(AllStations, (52.2053, 0.1218), 10))

def test_rivers_by_station_number():
    river_test = rivers_by_station_number(AllStations, 10)
    assert len(river_test) >= 1
    assert river_test[1][1] >= river_test[4][1]
    assert type(river_test) == list
    assert type(river_test[2]) == tuple

def test_rivers_with_station():
    assert len(rivers_with_station(AllStations)) > 0
    assert len(rivers_with_station([])) == 0

def test_stations_with_river():
    assert len(stations_by_river(AllStations)) > 0
    assert len(stations_by_river([])) == 0
