==========================
Lists
==========================

Lists
--------------

| List is a data structure used to store any data type in **order**. 
| The pieces of data stored in a list are called `elements`. 


To create a list, you specify its contents enclosed within brackets and delimited by commas: 

.. code-block:: python

    from microbit import *

    high_scores = [25, 20, 10, 15, 30]    # Create a list and store some values in it.
    print(high_scores[0])            # Print 25
    print(high_scores[3])            # Print 15


Finding the value of one of the elements in a list is straightforward as long as you keep in mind that Python counts the elements from '0'. In the ``high_scores`` list 
above, ``high_scores[0]`` is 25 and ``high_scores[3]`` is 15.

Here you can also see that particular elements in a list can be accessed by their index. Furthermore, it is possible to slice lists to get only a part of a list depending
on the index. If you only want the first three, you can write ``high_scores[0:3]``, or, since we are starting at 0, we can shorten it to ``high_scores[:3]``. Mind that
the right endpoint is alway excluded, so the 'slice' above refers to the mathematical interval ``[0,2]``.

Not surprisingly, Python has features for working with lists. The code snippet below calculates the sum of all elements and then calculates the average high score. 

.. code-block:: python

    total_score = 0

    for score in high_scores:         # For each element ...
        total_score = total_score + score

    average = total_score / len(high_scores)  # Use the len() function here to find the length of the array 

The same can be done in one line using the ``sum`` function.

.. code-block:: python

   average_quick = sum(high_score) / len(high_score)     


Since you don't necessarily know what values in the list are going to be, or how large the list will be, it's useful to know the ``append`` function. 
For example, you can use it to fill a list with temperature readings or accelerometer values

.. code-block:: python

    from microbit import *

    recorded_temperature = []         # Create an empty list
    for i in range(100):            # Add 100 temperature values
        recorded_temperature.append(temperature())
        sleep(1000)             

The ``for`` loop is executed 100 times and ``i`` will have values from 0 to 99. This will measure the temperature every second for 100 seconds and append the value 
to the end of the list. 


Deleting items from a list is just as straightforward.

.. code-block:: python

    high_scores.delete(24)

This will delete the first element with the value 24.
Alternatively, you might want to delete an element at a specific position, if you know it:

.. code-block:: python

    high_scores.pop(3)

This will delete or 'pop' the element at the given position in the list. Note that:

.. code-block:: python

     high_scores.pop() 

will delete the last element in the list.


.. tip:: You can look here_ to see more useful methods on lists.

.. _here: https://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences

.. note:: You might be wondering whether strings can be considered to be a list. Even though string is an array of characters and we can even do similar operations on 
    them (like slicing), they are both different types of objects with different methods (try to type ``dir(str)`` and ``dir(list)`` in your console). 

Sorting
---------

Often you'll find the need to have data in your list sorted, for example when implementing search algorithms. In Python, sorting lists is easy using the ``sort(key=, reverse=)`` method:

.. code-block:: python

     high_scores = [25, 20, 10, 15, 30]
    high_scores.sort()

You don't only have to sort numbers - its optional key parameter allows you to specify your own    function for comparing elements in your list (for example, while 
sorting a list of strings according to length, you can pass the len() function as the parameter). Passing false to reverse parameter allows you to sort in a descending 
order. 

.. code-block:: python

    list = ['longest', 'short', 'longer']

    # Sort list in ascending order of string length
    list.sort(key=len)
    # Sort list in descending order of string length
    list.sort(key=len, reverse=True)

