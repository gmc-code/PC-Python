===============================
Dictionary Methods
===============================

Summary of Dictionary Methods
--------------------------------

Accessing Items
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. role:: blue

- :blue:`get()`: Returns the value for a specified key if it exists, otherwise returns a default value.
- :blue:`items()`: Returns a view object displaying a list of the dictionary's key-value pairs.
- :blue:`keys()`: Returns a view object displaying a list of all the keys in the dictionary.
- :blue:`values()`: Returns a view object displaying a list of all the values in the dictionary.

Modifying Items
~~~~~~~~~~~~~~~~~~~~~~~~~~

- :blue:`update()`: Updates the dictionary with elements from another dictionary or an iterable of key-value pairs.
- :blue:`setdefault()`: Returns the value of a specified key, inserting it with a default value if it doesn't exist.
- :blue:`pop()`: Removes the specified key and returns the corresponding value.
- :blue:`popitem()`: Removes and returns a key-value pair from the dictionary in LIFO order.

Dictionary Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~

- :blue:`copy()`: Returns a shallow copy of the dictionary.
- :blue:`clear()`: Removes all items from the dictionary.
- :blue:`fromkeys()`: Creates a new dictionary with keys from an iterable and values set to a specified value.

----

Accessing Items
---------------

get()
~~~~~~~~~~~~~

.. py:method:: dict.get(key, default=None)

    Returns the value for the specified key if the key is in the dictionary, otherwise returns the default value.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    value = sample_dict.get('a')
    print(value)
    # Output is 1
    value = sample_dict.get('d')
    print(value)
    # Output is None
    value = sample_dict.get('d', 0)
    print(value)
    # Output is 0

| The get method is often used since it avoids error messages that occur when a key doesn't exist.
| The code below uses dictionary key access, which accesses the value associated with a specific key in a dictionary using square brackets as in dict[key].

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    value = sample_dict['a']
    print(value)
    # Output is 1
    value = sample_dict['d']
    print(value)
    # Output is Error message KeyError: 'd'

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to print the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}.
    #. Write code to print the value of 'banana' in the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}.
    #. Write code to print the value of 'blue' in the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}.
    #. Write code to print the value of 'dog' in the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to print the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}.

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    value = coordinates_dict.get('y')
                    print(value)
                    # Output is 20

            .. tab-item:: Q2

                Write code to print the value of 'banana' in the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}.

                .. code-block:: python

                    fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}
                    value = fruits_dict.get('banana')
                    print(value)
                    # Output is 'yellow'

            .. tab-item:: Q3

                Write code to print the value of 'blue' in the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}.

                .. code-block:: python

                    colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
                    value = colors_dict.get('blue')
                    print(value)
                    # Output is '#0000FF'


            .. tab-item:: Q4

                Write code to print the value of 'dog' in the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}.

                .. code-block:: python

                    animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}
                    value = animals_dict.get('dog')
                    print(value)
                    # Output is 'woof'

----

items()
~~~~~~~~~~~~~

.. py:method:: dict.items()

    Returns a view object that displays a list of dictionary's key-value tuple pairs.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    items = sample_dict.items()
    print(items)
    # Output is dict_items([('a', 1), ('b', 2), ('c', 3)])

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to print the key-value tuple pairs in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}.
    #. Write code to print the key-value tuple pairs in the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}.
    #. Write code to print the key-value tuple pairs in the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}.
    #. Write code to print the key-value tuple pairs in the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to print the key-value tuple pairs in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}.

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    coordinates_items = coordinates_dict.items()
                    print(coordinates_items)
                    # Output is dict_items([('x', 10), ('y', 20), ('z', 30)])

            .. tab-item:: Q2

                Write code to print the key-value tuple pairs in the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}.

                .. code-block:: python

                    fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}
                    fruits_items = fruits_dict.items()
                    print(fruits_items)
                    # Output is dict_items([('apple', green), ('banana', yellow), ('cherry', red)])


            .. tab-item:: Q3

                Write code to print the key-value tuple pairs in the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}.

                .. code-block:: python

                    colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
                    colors_items = colors_dict.items()
                    print(colors_items)
                    # Output is dict_items([('red', '#FF0000'), ('green', '#00FF00'), ('blue', '#0000FF')])


            .. tab-item:: Q4

                Write code to print the key-value tuple pairs in the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}.

                .. code-block:: python

                    animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}
                    animals_items = animals_dict.items()
                    print(animals_items)
                    # Output is dict_items([('cat', 'meow'), ('dog', 'woof'), ('bird', 'tweet')])

