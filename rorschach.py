# rorschach.py
from car import Car
from willoughby_engine import WilloughbyEngine
from nubbin_battery import NubbinBattery


class Rorschach(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, current_date):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        super().__init__(engine, battery)
