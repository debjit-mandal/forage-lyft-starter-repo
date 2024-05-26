# car_factory.py
from calliope import Calliope
from glissade import Glissade
from palindrome import Palindrome
from rorschach import Rorschach
from thovex import Thovex
from datetime import datetime


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Calliope(last_service_date, current_mileage, last_service_mileage, current_date)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Glissade(last_service_date, current_mileage, last_service_mileage, current_date)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Palindrome(last_service_date, warning_light_on, current_date)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Rorschach(last_service_date, current_mileage, last_service_mileage, current_date)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Thovex(last_service_date, current_mileage, last_service_mileage, current_date)
