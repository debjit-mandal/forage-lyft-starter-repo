# test_new_functionality.py

import unittest
from datetime import datetime, timedelta
from spindler_battery import SpindlerBattery
from carrigan_tire import CarriganTire
from octoprime_tire import OctoprimeTire


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = datetime.today().date() - timedelta(days=3*365 + 1)
        current_date = datetime.today().date()
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = datetime.today().date() - timedelta(days=3*365 - 1)
        current_date = datetime.today().date()
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.8, 0.9, 0.7, 0.6]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.8, 0.8, 0.7, 0.6]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.8, 0.9, 0.8, 0.7]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.8, 0.8, 0.8, 0.5]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
