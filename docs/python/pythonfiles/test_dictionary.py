eastern_state_capitals = {
                'Victoria': 'Melbourne',
                'New South Wales': 'Sydney',
                'Queensland': 'Brisbane'
                }
capital = eastern_state_capitals['Victoria']
print(capital)

# --------------------
state_capitals = dict([
    ["New South Wales", "Sydney"],
    ["Victoria", "Melbourne"],
    ["Queensland", "Brisbane"]
])
print(state_capitals)
# {'New South Wales': 'Sydney', 'Victoria': 'Melbourne', 'Queensland': 'Brisbane'}
# --------------------
capitals = dict([
    ("South Australia", "Adelaide"),
    ("Western Australia", "Perth"),
    ("Australian Capital Territory", "Canberra")
])
print(capitals)
# {'South Australia': 'Adelaide', 'Western Australia': 'Perth', 'Australian Capital Territory': 'Canberra'}
# --------------------
states = ["Queensland", "South Australia", "Western Australia"]
cities = ["Brisbane", "Adelaide", "Perth"]
capitals = dict(zip(states, cities))
print(capitals)
# --------------------
states = ["Western Australia", "Tasmania", "Northern Territory"]
cities = ["Perth", "Hobart", "Darwin"]
capitals = {state: city for state, city in zip(states, cities)}
print(capitals)


simple_dict = dict(a=1, b=2, c=3, d=4)
print(simple_dict)

"""
my_dict = {'y': 'triangle', 'x': 'square', 'z': 'pentagon'}
my_dict_sorted_list = sorted(my_dict)
print(my_dict_sorted_list)
"""

states = ["Western Australia", "Tasmania", "Northern Territory"]
cities = ["Perth", "Hobart", "Darwin"]

capitals = {}
for i in range(len(states)):
    capitals[states[i]] = cities[i]

print(capitals)

# ----------------------

states = ["Queensland", "South Australia", "Western Australia"]
cities = ["Brisbane", "Adelaide", "Perth"]

capitals = {}
for i in range(len(states)):
    capitals[states[i]] = cities[i]
print(capitals)
# {'Queensland': 'Brisbane', 'South Australia': 'Adelaide', 'Western Australia': 'Perth'}

simple_dict = dict(a=1, b=2, c=3, d=4)
print(simple_dict)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

continents = dict(Africa=30.37, Asia=44.58, Europe=10.18)
print(continents)
# {'Africa': 30.37, 'Asia': 44.58, 'Europe': 10.18}

languages_release_years = dict(Python=1991, Java=1995, JavaScript=1995)
print(languages_release_years)
# {'Python': 1991, 'Java': 1995, 'JavaScript': 1995}