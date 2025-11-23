"""
Taxi Simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Main function for Taxi Simulator."""
    print("Let's drive!")
    print(MENU)
    taxis = [Taxi('Prius', 100), SilverServiceTaxi('Limo', 100, 2), SilverServiceTaxi('Hummer', 200, 4)]
    current_taxi = None
    total_bill = 0
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'C':
            print('Taxis available:')
            display_taxis(taxis)
            try:
                chosen_taxi = int(input("Choose taxi: "))
                current_taxi = taxis[chosen_taxi]
            except IndexError:
                print("Invalid taxi choice")
            print(f"Bill to date: ${total_bill:.2f}")
        elif choice == 'D':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print(f"Bill to date: ${total_bill:.2f}")
            else:
                current_taxi.start_fare()
                driving_distance = float(input("Drive how far? "))
                current_taxi.drive(driving_distance)
                print(f"Your {current_taxi.name} trip costs you ${current_taxi.get_fare():.2f}")
                total_bill += current_taxi.get_fare()
                print(f"Bill to date: ${total_bill:.2f}")
        else:
            print("Invalid option")
            print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the list of taxis and their updated values."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
