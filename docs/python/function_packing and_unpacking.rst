================================
Function packing and unpacking
================================

Packing arguments of a function
----------------------------------

| When a function has a parameter preceded by an asterisk \*, it can accept a variable number of arguments. 
| Pass zero, one, or more arguments to the \*args parameter.
| The arguments are packed into a tuple.

.. code-block:: python
 
    def polygon_perimeter(*args):
        return sum(args)

    perimeter = polygon_perimeter(3, 4, 5, 6)
    print(perimeter)


----

Unpacking for a function
-----------------------------------

| The function below, tri_perimeter, requires 3 arguments, (a, b, c).
| The list, sides, can be passed to the function by unpacking the list using \*sides.

.. code-block:: python

    def tri_perimeter(a, b, c):
        return a + b + c

    sides = [7, 12, 13]
    perimeter = tri_perimeter(*sides)
    print(perimeter)

----

Unpacking with more than one value
-----------------------------------

| The range function below can take two values, the start and stop values.
| The **for-loop** code below would normally look like: **for x in range(0, 5)**.
| The unpacking operator, \*, can be used to unpack the variable vals, so that the tuple (0, 5) is turned into 2 separate arguments, 0 and 5, instead of staying as the single tuple (0, 5).

| The code below runs as if the arguments to the range function were 0 and 5.
| The code prints out: 0, 1, 2, 3, 4, 

.. code-block:: python

    vals = (0, 5)
    for x in range(*vals):
        print(x, end=", ")

| The code below runs as if the arguments to the range function were 0, 5 and 2.
| The code prints out: 0, 2, 4, 

.. code-block:: python

    vals = (0, 5, 2)
    for x in range(*vals):
        print(x, end=", ")

----

Unpacking with just one value
-----------------------------------
 
| For tuples with just one value, a trailing comma is required. e.g (5,)
| The range function expects a tuple for unpacking via (\*vals), so (5,) is needed.
| The code prints out: 0, 1, 2, 3, 4, 


.. code-block:: python

    vals = (5, )
    for x in range(*vals):
        print(x, end=", ")

