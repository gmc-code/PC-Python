==========================
Dictionary Comprehensions
==========================

| See docs at: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
| See ref video at: https://youtu.be/3dt4OGnU5sM?feature=shared&t=738

----

Dictionary comprehension
---------------------------

| Dictionary comprehensions provide a concise way to create dictionaries. 
| They are used to make new dictionaries where each key-value pair is the result of some operations applied to each member of a string, list, tuple, sets, dictionary, and zip of 2 lists.
| Conditions can be applied that restrict the formation of the dictionary.

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
-----------------------------------------------

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
    #. Create a dictionary comprehension that maps the names of products, 'apple', 'banana', 'cherry', and 'date', to their prices: 15, 25, 10, and 30 dollars. Print the dictionary.
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
                    student_test_scores = {student: score for student, score in zip(students, test_scores)}
                    print(student_test_scores)
                    # Output: {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 65}

            .. tab-item:: Q2

                Create a dictionary comprehension that maps the names of products, 'apple', 'banana', 'cherry', and 'date', to their prices: 15, 25, 10, and 30 dollars. Print the dictionary.

                .. code-block:: python

                    products = ['apple', 'banana', 'cherry', 'date']
                    prices = [15, 25, 10, 30]
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

Conditions in a dictionary comprehension
----------------------------------------------------------

Syntax:

.. py:function:: new_dictionary = {key: value for item in iterable if condition}
    
    :param key: the key variable only or any expression such as one that uses the item variable (e.g. n).
    :param value: the value variable only or any expression such as one that uses the item variable (e.g. 2 * n).
    :param item:  a variable that gets each item in the iterable.
    :param iterable: iterable objects like strings, lists, dictionaries, range function and others.
    :param condition: a condition that resolves to True or False.

| Create a dictionary comprehension that maps numbers from 1 to 10 to their co-factor, but only include factors of 40.

