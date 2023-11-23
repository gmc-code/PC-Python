import pandas as pd

def process_data(csv_path):
    # Use StringIO to read the string data into a pandas DataFrame
    df = pd.read_csv(csv_path)

    # Concatenate the 'Premiership team' and 'Runner-up' columns
    teams = pd.concat([df['Premiership team'], df['Runner-up']])

    # Use value_counts to get the number of times each team is listed
    team_counts = teams.value_counts()

    return(team_counts)


csv_path = 'files/afl_premiers_2000s.csv'
print(process_data(csv_path))

