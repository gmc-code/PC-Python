==========================
Multiple Assignment
==========================

Multiple Assignment in Tuple, list, strings
---------------------------------------------

| Assign multiple variables at the same time time using commas.
| The code below assigns 3 variables in one line resulting in: a = 1, b = 2, c = 3.
| This can also be written as tuples: (a, b, c) = (1, 2, 3)

.. code-block:: python

    a, b, c = 1, 2, 3
    print(a, b, c)

| This works with tuples fully written.

.. code-block:: python

    (a, b, c) = (4, 5, 6)
    print(a, b, c)

| This works with lists.

.. code-block:: python

    [a, b, c] = [7, 8, 9]
    print(a, b, c)

| This works with strings.

.. code-block:: python

    a, b, c = "xyz"
    print(a, b, c)

----

Packing with * in multiple assignment
----------------------------------------

| In the code below, a is assigned 1 and b is assigned 2, and c is assigned the rest of the values packed as a list.
| Note that in the print output, c is a list.


.. code-block:: python

    a, b, *c = 1, 2, 4, 5, 6, 7
    print(a, b, c)

----

Swapping variable values
--------------------------

| In the code below, a is assigned 7 and b is assigned 8.
| ``a, b = b, a`` swaps those values so a is 8 and b is 7.

.. code-block:: python

    a, b = 7, 8
    a, b = b, a
    print(a, b)

