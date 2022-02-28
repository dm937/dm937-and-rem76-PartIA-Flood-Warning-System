from floodsystem.analysis import flood_risk_assessment
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    # aiming to return the number of stations that are at severe, high, moderate and low risk 
    stations = build_station_list()
    update_water_levels(stations)
    NumStations = 6
    stations = stations_highest_rel_level(stations, NumStations)
    Nsevere, Nhigh, Nmoderate, Nlow = 0,0,0,0
    for station in stations:
        if flood_risk_assessment(station) =='severe':
            Nsevere +=1
        if flood_risk_assessment(station) =='high':
            Nhigh +=1
        if flood_risk_assessment(station) =='moderate':
            Nmoderate += 1
        elif flood_risk_assessment(station) =='low':
            Nlow +=1
    print('{} stations are at severe risk of flooding, {} stations are at high risk of flooding, {} stations are at moderate risk of flooding and {} stations are at low risk of flooding'.format(Nsevere, Nhigh, Nmoderate, Nlow))


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()