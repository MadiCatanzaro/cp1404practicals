"""
Silver Service Taxi Class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi which includes fanciness score used to calculate price per km."""
    flagfall = 4.50

    def __init__(self, name="", fuel=0.00, fanciness=0.00):
        """Initialise Silver Service Taxi class."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
        self.current_fare_distance = 0

    def __str__(self):
        """Return string representation of Silver Service Taxi class."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the calculated fare based on Taxi get_fare() method incorporating the flagfall value."""
        return super().get_fare() + self.flagfall