.. code-block:: python

    numbers = range(1, 11)
    factors_of_40 = {i: 40 // i for i in range(1, 11) if 40 % i == 0}
    print(factors_of_40)
    # Output: {1: 40, 2: 20, 4: 10, 5: 8, 8: 5, 10: 4}

----

Practice Questions
--------------------

.. admonition:: Tasks

    #. Create a dictionary comprehension that maps numbers from 0 to 9 to their squares, but only include even numbers. Print the dictionary.
    #. Create a dictionary comprehension that maps numbers from 0 to 9 to their squares, but only include even numbers. Print the dictionary.
    #. Create a dictionary comprehension that maps numbers from 0 to 9 to their squares, but only include even numbers. Print the dictionary.
    #. Create a dictionary comprehension that maps numbers from 0 to 9 to their squares, but only include even numbers. Print the dictionary.
    #. Create a dictionary comprehension that maps numbers from 1 to 9 to their squares, but only include squares with 2 digits. Print the dictionary.
    #. Create a dictionary comprehension that maps numbers from 1 to 31 to their squares, but only include squares with 3 digits. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary comprehension that maps numbers from 1 to 9 to their squares, but only include even numbers. Print the dictionary.

                .. code-block:: python

                    numbers = range(1, 10)
                    squared_evens = {num: num ** 2 for num in numbers if num % 2 == 0}
                    print(squared_evens)
                    # Output: {2: 4, 4: 16, 6: 36, 8: 64}

            .. tab-item:: Q2

                Create a dictionary comprehension that maps numbers from 0 to 10 to their binary representation. Print the dictionary.

                .. code-block:: python

                    numbers = range(0, 11)
                    binary_representation = {i: bin(i) for i in numbers}
                    print(binary_representation)
                    # Output: {0: '0b0', 1: '0b1', 2: '0b10', 3: '0b11', 4: '0b100', 5: '0b101', 6: '0b110', 7: '0b111', 8: '0b1000', 9: '0b1001', 10: '0b1010'}


            .. tab-item:: Q3

                Create a dictionary comprehension that maps numbers from 0 to 10 to their binary representation without the '0b' prefix. Print the dictionary.

                .. code-block:: python

                    numbers = range(0, 11)
                    binary_representation = {i: bin(i)[2:] for i in numbers}
                    print(binary_representation)
                    # Output: {0: '0', 1: '1', 2: '10', 3: '11', 4: '100', 5: '101', 6: '110', 7: '111', 8: '1000', 9: '1001', 10: '1010'}

            .. tab-item:: Q4

                Create a dictionary comprehension that maps numbers from 1 to 9 to their squares, but only include even numbers. Print the dictionary.

                .. code-block:: python

                    numbers = range(1, 10)
                    squared_evens = {num: num ** 2 for num in numbers if num % 2 == 0}
                    print(squared_evens)
                    # Output: {2: 4, 4: 16, 6: 36, 8: 64}

            .. tab-item:: Q5

                Create a dictionary comprehension that maps numbers from 1 to 9 to their squares, but only include squares with 2 digits. Print the dictionary.

                .. code-block:: python

                    numbers = range(1, 10)
                    squares_with_two_digits = {i: i**2 for i in numbers if 10 <= i**2 < 100}
                    print(squares_with_two_digits)
                    # Output: {4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

            .. tab-item:: Q6

                Create a dictionary comprehension that maps numbers from 1 to 31 to their squares, but only include squares with 3 digits. Print the dictionary.

                .. code-block:: python

                    numbers = range(1, 32)
                    squares_with_three_digits = {i: i**2 for i in numbers if 100 <= i**2 < 1000}
                    print(squares_with_three_digits)
                    # Output: {10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400, 21: 441, 22: 484, 23: 529, 24: 576, 25: 625, 26: 676, 27: 729, 28: 784, 29: 841, 30: 900, 31: 961}

----

Multiple conditions in a dictionary comprehension
-----------------------------------------------------

| Multiple conditions can be used, using the keywords ``and`` or ``or``.
| Using ``and`` requires each condition to be True for the key: value pair to be included.
| Using ``or`` requires only one condition to be True for the key: value pair to be included.

Syntax:

.. py:function:: new_dictionary = {key: value for item in iterable if condition_1 and condition_2}
    
    :param key: the key variable only or any expression such as one that uses the item variable (e.g. n).
    :param value: the value variable only or any expression such as one that uses the item variable (e.g. 2 * n).
    :param item:  a variable that gets each item in the iterable.
    :param iterable: iterable objects like strings, lists, dictionaries, range function and others.
    :param condition_1: a condition that resolves to True or False.
    :param condition_2: a condition that resolves to True or False.

| Create a dictionary comprehension that maps numbers from 1 to 31 to their squares, but only include squares with 3 digits and the sum of the digits is less than 10. Use a function to calculate the sum of the digits. Print the dictionary.

.. code-block:: python

    # Function to calculate the sum of the digits of a number
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(n))

    numbers = range(1, 32)
    squares_with_three_digits_and_digit_sum_less_than_10 = {
        i: i**2 for i in numbers if 100 <= i**2 < 1000 and sum_of_digits(i**2) < 10
    }
    print(squares_with_three_digits_and_digit_sum_less_than_10)
    # Output is {10: 100, 11: 121, 12: 144, 15: 225, 18: 324, 20: 400, 21: 441, 30: 900}

----

Practice Questions
--------------------

