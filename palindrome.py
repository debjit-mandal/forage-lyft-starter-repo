# palindrome.py
from car import Car
from sternman_engine import SternmanEngine
from spindler_battery import SpindlerBattery


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_on, current_date):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        super().__init__(engine, battery)
