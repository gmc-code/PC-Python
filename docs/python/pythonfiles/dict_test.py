state_capitals = {
                'Victoria': "Melbourne",
                'Tasmania': "Hobart",
                'Queensland': "Brisbane"
                }
print(state_capitals)
# --------------------
state_capitals = dict([
    ["New South Wales", "Sydney"],
    ["Victoria", "Melbourne"],
    ["Queensland", "Brisbane"]
])
print(state_capitals)
# --------------------
capitals = dict([
    ("South Australia", "Adelaide"),
    ("Western Australia", "Perth"),
    ("Australian Capital Territory", "Canberra")
])
print(capitals)
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
