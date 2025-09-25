"""
Password Stars
"""

MINIMUM_LENGTH = 8


def main():
    password = get_password()

    while len(password) < MINIMUM_LENGTH:
        print(f"Password does not meet the minimum length requirement of {MINIMUM_LENGTH} characters.")
        password = get_password()
    print_password(password)


def print_password(password):
    print('*' * len(password))


def get_password():
    password = input("Password: ")
    return password


main()
