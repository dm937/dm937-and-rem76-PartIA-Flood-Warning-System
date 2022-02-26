from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

consistent_Station_2 = MonitoringStation(
    station_id=2,
    measure_id=10,
    label='Inconsistent_Station_1',
    coord=(float(3.1), float(3.0)),
    typical_range= (0.50, 1.50),
    river='lazy',
    town='nowhereland'
)

consistent_Station_1 = MonitoringStation(
    station_id=1,
    measure_id=10,
    label='Inconsistent_Station_1',
    coord=(float(3.0), float(3.0)),
    typical_range= (0.20, 1.20),
    river='lazy',
    town='nowhereland'
)

def test_stations_level_over_threshold():
    stations = [consistent_Station_1, consistent_Station_2]
    consistent_Station_1.latest_level = 1.20
    consistent_Station_2.latest_level = 0.50
    # testing that both stations are returned when a negative tolerance is given
    assert len(stations_level_over_threshold(stations, -1)) == 2
    # testing that only 1 is returned when 0 is the tolerance
    assert len(stations_level_over_threshold(stations, 0)) == 1
    # testing that none are given when 0 is the tolerance (as 1 is not greater than 1)
    assert len(stations_level_over_threshold(stations, 1)) == 0
    

