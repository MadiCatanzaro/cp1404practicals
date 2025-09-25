"""
Sequences
"""

MENU = """
1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program
"""

x = int(input("Please enter value for x: "))
y = int(input("Please enter value for y: "))

option = input("Please choose an option (1,2,3,4): ")
while option != '4':
    if option == '1':
        if x % 2 == 0:
            for i in range(x, y, 2):
                print(i, end=' ')
            print()
        else:
            for i in range(x + 1, y, 2):
                print(i, end=' ')
            print()
    elif option == '2':
        if x % 2 == 1:
            for i in range(x, y, 2):
                print(i, end=' ')
            print()
        else:
            for i in range(x + 1, y, 2):
                print(i, end=' ')
            print()
    elif option == '3':
        for i in range(x, y + 1):
            print(i ** 2, end=' ')
        print()
    else:
        print("Invalid Option")
    option = input("Please choose an option (1,2,3,4): ")
print("Thank you for participating.")