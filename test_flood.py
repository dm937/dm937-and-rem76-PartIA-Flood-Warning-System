from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

consistent_Station_3 = MonitoringStation(
    station_id=3,
    measure_id=10,
    label='consistent_Station_3',
    coord=(float(3.1), float(3.0)),
    typical_range= (0.30, 1.30),
    river='lazy',
    town='nowhereland'
)


consistent_Station_2 = MonitoringStation(
    station_id=2,
    measure_id=10,
    label='consistent_Station_2',
    coord=(float(3.1), float(3.0)),
    typical_range= (0.50, 1.50),
    river='lazy',
    town='nowhereland'
)

consistent_Station_1 = MonitoringStation(
    station_id=1,
    measure_id=10,
    label='consistent_Station_1',
    coord=(float(3.0), float(3.0)),
    typical_range= (0.20, 1.20),
    river='lazy',
    town='nowhereland'
)

stations = [consistent_Station_1, consistent_Station_2, consistent_Station_3]
consistent_Station_1.latest_level = 1.20
consistent_Station_2.latest_level = 0.50
consistent_Station_3.latest_level = 1.33

station_dict = {i.name : i for i in stations}


def test_stations_level_over_threshold():
    # testing that all stations are returned when a negative tolerance is given
    assert len(stations_level_over_threshold(stations, -1)) == 3
    # testing descending order
    assert stations_level_over_threshold(stations, -1)[0][1] > stations_level_over_threshold(stations, -1)[1][1] > stations_level_over_threshold(stations, -1)[2][1]
    # testing that 2 are returned when 0 is the tolerance
    assert len(stations_level_over_threshold(stations, 0)) == 2
    # testing that only 1 is given when 1 is the tolerance
    assert len(stations_level_over_threshold(stations, 1)) == 1
    # testing that the name of the station given is consistent station 3
    assert stations_level_over_threshold(stations, 1)[0][0].name == 'consistent_Station_3'
    
    
def test_stations_highest_rel_level():
    high_rev_level = stations_highest_rel_level(stations, 3)
    assert len(high_rev_level) == 3 #testing that correct number of stations are returned
    assert high_rev_level[1][1] >= high_rev_level[2][1] #checking that sort is correct
    high_rev_level[0][0]
    "assert high_rev_level[0][1] == station_dict[high_rev_level[0][0]].relative_water_level()" #Checking the relative water level value
    assert high_rev_level[0][1] == station_dict[consistent_Station_1].relative_water_level()