.. admonition:: Tasks

    #. Create a dictionary comprehension that maps numbers from 1 to 31 to their squares, but only include squares with 3 digits where all the digits are even. Use a function to check if all digits are even, using ``return all(int(digit) % 2 == 0 for digit in str(n))``. Print the dictionary.
    #. Create a dictionary comprehension that maps the first 100 triangular numbers to their values, but only include those where the sum of the digits is less than 10. Use a function to calculate the sum of the digits. Use ``return n * (n + 1) // 2``, to get triangular numbers. Print the dictionary.
    #. Create a dictionary comprehension that maps numbers from 1 to 100 to their squares, but only include those where the number is automorphic. Use ``str(n**2).endswith(str(n))``, to get automorphic numbers. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary comprehension that maps numbers from 1 to 31 to their squares, but only include squares with 3 digits where all the digits are even. Use a function to check if all digits are even, using ``return all(int(digit) % 2 == 0 for digit in str(n))``. Print the dictionary.

                .. code-block:: python

                    # Function to check if all digits of a number are even
                    # The all() function takes an iterable (in this case, the generator expression) and returns True if all elements of the iterable are True. If any element is False, all() returns False.
                    def all_digits_even(n):
                        return all(int(digit) % 2 == 0 for digit in str(n))

                    numbers = range(1, 32)
                    squares_with_three_digits_all_even = {
                        i: i**2 for i in numbers if 100 <= i**2 < 1000 and all_digits_even(i**2)
                    }
                    print(squares_with_three_digits_all_even)
                    # Output: {20: 400, 22: 484}

            .. tab-item:: Q2

                Create a dictionary comprehension that maps the first 100 triangular numbers to their values, but only include those where the sum of the digits is less than 10. Use a function to calculate the sum of the digits. Use ``return n * (n + 1) // 2``, to get triangular numbers. Print the dictionary.

                .. code-block:: python

                    # Function to calculate the sum of the digits of a number
                    def sum_of_digits(n):
                        return sum(int(digit) for digit in str(n))

                    # Function to calculate the nth triangular number
                    def triangular_number(n):
                        return n * (n + 1) // 2

                    numbers = range(1, 101)
                    triangular_numbers_with_digit_sum_less_than_10 = {
                        n: triangular_number(n) for n in numbers if sum_of_digits(triangular_number(n)) < 10
                    }
                    print(triangular_numbers_with_digit_sum_less_than_10)
                    # Output: {1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21, 8: 36, 9: 45, 14: 105, 15: 120, 17: 153, 18: 171, 20: 210, 21: 231, 24: 300, 26: 351, 35: 630, 45: 1035, 53: 1431, 63: 2016, 66: 2211, 77: 3003, 80: 3240, 81: 3321, 89: 4005}

            .. tab-item:: Q3

                Create a dictionary comprehension that maps numbers from 1 to 100 to their squares, but only include those where the number is automorphic. Use ``str(n**2).endswith(str(n))``, to get automorphic numbers. Print the dictionary.

                .. code-block:: python

                    # Function to check if a number is automorphic
                    def is_automorphic(n):
                        return str(n**2).endswith(str(n))

                    numbers = range(1, 101)
                    automorphic_numbers = {
                        i: i**2 for i in numbers if is_automorphic(i)
                    }
                    print(automorphic_numbers)
                    # Output: {1: 1, 5: 25, 6: 36, 25: 625, 76: 5776}

----

Using a condition in a dictionary comprehension with zipped lists
--------------------------------------------------------------------

Syntax:

.. py:function:: new_dictionary = {key: value for key, value in iterable if condition}

    :param key: the key variable only or any expression such as one that uses the item variable (e.g. n).
    :param value: the value variable only or any expression such as one that uses the item variable (e.g. 2 * n).
    :param item:  a variable that gets each item in the iterable.
    :param iterable: iterable objects like strings, lists, dictionaries, range function and others.
    :param condition: a condition that resolves to True or False.

.. code-block:: python

    names = ['Alex', 'Brooke', 'Chris', 'Dana']
    scores = [85, 92, 78, 90]
    min_score = 80
    high_scores = {name: score for name, score in zip(names, scores) if score >= min_score}
    print(high_scores)
    # Output: {'Alex': 85, 'Brooke': 92, 'Dana': 90}

----

Practice Questions
--------------------

.. admonition:: Tasks

    #. Create a dictionary comprehension that maps the names of students, Alice, Bob, Charlie, and David, to their test_scores: 85, 72, 90, and 65, but only include students who scored above 75. Print the dictionary.
    #. Create a dictionary comprehension that maps the names of products, apple, banana, cherry, and date, to their prices: 15, 25, 10, and 30, but only include products that cost more than $20. Print the dictionary.
    #. Create a dictionary comprehension that maps the names of vehicles, 'car', 'bike', 'boat', and 'plane', to their types: 'land', 'land', 'water', and 'air', but only include vehicles that operate on land. Print the dictionary.

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
                    min_score = 76
                    passed_students = {student: score for student, score in zip(students, test_scores) if score >= min_score}
                    print(passed_students)
                    # Output: {'Alice': 85, 'Charlie': 90}

            .. tab-item:: Q2

                Create a dictionary comprehension that maps the names of products, apple, banana, cherry, and date, to their prices: 15, 25, 10, and 30 dollars, but only include products that cost more than $20. Print the dictionary.

                .. code-block:: python

                    products = ['apple', 'banana', 'cherry', 'date']
                    prices = [15, 25, 10, 30]
                    above_cost = 20
                    expensive_products = {product: price for product, price in zip(products, prices) if price > above_cost}
                    print(expensive_products)
                    # Output: {'banana': 25, 'date': 30}

            .. tab-item:: Q3

                Create a dictionary comprehension that maps the names of vehicles, 'car', 'bike', 'boat', and 'plane', to their types: 'land', 'land', 'water', and 'air', but only include vehicles that operate on land. Print the dictionary.

                .. code-block:: python

                    vehicles = ['car', 'bike', 'boat', 'plane']
                    types = ['land', 'land', 'water', 'air']
                    type = 'land'
                    land_vehicles = {vehicle: vehicle_type for vehicle, vehicle_type in zip(vehicles, types) if vehicle_type == type}
                    print(land_vehicles)
                    # Output: {'car': 'land', 'bike': 'land'}

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

