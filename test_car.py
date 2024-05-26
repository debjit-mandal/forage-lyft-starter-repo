# test_car.py
import unittest
from datetime import datetime
from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    # Add more tests for each car


if __name__ == '__main__':
    unittest.main()
