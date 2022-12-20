==========================
Enumerate
==========================

| See: Python enumerate: https://www.w3schools.com/python/ref_func_enumerate.asp
| The enumerate() function takes a collection (e.g. a list) and returns it as an enumerate object which is like a dictionary.
| The enumerate() function adds a counter as the key of the enumerate object.

Syntax:

.. py:function:: enumerate(iterable, start)

    :param iterable:	An iterable object, such as a list, tuple or string.
    :param integer: 	The start number of the enumerate object. Default 0

----

| The enumerate object can be converted to a dictionary using the dict() function.

.. code-block:: python
    
    fruit = ['apple', 'banana', 'cherry']
    fruit_enum = enumerate(fruit)

    print(dict(fruit_enum))

| The print output is: {0: 'apple', 1: 'banana', 2: 'cherry'}

----

| The enumerate object can be looped through using a for-loop.

.. code-block:: python
    
    fruit = ['apple', 'banana', 'cherry']
    fruit_enum = enumerate(fruit)

    
    for num, element in fruit_enum:
        print(num, element, end="; ")

| The print output is: 0 apple; 1 banana; 2 cherry 

----

| The keys of a dictionary can be enumerated.

.. code-block:: python

    shapes = {'a': 'triangle', 'b': 'square', 'c': 'pentagon'}

    for num, key in enumerate(shapes):
        print(num, key, end="; ")

| The print output is: 0 a; 1 b; 2 c; 

----

| The values of a dictionary can be enumerated.

.. code-block:: python

    shapes = {'a': 'triangle', 'b': 'square', 'c': 'pentagon'}

    for num, value in enumerate(shapes.values()):
        print(num, value, end="; ")

| The print output is: 0 triangle; 1 square; 2 pentagon;  

----

| The items of a dictionary can be enumerated.
| Each item is a tuple of (key, value) from the shapes dictioary.

.. code-block:: python

    shapes = {'a': 'triangle', 'b': 'square', 'c': 'pentagon'}

    for num, (key, value) in enumerate(shapes.items()):
        print(num, key, value, end="; ")

| The print output is: 0 a triangle; 1 b square; 2 c pentagon;

