import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from datafetcher import fetch_measure_levels
import matplotlib.dates

def plot_water_levels(station, dates, levels):
    '''
    displays a plot of the water level data against time for a station.
    And includes plot lines for the typical low and high levels.
    '''
    if levels == [] or dates ==[]:
        pass
    elif type(levels) == list and type(dates) == list:
        dates = matplotlib.dates.date2num(dates)
        print(dates)
        
    else:
        return 'error, dates and/or levels were not correct type'
    # Plot
    plt.plot(, )
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()