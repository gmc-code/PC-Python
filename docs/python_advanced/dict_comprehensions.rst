==========================
Dictionary Comprehensions
==========================

See docs at: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
See ref video at: https://www.youtube.com/watch?v=3dt4OGnU5sM

----

List comprehension
=====================================

| List comprehensions provide a concise way to create lists.
| They are used to make new lists where each element is the result of some operations applied to each member of another sequence or iterable.
| They can create a subsequence of those elements that satisfy a certain condition.

Syntax:

.. py:function:: new_dictionary = [expression for item in iterable]

    :param expression: the item variable only (e.g. x) or any expression such as one that uses the item variable (e.g. x * x).
    :param item:  a variable.
    :param iterable: iterable objects like strings, lists, dictionaries, range function and others.

| A list comprehension consists of brackets containing an expression followed by a for clause.
| The result will be a new list created by evaluating the expression in the context of the for and if clauses which follow it.
| e.g newlist = [2 * n for n in range(5)]

----

.. code-block:: python
    
    names = ['Lockett', 'Coventry', 'Dunstall']
    goals = [1360, 1299, 1254]
    print(list(zip(names, goals)))
    # {'Lockett': 1360, 'Coventry': 1299, 'Dunstall': 1254}
    # I want a dict{'name': 'hero'} for each name, goal in zip(names, goals)
    my_dict = {}
    for name, goal in zip(names, goals):
        my_dict[name] = goal
    print(my_dict)
    # {'Lockett': 1360, 'Coventry': 1299, 'Dunstall': 1254}
    my_dict_comprehension = {name: goal for (name, goal) in zip(names, goals)}
    print(my_dict_comprehension)
    my_dict_comprehension = {name: goal for (name, goal) in zip(names, goals) if goal > 1275}
    print(my_dict_comprehension)
    {'Lockett': 1360, 'Coventry': 1299, 'Dunstall': 1254}
    {'Lockett': 1360, 'Coventry': 1299}

----

Practice Questions
--------------------

.. admonition:: Tasks

    1. Use a list comprehension to create the liset: [('A', 'X'), ('A', 'Y'), ('B', 'X'), ('B', 'Y')].
    2. Use a list comprehension to create the liset: ['AvX', 'AvY', 'BvX', 'BvY'].


