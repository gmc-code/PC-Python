==========================
Set Comprehensions
==========================

See ref video at: https://www.youtube.com/watch?v=1bwCstN0pFs

----

Set comprehension without condition
=====================================

| Python sets are not ordered.
| Duplicate items are automatically removed.
| Sets can only contain immutable objects like integers, floats, strings and tuples.
| Sets cannot contain lists, dictionaries or other sets.
| Basic uses include membership testing, eliminating duplicate entries and mathematical operations like union, intersection, and difference.
| To create an empty set use: ``set()``.
| Empty sets can't be created using ``{ }``, since that creates an empty dictionary instead.

Syntax:

.. py:function:: new_set = {expression for item in iterable}

    :param expression: the item variable only (e.g. x) or any expression such as one that uses the item variable (e.g. x * x).
    :param item:  a variable.
    :param iterable: iterable objects like strings, lists, dictionaries, range function and others.

| A set comprehension consists of braces (or "curly brackets") ``{ }`` containing an expression followed by a for clause.
| The result will be a new set created by evaluating the expression in the context of the for clause.

----

| The code below eliminating duplicate entries.

.. code-block:: python

    nums = [1, 2, 3, 1, 2, 3]
    my_set_comprehension = {n for n in nums}
    print(my_set_comprehension)

| The printed set is: {1, 2, 3}

----

| The code below converts the number strings to integers while eliminating duplicate entries.

.. code-block:: python

    str_nums = ['2', '2', '3', '3', '3', '6', '6', '7', '7', '8']
    num_set = {int(num) for num in str_nums}
    print(num_set)

| The printed set is: {2, 3, 6, 7, 8}

----

| The code below creates consistent capitalization, while removing duplicates.

.. code-block:: python

    names = ['tom', 'ted', 'tony', 'TOM', 'TONY']
    names_set = {n.capitalize() for n in names}
    print(names_set)

| The printed names_set is: {'Tom', 'Tony', 'Ted'}

----

| The code below makes a set of all the first numbers in each nested list.
| In the comprehension, ``xy`` will get each of the nested lists in tern starting with ``[1, 2]``.
| Index 1, ``xy[1]`` gets the second number. eg. ``4`` from ``[1, 4]``.

.. code-block:: python

    xycoords = [[1, 4], [2, 2], [3, 0], [4, 2]]
    y_set = {xy[1] for xy in xycoords}
    print(y_set)
    
| The printed y_set is: {0, 2, 4}

----

| The code below flatens the nested lists, while removing duplicates.

.. code-block:: python
    
    nums = [[1, 2], [2, 3], [3, 4], [4, 5]]
    flat_set = {a for pair in nums for a in pair}
    print(flat_set)
    
| The printed flat_set is: {1, 2, 3, 4, 5}

Practice Questions
--------------------

.. admonition:: Tasks

    1. Use a set comprehension with the range function to create {7, 8, 9}.
    2. Use a set comprehension with the range function to create {2, 4, 6, 8}.

----


Set comprehension with condition
=====================================

Syntax:

.. py:function:: new_set = {expression for item in iterable if condition}
    
    :param expression: the item variable only (e.g. x) or any expression such as one that uses the item variable (e.g. x * x).
    :param item:  a variable.
    :param iterable: iterable objects like strings, lists, dictionaries, range function and others.
    :param condition: any condition.

----

| In the code below, the set comprehension uses the range function with a condition filter
| ``i % 2 == 0`` check to see if the remainder from dividing by is 0.

.. code-block:: python

    evens = {i for i in range(10) if i % 2 == 0}
    print(evens)

| The printed set is: {0, 2, 4, 6, 8}

----



nums = [[1,3],[2,3],[3,98],[76,1]]
flat_set = {a for b in nums for a in b}
print(flat_set)
Eliminate Dups from a List

Get Car Make from list of Make & Model
We're getting the first word from each string.

cars = ['Toyota Prius', 'Chevy Bolt', 'Tesla Model 3', 'Tesla Model Y']
makes = {(c.split()[0]) for c in cars}
print(makes)
Get Initials from Names
Take first and last initials

names = ['Clint Barton', 'Tony', 'Nick Fury', 'Hank Pym']
inits = {(n.split()[0][0] + n.split()[1][0]) for n in names if len(n.split())==2}
print(inits)
