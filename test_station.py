# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
# below are bad stations 

Inconsistent_Station_1 = MonitoringStation(
    station_id=1,
    measure_id=10,
    label='Inconsistent_Station_1',
    coord=(float(3.0), float(3.0)),
    typical_range= None,
    river='lazy',
    town='nowhereland'
)

Inconsistent_Station_2 = MonitoringStation(
    station_id=2,
    measure_id=10,
    label='Inconsistent_Station_1',
    coord=(float(3.1), float(3.0)),
    typical_range= (1.19, 0.56),
    river='lazy',
    town='nowhereland'
)


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


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    assert MonitoringStation.typical_range_consistent(Inconsistent_Station_1) == False
    assert MonitoringStation.typical_range_consistent(Inconsistent_Station_2) == False

def test_inconsistent_typical_range_stations():
    BadStations = [Inconsistent_Station_1, Inconsistent_Station_2]
    assert len(inconsistent_typical_range_stations(BadStations)) == 2

def test_relative_water_level():
    consistent_Station_1.latest_level = 1.20
    assert MonitoringStation.relative_water_level(consistent_Station_1) == 1
    consistent_Station_1.latest_level = 0.20
    assert MonitoringStation.relative_water_level(consistent_Station_1) == 0
    consistent_Station_1.latest_level = 0.70
    assert round(MonitoringStation.relative_water_level(consistent_Station_1), 3) == 0.50
    # checking below the minimum gives 0
    consistent_Station_1.latest_level = 0.15
    assert round(MonitoringStation.relative_water_level(consistent_Station_1), 3) == 0.00
    # checking above the maximum will give an appropriate fraction
    consistent_Station_1.latest_level = 2.20
    assert round(MonitoringStation.relative_water_level(consistent_Station_1), 3) == 2.00
