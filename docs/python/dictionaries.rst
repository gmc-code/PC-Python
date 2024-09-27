===============================
Data Structures: Dictionaries
===============================

Dictionary structure
----------------------------

| A Python dictionary is a collection of items.
| Each item  is a ``key: value`` pair. 

.. code-block:: python

    dictionary_1 = {
        <key_1>: <value_1>,
        <key_2>: <value_2>,
        .
        .
        <key_n>: <value_n>
    }

| Dictionary items are ordered, changeable, and do not allow duplicates.
| All keys must be immutable (not able to be changed) such as integers, strings and tuples of integers or strings.
| Values can be any  data types such as string, int, boolean, tuple, list, dictionary. 
| Values in a dictionary are retrieved by using the key as an index. e.g print(dictionary_1[key_1])

----

Empty dictionary
-------------------

| An empty dictionary can be made using **curly brackets**:

.. code-block:: python

    empty_dict = {}

| An empty dictionary can be made using the **dict function**:

.. code-block:: python
    
    empty_dict = dict()

----

Making a dictionary
----------------------

Making a dictionary: curly brackets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Make a dictionary by enclosing a comma-separated sequence of key-value pairs in curly braces ``{}``. 
| The dictionary below has 3 items, each separated by a comma.
| Each item is a key: value pair separated by a colon.

.. code-block:: python

    state_capitals = {
                    'Victoria': "Melbourne",
                    'Tasmania': "Hobart",
                    'Queensland': "Brisbane"
                    } 
    print(state_capitals)

----

Making a dictionary from a list of lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Make a dictionary using the dict function.
| Pass in a list of lists, with each list made up 2 elements, e.g ``["New South Wales", "Sydney"]``
| The first element becomes the key and the second element becomes the value. e.g ``"New South Wales": "Sydney"``

.. code-block:: python

    state_capitals = dict([
        ["New South Wales", "Sydney"],
        ["Victoria", "Melbourne"],
        ["Queensland", "Brisbane"]
    ])

    print(state_capitals)


----

Making a dictionary from a list of tuples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Make a dictionary using the dict function.
| Pass in a list of tuples, with each tuple made up 2 elements, e.g ``("New South Wales", "Sydney")``
| The first element becomes the key and the second element becomes the value. e.g ``"New South Wales": "Sydney"``

.. code-block:: python

    capitals = dict([
        ("South Australia", "Adelaide"),
        ("Western Australia", "Perth"),
        ("Australian Capital Territory", "Canberra")
    ])
    print(capitals)


----

Making a dictionary from 2 lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 2 lists of keys and values can be combined and converted into a dictionary.
| The zip() function pairs each element from the states list with the corresponding element from the cities list. 
| The result is an iterator containing these tuples: ``('Queensland', 'Brisbane'), ('South Australia', 'Adelaide'), ('Western Australia', 'Perth')``
| The dict function then converts the zip object into a dictionary.

.. code-block:: python

    states = ["Queensland", "South Australia", "Western Australia"]
    cities = ["Brisbane", "Adelaide", "Perth"]

    capitals = dict(zip(states, cities))
    print(capitals)


----

Making a dictionary by dictionary comprehension from 2 lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The dictionary comprehension below creates a dictionary by iterating over the tuples produced by zip(). 
For each tuple, the state becomes the key and city becomes the value.

.. code-block:: python

    states = ["Western Australia", "Tasmania", "Northern Territory"]
    cities = ["Perth", "Hobart", "Darwin"]

    capitals = {state: city for state, city in zip(states, cities)}

----

Making a dictionary from key word arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Make a dictionary using the dict function and key word arguments.
| ``a=1`` will become the key value pair ``'a': 1``

.. code-block:: python

    simple_dict = dict(a=1, b=2, c=3, d=4)
    print(simple_dict)

----

----

.. admonition:: Tasks

    #. Create a dictionary using curly brackets such that it maps the names of three countries, Japan, France and England, to their capitals. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary using curly brackets such that it maps the names of three countries, Japan, France and England, to their capitals. Print the dictionary.

                .. code-block:: python

                    country_capitals = {
                        'Japan': 'Tokyo',
                        'France': 'Paris',
                        'England': 'London'
                    }
                    print(country_capitals)


----

----

# Access elements
game_register['dent']

# Add or update and existing entry
game_register['pepper'] = 50

# Delete an entry
del game_register['pepper']    

# Delete all entries
game_register.clear()

# Delete the dictionary
del game_register

# Retrieve a value for the key or default if not in dicionary
game_register.get('dent')        

----

Dictionary methods:
----------------------

| clear() Removes all the elements from the dictionary
| copy() Returns a copy of the dictionary
| fromkeys() Returns a dictionary with the specified keys and value
| get() Returns the value of the specified key
| items() Returns a list containing a tuple for each key value pair
| keys() Returns a list containing the dictionary's keys
| pop() Removes the element with the specified key
| popitem() Removes the last inserted key-value pair
| setdefault() Returns the value of the specified key. If the key does not exist: it inserts the key, with the specified value
| update() Updates the dictionary with the specified key-value pairs
| values() Returns a list of all the values in the dictionary



