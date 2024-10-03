
premiers = {"ESS":16, "COLL":16, "CARL":16,
            "MELB":13, "RICH":13, "HAW":13, "GEE":10}



print("=========ALL===========")
teams = premiers.keys()
for team in teams:
    print(team, premiers.get(team))

print("===========FAVS=========")
fav_teams = ["MELB", "RICH", "HAW"]
for team in fav_teams:
    print(team, premiers.get(team))

print("===========using keys of the dictionary automatically in a for loop=========")
for premier_key in premiers:
    print(premier_key, premiers.get(premier_key))

print("==========use items method==========")
for premier_key, premierships_value in premiers.items():
    print(premier_key, premierships_value)
