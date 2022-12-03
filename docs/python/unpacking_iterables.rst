==========================
Unpacking iterables
==========================

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

----

Unpacking for a function
-----------------------------------

| The function below, tri_perimeter, requires 3 arguments, (a, b, c).
| The list, sides, can be passed to the function by unpacking the list using \*sides.

.. code-block:: python

    sides = [7, 12, 13]

    def tri_perimeter(a, b, c):
        return a + b + c

    print(tri_perimeter(*sides))

----

Unpacking to merge tuples
------------------------------

| Tuple unpacking below can be used to merge tuples.

.. code-block:: python
 
    tuple1 = ("a", "b", "c")
    tuple2 = (3, 2, 1)
    merged_tuple = (*tuple1, *tuple2)
    print(merged_tuple)

----

Unpacking to merge lists
------------------------------

| List unpacking below can be used to merge lists.

.. code-block:: python
 
    list1 = ["a", "b", "c"]
    list2 = [3, 2, 1]
    merged_list = [*list1, *list2]
    print(merged_list)


