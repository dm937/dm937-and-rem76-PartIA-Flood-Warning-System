from floodsystem.stationdata import build_station_list, update_water_levels
from datetime import datetime, timedelta
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    # number of stations to plot 
    NumStations = 5
    # number of days going back
    dt = 2
    StationsInterest = stations_highest_rel_level(stations, NumStations)
    for station in StationsInterest:
        dates, levels = fetch_measure_levels(station.measure_id, dt= timedelta(days=dt))
        print(dates)
        plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
