==========================
Dictionary Comprehensions
==========================

See docs at: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
See ref video at: https://www.youtube.com/watch?v=3dt4OGnU5sM

----

Dictionary comprehension
---------------------------

| Dictionary comprehensions provide a concise way to create dictionaries. 
| They are used to make new dictionaries where each key-value pair is the result of some operations applied to each member of another sequence (e.g. list, range function) or iterable (e.g. list, zip of 2 list-comprehensions).
| They can also create a sub-sequence of those elements that satisfy a certain condition.

----

Syntax
------------

.. py:function:: new_dictionary = {key: value for item in iterable}
or 
.. py:function:: new_dictionary = {key: value for key, value in iterable}

    :param key: the key variable only or any expression such as one that uses the item variable (e.g. n).
    :param value: the value variable only or any expression such as one that uses the item variable (e.g. 2 * n).
    :param item:  a variable that gets each item in the iterable.
    :param iterable: iterable objects like strings, lists, dictionaries, range function and others.

| A dictionary comprehension consists of braces containing an expression followed by a for clause. 
| The result will be a new dictionary created by evaluating the expression in the context of the for and if clauses which follow it. 
| e.g new_dict = {n: 2 * n for n in range(5)}
| The dictionary produced is: {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

.. code-block:: python
    
    names = ['Lockett', 'Coventry', 'Dunstall']
    goals = [1360, 1299, 1254]
    my_dict_comprehension = {name: goal for (name, goal) in zip(names, goals)}
    print(my_dict_comprehension)
    # {'Lockett': 1360, 'Coventry': 1299, 'Dunstall': 1254}


----

Practice Questions
--------------------

.. admonition:: Tasks

    #. Create a dictionary comprehension that maps the names of students, Alice, Bob, Charlie, and David, to their grades: 85, 72, 90, and 65. Print the dictionary.
    #. Create a dictionary comprehension that maps numbers from 0 to 9 to their squares. Print the dictionary.
    #. Create a dictionary comprehension that maps the names of products, apple, banana, cherry, and date, to their prices: 15, 25, 10, and 30. Print the dictionary.
    #. Create a dictionary comprehension that maps the names of vehicles, 'car', 'bike', 'boat', and 'plane', to their types: 'land', 'land', 'water', and 'air'. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary comprehension that maps the names of students, Alice, Bob, Charlie, and David, to their grades: 85, 72, 90, and 65. Print the dictionary.

                .. code-block:: python

                    students = ['Alice', 'Bob', 'Charlie', 'David']
                    grades = [85, 72, 90, 65]
                    # Dictionary comprehension with a condition
                    student_grades = {student: grade for student, grade in zip(students, grades)}
                    print(student_grades)
                    # Output: {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 65}

            .. tab-item:: Q2

                Create a dictionary comprehension that maps numbers from 1 to 9 to their squares. Print the dictionary.

                .. code-block:: python

                    numbers = range(1, 10)
                    # Dictionary comprehension with a condition
                    squared_evens = {num: num ** 2 for num in numbers}
                    print(squared_evens)
                    # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
                    
            .. tab-item:: Q3

                Create a dictionary comprehension that maps the names of products, apple, banana, cherry, and date, to their prices: 15, 25, 10, and 30 dollars. Print the dictionary.

                .. code-block:: python

                    products = ['apple', 'banana', 'cherry', 'date']
                    prices = [15, 25, 10, 30]
                    # Dictionary comprehension with a condition
                    expensive_products = {product: price for product, price in zip(products, prices)}
                    print(expensive_products)
                    # Output: {'apple': 15, 'banana': 25, 'cherry': 10, 'date': 30}

            .. tab-item:: Q4

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
    
or
    
.. py:function:: high_scores = {key: value for key, value in iterable if condition}

    :param key: the key variable only or any expression such as one that uses the item variable (e.g. n).
    :param value: the value variable only or any expression such as one that uses the item variable (e.g. 2 * n).
    :param item:  a variable that gets each item in the iterable.
    :param iterable: iterable objects like strings, lists, dictionaries, range function and others.
    :param condition:  a condition that resolves to True or False.

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

    #. Create a dictionary comprehension that maps the names of students, Alice, Bob, Charlie, and David, to their grades: 85, 72, 90, and 65, but only include students who scored above 75. Print the dictionary.
    #. Create a dictionary comprehension that maps numbers from 0 to 9 to their squares, but only include even numbers. Print the dictionary.
    #. Create a dictionary comprehension that maps the names of products, apple, banana, cherry, and date, to their prices: 15, 25, 10, and 30, but only include products that cost more than $20. Print the dictionary.
    #. Create a dictionary comprehension that maps the names of vehicles, 'car', 'bike', 'boat', and 'plane', to their types: 'land', 'land', 'water', and 'air', but only include vehicles that operate on land. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary comprehension that maps the names of students, Alice, Bob, Charlie, and David, to their grades: 85, 72, 90, and 65, but only include students who scored above 75. Print the dictionary.

                .. code-block:: python

                    students = ['Alice', 'Bob', 'Charlie', 'David']
                    grades = [85, 72, 90, 65]

                    # Dictionary comprehension with a condition
                    passed_students = {student: grade for student, grade in zip(students, grades) if grade > 75}
                    print(passed_students)
                    # Output: {'Alice': 85, 'Charlie': 90}

            .. tab-item:: Q2

                Create a dictionary comprehension that maps numbers from 1 to 9 to their squares, but only include even numbers. Print the dictionary.

                .. code-block:: python

                    numbers = range(1, 10)

                    # Dictionary comprehension with a condition
                    squared_evens = {num: num ** 2 for num in numbers if num % 2 == 0}
                    print(squared_evens)
                    # Output: {2: 4, 4: 16, 6: 36, 8: 64}
                    
            .. tab-item:: Q3

                Create a dictionary comprehension that maps the names of products, apple, banana, cherry, and date, to their prices: 15, 25, 10, and 30 dollars, but only include products that cost more than $20. Print the dictionary.

                .. code-block:: python

                    products = ['apple', 'banana', 'cherry', 'date']
                    prices = [15, 25, 10, 30]

                    # Dictionary comprehension with a condition
                    expensive_products = {product: price for product, price in zip(products, prices) if price > 20}
                    print(expensive_products)
                    # Output: {'banana': 25, 'date': 30}

            .. tab-item:: Q4

                Create a dictionary comprehension that maps the names of vehicles, 'car', 'bike', 'boat', and 'plane', to their types: 'land', 'land', 'water', and 'air', but only include vehicles that operate on land. Print the dictionary.

                .. code-block:: python

                    vehicles = ['car', 'bike', 'boat', 'plane']
                    types = ['land', 'land', 'water', 'air']

                    land_vehicles = {vehicle: vehicle_type for vehicle, vehicle_type in zip(vehicles, types) if vehicle_type == 'land'}
                    print(land_vehicles)
                    # Output: {'car': 'land', 'bike': 'land'}









