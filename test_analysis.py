import datetime
from floodsystem.analysis import flood_risk_assessment, polyfit
from floodsystem.station import MonitoringStation
import numpy as np
import matplotlib

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
    """    test_dates = [datetime.datetime.utcnow() - datetime.timedelta(days=x) for x in range(10)]
    test_poly = np.poly1d([2,3,4,5])
    test_levels = test_poly(np.array(matplotlib.dates.date2num(test_dates)))
    poly, d0 = polyfit(test_dates, test_levels, 4)
    print(poly)
    assert poly == test_poly"""
    # test: wacky dates, warning for high order, warning for empty

    test_dates = [datetime.datetime.now() - datetime.timedelta(days=x) for x in range(10)]
    test_poly = np.poly1d([2, 1, 7])
    test_date_numbers = matplotlib.dates.date2num(test_dates)
    test_date_numbers -= test_date_numbers[0]
    test_levels = test_poly(np.array(test_date_numbers))
    poly, d0 = polyfit(test_dates, test_levels, 4)
    assert all(poly.c) == all(test_poly.c)
    # assert d0 == test_date_numbers[0]
