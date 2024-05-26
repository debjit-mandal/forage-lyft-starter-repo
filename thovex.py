# thovex.py
from car import Car
from capulet_engine import CapuletEngine
from nubbin_battery import NubbinBattery


class Thovex(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, current_date):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        super().__init__(engine, battery)
