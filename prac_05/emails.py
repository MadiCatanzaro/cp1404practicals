"""
Emails
Estimate: 30 minutes
Actual: Approximately 45 minutes
"""


def main():
    """Take user input and display the corresponding name and email."""
    email_to_name = {}
    email = input("Email: ")
    while email != '':
        name = evaluate_name_from_email(email)
        email_to_name[email] = name
        check_name(email, email_to_name, name)
        email = input("Email: ")
    display_names(email_to_name)


def check_name(email, email_to_name, name):
    print(f"Is your name {name}? (Y/n)")
    name_check = input("")
    if 'n' or 'N' in name_check:  # accommodate for any type of 'no'
        name = input("Name: ").title()
        email_to_name[email] = name


def evaluate_name_from_email(email):
    """Convert the email to its equivalent name."""
    name1 = email.split('@')[0]
    if '.' in name1:
        name2 = " ".join(name1.split('.'))
        return str(name2).title()
    else:
        return str(name1).title()


def display_names(email_to_name):
    """Display the correct names to the corresponding email address."""
    print("")  # blank line
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
