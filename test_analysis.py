import datetime
from floodsystem.analysis import flood_risk_assessment
from floodsystem.station import MonitoringStation


Test_station = MonitoringStation(
    station_id=1,
    measure_id=10,
    label='Test Station',
    coord=(float(3.1), float(3.0)),
    typical_range= (0.30, 1.30),
    river='lazy',
    town='nowhereland'
)


def test_flood_risk_assessment():
    levels, dates = [3.90], [datetime.datetime.utcnow()]
    # checking these levels produce a severe threat response 
    assert flood_risk_assessment(Test_station, dates, levels) == 'severe'
    levels, dates = [1.30], [datetime.datetime.utcnow()]
    # checking these levels produce a high threat response 
    assert flood_risk_assessment(Test_station, dates, levels) == 'high'
    levels, dates = [1.20], [datetime.datetime.utcnow()]
    # checking these levels produce a moderate threat response 
    assert flood_risk_assessment(Test_station, dates, levels) == 'moderate'
    levels, dates = [0.30], [datetime.datetime.utcnow()]
    # checking these levels produce a low threat response 
    assert flood_risk_assessment(Test_station, dates, levels) == 'low'
    levels, dates = [], [datetime.datetime.utcnow()]
    # checking inconsistent results produce no response
    assert flood_risk_assessment(Test_station, dates, levels) == None