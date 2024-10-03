import random

# Nested dictionary, keys are the year in quotes
# Values are dictionaries with keys "premier" and "runner-up"
afl_grand_finals = {
    "2024": {"premier": "Brisbane Lions", "runner-up": "Sydney Swans"},
    "2023": {"premier": "Collingwood", "runner-up": "Brisbane Lions"},
    "2022": {"premier": "Geelong", "runner-up": "Sydney Swans"},
    "2021": {"premier": "Melbourne", "runner-up": "Western Bulldogs"}
}

while True:
    # Randomly select a year and a key
    year = random.choice(list(afl_grand_finals.keys()))
    key = random.choice(["premier", "runner-up"])

    # Get the team based on the random year and key
    team = afl_grand_finals[year][key]
    print(f"The {key} of {year} is {team}.")

    # Ask the user if they want to continue or exit
    user_input = input("Do you want to continue? (Y/N): ").strip().upper()
    if user_input != "Y":
        print("Exiting the program.")
        break

