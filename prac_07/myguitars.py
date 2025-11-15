"""
My Guitars
"""

from guitar import Guitar


def main():
    """Main guitars function; displaying guitars, sorting guitars, adding new guitars, and saving guitars to file."""
    guitars = process_guitars()
    display_guitars(guitars)

    display_sorted_guitars(guitars)

    get_new_guitars(guitars)
    save_guitars_to_file(guitars)


def display_sorted_guitars(guitars):
    """Sort guitars and display them."""
    print("\nGuitars sorted by year: ")
    for guitar in sorted(guitars):
        print(guitar)


def save_guitars_to_file(guitars):
    """Save guitars to file in the appropriate format."""
    out_file = open("guitars.csv", "w")
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()
    print("Guitars successfully saved to 'guitars.cvs'")


def get_new_guitars(guitars):
    """Add a new guitar; name, year, cost to the list of guitars."""
    print("\nAdd a new guitar")
    user_guitar = input("Guitar: ")
    while user_guitar != "":
        user_year = int(input("Year: "))
        user_cost = float(input("Cost: $"))
        guitar = Guitar(user_guitar, user_year, user_cost)
        guitars.append(guitar)
        user_guitar = input("Guitar: ")


def display_guitars(guitars):
    """Display guitars."""
    print("Guitars:")
    for guitar in guitars:
        print(guitar)


def process_guitars():
    """Read guitars from a file and process them into an appropriate form."""
    guitars = []
    in_file = open("guitars.csv", 'r')
    for line in in_file:
        parts = line.strip().split(',')
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(parts[0], year, cost)
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
