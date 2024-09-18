==========================
Data Structures: Tuples
==========================

Tuples
----------

Tuples are similar to lists in that they are used to store an ordered sequence of items, usually of varying datatype.

.. code-block:: python

    high_scores_immutable = (25, 20, 10, 15, 30)

You can retrieve values in the same way as with lists, but the most important difference is that tuples are `immutable`. This means, that in the ``high_scores`` 
list above, you can change the value of individual elements:

.. code-block:: python

    high_scores[0] = 42

However, trying to change a value inside ``high_scores_immutable`` will return a ``TypeError: Object tuple does not support item assignment``. Once you assign values 
inside a tuple, they cannot be changed. 

Mutability is another difference between strings and lists - while lists are mutable, string are not.
