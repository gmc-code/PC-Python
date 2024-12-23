eastern_state_capitals = {
                'Victoria': 'Melbourne',
                'New South Wales': 'Sydney',
                'Queensland': 'Brisbane'
                }
capital = eastern_state_capitals['Victoria']
print(capital)

eastern_state_capitals = {
                'Vic': 'Melbourne',
                'VIC': 'MELB',
                }
print(eastern_state_capitals['Vic'])
print(eastern_state_capitals['VIC'])

# ===============================================
sample_dict = {'a': 1, 'b': 2, 'c': 3}
value = sample_dict.get('a')
print(value)
# Output is 1
value = sample_dict.get('d')
print(value)
# Output is None
value = sample_dict.get('d', 0)
print(value)
# Output is 0

sample_dict = {'a': 1, 'b': 2, 'c': 3}
value = sample_dict['a']
print(value)
# Output is 1
# value = sample_dict['d']
# print(value)
# Output is Error message KeyError: 'd'


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


# =========================================



import copy

# Original dictionary with various types of values
original_dict = {
    'a': 'string',          # String
    'b': 42,                # Integer
    'c': (1, 2, 3),         # Tuple
    'd': [4, 5, 6],         # List
    'e': {'key': 'value'}   # Dictionary
}

# Create a shallow copy
shallow_copy = original_dict.copy()

# the mutable objects will not change in the original
shallow_copy['a'] = 'new_string'
shallow_copy['b'] = 100
shallow_copy['c'] = (7, 8, 9)
# the mutable objects will change in the original
shallow_copy['d'].append(7)
shallow_copy['e']['key'] = 'new_value'

print("Original Dictionary:", original_dict)
# Output: {'a': 'string', 'b': 42, 'c': (1, 2, 3), 'd': [4, 5, 6, 7], 'e': {'key': 'new_value'}}
print("Shallow Copy:", shallow_copy)
# Output: {'a': 'new_string', 'b': 100, 'c': (7, 8, 9), 'd': [4, 5, 6, 7], 'e': {'key': 'new_value'}}


import copy

# Original dictionary with various types of values
original_dict = {
    'a': 'string',          # String
    'b': 42,                # Integer
    'c': (1, 2, 3),         # Tuple
    'd': [4, 5, 6],         # List
    'e': {'key': 'value'}   # Dictionary
}

# Create a deep copy
deep_copy = copy.deepcopy(original_dict)

# Modify the values in the deep copy
deep_copy['a'] = 'new_string'
deep_copy['b'] = 100
deep_copy['c'] = (7, 8, 9)
deep_copy['d'].append(7)
deep_copy['e']['key'] = 'new_value'

print("Original Dictionary:", original_dict)
# Output: {'a': 'string', 'b': 42, 'c': (1, 2, 3), 'd': [4, 5, 6], 'e': {'key': 'value'}}
print("Deep Copy:", deep_copy)
# Output: {'a': 'new_string', 'b': 100, 'c': (7, 8, 9), 'd': [4, 5, 6, 7], 'e': {'key': 'new_value'}}

#==============================================

keys = ('a', 'b', 'c')
value = 0
new_dict = dict.fromkeys(keys, value)
print(new_dict)
# Output is {'a': 0, 'b': 0, 'c': 0}

# ==============================================

# Example 1: Create a dictionary with keys from coordinates_dict and a default value
keys = ('x', 'y', 'z')
value = 0
coordinates_dict = dict.fromkeys(keys, value)
print(coordinates_dict)
# Output is {'x': 0, 'y': 0, 'z': 0}

# Example 2: Create a dictionary with keys from fruits_dict and a default value
keys = ('apple', 'banana', 'cherry')
value = 'unknown'
fruits_dict = dict.fromkeys(keys, value)
print(fruits_dict)
# Output is {'apple': 'unknown', 'banana': 'unknown', 'cherry': 'unknown'}

# Example 3: Create a dictionary with keys from colors_dict and a default value
keys = ('red', 'green', 'blue')
value = '#FFFFFF'
colors_dict = dict.fromkeys(keys, value)
print(colors_dict)
# Output is {'red': '#FFFFFF', 'green': '#FFFFFF', 'blue': '#FFFFFF'}

# Example 4: Create a dictionary with keys from animals_dict and a default value
keys = ('cat', 'dog', 'bird')
value = 'sound'
animals_dict = dict.fromkeys(keys, value)
print(animals_dict)
# Output is {'cat': 'sound', 'dog': 'sound', 'bird': 'sound'}

# ==========================


