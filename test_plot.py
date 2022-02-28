# aim of this file to make a test for plot
# assert that nothing is returned when a 
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels



Test_station = MonitoringStation(
    station_id=3,
    measure_id=10,
    label='Test Station',
    coord=(float(3.1), float(3.0)),
    typical_range= (0.30, 1.30),
    river='lazy',
    town='nowhereland'
)

def test_plot_water_levels():
    dates, levels = [], []
    # testing that when an empty dates or levels list is inputted then no graph is plotted
    assert plot_water_levels(Test_station, dates, levels) == 'Test Station station has empty levels or dates list'



def test_plot_water_level_with_fit():
    dates, levels = [], []
    # testing that when an empty dates or levels list is inputted then no graph is plotted
    assert plot_water_levels(Test_station, dates, levels) == 'Test Station station has empty levels or dates list'