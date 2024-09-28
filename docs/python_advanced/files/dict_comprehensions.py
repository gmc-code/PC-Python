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

students = ['Alice', 'Bob', 'Charlie', 'David']
grades = [85, 72, 90, 65]
# Dictionary comprehension with a condition
student_grades = {student: grade for student, grade in zip(students, grades)}
print(student_grades)

numbers = range(1, 10)
# Dictionary comprehension with a condition
squared_evens = {num: num ** 2 for num in numbers}
print(squared_evens)

products = ['apple', 'banana', 'cherry', 'date']
prices = [15, 25, 10, 30]
# Dictionary comprehension with a condition
expensive_products = {product: price for product, price in zip(products, prices)}
print(expensive_products)

vehicles = ['car', 'bike', 'boat', 'plane']
types = ['land', 'land', 'water', 'air']
land_vehicles = {vehicle: vehicle_type for vehicle, vehicle_type in zip(vehicles, types)}
print(land_vehicles)



cities_in_F = {'Sydney': 86, 'Melbourne': 68, 'Brisbane': 95, 'Perth': 77}
cities_in_C = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)
# {'Sydney': 30, 'Melbourne': 20, 'Brisbane': 35, 'Perth': 25}


names = {'first': 'SHERLOCK', 'middle': 'HAMISH', 'surname': 'HOLMES'}
title_cased_names = {key.title(): value.title() for key, value in names.items()}
print(title_cased_names)
# {'First': 'Sherlock', 'Middle': 'Hamish', 'Surname': 'Holmes'}

string = "Python"
string_ascii = {char: ord(char) for char in string}
print(string_ascii)
# {'P': 80, 'y': 121, 't': 116, 'h': 104, 'o': 111, 'n': 110}

cities_in_F = {'Sydney': 19, 'Melbourne': 15, 'Brisbane': 35, 'Perth': 25}
cities_in_C = {key: "warm" if value > 20 else "cold" for (key, value) in cities_in_F.items()}
print(cities_in_C)
# Output is {'Sydney': 'cold', 'Melbourne': 'cold', 'Brisbane': 'warm', 'Perth': 'warm'}

def categorise_temp(temp_C):
    if temp_C > 30:
        return "hot"
    elif temp_C > 20:
        return "warm"
    elif temp_C > 10:
        return "cold"
    else:
        return "freezing"


cities_in_F = {'Sydney': 14, 'Melbourne': 6, 'Brisbane': 35, 'Perth': 25}
cities_in_C = {key: categorise_temp(value) for (key, value) in cities_in_F.items()}
print(cities_in_C)
# Output is {'Sydney': 'cold', 'Melbourne': 'freezing', 'Brisbane': 'hot', 'Perth': 'warm'}



car_speeds_kph = {'Hennessey Venom F5': 484, 'Koenigsegg Agera RS': 447, 'McLaren 720S': 341, 'Chevrolet Corvette C8': 312, 'Honda Civic': 201}

speed_category = {key: ("super fast" if value > 350 else "fast" if value > 250 else "slow") for (key, value) in car_speeds_kph.items()}
print(speed_category)
# Output:  {'Hennessey Venom F5': 'super fast', 'Koenigsegg Agera RS': 'super fast', 'McLaren 720S': 'fast', 'Chevrolet Corvette C8': 'fast', 'Honda Civic': 'slow'}



animal_weights_kg = {'Koala': 10, 'Kangaroo': 90, 'Lion': 190, 'Zebra': 350, 'Giraffe': 1200, 'Elephant': 5400}
weight_category = {key: ("heavy" if value > 1000 else "medium" if value > 100 else "light") for key, value in animal_weights_kg.items()}
print(weight_category)
# Output: {'Koala': 'light', 'Kangaroo': 'light', 'Lion': 'medium', 'Zebra': 'medium', 'Giraffe': 'heavy', 'Elephant': 'heavy'}



#
