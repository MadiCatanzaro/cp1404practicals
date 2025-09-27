"""
Score Menu
"""

MENU = """
G - Get a valid score (must be 0-100 inclusive)
P - Print result
S - Show stars
Q - Quit
"""


def main():
    score = get_valid_score()
    print(MENU)
    choice = input("> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == 'S':
            show_stars(score)
        else:
            print("Invalid input please try again")
        print(MENU)
        choice = input("> ").upper()
    print("Thank you, farewell")


def get_valid_score():
    score = float(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score, must be a value between 0 and 100")
        score = float(input("Score: "))
    return score


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print('*' * int(score))


main()