----

keys()
~~~~~~~~~~~~~

.. py:method:: dict.keys()

    Returns a view object that displays a list of all the keys in the dictionary.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    keys = sample_dict.keys()
    print(keys)
    # Output is dict_keys(['a', 'b', 'c'])

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to print the keys in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}.
    #. Write code to print the keys in the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}.
    #. Write code to print the keys in the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}.
    #. Write code to print the keys in the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to print the keys in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}.

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    coordinates_keys = coordinates_dict.keys()
                    print(coordinates_keys)
                    # Output is dict_keys(['x', 'y', 'z'])

            .. tab-item:: Q2

                Write code to print the keys in the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}.

                .. code-block:: python

                    fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}
                    fruits_keys = fruits_dict.keys()
                    print(fruits_keys)
                    # Output is dict_keys(['apple', 'banana', 'cherry'])

            .. tab-item:: Q3

                Write code to print the keys in the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}.

                .. code-block:: python

                    colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
                    colors_keys = colors_dict.keys()
                    print(colors_keys)
                    # Output is dict_keys(['red', 'green', 'blue'])

            .. tab-item:: Q4

                Write code to print the keys in the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}.

                .. code-block:: python

                    animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}
                    animals_keys = animals_dict.keys()
                    print(animals_keys)
                    # Output is dict_keys(['cat', 'dog', 'bird'])

----

values()
~~~~~~~~~~~~~

.. py:method:: dict.values()

    Returns a view object that displays a list of all the values in the dictionary.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    values = sample_dict.values()
    print(values)
    # Output is dict_values([1, 2, 3])

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to print the values in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}.
    #. Write code to print the values in the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}.
    #. Write code to print the values in the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}.
    #. Write code to print the values in the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to print the values in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}.

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    coordinates_values = coordinates_dict.values()
                    print(coordinates_values)
                    # Output is dict_values([10, 20, 30])

            .. tab-item:: Q2

                Write code to print the values in the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}.

                .. code-block:: python

                    fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}
                    fruits_values = fruits_dict.values()
                    print(fruits_values)
                    # Output is dict_values(['green', 'yellow', 'red'])

            .. tab-item:: Q3

                Write code to print the values in the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}.

                .. code-block:: python

                    colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
                    colors_values = colors_dict.values()
                    print(colors_values)
                    # Output is dict_values(['#FF0000', '#00FF00', '#0000FF'])

            .. tab-item:: Q4

                Write code to print the values in the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}.

                .. code-block:: python

                    animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}
                    animals_values = animals_dict.values()
                    print(animals_values)
                    # Output is dict_values(['meow', 'woof', 'tweet'])

----

Modifying Items
---------------

update()
~~~~~~~~~~~~~

.. py:method:: dict.update([other])

    Updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs.

| The code below updates the dictionary with elements from another dictionary.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    new_dict = {'d': 4, 'e': 5}
    sample_dict.update(new_dict)
    print(sample_dict)
    # Output is {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

