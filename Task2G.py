from floodsystem.analysis import flood_risk_assessment
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def run():
    # aiming to return the number of sattions that are at severe, high, moderate and low risk
    stations = 'hi'
    return '{} stations are at severe risk of flooding, {} stations are at high risk of flooding, {} stations are at moderate risk of flooding and {} stations are at low risk of flooding'


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()