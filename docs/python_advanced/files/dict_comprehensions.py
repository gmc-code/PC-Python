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

product_ratings = {"laptop": [4.5, 4.7, 4.6], "phone": [4.8, 4.9, 4.7], "tablet": [4.2, 4.3]}
average_ratings = {product: round(sum(ratings) / len(ratings), 1) for product, ratings in product_ratings.items()}
print(average_ratings)
# Output is {'laptop': 4.6, 'phone': 4.8, 'tablet': 4.2}

city_temperatures = {"Sydney": [25, 27, 26], "Melbourne": [20, 22, 21], "Brisbane": [28, 30, 29]}
average_temperatures = {city: (min(temps), max(temps)) for city, temps in city_temperatures.items()}
print(average_temperatures)
# {'Sydney': (25, 27), 'Melbourne': (20, 22), 'Brisbane': (28, 30)}

employee_salaries = {'engineering': [170000, 150000, 124000], 'marketing': [120000, 114000, 102000], 'sales': [100000, 84000]}
average_salaries = {department: round(sum(salaries) / len(salaries)) for department, salaries in employee_salaries.items()}
print(average_salaries)
# {'engineering': 148000, 'marketing': 112000, 'sales': 92000}

workout_durations = {"running": [30, 35, 40], "cycling": [45, 50, 55], "swimming": [25, 30]}
average_durations = {activity: max(durations) for activity, durations in workout_durations.items()}
print(average_durations)
# {'running': 40, 'cycling': 55, 'swimming': 30}

employee_reviews = {
    "John": {"communication": [4.5, 4.7, 4.8], "technical": [4.2, 4.3], "leadership": [4.8, 4.9]},
    "Jane": {"communication": [4.8, 4.9], "technical": [4.6, 4.7, 4.8], "creativity": [4.9, 5.0]},
    "Doe": {"technical": [4.1, 4.3], "leadership": [4.5, 4.6, 4.7], "teamwork": [4.8, 4.9]},
}

# Function to calculate average score for each skill
def average_scores(reviews):
    return {employee: {skill: round(sum(scores)/len(scores),1) for skill, scores in skills.items()} for employee, skills in reviews.items()}

print(average_scores(employee_reviews))

#

fitness_data = {
    "Alice": {"steps": [10000, 12000, 11000], "calories_burned": [500, 550, 520], "active_minutes": [60, 70, 65]},
    "Bob": {"steps": [8000, 8500, 9000], "calories_burned": [400, 420, 450], "active_minutes": [50, 55, 60]},
    "Charlie": {"steps": [12000, 13000, 12500], "calories_burned": [600, 650, 620], "active_minutes": [75, 80, 78]},
}

# Function to calculate total data values for each category using dict comprehension
def total_data_by_category(data):
    return {
        "total_steps": {person: sum(info["steps"]) for person, info in data.items()},
        "total_calories_burned": {person: sum(info["calories_burned"]) for person, info in data.items()},
        "total_active_minutes": {person: sum(info["active_minutes"]) for person, info in data.items()}
    }

print(total_data_by_category(fitness_data))
# Output: {'total_steps': {'Alice': 33000, 'Bob': 25500, 'Charlie': 37500}, 
#          'total_calories_burned': {'Alice': 1570, 'Bob': 1270, 'Charlie': 1870}, 
#          'total_active_minutes': {'Alice': 195, 'Bob': 165, 'Charlie': 233}}


trees = [
    {'species': 'Oak', 'growth_rate': [2.5, 2.7, 2.6]},  # in cm per year
    {'species': 'Pine', 'growth_rate': [3.0, 3.2, 3.1]},
    {'species': 'Maple', 'growth_rate': [2.8, 2.9, 2.85]}
]

# Function to calculate the average growth rate for each tree species
def average_growth(data):
    return {tree['species']: round(sum(tree['growth_rate']) / len(tree['growth_rate']), 1) for tree in data}

print(average_growth(trees))
# Output: {'Oak': 2.6, 'Pine': 3.1, 'Maple': 2.9}



elements = [
    {'name': 'Hydrogen', 'atomic_number': 1, 'atomic_mass': 1.008, 'electronegativity': 2.20},
    {'name': 'Oxygen', 'atomic_number': 8, 'atomic_mass': 15.999, 'electronegativity': 3.44},
    {'name': 'Carbon', 'atomic_number': 6, 'atomic_mass': 12.011, 'electronegativity': 2.55}
]

# Using dictionary comprehension to create a dictionary of element names and their electronegativities
element_electronegativities = {element['name']: element['electronegativity'] for element in elements}

print(element_electronegativities)
# Output: {'Hydrogen': 2.20, 'Oxygen': 3.44, 'Carbon': 2.55}



#
