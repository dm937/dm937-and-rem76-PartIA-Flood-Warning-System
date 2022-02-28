from floodsystem.analysis import flood_risk_assessment
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    # gives the number of stations for each type of threat level in a smaller sample of all stations so as to reduce computation time
    stations = build_station_list()
    update_water_levels(stations)
    Nsevere, Nhigh, Nmoderate, Nlow, Nincompatible = 0,0,0,0, 0
    for station in stations[-21:-1]:
        assessment = flood_risk_assessment(station)
        if  assessment =='severe':
            Nsevere +=1
        elif  assessment =='high':
            Nhigh +=1
        elif  assessment =='moderate':
            Nmoderate += 1
        elif assessment =='low':
            Nlow +=1
        else:
            Nincompatible +=1
    print('{} stations are at severe risk of flooding, {} stations are at high risk of flooding, {} stations are at moderate risk of flooding, {} stations are at low risk of flooding and {} stations were incompatible with assessment'.format(Nsevere, Nhigh, Nmoderate, Nlow, Nincompatible))


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()