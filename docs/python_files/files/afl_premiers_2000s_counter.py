import csv

def process_data(csv_path):
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

    # Sort the dictionary by values in descending order
    sorted_teams = sorted(team_dict.items(), key=lambda x: x[1], reverse=True)

    # Create a string with the team name and its count in descending order
    output = '\n'.join([f'{count} {team}' for team, count in sorted_teams])

    # Return the output string
    return output

csv_path = 'files/afl_premiers_2000s.csv'
print(process_data(csv_path))

