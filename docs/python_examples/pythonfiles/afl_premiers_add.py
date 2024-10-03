premiers = {"ESS": 16, "COLL": 16, "CARL": 16, "MELB": 13, "RICH": 13, "HAW": 13, "GEE": 10}

while True:
    user_team = input("What team (short name)? ").upper().strip()

    # Check if the input is valid (not empty and only letters)
    if not user_team.isalpha():
        print("Invalid input. Please enter a valid team short name consisting of letters only.")
        continue

    team_premierships = premiers.get(user_team)
    if team_premierships is None:
        print(f"{user_team} is not in the dictionary")
        while True:
            try:
                new_team_premierships = int(input("How many premierships have they won? "))
                break
            except ValueError:
                print("Please enter a valid number.")
        premiers[user_team] = new_team_premierships
        print(f"{user_team} has won {new_team_premierships} premierships.")
    else:
        print(f"{user_team} has won {team_premierships} premierships.")

    get_more_premiers = input("Press Enter to continue or any other key to exit: ").strip()
    if get_more_premiers != "":
        print("Exiting the program.\n")
        break

print(premiers)
