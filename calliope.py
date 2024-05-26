# calliope.py

from car import Car
from capulet_engine import CapuletEngine
from spindler_battery import SpindlerBattery
from carrigan_tire import CarriganTire


class Calliope(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, current_date, tire_wear):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(tire_wear)
        super().__init__(engine, battery, tires)
