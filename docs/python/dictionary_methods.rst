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
    # Output is 1

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?
    #. Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?
    #. Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?
    #. Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    value = coordinates_dict.get('y')
                    # Output is 20

            .. tab-item:: Q2

                Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?

                .. code-block:: python

                    fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}
                    value = fruits_dict.get('banana')
                    # Output is 10

            .. tab-item:: Q3

                Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?

                .. code-block:: python

                    colors_dict = {'red': 100, 'green': 200, 'blue': 300}
                    value = colors_dict.get('blue')
                    # Output is 300

            .. tab-item:: Q4

                Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

                .. code-block:: python

                    animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}
                    value = animals_dict.get('dog')
                    # Output is 2

----

items()
~~~~~~~~~~~~~

.. py:method:: dict.items()

    Returns a view object that displays a list of dictionary's key-value tuple pairs.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    items = sample_dict.items()
    # Output is dict_items([('a', 1), ('b', 2), ('c', 3)])

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?
    #. Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?
    #. Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?
    #. Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    value = coordinates_dict.get('y')
                    # Output is 20

            .. tab-item:: Q2

                Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?

                .. code-block:: python

                    fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}
                    value = fruits_dict.get('banana')
                    # Output is 10

            .. tab-item:: Q3

                Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?

                .. code-block:: python

                    colors_dict = {'red': 100, 'green': 200, 'blue': 300}
                    value = colors_dict.get('blue')
                    # Output is 300

            .. tab-item:: Q4

                Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

                .. code-block:: python

                    animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}
                    value = animals_dict.get('dog')
                    # Output is 2

----

keys()
~~~~~~~~~~~~~

.. py:method:: dict.keys()

    Returns a view object that displays a list of all the keys in the dictionary.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    keys = sample_dict.keys()
    # Output is dict_keys(['a', 'b', 'c'])

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?
    #. Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?
    #. Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?
    #. Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    value = coordinates_dict.get('y')
                    # Output is 20

            .. tab-item:: Q2

                Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?

                .. code-block:: python

                    fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}
                    value = fruits_dict.get('banana')
                    # Output is 10

            .. tab-item:: Q3

                Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?

                .. code-block:: python

                    colors_dict = {'red': 100, 'green': 200, 'blue': 300}
                    value = colors_dict.get('blue')
                    # Output is 300

            .. tab-item:: Q4

                Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

                .. code-block:: python

                    animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}
                    value = animals_dict.get('dog')
                    # Output is 2

----

values()
~~~~~~~~~~~~~

.. py:method:: dict.values()

    Returns a view object that displays a list of all the values in the dictionary.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    values = sample_dict.values()
    # Output is dict_values([1, 2, 3])

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?
    #. Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?
    #. Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?
    #. Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    value = coordinates_dict.get('y')
                    # Output is 20

            .. tab-item:: Q2

                Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?

                .. code-block:: python

                    fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}
                    value = fruits_dict.get('banana')
                    # Output is 10

            .. tab-item:: Q3

                Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?

                .. code-block:: python

                    colors_dict = {'red': 100, 'green': 200, 'blue': 300}
                    value = colors_dict.get('blue')
                    # Output is 300

            .. tab-item:: Q4

                Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

                .. code-block:: python

                    animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}
                    value = animals_dict.get('dog')
                    # Output is 2

----

Modifying Items
---------------

update()
~~~~~~~~~~~~~

.. py:method:: dict.update([other])

    Updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    sample_dict.update({'d': 4, 'e': 5})
    # Output is {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?
    #. Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?
    #. Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?
    #. Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    value = coordinates_dict.get('y')
                    # Output is 20

            .. tab-item:: Q2

                Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?

                .. code-block:: python

                    fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}
                    value = fruits_dict.get('banana')
                    # Output is 10

            .. tab-item:: Q3

                Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?

                .. code-block:: python

                    colors_dict = {'red': 100, 'green': 200, 'blue': 300}
                    value = colors_dict.get('blue')
                    # Output is 300

            .. tab-item:: Q4

                Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

                .. code-block:: python

                    animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}
                    value = animals_dict.get('dog')
                    # Output is 2

----

setdefault()
~~~~~~~~~~~~~

