names = ['Lockett', 'Coventry', 'Dunstall']
goals = [1360, 1299, 1254]
print(dict(zip(names, goals)))
# {'Lockett': 1360, 'Coventry': 1299, 'Dunstall': 1254}

my_dict = {}
for name, goal in zip(names, goals):
    my_dict[name] = goal
print(my_dict)
# {'Lockett': 1360, 'Coventry': 1299, 'Dunstall': 1254}

my_dict_comprehension = {name: goal for (name, goal) in zip(names, goals)}
print(my_dict_comprehension)
# {'Lockett': 1360, 'Coventry': 1299, 'Dunstall': 1254}

my_dict_comprehension = {name: goal for (name, goal) in zip(names, goals) if goal > 1275}
print(my_dict_comprehension)
# {'Lockett': 1360, 'Coventry': 1299}

new_dict = {n: 2 * n for n in range(5)}
print(new_dict)

numbers = range(1, 10)
# Dictionary comprehension with a condition
squared_evens = {num: num ** 2 for num in numbers if num % 2 == 0}
print(squared_evens)
# Output: {2: 4, 4: 16, 6: 36, 8: 64}


names = ['Alex', 'Brooke', 'Chris', 'Dana']
scores = [85, 92, 78, 90]

# Dictionary comprehension with a condition
high_scores = {name: score for name, score in zip(names, scores) if score > 80}
print(high_scores)
# Output: {'Alex': 85, 'Brooke': 92, 'Dana': 90}
