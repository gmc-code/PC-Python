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
