pet = {"type": "dog", "name": "Buddy", "age": 3, "color": "brown"}

# Removes "age" and stores its value (3) in a variable
removed_age = pet.pop("age")  # Result: {"type": "dog", "name": "Buddy", "color": "brown"}
print(removed_age)
print(pet)

# Deletes the key "color" and its value
del pet["color"]              # Result: {"type": "dog", "name": "Buddy"}
print(pet)

# Removes the last inserted item ("name": "Buddy")
last_removed = pet.popitem()     # Result: {"type": "dog"}
print(last_removed)
print(pet)

# Wipes all key-value pairs from the dictionary
pet.clear()                   # Result: {}
print(pet)