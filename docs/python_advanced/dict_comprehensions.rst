==========================
Dictionary Comprehensions
==========================

| See docs at: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
| See ref video at: https://youtu.be/3dt4OGnU5sM?feature=shared&t=738

----

Dictionary comprehension
---------------------------

| Dictionary comprehensions provide a concise way to create dictionaries. 
| They are used to make new dictionaries where each key-value pair is the result of some operations applied to each member of another sequence (e.g. list, range function) or iterable (e.g. list, zip of 2 lists, dictionary).
| They can also create a sub-sequence of those elements that satisfy a certain condition.

| A dictionary comprehension consists of braces containing an expression followed by a for-clause. 
| The result will be a new dictionary created by evaluating the expression in the context of the for-clauses which follow it. 

----

Dictionary comprehension of the range function, lists and strings
----------------------------------------------------------------------

.. py:function:: new_dictionary = {key: value for item in iterable}

    :param key: the key variable only, (e.g. n), or any expression such as one that uses the item variable.
    :param value: the value variable only or any expression such as one that uses the item variable (e.g. 2 * n).
    :param item:  a variable that gets each item in the iterable.
    :param iterable: iterable objects like strings, lists, and range function.

| The code below uses n with values of 0 to 4 to make a dictionary with values that are the keys doubled.

.. code-block:: python
    
    new_dict = {n: 2 * n for n in range(5)}
    print(new_dict)
    # output is {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}


Practice Questions
--------------------

.. admonition:: Tasks

    #. Using a range function, create a dictionary comprehension that maps numbers from 0 to 9 to their squares. Print the dictionary.
    #. Create a dictionary comprehension that maps the names of fruits, 'apple', 'banana', 'cherry', and 'date', to their lengths. Print the dictionary.
    #. Create a dictionary comprehension that maps the names of the days of the week, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', and 'Sunday', to their first three letters in uppercase. Print the dictionary.
    #. Create a dictionary comprehension that maps the first three letters in uppercase of the days of the week to their full names. Print the dictionary.
    #. Create a dictionary comprehension that maps the names of the months of the year, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', and 'December', to their first three letters in uppercase. Print the dictionary.
    #. Create a dictionary comprehension that maps the first three letters in uppercase of the months of the year to their full names. Print the dictionary.
    #. Use a dictionary comprehension that maps each character in the string "Python" to its ASCII values. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Using a range function, create a dictionary comprehension that maps the even numbers from 2 to 8 to their squares. Print the dictionary.

                .. code-block:: python

                    numbers = range(2, 10, 2)
                    # Dictionary comprehension with a condition
                    squared_evens = {num: num ** 2 for num in numbers}
                    print(squared_evens)
                    # Output: {2: 4, 4: 16, 6: 36, 8: 64}

            .. tab-item:: Q2

                Create a dictionary comprehension that maps the names of fruits, 'apple', 'banana', 'cherry', and 'date', to their lengths. Print the dictionary.

                .. code-block:: python

                    fruits = ['apple', 'banana', 'cherry', 'date']
                    fruit_lengths = {fruit: len(fruit) for fruit in fruits}
                    print(fruit_lengths)
                    # Output: {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}

            .. tab-item:: Q3

                Create a dictionary comprehension that maps the names of the days of the week, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', and 'Sunday', to their first three letters in uppercase. Print the dictionary.

                .. code-block:: python

                    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                    abbreviated_days = {day: day[:3].upper() for day in days}
                    print(abbreviated_days)
                    # Output: {'Monday': 'MON', 'Tuesday': 'TUE', 'Wednesday': 'WED', 'Thursday': 'THU', 'Friday': 'FRI', 'Saturday': 'SAT', 'Sunday': 'SUN'}

            .. tab-item:: Q4

                Create a dictionary comprehension that maps the first three letters in uppercase of the days of the week to their full names. Print the dictionary.

                .. code-block:: python

                    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                    abbreviated_days = {day[:3].upper(): day for day in days}
                    print(abbreviated_days)
                    # Output: {'MON': 'Monday', 'TUE': 'Tuesday', 'WED': 'Wednesday', 'THU': 'Thursday', 'FRI': 'Friday', 'SAT': 'Saturday', 'SUN': 'Sunday'}

            .. tab-item:: Q5

                Create a dictionary comprehension that maps the names of the months of the year, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', and 'December', to their first three letters in uppercase. Print the dictionary.

                .. code-block:: python

                    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                    abbreviated_months = {month: month[:3].upper() for month in months}
                    print(abbreviated_months)
                    # Output: {'January': 'JAN', 'February': 'FEB', 'March': 'MAR', 'April': 'APR', 'May': 'MAY', 'June': 'JUN', 'July': 'JUL', 'August': 'AUG', 'September': 'SEP', 'October': 'OCT', 'November': 'NOV', 'December': 'DEC'}


            .. tab-item:: Q6

                Create a dictionary comprehension that maps the first three letters in uppercase of the months of the year to their full names. Print the dictionary.

                .. code-block:: python

                    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                    abbreviated_months = {month[:3].upper(): month for month in months}
                    print(abbreviated_months)
                    # Output: {'JAN': 'January', 'FEB': 'February', 'MAR': 'March', 'APR': 'April', 'MAY': 'May', 'JUN': 'June', 'JUL': 'July', 'AUG': 'August', 'SEP': 'September', 'OCT': 'October', 'NOV': 'November', 'DEC': 'December'}


            .. tab-item:: Q7

                Use a dictionary comprehension that maps each character in the string "Python" to its ASCII values. Print the dictionary.

                .. code-block:: python

                    string = "Python"
                    string_ascii = {char: ord(char) for char in string}
                    print(string_ascii)
                    # {'P': 80, 'y': 121, 't': 116, 'h': 104, 'o': 111, 'n': 110}

