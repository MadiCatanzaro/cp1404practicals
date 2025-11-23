"""
Unreliable Car Class
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of car which includes reliability score."""

    def __init__(self, name='', fuel=0.00, reliability=0.00):
        """Initialise unreliable car class."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Return the distance driven using the previous car drive method if a random number (0-100) is less than the
        reliability value, otherwise set the distance driven to zero."""
        number = randint(0, 100)
        if number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