| The code below updates the dictionary with elements from list of tuples, where each tuple contains a key-value pair

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    new_items = [('d', 4), ('e', 5)]
    sample_dict.update(new_items)
    print(sample_dict)
    # Output is {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to update the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30} with a second dictionary {'a': 40, 'b': 50, 'c': 60}. Print the dictionary.
    #. Write code to update the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'} with a second dictionary {'date': 'brown', 'elderberry': 'purple'}. Print the dictionary.
    #. Write code to update the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'} with the list of tuples [('yellow', '#FFFF00'), ('purple', '#800080'), ('orange', '#FFA500')]. Print the dictionary.
    #. Write code to update the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'} with the list of tuples [('fish', 'blub'), ('hamster', 'squeak')]. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to update the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30} with a second dictionary {'a': 40, 'b': 50, 'c': 60}. Print the dictionary.

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    new_dict = {'a': 40, 'b': 50, 'c': 60}
                    coordinates_dict.update(new_dict)
                    print(coordinates_dict)
                    # Output is {'x': 10, 'y': 20, 'z': 30, 'a': 40, 'b': 50, 'c': 60}

            .. tab-item:: Q2

                Write code to update the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'} with a second dictionary {'date': 'brown', 'elderberry': 'purple'}. Print the dictionary.

                .. code-block:: python

                    fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}
                    new_dict = {'date': 'brown', 'elderberry': 'purple'}
                    fruits_dict.update(new_dict)
                    print(fruits_dict)
                    # Output is {'apple': 'green', 'banana': 'yellow', 'cherry': 'red', 'date': 'brown', 'elderberry': 'purple'}

            .. tab-item:: Q3

                Write code to update the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'} with the list of tuples [('yellow', '#FFFF00'), ('purple', '#800080'), ('orange', '#FFA500')]. Print the dictionary.

                .. code-block:: python

                    colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
                    new_items = [('yellow', '#FFFF00'), ('purple', '#800080'), ('orange', '#FFA500')]
                    colors_dict.update(new_items)
                    print(colors_dict)
                    # Output is {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'yellow': '#FFFF00', 'purple': '#800080', 'orange': '#FFA500'}

            .. tab-item:: Q4

                Write code to update the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'} with the list of tuples [('fish', 'blub'), ('hamster', 'squeak')]. Print the dictionary.

                .. code-block:: python

                    animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}
                    new_items = [('fish', 4), ('hamster', 5)]
                    animals_dict.update(new_items)
                    print(animals_dict)
                    # Output is {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet', 'fish': 'blub', 'hamster': 'squeak'}

----

setdefault()
~~~~~~~~~~~~~

.. py:method:: dict.setdefault(key, default=None)

    Returns the value of the specified key. If the key does not exist, inserts the key with the specified default value.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    value = sample_dict.setdefault('d', 4)
    print(value)
    # Output is 4
    print(sample_dict)
    # sample_dict is now {'a': 1, 'b': 2, 'c': 3, 'd': 4}

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to find the value of 'a' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30} setting it to a default value of 40 if it is not in the dictionary. Print value and print the dictionary.
    #. Write code to find the value of 'date' in the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'} setting it to a default value of 'brown' if it is not in the dictionary. Print value and print the dictionary.
    #. Write code to find the value of 'yellow', in the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'} setting it to a default value of '#FFFF00' if it is not in the dictionary. Print value and print the dictionary.
    #. Write code to find the value of 'fish' in the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'} setting it to a default value of 'blub' if it is not in the dictionary. Print value and print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to find the value of 'a' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30} setting it to a default value of 40 if it is not in the dictionary.  Print value and print the dictionary.

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    value = coordinates_dict.setdefault('a', 40)
                    print(value)
                    # Output is 40
                    print(coordinates_dict)
                    # coordinates_dict is now {'x': 10, 'y': 20, 'z': 30, 'a': 40}

            .. tab-item:: Q2

                Write code to find the value of 'date' in the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'} setting it to a default value of 'brown' if it is not in the dictionary. Print value and print the dictionary.

                .. code-block:: python

                    fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}
                    value = fruits_dict.setdefault('date', 'brown')
                    print(value)
                    # Output is 'brown'
                    print(fruits_dict)
                    # fruits_dict is now {'apple': 'green', 'banana': 'yellow', 'cherry': 'red', 'date': 'brown'}

            .. tab-item:: Q3

                Write code to find the value of 'yellow', in the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'} setting it to a default value of '#FFFF00' if it is not in the dictionary. Print value and print the dictionary.

                .. code-block:: python

                    colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
                    value = colors_dict.setdefault('yellow', '#FFFF00')
                    print(value)
                    # Output is '#FFFF00'
                    print(colors_dict)
                    # colors_dict is now {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'yellow': '#FFFF00'}

            .. tab-item:: Q4

                Write code to find the value of 'fish' in the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'} setting it to a default value of 'blub' if it is not in the dictionary. Print value and print the dictionary.

                .. code-block:: python

                    animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}
                    value = animals_dict.setdefault('fish', 'blub')
                    print(value)
                    # Output is 'blub'
                    print(animals_dict)
                    # animals_dict is now {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet', 'fish': 'blub'}