----

Dictionary comprehension of dictionaries using if-else for value
----------------------------------------------------------------------

Syntax:

.. py:function:: new_dictionary = {key: value_1 if condition  else value_2  for key, value in dictionary.items()}

    :param key: the key variable.
    :param value: the value variable.
    :param condition: an expression based on the value variable.
    :param value_1: an expression.
    :param value_2: an expression.
    :param dictionary: starting dictionary with keys and values ot be used.

| This can be useful for doing numerical conversions on values in a dictionary.
| The code below creates a new dictionary with categories rather than numerical data.

.. code-block:: python
    
    cities_in_F = {'Sydney': 19, 'Melbourne': 15, 'Brisbane': 35, 'Perth': 25}
    cities_in_C = {key: ("warm" if value > 20 else "cold") for (key, value) in cities_in_F.items()}
    print(cities_in_C)
    # Output is {'Sydney': 'cold', 'Melbourne': 'cold', 'Brisbane': 'warm', 'Perth': 'warm'}


----

Practice Questions
--------------------

.. admonition:: Tasks

    #. Use a dictionary comprehension starting with a dictionary of animal names and their weights in kilograms, ``{'Koala': 10, 'Kangaroo': 90, 'Lion': 190, 'Zebra': 350, 'Giraffe': 1200, 'Elephant': 5400}``, and categorize them into three weight classes: "heavy" (more than 1000 kg), "medium" (between 100 and 1000 kg), and "light" (less than 100 kg). Print the dictionary.
    #. Use a dictionary comprehension starting with a dictionary of car names and their top speeds in kilometers per hour, ``{'Hennessey Venom F5': 484, 'Koenigsegg Agera RS': 447, 'McLaren 720S': 341, 'Chevrolet Corvette C8': 312, 'Honda Civic': 201}``, and categorize them into three speed categories: "super fast", "fast", and "slow". Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Use a dictionary comprehension starting with a dictionary of animal names and their weights in kilograms, ``{'Koala': 10, 'Kangaroo': 90, 'Lion': 190, 'Zebra': 350, 'Giraffe': 1200, 'Elephant': 5400}``, and categorize them into three weight classes: "heavy" (more than 1000 kg), "medium" (between 100 and 1000 kg), and "light" (less than 100 kg). Print the dictionary.

                .. code-block:: python

                    animal_weights_kg = {'Koala': 10, 'Kangaroo': 90, 'Lion': 190, 'Zebra': 350, 'Giraffe': 1200, 'Elephant': 5400}
                    weight_category = {key: ("heavy" if value > 1000 else "medium" if value > 100 else "light") for key, value in animal_weights_kg.items()}
                    print(weight_category)
                    # Output: {'Koala': 'light', 'Kangaroo': 'light', 'Lion': 'medium', 'Zebra': 'medium', 'Giraffe': 'heavy', 'Elephant': 'heavy'}

            .. tab-item:: Q2

                Use a dictionary comprehension starting with a dictionary of car names and their top speeds in kilometers per hour, ``{'Hennessey Venom F5': 484, 'Koenigsegg Agera RS': 447, 'McLaren 720S': 341, 'Chevrolet Corvette C8': 312, 'Honda Civic': 201}``, and categorize them into three speed categories: "super fast", "fast", and "slow". Print the dictionary.

                .. code-block:: python

                    car_speeds_kph = {'Hennessey Venom F5': 484, 'Koenigsegg Agera RS': 447, 'McLaren 720S': 341, 'Chevrolet Corvette C8': 312, 'Honda Civic': 201}

                    speed_category = {key: ("super fast" if value > 350 else "fast" if value > 250 else "slow") for (key, value) in car_speeds_kph.items()}
                    print(speed_category)
                    # Output:  {'Hennessey Venom F5': 'super fast', 'Koenigsegg Agera RS': 'super fast', 'McLaren 720S': 'fast', 'Chevrolet Corvette C8': 'fast', 'Honda Civic': 'slow'}

