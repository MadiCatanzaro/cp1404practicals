"""
Unreliable Car Test
"""

from unreliable_car import UnreliableCar

unreliable_car1 = UnreliableCar('Albert', 100, 25)
unreliable_car2 = UnreliableCar('Beatrice', 100, 50)
unreliable_car3 = UnreliableCar('Camilla', 100, 75)
unreliable_car4 = UnreliableCar('Dunkin', 100, 100)

# Test the drive method over a large series of tests (1-99) to evaluate the effect the reliability value has on a cars
# ability to drive.
for i in range(1, 100):
    print(f"Car 1 Test {i}: {unreliable_car1.drive(50)}")
    print(f"Car 2 Test {i}: {unreliable_car2.drive(50)}")
    print(f"Car 3 Test {i}: {unreliable_car3.drive(50)}")
    print(f"Car 4 Test {i}: {unreliable_car4.drive(50)}")
    print('\n')
    # Reset the fuel values to 100 so the tests are both fair and valid each time
    unreliable_car1.fuel = 100
    unreliable_car2.fuel = 100
    unreliable_car3.fuel = 100
    unreliable_car4.fuel = 100

# Based on the tests it is evident the cars drive further the higher the reliability value. This is supported by the
# evidence that Car 4 always drives (as expected), and the remaining cars drive, however have cases where they do not
# drive, with Car 1 having the most instances of this scenario.