.. py:method:: dict.setdefault(key, default=None)

    Returns the value of the specified key. If the key does not exist, inserts the key with the specified default value.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    value = sample_dict.setdefault('d', 4)
    # Output is 4
    # sample_dict is now {'a': 1, 'b': 2, 'c': 3, 'd': 4}

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?
    #. Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?
    #. Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?
    #. Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    value = coordinates_dict.get('y')
                    # Output is 20

            .. tab-item:: Q2

                Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?

                .. code-block:: python

                    fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}
                    value = fruits_dict.get('banana')
                    # Output is 10

            .. tab-item:: Q3

                Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?

                .. code-block:: python

                    colors_dict = {'red': 100, 'green': 200, 'blue': 300}
                    value = colors_dict.get('blue')
                    # Output is 300

            .. tab-item:: Q4

                Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

                .. code-block:: python

                    animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}
                    value = animals_dict.get('dog')
                    # Output is 2

----

pop()
~~~~~~~~~~~~~

.. py:method:: dict.pop(key, default=None)

    Removes the specified key and returns the corresponding value. If the key is not found, the default value is returned if provided, otherwise a KeyError is raised.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    value = sample_dict.pop('a')
    # Output is 1
    # sample_dict is now {'b': 2, 'c': 3}

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?
    #. Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?
    #. Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?
    #. Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    value = coordinates_dict.get('y')
                    # Output is 20

            .. tab-item:: Q2

                Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?

                .. code-block:: python

                    fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}
                    value = fruits_dict.get('banana')
                    # Output is 10

            .. tab-item:: Q3

                Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?

                .. code-block:: python

                    colors_dict = {'red': 100, 'green': 200, 'blue': 300}
                    value = colors_dict.get('blue')
                    # Output is 300

            .. tab-item:: Q4

                Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

                .. code-block:: python

                    animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}
                    value = animals_dict.get('dog')
                    # Output is 2

----

popitem()
~~~~~~~~~~~~~

.. py:method:: dict.popitem()

    Removes and returns a key-value pair from the dictionary. Pairs are returned in LIFO (last-in, first-out) order.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    item = sample_dict.popitem()
    # Output is ('c', 3)
    # sample_dict is now {'a': 1, 'b': 2}

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?
    #. Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?
    #. Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?
    #. Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    value = coordinates_dict.get('y')
                    # Output is 20

            .. tab-item:: Q2

                Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?

                .. code-block:: python

                    fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}
                    value = fruits_dict.get('banana')
                    # Output is 10

            .. tab-item:: Q3

                Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?

                .. code-block:: python

                    colors_dict = {'red': 100, 'green': 200, 'blue': 300}
                    value = colors_dict.get('blue')
                    # Output is 300

            .. tab-item:: Q4

                Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

                .. code-block:: python

                    animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}
                    value = animals_dict.get('dog')
                    # Output is 2

----

Dictionary Operations
---------------------

copy()
~~~~~~~~~~~~~

.. py:method:: dict.copy()

    Returns a shallow copy of the dictionary.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    new_dict = sample_dict.copy()
    # Output is {'a': 1, 'b': 2, 'c': 3}

----

clear()
~~~~~~~~~~~~~

.. py:method:: dict.clear()

    Removes all items from the dictionary.

.. code-block:: python

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    sample_dict.clear()
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
    # Output is {'a': 0, 'b': 0, 'c': 0}

----

Practice Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Tasks

    #. Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?
    #. Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?
    #. Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?
    #. Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to find the value of 'y' in the dictionary coordinates_dict = {'x': 10, 'y': 20, 'z': 30}?

                .. code-block:: python

                    coordinates_dict = {'x': 10, 'y': 20, 'z': 30}
                    value = coordinates_dict.get('y')
                    # Output is 20

            .. tab-item:: Q2

                Write code to find the value of 'banana' in the dictionary fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}?

                .. code-block:: python

                    fruits_dict = {'apple': 5, 'banana': 10, 'cherry': 15}
                    value = fruits_dict.get('banana')
                    # Output is 10

            .. tab-item:: Q3

                Write code to find the value of 'blue' in the dictionary colors_dict = {'red': 100, 'green': 200, 'blue': 300}?

                .. code-block:: python

                    colors_dict = {'red': 100, 'green': 200, 'blue': 300}
                    value = colors_dict.get('blue')
                    # Output is 300

            .. tab-item:: Q4

                Write code to find the value of 'dog' in the dictionary animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}?

                .. code-block:: python

                    animals_dict = {'cat': 1, 'dog': 2, 'bird': 3}
                    value = animals_dict.get('dog')
                    # Output is 2