----

Dictionary comprehension of dictionaries using a function for the value
-------------------------------------------------------------------------------------

Syntax:

.. py:function:: new_dictionary = {key: function for key, value in dictionary.items()}

    :param key: the key variable.
    :param value: the value variable.
    :param function: an expression based on value.
    :param dictionary: starting dictionary with keys and values ot be used.

| This can be useful for doing numerical conversions on values in a dictionary.
| The code below creates a new dictionary with categories rather than numerical data.

.. code-block:: python
    
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

----

Practice Questions
--------------------

.. admonition:: Tasks

    #. Use a dictionary comprehension starting with a dictionary of animal names and their weights in kilograms, ``{'Koala': 10, 'Kangaroo': 90, 'Lion': 190, 'Zebra': 350, 'Giraffe': 1200, 'Elephant': 5400}``, and use a function to categorize them into three weight classes: "heavy" (more than 1000 kg), "medium" (between 100 and 1000 kg), and "light" (less than 100 kg). Print the dictionary.
    #. Use a dictionary comprehension starting with a dictionary of car names and their top speeds in kilometers per hour, ``{'Hennessey Venom F5': 484, 'Koenigsegg Agera RS': 447, 'McLaren 720S': 341, 'Chevrolet Corvette C8': 312, 'Honda Civic': 201}``, and use a function to categorize them into three speed categories: "super fast", "fast", and "slow". Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Use a dictionary comprehension starting with a dictionary of animal names and their weights in kilograms, ``{'Koala': 10, 'Kangaroo': 90, 'Lion': 190, 'Zebra': 350, 'Giraffe': 1200, 'Elephant': 5400}``, and use a function to categorize them into three weight classes: "heavy" (more than 1000 kg), "medium" (between 100 and 1000 kg), and "light" (less than 100 kg). Print the dictionary.

                .. code-block:: python

                    def categorize_weight(weight):
                        if weight > 1000:
                            return "heavy"
                        elif weight > 100:
                            return "medium"
                        else:
                            return "light"

                    animal_weights_kg = {
                        'Koala': 10,
                        'Kangaroo': 90,
                        'Lion': 190,
                        'Zebra': 350,
                        'Giraffe': 1200,
                        'Elephant': 5400
                    }

                    weight_category = {animal: categorize_weight(weight) for animal, weight in animal_weights_kg.items()}
                    print(weight_category)
                    # Output: {'Koala': 'light', 'Kangaroo': 'light', 'Lion': 'medium', 'Zebra': 'medium', 'Giraffe': 'heavy', 'Elephant': 'heavy'}

            .. tab-item:: Q2

                Use a dictionary comprehension starting with a dictionary of car names and their top speeds in kilometers per hour, ``{'Hennessey Venom F5': 484, 'Koenigsegg Agera RS': 447, 'McLaren 720S': 341, 'Chevrolet Corvette C8': 312, 'Honda Civic': 201}``, and use a function to categorize them into three speed categories: "super fast", "fast", and "slow". Print the dictionary.

                .. code-block:: python

                    def categorize_speed(speed):
                        if speed > 350:
                            return "super fast"
                        elif speed > 250:
                            return "fast"
                        else:
                            return "slow"

                    car_speeds_kph = {
                        'Hennessey Venom F5': 484,
                        'Koenigsegg Agera RS': 447,
                        'McLaren 720S': 341,
                        'Chevrolet Corvette C8': 312,
                        'Honda Civic': 201
                    }

                    speed_category = {car: categorize_speed(speed) for car, speed in car_speeds_kph.items()}
                    print(speed_category)

                    # Output:  {'Hennessey Venom F5': 'super fast', 'Koenigsegg Agera RS': 'super fast', 'McLaren 720S': 'fast', 'Chevrolet Corvette C8': 'fast', 'Honda Civic': 'slow'}
