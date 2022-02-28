from floodsystem.stationdata import build_station_list
from datetime import datetime, timedelta
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels

def run():
    stations = build_station_list()
    NumStations = 5
    # number of days going back
    dt = 10
    StationsInterest = stations_highest_rel_level(stations, NumStations)
    print(StationsInterest)
    for station in StationsInterest:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        print(dates, levels)
        plot_water_levels(station, levels, dates)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
