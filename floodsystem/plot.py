import matplotlib.pyplot as plt
from datetime import datetime, timedelta
<<<<<<< HEAD
from datafetcher import 

def plot_water_levels(station, dates, levels):
    '''
    displays a plot of the water level data against time for a station.
    And includes plot lines for the typical low and high levels.
    '''
=======
import numpy as np

def plot_water_levels(station, dates, levels):
    
    
>>>>>>> 4510fe8c2aaf5f45b9c9a76127bab544da0d4bb5

    # Plot
    plt.plot(t, level)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
<<<<<<< HEAD
    plt.title(station.name)
    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
=======
    plt.title("Station A")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

>>>>>>> 4510fe8c2aaf5f45b9c9a76127bab544da0d4bb5
    plt.show()