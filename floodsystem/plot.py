import matplotlib.pyplot as plt
from numpy import linspace
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.dates

def plot_water_levels(station, dates, levels):
    '''
    displays a plot of the water level data against time for a station.
    And includes plot lines for the typical low and high levels.
    '''
    if levels == [] or dates ==[]:
        return 'no current levels could be found'
    else:
        # converts dates to more useable format
        dates = matplotlib.dates.date2num(dates)
        # subtacts the first (and largest) date from all previous dates, giving an array ranging from 0 to -x where x is the number of days previously specified
        dates = dates - dates[0]
        num = 40
        dates_plotted_against = linspace(dates[0], dates[-1], num) 
        plt.plot(dates_plotted_against, linspace(station.typical_range[0], station.typical_range[0], num), '-g', label = 'typical low')
        plt.plot(dates_plotted_against, linspace(station.typical_range[1], station.typical_range[1], num), '-r', label = 'typical high')
        plt.plot(dates, levels, 'b')
        plt.xlabel('days before')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45);
        plt.title(station.name)
        # Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels
        plt.show()