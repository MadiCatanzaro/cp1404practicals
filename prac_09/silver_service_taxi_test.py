"""
Silver Service Taxi Test
"""

from silver_service_taxi import SilverServiceTaxi

silver_taxi = SilverServiceTaxi()

# Assertion tests for default values
assert silver_taxi.name == ""
assert silver_taxi.fuel == 0.00

silver_taxi = SilverServiceTaxi('Silver', 100, 2)
print(silver_taxi)
silver_taxi.drive(18)
print(f"Fare: ${(silver_taxi.get_fare()):.2f}")

# Assertion test for fare calculation (using rounded result of 48.80 as opposed to 48.78)
assert silver_taxi.get_fare() == 48.80

print(silver_taxi)  # check whether current fare distance is updated

hummer = SilverServiceTaxi('Hummer', 200, 4)
print(hummer)