----

Dictionary comprehension of zipped lists
----------------------------------------------------------------------

| Zipping 2 lists produces a zip object which is like a list of tuples.
| The zipped object acts as an iterable for the dictionary comprehension. 

| Syntax:

.. py:function:: new_dictionary = {key: value for key, value in iterable}

    :param key: the key variable.
    :param value: the value variable.
    :param iterable: iterable objects like zip objects from 2 lists.

.. code-block:: python
    
    names = ['Lockett', 'Coventry', 'Dunstall']
    goals = [1360, 1299, 1254]
    my_dict_comprehension = {name: goal for (name, goal) in zip(names, goals)}
    print(my_dict_comprehension)
    # Output is {'Lockett': 1360, 'Coventry': 1299, 'Dunstall': 1254}

----

Practice Questions
--------------------

.. admonition:: Tasks

    #. Create a dictionary comprehension that maps the names of students, 'Alice', 'Bob', 'Charlie', and 'David', to their test scores: 85, 72, 90, and 65. Print the dictionary.
    #. Create a dictionary comprehension that maps the names of products, apple, banana, cherry, and date, to their prices: 15, 25, 10, and 30. Print the dictionary.
    #. Create a dictionary comprehension that maps the names of vehicles, 'car', 'bike', 'boat', and 'plane', to their types: 'land', 'land', 'water', and 'air'. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary comprehension that maps the names of students, 'Alice', 'Bob', 'Charlie', and 'David', to their test scores: 85, 72, 90, and 65. Print the dictionary.

                .. code-block:: python

                    students = ['Alice', 'Bob', 'Charlie', 'David']
                    test_scores = [85, 72, 90, 65]
                    # Dictionary comprehension with a condition
                    student_test_scores = {student: score for student, score in zip(students, test_scores)}
                    print(student_test_scores)
                    # Output: {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 65}

            .. tab-item:: Q2

                Create a dictionary comprehension that maps the names of products, apple, banana, cherry, and date, to their prices: 15, 25, 10, and 30 dollars. Print the dictionary.

                .. code-block:: python

                    products = ['apple', 'banana', 'cherry', 'date']
                    prices = [15, 25, 10, 30]
                    # Dictionary comprehension with a condition
                    expensive_products = {product: price for product, price in zip(products, prices)}
                    print(expensive_products)
                    # Output: {'apple': 15, 'banana': 25, 'cherry': 10, 'date': 30}

            .. tab-item:: Q3

                Create a dictionary comprehension that maps the names of vehicles, 'car', 'bike', 'boat', and 'plane', to their types: 'land', 'land', 'water', and 'air'. Print the dictionary.

                .. code-block:: python

                    vehicles = ['car', 'bike', 'boat', 'plane']
                    types = ['land', 'land', 'water', 'air']
                    land_vehicles = {vehicle: vehicle_type for vehicle, vehicle_type in zip(vehicles, types)}
                    print(land_vehicles)
                    # Output: {'car': 'land', 'bike': 'land', 'boat': 'water', 'plane': 'air'}

