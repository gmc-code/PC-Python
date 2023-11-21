import csv
from collections import Counter

csv_path = 'files/afl_premiers_2000s.csv'

# Read data from CSV file
with open(csv_path, 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Load data into a dictionary
team_dict = {}
for row in data:
    if row['Premiership team'] not in team_dict:
        team_dict[row['Premiership team']] = 0
    team_dict[row['Premiership team']] += 1
    # if row['Runner-up'] not in team_dict:
    #     team_dict[row['Runner-up']] = 0
    # team_dict[row['Runner-up']] += 1

# Sort the dictionary by values in descending order
sorted_teams = sorted(team_dict.items(), key=lambda x: x[1], reverse=True)

# # Print out the team name and its count in descending order
for team, count in sorted_teams:
    print(f'{count} {team}')


# Print out the team name and its count in descending order with enumeration
# for i, (team, count) in enumerate(sorted_teams, start=1):
#     print(f'{i}. {count} {team}')
