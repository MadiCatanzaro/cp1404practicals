"""
Password Stars
"""

password = input("Password: ")
minimum_length = 8

while len(password) < minimum_length:
    print(f"Password does not meet the minimum length requirement of {minimum_length} characters.")
    password = input("Password: ")
print('*' * len(password))
