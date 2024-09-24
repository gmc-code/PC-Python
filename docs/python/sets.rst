==========================
Data Structures: Sets
==========================

Sets
---------

Unlike lists and tuples, sets hold an **unordered** collection of elements with no duplicates. This makes them suitable for testing membership or removing 
duplicate elements.

.. code-block:: python

    set = {8, 12, 22}

    # Add a single element to set
    set.add(42)

    # Add several elements to set
    set.update([16, 32, 64])

    # Remove an element from set - throws an error if element not in set 
    set.remove(42)

    # Remove an element if present in set 
    set.discard(42)



Since a set is an unordered collection of elements, indexing is not possible. Python supports typical set operation methods:

.. code-block:: python

    set_a = {1,2,3,4,5}
    set_b = {4,5,6,7}
    set_c = {1,2}

    # Check for membership
    2 in set_a

    # Return elements in the intersection of set_a and set_b
    set_a.intersection(set_b)
    # Return true if set_a contains all the elements of set_c
    set_a.issuperset(set_c)

An empty set is created using a ``set()`` method, as using braces creates an empty dictionary (see below).      

For more methods, visit Python documentation_.

.. _documentation: https://docs.python.org/3/tutorial/datastructures.html

See: https://www.w3schools.com/python/python_sets.asp
