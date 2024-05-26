# spindler_battery.py
from serviceable import Serviceable
from datetime import datetime


class SpindlerBattery(Serviceable):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 2)
        return self.current_date > service_threshold_date
