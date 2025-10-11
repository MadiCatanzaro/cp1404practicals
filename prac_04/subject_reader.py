"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    file_information = load_file_information(FILENAME)
    print(file_information)
    display_subject_details(file_information)


def load_file_information(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    processed_data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        processed_data.append(parts)
        print("----------")
    input_file.close()
    return processed_data


def display_subject_details(processed_data):
    """Generate contextual sentences using the processed data."""
    for line in processed_data:
        print(f"{line[0]} is taught by {line[1]} and has {line[2]} students.")


main()