----

Using a condition in a dictionary comprehension
----------------------------------------------------------

Syntax:

.. py:function:: new_dictionary = {key: value for item in iterable if condition}
.. py:function:: high_scores = {key: value for key, value in iterable if condition}

    :param key: the key variable only or any expression such as one that uses the item variable (e.g. n).
    :param value: the value variable only or any expression such as one that uses the item variable (e.g. 2 * n).
    :param item:  a variable that gets each item in the iterable.
    :param iterable: iterable objects like strings, lists, dictionaries, range function and others.
    :param condition: a condition that resolves to True or False.

.. code-block:: python

    names = ['Alex', 'Brooke', 'Chris', 'Dana']
    scores = [85, 92, 78, 90]
    # Dictionary comprehension with a condition
    high_scores = {name: score for name, score in zip(names, scores) if score > 80}
    print(high_scores)
    # Output: {'Alex': 85, 'Brooke': 92, 'Dana': 90}

----

Practice Questions
--------------------

.. admonition:: Tasks

    #. Create a dictionary comprehension that maps the names of students, Alice, Bob, Charlie, and David, to their test_scores: 85, 72, 90, and 65, but only include students who scored above 75. Print the dictionary.
    #. Create a dictionary comprehension that maps the names of products, apple, banana, cherry, and date, to their prices: 15, 25, 10, and 30, but only include products that cost more than $20. Print the dictionary.
    #. Create a dictionary comprehension that maps the names of vehicles, 'car', 'bike', 'boat', and 'plane', to their types: 'land', 'land', 'water', and 'air', but only include vehicles that operate on land. Print the dictionary.
    #. Create a dictionary comprehension that maps numbers from 0 to 9 to their squares, but only include even numbers. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary comprehension that maps the names of students, Alice, Bob, Charlie, and David, to their test_scores: 85, 72, 90, and 65, but only include students who scored above 75. Print the dictionary.

                .. code-block:: python

                    students = ['Alice', 'Bob', 'Charlie', 'David']
                    test_scores = [85, 72, 90, 65]
                    # Dictionary comprehension with a condition
                    passed_students = {student: score for student, score in zip(students, test_scores) if score > 75}
                    print(passed_students)
                    # Output: {'Alice': 85, 'Charlie': 90}

            .. tab-item:: Q2

                Create a dictionary comprehension that maps the names of products, apple, banana, cherry, and date, to their prices: 15, 25, 10, and 30 dollars, but only include products that cost more than $20. Print the dictionary.

                .. code-block:: python

                    products = ['apple', 'banana', 'cherry', 'date']
                    prices = [15, 25, 10, 30]
                    # Dictionary comprehension with a condition
                    expensive_products = {product: price for product, price in zip(products, prices) if price > 20}
                    print(expensive_products)
                    # Output: {'banana': 25, 'date': 30}

            .. tab-item:: Q3

                Create a dictionary comprehension that maps the names of vehicles, 'car', 'bike', 'boat', and 'plane', to their types: 'land', 'land', 'water', and 'air', but only include vehicles that operate on land. Print the dictionary.

                .. code-block:: python

                    vehicles = ['car', 'bike', 'boat', 'plane']
                    types = ['land', 'land', 'water', 'air']
                    land_vehicles = {vehicle: vehicle_type for vehicle, vehicle_type in zip(vehicles, types) if vehicle_type == 'land'}
                    print(land_vehicles)
                    # Output: {'car': 'land', 'bike': 'land'}

            .. tab-item:: Q4

                Create a dictionary comprehension that maps numbers from 1 to 9 to their squares, but only include even numbers. Print the dictionary.

                .. code-block:: python

                    numbers = range(1, 10)
                    # Dictionary comprehension with a condition
                    squared_evens = {num: num ** 2 for num in numbers if num % 2 == 0}
                    print(squared_evens)
                    # Output: {2: 4, 4: 16, 6: 36, 8: 64}

----

Dictionary comprehension of dictionaries
----------------------------------------------------------------------

Syntax:

