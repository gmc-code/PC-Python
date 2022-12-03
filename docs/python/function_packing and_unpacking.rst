================================
Function packing and unpacking
================================

Unpacking for a function
-----------------------------------

| The function below, tri_perimeter, requires 3 arguments, (a, b, c).
| The list, sides, can be passed to the function by unpacking the list using \*sides.

.. code-block:: python

    sides = [7, 12, 13]

    def tri_perimeter(a, b, c):
        return a + b + c

    perimeter = tri_perimeter(*sides)
    print(perimeter)

----

Packing arguments of a function
----------------------------------

| When a function has a parameter preceded by an asterisk \*, it can accept a variable number of arguments. 
| Pass zero, one, or more arguments to the \*args parameter.
| The arguments are packed into a tuple.

.. code-block:: python
 
    def poly_perimeter(*args):
        return sum(args)

    perimeter = poly_perimeter(3, 4, 5, 6)
    print(perimeter)


