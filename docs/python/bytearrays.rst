==========================
bytearrays
==========================

| `bytearray` objects in Python come with a variety of methods that allow you to manipulate and interact with the byte data. Here are some of the most commonly used methods:
| These methods provide a lot of flexibility for working with bytearrays, allowing you to manipulate the data in various ways.

### Common Methods for `bytearray`


bytearray Methods
=================

The `bytearray` type in Python provides a variety of methods for manipulating and interacting with byte data. Below are some commonly used methods:

----

append
----------------

.. py:method:: append(x)

    Append a single byte to the end of the bytearray.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67])
        my_ba.append(68)
        print(my_ba)
        # Output is bytearray(b'ABCD')

----

append
----------------

.. py:method:: extend(iterable)

    Extend the bytearray by appending elements from the iterable.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67])
        my_ba.extend([68, 69])
        print(my_ba)
        # Output is bytearray(b'ABCDE')

----

append
----------------

.. py:method:: insert(i, x)

    Insert a single byte at a given position.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67])
        my_ba.insert(1, 68)
        print(my_ba)
        # Output is bytearray(b'ADBC')

----

append
----------------

.. py:method:: remove(x)

    Remove the first occurrence of a byte.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67, 66])
        my_ba.remove(66)
        print(my_ba)
        # Output is bytearray(b'ACB')

----

append
----------------

.. py:method:: pop([i])

    Remove and return a byte at a given position. If no index is specified, removes and returns the last byte.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67])
        byte = my_ba.pop(1)
        print(byte)
        # Output is 66
        print(my_ba)
        # Output is bytearray(b'AC')

----

append
----------------

.. py:method:: clear()

    Remove all bytes from the bytearray.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67])
        my_ba.clear()
        print(my_ba)
        # Output is bytearray(b'')

----

append
----------------

.. py:method:: count(x)

    Return the number of occurrences of a byte.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67, 66])
        count = my_ba.count(66)
        print(count)
        # Output is 2

----

append
----------------

.. py:method:: find(sub[, start[, end]])

    Return the lowest index where the subsequence is found.

    Example:

    .. code-block:: python

        my_ba = bytearray(b'Hello, World!')
        index = my_ba.find(b'World')
        print(index)
        # Output is 7

----

append
----------------

.. py:method:: reverse()

    Reverse the bytes in place.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67])
        my_ba.reverse()
        print(my_ba)
        # Output is bytearray(b'CBA')

----

append
----------------

.. py:method:: decode(encoding='utf-8', errors='strict')

    Decode the bytearray to a string using the specified encoding.

    Example:

    .. code-block:: python

        my_ba = bytearray(b'Hello, World!')
        string = my_ba.decode('utf-8')
        print(string)
        # Output is Hello, World!