.. py:function:: new_dictionary = {key: value_expression for key, value in dictionary.items()}

    :param key: the key variable.
    :param value: the value variable.
    :param value_expression: an expression based on the value variable.
    :param dictionary: starting dictionary with keys and values ot be used.

| This can be useful for doing numerical conversions on values in a dictionary.
| The code below creates a new dictionary with temperatures in Celsius instead of Fahrenheit.

.. code-block:: python
    
    cities_in_F = {'Sydney': 86, 'Melbourne': 68, 'Brisbane': 95, 'Perth': 77}
    cities_in_C = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
    print(cities_in_C)
    # {'Sydney': 30, 'Melbourne': 20, 'Brisbane': 35, 'Perth': 25}


----

Practice Questions
--------------------

.. admonition:: Tasks

    #. Use a dictionary comprehension starting with a dictionary of the animal names and their weights in pounds, ``{'Elephant': 12000, 'Tiger': 500, 'Kangaroo': 200, 'Panda': 300}``, and converts them to kilograms. Print the dictionary.
    #. Use a dictionary comprehension starting with a dictionary of the names of famous basketball players and their heights in inches, ``{"Michael": 78, "LeBron": 81, "Kobe": 78, "Shaquille": 85}``, and converts them to centimeters. Print the dictionary.
    #. Use a dictionary comprehension starting with a dictionary of the vehicle names and their speeds in mph, ``{'Car': 60, 'Bike': 20, 'Train': 80, 'Plane': 500}``, and converts them to kph. Print the dictionary.
    #. Use a dictionary comprehension starting with a dictionary of the parts of a name and their values in uppercase, ``{'first': 'SHERLOCK', 'middle': 'HAMISH', 'surname': 'HOLMES'}``, and converts them to title case. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Use a dictionary comprehension starting with a dictionary of the animal names and their weights in pounds, ``{'Elephant': 12000, 'Tiger': 500, 'Kangaroo': 200, 'Panda': 300}``, and converts them to kilograms. Print the dictionary.

                .. code-block:: python

                    weights_in_pounds = {'Elephant': 12000, 'Tiger': 500, 'Kangaroo': 200, 'Panda': 300}
                    weights_in_kg = {key: round(value * 0.453592, 2) for key, value in weights_in_pounds.items()}
                    print(weights_in_kg)
                    # {'Elephant': 5443.11, 'Tiger': 226.8, 'Kangaroo': 90.72, 'Panda': 136.08}

            .. tab-item:: Q2

                Use a dictionary comprehension starting with a dictionary of the names of famous basketball players and their heights in inches, ``{"Michael": 78, "LeBron": 81, "Kobe": 78, "Shaquille": 85}``, and converts them to centimeters. Print the dictionary.

                .. code-block:: python

                    heights_in_inches = {"Michael": 78, "LeBron": 81, "Kobe": 78, "Shaquille": 85}
                    heights_in_cm = {key: round(value * 2.54) for key, value in heights_in_inches.items()}
                    print(heights_in_cm)
                    # {"Michael": 198, "LeBron": 206, "Kobe": 198, "Shaquille": 216}


            .. tab-item:: Q3

                Use a dictionary comprehension starting with a dictionary of the vehicle names and their speeds in mph, ``{'Car': 60, 'Bike': 20, 'Train': 80, 'Plane': 500}``, and converts them to kph. Print the dictionary.

                .. code-block:: python

                    speeds_in_mph = {'Car': 60, 'Bike': 20, 'Train': 80, 'Plane': 500}
                    speeds_in_kph = {key: round(value * 1.60934) for key, value in speeds_in_mph.items()}
                    print(speeds_in_kph)
                    # {'Car': 97, 'Bike': 32, 'Train': 129, 'Plane': 805}

            .. tab-item:: Q4

                Use a dictionary comprehension starting with a dictionary of the parts of a name and their values in uppercase, ``{'first': 'SHERLOCK', 'middle': 'HAMISH', 'surname': 'HOLMES'}``, and converts them to title case. Print the dictionary.

                .. code-block:: python

                    names = {'first': 'SHERLOCK', 'middle': 'HAMISH', 'surname': 'HOLMES'}
                    title_cased_names = {key.title(): value.title() for key, value in names.items()}
                    print(title_cased_names)
                    # {'First': 'Sherlock', 'Middle': 'Hamish', 'Surname': 'Holmes'}




