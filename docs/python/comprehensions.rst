==========================
Comprehensions
==========================

See ref video at: https://www.youtube.com/watch?v=3dt4OGnU5sM

Anything that can be done with a for loop can be done as a comprehension.

----

Lists comprehension
-------------------------

Syntax:

.. py:function:: newlist = [expression for item in iterable]

    | expression could be the item variable only (e.g. x) or any expression such as one that uses the item variable (e.g. x*x, x.upper()).
    | item is a variable
    | iterable can be objects like strings, lists, dictionaries, range function and others.

e.g newlist = [n for n in range(5)]

----

Lists Example 1
-------------------   

| In the code below, a for-loop is used to get each value from the range function then append it to a new list, my_list.

.. code-block:: python


    # I want 'n' for each 'n' from 1 to 10
    my_list = []
    for n in range(1,11):
        my_list.append(n)
    print(my_list)

| The list comprehension, ``my_list_comprehension = [n for n in range(1,11)]``, does this in one line.

.. code-block:: python


    # I want 'n' for each 'n' in range(1,11)
    my_list_comprehension = [n for n in range(1,11)]
    print(my_list_comprehension)


----

List Example 2
-------------------

| In the code below, a for-loop is used to get each value in the nums list then append it to a new list, my_list.
| The list comprehension, ``my_list_comprehension = [n for n in nums]``, does this in one line, but needs the original list.
| The second list comprehension, ``my_list_range_comprehension = [n for n in range(1,11)]``, does this in one line, but uses the range function.

.. code-block:: python


    # I want 'n*n' for each 'n' in nums
    my_list = []
    for n in  range(1,11):
        my_list.append(n*n)
    print(my_list)

    my_list_comprehension = [n*n for n in range(1,11)]
    print(my_list_comprehension)


Practice Questions
--------------------

.. admonition:: Tasks

    1. Display a different image depending on which side microbit is tilted in.
    2. Program an LED 'sprite' that moves in the direction micro:bit is tilted in.
    3. Program an LED sprite to run in a circle. Try to extend it to a snake by adding a tail of LEDs to the original sprite.
    4. Do the same as in previous question, but this time make the sprite stop when a button is being pressed and restart if it's pressed again.



----

Lists comprehension
-------------------

Syntax:

.. py:function:: newlist = [expression for item in iterable if condition == True]

    | Scrolls ``value`` horizontally on the display. 
    