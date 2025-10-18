"""
Wimbledon
Estimate: 40 minutes
Actual: 42 minutes
"""


def main():
    champion_to_times_won = {}
    countries = []
    with open('wimbledon.csv', "r", encoding='utf-8-sig') as in_file:
        in_file.readline()
        for line in in_file:
            wimbledon = line.split(',')
            count_winning_players(champion_to_times_won, wimbledon)
            get_countries(wimbledon, countries)
        display_champions(champion_to_times_won)
        display_winning_countries(countries)


def count_winning_players(champion_to_times_won, wimbledon):
    player = wimbledon[2]
    if player in champion_to_times_won:
        champion_to_times_won[player] += 1
    else:
        champion_to_times_won[player] = 1


def get_countries(wimbledon, countries):
    country = wimbledon[1]
    countries.append(country)
    return countries


def display_champions(champion_to_times_won):
    print("Wimbledon Champions:")
    for champion, times_won in champion_to_times_won.items():
        print(f"{champion} {times_won}")


def display_winning_countries(countries):
    print("")  # blank line
    winning_countries = sorted(set(countries))
    print(f"These {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(winning_countries))


main()