----

pop()
~~~~~~~~~~~~~

.. py:method:: dict.pop(key, default=None)

    Removes the specified key and returns the corresponding value. If the key is not found, the default value is returned if provided, otherwise a KeyError is raised.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    value = sample_dict.pop('a')
    print(value)
    # Output is 1
    print(sample_dict)
    # sample_dict is now {'b': 2, 'c': 3}

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Remove the value of 'x' (first position) from the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30, 'a': 40} and print its value and print the dictionary.
    #. Remove the value of 'banana' from the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red', 'date': 'brown'} and print its value and print the dictionary.
    #. Remove the value of 'blue' from the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'yellow': '#FFFF00'} and print its value and print the dictionary.
    #. Remove the value of 'hamster' from the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet', 'hamster': 'squeak'} and print its value and print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Remove the value of 'x' (first position) from the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30, 'a': 40} and print its value and print the dictionary.

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30, 'a': 40}
                    value = coordinates_dict.pop('x')
                    print(value)
                    # Output is 10
                    print(coordinates_dict)
                    # coordinates_dict is now {'y': 20, 'z': 30, 'a': 40}

            .. tab-item:: Q2

                Remove the value of 'banana' from the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red', 'date': 'brown'} and print its value and print the dictionary.

                .. code-block:: python

                    fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red', 'date': 'brown'}
                    value = fruits_dict.pop('banana')
                    print(value)
                    # Output is 'yellow'
                    print(fruits_dict)
                    # fruits_dict is now {'apple': 'green', 'cherry': 'red', 'date': 'brown'}

            .. tab-item:: Q3

                Remove the value of 'blue' from the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'yellow': '#FFFF00'} and print its value and print the dictionary.

                .. code-block:: python

                    colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'yellow': '#FFFF00'}
                    value = colors_dict.pop('blue')
                    print(value)
                    # Output is '#0000FF'
                    print(colors_dict)
                    # colors_dict is now {'red': '#FF0000', 'green': '#00FF00', 'yellow': '#FFFF00'}

            .. tab-item:: Q4

                Remove the value of 'hamster' from the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet', 'hamster': 'squeak'} and print its value and print the dictionary.

                .. code-block:: python

                    animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet', 'hamster': 'squeak'}
                    value = animals_dict.pop('hamster')
                    print(value)
                    # Output is 'squeak'
                    print(animals_dict)
                    # animals_dict is now {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}


----

popitem()
~~~~~~~~~~~~~

