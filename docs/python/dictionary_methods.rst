===============================
Dictionary Methods
===============================

Summary of Dictionary Methods
--------------------------------

Accessing Items
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **get()**: Returns the value for a specified key if it exists, otherwise returns a default value.
- **items()**: Returns a view object displaying a list of the dictionary's key-value pairs.
- **keys()**: Returns a view object displaying a list of all the keys in the dictionary.
- **values()**: Returns a view object displaying a list of all the values in the dictionary.

Modifying Items
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **update()**: Updates the dictionary with elements from another dictionary or an iterable of key-value pairs.
- **setdefault()**: Returns the value of a specified key, inserting it with a default value if it doesn't exist.
- **pop()**: Removes the specified key and returns the corresponding value.
- **popitem()**: Removes and returns a key-value pair from the dictionary in LIFO order.

Dictionary Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **copy()**: Returns a shallow copy of the dictionary.
- **clear()**: Removes all items from the dictionary.
- **fromkeys()**: Creates a new dictionary with keys from an iterable and values set to a specified value.


----

Sample dictionary for examples
-----------------------------------

.. code-block:: python

    # Creating a sample dictionary
    sample_dict = {'a': 1, 'b': 2, 'c': 3}

-----

Accessing Items
---------------

get()
~~~~~~~~~~~~~

.. py:method:: dict.get(key, default=None)

    **Description**: Returns the value for the specified key if the key is in the dictionary, otherwise returns the default value.

.. code-block:: python

    value = sample_dict.get('a')
    # Output: 1

----

items()
~~~~~~~~~~~~~

.. py:method:: dict.items()

    **Description**: Returns a view object that displays a list of dictionary's key-value tuple pairs.

.. code-block:: python

    items = sample_dict.items()
    # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

----

keys()
~~~~~~~~~~~~~

.. py:method:: dict.keys()

    **Description**: Returns a view object that displays a list of all the keys in the dictionary.

.. code-block:: python

    keys = sample_dict.keys()
    # Output: dict_keys(['a', 'b', 'c'])

----

values()
~~~~~~~~~~~~~

.. py:method:: dict.values()

    **Description**: Returns a view object that displays a list of all the values in the dictionary.

.. code-block:: python

    values = sample_dict.values()
    # Output: dict_values([1, 2, 3, 4, 5])

----

Modifying Items
---------------

update()
~~~~~~~~~~~~~

.. py:method:: dict.update([other])

    **Description**: Updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs.

.. code-block:: python

    sample_dict.update({'e': 5})
    # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

----

setdefault()
~~~~~~~~~~~~~

.. py:method:: dict.setdefault(key, default=None)

    **Description**: Returns the value of the specified key. If the key does not exist, inserts the key with the specified default value.

.. code-block:: python

    value = sample_dict.setdefault('d', 4)
    # Output: 4
    # sample_dict is now {'a': 1, 'b': 2, 'c': 3, 'd': 4}

----

pop()
~~~~~~~~~~~~~

.. py:method:: dict.pop(key, default=None)

    **Description**: Removes the specified key and returns the corresponding value. If the key is not found, the default value is returned if provided, otherwise a KeyError is raised.

.. code-block:: python

    value = sample_dict.pop('a')
    # Output: 1
    # sample_dict is now {'b': 2, 'c': 3}

----

popitem()
~~~~~~~~~~~~~

.. py:method:: dict.popitem()

    **Description**: Removes and returns a key-value pair from the dictionary. Pairs are returned in LIFO (last-in, first-out) order.

.. code-block:: python

    item = sample_dict.popitem()
    # Output: ('c', 3)
    # sample_dict is now {'a': 1, 'b': 2}

----

Dictionary Operations
---------------------

copy()
~~~~~~~~~~~~~

.. py:method:: dict.copy()

    **Description**: Returns a shallow copy of the dictionary.

.. code-block:: python

    new_dict = sample_dict.copy()
    # Output: {'a': 1, 'b': 2, 'c': 3}

----

clear()
~~~~~~~~~~~~~

.. py:method:: dict.clear()

    **Description**: Removes all items from the dictionary.

.. code-block:: python

    sample_dict.clear()
    # Output: {}

----

fromkeys()
~~~~~~~~~~~~~

.. py:method:: dict.fromkeys(iterable, value=None)

    **Description**: Creates a new dictionary with keys from the given iterable and values set to the specified value.

.. code-block:: python

    keys = ('a', 'b', 'c')
    value = 0
    new_dict = dict.fromkeys(keys, value)
    # Output: {'a': 0, 'b': 0, 'c': 0}


