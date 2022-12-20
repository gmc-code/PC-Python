==========================
Generators
==========================

See ref video at: https://www.youtube.com/watch?v=bD05uGo_sVI

----

Generator via a for-loop
=============================================

| Python generators use the yield keyword.
| The code below uses a generator for square numbers.
| The generator object does not hold all the values it generates in memory, whereas a list does.


.. code-block:: python

    # I want to yield 'n * n' for each 'n' in nums
    nums = [1, 2, 3, 4, 5]


    def gen_squares(nums):
        for n in nums:
            yield n * n


    my_gen_squares = gen_squares(nums)

    for num in my_gen_squares:
        print(num, end=" ")

| The printout is: 1 4 9 16 25

----


Generator comprehension 
=============================================

| Generator comprehension looks just like list comprehension but uses parentheses ``()`` rather than square brackets ``[]``.

Syntax:

.. py:function:: new_generator = (expression for item in iterable)

    :param expression: the item variable only (e.g. x) or any expression such as one that uses the item variable (e.g. x * x).
    :param item:  a variable.
    :param iterable: iterable objects like strings, lists, dictionaries, range function and others.


| The code below is a generator for square numbers.

.. code-block:: python

    # I want to yield 'n * n' for each 'n' in nums
    nums = [1, 2, 3, 4, 5]

    my_gen_squares = (x * x for x in nums)

    for num in my_gen_squares:
        print(num, end=" ")


| The printout is: 1 4 9 16 25


----


Practice Questions
--------------------

.. admonition:: Tasks

    1. Use a generator comprehension to produce the first 5 cubic numbers.
    2. Use a generator comprehension to get the value of (x ** 2 + 2 * x + 1) for each x from 1 to 5.