.. py:method:: dict.popitem()

    Removes and returns a key-value pair from the dictionary. Pairs are returned in LIFO (last-in, first-out) order.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    item = sample_dict.popitem()
    print(item)
    # Output is ('c', 3)
    print(animals_dict)
    # sample_dict is now {'a': 1, 'b': 2}

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Remove the last item from the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30} and print it and print the dictionary.
    #. Remove the last item from the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'} and print it and print the dictionary.
    #. Remove the last item from the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'} and print it and print the dictionary.
    #. Remove the last item from the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'} and print it and print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Remove the last item from the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30} and print it and print the dictionary.

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    item = coordinates_dict.popitem()
                    print(item)
                    # Output is ('z', 30)
                    print(coordinates_dict)
                    # coordinates_dict is now {'x': 10, 'y': 20}

            .. tab-item:: Q2

                Remove the last item from the dictionary fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'} and print it and print the dictionary.

                .. code-block:: python

                    fruits_dict = {'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}
                    item = fruits_dict.popitem()
                    print(item)
                    # Output is ('cherry', 'red')
                    print(fruits_dict)
                    # fruits_dict is now {'apple': 'green', 'banana': 'yellow'}

            .. tab-item:: Q3

                Remove the last item from the dictionary colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'} and print it and print the dictionary.

                .. code-block:: python

                    colors_dict = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
                    item = colors_dict.popitem()
                    print(item)
                    # Output is ('blue', '#0000FF')
                    print(colors_dict)
                    # colors_dict is now {'red': '#FF0000', 'green': '#00FF00'}

            .. tab-item:: Q4

                Remove the last item from the dictionary animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'} and print it and print the dictionary.

                .. code-block:: python

                    animals_dict = {'cat': 'meow', 'dog': 'woof', 'bird': 'tweet'}
                    item = animals_dict.popitem()
                    print(item)
                    # Output is ('bird', 'tweet')
                    print(animals_dict)
                    # animals_dict is now {'cat': 'meow', 'dog': 'woof'}

----

Dictionary Operations
---------------------

copy()
~~~~~~~~~~~~~

| The copy method is fine to use when the values in the dictionary are immutable. i.e. strings, integers, floats, tuples.

.. py:method:: dict.copy()

    | Returns a shallow copy of the dictionary.
    | Mutable objects (lists, dictionaries) will change in the original dictionary if altered in the new dictionary.

.. code-block:: python

    # Original dictionary with various types of values
    original_dict = {
        'a': 'string',          # String
        'b': 42,                # Integer
        'c': (1, 2, 3),         # Tuple
        'd': [4, 5, 6],         # List
        'e': {'key': 'value'}   # Dictionary
    }

    # Create a shallow copy
    shallow_copy = original_dict.copy()

    # the mutable objects will not change in the original
    shallow_copy['a'] = 'new_string'
    shallow_copy['b'] = 100
    shallow_copy['c'] = (7, 8, 9)
    # the mutable objects will change in the original
    shallow_copy['d'].append(7)
    shallow_copy['e']['key'] = 'new_value'

    print("Original Dictionary:", original_dict)
    # Output is Original Dictionary: {'a': 'string', 'b': 42, 'c': (1, 2, 3), 'd': [4, 5, 6, 7], 'e': {'key': 'new_value'}}
    print("Shallow Copy:", shallow_copy)
    # Output is Shallow Copy:  {'a': 'new_string', 'b': 100, 'c': (7, 8, 9), 'd': [4, 5, 6, 7], 'e': {'key': 'new_value'}}


copy.deepcopy()
~~~~~~~~~~~~~

| Deepcopy is part of the copy module.
| The deepcopy function is best to use when the values in the dictionary are mutable, i.e. lists, dictionaries, and an independent copy is wanted.

.. py:method:: copy.deepcopy(dict)

    | Returns a deep copy of the dictionary.
    | All objects are independent of those in the original dictionary
    | Changing any key: value will not result in changes in the original dictionary.

.. code-block:: python

    import copy

    # Original dictionary with various types of values
    original_dict = {
        'a': 'string',          # String
        'b': 42,                # Integer
        'c': (1, 2, 3),         # Tuple
        'd': [4, 5, 6],         # List
        'e': {'key': 'value'}   # Dictionary
    }

    # Create a deep copy
    deep_copy = copy.deepcopy(original_dict)

    # Modify the values in the deep copy
    deep_copy['a'] = 'new_string'
    deep_copy['b'] = 100
    deep_copy['c'] = (7, 8, 9)
    deep_copy['d'].append(7)
    deep_copy['e']['key'] = 'new_value'

    print("Original Dictionary:", original_dict)
    # Output is Original Dictionary: {'a': 'string', 'b': 42, 'c': (1, 2, 3), 'd': [4, 5, 6], 'e': {'key': 'value'}}
    print("Deep Copy:", deep_copy)
    # Output is Deep Copy: {'a': 'new_string', 'b': 100, 'c': (7, 8, 9), 'd': [4, 5, 6, 7], 'e': {'key': 'new_value'}}

----

clear()
~~~~~~~~~~~~~

.. py:method:: dict.clear()

    Removes all items from the dictionary.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    sample_dict.clear()
    print(sample_dict)
    # Output is {}

----

fromkeys()
~~~~~~~~~~~~~

.. py:method:: dict.fromkeys(iterable, value=None)

    Creates a new dictionary with keys from the given iterable and values set to the specified value.

.. code-block:: python

    keys = ('a', 'b', 'c')
    value = 0
    new_dict = dict.fromkeys(keys, value)
    print(new_dict)
    # Output is {'a': 0, 'b': 0, 'c': 0}

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Create a dictionary named coordinates_dict with the keys 'x', 'y', and 'z', each having the default value 0. Use the dict.fromkeys() method to achieve this and print the resulting dictionary.
    #. Create a dictionary named fruits_dict with the keys 'apple', 'banana', and 'cherry', each having the default value 'unknown'. Use the dict.fromkeys() method to achieve this and print the resulting dictionary.
    #. Create a dictionary named colors_dict with the keys 'red', 'green', and 'blue', each having the default value '#FFFFFF'. Use the dict.fromkeys() method to achieve this and print the resulting dictionary.
    #. Create a dictionary named animals_dict with the keys 'cat', 'dog', and 'bird', each having the default value 'sound'. Use the dict.fromkeys() method to achieve this and print the resulting dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary named coordinates_dict with the keys 'x', 'y', and 'z', each having the default value 0. Use the dict.fromkeys() method to achieve this and print the resulting dictionary.

                .. code-block:: python

                    keys = ('x', 'y', 'z')
                    value = 0
                    coordinates_dict = dict.fromkeys(keys, value)
                    print(coordinates_dict)
                    # Output is {'x': 0, 'y': 0, 'z': 0}

            .. tab-item:: Q2

                Create a dictionary named fruits_dict with the keys 'apple', 'banana', and 'cherry', each having the default value 'unknown'. Use the dict.fromkeys() method to achieve this and print the resulting dictionary.

                .. code-block:: python

                    keys = ('apple', 'banana', 'cherry')
                    value = 'white'
                    fruits_dict = dict.fromkeys(keys, value)
                    print(fruits_dict)
                    # Output is {'apple': 'white', 'banana': 'white', 'cherry': 'white'}

            .. tab-item:: Q3

                Create a dictionary named colors_dict with the keys 'red', 'green', and 'blue', each having the default value '#FFFFFF'. Use the dict.fromkeys() method to achieve this and print the resulting dictionary.

                .. code-block:: python

                    keys = ('red', 'green', 'blue')
                    value = '#FFFFFF'
                    colors_dict = dict.fromkeys(keys, value)
                    print(colors_dict)
                    # Output is {'red': '#FFFFFF', 'green': '#FFFFFF', 'blue': '#FFFFFF'}

            .. tab-item:: Q4

                Create a dictionary named animals_dict with the keys 'cat', 'dog', and 'bird', each having the default value 'sound'. Use the dict.fromkeys() method to achieve this and print the resulting dictionary.

                .. code-block:: python

                    keys = ('cat', 'dog', 'bird')
                    value = 'sound'
                    animals_dict = dict.fromkeys(keys, value)
                    print(animals_dict)
                    # Output is {'cat': 'sound', 'dog': 'sound', 'bird': 'sound'}




