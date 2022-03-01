import datetime
from floodsystem.analysis import flood_risk_assessment, polyfit
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


    
def test_polyfit():
    levels, dates = [3.90], [datetime.datetime.utcnow()]
    # testing that when an empty dates or levels list is inputted then an error is returned
    poly, d0 = polyfit(dates, levels, 3)
    assert len(poly)
    # test: wacky dates, warning for high order, warning for empty