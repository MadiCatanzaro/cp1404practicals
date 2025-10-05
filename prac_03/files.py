"""
Files
"""

# 1.
name = input("User name: ")
out_file = open("name.txt", 'w')
print(f"{name}", file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", 'r')
contents = in_file.read().strip()
print(f"Hi {contents}!")
in_file.close()

# 3.
with open("numbers.txt", 'r') as out_file:
    number_line1 = int(out_file.readline().strip())
    number_line2 = int(out_file.readline().strip())
    total = number_line1 + number_line2
    print(total)

# 4.
total = 0
with open("numbers.txt", 'r') as working_file:
    for line in working_file:
        number = int(line.strip())
        total = total + number
    print(total)
