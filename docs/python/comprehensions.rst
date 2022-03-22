==========================
Comprehensions
==========================

See ref video at: https://www.youtube.com/watch?v=3dt4OGnU5sM

Anything that can be done with a for loop can be done as a comprehension.

----

==========================
Lists comprehension 1
==========================

Syntax:

.. py:data:: newlist = [expression for item in iterable]

    | expression could be the item variable only (e.g. x) or any expression such as one that uses the item variable (e.g. x*x, x.upper()).
    | item is a variable
    | iterable can be objects like strings, lists, dictionaries, range function and others.

e.g newlist = [n for n in range(5)]

----

The first 2 examples illustrate simple list comprehensions without doing anything with the values.


Lists Example 1: list
-------------------------   

| In the code below, a for-loop is used to get each value from an original list then append it to a new list, my_list.


.. code-block:: python


    nums = [1, 3, 6, 10, 15, 21, 28]

    # I want 'n' for each 'n' in nums
    my_list = []
    for n in nums:
        my_list.append(n)
    print(my_list)


 | The list comprehension, ``my_list_comprehension = [n for n in nums]``, does this in one line.

.. code-block:: python
    
    # I want 'n' for each 'n' in nums
    my_list_comprehension = [n for n in nums]
    print(my_list_comprehension)



----

Lists Example 2: range
-------------------------   

| In the code below, a for-loop is used to get each value from the range function then append it to a new list, my_list.


.. code-block:: python


    # I want 'n' for each 'n' from 1 to 10
    my_list = []
    for n in range(1, 11):
        my_list.append(n)
    print(my_list)

| The list comprehension, ``my_list_comprehension = [n for n in range(1, 11)]``, does this in one line.

.. code-block:: python


    # I want 'n' for each 'n' in range(1, 11)
    my_list_comprehension = [n for n in range(1, 11)]
    print(my_list_comprehension)


----

List Example 3
-------------------

| In the code below, a for-loop is used to get each value from an original list then append a calculated value to a new list, my_list.


.. code-block:: python


    nums = [1, 3, 6, 10, 15, 21, 28]

    # I want 'n*n' for each 'n' in nums
    my_list = []
    for n in nums:
        my_list.append(n * n)
    print(my_list)


 | The list comprehension, ``my_list_comprehension = [n * n for n in nums]``, does this in one line.

.. code-block:: python
    

    # I want 'n*n' for each 'n' in nums
    my_list_comprehension = [n * n for n in nums]
    print(my_list_comprehension)



Practice Questions
--------------------

.. admonition:: Tasks

    1. Use a list comprehension to create a list of 2 * n for each n in [0, 1, 1, 2, 3, 5, 8].
    2. Use a list comprehension to create a list of 2 * n - 1  for each n in [2, 3, 5, 6, 7, 8, 10].
   
----

==========================
Lists comprehension 2
==========================

Syntax:

.. py:function:: newlist = [expression for item in iterable if condition == True]

    | :paramstr expression: expression could be the item variable only (e.g. x) or any expression such as one that uses the item variable (e.g. x*x, x.upper()).
    | :param item: item is a variable.
    | :param iterable: iterable can be objects like strings, lists, dictionaries, range function and others.
    | :param condition: condition is any condition.

    

List Example 1
-------------------

| In the code below, a for-loop is used to get a list of event numbers from a list.
| Using the modulus, ``num % 2`` gives 0 for even numbers.


.. code-block:: python


    nums = [1, 3, 6, 10, 15, 21, 28]

    # I want n for each n in nums if n is even 
    my_list = []
    for n in nums:
        my_list.append(n * n)
    print(my_list)


 | The list comprehension, ``my_list_comprehension = [n * n for n in nums]``, does this in one line.

.. code-block:: python
    

    # I want n for each n in nums if n is even 
    my_list_comprehension = [n for n in nums if num % 2 == 0]
    print(my_list_comprehension)

nested+